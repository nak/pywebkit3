#!/usr/bin/python

import os.path
from ctypes import *
from twisted.test.test_sslverify import Constructors
import logging

ptr_types = {}
methods = {}
staticmethods={}
enum_types=[]
constructors={}
prefix = ""
classname=None

LIB_NAME='libwebkit'

DEFAULT_TYPES=['gboolean',
                      'gint',
                      'guint' ,
                      'gpointer' ,
                      'gconstpointer',
                      'gchar',
                      'guchar',
                      'gshort',
                      'gushort',
                      'glong',
                      'gulong',
                      'gint8',
                      'guint8',
                      'gint16',
                      'guint16',
                      'gint32',
                      'guint32',
                      'gfloat',
                      'gdouble',
                      'gsize',
                      'GdkGravity',
                      'GQuark',
                      'GtkIconSize',
                      'GDestroyNotify',
                      'GDuplicateFunc',
                      'GtkWindowType'
                    ]

inheritances={'WebKitWebView': 'gtk.GtkContainer',
              'GtkContainer' : 'gtk.GtkWidget',
              'GtkWidget': 'gobject.GObject',
              'GtkWindow': 'gtk.GtkBin',
              'GtkBin': 'gtk.GtkContainer',
              'GObject': 'object'
              }

def parse_params( methodname, returntype, api, position):
    #print "PARSING %d %s"%(position, api)
    global classname
    global DEFAULT_TYPES
    tokens = api.split()
    #print "TOKENS %s"%tokens
    if tokens[0] == 'void' and methodname.endswith('new') and position==0:
        assert(position == 0)
        constructors[methodname]=[]
        return 
    elif tokens[0] != classname and methodname.endswith('new'):
        if position == 0:
            constructors[methodname] = []
        if len(tokens) >=3:
            typename = tokens[0]
            if typename in DEFAULT_TYPES:
                if typename == "gchar":
                    paramname = 'c_char_p'
                else:
                    paramname = "POINTER(%s)"%tokens[2]
            else:
                paramname = '_%s'%tokens[2]
                
        elif len(tokens) > 1:
            typename = tokens[0]
            paramname = tokens[1]
        else:
            logging.error("Unable to parse %s"%api)
            return
        constructors[methodname].append((paramname, typename))
        return
    elif tokens[0] in DEFAULT_TYPES and tokens[1] !='*':
        typename=tokens[0]
        paramname = tokens[1]
    elif tokens[0] == classname and position == 0:
        methods[methodname] = [returntype]
        return
    else:
        if len(tokens) < 2 or tokens[1]!='*':
            logging.error("UNABLE TO PARSE %s: %s"%(api,tokens))
            return
        if len(tokens)!=3:
            typename = tokens[0]
            paramname = tokens[1]
        else:
            assert(tokens[1]=='*')
            typename = tokens[0]
            if not typename in DEFAULT_TYPES:
                ptr_types[typename] = 'c_void_p'
                typename = "_%s"%typename
            else:
                if typename =='gchar':
                    typename = 'c_char_p'
                else:
                    typename = "POINTER(%s)"%typename
            paramname = tokens[2]
    if(paramname =='*'):
        logging.error("UNABLE TO PARSE %s: %s"%(api,tokens))
    assert(paramname !='*')
    if position == 0:
        if not staticmethods.has_key(methodname) and not constructors.has_key(methodname):
            staticmethods[methodname] = [returntype]
            staticmethods[methodname].append((paramname, typename))
    elif constructors.has_key(methodname):
        constructors[methodname].append((paramname,typename))
    elif methods.has_key(methodname):
        methods[methodname].append((paramname, typename))
    else:
        if not staticmethods.has_key(methodname) and not constructors.has_key(methodname):
            staticmethods[methodname] = [returntype]
            staticmethods[methodname].append((paramname, typename))
         
    return 

def to_python( api ):
    global classname
    if api.find('va_list') >=0:
        logging.error("Unable to parse variable arguments for %s"%api)
        return
    tokens = api.replace('const','').replace('**','*').replace('*','* ').replace(';','').replace('(','|').replace(')','|').replace('  ',' ').split('|')
    declaration = tokens[0].split()
    if declaration[0] == 'enum':
        enum_types.append(declaration[1])
    elif api[0] == '#':
        return
    elif len(declaration)==1:
        if not classname:
            classname = declaration[0]
    elif declaration[0] == 'struct':
        if not classname:
            classname = declaration[1]
    else:
        #function declration
        if declaration[0] == 'void' and declaration[1] != '*':
            methodname = declaration[1]
            methods[methodname] = [None]
            return
        elif len(declaration) == 2:
            methodname = declaration[1]
            #methods[methodname] = [declaration[0]]
            returntype = declaration[0]
        elif(declaration[1] == '*'):
            ptr_types[declaration[0]] = 'c_void_p'
            methodname = declaration[2]
            #methods[methodname] = ['_%s'%declaration[0]]
            returntype = ['_%s'%declaration[0]]
        elif declaration[0] in DEFAULT_TYPES and declaration[1] == '*':
            methodname = declaration[2]
            if declaration[0] != 'gchar':
                returntype = ['POINTER(%s)'%declaration[0]]
            else:
                returntype = ['c_char_p']
            #returntype = methods[methodname][0]
        else:
            logging.error("ERROR: parsing line %s",api)
            return
        if len(tokens)>1:
            params = tokens[1].split(',')
            index = 0
            for paramline in params:
                parse_params(methodname, returntype, paramline, index)
                index += 1
            if staticmethods.has_key(methodname) and methods.has_key(methodname):
                del methods[methodname]
 
