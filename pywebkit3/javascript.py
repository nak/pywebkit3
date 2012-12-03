import pywebkit3.javascriptcore
from pywebkit3 import gobject

import inspect
import threading
from javascriptcore import *
from ctypes import *
import logging
import traceback
import importlib

def strid(obj):
    return str( cast( obj._object, c_void_p))

def to_pyvalue( context, jsvalue ):
    valtype = jsvalue.GetType( context)
    if valtype == kJSTypeNull.value  or valtype == kJSTypeUndefined.value:
        return None
    elif valtype == kJSTypeNumber.value:
        return jsvalue.ToNumber( context, NULL)
    elif valtype == kJSTypeBoolean.value:
        return jsvalue.ToBoolean( context, NULL)
    elif valtype == kJSTypeString.value:
        jstext = jsvalue.ToStringCopy( context, NULL)
        length = jstext.GetMaximumUTF8CStringSize()
        cstring = (c_char*(length))()
        jstext.GetUTF8CString( cstring, length )
    
        return cstring.value 
    elif valtype == kJSTypeObject.value:
        jsobj = jsvalue.ToObject(context, NULL)
        found = JavascriptClass._jsobjects.get(strid(jsobj))
        if found:
            (_,found) = found
        return  found

    logging.error("Unknown object passed to python from javascript. Object must be know in both worlds.  %d"%valtype)
    return None


class JavascriptClass(object):
    """Class instance of which are accessible within a javascript"""
    _methods = None
    _methods_by_name= {}
    _jsobjects = {}
    _python_to_js = {}
    _constructors = {}
    _jsliveobjects={}
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
                    context = JSObject(obj=ctxt)
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
                                args.append(JSValue(arguments[i]).ToBoolean( context, NULL))
                            elif valtype == kJSTypeString.value:
                                jstext = JSValue(arguments[i]).ToStringCopy( context, NULL)
                                length = jstext.GetMaximumUTF8CStringSize()
                                cstring = (c_char*(length))()
                                jstext.GetUTF8CString( cstring, length )

                                args.append( cstring.value )
                            elif valtype == kJSTypeObject.value:
                                jsobject = JSValue(arguments[i]).ToObject( context, NULL)
                                logging.error("XXXXXXXXXX %s"%jsobject)
                                found = JavascriptClass._jsobjects.get(strid(jsobject))
                                if found:
                                    (_,found) = found
                                    args.append( found._javascript_obj )
                                else:
                                    pyarg = _wrapJs( context, jsobject, "arg%s"%i)
                                    assert(pyarg)
                                    args.append( pyarg )
                            else:
                                logging.error( "Invalid javascript value %d"%valtype)
                                return 0
                    try:
                        logging.error("#####################%s"%pyobj.__name__)
                    except:
                        pass
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
            ScriptEnv( js_context )

        if not "_module" in kargs.iterkeys():
            _module = None
        else:
            _module = kargs['_module']
        self._var_name = var_name
        """This should take no parameters, to prevent repercussions throughout hierarchy"""
        cls = self.__class__
        logging.error("VAR NAME IS %s"%var_name)
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
        
        JavascriptClass._jsobjects[str(cast(self._javascript_obj._object,c_void_p))] =  (self._javascript_obj,self)
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
            logging.error("CLASS CB IS %s"%self._pyclass)
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




def _wrap(context, pyobj, obj_name):
    if isinstance(pyobj, JavascriptClass):
        return pyobj
    if pyobj.__module__:
        module = importlib.import_module(pyobj.__module__)
        export_module( context, module)
    else: 
        module = None
    cls = pyobj.__class__
            

    class PythonToJSWrapper(cls, JavascriptClass):
    
        def __init__(self,context, obj_name, wrapped_obj):
            JavascriptClass.__init__(self, context, obj_name)
            self.wrapped_obj = wrapped_obj
    
        def __getattr__(self,attr):
            orig_attr = self.wrapped_obj.__getattribute__(attr)
            if callable(orig_attr):
                def hooked(*args, **kwargs):
                    return orig_attr(*args, **kwargs)
                return hooked
            else:
                return orig_attr
    return PythonToJSWrapper(context, obj_name, pyobj)


def _wrapJs(context,  jsobj, var_name, can_call = False):
    id = str(cast( jsobj._object, c_void_p))
    wrapped = PythonWrapper( context, jsobj, var_name, can_call)
    JavascriptClass._jsliveobjects[id] = wrapped
    return wrapped
    

