# Copyright, John Rusnak, 2012
# This code binding is available under the license agreement of the LGPL with
# an additional constraint described below,
# and with the understanding that the webkit API is copyright protected
# by Apple Computer, Inc. (see below).
# There is an  additional constraint that any derivatives of this work aimed
# at providing bindings to GObject, GTK, GDK, or WebKit be strictly
# python-only bindings with no native code.
# * THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY
# * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
# * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# ******************************************************
# For the API:
# /*
# * Copyright (C) 2006 Apple Computer, Inc.  All rights reserved.
# *
# * Redistribution and use in source and binary forms, with or without
# * modification, are permitted provided that the following conditions
# * are met:
# * 1. Redistributions of source code must retain the above copyright
# *    notice, this list of conditions and the following disclaimer.
# * 2. Redistributions in binary form must reproduce the above copyright
# *    notice, this list of conditions and the following disclaimer in the
# *    documentation and/or other materials provided with the distribution.
# *
# * THIS SOFTWARE IS PROVIDED BY APPLE COMPUTER, INC. ``AS IS'' AND ANY
# * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
# * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# */
import collections
import numbers
from .gtk3_types import *
from .javascriptcore_types import *
import logging
from .javascriptcore_enums import *
from .javascriptcore__JSValue import JSValue

OPAQUE_PTR = POINTER(c_void_p)
NULL = OPAQUE_PTR()

"""Derived Pointer Types"""
__JSValue = OPAQUE_PTR
_JSContext = OPAQUE_PTR
_JSObject = OPAQUE_PTR
_JSGlobalContext = OPAQUE_PTR
_JSClass = OPAQUE_PTR
_JSValue = OPAQUE_PTR
_JSContextGroup = OPAQUE_PTR
_JSPropertyNameArray = OPAQUE_PTR
_JSString = OPAQUE_PTR
_JSPropertyNameAccumulator = OPAQUE_PTR

libjavascriptcore.JSObjectCallAsFunction.argtypes = [_JSContext, _JSObject, _JSObject, c_int, _JSValue,
                                                     POINTER(_JSValue)]
libjavascriptcore.JSObjectCallAsFunction.restype = _JSValue
libjavascriptcore.JSObjectSetPrivate.restype = bool
libjavascriptcore.JSObjectSetPrivate.argtypes = [_JSObject, Asciifier]
libjavascriptcore.JSObjectGetProperty.restype = _JSValue
libjavascriptcore.JSObjectGetProperty.argtypes = [_JSContext, _JSObject, _JSString, _JSValue]
libjavascriptcore.JSPropertyNameAccumulatorAddName.argtypes = [_JSObject, _JSPropertyNameAccumulator, _JSString]
libjavascriptcore.JSObjectSetPrototype.argtypes = [_JSContext, _JSObject, _JSValue]
libjavascriptcore.JSObjectHasProperty.restype = bool
libjavascriptcore.JSObjectHasProperty.argtypes = [_JSContext, _JSObject, _JSString]
libjavascriptcore.JSObjectGetPrototype.restype = _JSValue
libjavascriptcore.JSObjectGetPrototype.argtypes = [_JSContext, _JSObject]
libjavascriptcore.JSObjectCallAsConstructor.restype = _JSObject
libjavascriptcore.JSObjectCallAsConstructor.argtypes = [_JSContext, _JSObject, size_t, _JSValue, _JSValue]
libjavascriptcore.JSPropertyNameArrayRelease.argtypes = [_JSObject, _JSPropertyNameArray]
libjavascriptcore.JSObjectCopyPropertyNames.restype = _JSPropertyNameArray
libjavascriptcore.JSObjectCopyPropertyNames.argtypes = [_JSContext, _JSObject]
libjavascriptcore.JSObjectMakeFunction.restype = _JSObject
libjavascriptcore.JSObjectMakeFunction.argtypes = [_JSContext, _JSString, unsigned, _JSString, _JSString, _JSString,
                                                   c_int, _JSValue]
