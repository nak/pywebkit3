from .. import  gobject
from ..gobject import GObject
from ..gtk3 import libgtk3

import inspect
import numbers
import threading
from ..javascriptcore import *
from ctypes import *
import logging
import traceback
import importlib
import logging

document = None

def strid(obj):
    return str(cast(obj._object, c_void_p).value)

def jsEqual(obj1, obj2):
    return cast(obj1._object, c_void_p).value == cast(obj2._object, c_void_p).value 

funccount = 0
def to_jsfunction(env, func):
    global funccount
    def C_Callable( context, function, thisObject,  argumentCount, arguments, exception):
        context = JSObject(obj = context, context = None)
        if cast(thisObject, c_void_p).value == None:
            thisObject= None
        else:
            thisObject = JSObject(obj = thisObject, context = context._object)
        try:
            args = []
            for i in xrange(argumentCount):
                argument = JSValue(obj = arguments[i], context = context._object)
                valtype = argument.GetType(context)
                if valtype == kJSTypeObject.value:
                    jsobject = argument.ToObject(context, NULL)
                    can_call = jsobject.IsFunction(context)
                    pyarg = _wrapJs(env, jsobject, None, can_call=can_call)
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
            assert(len(args) == argumentCount)
            
            retval = func(*args)
            del args
            
            if retval == None:
                retval = JSValue.MakeNull(context)
            elif isinstance(retval, numbers.Number):
                retval = JSValue.MakeNumber( context, retval)
            elif isinstance(retval, str):
                cstring = c_char_p(retval)
                retval = JSValue.MakeString(context, text);
                #text.Release()
            elif retval in [True, False]:
                retval = JSValue.MakeBoolean(context, retval)
            assert( isinstance(retval, JSValue))
            #retval.Protect(context)#will go out of scope and underlying object needs to be retained
            retval =  cast(byref(retval._object),POINTER(c_longlong)).contents
            return retval.value
        except:
            logging.error(traceback.format_exc())
            logging.error("Error in calling argument function ")
            return 0
    cfunc = JSObjectCallAsFunctionCallback(C_Callable)
    jsobj = JSObject.MakeFunctionWithCallback(env._context, NULL, cfunc)
    assert ( not cast(jsobj._object,c_void_p).value == None)
    jsobj._callable = cfunc
    return jsobj



def to_pythonjs( env, val): 
    context = env._context
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
        retval = cstring.value
        del cstring
    elif valtype == kJSTypeObject.value:
        jsobject = val.ToObject(context, NULL)
        can_call = jsobject.IsFunction(context)
        pyarg = _wrapJs(env, jsobject, None, can_call=can_call)
        retval = pyarg
    else:
        logging.error("Invalid javascript value type encountered!: %d" % valtype)
        retval = None
    return retval
        

class JSFunction(JSObject):

    def __init__(self, env, obj, thisobj, name):
        JSObject.__init__(self, obj=obj._object, context = env._context._object)
        self._thisjsobj = thisobj
        self._jsfuncobj = obj
        if thisobj and cast(thisobj._object, c_void_p ).value == None:
            self._thisjsobj = None
        self._env  = env
        self._callable = None
        self._name = name
        self._count = 0
        self._jsArgs = []
        
    def __call__(self, *args):
        #We must keep the javascript arguments active while this object is active 
        #and before another call is made to this JSFunction.  We cannot guarentee
        #when the jsFunction will be invoked (CallAsFunction seems to squirrel it 
        #away until it is called).  It is assumed that a second call will be made
        #to the jsfunction by the core engine only when a first call has been fully
        #processed (args will then go away).  
        self._jsArgs = []
        self._count += 1
            
        for arg in args:
            if isinstance(arg, numbers.Number):
                jsarg = JSValue.MakeNumber( self._env._context, arg)
            elif isinstance(arg, str):
                cstring = c_char_p(arg)
                jsstring = JSString.CreateWithUTF8CString(cstring)
                jsarg = JSValue.MakeString(self._env._context, jsstring)
                ##according to doc, arg now retains the string, but memory leak ensues if we don't do this??
                jsstring.Release()
                del cstring
            elif isinstance( arg, JSObject):
                jsarg = arg
            elif callable(arg):
                jsarg = to_jsfunction(self._env, arg)
                assert(jsarg.IsFunction(self._env._context))
                self._callable = arg#must maintain this to prevent from going out of scope!!
            
            self._jsArgs.append( jsarg )
        if len(self._jsArgs)==0:
            self._jsArgs = NULL
        
        retval =  self._jsfuncobj.CallAsFunction( self._env._context, self._thisjsobj,
                                        c_int(len(args)),
                                        self._jsArgs,
                                        NULL)
        if cast( retval._object, c_void_p).value == None:
            return None
        return  to_pythonjs(self._env, retval)


        