class PythonWrapper( JSObject ):

    
    
    def __init__(self, context, obj, var_name, can_call = False):
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
            exc = POINTER(c_int)(c_int(0))
            prop = obj.GetProperty( context, var_name_ref, exc)
            self._attributes[var_name.value] =  to_pyvalue(context, prop)
            if self._attributes[var_name.value]:
                print "XXXXXXXX GOT PROP %s: %s"%(var_name.value, self._attributes[var_name.value])
            else:
                print "XXXXXXXX GOT PROP %s: %s"%(var_name.value, exc.contents.value)

                
    def __call__(self, *args):
        
        def to_string(var):
            if isisntance(var, JavascriptClass):
                return var._var_name
            else:
                return str(var)
        if not self._callable:
            raise Exception("Object not callable")
        id = str(cast( self._context._object, c_void_p))
        env = JavascriptClass._python_to_js[id]
        (retval, exc ) = env.execute( self, "try{python.PY_RETURN(%s.%s(%s));}catch(err){python.PY_THROW(err);}"%(self._varname, attr, ",".join([to_string(v) for v in args])) )
        if exc:
            raise exc
        else:
            return retval
        
        
    def __getattr__(self,attr):
        def to_string(var):
            if isisntance(var, JavascriptClass):
                return var._var_name
            else:
                return str(var)
        logging.error("GETTING ATTR %s"%attr)
        if not attr in self._attributes.iterkeys():
            raise Exception("No such method or attribute: %s"%attr)
        val = self._attributes[attr]
        if not val:
            #undefiend type is a function(?) in javascript
            def hooked(*args):
                id = str(cast( self._context._object, c_void_p))
                env = JavascriptClass._python_to_js[id]
                logging.error("EXECUTING %s"%(  "try{python.PY_RETURN(%s.%s(%s));}catch(err){python.PY_THROW(err);}"%(self._varname, attr, ",".join([to_string(v) for v in args]))))
                (retval, exc ) = env.execute( self,  "try{python.PY_RETURN(%s.%s(%s));}catch(err){python.PY_THROW(err);}"%(self._varname, attr, ",".join([to_string(v) for v in args])) )
                logging.error("... %s %s"%(retval, exc))
                if exc:
                    raise exc
                else:
                    return retval
        
            return hooked
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
        self._err = err

        

class ScriptEnv( JavascriptClass ):

    _jsobjects = {}
    _sem = threading.Semaphore()
    
    def __init__( self, context):
        id = str(cast( context._object, c_void_p))
        JavascriptClass._python_to_js[id] = self
        JavascriptClass.__init__(self, context, "python")
        self._context = context
        self._contextid = str(cast(context._object, c_void_p))
        self._exception = None
        self._returnval = None

    def export_to_python( self, jsobj , var_name, can_call = False ):
        logging.error("EXPORT FROM JS")
        ScriptEnv._jsobjects[self._contextid + var_name] = _wrapJs( self._context, jsobj, var_name, can_call )
        
    def PY_RETURN( self, jsobj ):
        logging.error("GOT OBJ %s"%jsobj)
        self._returnval = jsobj
        self._exception = None

    def PY_THROW( self , jserr):
        logging.error("GOT EXC %s"%jserr)
        self._exception =  JSException( jserr )


    def execute( self, source, cmd):
        self._sem.acquire()
        gobject.idle_add(source._webview.execute_script,cmd)
        exc = self._exception
        retval = self._returnval
        self._sem.release()
        return (retval, exc )

    @staticmethod
    def get_jsobject(webview, name , can_call = False):
        context = webview.get_main_frame().get_global_context()
        id = str(cast(context._object, c_void_p))
        if not id in JavascriptClass._python_to_js.iterkeys():
            logging.error("NEW ENV")
            ScriptEnv(context)
        retval =  ScriptEnv._jsobjects.get( id+name)
        
        if retval:
            retval._webview = webview
        else:
            logging.error("NOT FOUND. ATTEMPTING TO EXPORT")
            webview.execute_script,"python.export_to_python(%s,'%s', %s);"%(name, name, can_call)
            retval =  ScriptEnv._jsobjects.get( id+name)
            retval._webview = webview
        logging.error("RETURNING %s"%retval)
        return retval


