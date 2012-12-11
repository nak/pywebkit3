from .. import  gobject
from ..gobject import GObject
from ..gtk3 import libgtk3

import inspect
import threading
from ..javascriptcore import *
from ctypes import *
import logging
import traceback
import importlib

def strid(obj):
    return str(cast(obj._object, c_void_p))

   
def to_jsfunction(env, func):
    import numbers
    def C_Callable( context, function, thisObject,  argumentCount, arguments, exception):
            context = JSObject(obj = context)
            thisObject = JSObject(obj = context)
            try:
                args = []
                for i in xrange(argumentCount):
                    argument = JSValue(obj = arguments[i])
                    
                    valtype = argument.GetType(context)
                    if valtype == kJSTypeNull.value or valtype == kJSTypeUndefined.value:
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
                    elif valtype == kJSTypeObject.value:
                        jsobject = argument.ToObject(context, NULL)
                        
                        can_call = jsobject.IsFunction(context)
                        pyarg = _wrapJs(env, jsobject, None, can_call=can_call)
                        pyarg._javascript_obj = jsobject
                        args.append(pyarg)
                    else:
                        logging.error("Invalid javascript value type encountered!: %d" % valtype)
                        return c_longlong(0)
                assert(len(args) == argumentCount)
                retval = func(*args)
                if retval == None:
                    retval = JSValue.MakeNull(env._context)
                elif isinstance(retval, numbers.Number):
                    retval = JSValue.MakeNumber( env._context, retval)
                elif isinstance(retval, str):
                    cstring = c_char_p(retval)
                    text = JSString.CreateWithUTF8CString(cstring);
                    retval = JSValue.MakeString(context, text);
                    #text.Release()
                elif retval in [True, False]:
                    retval = JSValue.MakeBoolean(context, retval)
                assert( isinstance(retval, JSValue))
                
                retval =  cast(byref(retval._object),POINTER(c_longlong)).contents
                return retval.value
            except:
                logging.error(traceback.format_exc())
                logging.error("Error in calling argument function ")
                return c_longlong(0)
    #logging.error("ENTER")
    #libgtk3.gdk_threads_enter()
    cfunc = JSObjectCallAsFunctionCallback(C_Callable)
    #libgtk3.gdk_threads_leave()
    #logging.error("LEAVE")
    jsobj = JSObject.MakeFunctionWithCallback(env._context, NULL, cfunc)
    jsobj._callable = cfunc
    return jsobj

def to_pythonjs( env, val): 
    context = env._context
    valtype= val.GetType(context)
    if valtype == kJSTypeNull.value or valtype == kJSTypeUndefined:
        return None
    elif valtype == kJSTypeNumber.value:
        return val.ToNumber(context, NULL)
    elif valtype == kJSTypeBoolean.value:
        return val.ToBoolean(context)
    elif valtype == kJSTypeString.value:
        jstext = val.ToStringCopy(context, NULL)
        length = jstext.GetMaximumUTF8CStringSize()
        cstring = (c_char * (length))()
        jstext.GetUTF8CString(cstring, length)
        jstext.Release()
        return cstring.value
    elif valtype == kJSTypeObject.value:
        jsobject = val.ToObject(context, NULL)
        
        can_call = jsobject.IsFunction(context)
        pyarg = _wrapJs(env, jsobject, None, can_call=can_call)
        pyarg._javascript_obj = jsobject
        return pyarg
    else:
        logging.error("Invalid javascript value type encountered!: %d" % valtype)
        return None
                              
class JSFunction(JSObject):

    def __init__(self, env, obj, thisobj):
        JSObject.__init__(self, obj=obj._object)
        self._thisjsobj = thisobj
        self._jsfuncobj = obj
        self._env  = env
        
    def __call__(self, *args):
        import numbers
        jsArgs = []
        
        for arg in args:
            if isinstance(arg, numbers.Number):
                arg = JSValue.MakeNumber( self._env._context, arg)
            elif isinstance(arg, str):
                string = JSString.CreateWithUTF8CString(c_char_p(arg))
                arg = JSValue.MakeString(self._env._context, string)
                #string.Release()
            elif isinstance( arg, JSObject):
                pass
            elif callable(arg):
                arg = to_jsfunction(self._env, arg)
                #logging.error("ARG FUNC: %s"%JSValue(obj=arg._object).GetType(self._env._context))
            jsArgs.append( arg )
        retval =  self._jsfuncobj.CallAsFunction( self._env._context, self._thisjsobj,
                                        c_int(len(args)),
                                        jsArgs,
                                        NULL)
        assert(isinstance(retval, JSValue))
        if cast( retval._object, c_void_p).value == None:
            return None
        return to_pythonjs(self._env, retval)
        
