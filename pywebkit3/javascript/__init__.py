import gobject
from gobject import GObject

import inspect
import threading
from ..javascriptcore import *
from ctypes import *
import logging
import traceback
import importlib

def strid(obj):
    return str( cast( obj._object, c_void_p))

def to_string(var):
    if isinstance(var, JavascriptClass):
        return var._varname
    elif isinstance(var, str):
        return "'%s'"%var
    else:
        return str(var)

def to_pyvalue( context, jsvalue, name ):
    valtype = jsvalue.GetType( context)
    if valtype == kJSTypeNull.value  or valtype == kJSTypeUndefined.value:
        return None
    elif valtype == kJSTypeNumber.value:
        return jsvalue.ToNumber( context, NULL)
    elif valtype == kJSTypeBoolean.value:
        return jsvalue.ToBoolean( context)
    elif valtype == kJSTypeString.value:
        jstext = jsvalue.ToStringCopy( context, NULL)
        length = jstext.GetMaximumUTF8CStringSize()
        cstring = (c_char*(length))()
        jstext.GetUTF8CString( cstring, length )
    
        return cstring.value 
    elif valtype == kJSTypeObject.value:
        jsobj = jsvalue.ToObject(context, NULL)
        if jsobj.IsFunction(context):
            return None
            #assert( isinstance( context, JSContext ))
            #return _wrapJs( context, jsobj, name, can_call = True)
        found = JavascriptClass._jsobjects.get(strid(jsobj))
        if found:
            (_,found) = found
        else:
            found = JavascriptClass._globalobjects.get(strid(context)+name)
        return  found

    logging.error("Unknown object passed to python from javascript. Object must be known in both worlds.  %d"%valtype)
    return None


