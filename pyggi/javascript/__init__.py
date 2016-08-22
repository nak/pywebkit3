import logging
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
import collections

document = None
from ctypes import POINTER, c_int
OPAQUE_PTR = POINTER(c_int)

def strid(obj):
    try:
        return str(cast(obj._object(), c_void_p).value)
    except:
        return str(cast(obj._object, c_void_p).value)

def jsEqual(obj1, obj2):
    return cast(obj1._object(), c_void_p).value == cast(obj2._object(), c_void_p).value 

list_of_cfuncs = {}

def to_jsfunction( ctxt, func):
    if func in list_of_cfuncs:
        text = JSString.CreateWithUTF8CString( func.__name__)
        jsobj = JSObject.MakeFunctionWithCallback(ctxt, text, list_of_cfuncs[func][2])
        text.Release()
        return jsobj
    if (not hasattr(func, '__call__')) and func.IsFunction(ctxt):
            func = JSFunction(ctxt, obj=func, thisobj = NULL, name="anon")
    def get_callable( func ):
        def C_Callable( context, function, thisObject,  argumentCount, arguments, exception):
            context = JSContext(obj = context)
            if cast(thisObject, c_void_p).value == None:
                thisObject= NULL#JSObject.MakeNull( context )
                args = []
            else:
                thisObject = JSObject(obj = thisObject, context = context)
                args = [thisObject]
            try:
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
                        return None
                try:
                    retval = func(*args)
                except:
                    import traceback
                    logging.error(traceback.format_exc())
                    retval = None
                    
                if retval == None:
                    retval = JSValue.MakeNull(context)
                elif isinstance(retval, numbers.Number):
                    retval = JSValue.MakeNumber( context, retval)
                elif isinstance(retval, str):
                    cstring = c_char_p(retval)
                    text = JSString.CreateWithUTF8CString(cstring)
                    retval = JSValue.MakeString(context, text);
                    text.Release()
                elif retval in [True, False]:
                    retval = JSValue.MakeBoolean(context, retval)
                assert( isinstance(retval, JSValue))
                #retval.Protect(context)#will go out of scope and underlying object needs to be retained
                retval =  cast(retval._object(), c_void_p)
                return retval.value
            except:
                import traceback
                logging.error(traceback.format_exc())
                logging.error("Error in calling argument function ")
                return None
        return C_Callable
    tocall = get_callable( func )
    tocall.__name__ = func.__name__
    
    cccfunc = JSObjectCallAsFunctionCallback(tocall)
    tocall.cfunc = cccfunc
    text = JSString.CreateWithUTF8CString( func.__name__)
    jsobj = JSObject.MakeFunctionWithCallback(ctxt, text, cccfunc)
    assert (isinstance(jsobj, JSObject))
    list_of_cfuncs[func] = (jsobj,tocall, cccfunc, func)
    text.Release()
    return jsobj



def to_pythonjs( context, val): 
    valtype= val.GetType(context)
    if valtype is None or valtype == kJSTypeNull.value:
        
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
    elif valtype == kJSTypeObject.value or valtype == kJSTypeUndefined.value:
        jsobject = val.ToObject(context, NULL)
        retval = _wrapJs(context, jsobject, None)
    else:
        logging.error("Invalid javascript value type encountered!: %d" % valtype.value)
        retval = None
    return retval
        

