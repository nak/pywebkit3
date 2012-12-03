import pywebkit3.javascriptcore

import inspect
from javascriptcore import *
from ctypes import *
import logging
import traceback
import importlib

def strid(obj):
    return str( cast( obj._object, c_void_p))

class JavascriptClass(object):
    """Class instance of which are accessible within a javascript"""
    _methods = None
    _methods_by_name= {}
    _jsobjects = {}
    _constructors = {}
    
    @classmethod
    def _populate(cls):
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
                            if valtype == kJSTypeNull.value:
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
                                (found,_) = JavascriptClass._jsobjects.get(strid(obj))
                                args.append( found._javascript_obj )
                                if not found:
                                    logging.error("Unknown object passed to python frmo javascript. Object must be know in both worlds.")
                                return NULL
                            else:
                                logging.error( "Invalid javascript value %d"%valtype)
                                return NULL
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
        if not "_module" in kargs.iterkeys():
            _module = None
        else:
            _module = kargs['_module']
        """This should take no parameters, to prevent repercussions throughout hierarchy"""
        cls = self.__class__
        if not isinstance(cls, Namespace) and not cls._methods:
            cls._populate()
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
                
        if not cls._methods:
            cls._populate()

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
    GLOBAL = {}
    global_defined = False
    
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
        return Namespace.get_namespace( context, "")
        
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


def export_module( context, module):
    import importlib
    importlib.import_module( module.__name__)
    if module.__name__ in Namespace._namespaces:
        return
    return Namespace( context, module )
    #class MyNamespace(Namespace):
    #    def __init__(self, context, module):
    #        assert(module)
    #        assert(context)
    #        Namespace.__init__(self, context, module)
    #        
    #module_name = module.__name__.split('.')[-1]
    #MyNamespace.__name__ = module_name
    #return MyNamespace.create(context , None, 
    #                       module_name, context,module)

       