class JavascriptClass(object):
    """Class instance of which are accessible within a javascript"""
    _methods = None
    _methods_by_name= {}
    _jsobjects = {}
    _globalobjects = {}
    _python_to_js = {}
    _constructors = {}

    @classmethod
    def _populate(cls ):
        cls._methods = [m for m in inspect.getmembers(cls, predicate=inspect.ismethod) if not m[0].startswith('_') and not m[0] == 'create']
        cls.staticmethods = (JSStaticFunction*(len(cls._methods)+1))()
        #tag end:
        cls.staticmethods[-1].name = cast(NULL, c_char_p)
        cls.staticmethods[-1].callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
        cls.staticmethods[-1].attributes = 0
        def getfunc(index):
            def call_method(ctxt, function, obj, argumentCount, arguments, exception):
                try:
                    id = strid(JSContext(obj = ctxt))
                    #context =  JavascriptClass._jsobjects[id]
                    context = JSContext(obj=ctxt)
                    (_,pyobj) = JavascriptClass._jsobjects[ str(cast(obj, c_void_p))]
                    method = cast(function, c_void_p)
                    key = cls.staticmethods[index].name
                    to_call = cls._methods_by_name.get(key)
                    if not to_call:
                        logging.error("Unrecognized method!  Internal error in javascript python binding %s"%key)
                    arguments = cast(arguments, POINTER(POINTER(c_int)))
                    ctxt = cast(ctxt, POINTER(c_int))
                    args = []
                    for i in xrange(argumentCount):
                        import numbers
                        if isinstance(arguments[i],numbers.Number):
                            args.append(arguments[i])
                        else:
                            valtype = JSValue(obj=arguments[i]).GetType( context)
                            if valtype == kJSTypeNull.value or valtype== kJSTypeUndefined:
                                args.append(None)
                            elif valtype == kJSTypeNumber.value:
                                args.append(JSValue(arguments[i]).ToNumber( context, NULL))
                            elif valtype == kJSTypeBoolean.value:
                                args.append(JSValue(arguments[i]).ToBoolean( context))
                            elif valtype == kJSTypeString.value:
                                jstext = JSValue(arguments[i]).ToStringCopy( context, NULL)
                                length = jstext.GetMaximumUTF8CStringSize()
                                cstring = (c_char*(length))()
                                jstext.GetUTF8CString( cstring, length )

                                args.append( cstring.value )
                            elif valtype == kJSTypeObject.value:
                                jsobject = JSValue(arguments[i]).ToObject( context, NULL)
                                found = JavascriptClass._jsobjects.get(strid(jsobject))
                                if found:
                                    (_,found) = found
                                    args.append( found._javascript_obj )
                                else:
                                    can_call = jsobject.IsFunction(context)
                                    pyarg = _wrapJs( context, jsobject, "arg%s"%i, can_call = can_call)
                                    assert(pyarg)
                                    args.append( pyarg )
                            else:
                                logging.error( "Invalid javascript value %d"%valtype)
                                return 0
                    assert(len(args) == argumentCount)
                    value =  to_call[1]( pyobj, *args )
                    import numbers
                    if isinstance( value, numbers.Number):
                        retval= JSValue.MakeNumber(context, value)._object
                    elif isinstance( value, str):
                        cstring = c_char_p(value)
                        text = JSString.CreateWithUTF8CString(cstring);
                        retval = JSValue.JSValueMakeString(context, text)._object;
                    elif isinstance( value, JavascriptClass):
                        retval = value._javascript_obj._object
                    else:
                        retval = NULL
                    retvalp = cast(byref(retval), POINTER(c_longlong))
                    return retvalp.contents.value
                except:
                    logging.error("EXCEPTION calling python method from javascript:")
                    logging.error(traceback.format_exc())
                    return 0#NULL
                
            return call_method

        
        for index in xrange(len(cls._methods)):
            name = cls._methods[index][0]
            call_method = getfunc(index)
            cls.staticmethods[index].name = c_char_p( name)
            cls.staticmethods[index].callAsFunction  = JSObjectCallAsFunctionCallback( call_method)
            cls.staticmethods[index].attributes = kJSPropertyAttributeReadOnly
            cls._methods_by_name[cls.staticmethods[index].name] = cls._methods[index]        

    def __init__(self, js_context, var_name, **kargs):
        id = str(cast( js_context._object, c_void_p))
        if not id in JavascriptClass._python_to_js.iterkeys():
            if not JavascriptClass._python_to_js:
                ScriptEnv( self._context )
            else:
                id = JavascriptClass._python_to_js.keys()[0]

        if not "_module" in kargs.iterkeys():
            _module = None
        else:
            _module = kargs['_module']
        self._varname = var_name
        """This should take no parameters, to prevent repercussions throughout hierarchy"""
        cls = self.__class__
        if not isinstance(cls, Namespace) and not cls._methods:
            cls._populate( )
        elif not cls._methods:
            cls._populate( )
        if not _module:
            try:
                #modulename =self.__module__
                if var_name.find('.')>=0:
                    modulename = ".".join(var_name.split(".")[:-1])
                else:
                    modulename = ""
            except:
                modulename = None
        else:
            if isinstance( self, Constructor):                    
                modulename = _module.__name__
            else:
                modulename =  '.'.join(_module.__name__.split('.')[:-1])
            
        if modulename:
            ns = Namespace.get_namespace(js_context, modulename )
            assert(ns)
            assert( str(cast(js_context._object,c_void_p))+modulename in Namespace._namespaces.iterkeys() )
        else:
            if var_name and modulename == "":
                ns = Namespace.get_global(js_context)                
                assert(ns)
            elif not var_name:
                ns = None
                self._javascript_obj = js_context.GetGlobalObject()
                
        def _init_cb(context, obj):
            pass
          
        def _finalize_cb(obj):
            (_,pyobj) = JavascriptClass._jsobjects.get(str(cast(obj,c_void_p)))
            if pyobj:
                del JavascriptClass._jsobjects[str(cast(obj,c_void_p))]
                pyobj._javascript_obj = None
                

        jscd = JSClassDefinition()
        jscd.version = 0
        jscd.attributes = kJSClassAttributeNone
        jscd.className =c_char_p( cls.__name__) 
        jscd.parentClass = NULL
        jscd.staticValues = POINTER(JSStaticValue)()
        jscd.staticFunctions = cls.staticmethods
        if not _module:
            jscd.initialize = JSObjectInitializeCallback ( _init_cb)
            jscd.finalize = JSObjectFinalizeCallback (_finalize_cb)
        else:
            jscd.initialize = cast(NULL, JSObjectInitializeCallback )
            jscd.finalize = cast(NULL, JSObjectFinalizeCallback )
           
        jscd.hasProperty = cast(NULL,JSObjectHasPropertyCallback)
        jscd.getProperty = cast(NULL,JSObjectGetPropertyCallback)
        jscd.setPrpoerty = cast(NULL,JSObjectSetPropertyCallback)
        jscd.deleteProprety = cast(NULL,JSObjectDeletePropertyCallback)
        jscd.getPropertyName = cast(NULL, JSObjectGetPropertyNamesCallback)
        jscd.callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
        jscd.callAsConstructor = cast(NULL,JSObjectCallAsConstructorCallback)
        jscd.hasInstance = cast(NULL,JSObjectHasInstanceCallback)
        jscd.convertToType = cast(NULL, JSObjectConvertToTypeCallback)
        jscd.argtype=[POINTER(c_int), POINTER(c_int)]
        classDef = JSObject.JSClassCreate( byref(jscd) )
        self._javascript_obj = JSObject.Make( js_context, classDef, None )
        
        JavascriptClass._jsobjects[strid(self._javascript_obj)] =  (self._javascript_obj,self)
        if not _module:
            if not self.__class__.__name__ in JavascriptClass._constructors:
                self.__class__.export_class(js_context, ns)
        if ns:  
            text = JSString.CreateWithUTF8CString(var_name.split('.')[-1])
            ns._javascript_obj.SetProperty( js_context,
                                            text,
                                            self._javascript_obj,
                                            kJSPropertyAttributeNone,
                                            NULL)
        assert(self._javascript_obj)
               
        
            
    @classmethod
    def export_class(cls, js_context, ns):
        if not issubclass(cls, Constructor) and not cls.__name__ in JavascriptClass._constructors.iterkeys():
            js_constructor = JavascriptClass.get_constructor( cls, js_context, ns)
            text = JSString.CreateWithUTF8CString("%s"%( cls.__name__.split('.')[-1]))
            JavascriptClass._constructors[cls.__name__] = js_constructor


    @staticmethod
    def get_constructor( pyclass, context, namespace):
        
        assert(isinstance(namespace,Namespace))
        pyclass._constructor = Constructor
        retval = pyclass._constructor(pyclass, context, namespace)
        return retval

