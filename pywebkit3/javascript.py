
import inspect
from pywebkit3.javascriptcore import *
from ctypes import *

def strid(obj):
    return str( cast( obj._object, c_void_p))

class JavascriptClass(object):
    """Class instance of which are accessible within a javascript"""

    _methods = None
    _jsobjects = {}
    
    @classmethod
    def _populate(cls):
        JavascriptClass._methods = [m for m in inspect.getmembers(cls, predicate=inspect.ismethod) if not m[0].startswith('_')]
        
    _prefix = ""

    @staticmethod
    def set_jsnaming_conventions(prefix):
        """Set naming convnetions for javascript objects
        created through Python.  The prefix supplied will be
        prepended to all object names of crated objects"""
        _prefix = prefix

    def __init__(self):
        pass

    @classmethod
    def create(cls, context, obj_name, *constructor_args):
        if not cls._methods:
            cls._populate()
        cls.staticmethods = (JSStaticFunction*(len(cls._methods)+2))()
        #tag end:
        cls.staticmethods[-1].name = cast(NULL, c_char_p)
        cls.staticmethods[-1].callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
        cls.staticmethods[-1].attributes = 0
        def call_constructor(ctxt, function,obj, argumentCount, arguments, exception):
            newobj = cls( *constructor_args)
            newobj._javascript_object = obj
            JavascriptClass._jsobjects[strid(obj)] =  newobj
            return obj
        cls.staticmethods[-2].name = c_char_p("%s%s_new"%(cls._prefix,cls.__name__))
        cls.staticmethods[-2].callAsFunction = JSObjectCallAsFunctionCallback(call_constructor)
        cls.staticmethods[-2].attributes = kJSPropertyAttributeReadOnly
        
        for index in xrange(len(JavascriptClass._methods)-1):
            name = JavascriptClass._methods[index][0]
            cls.staticmethods[index].name = c_char_p( name)
            def call_method(ctxt, function, argumentCount, arguments, exception):
                args = []
                for i in xrange(argumentCount):
                    type = JSValue.JSValueGetType( context, arguments[i])
                    if type == kJSTypeNull:
                        args.append[None]
                    elif type == kJSTypeBoolean:
                        args.append[JSValue.JSValueToBoolean( context, arguments[i])]
                    elif type == kJSTypeString:
                        jstext = JSString( JSValue.JSValueToStringCopy( context, arguments[i]))
                        length = JSString.JSStringGetMaximumUTF8CStringSize()
                        cstring = (c_char*(lenght_1))()
                        jstext.JSStringGetUTR8CString( cstring, length )
                        
                        args.append[ cstring.value ]
                    elif type == kJSTypeObject:
                        found = JavascriptClass._jsobjects.get(strid(obj))
                        args.append[ found._javascript_object]
                        if not found:
                            import logging
                            logging.error("Unknown object passed to python frmo javascript. Object must be know in both worlds.")
                            return NULL
                    else:
                        import logging
                        logging.error( "Invalid javascript value")
                        return NULL
                                    
                value =  JavascriptClass._methods[index][1](target, *args)
                import Number
                if isinstance( value, Number):
                    return JSValue.JSValueMakeNumber(context, value)
                elif isinstance( value, str):
                    cstring = c_char_p(value)
                    text = JSString.JSStringCreateWithUTF8CString(cstring);
                    return JSValue.JSValueMakeString(context, text);
                elif isinstance( value, JavascriptClass):
                    return value._javascript_object
            print cls.staticmethod[index].staticFunctions[0]
            raise Exception()
            cls.staticmethods[index].callAsFunction  = JSObjectCallAsFunctionCallback( call_method)
            cls.staticmethods[index].attributes = kJSPropertyAttributeReadOnly
        newobj = None
        def _init_cb( ctxt, obj):
            newobj = cls( *constructor_args)
            newobj._javascript_object = obj
            JavascriptClass._jsobjects[str(cast(obj,c_void_p))] =  newobj
            
        def _finalize_cb(obj):
            index = -1
            pyobj= JavascriptClass._jsobjects.get(strid(obj))
            if pyobj:
                del JavascriptClass._jsobjects[strid(obj)]
            
                
        jscd = JSClassDefinition()
        jscd.version = 0
        jscd.attributes = kJSClassAttributeNone
        jscd.className =c_char_p( cls.__name__) 
        jscd.parentClass = NULL
        jscd.staticValues = POINTER(JSStaticValue)()
        jscd.staticFunctions = cls.staticmethods
        jscd.initialize = JSObjectInitializeCallback (_init_cb)
        jscd.finalize = JSObjectFinalizeCallback ( _finalize_cb)
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
        globalObj = context.GetGlobalObject( )
        text = JSString.CreateWithUTF8CString("%s%s"%(cls._prefix, obj_name))
        globalObj.SetProperty( context,
                               text,
                               obj,
                               kJSPropertyAttributeNone,
                               NULL)
        
        return JavascriptClass._jsobjects[ strid(obj)]




JavascriptClass._populate()