class JSFunction(JSObject):

    def __init__(self, context, obj, thisobj, name,
                 _call_as_constructor = False):
        assert(isinstance(context, JSContext))
        JSObject.__init__(self, obj=obj._object(), context = context)
        self._thisjsobj = thisobj
        self._jsfuncobj = obj
        if thisobj and not thisobj._object():
            self._thisjsobj = None
        self._name = name
        self._call_as_constructor = _call_as_constructor

    def promote_to_constructor( self ):
        self._call_as_constructor = True
        
    def __call__(self, *args):
        #We must keep the javascript arguments active while this object is active 
        #and before another call is made to this JSFunction.  We cannot guarentee
        #when the jsFunction will be invoked (CallAsFunction seems to squirrel it 
        #away until it is called).  It is assumed that a second call will be made
        #to the jsfunction by the core engine only when a first call has been fully
        #processed (args will then go away).
        jsArgs = []
        def get_jsobj( arg ):
            if arg is None:
                jsarg = JSValue.MakeNull( self._context )
                
            elif isinstance(arg, numbers.Number):
                jsarg = JSValue.MakeNumber( self._context, arg)
            elif isinstance(arg, str) or isinstance(arg, bytes) or isinstance(arg, bytearray) or isinstance( arg, unicode):

                jsstring = JSString.CreateWithUTF8CString(arg)
                jsarg = JSValue.MakeString(self._context, jsstring)
               
                jsstring.Release()

            elif isinstance( arg, JSObject):
                jsarg = arg

            elif isinstance(arg, collections.Callable):
                jsarg = to_jsfunction(self._context, arg)
                assert(jsarg.IsFunction(self._context))

            elif isinstance( arg, dict):
                text = JSString.CreateWithUTF8CString("{}")#"%s"%dict)
                jsarg =  JSValue.MakeFromJSONString(self._context, text)
                jsarg = jsarg.ToObject(self._context, NULL)
                text.Release()
                for key,value in arg.items():
                    #resucrion here:
                    value = get_jsobj( value)

                    name = JSString.CreateWithUTF8CString( key )
                    jsarg.SetProperty( self._context,
                                       name, 
                                       value,
                                       kJSPropertyAttributeNone,
                                       NULL)
                    name.Release()

            elif hasattr( arg, '__iter__'):
                text = JSString.CreateWithUTF8CString("{}")
                jsarg =JSValue.MakeFromJSONString(self._context, text)
                jsarg = jsarg.ToObject(self._context,NULL)

                text.Release()
                for index,value in enumerate(arg):
                    #recursion here:
                    value = get_jsobj( value)

                    name = JSString.CreateWithUTF8CString( "%d"%index )
                    jsarg.SetProperty( self._context,
                                       name,
                                       value,
                                       kJSPropertyAttributeNone,
                                       NULL)
                    name.Release()


            else:
                raise Exception("Unknown type %s to convert to javascript"%type(arg))
            return jsarg
        for arg in args:
            jsArgs.append( get_jsobj(arg ) )
        if len(jsArgs)==0:
            jsArgs =  NULL
        else:
            jsArgs.append(JSValue.MakeNull(self._context))
        if self._jsfuncobj.IsConstructor( self._context ) and self._call_as_constructor:
            retval =  self._jsfuncobj.CallAsConstructor( self._context,
                                                         c_int(len(args)),
                                                         jsArgs,
                                                         NULL)
        else:
            retval =  self._jsfuncobj.CallAsFunction( self._context,
                                                  self._thisjsobj,
                                                  c_int(len(args)),
                                                  jsArgs,
                                                  NULL)
        retval =   to_pythonjs(self._context, retval)
        
        return retval

        
