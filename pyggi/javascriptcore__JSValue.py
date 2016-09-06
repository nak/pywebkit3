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
from .gtk3_types import *
from .javascriptcore_types import *
import weakref

"""Derived Pointer Types"""
_JSObject = POINTER(c_void_p)
_JSValue = POINTER(c_void_p)
_JSContextGroup = POINTER(c_void_p)
_JSPropertyNameArray = POINTER(c_void_p)
_JSClass = POINTER(c_void_p)
_JSString = POINTER(c_void_p)
_JSContext = POINTER(c_void_p)

libjavascriptcore.JSValueToObject.restype = _JSObject
libjavascriptcore.JSValueToObject.argtypes = [_JSContext, _JSValue, _JSValue]
libjavascriptcore.JSValueIsUndefined.restype = bool
libjavascriptcore.JSValueIsUndefined.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueIsObjectOfClass.restype = bool
libjavascriptcore.JSValueIsObjectOfClass.argtypes = [_JSContext, _JSValue, _JSClass]
libjavascriptcore.JSValueIsStrictEqual.restype = bool
libjavascriptcore.JSValueIsStrictEqual.argtypes = [_JSContext, _JSValue, _JSValue]
libjavascriptcore.JSValueIsNull.restype = bool
libjavascriptcore.JSValueIsNull.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueProtect.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueIsObject.restype = bool
libjavascriptcore.JSValueIsObject.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueIsBoolean.restype = bool
libjavascriptcore.JSValueIsBoolean.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueIsString.restype = bool
libjavascriptcore.JSValueIsString.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueToStringCopy.restype = _JSString
libjavascriptcore.JSValueToStringCopy.argtypes = [_JSContext, _JSValue, _JSValue]
libjavascriptcore.JSValueToBoolean.restype = bool
libjavascriptcore.JSValueToBoolean.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueIsEqual.restype = bool
libjavascriptcore.JSValueIsEqual.argtypes = [_JSContext, _JSValue, _JSValue, _JSValue]
libjavascriptcore.JSValueCreateJSONString.restype = _JSString
libjavascriptcore.JSValueCreateJSONString.argtypes = [_JSContext, _JSValue, unsigned, _JSValue]
libjavascriptcore.JSValueUnprotect.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueGetType.restype = JSType
libjavascriptcore.JSValueGetType.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueToNumber.restype = double
libjavascriptcore.JSValueToNumber.argtypes = [_JSContext, _JSValue, _JSValue]
libjavascriptcore.JSValueMakeNumber.restype = _JSValue
libjavascriptcore.JSValueMakeNumber.argtypes = [_JSContext, c_double]
libjavascriptcore.JSValueMakeUndefined.restype = _JSValue
libjavascriptcore.JSValueMakeUndefined.argtypes = [_JSContext]
libjavascriptcore.JSValueMakeNull.restype = _JSValue
libjavascriptcore.JSValueMakeNull.argtypes = [_JSContext]
libjavascriptcore.JSValueMakeBoolean.restype = _JSValue
libjavascriptcore.JSValueMakeBoolean.argtypes = [_JSContext, c_byte]
libjavascriptcore.JSValueMakeString.restype = _JSValue
libjavascriptcore.JSValueMakeString.argtypes = [_JSContext, _JSString]
libjavascriptcore.JSValueUnprotect.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueIsInstanceOfConstructor.restype = c_char
libjavascriptcore.JSValueIsInstanceOfConstructor.argtypes = [_JSContext, _JSValue, _JSObject, _JSValue]
libjavascriptcore.JSValueIsNumber.restype = c_char
libjavascriptcore.JSValueIsNumber.argtypes = [_JSContext, _JSValue]
libjavascriptcore.JSValueMakeFromJSONString.restype = _JSValue
libjavascriptcore.JSValueMakeFromJSONString.argtypes = [_JSContext, _JSString]