_constructors=[]
 

class Constructor(JavascriptClass):

    def __init__(self, pyclass, context, namespace):
        pymodule = importlib.import_module(pyclass.__module__)
        JavascriptClass.__init__(self, context,
                                 var_name="%s"%pyclass.__name__, 
                                 _module = pymodule)
        self._pyclass = pyclass
        self._context = context

    def new_( self, name, *args):
        try:
            return self._pyclass( self._context, name, *args)
        except:
            logging.error("Exception instantiating %s"%pyclass)
            logging.error(traceback.format_exc())
            return None
        
class Namespace( JavascriptClass ):

    _namespaces = {}
    
    def __init__(self, context, module ):
        assert(context)
        module_name = module.__name__ if module else ""
        self._context = context
        self._module = module
        
        if module: 
            module_name = module.__name__
            JavascriptClass.__init__(self, context, module_name , _module = module)
        else:
            module_name = ""
            self._javascript_obj = context.GetGlobalObject()
            
        Namespace._namespaces[ str(cast(context._object, c_void_p)) + module_name ] = self
        if module:
            self._export_classes()

        
    def _export_classes(self):
        for name, obj in inspect.getmembers(self._module):
            if inspect.isclass(obj) and issubclass(obj, JavascriptClass) and \
                   not issubclass(obj, Namespace ) and not obj==JavascriptClass:
                
                self._add_child_class(  obj)
        
            
    @staticmethod
    def get_namespace( context, modulename):
        id = str(cast(context._object, c_void_p))+modulename
        if not id in Namespace._namespaces.iterkeys():
            if modulename:
                m = importlib.import_module(modulename)
                Namespace._namespaces[id] = Namespace( context, m)
            else:
                Namespace._namespaces[id] = Namespace( context, None)
        return Namespace._namespaces[id]
    
    @staticmethod
    def get_global( context):
        ns =  Namespace.get_namespace( context, "")
        return ns
        
    @staticmethod
    def add_global_class( context, pyclass , *args):
        pyclass.export_class( context, Namespace.get_global(context))
        
    def _add_child_class(self,  cls):
        cls.export_class( self._context, self)




def _wrapJs(context,  jsobj, var_name, can_call = False):
    assert( isinstance( context, JSContext ))
    id = str(cast( jsobj._object, c_void_p))
    wrapped = PythonWrapper( context, jsobj, var_name, can_call)
    return wrapped
    

