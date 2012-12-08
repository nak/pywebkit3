from .. import  gobject
from ..gobject import GObject

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
        return '"%s"'%var
    else:
        return str(var)

def to_pyvalue( env, jsvalue, name ):
    valtype = jsvalue.GetType(env._context)
    if valtype == kJSTypeNull.value  or valtype == kJSTypeUndefined.value:
        return None
    elif valtype == kJSTypeNumber.value:
        return jsvalue.ToNumber( env._context, NULL)
    elif valtype == kJSTypeBoolean.value:
        return jsvalue.ToBoolean( env._context)
    elif valtype == kJSTypeString.value:
        jstext = jsvalue.ToStringCopy( env._context, NULL)
        length = jstext.GetMaximumUTF8CStringSize()
        cstring = (c_char*(length))()
        jstext.GetUTF8CString( cstring, length )
    
        return cstring.value 
    elif valtype == kJSTypeObject.value:
        jsobj = jsvalue.ToObject(env._context, NULL)
        if jsobj.IsFunction(env._context):
            return None
            #assert( isinstance( context, JSContext ))
            #return _wrapJs( env, jsobj, name, can_call = True)
        found = JavascriptClass._jsobjects.get(strid(jsobj))
        if found:
            (_,found) = found
        else:
            found = JavascriptClass._globalobjects.get(strid(env._context)+name)
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
    def _populate(cls , env, _module):
        """
        Called once per derived class to populate the
        methods made available to javascript
        """
        cls._methods = [m for m in inspect.getmembers(cls, predicate=inspect.ismethod) if not m[0].startswith('_') and not m[0] == 'create']
        cls.staticmethods = (JSStaticFunction*(len(cls._methods)+1))()
        #end must be "null"; javascriptcore uses this to determine terminator:
        cls.staticmethods[-1].name = cast(NULL, c_char_p)
        cls.staticmethods[-1].callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
        cls.staticmethods[-1].attributes = 0
        #Function to get a function to cast into javascript callback:
        def getfunc(index):
            def call_method(ctxt, function, obj, argumentCount, arguments, exception):
                try:
                    context = JSContext(obj=ctxt)
                    id = strid(context)
                    (_,pyobj) = JavascriptClass._jsobjects[ str(cast(obj, c_void_p))]
                    #get the method to be called
                    method = cast(function, c_void_p)
                    methodname = cls.staticmethods[index].name
                    to_call = cls._methods_by_name.get(methodname)
                    if not to_call:
                        logging.error("Unrecognized method!  Internal error in javascript python binding %s"%methodname)

                    #now loop through arugments and convert
                    #TODO: Handle arrays
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
                                    pyarg = _wrapJs( env, jsobject, "arg%s"%i, can_call = can_call)
                                    assert(pyarg)
                                    args.append( pyarg )
                            else:
                                logging.error( "Invalid javascript value type encountered!: %d"%valtype)
                                return 0
                    assert(len(args) == argumentCount)
                    #make the call:
                    value =  to_call[1]( pyobj, *args )

                    #now convert the return value to something pythonic:
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

        #poptulate all the classmethods into the javascript
        #class definition structure:
        for index in xrange(len(cls._methods)):
            name = cls._methods[index][0]
            call_method = getfunc(index)
            cls.staticmethods[index].name = c_char_p( name)
            cls.staticmethods[index].callAsFunction  = JSObjectCallAsFunctionCallback( call_method)
            cls.staticmethods[index].attributes = kJSPropertyAttributeReadOnly
            cls._methods_by_name[cls.staticmethods[index].name] = cls._methods[index]        


        def _init_cb(context, obj):
            pass
          
        def _finalize_cb(obj):
            #cleanup if javascript side decides to delete the object:
            pyobj = JavascriptClass._jsobjects.get(str(cast(obj,c_void_p)))
            if pyobj:
                del JavascriptClass._jsobjects[str(cast(obj,c_void_p))]
                pyobj[1]._javascript_obj = None
                

        #create the class definition
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
        cls._classDef = JSObject.JSClassCreate( byref(jscd) )
        cls._jscd = jscd #don't let it go out of scope!!!


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
        if not "_module" in kargs.iterkeys():
            _module = None
        else:
            _module = kargs['_module']
        self._varname = var_name
        if not _module:
            try:
                #if module not explicit, determine it here:
                if var_name.find('.')>=0:
                    modulename = ".".join(var_name.split(".")[:-1])
                else:
                    #Oooh!  global namespace
                    modulename = ""
            except:
                modulename = None
        else:
            if isinstance( self, Constructor):                    
                modulename = _module.__name__
            else:
                modulename =  '.'.join(_module.__name__.split('.')[:-1])

        
        """This should take no parameters, to prevent repercussions throughout hierarchy"""
        cls = self.__class__
        if not isinstance(cls, Namespace) and not cls._methods:
            #(do not populate methods for namespace classes)
            cls._populate( env , _module)
        elif var_name:
            #or maybe not?
            #TODO: determine if this code makes sense
            #this seems to populate even Namepsace classes??
            cls._populate( env ,_module)
            
            
        if modulename:
            #if we determined a module name, get/create the namespace
            #associated with it
            ns = Namespace.get_namespace(env, modulename )
            assert(ns)
            assert( str(cast(env._context._object,c_void_p))+modulename in Namespace._namespaces.iterkeys() )
        else:
            if var_name and modulename == "":
                #have global namespace:
                ns = Namespace.get_global(env)                
                assert(ns)
            elif not var_name:
                #have no namespace.  This should only happen
                #if the object self is itself the global namespace
                ns = None
                self._javascript_obj = env._context.GetGlobalObject()
                
        #now make the object and squirrel it away:
        self._javascript_obj = JSObject.Make( env._context, cls._classDef, None )   
        JavascriptClass._jsobjects[strid(self._javascript_obj)] =  (self._javascript_obj,self)

        
        if not _module:
            if not self.__class__.__name__ in JavascriptClass._constructors:
                #export this class  to be visible in javascript namespace
                self.__class__.export_class(env, ns)
        if ns:
            #if not global namespace, add javascript namespace object
            #explicitly to ns
            text = JSString.CreateWithUTF8CString(var_name.split('.')[-1])
            ns._javascript_obj.SetProperty( env._context,
                                            text,
                                            self._javascript_obj,
                                            kJSPropertyAttributeNone,
                                            NULL)
        assert(self._javascript_obj)
        self._env = env
               
    def __del__(self):
        if hasattr(self, '_varname'):
            self._env.execute("delete %s;"%self._varname)
            
    @classmethod
    def export_class(cls, env, ns):
        """Export a class to be visible within javascript"""
        assert( isinstance(env, ScriptEnv ))
        if not issubclass(cls, Constructor) and not cls.__name__ in JavascriptClass._constructors.iterkeys():
            js_constructor = JavascriptClass.get_constructor( cls, env, ns)
            text = JSString.CreateWithUTF8CString("%s"%( cls.__name__.split('.')[-1]))
            JavascriptClass._constructors[cls.__name__] = js_constructor


    @staticmethod
    def get_constructor( pyclass, context, namespace):        
        assert(isinstance(namespace,Namespace))
        pyclass._constructor = Constructor
        retval = pyclass._constructor(pyclass, context, namespace)
        return retval

  
    def __getattr__(self,attr):
        orig_attr = getattr(self, attr)
        def _hooked_( *args):
            """A hook method to pass as a callback"""
            with self._env.execution() as js_execution:
                orig_attr( *args )

        if callable( orig_attr ):
            
            return _hooked_
        else:
            return orig_attr

