try:
    test = unicode
except:
    unicode = str
from ..javascriptcore import *
from ctypes import *
import inspect
import traceback
import importlib

from ctypes import POINTER, c_int

OPAQUE_PTR = POINTER(c_int)
document = None


# noinspection PyProtectedMember
class JSFunction(JSObject):
    def __init__(self, context, obj, thisobj, name, _call_as_constructor=False):
        assert (isinstance(context, JSContext))
        JSObject.__init__(self, obj=obj, context=context)
        self._thisjsobj = thisobj
        if thisobj and not thisobj._object():
            self._thisjsobj = None
        self._name = name
        self._call_as_constructor = _call_as_constructor

    def promote_to_constructor(self):
        self._call_as_constructor = True

    def __call__(self, *args):
        # We must keep the javascript arguments active while this object is active 
        # and before another call is made to this JSFunction.  We cannot guarentee
        # when the jsFunction will be invoked (CallAsFunction seems to squirrel it 
        # away until it is called).  It is assumed that a second call will be made
        # to the jsfunction by the core engine only when a first call has been fully
        # processed (args will then go away).
        js_args = [get_jsobj(arg, self._context) for arg in args] if len(args) else NULL
        exc = JSValue.MakeNull(self._context)
        if self.IsConstructor(self._context) and self._call_as_constructor:
            return_value = self.CallAsConstructor(self._context,
                                                  c_int(len(args)),
                                                  js_args,
                                                  exc)
        else:
            return_value = self.CallAsFunction(self._context,
                                               self._thisjsobj,
                                               c_int(len(args)),
                                               js_args,
                                               exc)
        # TODO: handle exception
        return to_pythonjs(self._context, return_value) if return_value else None