class JavascriptClass(object):
    """Class instance of which are accessible within a javascript"""
    _methods = None
    _methods_by_name = {}
    _globalobjects = {}
    _constructors = {}

    @classmethod
    def _populate(cls , env, ns, _module):
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
                    pyobj = env._jsobjects[ strid(val) ]
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
                    for i in xrange(argumentCount):
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
                                can_call = jsobject.IsFunction(context)
                                
                                pyarg = _wrapJs(env, jsobject, "arg%s" % i, can_call=can_call)
                              
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
                        retval = JSObject(obj  = value._javascript_obj._object, context = context._object)
                    else:
                        retval = NULL
                        return cast(byref(retval), POINTER(c_longlong)).contents.value
                    retval.Protect(context)
                    retval = cast(byref(retval._object), POINTER(c_longlong)).contents
                    
                except:
                    logging.error("EXCEPTION calling python method from javascript:")
                    logging.error(traceback.format_exc()) 
                    return 0#NULL
                return retval.value
                
            return call_method

        #poptulate all the classmethods into the javascript
        #class definition structure:
        for index in xrange(len(cls._methods)):
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
            if not cls.__name__ in JavascriptClass._constructors and not cls.__name__=="ScriptEnv":
                #export this class  to be visible in javascript namespace
                cls.export_class(env, ns)


    def __init__(self, env, var_name, **kargs):
        assert isinstance(env, ScriptEnv)

        #see if the module was explcitly called out:
        self._env = env
        if not "_module" in kargs.iterkeys():
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
            ns = Namespace.get_namespace(env, modulename)
            assert(ns)
            assert(str(cast(env._context._object, c_void_p)) + modulename in Namespace._namespaces.iterkeys())
        else:
            if var_name and modulename == "":
                #have global namespace:
                ns = Namespace.get_global(env)                
                assert(ns)
                #now make the object and squirrel it away:
                #self._javascript_obj = JSObject.Make( env._context, cls._classDef, None )   
            else:
                ns = None
                #self._javascript_obj = None

        cls._populate(env , ns, _module)

        if ns:
            name = ns.get_name() + "." + var_name.split('.')[-1]
        else:
            name = "__global.%s" % var_name.split('.')[-1]
            
        if not modulename:
            if var_name and modulename == "":
                #now make the object and squirrel it away:
                self._javascript_obj = JSObject.Make(env._context, cls._classDef, None)   
            elif var_name == "":
                #have no namespace.  This should only happen
                #if the object self is itself the global namespace
                self._javascript_obj = env._context.GetGlobalObject()
        else:
            logging.error("MAKING OBJ %s: %s"%(var_name,ns._name))
            self._javascript_obj = JSObject.Make(env._context, cls._classDef, None)  

        env._jsobjects[ strid(self._javascript_obj)] = self
        self._javascript_obj.Protect( env._context)
        if ns and self._javascript_obj:
            #if not global namespace, add javascript namespace object
            #explicitly to ns
            text = JSString.CreateWithUTF8CString(var_name.split('.')[-1])
            ns._javascript_obj.SetProperty(env._context,
                                            text,
                                            self._javascript_obj,
                                            kJSPropertyAttributeNone,
                                            NULL)
            
            text.Release()
        #assert(self._javascript_obj)
        self._env = env
               
    def __del__(self):
        if hasattr(self, '_varname'):
            self._env._webview.execute_script("delete %s;" % self._varname)
            
    @classmethod
    def export_class(cls, env, ns):
        """Export a class to be visible within javascript"""
        assert(isinstance(env, ScriptEnv))
        if not issubclass(cls, Constructor) and not cls.__name__ in JavascriptClass._constructors.iterkeys():
            js_constructor = JavascriptClass.get_constructor(cls, env, ns)
            text = JSString.CreateWithUTF8CString("%s" % (cls.__name__.split('.')[-1]))
            JavascriptClass._constructors[cls.__name__] = js_constructor
            text.Release()

    @staticmethod
    def get_constructor(pyclass, context, namespace):
        if namespace == None:
            namespace = Namespace.get_namespace(context._env, "")#global
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
            logging.error("ARGS ARE %s"%[a for a in args])
            return self._pyclass(self._env, *args)
        except:
            logging.error("Exception instantiating %s" % self._pyclass)
            logging.error(traceback.format_exc())
            return None
        