def javascript(func, env):
    with env.execution() as js_execution:
        orig_func = func
        def hooked__(*args):
            with env.execution() as js_execution:
                orig_func(*args)
        importlib.import_module(func.__module__).setattr(func.__name,hooked__)

class Constructor(JavascriptClass):

    def __init__(self, pyclass, context, namespace):
        pymodule = importlib.import_module(pyclass.__module__)
        JavascriptClass.__init__(self, context,
                                 var_name="%s"%pyclass.__name__, 
                                 _module = pymodule)
        self._pyclass = pyclass
        self._context = context

    def new_( self, name, *args):
        """
        The constructor is an object (class) available in javascript, with a "._new"
        method for creating instance (an underlying python instance, acutally) from
        within javascript
        """
        try:
            return self._pyclass( self._context, name, *args)
        except:
            logging.error("Exception instantiating %s"%pyclass)
            logging.error(traceback.format_exc())
            return None
        
class Namespace( JavascriptClass ):

    _namespaces = {}
    
    def __init__(self, env, module ):
        assert(isinstance(env, ScriptEnv))
        module_name = module.__name__ if module else ""
        self._context = env._context
        self._module = module
        
        if module: 
            module_name = module.__name__
            JavascriptClass.__init__(self, env, module_name , _module = module)
        else:
            #if global namespace, do not call base class __init__ (infinite recurion),
            #but set necessary properties explicitly
            module_name = ""
            self._javascript_obj = env._context.GetGlobalObject()
            
        Namespace._namespaces[ str(cast(env._context._object, c_void_p)) + module_name ] = self
        if module:
            self._export_classes()

        
    def _export_classes(self):
        """
        Export all classes from the python module associated
        with this namespace
        """
        for name, obj in inspect.getmembers(self._module):
            if inspect.isclass(obj) and issubclass(obj, JavascriptClass) and \
                   not issubclass(obj, Namespace ) and not obj==JavascriptClass:
                
                self._add_child_class(  obj)
        
            
    @staticmethod
    def get_namespace( env, modulename):
        """
        Get or create the namespace for the given module name
        """
        assert( isinstance(env, ScriptEnv ))
        id = str(cast(env._context._object, c_void_p))+modulename
        if not id in Namespace._namespaces.iterkeys():
            if modulename:
                m = importlib.import_module(modulename)
                Namespace._namespaces[id] = Namespace( env, m)
            else:
                Namespace._namespaces[id] = Namespace( env, None)
        return Namespace._namespaces[id]
    
    @staticmethod
    def get_global( env):
        """
        Get or create the global namespace
        """
        assert( isinstance(env, ScriptEnv) )
        ns =  Namespace.get_namespace( env, "")
        return ns
        
    @staticmethod
    def add_global_class( env, pyclass , *args):
        """
        Add a python class to be accessible at global level
        in javascript
        """
        assert( isinstance(env, ScriptEnv ) )
        pyclass.export_class( env, Namespace.get_global(env))
        
    def _add_child_class(self,  cls):
        """Add a child class to this namespace, avaiable in js"""
        cls.export_class( self._env, self)




