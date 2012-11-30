import pywebkit3.javascriptcore

import inspect
from javascriptcore import *
from ctypes import *
import logging
import traceback
            
def strid(obj):
    return str( cast( obj._object, c_void_p))

class JavascriptClass(object):
    """Class instance of which are accessible within a javascript"""
    _methods = None
    _methods_by_name= {}
    _jsobjects = {}

    
    @classmethod
    def _populate(cls):
        cls._methods = [m for m in inspect.getmembers(cls, predicate=inspect.ismethod) if not m[0].startswith('_') and not m[0] == 'create']
        

    def __init__(self):
        """This should take no parameters, to prevent repercussions throughout hierarchy"""
        pass

    @classmethod
    def create(cls, context, namespace, obj_name, *constructor_args):
        logging.error("#######CREATING %s %s"%(namespace.__class__, [a for a in constructor_args]))
        assert( not namespace or isinstance(namespace, Namespace))
        if namespace:
            assert(namespace._javascript_object)
        if not cls._methods:
            cls._populate()
        cls.staticmethods = (JSStaticFunction*(len(cls._methods)+1))()
        #tag end:
        cls.staticmethods[-1].name = cast(NULL, c_char_p)
        cls.staticmethods[-1].callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
        cls.staticmethods[-1].attributes = 0
        def getfunc(index):
            def call_method(ctxt, function, obj, argumentCount, arguments, exception):
                pyobj = JavascriptClass._jsobjects[ str(cast(obj, c_void_p))]
                method = cast(function, c_void_p)
                key = cls.staticmethods[index].name
                to_call = cls._methods_by_name.get(key)
                if not to_call:
                    loggin.error("Unrecognized method!  Internal error in javascript python binding %s"%key)
                try:
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
                                found = JavascriptClass._jsobjects.get(strid(obj))
                                args.append( found._javascript_object )
                                if not found:
                                    logging.error("Unknown object passed to python frmo javascript. Object must be know in both worlds.")
                                return NULL
                            else:
                                logging.error( "Invalid javascript value %d"%valtype)
                                return NULL
                    target = JavascriptClass._jsobjects.get(str(cast(obj, c_void_p)))
                    import numbers
                    assert(not isinstance(pyobj, numbers.Number))
                    value =  to_call[1]( pyobj, *args )
                    import numbers
                    if isinstance( value, numbers.Number):
                        retval= JSValue.MakeNumber(context, value)._object
                    elif isinstance( value, str):
                        cstring = c_char_p(value)
                        text = JSString.CreateWithUTF8CString(cstring);
                        retval = JSValue.JSValueMakeString(context, text)._object;
                    elif isinstance( value, JavascriptClass):
                        retval = value._javascript_object
                    else:
                        retval = NULL
                    retvalp = cast(byref(retval), POINTER(c_longlong))
                    return retvalp.contents.value
                except:
                    logging.error("EXCEPTION: calling python method from javascript")
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
        newobj = None
        def _init_cb( ctxt, obj):
            print "ARGS: %s %s"%(cls.__name__, [a for a in constructor_args])
            newobj = cls( *constructor_args)
            newobj._javascript_object = obj
            if isinstance(newobj, Namespace):
                newobj._export_classes()
            JavascriptClass._jsobjects[str(cast(obj,c_void_p))] =  newobj
          
        def _finalize_cb(obj):
            index = -1
            
            pyobj= JavascriptClass._jsobjects.get(str(cast(obj,c_void_p)))
            if pyobj:
                del JavascriptClass._jsobjects[str(cast(obj,c_void_p))]
            
                
        jscd = JSClassDefinition()
        jscd.version = 0
        jscd.attributes = kJSClassAttributeNone
        jscd.className =c_char_p( cls.__name__) 
        jscd.parentClass = NULL
        jscd.staticValues = POINTER(JSStaticValue)()
        jscd.staticFunctions = cls.staticmethods
        if True or namespace:
            jscd.initialize = JSObjectInitializeCallback (_init_cb)
            jscd.finalize = JSObjectFinalizeCallback ( _finalize_cb)
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
        obj = JSObject.Make( context, classDef, None )
        if not namespace:
            
            id = ""
            if not JavascriptClass._jsobjects.get(id):                
                JavascriptClass._jsobjects[id] = context.GetGlobalObject()
            parentObj = JavascriptClass._jsobjects[id] 
        else:
            parentObj = JSObject(namespace._javascript_object)
            id = strid(obj)
        text = JSString.CreateWithUTF8CString("%s"%( obj_name))
        parentObj.SetProperty( context,
                               text,
                               obj,
                               kJSPropertyAttributeNone,
                               NULL)
        if id == "":
            JavascriptClass._jsobjects[str(cast(parentObj._object,c_void_p))] = parentObj
            return parentObj
        return JavascriptClass._jsobjects[ id ]

    @staticmethod
    def get_constructor( pyclass, context, namespace):
        class Constructor(_Constructor):

            def __init__(self, pyclass, context, namespace):
                JavascriptClass.__init__(self)
                self._pyclass = pyclass
                import numbers
                assert (not isinstance(context, numbers.Number))
                self._context = context
        
            def new_( self, name, *args):
                return self._pyclass.create( self._context, namespace, name, *args)
        assert(isinstance(namespace,Namespace))
        retval = Constructor(pyclass, context, namespace)
        retval.__name__ = pyclass.__name__ +"_Constructor"
        return retval


class _Constructor(JavascriptClass):

    pass


