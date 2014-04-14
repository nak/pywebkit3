from .. import  gobject
from ..gobject import GObject
from ..gtk3 import libgtk3

try:
    test = unicode
except:
    unicode = str
import inspect
import numbers
import threading
from ..javascriptcore import *
from ctypes import *
import logging
import traceback
import importlib
import logging
import collections

document = None

def strid(obj):
    try:
        return str(cast(obj._object(), c_void_p).value)
    except:
        return str(cast(obj._object, c_void_p).value)

def jsEqual(obj1, obj2):
    return cast(obj1._object(), c_void_p).value == cast(obj2._object(), c_void_p).value 

def to_jsfunction( ctxt, func):
    def C_Callable( context, function, thisObject,  argumentCount, arguments, exception):
        context = JSContext(obj = context)
        if cast(thisObject, c_void_p).value == None:
            thisObject= None
        else:
            thisObject = JSObject(obj = thisObject, context = context._object())
        try:
            args = [thisObject]
            for i in range(argumentCount):
                argument = JSValue(obj = arguments[i],
                                   context = context)
                valtype = argument.GetType(context)
                if valtype == kJSTypeObject.value:
                    jsobject = argument.ToObject(context, NULL)
                    pyarg = _wrapJs(context, jsobject, None)
                    #pyarg._javascript_obj = jsobject
                    args.append(pyarg)
                elif valtype == kJSTypeNull.value or valtype == kJSTypeUndefined.value:
                    args.append(None)
                elif valtype == kJSTypeNumber.value:
                    args.append(argument.ToNumber(context, NULL))
                elif valtype == kJSTypeBoolean.value:
                    args.append(argument.ToBoolean(context))
                elif valtype == kJSTypeString.value:
                    jstext = argument.ToStringCopy(context, NULL)
                    length = jstext.GetMaximumUTF8CStringSize()
                    cstring = (c_char * (length))()
                    jstext.GetUTF8CString(cstring, length)
                    jstext.Release()
                    args.append(cstring.value)
                else:
                    logging.error("Invalid javascript value type encountered!: %d" % valtype)
                    return c_longlong(0)
            assert(len(args) == argumentCount +1)
            try:
                if len(args) >=1:
                    args2 = args[1:]
                else:
                    args2 = args
                retval = func(None, None)#func(*args2)
            except TypeError:
                try:
                    retval = func(None,None)#*args)
                except:
                    import traceback
                    import logging
                    logging.error(traceback.format_exc())
            except:
                import traceback
                import logging
                logging.error(traceback.format_exc())
                
            if retval == None:
                retval = JSValue.MakeNull(context)
            elif isinstance(retval, numbers.Number):
                retval = JSValue.MakeNumber( context, retval)
            elif isinstance(retval, str):
                cstring = c_char_p(retval)
                text = JSString.CreateWithUTF8String(cstring)
                retval = JSValue.MakeString(context, text);
                text.Release()
            elif retval in [True, False]:
                retval = JSValue.MakeBoolean(context, retval)
            assert( isinstance(retval, JSValue))
            #retval.Protect(context)#will go out of scope and underlying object needs to be retained
            retval =  cast(byref(retval._object()),POINTER(c_longlong)).contents
            return retval.value
        except:
            import traceback
            import logging
            logging.error(traceback.format_exc())
            logging.error("Error in calling argument function ")
            return 0
    cfunc = JSObjectCallAsFunctionCallback(C_Callable)
    jsobj = JSObject.MakeFunctionWithCallback(ctxt, NULL, cfunc)
    assert ( not cast(jsobj._object(),c_void_p).value == None)
    jsobj._callable = cfunc
    jsobj._func = func
    return jsobj



def to_pythonjs( context, val): 
    valtype= val.GetType(context)
    if valtype == kJSTypeNull.value or valtype == kJSTypeUndefined.value:
        return None
    elif valtype == kJSTypeNumber.value:
        retval = val.ToNumber(context, NULL)
    elif valtype == kJSTypeBoolean.value:
        retval = val.ToBoolean(context)
    elif valtype == kJSTypeString.value:
        jstext = val.ToStringCopy(context, NULL)
        length = jstext.GetMaximumUTF8CStringSize()
        cstring = (c_char * (length))()
        jstext.GetUTF8CString(cstring, length)
        jstext.Release()
        retval = cstring.value.decode('ascii')
        del cstring
    elif valtype == kJSTypeObject.value:
        jsobject = val.ToObject(context, NULL)
        retval = _wrapJs(context, jsobject, None)
    else:
        logging.error("Invalid javascript value type encountered!: %d" % valtype)
        retval = None
    return retval
        