def _wrapJs(env,  jsobj, var_name, can_call = False):
    """
    Wrap a provided js object as a python object, with a given
    js name.  Can set a flag if js object is callable to make
    it callable in python too.  This is to be used only internally
    """
    assert(isinstance(env, ScriptEnv))
    id = str(cast( jsobj._object, c_void_p))
    wrapped = PythonWrapper( env, jsobj, var_name, can_call)
    return wrapped
    

class PythonWrapper( JSObject ):
    """
    Wrap a javascript object into a python object that transparently
    interacts with the javascript environment, with all js methods
    available to the created python class!!
    """
    
    
    def __init__(self, env, obj, var_name, can_call = False):
        assert(isinstance(env, ScriptEnv))
        self._cmd = ""
        self._retval = None
        JSObject.__init__(self, obj=obj._object )
        self._varname = var_name
        self._wrapped_obj = obj
        names = obj.CopyPropertyNames( env._context )
        count = JSObject.JSPropertyNameArrayGetCount( names )
        self._can_call = can_call
        self._attributes = {}
        self._context = env._context
        self._env = env
        for index in xrange(count):
            var_name_ref = JSObject.JSPropertyNameArrayGetNameAtIndex( names, index)
            length = var_name_ref.GetMaximumUTF8CStringSize()
            var_name = (c_char*(length))()
            var_name_ref.GetUTF8CString( var_name, length )
            if var_name.value != "each":
                exc = POINTER(c_int)(c_int(0))
                prop = obj.GetProperty( env._context, var_name_ref, exc)
                self._attributes[var_name.value] =  to_pyvalue(env, prop, var_name.value)

                
    def __call__(self, *args):
        cmd=  "%s(%s)"%(self._varname, ",".join([to_string(v) for v in args]))
        (index, tmpvarname) = self._env._tmpvarname()
        cmd = "try{python.PY_RETURN( %(cmd)s,'%(tmp)s');}catch(err){python.PY_THROW(err,'%(tmp)s');}"%\
              {'tmp':tmpvarname,
               'cmd':cmd}
        (returnval, exc)  =self._env.execute( cmd, tmpvarname)
        if exc:
            logging.error("ERROR Executing command %s"%cmd)
            logging.error(traceback.format_exc())
            return None
        if returnval:
            self._retval = (returnval , "python.%s"%tmpvarname)
            self._retval[0]._webview = self._webview
            self._retval[0]._varname = "python.%s"%tmpvarname 
            return self._retval[0]
        else:
            return None



    def each(self, func, *args):
        """TODO: This should only be available for jquery $() objects"""
        js = "%s.each( function(index,obj){try{python.PY_EACH(  $(obj), index);}catch(err){PY_THROW(err,'_jqobj'+index);}})"%self._varname
        self._env._each_apply = (func, args)
        self._env._each_objs = []
        try:
            self._env.execute( js , None)
            js = ""
            index = 0
            for obj in self._env._each_objs:
                func(obj, index, *args)
                index +=1
        except:
            logging.error( "Problem executing %s"%js)
            self._env._each_apply = None
        self._env._each_objs = []
        self._env._each_apply = None
        
        
    def _hooked(self, *args):
        """A hook method to pass as a callback"""
        cmd=  "%s.%s(%s)"%(self._varname, self._attr, ",".join([to_string(v) for v in args]))
        #get the execution envrionment:
        
        #generate a tmp var name to use as return value:
        (index, tmpvarname) = self._env._tmpvarname()
        cmd = "try{python.PY_RETURN( %(cmd)s,'%(tmp)s');}catch(err){python.PY_THROW(err,'%(tmp)s');}"%\
            {'tmp':tmpvarname,
             'cmd':cmd}

        #execute the command, and get return value or exception:
        (retval, exc ) = self._env.execute( cmd, tmpvarname)
        if exc:
            #OOh! problem executing command
            raise exc
        else:
            #set the webview executor (pass it along) if
            #this the return value is a JavascriptClass python instance
            if retval and isinstance(retval, JavascriptClass):
                retval._webview = self._webview
            return retval
        
        
    def __getattr__(self,attr):
        
        if not attr in self._attributes.iterkeys():
            if  hasattr(self, attr):
                return getattr(self, attr)
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
        
        
def export_module( env, module):
    """Export a python module and all JavascriptClass derived
    subclasses to javascript execution environment
    """
    assert( isinstance(env, ScriptEnv))
    import importlib
    importlib.import_module( module.__name__)
    if module.__name__ in Namespace._namespaces:
        return
    return Namespace( env, module )