def emit_python(namespace):
    global constructors
 
    def gen_params_constructor(index):
        text = ""
        callable_text = ""
        assertions = []
        for cmethod,params in constructors.iteritems():
            for param in params:
             
                if (param[1] in DEFAULT_TYPES) or (param[1] == 'c_char_p'):
                    callable_text += "%s, "%param[0]
                else:
                        callable_text += "%s._object, "%(param[0])
                
                text += "%s, "%param[0]
                assertions.append("assert(isinstance(%s, %s))"%(param[0], param[1]))
        return (text, callable_text, assertions)
    
    def gen_params(methodname, callable= False):
        text = ""
        if methods.has_key(methodname):
            m = methods
            is_static = False
        else:
            m = staticmethods
            is_static = True
        for param in m[methodname][1:]:
            if callable:
                if param[1] in DEFAULT_TYPES or param[1] == 'c_char_p':
                    text += "%s, "%param[0]
                else:
                    text += "%s._object, "%param[0]
            else:
                text += " %s,"%param[0]
        return text
    global classname
    with open(os.path.join('src','_%s_%s.py'%(namespace,classname)),'w') as f:
        prefix = "_".join(l.lower() for l in re.findall('[A-Z][^A-Z]*', classname.replace('WebKit','Webkit')))
        prefix += '_' 
        f.write("""from ctypes import *
#from gi.repository import Gtk as gtk
from gtk_types import *


""")
            
        f.write("\n")
        f.write('"""Derived Pointer Types"""\n')
        for t,val in ptr_types.iteritems():
            f.write(("_%s = %s\n"%(t, val)))
            
        f.write("")
        f.write('"""Enumerations"""\n')
        for t in enum_types:
            f.write("%s = c_int\n"%t)
            
        f.write("\n")
        parentpackage = '_%s'%inheritances[classname].replace('.','_')
        parentclass = inheritances[classname].split('.')[-1]
        if inheritances[classname] != 'object':
            f.write('import %s\n'%parentpackage)
            f.write('class %s( %s.%s):\n'%(classname, parentpackage, parentclass))
        else:
            f.write('class %s( object):\n'%(classname))
        f.write('    """Class %s Constructors"""\n'%classname)
        index = 0
        for c_name, param in constructors.iteritems():
            (text, callable_text, assertions) = gen_params_constructor(index)
            f.write( "    def __init__( self, %s):\n"%text)
            for assertion in assertions:
                f.write("        %s\n"%assertion)
            f.write( "        %s.%s.restype = c_void_p\n"%(LIB_NAME,c_name ))
            if len(param)>0:
                f.write( "        %s.%s.argtypes = [%s]\n"%( LIB_NAME,c_name, ','.join([p[1] for p in param])))
            f.write("        self._object = %s.%s(%s)\n"%(LIB_NAME, c_name, callable_text))
            index += 1
            
        f.write("\n")
        f.write('    """Methods"""\n')
        for methodname in methods.iterkeys():
            f.write("    def %s(self, %s):\n"%(methodname.replace(prefix,''), gen_params(methodname)))
            if methods[methodname][0]:
                f.write( "        %s.%s.restype = %s\n"%(LIB_NAME,methodname,methods[methodname][0]))
            if len(methods[methodname])>1:
                f.write("        %s.%s.argtypes = [%s]\n"%(LIB_NAME,methodname,','.join([p[1] for p in methods[methodname][1:]])))
            if methods[methodname][0]:
                ret = "return "
            else:
                ret=""
            f.write("        %s%s.%s(self._object, %s)\n"%(ret, LIB_NAME,methodname, gen_params(methodname, callable=True))) 
            f.write("\n")
        for methodname in staticmethods.iterkeys():
            f.write("    @staticmethod\n")
            f.write("    def %s(%s):\n"%(methodname.replace(prefix,''), gen_params(methodname)))
            if staticmethods[methodname][0]:
                f.write( "        %s.%s.restype = %s\n"%(LIB_NAME,methodname, staticmethods[methodname][0]))
            if len(staticmethods[methodname])>1:
                f.write("        %s.%s.argtypes = [%s]\n"%(LIB_NAME,methodname,','.join([p[1] for p in staticmethods[methodname][1:]])))
            if staticmethods[methodname][0]:
                ret = "return "
            else:
                ret=""
            f.write("        %s%s.%s(%s)\n"%(ret, LIB_NAME,methodname, gen_params(methodname, callable=True))) 
            f.write("\n")
    
import sys, re
with open (sys.argv[1],'r') as f:
    line = ""
    global classname 
    while line != None:
        text = f.readline()
        if text=="":
            break
        line += text
        if line.find(';')>=0:
            #print "LINE:'%s'  %s"% (line, line.find(';'))
            to_python(line.replace('const',''))
            line="" 
    namespace = sys.argv[1][1:].split('_')[0]
    emit_python(namespace)


    
classname = None