class Namespace(JavascriptClass):

    _namespaces = {}
    
    def __init__(self, env, module):
        assert(isinstance(env, ScriptEnv))
        module_name = module.__name__ if module else ""
        self._context = env._context
        self._module = module
        if module_name == "__main__":
            module_name = ""
        self._name = module_name
        
        if module and module_name != "": 
            module_name = module.__name__
            JavascriptClass.__init__(self, env, module_name , _module=module)
        else:
            #if global namespace, do not call base class __init__ (infinite recurion),
            #but set necessary properties explicitly
            module_name = ""
            self._env = env
            self._context = env._context
            self._javascript_obj = env._context.GetGlobalObject()
            
        Namespace._namespaces[ str(cast(env._context._object, c_void_p)) + module_name ] = self
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
    def get_namespace(env, modulename):
        """
        Get or create the namespace for the given module name
        """
        assert(isinstance(env, ScriptEnv))
        id = str(cast(env._context._object, c_void_p)) + modulename
        if not id in Namespace._namespaces.iterkeys():
            if modulename:
                m = importlib.import_module(modulename)
                Namespace._namespaces[id] = Namespace(env, m)
            else:
                Namespace._namespaces[id] = Namespace(env, None)
        return Namespace._namespaces[id]
    
    @staticmethod
    def get_global(env):
        """
        Get or create the global namespace
        """
        assert(isinstance(env, ScriptEnv))
        ns = Namespace.get_namespace(env, "")
        return ns
        
    @staticmethod
    def add_global_class(env, pyclass , *args):
        """
        Add a python class to be accessible at global level
        in javascript
        """
        assert(isinstance(env, ScriptEnv))
        pyclass.export_class(env, Namespace.get_global(env))
        
    def _add_child_class(self, cls):
        """Add a child class to this namespace, avaiable in js"""
        cls.export_class(self._env, self)




def _wrapJs(env, jsobj, var_name, can_call=False):
    """
    Wrap a provided js object as a python object, with a given
    js name.  Can set a flag if js object is callable to make
    it callable in python too.  This is to be used only internally
    """
    assert(isinstance(env, ScriptEnv))
    if jsobj.IsFunction(env._context):
        wrapped = JSFunction(env, obj=jsobj, thisobj = None, name = var_name)
    else:
        wrapped = PythonWrapper(env, jsobj, var_name, can_call)
    return wrapped
    