# noinspection PyProtectedMember,PyBroadException
class JavascriptClass(object):
    """Class instance which is accessible within a javascript script"""
    _methods = None
    _methods_by_name = {}
    _constructors = {}
    items = {}
    items_py = {}
    index = 0
    _classDef = None

    @classmethod
    def _populate(cls, context, ns, _module):
        """
        Called once per derived class to populate the
        methods made available to javascript
        """
        if cls._methods:
            return
        cls._methods = [m for m in inspect.getmembers(cls, predicate=inspect.ismethod) if not m[0].startswith('_') and
                        m[0] != 'create' and m[0] != 'export_class']
        cls.staticmethods = (JSStaticFunction * (len(cls._methods) + 1))()
        # end must be "null"; javascriptcore uses this to determine terminator:
        cls.staticmethods[-1].name = c_char_p()
        cls.staticmethods[-1].callAsFunction = JSObjectCallAsFunctionCallback()
        cls.staticmethods[-1].attributes = 0

        # Function to get a function to cast into javascript callback:
        def getfunc(index_, _):
            callable_ = JSCallable(cls._methods[index_][1], cls._methods[index_][0], deduce_self=True)
            return callable_.callable

        # populate all the class methods into the javascript
        # class definition structure:
        for index in range(len(cls._methods)):
            name = cls._methods[index][0]
            cls.staticmethods[index].name = c_char_p(name)
            call_method = getfunc(index, name)
            cls.staticmethods[index].callAsFunction = JSObjectCallAsFunctionCallback(call_method)
            cls.staticmethods[index].attributes = kJSPropertyAttributeReadOnly
            cls._methods_by_name[cls.staticmethods[index].name] = cls._methods[index]
            cls.staticmethods[index].callback_ref = call_method

        # noinspection PyUnusedLocal
        def _init_cb(context_, obj):
            pass

        def _finalize_cb(obj):
            # cleanup if javascript side decides to delete the object:
            try:
                del JavascriptClass.items[obj._strong_ref.contents.value]
            except:
                pass

        # noinspection PyUnusedLocal
        def constructor_method(context_, _, this_object, argumentCount, arguments, exception):
            obj = JSObject.Make(JSContext(context_), cls._classDef, NULL)
            context_ = JSContext(context_)
            args = [context_]
            try:
                for i in range(argumentCount):
                    arg = JSObject(arguments[i], context_)
                    args.append(to_pythonjs(context_, arg))
                JavascriptClass.items_py[obj._strong_ref.contents.value] = cls(*args)
                JavascriptClass.items[obj._strong_ref.contents.value] = obj
                return cast(pointer(obj._strong_ref), POINTER(c_longlong)).contents.value
            except:
                import traceback
                traceback.print_exc()
                return_value = JSValue.MakeNull(context_)._strong_ref
                p_long_long = cast(pointer(return_value), POINTER(c_longlong))
                string = JSString.CreateWithUTF8CString(traceback.format_exc())
                s = JSValue.MakeString(context_, string)._strong_ref
                exception.contents = s
                string.Release()
                return p_long_long.contents.value

        JSObject.global_references[constructor_method] = constructor_method
        constructor_static_methods = (JSStaticFunction * 2)()
        # sentinel:
        constructor_static_methods[-1].name = c_char_p()
        constructor_static_methods[-1].callAsFunction = JSObjectCallAsFunctionCallback()
        constructor_static_methods[-1].attributes = 0
        # "new" constructor to create instance on javascript side:
        constructor_static_methods[0].name = c_char_p("new_")
        constructor_static_methods[0].attributes = kJSPropertyAttributeReadOnly
        constructor_static_methods[0].callAsFunction = JSObjectCallAsFunctionCallback(constructor_method)
        constructor_static_methods[0].callback_ref = constructor_method

        constructor = POINTER(JSClassDefinition)(JSClassDefinition(c_int(0),
                                                                   kJSClassAttributeNone,
                                                                   c_char_p(
                                                                       cls.__name__.encode('ascii') + ".Constructor"),
                                                                   NULL,
                                                                   POINTER(JSStaticValue)(),
                                                                   constructor_static_methods,
                                                                   JSObjectInitializeCallback(),
                                                                   JSObjectFinalizeCallback(),
                                                                   JSObjectHasPropertyCallback(),
                                                                   JSObjectGetPropertyCallback(),
                                                                   JSObjectSetPropertyCallback(),
                                                                   JSObjectDeletePropertyCallback(),
                                                                   JSObjectGetPropertyNamesCallback(),
                                                                   JSObjectCallAsFunctionCallback(),
                                                                   JSObjectCallAsConstructorCallback(),
                                                                   JSObjectHasInstanceCallback(),
                                                                   JSObjectConvertToTypeCallback()))
        constructor_obj = JSObject.Make(context, JSObject.JSClassCreate(constructor), None)
        propertyName = JSString.CreateWithUTF8CString(cls.__name__.encode('ascii'))
        ns._javascript_obj.SetProperty(context, propertyName, constructor_obj, kJSPropertyAttributeNone, NULL)
        propertyName.Release()
        # create the class definition
        jscd = POINTER(JSClassDefinition)(JSClassDefinition(c_int(0),
                                                            kJSClassAttributeNone,
                                                            c_char_p(cls.__name__.encode('ascii')),
                                                            NULL,
                                                            POINTER(JSStaticValue)(),
                                                            cls.staticmethods,
                                                            {False: JSObjectInitializeCallback(_init_cb),
                                                             True: JSObjectInitializeCallback()}[_module is not None],
                                                            {False: JSObjectFinalizeCallback(_finalize_cb),
                                                             True: JSObjectFinalizeCallback()}[_module is not None],
                                                            JSObjectHasPropertyCallback(),
                                                            JSObjectGetPropertyCallback(),
                                                            JSObjectSetPropertyCallback(),
                                                            JSObjectDeletePropertyCallback(),
                                                            JSObjectGetPropertyNamesCallback(),
                                                            JSObjectCallAsFunctionCallback(),
                                                            JSObjectCallAsConstructorCallback(),
                                                            JSObjectHasInstanceCallback(),
                                                            JSObjectConvertToTypeCallback()))
        cls._classDef = JSObject.JSClassCreate(jscd)
        if not _module:
            if cls.__name__ not in JavascriptClass._constructors and not cls.__name__ == "JSContext":
                # export this class  to be visible in javascript namespace
                cls.export_class(context, ns)

    def __init__(self, context, var_name, **kargs):
        assert isinstance(context, JSContext)
        self._context = context

        # see if the module was explcitly called out:
        _module = kargs.get('_module')
        self._varname = var_name
        if not _module:
            try:
                # if module not explicit, determine it here:
                if var_name.find('.') >= 0:
                    module_name = ".".join(var_name.split(".")[:-1])
                else:
                    # Oooh!  global namespace
                    module_name = ""
            except:
                module_name = None
        else:
            module_name = '.'.join(_module.__name__.split('.')[:-1])

        """This should take no parameters, to prevent repercussions throughout hierarchy"""
        cls = self.__class__

        if module_name:
            # if we determined a module name, get/create the namespace
            # associated with it
            ns = Namespace.get_namespace(context, module_name)
            assert ns
        else:
            if var_name and module_name == "":
                # have global namespace:
                ns = Namespace.get_global(context)
                assert ns
            else:
                ns = None

        cls._populate(context, ns, _module)

        if not module_name:
            if var_name and module_name == "":
                # now make the object and squirrel it away:
                self._javascript_obj = JSObject.Make(context, cls._classDef, None)
            elif var_name == "":
                # have no namespace.  This should only happen
                # if the object self is itself the global namespace
                self._javascript_obj = context.GetGlobalObject()
        else:
            self._javascript_obj = JSObject.Make(context, cls._classDef, None)

        if ns and self._javascript_obj:
            text = JSString.CreateWithUTF8CString(var_name.split('.')[-1])
            ns._javascript_obj.SetProperty(context,
                                           text,
                                           self._javascript_obj,
                                           kJSPropertyAttributeNone,
                                           NULL)
            text.Release()
            JavascriptClass.items[self._javascript_obj._strong_ref.contents.value] = self

    def __del__(self):
        try:
            del self.items[self._javascript_obj._strong_ref.contents.value]
        except:
            pass

    @classmethod
    def export_class(cls, context_, _):
        """Export a class to be visible within javascript
        :param ns: namespace or None that class belongs to
        :param context_: context for creating class definition JS object and sucn\h
        """
        assert (isinstance(context_, JSContext))


