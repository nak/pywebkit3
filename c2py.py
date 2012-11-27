#!/usr/bin/python
# Copyright, John Rusnak, 2012
# This code is available under the license agreement of the LGPL,
# with the additional constraint that any derivatives of this work aimed
# at providing bindings to GObject, GTK, GDK, or WebKit be strictly
# python-only bindings with no native code.
import os.path, sys, re

from ctypes import *
import logging


KEY_WORDS=['print','raise']

DEFAULT_TYPES=['gboolean',
               'bool',
               'int',
               'long',
               'short'
               'float',
               'double',
               'gint',
               'gint32',
               'gint64',
               'guint32',
               'guint64',
               'guint' ,
               'gpointer' ,
               'gconstpointer',
               'char',
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
               'GdkWindowState',
               'GdkGrabStatus',
               'GdkEvent',
               'GQuark',
               'GtkIconSize',
               'GDestroyNotify',
               'GDuplicateFunc',
               'GSourceFunc',
               'GtkWindowType',
               'GdkModifierType',
               'GdkEventMask',
               'GtkDirectionType',
               'GtkOrientation',
               'GtkResizeType',
               'GtkRequestedSize',
               'GtkJunctionSides',
               'GtkStateFlags',
               'GtkResizeMode',
               'GtkTextDirection',
               'GtkPolicyType',
               'GtkPrintOperationResult',
               
               'GtkClipboardReceivedFunc',
               'GtkClipboardTextReceivedFunc',
               'GtkClipboardImageReceivedFunc',
               'GtkClipboardURIReceivedFunc',
               'GtkClipboardTargetsReceivedFunc',
               'GtkClipboardRichTextReceivedFunc',
               'GtkClipboardGetFunc',
               'GtkClipboardClearFunc',
               
               'GType',
               'GPollFunc',
               'GObjectGetPropertyFunc',
               'GObjectSetPropertyFunc',
               'GWeakNotify',
               'GToggleNotify',
               'GValueTransform',
               'GtkStateType',
               'GtkExpanderStyle',
               'GtkShadowType',
               'GtkCornerType',

               'PangoFontsetForeachFunc',
               'PangoCoverageLevel',
               'PangoDirection',
               'PangoGravity',
               'PangoGravityHint',

               'WebKitLoadStatus',
               
               'size_t',
               'JSPropertyAttributes',
               'JSClassAttributes',
               'JSChar',
               'JSType',
               'JSObjectInitializeCallback',
               'JSObjectFinalizeCallback',
               'JSObjectHasPropertyCallback',
               'JSObjectGetPropertyCallback'
               'JSObjectSetPropertyCallback',
               'JSObjectDeletePropertyCallback',
               'JSObjectGetPropertyNamesCallback',
               'JSObjectCallAsFunctionCallback',
               'JSObjectCallAsConstructorCallback',
               'JSObjectHasInstanceCallback'
               'JSObjectConvertToTypeCallback',
               'JSStaticValue',
               'JSStaticFunction',
               'JSClassDefinition',

               ]

inheritances={'GObject': 'object' }
current_file = None
ptr_types = {}
prefix = ""
enum_types=[]
constructormapping={}
all_constructors={}