def to_pyvalue(env, thisobj, jsvalue, name):
    #logging.error("CONVERTING %s"%jsvalue)
    valtype = jsvalue.GetType(env._context)
    #logging.error("CONVERTING TYPE %s"%valtype)
    if valtype == kJSTypeNull.value  or valtype == kJSTypeUndefined.value:
        return None
    elif valtype == kJSTypeNumber.value:
        return jsvalue.ToNumber(env._context, NULL)
    elif valtype == kJSTypeBoolean.value:
        return jsvalue.ToBoolean(env._context)
    elif valtype == kJSTypeString.value:
        jstext = jsvalue.ToStringCopy(env._context, NULL)
        length = jstext.GetMaximumUTF8CStringSize()
        cstring = (c_char * (length))()
        jstext.GetUTF8CString(cstring, length)
        jstext.Release()
        return cstring.value 
    elif valtype == kJSTypeObject.value:
        #logging.error("TO PY OBJECT")
        jsobj = jsvalue.ToObject(env._context, NULL)
        if jsobj.IsFunction(env._context):
            return JSFunction(env, obj=jsobj, thisobj= None)
            #logging.error("RETURNING NONE")
            return None
            #assert( isinstance( context, JSContext ))
            #return _wrapJs( env, jsobj, name, can_call = True)
        
        myname = jsobj.GetPrivate()
        found = None
        if myname:
            found = JavascriptClass._globalobjects.get(strid(env._context) + myname)
        if not found:
            return _wrapJs(env, jsobj = jsobj, var_name = myname or "_tmp", can_call = False)
        #logging.error("RETURNING ITEM %s"%found)
        return  found

    logging.error("Unknown object passed to python from javascript. Object must be known in both worlds.  %d" % valtype)
    return None