libjavascriptcore.argtypes = [_JSContext, _JSObject, unsigned, _JSValue, _JSValue]
libjavascriptcore.JSPropertyNameArrayRetain.restype = _JSPropertyNameArray
libjavascriptcore.JSPropertyNameArrayRetain.argtypes = [_JSPropertyNameArray]
libjavascriptcore.JSClassRelease.argtypes = [_JSObject, _JSClass]
libjavascriptcore.JSObjectGetPropertyAtIndex.restype = OPAQUE_PTR
libjavascriptcore.JSObjectGetPropertyAtIndex.argtypes = [_JSContext, _JSObject, unsigned, _JSValue]
libjavascriptcore.JSObjectMakeFunctionWithCallback.restype = _JSObject
libjavascriptcore.JSObjectMakeFunctionWithCallback.argtypes = [_JSContext, _JSString, JSObjectCallAsFunctionCallback]
libjavascriptcore.JSObjectMakeRegExp.restype = _JSObject
libjavascriptcore.JSObjectMakeRegExp.argtypes = [_JSContext, size_t, _JSValue, _JSValue]
libjavascriptcore.JSObjectGetPrivate.restype = c_char_p
libjavascriptcore.JSObjectGetPrivate.argtypes = [_JSObject]
libjavascriptcore.JSPropertyNameArrayGetCount.restype = size_t
libjavascriptcore.JSPropertyNameArrayGetCount.argtypes = [_JSPropertyNameArray]
libjavascriptcore.JSClassCreate.restype = _JSClass
libjavascriptcore.JSClassCreate.argtypes = [POINTER(JSClassDefinition)]
libjavascriptcore.JSObjectMake.restype = _JSObject
libjavascriptcore.JSObjectMake.argtypes = [_JSContext, _JSClass, Asciifier]
libjavascriptcore.JSObjectSetProperty.argtypes = [_JSContext, _JSObject, _JSString, _JSValue, JSPropertyAttributes,
                                                  _JSValue]
libjavascriptcore.JSObjectIsFunction.restype = bool
libjavascriptcore.JSObjectIsFunction.argtypes = [_JSContext, _JSObject]
libjavascriptcore.JSObjectMakeArray.restype = _JSObject
libjavascriptcore.JSObjectMakeArray.argtypes = [_JSContext, size_t, _JSValue, _JSValue]


def _wrapJs(context, jsobj, var_name, val):
    """
    Wrap a provided js object as a python object, with a given
    js name.  Can set a flag if js object is callable to make
    it callable in python too.  This is to be used only internally
    """
    from javascript import JSContext, JSFunction
    assert (isinstance(context, JSContext))
    if jsobj.IsFunction(context) and not isinstance(jsobj, JSFunction):
        wrapped = JSFunction(context, obj=jsobj._object(), thisobj=NULL, name=var_name)
    else:
        wrapped = jsobj  # PythonWrapper(context, jsobj, var_name, can_call)
    return wrapped


class JSCallable(object):
    def __init__(self, func, name=None, deduce_self=False):
        self._func = func
        self.__name__ = name or func.__name__
        self._c_callable = JSObjectCallAsFunctionCallback(self.callable)
        import inspect
        if deduce_self and inspect.ismethod(func):
            self.this = func.__self__
            self.deduce_self = func.__self__ is None
        else:
            self.this = None
            self.deduce_self = deduce_self

    def callable(self, context, function, thisObject, argumentCount, arguments, exception):
        from javascript import JSString, JSContext, JavascriptClass
        context = JSContext(obj=context)
        this = self.this if not self.deduce_self else JavascriptClass.items_py.get(thisObject.contents.value)
        try:
            args = [] if this is None else [this]
            for i in range(argumentCount):
                argument = JSValue(obj=arguments[i],
                                   context=context)
                # valtype = argument.GetType(context)
                args.append(to_pythonjs(context, argument))

            return_value = get_jsobj(self._func(*args), context)
            p = pointer(return_value._object())
            # return plonglong, as ctypes for c_void_p sometimes truncates pointer to 32-bit (!?!)
            return cast(p, POINTER(c_longlong)).contents.value
        except:
            import traceback
            traceback.print_exc()
            logging.error(traceback.format_exc())
            logging.error("Error in calling argument function ")
            return_value = JSValue.MakeNull(context)
            retvalc = return_value._object()
            p = pointer(retvalc)
            plonglong = cast(p, POINTER(c_longlong))
            string = JSString.CreateWithUTF8CString(traceback.format_exc())
            s = JSValue.MakeString(context, string)._strong_ref
            exception.contents = s
            string.Release()
            return plonglong.contents.value

    def C_callable(self):
        return self._c_callable