class Parser:
    
    def __init__(self, namespace):
        self._methods = {}
        self._staticmethods={}
        self._constructor = None
        self._classname=None
        self._namespace = namespace

    def parse_as_typedef_or_function_decl(self,  tokens ):
        if tokens[0]=='...':
            assert(len(tokens)==1)
            return ("*args","")
        name = tokens[-1]
        assert(name != '*')
        pointer_depth = 0
        del tokens[-1]
        while tokens and tokens[-1]=='*':
            pointer_depth +=1
            del tokens[-1]
        assert(len(tokens) == 1)
        typename = tokens[0]
        if typename in ['char','gchar'] and pointer_depth:
            pointer_depth -=1
            typename = 'c_char_p'
        elif pointer_depth and not typename in DEFAULT_TYPES:
            typename = "_"+typename
            ptr_types[typename] = 'c_void_p'
            pointer_depth -= 1
        while pointer_depth:
            typename = "POITNER(%s)"%typename
            pointer_depth -= 1
        return (name, typename)
    
    def wrap( self, returntype, statement):
        global constructormapping
        global all_onstructors
        global current_file
        if not returntype:
            numfuncargs = 0
        elif returntype in DEFAULT_TYPES:
            return ("return %s"%statement, "")
        elif returntype == None:
            return (statement,"")
        elif returntype[1:] in DEFAULT_TYPES:
            return ( "return %s"%statement,"")
        else:
            dependent = returntype[1:]
            
            #print "WRAPPING ########## %s %s"%(returntype, statement)
            returnmethod = constructormapping.get(dependent)
            if dependent == self._classname:
                numfuncargs = len(statement.split(','))-1
            elif returnmethod != None:
                numfuncargs = len(all_constructors[dependent])-1
            else:
                import glob
                for f in glob.glob('*%s.if'%returntype):
                    if f != current_file:
                        print "Processing %s: %s from %s: %s"%(f, current_file, statement, all_constructors)
                        namespac = f[1:].split('_')[0]
                        Parser(namespac).process(f)
                if all_constructors.get(dependent)==None:
                    raise Exception("Unknown class/constructor %s to return from %s; %s"%(dependent,statement,all_constructors))
                if not constructormapping.get(dependent):
                    constructormapping[dependent] = ""
                numfuncargs = len(all_constructors[dependent])
        if not returntype:
            return (statement, "")
        else:
            if numfuncargs>0:
                paramtext = ",".join( ["None" for i in xrange(numfuncargs)]) +","
            else:
                paramtext = ""
        if returntype in DEFAULT_TYPES:
            return ( "return %s"%statement, "")
        elif returntype.startswith("_WebKit"):
            return ( "return %s(%s obj=%s or c_void_p() )"%(dependent, paramtext, statement),
                     "from pywebkit3.webkit3 import %s"%dependent)
        elif returntype.startswith ("_Pango"):
            return ( "return %s(%s obj=%s  or c_void_p())"%(dependent, paramtext, statement),
                     "from pywebkit3.gtk3 import %s"%dependent)
        elif returntype.startswith ("_JS"):
            return ( "return %s(%s obj=%s  or c_void_p())"%(dependent, paramtext, statement),
                     "from pywebkit3.javascriptcore import %s"%dependent)
        elif returntype.startswith ("_Gtk"):
            return ( "return %s(%s obj=%s or c_void_p())"%(returntype[1:],paramtext, statement),
                     "from pywebkit3.gtk3 import %s"%dependent)
        elif returntype.startswith ("_G"):
            return ( "return %s(%s obj=%s or c_void_p())"%(returntype[1:], paramtext, statement),
                     "from pywebkit3.gobject import %s"%dependent)
        else:
            return ("return %s"%statement,"")
    
    def parse_params( self, methodname, returntype, api, position):
            
        global constructormapping
        global DEFAULT_TYPES
        assert(methodname != "*")
        tokens = api.split()
        if not tokens:
            return
        #print "TOKENS %s: %s: %s"%(tokens, returntype, self._classname)
        if tokens[0] == '...' and self._methods.has_key(methodname):
            self._methods[methodname].append(("*args",''))
            return
        elif (tokens[0] == 'void' and methodname.endswith('new') and position==0 and self._constructor==None) or (methodname.endswith('new') and returntype[1:] == self._classname) or (methodname.endswith('Create') and returntype[1:].startswith('JS') and (tokens[0] == returntype[1:] or tokens[1] == returntype[1:])):
            if tokens[0].startswith('JS') and tokens[0] != returntype[1:]:
                tmp = tokens[0]
                tokens[0] = tokens[1]
                tokens[1] = tmp
            all_constructors[self._classname]=[methodname]
            if len(tokens)>1:
                paramname, typename = self.parse_as_typedef_or_function_decl(tokens)
                all_constructors[self._classname].append( (paramname, typename))
            constructormapping[self._classname]=methodname
            self._constructor = all_constructors[self._classname]
            return 
        elif tokens[0] == 'void':
            assert(position == 0)
            self._staticmethods[methodname] = [returntype]
            return
        elif tokens[0] != self._classname and methodname.endswith('new'):
            if position == 0:
                all_constructors[self._classname] = [methodname]
                constructormapping[self._classname]=methodname
                self._constructor = all_constructors[self._classname]
            (paramname, typename) = self.parse_as_typedef_or_function_decl( tokens )