# noinspection PyProtectedMember
class Namespace(JavascriptClass):
    _namespaces = {}

    def __init__(self, context, module):
        assert (isinstance(context, JSContext))
        module_name = module.__name__ if module else ""
        self._context = context
        self._module = module
        if module_name == "__main__":
            module_name = ""
        self._name = module_name

        if module and module_name != "":
            module_name = module.__name__
            JavascriptClass.__init__(self, context, module_name, _module=module)
        else:
            # if global namespace, do not call base class __init__ (infinite recurion),
            # but set necessary properties explicitly
            module_name = ""
            self._context = context
            self._javascript_obj = context.GetGlobalObject()

        Namespace._namespaces[str(cast(context._strong_ref, OPAQUE_PTR)) + module_name] = self
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
    def get_namespace(context_, modulename):
        assert (isinstance(context_, JSContext))
        ptr = cast(context_._strong_ref, OPAQUE_PTR)
        id_ = str(ptr) + modulename
        if id_ not in iter(Namespace._namespaces.keys()):
            if modulename:
                m = importlib.import_module(modulename)
                Namespace._namespaces[id_] = Namespace(context_, m)
            else:
                Namespace._namespaces[id_] = Namespace(context_, None)
        return Namespace._namespaces[id_]

    @staticmethod
    def get_global(context):
        assert (isinstance(context, JSContext))
        ns = Namespace.get_namespace(context, "")
        return ns

    @staticmethod
    def add_global_class(context_, pyclass, *args):
        assert (isinstance(context_, JSContext))
        pyclass.export_class(context_, Namespace.get_global(context_))

    def _add_child_class(self, cls):
        """Add a child class to this namespace, avaiable in js"""
        cls.export_class(self._context, self)
        cls._populate(self._context, self, self._module)


# noinspection PyProtectedMember
def export_module(context_, module):
    """Export a python module and all JavascriptClass derived
    subclasses to javascript execution environment
    :param module:
    :param context_:
    """
    assert (isinstance(context_, JSContext))
    import importlib
    importlib.import_module(module.__name__)
    if module.__name__ in Namespace._namespaces:
        return
    return Namespace(context_, module)