def to_jsfunction(ctxt, func):
    if JSObject.global_references.get(func):
        return JSObject.global_references[func]
    from javascript import JSString, JSFunction
    if (not hasattr(func, '__call__')) and func.IsFunction(ctxt):
        func = JSFunction(ctxt, obj=func, thisobj=NULL, name="anon")

    callable_ = JSCallable(func)
    tocall = callable_.C_callable()
    text = JSString.CreateWithUTF8CString(func.__name__ or "anonfunct")
    js_obj = JSObject.MakeFunctionWithCallback(ctxt, text, tocall)
    assert (isinstance(js_obj, JSObject))
    js_obj.references[str(tocall)] = tocall
    text.Release()
    JSObject.global_references[func] = js_obj  # cannot let this go out of scope, otherwise
    # python function object will go out of scope and cause segfault when called
    if js_obj.IsNull(ctxt):
        return None
    return js_obj


def to_pythonjs(context, val):
    value_type = val.GetType(context)
    if value_type is None or value_type == kJSTypeNull.value:
        return_value = None
    elif value_type == kJSTypeNumber.value:
        return_value = val.ToNumber(context, NULL)
    elif value_type == kJSTypeBoolean.value:
        return_value = val.ToBoolean(context)
    elif value_type == kJSTypeString.value:
        js_text = val.ToStringCopy(context, NULL)
        length = js_text.GetMaximumUTF8CStringSize()
        c_string = (c_char*(length + 1))()
        js_text.GetUTF8CString(c_string, length)
        js_text.Release()
        return_value = c_string.value.decode('ascii')
        del c_string
    elif value_type == kJSTypeObject.value or value_type == kJSTypeUndefined.value:
        js_object = val.ToObject(context, NULL)
        if js_object.IsNull(context):
            return_value = None
        else:
            return_value = _wrapJs(context, js_object, None, val=val)
    else:
        raise Exception("Invalid javascript value type encountered!: %d" % value_type.value)
    return return_value


def get_jsobj(arg, context, name=None):
    from javascript import JSString, JSFunction
    if arg is None:
        js_arg = JSValue.MakeNull(context)
    elif isinstance(arg, numbers.Number):
        js_arg = JSValue.MakeNumber(context, arg)
    elif isinstance(arg, str) or isinstance(arg, bytes) or isinstance(arg, bytearray) or isinstance(arg, unicode):
        arg += '\0'
        js_string = JSString.CreateWithUTF8CString(arg)
        js_arg = JSValue.MakeString(context, js_string)
        js_string.Release()
    elif isinstance(arg, JSFunction):
        js_arg = arg
    elif isinstance(arg, JSObject):
        js_arg = _wrapJs(context, arg, name, val=arg)
    elif isinstance(arg, collections.Callable):
        js_arg = JSObject.global_references.get(arg)
        if js_arg is None:
            js_arg = to_jsfunction(context, arg)
            assert js_arg.IsFunction(context)
            JSObject.global_references[arg] = js_arg  # must not let python object go out of scope
            js_arg.references[arg] = arg
    elif arg is True or arg is False:
        js_arg = JSValue.MakeBoolean(context, arg)
    elif isinstance(arg, dict):
        from javascript import JSString
        text = JSString.CreateWithUTF8CString("{}")
        js_arg = JSValue.MakeFromJSONString(context, text)
        js_arg = js_arg.ToObject(context, NULL)
        text.Release()
        for key, value in arg.items():
            # recursion here:
            value = get_jsobj(value, context)

            name = JSString.CreateWithUTF8CString(key)
            js_arg.SetProperty(context,
                               name,
                               value,
                               kJSPropertyAttributeNone,
                               NULL)
            name.Release()
    elif hasattr(arg, '__iter__'):
        text = JSString.CreateWithUTF8CString("[]")
        js_arg = JSValue.MakeFromJSONString(context, text)
        js_arg = js_arg.ToObject(context, NULL)
        text.Release()
        for index, value in enumerate(arg):
            # recursion here:
            value = get_jsobj(value, context)

            js_arg.SetPropertyAtIndex(context,
                                      unsigned(index),
                                      value,
                                      NULL)

    else:
        raise Exception("Unknown type %s to convert to javascript" % type(arg))
    return js_arg