class JavascriptClass(object):
    """Class instance of which are accessible within a javascript"""
    _methods = None
    _methods_by_name = {}
    _globalobjects = {}
    _python_to_js = {}
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
                #ogging.error("MENTER")
                #libgtk3.gdk_threads_enter()
                try:
                    context = JSContext(obj=ctxt)
                    name = JSObject(obj=obj).GetPrivate()
                    pyobj = env._jsobjects[ name ]
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
                        import numbers
                        if isinstance(arguments[i], numbers.Number):
                            args.append(arguments[i])
                        else:
                            valtype = JSValue(obj=arguments[i]).GetType(context)
                            if valtype == kJSTypeNull.value or valtype == kJSTypeUndefined:
                                args.append(None)
                            elif valtype == kJSTypeNumber.value:
                                args.append(JSValue(arguments[i]).ToNumber(context, NULL))
                            elif valtype == kJSTypeBoolean.value:
                                args.append(JSValue(arguments[i]).ToBoolean(context))
                            elif valtype == kJSTypeString.value:
                                jstext = JSValue(arguments[i]).ToStringCopy(context, NULL)
                                length = jstext.GetMaximumUTF8CStringSize()
                                cstring = (c_char * (length))()
                                
                                jstext.GetUTF8CString(cstring, length)
                                jstext.Release()
                                args.append(cstring.value)
                            elif valtype == kJSTypeObject.value:
                                jsobject = JSValue(arguments[i]).ToObject(context, NULL)
                                jsname = jsobject.GetPrivate() or ""
                                
                                #logging.error("IS FUNCTION? '%s'"%jsobject._object)
                                can_call = jsobject.IsFunction(context)
                                pyarg = _wrapJs(env, jsobject, "arg%s" % i, can_call=can_call)
                                pyarg._javascript_obj = jsobject
                                args.append(pyarg)
                            else:
                                logging.error("Invalid javascript value type encountered!: %d" % valtype)
                                return 0
                    assert(len(args) == argumentCount)
                    #make the call:
                    value = to_call[1](pyobj, *args)
                    #now convert the return value to something pythonic:
                    import numbers
                    if isinstance(value, numbers.Number):
                        retval = JSValue.MakeNumber(context, value)._object
                    elif isinstance(value, str):
                        cstring = c_char_p(value)
                        text = JSString.CreateWithUTF8CString(cstring);
                        retval = JSValue.MakeString(context, text)._object;
                        #text.Release()
                    elif isinstance(value, JavascriptClass):
                        retval = value._javascript_obj._object
                    else:
                        retval = NULL
                    retvalp = cast(byref(retval), POINTER(c_longlong))
                    return retvalp.contents.value
                except:
                    logging.error("EXCEPTION calling python method from javascript:")
                    logging.error(traceback.format_exc())
                    return 0#NULL
                finally:
                    #logging.error("MLEAVE")
                    #libgtk3.gdk_threads_leave()
                    pass
                
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
            name = JSObject(obj=obj).GetPrivate()
            if name:
                pyobj = env._jsobjects.get(name)
                if pyobj:
                    del env._jsobjects[name]
                    pyobj._javascript_obj = None
                

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
            if not cls.__name__ in JavascriptClass._constructors:
                #export this class  to be visible in javascript namespace
                cls.export_class(env, ns)


    def __init__(self, env, var_name, **kargs):
        assert isinstance(env, ScriptEnv)
        ##id = str(cast( js_context._object, c_void_p))
        #it seems sometimes the context id different than the webview
        #original context we used????:
        ##if not id in JavascriptClass._python_to_js.iterkeys():
        ##    if not JavascriptClass._python_to_js:
        ##        ScriptEnv( self._context )
        ##    else:
        ##        id = JavascriptClass._python_to_js.keys()[0]

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

        if not isinstance(cls, Namespace) and not cls._methods:
            #(do not populate methods for namespace classes)
            cls._populate(env , ns, _module)
        elif var_name:
            #or maybe not?
            #TODO: determine if this code makes sense
            #this seems to populate even Namepsace classes??
            cls._populate(env , ns, _module)

        if ns:
            name = ns.get_name() + "." + var_name
        else:
            name = "__global.%s" % var_name
            
        if not modulename:
            if var_name and modulename == "":
                #now make the object and squirrel it away:
                self._javascript_obj = JSObject.Make(env._context, cls._classDef, None)   
            elif var_name == "":
                #have no namespace.  This should only happen
                #if the object self is itself the global namespace
                self._javascript_obj = env._context.GetGlobalObject()
        else:
            self._javascript_obj = JSObject.Make(env._context, cls._classDef, None)   
           
        env._jsobjects[name] = self
        self._javascript_obj.SetPrivate(c_char_p(name))
        
        logging.error("ADDED OBJ WITH NAME %s" % name)
        
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

    def new_(self, name, *args):
        """
        The constructor is an object (class) available in javascript, with a "._new"
        method for creating instance (an underlying python instance, acutally) from
        within javascript
        """
        try:
            return self._pyclass(self._context, name, *args)
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
        self._name = module_name
        
        if module: 
            module_name = module.__name__
            JavascriptClass.__init__(self, env, module_name , _module=module)
        else:
            #if global namespace, do not call base class __init__ (infinite recurion),
            #but set necessary properties explicitly
            module_name = ""
            self._javascript_obj = env._context.GetGlobalObject()
            
        Namespace._namespaces[ str(cast(env._context._object, c_void_p)) + module_name ] = self
        if module:
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
    id = str(cast(jsobj._object, c_void_p))
    if jsobj.IsFunction(env._context):
        wrapped = JSFunction(env, obj=jsobj, thisobj = None)
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
        JSObject.__init__(self, obj=obj._object)
        self._varname = var_name
        self._wrapped_obj = obj
        if obj:
            names = obj.CopyPropertyNames(env._context)
            count = JSObject.JSPropertyNameArrayGetCount(names)
        else:
            names=[]
            count = 0
        self._can_call = can_call
        self._attributes = {}
        self._jsmethods = {}
        self._context = env._context
        self._env = env
        iteritems = {}
        itercount = 0
        for index in xrange(count):
            var_name_ref = JSObject.JSPropertyNameArrayGetNameAtIndex(names, index)
            length = var_name_ref.GetMaximumUTF8CStringSize()
            var_name = (c_char * (length))()
            var_name_ref.GetUTF8CString(var_name, length)
            if not var_name.value.startswith('_'):
                exc = POINTER(c_int)(c_int(0))
                prop = obj.GetProperty(env._context, var_name_ref, exc)
                if prop.IsObject( env._context ):
                    if prop.ToObject(env._context, NULL).IsFunction(env._context):
                        self._jsmethods[var_name.value] = JSFunction(env, obj = prop.ToObject(env._context, NULL), thisobj = self._wrapped_obj)
                    else:
                        self._attributes[var_name.value] = prop
                        if var_name.value.isdigit():
                            iteritems[var_name.value] = prop
                            itercount += 1
        self._iteritems = [None for i in xrange(itercount)]
        for key,val in iteritems.iteritems():
            self._iteritems[int(key)] = val
            
    def __iter__(self, index):
        return self._iteritems[index]
    
    def __call__(self, *args):
        raise Exception()
        
        
        
    def __getattr__(self, attr):
        if attr in self._jsmethods.keys():
            return self._jsmethods[attr]
        elif attr in self._attributes.keys():
            val = self._attributes[attr]
            if isinstance(val, JSValue):
                val = to_pyvalue(self._env, self, val, attr)
                self._attributes[attr] = val #we chose to delay processing
            if val and hasattr(self, '_webview'):
                val._webview = self._webview
            return val
        else:
            return object.__getattribute__(self, attr)
        
   
        
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