class PythonWrapper(JSObject):
    """
    Wrap a javascript object into a python object that transparently
    interacts with the javascript environment, with all js methods
    available to the created python class!!
    """
    
    
    def __init__(self, env, obj, var_name, can_call=False):
        assert(isinstance(env, ScriptEnv))
        assert(obj)
        self._cmd = ""
        JSObject.__init__(self, obj=obj._object, context=env._context._object)
        self._varname = var_name
        self._can_call = can_call
        self._context = env._context
        self._env = env
        self._iteritems = []
        itercount = 0
        while True:
            prop = obj.GetProperty(env._context,JSString.CreateWithUTF8CString("%d"%itercount), NULL)
            if prop.IsUndefined(env._context):
                break
            else:
                prop._context = None
                self._iteritems.append(prop)
            itercount += 1
          
            
    def __getattr__(self, attr):
        prop = self.GetProperty(self._context, JSString.CreateWithUTF8CString( attr) , NULL)
        jstype = prop.GetType(self._env._context)
        if jstype == kJSTypeUndefined.value:
            return object.__getattribute__(self, attr)
        else:
            
            if jstype == kJSTypeObject.value:
                propobj = prop.ToObject(self._env._context, NULL)
                if propobj.IsFunction(self._env._context):
                    jsfunc = JSFunction(self._env, obj = propobj, thisobj = self, name = attr)
                    setattr(self, attr, 
                            jsfunc)
                    #if cast (propobj._object,c_void_p).value != cast (prop._object,c_void_p).value:
                    #    prop.Unprotect(self._env._context)
                    return jsfunc
                else:
                    setattr(self, attr, prop)
                    return prop
            elif jstype== kJSTypeNumber.value:
                val = prop.ToNumber( self._env._context, NULL)
                setattr(self, attr, val)    
                
                return val
            elif jstype==kJSTypeBoolean.value:
                val = prop.ToBoolean( self._env._context, NULL)
                setattr(self, attr, val)
                return val
            elif jstype == kJSTypeString.value:
                val = prop.ToPyString( self._env._cpntext, NULL)
                setattr (self, attr, val)
                return val
            elif jstype == kJSTypeNull.value:
                return None
        raise Exception("unknown javascript type")
                
    def __iter__(self, index):
        return self._iteritems[index]
    
    def __call__(self, *args):
        raise Exception()
        
        
     
        
def export_module(env, module):
    """Export a python module and all JavascriptClass derived
    subclasses to javascript execution environment
    """
    assert(isinstance(env, ScriptEnv))
    import importlib
    importlib.import_module(module.__name__)
    if module.__name__ in Namespace._namespaces:
        return
    return Namespace(env, module)



class ScriptEnv(JavascriptClass):
    """Javascript execution environment"""
    _jsobjects = {}
         

        
    
    def __init__(self, webview):
        
        self._webview = webview
        self._context = webview.get_main_frame().get_global_context()
        JavascriptClass.__init__(self, self, "python")
        
        #self._sem = ScriptEnv._sem[id]
        import jquery
        jquery.initialize(self)
        def get_document():
            global document
            document = self.get_jsobject( "document")
        webview.on_view_ready( get_document )
        
    def export_to_python(self, jsobj , var_name, can_call=False):
        wrapped = _wrapJs(self._env, jsobj, var_name, can_call)
        JavascriptClass._globalobjects[strid(self._context) + var_name] = wrapped
   
    
    def get_jsobject(self, name , can_call=False):
        ident = strid(self._context)
        retval = JavascriptClass._globalobjects.get(ident + name)
        
        if retval:
            retval._webview = self._webview
            
        else:
            self._webview.execute_script("python.export_to_python(%s,'%s', %s);" % (name, name, int(can_call)))
            retval = JavascriptClass._globalobjects.get(ident + name)
            if retval:
                retval._webview = self._webview
                retval._env = self
            else:                
                raise Exception("Unknown javascript object by name %s" % name)
        JavascriptClass._globalobjects[ident + name] = retval
        return retval