# noinspection PyPep8Naming,PyProtectedMember
class JSObject(JSValue):
    global_references = {}

    """Class JSObject Constructors"""

    def __init__(self, obj, context):
        JSValue.__init__(self, obj, context)

    """Methods"""

    def GetProperty(self, propertyName, exception, ):
        from javascript import JSValue
        if propertyName:
            propertyName = propertyName._object()
        else:
            propertyName = JSValue.MakeNull(self._context)
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()

        from .javascriptcore import JSValue, JSContext
        if isinstance(self, JSContext):
            raise AttributeError("No such attribute")
        else:
            context = self._context
        if self._object() and propertyName and context._object():
            return JSValue(obj=libjavascriptcore.JSObjectGetProperty(context._object(),
                                                                     self._object(), propertyName, exception),
                           context=context)
        else:
            return None

    def JSPropertyNameAccumulatorAddName(self, accumulator, propertyName, ):
        if accumulator:
            accumulator = accumulator._object()
        else:
            accumulator = OPAQUE_PTR()
        if propertyName:
            propertyName = propertyName._object()
        else:
            propertyName = OPAQUE_PTR()
        if self._object():
            libjavascriptcore.JSPropertyNameAccumulatorAddName(self._object(), accumulator, propertyName)

    def SetPrototype(self, ctx, value, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if value:
            value = value._object()
        else:
            value = OPAQUE_PTR()

        if self._object():
            libjavascriptcore.JSObjectSetPrototype(ctx, self._object(), value)

    def HasProperty(self, ctx, propertyName, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if propertyName:
            propertyName = propertyName._object()
        else:
            propertyName = OPAQUE_PTR()

        if self._object():
            return libjavascriptcore.JSObjectHasProperty(ctx, self._object(), propertyName)

    def GetPrototype(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()

        from .javascriptcore import JSValue
        if self._object():
            return JSValue(obj=libjavascriptcore.JSObjectGetPrototype(ctx, self._object()) or OPAQUE_PTR(),
                           context=ctx)

    def CallAsConstructor(self, ctx, argumentCount, arguments, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()

        if argumentCount.value:
            args = (_JSValue * argumentCount.value)()
            for index in range(argumentCount.value):
                args[index] = arguments[index]._object()
        else:
            args = NULL
        if self._object():
            from .javascriptcore import JSObject
            return JSObject(obj=libjavascriptcore.JSObjectCallAsConstructor(ctx, self._object(), argumentCount.value,
                                                                            cast(args, OPAQUE_PTR), exception),
                            context=self._context)

    def JSPropertyNameArrayRelease(self, array, ):
        if array:
            array = array._object()
        else:
            array = OPAQUE_PTR()
        if self._object():
            libjavascriptcore.JSPropertyNameArrayRelease(self._object(), array)

    def DeleteProperty(self, ctx, propertyName, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if propertyName:
            propertyName = propertyName._object()
        else:
            propertyName = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()

        libjavascriptcore.JSObjectDeleteProperty.restype = bool
        libjavascriptcore.JSObjectDeleteProperty.argtypes = [_JSContext, _JSObject, _JSString, _JSValue]

        if self._object():
            return libjavascriptcore.JSObjectDeleteProperty(ctx, self._object(), propertyName, exception)

    def IsConstructor(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()

        libjavascriptcore.JSObjectIsConstructor.restype = bool
        libjavascriptcore.JSObjectIsConstructor.argtypes = [_JSContext, _JSObject]

        if self._object():
            return libjavascriptcore.JSObjectIsConstructor(ctx, self._object())

    def SetPropertyAtIndex(self, ctx, propertyIndex, value, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        # if propertyIndex: propertyIndex = propertyIndex._object()
        # else: propertyIndex = OPAQUE_PTR()
        if value:
            value = value._object()
        else:
            value = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()

        if self._object():
            libjavascriptcore.JSObjectSetPropertyAtIndex(ctx, self._object(), propertyIndex, value, exception)

    def SetPrivate(self, data, ):

        return libjavascriptcore.JSObjectSetPrivate(self._object(), str(data).encode('ascii'))

    def JSClassRelease(self, jsClass, ):
        if jsClass:
            jsClass = jsClass._object()
        else:
            jsClass = OPAQUE_PTR()

        if self._object():
            libjavascriptcore.JSClassRelease(self._object(), jsClass)

    def CallAsFunction(self, ctx, thisObject, argumentCount, arguments, exception, ):
        if exception and exception is not True:
            exception = exception._object()
        else:
            exception = None
        if argumentCount.value:
            args = (_JSValue * argumentCount.value)()
            for index in range(argumentCount.value):
                args[index] = arguments[index]._object()

        else:
            args = NULL
        if thisObject:
            thisObject = thisObject._object()
        else:
            thisObject = NULL

        if self._object():
            if not thisObject:
                thisObject = self._object()
            retval = libjavascriptcore.JSObjectCallAsFunction(ctx._object(),
                                                              self._object(),
                                                              thisObject,
                                                              argumentCount,
                                                              cast(args, OPAQUE_PTR),
                                                              byref(exception))
            if not retval and exception:
                string = libjavascriptcore.JSValueToStringCopy(ctx._object(), exception, NULL)
                unicodedata = libjavascriptcore.JSStringGetCharactersPtr(string)
                cstring = u''
                length = libjavascriptcore.JSStringGetLength(string)
                for i in range(length):
                    cstring += chr(unicodedata[i]) if unicodedata[i] < 256 else '?'
                    i += 1
                raise Exception(cstring)
            return JSValue(obj=retval, context=ctx)

    def CopyPropertyNames(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()

        from .javascriptcore import JSPropertyNameArray
        return JSPropertyNameArray(obj=libjavascriptcore.JSObjectCopyPropertyNames(ctx, self._object()) or OPAQUE_PTR())

    def GetPropertyAtIndex(self, propertyIndex, exc, ):
        from .javascriptcore import JSValue
        if self._object():
            return JSValue(obj=libjavascriptcore.JSObjectGetPropertyAtIndex(self._context._object(),
                                                                            self._object(),
                                                                            propertyIndex, exc) or OPAQUE_PTR(),
                           context=self._context)

    def GetPrivate(self, ):
        if self._object():
            return libjavascriptcore.JSObjectGetPrivate(self._object())

    def set(self, ctxt, name, value, ):
        from pyggi.javascript import JSString
        js_name = JSString.CreateWithUTF8CString(name)
        js_value = get_jsobj(value, ctxt)
        self.SetProperty(ctxt, js_name, js_value, kJSPropertyAttributeNone, None)
        js_name.Release()

    def SetProperty(self, ctx, propertyName, value, attributes, exception, ):
        from .javascript import JSString, JSContext
        assert (isinstance(propertyName, JSString))
        assert (isinstance(ctx, JSContext))
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if propertyName:
            propertyName = propertyName._object()
        else:
            propertyName = OPAQUE_PTR()
        if value:
            value = value._object()
        else:
            value = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()
        if self._object():
            libjavascriptcore.JSObjectSetProperty(ctx, self._object(), propertyName, value, attributes, exception)

    def IsFunction(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if self._object():
            return libjavascriptcore.JSObjectIsFunction(ctx, self._object())

    @staticmethod
    def JSClassRetain(js_class, ):
        if js_class:
            js_class = js_class._object()
        else:
            js_class = OPAQUE_PTR()
        libjavascriptcore.JSClassRetain.restype = _JSClass
        libjavascriptcore.JSClassRetain.argtypes = [_JSClass]
        from .javascriptcore import JSClass
        return JSClass(obj=libjavascriptcore.JSClassRetain(js_class) or OPAQUE_PTR())

    @staticmethod
    def MakeError(ctx, argumentCount, arguments, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if arguments:
            arguments = arguments._object()
        else:
            arguments = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()
        libjavascriptcore.JSObjectMakeError.restype = _JSObject
        libjavascriptcore.JSObjectMakeError.argtypes = [_JSContext, size_t, _JSValue, _JSValue]
        return JSObject(obj=libjavascriptcore.JSObjectMakeError(ctx, argumentCount,
                                                                arguments, exception) or OPAQUE_PTR(),
                        context=ctx)

    @staticmethod
    def MakeFunctionWithCallback(ctx, name, callAsFunction, ):
        if name:
            name = name._object()
        else:
            name = OPAQUE_PTR()
        from pyggi.javascript import JSFunction
        obj = libjavascriptcore.JSObjectMakeFunctionWithCallback(ctx._object(), name, callAsFunction, )

        if libjavascriptcore.JSValueIsNull(ctx._object(), obj):
            return None
        return JSFunction(context=ctx, obj=obj, thisobj=None, name=name)

    @staticmethod
    def MakeArray(ctx, argumentCount, arguments, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if arguments:
            arguments = arguments._object()
        else:
            arguments = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()
        return JSObject(obj=libjavascriptcore.JSObjectMakeArray(ctx, argumentCount,
                                                                arguments, exception) or OPAQUE_PTR(),
                        context=ctx)

    @staticmethod
    def MakeConstructor(ctx, jsClass, callAsConstructor, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if jsClass:
            jsClass = jsClass._object()
        else:
            jsClass = OPAQUE_PTR()
        libjavascriptcore.JSObjectMakeConstructor.restype = _JSObject
        libjavascriptcore.JSObjectMakeConstructor.argtypes = [_JSContext, _JSClass, JSObjectCallAsConstructorCallback]
        return JSObject(obj=libjavascriptcore.JSObjectMakeConstructor(ctx, jsClass, callAsConstructor) or OPAQUE_PTR(),
                        context=ctx)

    @staticmethod
    def MakeDate(ctx, argumentCount, arguments, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if arguments:
            arguments = arguments._object()
        else:
            arguments = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()
        libjavascriptcore.JSObjectMakeDate.restype = _JSObject
        libjavascriptcore.JSObjectMakeDate.argtypes = [_JSContext, size_t, _JSValue, _JSValue]
        return JSObject(obj=libjavascriptcore.JSObjectMakeDate(ctx, argumentCount,
                                                               arguments, exception) or OPAQUE_PTR(),
                        context=ctx)

    @staticmethod
    def JSPropertyNameArrayRetain(array):
        if array:
            array = array._object()
        else:
            array = OPAQUE_PTR()
        from .javascriptcore import JSPropertyNameArray
        return JSPropertyNameArray(obj=libjavascriptcore.JSPropertyNameArrayRetain(array) or OPAQUE_PTR())

    @staticmethod
    def JSPropertyNameArrayGetNameAtIndex(array, index, ):
        if array:
            array = array._object()
        else:
            array = OPAQUE_PTR()
        libjavascriptcore.JSPropertyNameArrayGetNameAtIndex.restype = _JSString
        libjavascriptcore.JSPropertyNameArrayGetNameAtIndex.argtypes = [_JSPropertyNameArray, size_t]
        from .javascriptcore import JSString
        return JSString(obj=libjavascriptcore.JSPropertyNameArrayGetNameAtIndex(array, index) or OPAQUE_PTR())

    @staticmethod
    def MakeFunction(ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if name:
            name = name._object()
        else:
            name = OPAQUE_PTR()
        if parameterCount:
            parameterCount = parameterCount._object()
        else:
            parameterCount = OPAQUE_PTR()
        if parameterNames:
            parameterNames = parameterNames._object()
        else:
            parameterNames = OPAQUE_PTR()
        if body:
            body = body._object()
        else:
            body = OPAQUE_PTR()
        if sourceURL:
            sourceURL = sourceURL._object()
        else:
            sourceURL = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()
        from .javascriptcore import JSObject
        return JSObject(
                obj=libjavascriptcore.JSObjectMakeFunction(ctx, name, parameterCount, parameterNames, body, sourceURL,
                                                           startingLineNumber, exception, ) or OPAQUE_PTR(),
                context=ctx)

    @staticmethod
    def Make(ctx, jsClass, data, ):
        if jsClass:
            jsClass = jsClass._object()
        else:
            jsClass = OPAQUE_PTR()
        if data is not None:
            data = str(data).encode('ascii')
        obj = libjavascriptcore.JSObjectMake(ctx._object(), jsClass, data)
        return JSObject(obj=obj,
                        context=ctx)

    @staticmethod
    def JSPropertyNameArrayGetCount(array, ):
        if array:
            array = array._object()
        else:
            array = OPAQUE_PTR()

        return libjavascriptcore.JSPropertyNameArrayGetCount(array, )

    @staticmethod
    def MakeRegExp(ctx, argumentCount, arguments, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        if arguments:
            arguments = arguments._object()
        else:
            arguments = OPAQUE_PTR()
        if exception:
            exception = exception._object()
        else:
            exception = OPAQUE_PTR()
        from .javascriptcore import JSObject
        return JSObject(obj=libjavascriptcore.JSObjectMakeRegExp(ctx, argumentCount,
                                                                 arguments, exception, ) or OPAQUE_PTR(),
                        context=ctx)

    @staticmethod
    def JSClassCreate(definition, ):
        from .javascriptcore import JSClass
        obj = libjavascriptcore.JSClassCreate(definition)
        return JSClass(obj=obj or OPAQUE_PTR())

    def __getattr__(self, attr):
        from .javascriptcore import JSContext
        if not self._context:
            assert (self._context and isinstance(self, JSContext))
        if isinstance(self, JSContext):
            context = self
        else:
            assert self._context
            context = self._context
        if attr == "__len__":
            from .javascript import JSString
            name = JSString.CreateWithUTF8CString("length")
            length = self.GetProperty(name, NULL)
            name.Release()
            if length.GetType(context) == kJSTypeUndefined.value:
                raise AttributeError("No such attribute: length")
            val = int(length.ToNumber(context, NULL))

            def _len():
                return val

            return _len
        from .javascriptcore import JSString
        text = JSString.CreateWithUTF8CString(attr)
        prop = self.GetProperty(text, NULL)
        text.Release()
        if prop is None:
            return None
        jstype = prop.GetType(context)
        if jstype == kJSTypeNull.value:
            return None  # object.__getattribute__(self, attr)
        elif jstype == kJSTypeObject.value or jstype == kJSTypeUndefined.value:
            propobj = prop.ToObject(context, NULL)
            if propobj.IsFunction(context):
                from .javascript import JSFunction
                jsfunc = JSFunction(context, obj=prop._object(), thisobj=self, name=attr)
                return jsfunc
            else:
                propobj._name = attr
                return propobj
        elif jstype == kJSTypeNumber.value:
            val = prop.ToNumber(context, NULL)
            return val
        elif jstype == kJSTypeBoolean.value:
            val = prop.ToBoolean(context)
            return val
        elif jstype == kJSTypeString.value:
            val = prop.ToPyString(context, NULL)
            return val
        raise Exception("unknown javascript type")

    def __iter__(self, index):
        from javascript import JSContext
        if isinstance(self, JSContext):
            context = self
        else:
            assert self._context
            context = self._context
        prop = self.GetPropertyAtIndex(index, NULL)
        return to_pythonjs(context, prop)