class PythonWrapper( JSObject ):

    
    
    def __init__(self, context, obj, var_name, can_call = False):
        assert( isinstance( context, JSContext ))
        self._cmd = ""
        self._retval = None
        JSObject.__init__(self, obj=obj._object )
        self._varname = var_name
        self._wrapped_obj = obj
        names = obj.CopyPropertyNames( context )
        count = JSObject.JSPropertyNameArrayGetCount( names )
        self._can_call = can_call
        self._attributes = {}
        self._context = context
        for index in xrange(count):
            var_name_ref = JSObject.JSPropertyNameArrayGetNameAtIndex( names, index)
            length = var_name_ref.GetMaximumUTF8CStringSize()
            var_name = (c_char*(length))()
            var_name_ref.GetUTF8CString( var_name, length )
            if var_name.value != "each":
                exc = POINTER(c_int)(c_int(0))
                prop = obj.GetProperty( context, var_name_ref, exc)
                self._attributes[var_name.value] =  to_pyvalue(context, prop, var_name.value)

                
    def __call__(self, *args):
        cmd=  "%s(%s)"%(self._varname, ",".join([to_string(v) for v in args]))
        id = str(cast( self._context._object, c_void_p))
        if not id in JavascriptClass._python_to_js.iterkeys():
            if not JavascriptClass._python_to_js:
                ScriptEnv( self._context )
            else:
                id = JavascriptClass._python_to_js.keys()[0]

        env = JavascriptClass._python_to_js[id]
        (index, tmpvarname) = env._tmpvarname()
        cmd = "try{python.PY_RETURN( %(cmd)s,'%(tmp)s');}catch(err){python.PY_THROW(err);}"%\
              {'tmp':tmpvarname,
               'cmd':cmd}
        (returnval, exc)  = env.execute( self, cmd, tmpvarname)
        if exc:
            raise exc
        if returnval:
            self._retval = (returnval , "python.%s"%tmpvarname)
            self._retval[0]._webview = self._webview
            self._retval[0]._varname = "python.%s"%tmpvarname 
            return self._retval[0]
        else:
            return None



    def each(self, func, *args):
        js = "%s.each( function(index,obj){try{python.PY_EACH(  $(obj), index);}catch(err){PY_THROW(err);}})"%self._varname
        id = str(cast( self._context._object, c_void_p))
        if not id in JavascriptClass._python_to_js.iterkeys():
            if not JavascriptClass._python_to_js:
                ScriptEnv( self._context )
            else:
                id = JavascriptClass._python_to_js.keys()[0]
        env = JavascriptClass._python_to_js[id]
        env._webview = self._webview
        env._each_apply = (func, args)
        env.execute( self, js , None)
        env._each_apply = None
        
        
    def _hooked(self, *args):
        cmd=  "%s.%s(%s)"%(self._varname, self._attr, ",".join([to_string(v) for v in args]))
        id = str(cast( self._context._object, c_void_p))
        if not id in JavascriptClass._python_to_js.iterkeys():
            if not JavascriptClass._python_to_js:
                ScriptEnv( self._context )
            else:
                id = JavascriptClass._python_to_js.keys()[0]
        env = JavascriptClass._python_to_js[id]
        (index, tmpvarname) = env._tmpvarname()
        cmd = "try{python.PY_RETURN( %(cmd)s,'%(tmp)s');}catch(err){python.PY_THROW(err);}"%\
            {'tmp':tmpvarname,
             'cmd':cmd}
        (retval, exc ) = env.execute(self, cmd, tmpvarname)
        if exc:
            raise exc
        else:
            if retval and isinstance(retval, JavascriptClass):
                retval._webview = self._webview
                return retval
        
        
    def __getattr__(self,attr):
        if not attr in self._attributes.iterkeys():
            if  hasattr(self, attr):
                logging.error("RETURNING KNOWN ATTR")
                #env.execute( self, self._cmd)
                return getattr(self, attr)
#            elif attr.startswith('__'):
#                return None
            else:
                raise Exception("No such method or attribute in %s: %s in %s %s"%(self._varname, attr,[k for k in self._attributes.iterkeys()],dir(self)))
        val = self._attributes[attr]
        if val and hasattr(self, '_webview'):
            val._webview = self._webview
            
        if not val:
            self._attr = attr
            return self._hooked
        else:
            return val
        
        
        