class JSFunction(JSObject):

    def __init__(self, context, obj, thisobj, name):
        assert(isinstance(context, JSContext))
        JSObject.__init__(self, obj=obj._object(), context = context)
        self._thisjsobj = thisobj
        self._jsfuncobj = obj
        if thisobj and cast(thisobj._object(), c_void_p ).value == None:
            self._thisjsobj = None
        self._name = name
        
    def __call__(self, *args):
        #We must keep the javascript arguments active while this object is active 
        #and before another call is made to this JSFunction.  We cannot guarentee
        #when the jsFunction will be invoked (CallAsFunction seems to squirrel it 
        #away until it is called).  It is assumed that a second call will be made
        #to the jsfunction by the core engine only when a first call has been fully
        #processed (args will then go away).
        jsArgs = []
        for arg in args:
            if isinstance(arg, numbers.Number):
                jsarg = JSValue.MakeNumber( self._context, arg)
                
            elif isinstance(arg, str) or isinstance(arg, bytes) or isinstance(arg, bytearray) or isinstance( arg, unicode):
                jsstring = JSString.CreateWithUTF8CString(arg)
                jsarg = JSValue.MakeString(self._context, jsstring)
                ##according to doc, arg now retains the string, but memory leak ensues if we don't do this??
                jsstring.Release()
            elif isinstance( arg, JSObject):
                jsarg = arg
            elif isinstance(arg, collections.Callable):
                jsarg = to_jsfunction(self._context, arg)
                assert(jsarg.IsFunction(self._context))
            elif isinstance( arg, dict):
                this = self
                class Arg(JavascriptClass):
                    def __init__(self, context):
                        #JavascriptClass.__init__(self, context, "tmpjs%d"%len(this._jsArgs))
                
                        for key,value in arg.items( ):
                            if isinstance(value, collections.Callable):
                                value = to_jsfunction(this._context, value)
                            setattr(self, key, value)
                                
                jsarg = Arg()._javascript_obj
            elif arg is None:
                jsarg =  JSObject(NULL )
            else:
                import logging
                logging.error("ARG UNKNOWN %s"%type(arg))
            jsArgs.append( jsarg )
        if len(jsArgs)==0:
            jsArgs = NULL
        import logging
        retval =  self._jsfuncobj.CallAsFunction( self._context,
                                                  self._thisjsobj,
                                                  c_int(len(args)),
                                                  jsArgs,
                                                  NULL)
        if cast( retval._object(), c_void_p).value == None:
            return None
        return  to_pythonjs(self._context, retval)


        