# noinspection PyProtectedMember,PyPep8Naming
class JSValue(object):
    """Class JSValue Constructors"""

    def __init__(self, obj, context):
        if not obj:
            obj = JSValue.MakeNull(context)._strong_ref
        self._object = weakref.ref(obj)
        self._strong_ref = obj
        self._context = context
        self._name = None
        self._do_protect = context is not None
        from .javascript import JSContext

        if self._do_protect:
            libjavascriptcore.JSValueProtect(self._context._object(),
                                             self._object())
        self.references = {}
        assert (isinstance(context, JSContext) or context is None)

    """Methods"""
    def IsInstanceOfConstructor(self, ctx, ructor, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if ructor:
            ructor = ructor._object()
        else:
            ructor = POINTER(c_void_p)()
        if exception:
            exception = exception._object()
        else:
            exception = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsInstanceOfConstructor(ctx, self._object(), ructor, exception)

    def ToObject(self, ctx, exception):
        if exception:
            exception = exception._object()
        else:
            exception = POINTER(c_void_p)()

        from .javascriptcore import JSObject
        if self._object():
            return JSObject(obj=libjavascriptcore.JSValueToObject(ctx._object(), self._object(), exception),
                            context=ctx)

    def IsUndefined(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()

        if self._object():
            return libjavascriptcore.JSValueIsUndefined(ctx, self._object())

    def IsObjectOfClass(self, ctx, jsClass, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if jsClass:
            jsClass = jsClass._object()
        else:
            jsClass = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsObjectOfClass(ctx, self._object(), jsClass)

    def IsStrictEqual(self, ctx, b, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if b:
            b = b._object()
        else:
            b = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsStrictEqual(ctx, self._object(), b)

    def IsNull(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsNull(ctx, self._object())

    def Protect(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if self._object():
            libjavascriptcore.JSValueProtect(ctx, self._object())

    def IsObject(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsObject(ctx, self._object())

    def IsBoolean(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsBoolean(ctx, self._object())

    def IsString(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsString(ctx, self._object())

    def ToStringCopy(self, ctx, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if exception:
            exception = exception._object()
        else:
            exception = POINTER(c_void_p)()

        from .javascriptcore import JSString
        if self._object():
            return JSString(
                obj=libjavascriptcore.JSValueToStringCopy(ctx, self._object(), exception) or POINTER(c_void_p)())

    def ToPyString(self, ctx, exception):
        js_text = self.ToStringCopy(ctx, exception)
        length = js_text.GetMaximumUTF8CStringSize()
        c_string = (c_char*(length+1))()
        js_text.GetUTF8CString(c_string, length)
        js_text.Release()
        return c_string.value

    def ToBoolean(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueToBoolean(ctx, self._object())

    def IsNumber(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()

        if self._object():
            return libjavascriptcore.JSValueIsNumber(ctx, self._object())

    def IsEqual(self, ctx, b, exception, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if b:
            b = b._object()
        else:
            b = POINTER(c_void_p)()
        if exception:
            exception = exception._object()
        else:
            exception = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsEqual(ctx, self._object(), b, exception)

    def CreateJSONString(self, ctx, indent, exception, ):
        if indent:
            indent = indent._object()
        else:
            indent = POINTER(c_void_p)()
        if exception:
            exception = exception._object()
        else:
            exception = POINTER(c_void_p)()
        from .javascriptcore import JSString
        if self._object():
            return JSString(obj=libjavascriptcore.JSValueCreateJSONString(ctx._object(), self._object(), indent,
                                                                          exception) or POINTER(c_void_p)())

    def Unprotect(self, ctx, ):
        if self._object() and ctx._object():
            libjavascriptcore.JSValueUnprotect(ctx._object(), self._object())

    def GetType(self, ctx, ):
        # import logging,traceback
        # logging.error(traceback.format_stack())
        if ctx:
            if not isinstance(ctx, POINTER(c_void_p)):
                ctx = ctx._object()
        else:
            ctx = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueGetType(ctx, self._object())

    def ToNumber(self, ctx, exception, ):
        if exception:
            exception = exception._object()
        else:
            exception = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueToNumber(ctx._object(), self._object(), exception)

    @staticmethod
    def MakeNumber(ctx, number, ):
        obj = libjavascriptcore.JSValueMakeNumber(ctx._object(),
                                                  c_double(number), )
        return JSValue(obj, context=ctx)

    @staticmethod
    def MakeUndefined(ctx, ):
        return JSValue(obj=libjavascriptcore.JSValueMakeUndefined(ctx._object(), ), context=ctx)

    @staticmethod
    def MakeNull(ctx, ):
        return JSValue(obj=libjavascriptcore.JSValueMakeNull(ctx._object(), ),
                       context=ctx)

    @staticmethod
    def MakeFromJSONString(ctx, string, ):
        if string:
            string = string._object()
        else:
            string = POINTER(c_void_p)()
        return JSValue(obj=libjavascriptcore.JSValueMakeFromJSONString(ctx._object(), string), context=ctx)

    @staticmethod
    def MakeBoolean(ctx, boolean, ):
        return JSValue(obj=libjavascriptcore.JSValueMakeBoolean(ctx._object(), c_byte(boolean)), context=ctx)

    @staticmethod
    def MakeString(ctx, string, ):
        if string:
            string = string._object()
        else:
            string = POINTER(c_void_p)()
        from .javascriptcore import JSValue
        retval = JSValue(obj=libjavascriptcore.JSValueMakeString(ctx._object(), string), context=ctx)
        return retval

    def __del__(self):
        try:
            if self._do_protect:
                libjavascriptcore.JSValueUnprotect(self._context._object(),
                                                   self._object())
        except:
            import traceback
            traceback.print_exc()
            pass
        self._do_protect = False
        self._context = None
        self._strong_ref = None
        self._object = None