class JavascriptClass(object):
    """Class instance which is accessible within a javascript script"""
    _methods = None
    _methods_by_name = {}
    _globalobjects = {}
    _constructors = {}

    index = 0
    @classmethod
    def _populate(cls , context, ns, _module):
        """
        Called once per derived class to populate the
        methods made available to javascript
        """
        cls._methods = [m for m in inspect.getmembers(cls, predicate=inspect.ismethod) if not m[0].startswith('_') and not m[0] == 'create' and not m[0] == 'export_class']
        cls.staticmethods = (JSStaticFunction * (len(cls._methods) + 1))()
        #end must be "null"; javascriptcore uses this to determine terminator:
        cls.staticmethods[-1].name = c_char_p()
        cls.staticmethods[-1].callAsFunction = JSObjectCallAsFunctionCallback()
        cls.staticmethods[-1].attributes = 0
        #Function to get a function to cast into javascript callback:
        def getfunc(index):
            def call_method(ctxt, function, obj, argumentCount, arguments, exception):
                try:
                    context = JSContext(obj=ctxt)
                    val = JSObject(obj = obj, context= context)
                    if strid(val) in JavascriptClass._globalobjects:
                        pyobj = JavascriptClass._globalobjects[ strid(val) ]
                    else:
                        pyobj = val
                    #get the method to be called
                    methodname = cls.staticmethods[index].name
                    to_call = cls._methods_by_name.get(methodname)
                    if not to_call:
                        logging.error("Unrecognized method!  Internal error in javascript python binding %s" % methodname)

                    #now loop through arugments and convert
                    #TODO: Handle arrays
                    arguments = cast(arguments, POINTER(OPAQUE_PTR))
                    ctxt = cast(ctxt, OPAQUE_PTR)
                    args = []
                    for i in range(argumentCount):
                        if isinstance(arguments[i], numbers.Number):
                            args.append(arguments[i])
                        else:
                            
                            valtype = JSValue(obj=arguments[i], context = context).GetType(context)#None context here to prevent unprotect on __del__
                            if valtype == kJSTypeNull.value:
                                args.append(None)
                            elif valtype == kJSTypeNumber.value:
                                args.append(JSValue(arguments[i], context = context ).ToNumber(context, NULL))
                            elif valtype == kJSTypeBoolean.value:
                                args.append(JSValue(arguments[i], context = context).ToBoolean(context))
                            elif valtype == kJSTypeString.value:
                                jstext = JSValue(arguments[i], context = context).ToStringCopy(context, NULL)
                                length = jstext.GetMaximumUTF8CStringSize()
                                cstring = (c_char * (length))()
                                
                                jstext.GetUTF8CString(cstring, length)
                                jstext.Release()
                                args.append(cstring.value)
                                del cstring
                            elif valtype == kJSTypeObject.value  or valtype == kJSTypeUndefined.value:
                                jsobject = JSValue(arguments[i], context = context).ToObject(context, NULL)
                                
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
            cls.staticmethods[index].callback_ref = call_method
        def _init_cb(context, obj):
            pass
          
        def _finalize_cb(obj):
            #cleanup if javascript side decides to delete the object:
            logging.error("FINALIZE %s"%obj)
            pass
                

        #create the class definition
        jscd = POINTER(JSClassDefinition)(JSClassDefinition( c_int(0),
                                  kJSClassAttributeNone,
                                  c_char_p(cls.__name__.encode('ascii')),
                                  NULL,
                                  POINTER(JSStaticValue)(),
                                  cls.staticmethods,
                                  {False:JSObjectInitializeCallback (_init_cb) , True: JSObjectInitializeCallback()}[_module is not None],
                                  {False:JSObjectFinalizeCallback (_init_cb) , True: JSObjectFinalizeCallback()}[_module is not None],
                                  JSObjectHasPropertyCallback(),
                                  JSObjectGetPropertyCallback(),
                                  JSObjectSetPropertyCallback(),
                                  JSObjectDeletePropertyCallback(),
                                  JSObjectGetPropertyNamesCallback(),
                                  JSObjectCallAsFunctionCallback(),
                                  JSObjectCallAsConstructorCallback(),
                                  JSObjectHasInstanceCallback(),
                                  JSObjectConvertToTypeCallback()))
        #jscd.argtype = [POINTER(OPAQUE_PTR), POINTER(OPAQUE_PTR)]
        cls._classDef = JSObject.JSClassCreate(jscd)
        #cls._jscd = jscd #don't let it go out of scope!!!
        if not _module:
            if not cls.__name__ in JavascriptClass._constructors and not cls.__name__=="JSContext":
                #export this class  to be visible in javascript namespace
                cls.export_class( context, ns)


    def __init__(self, context, var_name, **kargs):
        assert isinstance(context, JSContext)
        self._context = context

        #see if the module was explcitly called out:
        _module = kargs.get('_module')
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
            assert(str(cast(context._object(), OPAQUE_PTR)) + modulename in iter(Namespace._namespaces.keys()))
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

        JavascriptClass._globalobjects[ strid(self._javascript_obj)] = self
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
               
#    def __del__(self):
#        if hasattr(self, '_varname'):
#            self._env._webview.execute_script("delete %s;" % self._varname)
            
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
            
        Namespace._namespaces[ str(cast(context._object(), OPAQUE_PTR)) + module_name ] = self
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
        id = str(cast(context._object(), OPAQUE_PTR)) + modulename
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
        wrapped = JSFunction(context, obj=jsobj, thisobj = NULL, name = var_name)
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