class JavascriptClass(object):
    """Class instance which is accessible within a javascript script"""
    _methods = None
    _methods_by_name = {}
    _globalobjects = {}
    _constructors = {}

    @classmethod
    def _populate(cls , context, ns, _module):
        """
        Called once per derived class to populate the
        methods made available to javascript
        """
        cls._methods = [m for m in inspect.getmembers(cls, predicate=inspect.ismethod) if not m[0].startswith('_') and not m[0] == 'create']
        cls.staticmethods = (JSStaticFunction * (len(cls._methods) + 1))()
        #end must be "null"; javascriptcore uses this to determine terminator:
        cls.staticmethods[-1].name = cast(NULL, c_char_p)
        cls.staticmethods[-1].callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
        cls.staticmethods[-1].attributes = 0
        #Function to get a function to cast into javascript callback:
        def getfunc(index):
            def call_method(ctxt, function, obj, argumentCount, arguments, exception):
                try:
                    context = JSContext(obj=ctxt)
                    val = JSObject(obj = obj, context= ctxt)
                    pyobj = context._jsobjects[ strid(val) ]
                    #get the method to be called
                    methodname = cls.staticmethods[index].name
                    to_call = cls._methods_by_name.get(methodname)
                    if not to_call:
                        logging.error("Unrecognized method!  Internal error in javascript python binding %s" % methodname)

                    #now loop through arugments and convert
                    #TODO: Handle arrays
                    arguments = cast(arguments, POINTER(POINTER(c_int)))
                    ctxt = cast(ctxt, POINTER(c_int))
                    args = []
                    for i in range(argumentCount):
                        if isinstance(arguments[i], numbers.Number):
                            args.append(arguments[i])
                        else:
                            
                            valtype = JSValue(obj=arguments[i], context = ctxt).GetType(context)#None context here to prevent unprotect on __del__
                            if valtype == kJSTypeNull.value or valtype == kJSTypeUndefined.value:
                                args.append(None)
                            elif valtype == kJSTypeNumber.value:
                                args.append(JSValue(arguments[i], context = ctxt ).ToNumber(context, NULL))
                            elif valtype == kJSTypeBoolean.value:
                                args.append(JSValue(arguments[i], context = ctxt).ToBoolean(context))
                            elif valtype == kJSTypeString.value:
                                jstext = JSValue(arguments[i], context = ctxt).ToStringCopy(context, NULL)
                                length = jstext.GetMaximumUTF8CStringSize()
                                cstring = (c_char * (length))()
                                
                                jstext.GetUTF8CString(cstring, length)
                                jstext.Release()
                                args.append(cstring.value)
                                del cstring
                            elif valtype == kJSTypeObject.value:
                                jsobject = JSValue(arguments[i], context = ctxt).ToObject(context, NULL)
                                
                                pyarg = _wrapJs(context, jsobject, "arg%s" % i)
                              
                                #pyarg._javascript_obj = jsobject
                                args.append(pyarg)
                            else:
                                logging.error("Invalid javascript value type encountered!: %d" % valtype)
                                return 0
                    assert(len(args) == argumentCount)
                    #make the call:
                    value = to_call[1](pyobj, *args)
                    #now convert the return value to something pythonic:
                    if isinstance(value, numbers.Number):
                        retval = JSValue.MakeNumber(context, value)
                    elif isinstance(value, str):
                        cstring = c_char_p(value)
                        text = JSString.CreateWithUTF8CString(cstring);
                        retval = JSValue.MakeString(context, text)
                        text.Release()
                        del cstring
                    elif isinstance(value, JSObject):
                        retval = value
                    elif isinstance(value, JavascriptClass):
                        retval = JSObject(obj  = value._javascript_obj._object(), context = context  )
                    else:
                        retval = NULL
                        return cast(byref(retval), POINTER(c_longlong)).contents.value
                    #retval.Protect(context)
                    retval = cast(byref(retval._object()), POINTER(c_longlong)).contents
                    
                except:
                    logging.error("EXCEPTION calling python method from javascript:")
                    logging.error(traceback.format_exc()) 
                    return 0#NULL
                return retval.value
                
            return call_method

        #poptulate all the classmethods into the javascript
        #class definition structure:
        for index in range(len(cls._methods)):
            name = cls._methods[index][0]
            call_method = getfunc(index)
            cls.staticmethods[index].name = c_char_p(name)
            cls.staticmethods[index].callAsFunction = JSObjectCallAsFunctionCallback(call_method)
            cls.staticmethods[index].attributes = kJSPropertyAttributeReadOnly           
            cls._methods_by_name[cls.staticmethods[index].name] = cls._methods[index]        
            
        def _init_cb(context, obj):
            pass
          
        def _finalize_cb(obj):
            #cleanup if javascript side decides to delete the object:
            logging.error("FINALIZ %s"%obj)
            pass
                

        #create the class definition
        jscd = JSClassDefinition()
        jscd.version = 0
        jscd.attributes = kJSClassAttributeNone
        jscd.className = c_char_p(cls.__name__) 
        jscd.parentClass = NULL
        jscd.staticValues = POINTER(JSStaticValue)()
        jscd.staticFunctions = cls.staticmethods
        if not _module:
            jscd.initialize = JSObjectInitializeCallback (_init_cb)
            jscd.finalize = JSObjectFinalizeCallback (_finalize_cb)
        else:
            jscd.initialize = cast(NULL, JSObjectInitializeCallback)
            jscd.finalize = cast(NULL, JSObjectFinalizeCallback)
           
        jscd.hasProperty = cast(NULL, JSObjectHasPropertyCallback)
        jscd.getProperty = cast(NULL, JSObjectGetPropertyCallback)
        jscd.setPrpoerty = cast(NULL, JSObjectSetPropertyCallback)
        jscd.deleteProprety = cast(NULL, JSObjectDeletePropertyCallback)
        jscd.getPropertyName = cast(NULL, JSObjectGetPropertyNamesCallback)
        jscd.callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
        jscd.callAsConstructor = cast(NULL, JSObjectCallAsConstructorCallback)
        jscd.hasInstance = cast(NULL, JSObjectHasInstanceCallback)
        jscd.convertToType = cast(NULL, JSObjectConvertToTypeCallback)
        jscd.argtype = [POINTER(c_int), POINTER(c_int)]
        cls._classDef = JSObject.JSClassCreate(byref(jscd))
        cls._jscd = jscd #don't let it go out of scope!!!
        if not _module:
            if not cls.__name__ in JavascriptClass._constructors and not cls.__name__=="JSContext":
                #export this class  to be visible in javascript namespace
                cls.export_class( context, ns)


    def __init__(self, context, var_name, **kargs):
        assert isinstance(context, JSContext)

        #see if the module was explcitly called out:
        self._context = context
        if not "_module" in iter(kargs.keys()):
            _module = None
        else:
            _module = kargs['_module']
        self._varname = var_name
        if not _module:
            try:
                #if module not explicit, determine it here:
                if var_name.find('.') >= 0:
                    modulename = ".".join(var_name.split(".")[:-1])
                else:
                    #Oooh!  global namespace
                    modulename = ""
            except:
                modulename = None
        else:
            if isinstance(self, Constructor):                    
                modulename = _module.__name__
            else:
                modulename = '.'.join(_module.__name__.split('.')[:-1])

        
        """This should take no parameters, to prevent repercussions throughout hierarchy"""
        cls = self.__class__
           
        
             
        if modulename:
            #if we determined a module name, get/create the namespace
            #associated with it
            ns = Namespace.get_namespace( context, modulename)
            assert(ns)
            assert(str(cast(context._object(), c_void_p)) + modulename in iter(Namespace._namespaces.keys()))
        else:
            if var_name and modulename == "":
                #have global namespace:
                ns = Namespace.get_global( context )                
                assert(ns)
                #now make the object and squirrel it away:
                #self._javascript_obj = JSObject.Make( context, cls._classDef, None )   
            else:
                ns = None
                #self._javascript_obj = None

        cls._populate( context , ns, _module)

        if ns:
            name = ns.get_name() + "." + var_name.split('.')[-1]
        else:
            name = "__global.%s" % var_name.split('.')[-1]
            
        if not modulename:
            if var_name and modulename == "":
                #now make the object and squirrel it away:
                self._javascript_obj = JSObject.Make( context, cls._classDef, None)   
            elif var_name == "":
                #have no namespace.  This should only happen
                #if the object self is itself the global namespace
                self._javascript_obj = context.GetGlobalObject()
        else:
            self._javascript_obj = JSObject.Make( context, cls._classDef, None)  

        context._jsobjects[ strid(self._javascript_obj)] = self
        #self._javascript_obj.Protect( context)
        if ns and self._javascript_obj:
            #if not global namespace, add javascript namespace object
            #explicitly to ns
            text = JSString.CreateWithUTF8CString(var_name.split('.')[-1])
            ns._javascript_obj.SetProperty( context,
                                            text,
                                            self._javascript_obj,
                                            kJSPropertyAttributeNone,
                                            NULL)
            
            text.Release()
               
    def __del__(self):
        if hasattr(self, '_varname'):
            self._env._webview.execute_script("delete %s;" % self._varname)
            
    @classmethod
    def export_class(cls, context , ns):
        """Export a class to be visible within javascript"""
        assert(isinstance(context, JSContext))
        if not issubclass(cls, Constructor) and not cls.__name__ in iter(JavascriptClass._constructors.keys()):
            js_constructor = JavascriptClass.get_constructor(cls, context, ns)
            text = JSString.CreateWithUTF8CString("%s" % (cls.__name__.split('.')[-1]))
            JavascriptClass._constructors[cls.__name__] = js_constructor
            text.Release()

    @staticmethod
    def get_constructor(pyclass, context, namespace):
        if namespace == None:
            namespace = Namespace.get_namespace(context, "")#global
        assert(isinstance(namespace, Namespace))
        pyclass._constructor = Constructor
        retval = pyclass._constructor(pyclass, context, namespace)
        return retval



