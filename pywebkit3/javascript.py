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
        print cls._methods
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
            newobj = cls( *constructor_args)
            newobj._javascript_object = obj
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



