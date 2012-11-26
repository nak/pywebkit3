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

from ctypes import *
from gtk3_types import *
from javascriptcore_types import *


"""Derived Pointer Types"""
_JSValue = c_void_p
_JSObject = c_void_p
_JSContext = c_void_p
_JSClass = c_void_p
_JSString = c_void_p
"""Enumerations"""

import _javascriptcore_JSObject
class JSValue( _javascriptcore_JSObject.JSObject):
    """Class JSValue Constructors"""

    """Methods"""
    def JSValueUnprotect(self,  ctx, value,):
        libjavascriptcore.JSValueUnprotect.argtypes = [c_void_p, _JSContext,_JSValue]
        libjavascriptcore.JSValueUnprotect(self._object, ctx, value, )

    def JSValueProtect(self,  ctx, value,):

        libjavascriptcore.JSValueProtect.argtypes = [c_void_p, _JSContext,_JSValue]
        libjavascriptcore.JSValueProtect(self._object, ctx, value, )

    @staticmethod
    def JSValueToObject( ctx, value, exception,):
        libjavascriptcore.JSValueToObject.restype = _JSObject
        libjavascriptcore.JSValueToObject.argtypes = [_JSContext,_JSValue,JSValue]
        return libjavascriptcore.JSValueToObject(ctx, value, exception, )

    @staticmethod
    def JSValueCreateJSONString( ctx, value, exception,):
        libjavascriptcore.JSValueCreateJSONString.restype = _JSString
        libjavascriptcore.JSValueCreateJSONString.argtypes = [_JSContext,_JSValue,JSValue]
        return libjavascriptcore.JSValueCreateJSONString(ctx, value, exception, )

    @staticmethod
    def JSValueIsObject( ctx, value,):
        libjavascriptcore.JSValueIsObject.restype = bool
        libjavascriptcore.JSValueIsObject.argtypes = [_JSContext,_JSValue]
        return libjavascriptcore.JSValueIsObject(ctx, value, )

    @staticmethod
    def JSValueToBoolean( ctx, value,):
        libjavascriptcore.JSValueToBoolean.restype = bool
        libjavascriptcore.JSValueToBoolean.argtypes = [_JSContext,_JSValue]
        return libjavascriptcore.JSValueToBoolean(ctx, value, )

    @staticmethod
    def JSValueIsString( ctx, value,):
        libjavascriptcore.JSValueIsString.restype = bool
        libjavascriptcore.JSValueIsString.argtypes = [_JSContext,_JSValue]
        return libjavascriptcore.JSValueIsString(ctx, value, )

    @staticmethod
    def JSValueMakeString( ctx, string,):
        libjavascriptcore.JSValueMakeString.restype = _JSValue
        libjavascriptcore.JSValueMakeString.argtypes = [_JSContext,_JSString]
        return libjavascriptcore.JSValueMakeString(ctx, string, )

    @staticmethod
    def JSValueIsUndefined( ctx, value,):
        libjavascriptcore.JSValueIsUndefined.restype = bool
        libjavascriptcore.JSValueIsUndefined.argtypes = [_JSContext,_JSValue]
        return libjavascriptcore.JSValueIsUndefined(ctx, value, )

    @staticmethod
    def JSValueIsObjectOfClass( ctx, value, jsClass,):
        libjavascriptcore.JSValueIsObjectOfClass.restype = bool
        libjavascriptcore.JSValueIsObjectOfClass.argtypes = [_JSContext,_JSValue,_JSClass]
        return libjavascriptcore.JSValueIsObjectOfClass(ctx, value, jsClass, )

    @staticmethod
    def JSValueMakeNull( ctx,):
        libjavascriptcore.JSValueMakeNull.restype = _JSValue
        libjavascriptcore.JSValueMakeNull.argtypes = [_JSContext]
        return libjavascriptcore.JSValueMakeNull(ctx, )

    @staticmethod
    def JSValueMakeBoolean( ctx, val):
        libjavascriptcore.JSValueMakeBoolean.restype = _JSValue
        libjavascriptcore.JSValueMakeBoolean.argtypes = [_JSContext, c_ubyte]
        return libjavascriptcore.JSValueMakeBoolean(ctx, c_ubyte(val))

    @staticmethod
    def JSValueMakeNumber( ctx,number):
        libjavascriptcore.JSValueMakeNumber.restype = _JSValue
        libjavascriptcore.JSValueMakeNumber.argtypes = [_JSContext, c_double]
        return libjavascriptcore.JSValueMakeNumber(ctx, c_double(number))

    @staticmethod
    def JSValueIsNull( ctx, value,):
        libjavascriptcore.JSValueIsNull.restype = bool
        libjavascriptcore.JSValueIsNull.argtypes = [_JSContext,_JSValue]
        return libjavascriptcore.JSValueIsNull(ctx, value, )

    @staticmethod
    def JSValueMakeUndefined( ctx,):
        libjavascriptcore.JSValueMakeUndefined.restype = _JSValue
        libjavascriptcore.JSValueMakeUndefined.argtypes = [_JSContext]
        return libjavascriptcore.JSValueMakeUndefined(ctx, )

    @staticmethod
    def JSValueToStringCopy( ctx, value, exception,):
        libjavascriptcore.JSValueToStringCopy.restype = _JSString
        libjavascriptcore.JSValueToStringCopy.argtypes = [_JSContext,_JSValue,JSValue]
        return libjavascriptcore.JSValueToStringCopy(ctx, value, exception, )

    @staticmethod
    def JSValueMakeFromJSONString( ctx, string,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if string : string = string._object
        else : string = c_void_p()
        libjavascriptcore.JSValueMakeFromJSONString.restype = _JSValue
        libjavascriptcore.JSValueMakeFromJSONString.argtypes = [_JSContext,_JSString]
        return libjavascriptcore.JSValueMakeFromJSONString(ctx, string, )

    @staticmethod
    def JSValueIsNumber( ctx, value,):
        libjavascriptcore.JSValueIsNumber.restype = bool
        libjavascriptcore.JSValueIsNumber.argtypes = [_JSContext,_JSValue]
        return libjavascriptcore.JSValueIsNumber(ctx, value, )

    @staticmethod
    def JSValueIsEqual( ctx, a, b, exception,):
        libjavascriptcore.JSValueIsEqual.restype = bool
        libjavascriptcore.JSValueIsEqual.argtypes = [_JSContext,_JSValue,_JSValue,JSValue]
        return libjavascriptcore.JSValueIsEqual(ctx, a, b, exception, )

    @staticmethod
    def JSValueToNumber( ctx, value, exception,):
        libjavascriptcore.JSValueToNumber.restype = double
        libjavascriptcore.JSValueToNumber.argtypes = [_JSContext,_JSValue,JSValue]
        return libjavascriptcore.JSValueToNumber(ctx, value, exception, )

    @staticmethod
    def JSValueIsInstanceOfConstructor( ctx, value, ructor, exception,):
        libjavascriptcore.JSValueIsInstanceOfConstructor.restype = bool
        libjavascriptcore.JSValueIsInstanceOfConstructor.argtypes = [_JSContext,_JSValue,_JSObject,JSValue]
        return libjavascriptcore.JSValueIsInstanceOfConstructor(ctx, value, ructor, exception, )

    @staticmethod
    def JSValueIsStrictEqual( ctx, a, b,):
        if ctx : ctx = ctx._object
        libjavascriptcore.JSValueIsStrictEqual.restype = bool
        libjavascriptcore.JSValueIsStrictEqual.argtypes = [_JSContext,_JSValue,_JSValue]
        return libjavascriptcore.JSValueIsStrictEqual(ctx, a, b, )

    @staticmethod
    def JSValueIsBoolean( ctx, value,):
        libjavascriptcore.JSValueIsBoolean.restype = bool
        libjavascriptcore.JSValueIsBoolean.argtypes = [_JSContext,_JSValue]
        return libjavascriptcore.JSValueIsBoolean(ctx, value, )

    @staticmethod
    def JSValueGetType( ctx, value,):
        libjavascriptcore.JSValueGetType.restype = JSType
        libjavascriptcore.JSValueGetType.argtypes = [_JSContext,_JSValue]
        return libjavascriptcore.JSValueGetType(ctx, value, )

