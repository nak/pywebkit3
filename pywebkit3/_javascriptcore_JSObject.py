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
_JSPropertyNameArray = c_void_p
_JSContext = c_void_p
_JSClass = c_void_p
_JSPropertyNameAccumulator = c_void_p
_JSString = c_void_p
_JSValue = c_void_p
_JSObject = c_void_p
"""Enumerations"""

class JSObject( object):
    """Class JSObject Constructors"""

    """Methods"""
    def JSPropertyNameAccumulatorAddName(self,  accumulator, propertyName,):
        if accumulator : accumulator = accumulator._object
        else : accumulator = c_void_p()
        if propertyName : propertyName = propertyName._object
        else : propertyName = c_void_p()

        libjavascriptcore.JSPropertyNameAccumulatorAddName.argtypes = [c_void_p, _JSPropertyNameAccumulator,_JSString]
        libjavascriptcore.JSPropertyNameAccumulatorAddName(self._object, accumulator, propertyName, )

    def JSObjectSetPrototype(self,  ctx, object, value,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if value : value = value._object
        else : value = c_void_p()

        libjavascriptcore.JSObjectSetPrototype.argtypes = [c_void_p, _JSContext,_JSObject,_JSValue]
        libjavascriptcore.JSObjectSetPrototype(self._object, ctx, object, value, )

    def JSPropertyNameArrayRelease(self,  array,):
        if array : array = array._object
        else : array = c_void_p()

        libjavascriptcore.JSPropertyNameArrayRelease.argtypes = [c_void_p, _JSPropertyNameArray]
        libjavascriptcore.JSPropertyNameArrayRelease(self._object, array, )

    def JSObjectSetPropertyAtIndex(self,  ctx, object, value, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if value : value = value._object
        else : value = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()

        libjavascriptcore.JSObjectSetPropertyAtIndex.argtypes = [c_void_p, _JSContext,_JSObject,_JSValue,JSValue]
        libjavascriptcore.JSObjectSetPropertyAtIndex(self._object, ctx, object, value, exception, )

    def JSObjectSetPrivate(self, ):

        libjavascriptcore.JSObjectSetPrivate.restype = bool
        return libjavascriptcore.JSObjectSetPrivate(self._object, )

    def JSClassRelease(self,  jsClass,):
        if jsClass : jsClass = jsClass._object
        else : jsClass = c_void_p()

        libjavascriptcore.JSClassRelease.argtypes = [c_void_p, _JSClass]
        libjavascriptcore.JSClassRelease(self._object, jsClass, )

    def JSObjectGetPrivate(self, ):

        libjavascriptcore.JSObjectGetPrivate.restype = c_char_p
        return libjavascriptcore.JSObjectGetPrivate(self._object, )

    @staticmethod
    def JSObjectSetProperty(ctx, object, propertyName, value, attributes, exception,):
        libjavascriptcore.JSObjectSetProperty.restype = c_void_p
        libjavascriptcore.JSObjectSetProperty.argtypes = [ _JSContext,_JSObject,_JSString,_JSValue,JSPropertyAttributes, c_void_p]
        libjavascriptcore.JSObjectSetProperty( ctx, object, propertyName, value, attributes, exception, )

    @staticmethod
    def JSClassRetain( jsClass,):
        if jsClass : jsClass = jsClass._object
        else : jsClass = c_void_p()
        libjavascriptcore.JSClassRetain.restype = _JSClass
        libjavascriptcore.JSClassRetain.argtypes = [_JSClass]
        return libjavascriptcore.JSClassRetain(jsClass, )

    @staticmethod
    def JSObjectMakeFunctionWithCallback( ctx, name, callAsFunction,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if name : name = name._object
        else : name = c_void_p()
        libjavascriptcore.JSObjectMakeFunctionWithCallback.restype = _JSObject
        libjavascriptcore.JSObjectMakeFunctionWithCallback.argtypes = [_JSContext,_JSString,JSObjectCallAsFunctionCallback]
        return libjavascriptcore.JSObjectMakeFunctionWithCallback(ctx, name, callAsFunction, )

    @staticmethod
    def JSPropertyNameArrayRetain( array,):
        if array : array = array._object
        else : array = c_void_p()
        libjavascriptcore.JSPropertyNameArrayRetain.restype = _JSPropertyNameArray
        libjavascriptcore.JSPropertyNameArrayRetain.argtypes = [_JSPropertyNameArray]
        return libjavascriptcore.JSPropertyNameArrayRetain(array, )

    @staticmethod
    def JSObjectCopyPropertyNames( ctx, object,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        libjavascriptcore.JSObjectCopyPropertyNames.restype = _JSPropertyNameArray
        libjavascriptcore.JSObjectCopyPropertyNames.argtypes = [_JSContext,_JSObject]
        return libjavascriptcore.JSObjectCopyPropertyNames(ctx, object, )

    @staticmethod
    def JSObjectMake( ctx, jsClass, data,):
        libjavascriptcore.JSObjectMake.restype = _JSObject
        libjavascriptcore.JSObjectMake.argtypes = [_JSContext,_JSClass,_JSContext]
        return libjavascriptcore.JSObjectMake(ctx, jsClass, data, )

    @staticmethod
    def JSObjectIsFunction( ctx, object,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        libjavascriptcore.JSObjectIsFunction.restype = bool
        libjavascriptcore.JSObjectIsFunction.argtypes = [_JSContext,_JSObject]
        return libjavascriptcore.JSObjectIsFunction(ctx, object, )

    @staticmethod
    def JSObjectGetPrototype( ctx, object,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        libjavascriptcore.JSObjectGetPrototype.restype = _JSValue
        libjavascriptcore.JSObjectGetPrototype.argtypes = [_JSContext,_JSObject]
        return libjavascriptcore.JSObjectGetPrototype(ctx, object, )

    @staticmethod
    def JSObjectMakeArray( ctx, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectMakeArray.restype = _JSObject
        libjavascriptcore.JSObjectMakeArray.argtypes = [_JSContext,size_t,JSValue,JSValue]
        return libjavascriptcore.JSObjectMakeArray(ctx, argumentCount, arguments, exception, )

    @staticmethod
    def JSPropertyNameArrayGetNameAtIndex( array, index,):
        if array : array = array._object
        else : array = c_void_p()
        libjavascriptcore.JSPropertyNameArrayGetNameAtIndex.restype = _JSString
        libjavascriptcore.JSPropertyNameArrayGetNameAtIndex.argtypes = [_JSPropertyNameArray,size_t]
        return libjavascriptcore.JSPropertyNameArrayGetNameAtIndex(array, index, )

    @staticmethod
    def JSObjectCallAsConstructor( ctx, object, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectCallAsConstructor.restype = _JSObject
        libjavascriptcore.JSObjectCallAsConstructor.argtypes = [_JSContext,_JSObject,size_t,JSValue,JSValue]
        return libjavascriptcore.JSObjectCallAsConstructor(ctx, object, argumentCount, arguments, exception, )

    @staticmethod
    def JSObjectMakeRegExp( ctx, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectMakeRegExp.restype = _JSObject
        libjavascriptcore.JSObjectMakeRegExp.argtypes = [_JSContext,size_t,JSValue,JSValue]
        return libjavascriptcore.JSObjectMakeRegExp(ctx, argumentCount, arguments, exception, )

    @staticmethod
    def JSClassCreate( definition,):
        libjavascriptcore.JSClassCreate.restype = _JSClass
        libjavascriptcore.JSClassCreate.argtypes = [POINTER(JSClassDefinition)]
        return libjavascriptcore.JSClassCreate(definition, )

    @staticmethod
    def JSObjectMakeError( ctx, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectMakeError.restype = _JSObject
        libjavascriptcore.JSObjectMakeError.argtypes = [_JSContext,size_t,JSValue,JSValue]
        return libjavascriptcore.JSObjectMakeError(ctx, argumentCount, arguments, exception, )

    @staticmethod
    def JSObjectDeleteProperty( ctx, object, propertyName, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if propertyName : propertyName = propertyName._object
        else : propertyName = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectDeleteProperty.restype = bool
        libjavascriptcore.JSObjectDeleteProperty.argtypes = [_JSContext,_JSObject,_JSString,JSValue]
        return libjavascriptcore.JSObjectDeleteProperty(ctx, object, propertyName, exception, )

    @staticmethod
    def JSObjectMakeConstructor( ctx, jsClass, callAsConstructor,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if jsClass : jsClass = jsClass._object
        else : jsClass = c_void_p()
        libjavascriptcore.JSObjectMakeConstructor.restype = _JSObject
        libjavascriptcore.JSObjectMakeConstructor.argtypes = [_JSContext,_JSClass,JSObjectCallAsConstructorCallback]
        return libjavascriptcore.JSObjectMakeConstructor(ctx, jsClass, callAsConstructor, )

    @staticmethod
    def JSObjectMakeFunction( ctx, name, parameterNames, body, sourceURL, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if name : name = name._object
        else : name = c_void_p()
        if parameterNames : parameterNames = parameterNames._object
        else : parameterNames = c_void_p()
        if body : body = body._object
        else : body = c_void_p()
        if sourceURL : sourceURL = sourceURL._object
        else : sourceURL = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectMakeFunction.restype = _JSObject
        libjavascriptcore.JSObjectMakeFunction.argtypes = [_JSContext,_JSString,JSString,_JSString,_JSString,JSValue]
        return libjavascriptcore.JSObjectMakeFunction(ctx, name, parameterNames, body, sourceURL, exception, )

    @staticmethod
    def JSObjectGetPropertyAtIndex( ctx, object, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectGetPropertyAtIndex.restype = _JSValue
        libjavascriptcore.JSObjectGetPropertyAtIndex.argtypes = [_JSContext,_JSObject,JSValue]
        return libjavascriptcore.JSObjectGetPropertyAtIndex(ctx, object, exception, )

    @staticmethod
    def JSObjectGetProperty( ctx, object, propertyName, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if propertyName : propertyName = propertyName._object
        else : propertyName = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectGetProperty.restype = _JSValue
        libjavascriptcore.JSObjectGetProperty.argtypes = [_JSContext,_JSObject,_JSString,JSValue]
        return libjavascriptcore.JSObjectGetProperty(ctx, object, propertyName, exception, )

    @staticmethod
    def JSObjectHasProperty( ctx, object, propertyName,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if propertyName : propertyName = propertyName._object
        else : propertyName = c_void_p()
        libjavascriptcore.JSObjectHasProperty.restype = bool
        libjavascriptcore.JSObjectHasProperty.argtypes = [_JSContext,_JSObject,_JSString]
        return libjavascriptcore.JSObjectHasProperty(ctx, object, propertyName, )

    @staticmethod
    def JSObjectIsConstructor( ctx, object,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        libjavascriptcore.JSObjectIsConstructor.restype = bool
        libjavascriptcore.JSObjectIsConstructor.argtypes = [_JSContext,_JSObject]
        return libjavascriptcore.JSObjectIsConstructor(ctx, object, )

    @staticmethod
    def JSObjectMakeDate( ctx, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectMakeDate.restype = _JSObject
        libjavascriptcore.JSObjectMakeDate.argtypes = [_JSContext,size_t,JSValue,JSValue]
        return libjavascriptcore.JSObjectMakeDate(ctx, argumentCount, arguments, exception, )

    @staticmethod
    def JSObjectCallAsFunction( ctx, object, thisObject, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if thisObject : thisObject = thisObject._object
        else : thisObject = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libjavascriptcore.JSObjectCallAsFunction.restype = _JSValue
        libjavascriptcore.JSObjectCallAsFunction.argtypes = [_JSContext,_JSObject,_JSObject,size_t,JSValue,JSValue]
        return libjavascriptcore.JSObjectCallAsFunction(ctx, object, thisObject, argumentCount, arguments, exception, )

    @staticmethod
    def JSPropertyNameArrayGetCount( array,):
        if array : array = array._object
        else : array = c_void_p()
        libjavascriptcore.JSPropertyNameArrayGetCount.restype = size_t
        libjavascriptcore.JSPropertyNameArrayGetCount.argtypes = [_JSPropertyNameArray]
        return libjavascriptcore.JSPropertyNameArrayGetCount(array, )