class Constructor(JavascriptClass):

    def __init__(self, pyclass, context, namespace):
        pymodule = importlib.import_module(pyclass.__module__)
        JavascriptClass.__init__(self, context,
                                 var_name="%s" % pyclass.__name__,
                                 _module=pymodule)
        self._pyclass = pyclass
        self._context = context

    def new_(self, *args):
        """
        The constructor is an object (class) available in javascript, with a "._new"
        method for creating instance (an underlying python instance, acutally) from
        within javascript
        """
        try:
            return self._pyclass(self._context, *args)
        except:
            logging.error("Exception instantiating %s" % self._pyclass)
            logging.error(traceback.format_exc())
            return None
        
class Namespace(JavascriptClass):

    _namespaces = {}
    
    def __init__(self, context, module):
        assert(isinstance(context, JSContext))
        module_name = module.__name__ if module else ""
        self._context = context
        self._module = module
        if module_name == "__main__":
            module_name = ""
        self._name = module_name
        
        if module and module_name != "": 
            module_name = module.__name__
            JavascriptClass.__init__(self, context, module_name , _module=module)
        else:
            #if global namespace, do not call base class __init__ (infinite recurion),
            #but set necessary properties explicitly
            module_name = ""
            self._context = context
            self._javascript_obj = context.GetGlobalObject()
            
        Namespace._namespaces[ str(cast(context._object(), c_void_p)) + module_name ] = self
        if module and module_name != "":
            self._export_classes()
        
    def get_name(self):
        return self._name
    
    def _export_classes(self):
        """
        Export all classes from the python module associated
        with this namespace
        """
        for name, obj in inspect.getmembers(self._module):
            if inspect.isclass(obj) and issubclass(obj, JavascriptClass) and \
                   not issubclass(obj, Namespace) and not obj == JavascriptClass:
                
                self._add_child_class(obj)
        
            
    @staticmethod
    def get_namespace(context, modulename):
        """
        Get or create the namespace for the given module name
        """
        assert(isinstance(context, JSContext))
        id = str(cast(context._object(), c_void_p)) + modulename
        if not id in iter(Namespace._namespaces.keys()):
            if modulename:
                m = importlib.import_module(modulename)
                Namespace._namespaces[id] = Namespace(context, m)
            else:
                Namespace._namespaces[id] = Namespace(context, None)
        return Namespace._namespaces[id]
    
    @staticmethod
    def get_global( context ):
        """
        Get or create the global namespace
        """
        assert(isinstance(context, JSContext))
        ns = Namespace.get_namespace(context, "")
        return ns
        
    @staticmethod
    def add_global_class(context, pyclass , *args):
        """
        Add a python class to be accessible at global level
        in javascript
        """
        assert(isinstance(context, JSContext))
        pyclass.export_class(env, Namespace.get_global( context))
        
    def _add_child_class(self, cls):
        """Add a child class to this namespace, avaiable in js"""
        cls.export_class(self._context, self)




def _wrapJs(context, jsobj, var_name):
    """
    Wrap a provided js object as a python object, with a given
    js name.  Can set a flag if js object is callable to make
    it callable in python too.  This is to be used only internally
    """
    assert(isinstance(context, JSContext))
    if jsobj.IsFunction(context):
        wrapped = JSFunction(context, obj=jsobj, thisobj = None, name = var_name)
    else:
        wrapped = jsobj#PythonWrapper(context, jsobj, var_name, can_call)
    return wrapped
    

               
     
        
def export_module( context, module):
    """Export a python module and all JavascriptClass derived
    subclasses to javascript execution environment
    """
    assert(isinstance(context, JSContext))
    import importlib
    importlib.import_module(module.__name__)
    if module.__name__ in Namespace._namespaces:
        return
    return Namespace(context, module)