class Namespace( JavascriptClass ):

    _namespaces = {}
    GLOBAL = {}
    global_defined = False
    
    def __init__(self, context, module ):
        assert(context)
        self._context = context
        self._module = module
        if module:
            parent_module_name = ".".join( module.__name__.split('.')[:-1])
            if parent_module_name and  Namespace._namespaces.has_key( parent_module_name):
                parent = Namespace._namespaces[ parent_module_name ]
            elif parent_module_name:
                import importlib
                parent_module = importlib.import_module( parent_module_name )  
                parent = Namespace( context, parent_module)
            else:
                if not Namespace.GLOBAL.get(str(cast(context._object,c_void_p))):
                    Namespace.GLOBAL[ str(cast(context._object, c_void_p))] = \
                       Namespace( context, None)  
                parent = Namespace.GLOBAL[str(cast(context._object, c_void_p))]
            parent._add_child_package(  module.__name__.split('.')[-1])
        else:
            self._parentobj = context.GetGlobalObject( )
            self._javascript_object = self._parentobj
            parent = None
        if module: 
            module_name = module.__name__.split('.')[-1]
        else:
            module_name = ""
        Namespace._namespaces[ module_name ] = self

    def _export_classes(self):
        import inspect
        for name, obj in inspect.getmembers(self._module):
            if inspect.isclass(obj) and issubclass(obj, JavascriptClass) and \
                   not issubclass(obj, Namespace ) and not obj==JavascriptClass:
                
                self._add_child_class(  obj)
        for name in dir(self._module):
            import importlib
            try:
                m = importlib.importmodule( sef_module.__name__ + "." + name)
                if inspect.ismodule(m):
                    self._add_child_package(name)
                    export_module( self._context, m)
            except:
                pass
    @staticmethod
    def add_global_class( context, pyclass , *args):
        if not Namespace.GLOBAL.get(str(cast(context._object, c_void_p))):
            Namespace.GLOBAL[ str(cast(context._object, c_void_p))] = \
                           Namespace( context, None)  
                           
        constructor = JavascriptClass.get_constructor( pyclass, context, namespace = Namespace.GLOBAL[str(cast(context._object, c_void_p))])
        constructor.create(  context, Namespace.GLOBAL[str(cast(context._object, c_void_p))], pyclass.__name__,pyclass, context,  Namespace.GLOBAL[ str(cast(context._object, c_void_p))] )
        
    def _add_child_class(self,  cls):
        constructor = JavascriptClass.get_constructor(cls, self._context, self)
        constructor.create(  self._context, self, cls.__name__, cls, self._context,  self, )

    def _add_child_package( self, name ):
        jscd = JSClassDefinition()
        jscd.version = 0
        jscd.attributes = kJSClassAttributeNone
        jscd.className =c_char_p( name) 
        jscd.parentClass = NULL
        jscd.staticValues = POINTER(JSStaticValue)()
        jscd.staticFunctions = POINTER(JSStaticFunction)()
        jscd.initialize = cast(NULL, JSObjectInitializeCallback)
        jscd.finalize = cast(NULL, JSObjectFinalizeCallback)
        jscd.hasProperty = cast(NULL,JSObjectHasPropertyCallback)
        jscd.getProperty = cast(NULL,JSObjectGetPropertyCallback)
        jscd.setPrpoerty = cast(NULL,JSObjectSetPropertyCallback)
        jscd.deleteProprety = cast(NULL,JSObjectDeletePropertyCallback)
        jscd.getPropertyName = cast(NULL, JSObjectGetPropertyNamesCallback)
        jscd.callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
        jscd.callAsConstructor = cast(NULL,JSObjectCallAsConstructorCallback)
        jscd.hasInstance = cast(NULL,JSObjectHasInstanceCallback)
        jscd.convertToType = cast(NULL, JSObjectConvertToTypeCallback)
        classDef = JSObject.JSClassCreate( byref(jscd) )
        self._javascript_obj = JSObject.Make( self._context, classDef, None )
        text = JSString.CreateWithUTF8CString(name)
        JavascriptClass._jsobjects[str(cast(self._javascript_obj._object, c_void_p))] = self._javascript_obj
        "CREATED NEW SUBMOD %s"%name
        self._parentobj.SetProperty( self._context,
                                     text,
                                     self._javascript_obj,
                                     kJSPropertyAttributeNone,
                                     NULL)

def _wrap(context, pyobj, obj_name):
    import importlib
    if pyobj.__module__:
        module = importlib.import_module(pyobj.__module__)
        export_module( context, module)
    cls = pyobj.__class__
    class PythonToJSWrapper(cls, JavascriptClass):

        def __init__(self,wrapped_class):
            self.wrapped_class = wrapped_class()
            
    
        def __getattr__(self,attr):
            orig_attr = self.wrapped_class.__getattribute__(attr)
            if callable(orig_attr):
                def hooked(*args, **kwargs):
                    self.pre()
                    result = orig_attr(*args, **kwargs)
                    self.post()
                    return result
                return hooked
            else:
                return orig_attr
            
    PythonToJSWrapper.__name__ = cls.__name__
    PythonToJSWrapper.create(context, namespace, obj_name, pyobj)
    return PythonToJSWrapper

def export_module( context, module):
    import importlib
    importlib.import_module( module.__name__)
    if module.__name__ in Namespace._namespaces:
        return
    class MyNamespace(Namespace):
        def __init__(self, context, module):
            assert(module)
            assert(context)
            Namespace.__init__(self, context, module)
            
    module_name = module.__name__.split('.')[-1]
    MyNamespace.__name__ = module_name
    MyNamespace.create(context , None, 
                           module_name, context,module)

         

                
            
