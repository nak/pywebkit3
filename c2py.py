#!/usr/bin/python
from gi.repository import Gtk as gtk

from ctypes import c_void_p
from twisted.test.test_sslverify import Constructors
ptr_types = {}
methods = {}
enum_types=[]
constructors=[]
prefix = ""

DEFAULT_TYPES=['gboolean','gint', 'guint']
DEFAULT_TYPE_MAPPING={'gboolean': 'c_int',
                      'gint' : 'c_int',
                      'guint' : 'c_uint'}

def parse_params( methodname, returntype, api, position):
    print "PARSING %d %s"%(position, api)
    global classname
    tokens = api.split()
    print "TOKENS %s"%tokens
    if tokens[0] == 'void':
        assert(position == 0)
        constructors.append( [methodname] )
        return 
    elif tokens[0] in DEFAULT_TYPES:
        typename=tokens[0]
        paramname = tokens[1]
    elif tokens[0] != classname and position==0:
        constructors.append([methodname])
        return 
    elif tokens[0] == classname and position == 0:
        methods[methodname] = [returntype]
        return
    else:
        if tokens[1]!='*':
            print "UNABLE TO PARSE %s"%api
        assert(tokens[1]=='*')
        typename = tokens[0]
        paramname = tokens[2]
        ptr_types[typename] = 'c_void_p'
    if position == 0:
            print "UNABLE TO PARSE %s"%api
    assert(position > 0)
    if position > 0 and methods.has_key(methodname):
        methods[methodname].append((paramname, typename))
    elif position > 0:
        constructors[-1].append( (paramname, typename) )
    return 

def to_python( api ):
    tokens = api.replace('const','').replace('*','* ').replace(';','').replace('(','|').replace(')','|').replace('  ',' ').split('|')
    declaration = tokens[0].split()
    if declaration[0] == 'enum':
        enum_types.append(declaration[1])
    else:
        returntype = declaration[0]
        if declaration[0] == 'void' and declaration[1] != '*':
            methodname = declaration[1]
            methods[methodname] = [None]
            return
        elif(declaration[1] == '*'):
            ptr_types[declaration[0]] = 'c_void_p'
            methodname = declaration[2]
        elif declaration[0] in DEFAULT_TYPES:
            methodname = declaration[1]
        else:
            print("ERROR: parsing line %s",api)
            return
        methods[methodname] = [declaration[0]]
        params = tokens[1].split(',')
        index = 0
        for paramline in params:
            parse_params(methodname, returntype, paramline, index)
            index += 1
 
def emit_python():
    global constructors
 
    def gen_params_constructor(index, callable = False):
        text = ""
        for param in constructors[index][1:]:
            if callable:
                if param[0] in DEFAULT_TYPES:
                    text += "%s, "%param[0]
                else:
                    text += "%s._object, "%param[0]
            else:
                text += " %s,"%param[0] 
        return text
    
    def gen_params(methodname, callable= False):
        text = ""
        for param in methods[methodname][1:]:
            if callable:
                if param[0] in DEFAULT_TYPES:
                    text += "%s, "%param[0]
                else:
                    text += "%s._object"%param[0]
            else:
                text += " %s,"%param[0]
        return text
    with open('webkit_%s.py'%classname,'w') as f:
        f.write("""from ctypes import *
from gi.repository import Gtk as gtk

cdll.LoadLibrary("libwebkitgtk-3.0.so")
libwebkit = CDLL("libwebkitgtk-3.0.so")

""")
            
        f.write( '"""default gtk types"""\n')
        for t,val in DEFAULT_TYPE_MAPPING.iteritems():
            f.write( "%s = %s\n"%(t,val))
            
        f.write("\n")
        f.write('"""Derived Pointer Types"""\n')
        for t,val in ptr_types.iteritems():
            f.write(("%s = %s\n"%(t, val)))
            
        f.write("")
        f.write('"""Enumerations"""\n')
        for t in enum_types:
            f.write("%s = c_int\n"%t)
            
        f.write("\n")
        f.write('class %s( gtk.Window ):\n'%classname)
        f.write('    """Class %s Constructors"""\n'%classname)
        index = 0
        for c in constructors:
            c_name = c[0]
            f.write( "    def __init__( self, %s):\n"%gen_params_constructor(index))
            f.write( "        gtk.Window.__init__(self)\n")
            f.write( "        self.show_all()")
            f.write( "        libwebkit.%s.restype = c_void_p\n"%(c_name ))
            if len(c)>1:
                f.write( "        libwebkit.%s.argtypes = [%s]\n"%(c_name, ','.join([p[1] for p in c[1:]])))
            f.write("        self._object = libwebkit.%s(%s)\n"%(c_name, gen_params_constructor(index, callable=True)))
            index += 1
            
        f.write("\n")
        f.write('    """Methods"""\n')
        for methodname in methods.iterkeys():
            f.write("    def %s(self, %s):\n"%(methodname.replace(prefix,''), gen_params(methodname)))
            if methods[methodname][0]:
                f.write( "        libwebkit.%s.restype = %s\n"%(methodname,methods[methodname][0]))
            if len(methods[methodname])>1:
                f.write("        libwebkit.%s.argtypes = [%s]\n"%(methodname,','.join([p[1] for p in methods[methodname][1:]])))
            if methods[methodname][0]:
                ret = "return "
            else:
                ret=""
            f.write("        %slibwebkit.%s(%s)\n"%(ret, methodname, gen_params(methodname, callable=True))) 
            f.write("\n")
    
import sys, re
with open (sys.argv[1],'r') as f:
    line = ""
    global classname 
    classname = sys.argv[2]
    prefix = "_".join(l.lower() for l in re.findall('[A-Z][^A-Z]*', classname.replace('WebKit','Webkit')))
    prefix += '_'
    while line != None:
        text = f.readline()
        if text=="":
            break
        line += text
        if line.find(';')>=0:
            print "LINE:'%s'  %s"% (line, line.find(';'))
            to_python(line)
            line="" 
            
    emit_python()


           
classname = None