class JSException(Exception):

    def __init__(self, err):
        Exception.__init__(self, err)
        self._err = err


class ScriptEnv(JavascriptClass):
    """Javascript execution environment"""

    class Proxy(PythonWrapper):

        def __init__(self, env, name):
            PythonWrapper.__init__(self, env, obj=None, var_name=name, can_call=True)
            
        def __getattr__(self, attr):
            return ScriptEnv.Proxy(self._env, self._varname + "." + attr)
            
    TMPPREFIX = '_tmptmp_pyjs'
    
    _tmpindex = 0
    #_sem = {}
    
    def _tmpvarname(self):
        ScriptEnv._tmpindex += 1
        return (ScriptEnv._tmpindex - 1, "%s%d" % (ScriptEnv.TMPPREFIX, ScriptEnv._tmpindex - 1))
    
    def __init__(self, webview):
        
        self._exception = {}
        self._returnval = {}
        self._jsobjects = {}
        self._each_apply = None
        self._webview = webview
        self._context = webview.get_main_frame().get_global_context()
        id = str(cast(self._context._object, c_void_p))
        assert(not JavascriptClass._python_to_js)
        JavascriptClass._python_to_js[id] = self
        JavascriptClass.__init__(self, self, "python")
        
        #self._sem = ScriptEnv._sem[id]
        import jquery
        jquery.initialize(self)
        assert(hasattr(self, '_returnval'))
        
    class Execution_Env(object):
        
        _execution = None
        _count = 0
        
        def __init__(self, env):
            self._env = env
            self._execution = 0
            #if not ScriptEnv._sem.has_key(id):
            #    ScriptEnv._sem[id] = threading.Semaphore(0)
            #    self._sem = ScriptEnv._sem[id]
            #self._sem.acquire()#python.init() call from html/js will free
            #self._sem.release()
            self._js = []
             
             
    def export_to_python(self, jsobj , var_name, can_call=False):
        wrapped = _wrapJs(self._env, jsobj, var_name, can_call)
        JavascriptClass._globalobjects[strid(self._context) + var_name] = wrapped


   
    
    def get_jsobject(self, name , can_call=False):
        id = str(cast(self._context._object, c_void_p))
        retval = JavascriptClass._globalobjects.get(id + name)
        
        if retval:
            retval._webview = self._webview
            
        else:
            self._webview.execute_script("python.export_to_python(%s,'%s', %s);" % (name, name, int(can_call)))
            retval = JavascriptClass._globalobjects.get(id + name)
            if retval:
                retval._webview = self._webview
                retval._env = self
            else:                
                raise Exception("Unknown javascript object by name %s" % name)
        JavascriptClass._globalobjects[id + name] = retval
        return retval