def export_module( context, module):
    import importlib
    importlib.import_module( module.__name__)
    if module.__name__ in Namespace._namespaces:
        return
    return Namespace( context, module )


class JSException( Exception):

    def __init__(self, err):
        Exception.__init__(self, err)
        self._err = err

        

class ScriptEnv( JavascriptClass ):

    _sem = threading.Semaphore()
    _current_executor = None


    _tmps = []
    
    def _tmpvarname(self):
        l = len(ScriptEnv._tmps)
        ScriptEnv._tmps.append(l)
        return (l, "_tmp%d"%l)
    
    def __init__( self, context):
        id = str(cast( context._object, c_void_p))
        assert( not JavascriptClass._python_to_js)
        JavascriptClass._python_to_js[id] = self
        JavascriptClass.__init__(self, context, "python")
        self._context = context
        self._contextid = str(cast(context._object, c_void_p))
        self._exception = None
        self._returnval = None
        self._each_apply  = None
        
    def export_to_python( self, jsobj , var_name, can_call = False ):
        wrapped = _wrapJs( self._context, jsobj, var_name, can_call )
        JavascriptClass._globalobjects[self._contextid + var_name] = wrapped
        
    def PY_RETURN( self, jsobj , name):
        self._returnval = jsobj
        if isinstance( jsobj, JavascriptClass):
            self._returnval._varname = name
        #if jsobj and isinstance( jsobj, JavascriptClass):
        text = JSString.CreateWithUTF8CString(name)
        if not isinstance(jsobj, str):
            self._javascript_obj.SetProperty( self._context,
                                              text,
                                              jsobj,
                                              kJSPropertyAttributeNone,
                                              NULL)
        self._exception = None

    def PY_THROW( self , jserr):
        logging.error("javascript error encountered ")
        self._exception =  JSException( jserr.line  )

    

    def PY_EACH( self,  obj, index):
        text = JSString.CreateWithUTF8CString('_jqobj%d'%index)
        self._javascript_obj.SetProperty( self._context,
                                          text,
                                          obj,
                                          kJSPropertyAttributeNone,
                                          NULL)
        obj =  PythonWrapper(self._context, self._javascript_obj.GetProperty( self._context, text, NULL).ToObject(self._context, NULL), 'python._jqobj%d'%index)
        obj._webview = self._webview
        if self._each_apply:
            try:
                self._each_apply[0](obj, int(index), *self._each_apply[1])
                self._webview.execute_script("delete python._jqobj%d;"%index)
            except:
                logging.error("Error applying each function at index %d"%index)
                logging.error(traceback.format_exc())
            
        return False
        
    def execute( self, source, cmd, tmpvarname = None):
        try:
            source._webview.execute_script(cmd)
            exc    = self._exception
            retval = self._returnval
            if tmpvarname and retval and isinstance(retval, JavascriptClass):
                
                text = JSString.CreateWithUTF8CString("%s"%tmpvarname)
                self._javascript_obj.SetProperty( self._context,
                                                  text,
                                                  retval,
                                                  kJSPropertyAttributeNone,
                                                  NULL)

            if retval and isinstance(retval, JavascriptClass):
                retval._webview = source._webview
        except:
            logging.error(traceback.format_exc())
            exc = Exception
            retval = None
        return (retval, exc )

    @staticmethod
    def get_jsobject(webview, name , can_call = False):
        context = webview.get_main_frame().get_global_context()
        id = str(cast(context._object, c_void_p))
        if not id in JavascriptClass._python_to_js.iterkeys():
            if not JavascriptClass._python_to_js:
                ScriptEnv( self._context )
            else:
                id = JavascriptClass._python_to_js.keys()[0]
        
        retval =  JavascriptClass._globalobjects.get( id+name)
        
        if retval:
            retval._webview = webview
            
        else:
            webview.execute_script("python.export_to_python(%s,'%s', %s);"%(name, name, int(can_call)))
            retval =  JavascriptClass._globalobjects.get( id+name)
            if retval:
                retval._webview = webview
            else:                
                raise Exception("Unknown javascript object by name %s"%name)
        JavascriptClass._globalobjects[id+name] = retval
        return retval