##            if len(tokens) >=3:
##                typename = tokens[0]
##                if typename in DEFAULT_TYPES:
##                    if typename == "gchar":
##                        paramname = 'c_char_p'
##                    else:
##                        paramname = "POINTER(%s)"%tokens[-1]
##                else:
##                    paramname = '_%s'%tokens[-1]
##            elif len(tokens) > 1:
##                typename = tokens[0]
##                paramname = tokens[-1]
##            else:
##                logging.error("Unable to parse '%s'"%api)
##                return
            all_constructors[self._classname].append((paramname, typename))
            constructormapping[self._classname] = methodname
            self._constructor = all_constructors[self._classname]
            return
        elif tokens[0] in DEFAULT_TYPES and tokens[1] !='*':
            typename=tokens[0]
            paramname = tokens[-1]
        elif tokens[0] in ['GdkAtom'] and tokens[1] != '*':
            typename = 'c_void_p'
            paramname = tokens[-1]
        elif tokens[0] == self._classname and position == 0:
            self._methods[methodname] = [returntype]
            return
        else:
            (paramname, typename) = self.parse_as_typedef_or_function_decl(tokens)
##            if len(tokens) < 2 or tokens[1]!='*':
##                logging.error("UNABLE TO PARSE PARAMS '%s'"%(api))
##                return
##            if len(tokens)!=3:
##                typename = tokens[0]
##                paramname = tokens[-1]
##            else:
##                assert(tokens[1]=='*')
##                typename = tokens[0]
##                if not typename in DEFAULT_TYPES:
##                    ptr_types[typename] = 'c_void_p'
##                    typename = "_%s"%typename
##                else:
##                    if typename =='gchar':
##                        typename = 'c_char_p'
##                    else:
##                        typename = "POINTER(%s)"%typename
##                paramname = tokens[-1]
##        if(paramname =='*'):
##            logging.error("UNABLE TO PARSE %s: %s"%(api,tokens)) 
        assert(paramname !='*')
        if position == 0 and not self._methods.has_key(methodname):
            if not self._staticmethods.has_key(methodname) and not all_constructors.has_key(methodname):
                
                self._staticmethods[methodname] = [returntype]
                self._staticmethods[methodname].append((paramname, typename))
        elif all_constructors.has_key(methodname):
            all_constructors[self._classname].append((paramname,typename))
            self._constructor = all_constructors[methodname]
        elif self._methods.has_key(methodname):
            self._methods[methodname].append((paramname, typename))
        elif self._staticmethods.has_key(methodname):
            self._staticmethods[methodname].append((paramname, typename))
            
        else:
            if not self._staticmethods.has_key(methodname) and not all_constructors.has_key(methodname):
                self._staticmethods[methodname] = [returntype]
                self._staticmethods[methodname].append((paramname, typename))
             
    
    def to_python( self, api ):
        global enum_types
        global inheritances
        global ptr_types
        global constructormapping
        
        if api.find('va_list') >=0:
            logging.error("Unable to parse variable arguments for %s"%api)
            return
        tokens = api.replace('const','').replace('volatile','').replace('*',' * ').replace('*  *','*').replace(';','').replace('(','|').replace(')','|').replace('  ',' ').split('|')
        declaration = tokens[0].split()
        if declaration[0] == 'enum':
            enum_types.append(declaration[1])
            DEFAULT_TYPES.append(declaration[1])
        elif api[0] == '#':
            return
        elif len(declaration)==1:
            if not self._classname:
                self._classname = declaration[0]
            else:
                global current_file
                logging.error("Two classnames in one i/f spec: %s in %s"%(declaration[0],current_file))
                logging.error("... from line:  %s"%api)
                assert(not self._classname)
                
        elif declaration[0] == 'struct':
            if not self._classname:
                self._classname = declaration[1]
        elif declaration[0] == 'inherit':
            inheritances[self._classname] = declaration[1]
        else:
            if declaration[0] == 'void' and declaration[1] != '*':
                methodname = declaration[-1]
                self._methods[methodname] = [None]
                returntype = None
            elif len(declaration) == 2:
                methodname = declaration[-1]
                #methods[methodname] = [declaration[0]]
                returntype = declaration[0]
            elif(declaration[1] == '*'):
                ptr_types[declaration[0]] = 'c_void_p'
                methodname = declaration[-1]
                #methods[methodname] = ['_%s'%declaration[0]]
                returntype = '_%s'%declaration[0]
            elif declaration[0] in DEFAULT_TYPES and declaration[1] == '*':
                methodname = declaration[-1]
                if declaration[0] != 'gchar':
                    returntype = 'POINTER(%s)'%declaration[0]
                else:
                    returntype = 'c_char_p'
                #returntype = methods[methodname][0]
            else:
                logging.error("ERROR: parsing line %s",api)
                return
    
            if len(tokens)>1:
                params = tokens[1].split(',')
                index = 0
                for paramline in params:
                    self.parse_params(methodname, returntype, paramline, index)
                    index += 1
                if self._staticmethods.has_key(methodname) and self._methods.has_key(methodname):
                    del self._methods[methodname]
     
    def emit_python(self, namespace):
        global all_constructors
        global constructormapping
        LIB_NAME = "lib%s"%namespace
        def gen_params_constructor():
            text = ""
            eval_text = ""
            assertions = []
            cmethod = self._constructor[0]
            print "XXXXXXXXXXXX %s %s"%(self._constructor, all_constructors[self._classname])
            for param in self._constructor[1:]:
                if (not param[0].strip() == '*args') and  not((param[1] in DEFAULT_TYPES) or (param[1] == 'c_char_p')):
                    eval_text +="""        if %(paramname)s : %(paramname)s = %(paramname)s._object\n"""%{'paramname':param[0]}
                    eval_text += """        else : %(paramname)s = c_void_p()\n"""%{'paramname':param[0]}
                text += "%s, "%param[0]
                #assertions.append("assert(isinstance(%s, %s))"%(param[0], param[1]))
            return (text, eval_text, assertions)
        
        def gen_params(methodname, LIB_NAME, callable= False):
            text = ""
            pretext = ""
            evaltext= ""
            if self._methods.has_key(methodname):
                m = self._methods
                is_static = False
            else:
                m = self._staticmethods
                is_static = True
            for param in m[methodname][1:]:
                if callable:
                    if param[0]=='*args':
                        text +="*args"
                    else:
                        if not(param[0].strip()=='*args') and not(param[1] in DEFAULT_TYPES or param[1] == 'c_char_p'):
                            evaltext += """        if %(paramname)s : %(paramname)s = %(paramname)s._object\n"""%{'paramname':param[0]}
                            evaltext += """        else : %(paramname)s = c_void_p()\n"""%{'paramname':param[0]}
                        text += "%s, "%param[0]
                else:
                    if param[0] == '*args':
                        known_types = ['c_void_p']
                        known_args = []
                        for p in m[methodname][1:]:
                            if p[0] != '*args':
                                known_types.append(p[1])
                                known_args.append(p[0])
                        args = ', '.join(known_args)
                        if args: args += ','
                        pretext = """
        def callit( %(args)s *args ):
                %(lib_name)s.%(methodname)s.restype = %(return_type)s
                %(lib_name)s.%(methodname)s.argtypes = [c_void_p, %(known_types)s]
                for arg in args:
                     %(lib_name)s.%(methodname)s.argtypes.append(args[1])
                return %(lib_name)s.%(methodname)s(self._object, %(args)s *args)
    """%{'lib_name':LIB_NAME,'known_types':', '.join(known_types), 'args':args,
    'methodname':methodname, 'return_type': m[methodname][0]}
                        text += "*args "
                    else:
                        if not(param[0].strip()=="*args") and  not(param[1] in DEFAULT_TYPES or param[1] == 'c_char_p'):
                            evaltext += """        if %(paramname)s : %(paramname)s = %(paramname)s._object\n"""%{'paramname':param[0]}
                            evaltext += """        else : %(paramname)s = c_void_p()\n"""%{'paramname':param[0]}
                        text += " %s,"%param[0]
                        
            return (text, pretext, evaltext)
        if not self._classname:
            self._classname = ""
        if self._classname== "void":
            self._classname= ""
        with open(os.path.join('pywebkit3','_%s_%s.py'%(namespace,self._classname)),'w') as f:
            prefix = "_".join(l.lower() for l in re.findall('[A-Z][^A-Z]*', self._classname.replace('WebKit','Webkit')))
            prefix += '_'
            assert(namespace != 'gtk')
            f.write("""# Copyright, John Rusnak, 2012
    # This code binding is available under the license agreement of the LGPL with
    # an additional constraint described below,
    # and with the understanding that the webkit API is copyright protected
    # by Apple Computer, Inc. (see below).
    # There is an  additional constraint that any derivatives of this work aimed
    # at providing bindings to GObject, GTK, GDK, or WebKit be strictly
    # python-only bindings with no native code.
    # * THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY
    # * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    # * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
    # * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    # * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    # * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    # * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    #
    # ******************************************************
    # For the API:
    # /*
    # * Copyright (C) 2006 Apple Computer, Inc.  All rights reserved.
    # *
    # * Redistribution and use in source and binary forms, with or without
    # * modification, are permitted provided that the following conditions
    # * are met:
    # * 1. Redistributions of source code must retain the above copyright
    # *    notice, this list of conditions and the following disclaimer.
    # * 2. Redistributions in binary form must reproduce the above copyright
    # *    notice, this list of conditions and the following disclaimer in the
    # *    documentation and/or other materials provided with the distribution.
    # *
    # * THIS SOFTWARE IS PROVIDED BY APPLE COMPUTER, INC. ``AS IS'' AND ANY
    # * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    # * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
    # * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    # * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    # * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    # * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    # */\n""")
            f.write("""from ctypes import *
from gtk3_types import *
from %s_types import *
    
    """%namespace)
                
            f.write("\n")
            f.write('"""Derived Pointer Types"""\n')
            for t,val in ptr_types.iteritems():
                f.write(("_%s = %s\n"%(t, val)))
                
            f.write("")
            f.write('"""Enumerations"""\n')
            for t in enum_types:
                f.write("%s = c_int\n"%t)
                
            f.write("\n")
            if self._classname == "void":
                self._classname = ""
            if self._classname != "":
                parentpackage = '_%s'%inheritances[self._classname].replace('.','_')
                parentclass = inheritances[self._classname].split('.')[-1]
                if inheritances[self._classname] != 'object':
                    f.write('import %s\n'%parentpackage)
                    f.write('class %s( %s.%s):\n'%(self._classname, parentpackage, parentclass))
                else:
                    f.write('class %s( object):\n'%(self._classname))
                f.write('    """Class %s Constructors"""\n'%self._classname)
                
                #for c_name, param in self._constructor:
                if self._constructor:
                    (text, eval_text, assertions) = gen_params_constructor()
                    calltext = text
                    if text.find("*args,")>=0:
                        text = text.replace("*args,","")
                        text += "obj=None, *args"
                    else:
                        text += " obj = None"
                    f.write( "    def __init__( self, %s):\n"%text)
                    f.write("        if obj: self._object = obj\n")
                    f.write("        else:\n")
                    for assertion in assertions:
                        f.write("            %s\n"%assertion)
                    c_name = self._constructor[0]
                    
                    f.write( "            %s.%s.restype = c_void_p\n"%(LIB_NAME,c_name ))
                    f.write(eval_text+"\n")
                    if len(self._constructor)>0:
                        f.write( "        %s.%s.argtypes = [%s]\n"%( LIB_NAME,c_name, ','.join([p[1] for p in self._constructor[1:]])))
                    calltext = calltext.replace("*args,","*args")
                    f.write("        self._object = %s.%s(%s)\n"%(LIB_NAME, c_name, calltext))
                else:
                    f.write("    def __init__(self, obj = None):\n")
                    f.write("        self._object = obj")
                    all_constructors[self._classname] = []
                    constructormapping[self._classname] = ""
                f.write("\n")
                f.write('    """Methods"""\n')
                for methodname in self._methods.iterkeys():
                    methodname2 = methodname.replace(prefix,'')
                    if methodname2 in KEY_WORDS:
                        methodname2 = "py_%s"%methodname2
                
                    text, pretext, evaltext =  gen_params(methodname, LIB_NAME)
                    
                    f.write("    def %s(self, %s):\n"%(methodname2,text))
                    f.write(evaltext + "\n")                        
                    if pretext == "":
                        if self._methods[methodname][0]:
                            f.write( "        %s.%s.restype = %s\n"%(LIB_NAME,methodname, self._methods[methodname][0]))
                        if len(self._methods[methodname])>1:
                            f.write("        %s.%s.argtypes = [c_void_p, %s]\n"%(LIB_NAME,methodname,','.join([p[1] for p in self._methods[methodname][1:]])))
                        else:
                            f.write("        %s.%s.argtypes = [c_void_p]\n"%(LIB_NAME,methodname))
                        statement = "%s.%s(self._object, %s)"%( LIB_NAME,methodname, text)
                        (statement, importstatement) = self.wrap( self._methods[methodname][0], statement)
                        text,_,_ = gen_params(methodname, LIB_NAME,callable=True)
                        f.write("        %s\n"%importstatement)
                        f.write("        %s\n"%statement)
                    else:
                        f.write(pretext+"\n")
                        f.write("        return callit(%s)\n"%text)
                    f.write("\n")
                for methodname in self._staticmethods.iterkeys():
                    f.write("    @staticmethod\n")
                    text,pretext,evaltext = gen_params(methodname, LIB_NAME)
                    f.write("    def %s(%s):\n"%(methodname.replace(prefix,''), text))
                    f.write(evaltext)
                    if self._staticmethods[methodname][0]:
                        f.write( "        %s.%s.restype = %s\n"%(LIB_NAME, methodname, self._staticmethods[methodname][0]))
                    if len(self._staticmethods[methodname])>1:
                        f.write("        %s.%s.argtypes = [%s]\n"%(LIB_NAME, methodname, ','.join([p[1] for p in self._staticmethods[methodname][1:]])))
                    if self._staticmethods[methodname][0]:
                        ret = "return "
                    else:
                        ret=""
                    text,pretext,_ = gen_params(methodname, LIB_NAME, callable= True)
                    f.write("        %s%s.%s(%s)\n"%(ret, LIB_NAME,methodname, text)) 
                    f.write("\n")
            else:
                for methodname in self._staticmethods.iterkeys():
                    f.write("\n")
                    prefix='gtk3_'
                    text,_,evaltext =gen_params(methodname, LIB_NAME)
                    f.write("def %s(%s):\n"%(methodname.replace(prefix,''), text))
                    f.write(evaltext.replace("        ","    "))
                    if self._staticmethods[methodname][0]:
                        f.write( "    %s.%s.restype = %s\n"%(LIB_NAME,methodname, self._staticmethods[methodname][0]))
                    if len(self._staticmethods[methodname])>1:
                        f.write("    %s.%s.argtypes = [%s]\n"%(LIB_NAME,methodname,','.join([p[1] for p in self._staticmethods[methodname][1:]])))
                    if self._staticmethods[methodname][0]:
                        ret = "return "
                    else:
                        ret=""
                    gen_params(methodname, LIB_NAME,callable=True)
                    f.write("    %s%s.%s(%s)\n"%(ret, LIB_NAME,methodname, text)) 
                    f.write("\n")
    

    
    def process(self, filename):
        global current_file
        current_file = filename
        with open ( filename, 'r') as f:
            line = ""
            while line != None:
                text = f.readline()
                
                if text=="":
                    break
                elif not text.startswith('#'):
                    line += text
                    if line.find(';')>=0:
                        self.to_python(line.replace('const',''))
                        line="" 
        
            self.emit_python(namespace)
    

namespace = sys.argv[1][1:].split('_')[0]
    
classname = None
constructormapping={}
Parser(namespace).process(sys.argv[1])