class JSException( Exception):

    def __init__(self, err):
        Exception.__init__(self, err)
        self._err = err

        

class ScriptEnv( JavascriptClass ):
    """Javascript execution environment"""


    _tmpindex = 0
    _sem = {}
    
    def _tmpvarname(self):
        ScriptEnv._tmpindex += 1
        return ( ScriptEnv._tmpindex-1, "_tmp%d"%(ScriptEnv._tmpindex-1))
    
    def __init__( self, webview):
        
        self._webview = webview
        self._context = webview.get_main_frame().get_global_context()
        id = str(cast( self._context._object, c_void_p))
        assert( not JavascriptClass._python_to_js)
        JavascriptClass._python_to_js[id] = self
        JavascriptClass.__init__(self, self, "python")
        
        self._exception = {}
        self._returnval = {}
        
        self._each_apply  = None
        #self._sem = ScriptEnv._sem[id]
        self._each_objs = []
        import jquery
        jquery.initialize(self)
        
    class Execution_Env(object):
        
        def __init__(self, env):
            self._env = env
            if not ScriptEnv._sem.has_key(id):
                ScriptEnv._sem[id] = threading.Semaphore(0)
                self._sem = ScriptEnv._sem[id]
            self._sem.acquire()#python.init() call from html/js will free
            self._sem.release()
            
        def __enter__(self):
            self._env._sem.acquire()
            
        def __exit__(self):
            js = self._env._produce_js()
            self._env.execute( js )
            self._sem.release()
             
    def execution(self):
        return ScriptEnv.Execution_Env(self)
             
    def export_to_python( self, jsobj , var_name, can_call = False ):
        wrapped = _wrapJs( self._env, jsobj, var_name, can_call )
        JavascriptClass._globalobjects[strid(self._context) + var_name] = wrapped


    def PY_READY( self ):
        for (ready_listener, args) in self._ready_listeners:
            ready_listener( *args )
        
    def PY_RETURN( self, jsobj , name):
        
        self._returnval[name] = jsobj
        if isinstance( jsobj, JavascriptClass):
            self._returnval[name]._varname = name
        text = JSString.CreateWithUTF8CString(name)
        if not isinstance(jsobj, str):
            self._javascript_obj.SetProperty( self._context,
                                              text,
                                              jsobj,
                                              kJSPropertyAttributeNone,
                                              NULL)

        self._exception[name] = None

  
        
    def PY_THROW( self , jserr, name):
        logging.error("javascript error encountered ")
        self._exception[name] =  JSException( jserr.line  )
        self._returnval[name] = None
    

    def PY_EACH( self,  obj, index):
        text = JSString.CreateWithUTF8CString('_jqobj%d'%index)
        self._javascript_obj.SetProperty( self._context,
                                          text,
                                          obj,
                                          kJSPropertyAttributeNone,
                                          NULL)
        obj =  PythonWrapper(self._env, self._javascript_obj.GetProperty( self._context, text, NULL).ToObject(self._context, NULL), 'python._jqobj%d'%index)
        obj._webview = self._webview
        self._each_objs.append( obj )
        return False
        if self._each_apply:
            try:
                self._each_apply[0](obj, int(index), *self._each_apply[1])
                self._webview.execute_script("delete python._jqobj%d;"%index)
            except:
                logging.error("Error applying each function at index %d"%index)
                logging.error(traceback.format_exc())
            
        return False


        
    def execute( self, cmd, tmpvarname = None):
       
        try:
            if tmpvarname:
                self._returnval[tmpvarname] = None
                self._exception[tmpvarname] = None
            self._webview.execute_script(cmd)
            if tmpvarname:
                exc    = self._exception[tmpvarname]
                retval = self._returnval[tmpvarname]
                self._exception[tmpvarname] = None
                self._returnval[tmpvarname] = None
                del self._returnval[tmpvarname]
                del self._exception[tmpvarname]
            else:
                retval = None
                exc = None
            if retval and isinstance(retval, JavascriptClass):
                
                text = JSString.CreateWithUTF8CString("%s"%tmpvarname)
                self._javascript_obj.SetProperty( self._context,
                                                  text,
                                                  retval,
                                                  kJSPropertyAttributeNone,
                                                  NULL)

            if retval and isinstance(retval, JavascriptClass):
                retval._webview = self._webview
        except:
            logging.error("TRACEBACK........")
            logging.error(traceback.format_exc())
            exc = Exception
            retval = None
        finally:
            pass
        return (retval, exc )

    
    def get_jsobject( self, name , can_call = False):
        id = str(cast(self._context._object, c_void_p))
        retval =  JavascriptClass._globalobjects.get( id+name)
        
        if retval:
            retval._webview = self._webview
            
        else:
            self._webview.execute_script("python.export_to_python(%s,'%s', %s);"%(name, name, int(can_call)))
            retval =  JavascriptClass._globalobjects.get( id+name)
            if retval:
                retval._webview = self._webview
                retval._env = self
            else:                
                raise Exception("Unknown javascript object by name %s"%name)
        JavascriptClass._globalobjects[id+name] = retval
        return retval
