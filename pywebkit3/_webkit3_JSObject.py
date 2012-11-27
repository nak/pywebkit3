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
from webkit3_types import *
    
    
"""Derived Pointer Types"""
_WebKitNetworkResponse = c_void_p
_WebKitWebWindowFeatures = c_void_p
_GdkPixbuf = c_void_p
_WebKitWebFrame = c_void_p
_GList = c_void_p
_char = c_void_p
_GtkTargetList = c_void_p
_GtkWidget = c_void_p
_JSClass = c_void_p
_JSGlobalContext = c_void_p
__JSGlobalContext = c_void_p
__WebKitDOMNode = c_void_p
_WebKitSecurityOrigin = c_void_p
__WebKitNetworkRequest = c_void_p
_JSContext = c_void_p
_SoupMessage = c_void_p
_WebKitWebDataSource = c_void_p
_WebKitWebSettings = c_void_p
__JSClass = c_void_p
__WebKitWebHistoryItem = c_void_p
__GList = c_void_p
_JSContextGroup = c_void_p
__JSString = c_void_p
__WebKitWebWindowFeatures = c_void_p
_WebKitWebHistoryItem = c_void_p
__JSValue = c_void_p
__JSObject = c_void_p
__GdkEventButton = c_void_p
__JSContextGroup = c_void_p
_JSObject = c_void_p
_JSString = c_void_p
_WebKitViewportAttributes = c_void_p
_WebKitWebInspector = c_void_p
__GError = c_void_p
_JSPropertyNameArray = c_void_p
__JSPropertyNameAccumulator = c_void_p
__JSContext = c_void_p
__WebKitWebSettings = c_void_p
_gchar = c_void_p
__JSPropertyNameArray = c_void_p
__WebKitWebView = c_void_p
_guchar = c_void_p
_WebKitHitTestResult = c_void_p
_JSValue = c_void_p
_WebKitDOMDocument = c_void_p
__GtkPrintOperation = c_void_p
_WebKitWebBackForwardList = c_void_p
_WebKitWebView = c_void_p
"""Enumerations"""
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitLoadStatus = c_int
WebKitEditingBehavior = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int

class JSObject( object):
    """Class JSObject Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def JSPropertyNameAccumulatorAddName(self,  accumulator, propertyName,):
        if accumulator : accumulator = accumulator._object
        else : accumulator = c_void_p()
        if propertyName : propertyName = propertyName._object
        else : propertyName = c_void_p()

        libwebkit3.JSPropertyNameAccumulatorAddName.argtypes = [c_void_p, _JSPropertyNameAccumulator,_JSString]
        
        libwebkit3.JSPropertyNameAccumulatorAddName(self._object,  accumulator, propertyName,)

    def JSObjectSetPrototype(self,  ctx, object, value,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if value : value = value._object
        else : value = c_void_p()

        libwebkit3.JSObjectSetPrototype.argtypes = [c_void_p, _JSContext,_JSObject,_JSValue]
        
        libwebkit3.JSObjectSetPrototype(self._object,  ctx, object, value,)

    def JSPropertyNameArrayRelease(self,  array,):
        if array : array = array._object
        else : array = c_void_p()

        libwebkit3.JSPropertyNameArrayRelease.argtypes = [c_void_p, _JSPropertyNameArray]
        
        libwebkit3.JSPropertyNameArrayRelease(self._object,  array,)

    def JSObjectSetPropertyAtIndex(self,  ctx, object, propertyIndex, value, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if propertyIndex : propertyIndex = propertyIndex._object
        else : propertyIndex = c_void_p()
        if value : value = value._object
        else : value = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()

        libwebkit3.JSObjectSetPropertyAtIndex.argtypes = [c_void_p, _JSContext,_JSObject,unsigned,_JSValue,_JSValue]
        
        libwebkit3.JSObjectSetPropertyAtIndex(self._object,  ctx, object, propertyIndex, value, exception,)

    def JSObjectSetPrivate(self,  data,):

        libwebkit3.JSObjectSetPrivate.restype = bool
        libwebkit3.JSObjectSetPrivate.argtypes = [c_void_p, c_char_p]
        
        return libwebkit3.JSObjectSetPrivate(self._object,  data,)

    def JSClassRelease(self,  jsClass,):
        if jsClass : jsClass = jsClass._object
        else : jsClass = c_void_p()

        libwebkit3.JSClassRelease.argtypes = [c_void_p, _JSClass]
        
        libwebkit3.JSClassRelease(self._object,  jsClass,)

    def JSObjectGetPrivate(self, ):

        libwebkit3.JSObjectGetPrivate.restype = _char
        libwebkit3.JSObjectGetPrivate.argtypes = [c_void_p]
        
        return libwebkit3.JSObjectGetPrivate(self._object, )

    def JSObjectSetProperty(self,  ctx, object, propertyName, value, attributes, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if propertyName : propertyName = propertyName._object
        else : propertyName = c_void_p()
        if value : value = value._object
        else : value = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()

        libwebkit3.JSObjectSetProperty.argtypes = [c_void_p, _JSContext,_JSObject,_JSString,_JSValue,JSPropertyAttributes,_JSValue]
        
        libwebkit3.JSObjectSetProperty(self._object,  ctx, object, propertyName, value, attributes, exception,)

    @staticmethod
    def JSClassRetain( jsClass,):
        if jsClass : jsClass = jsClass._object
        else : jsClass = c_void_p()
        libwebkit3.JSClassRetain.restype = _JSClass
        libwebkit3.JSClassRetain.argtypes = [_JSClass]
        return libwebkit3.JSClassRetain(jsClass, )

    @staticmethod
    def JSObjectMakeFunctionWithCallback( ctx, name, callAsFunction,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if name : name = name._object
        else : name = c_void_p()
        libwebkit3.JSObjectMakeFunctionWithCallback.restype = _JSObject
        libwebkit3.JSObjectMakeFunctionWithCallback.argtypes = [_JSContext,_JSString,JSObjectCallAsFunctionCallback]
        return libwebkit3.JSObjectMakeFunctionWithCallback(ctx, name, callAsFunction, )

    @staticmethod
    def JSPropertyNameArrayRetain( array,):
        if array : array = array._object
        else : array = c_void_p()
        libwebkit3.JSPropertyNameArrayRetain.restype = _JSPropertyNameArray
        libwebkit3.JSPropertyNameArrayRetain.argtypes = [_JSPropertyNameArray]
        return libwebkit3.JSPropertyNameArrayRetain(array, )

    @staticmethod
    def JSObjectCopyPropertyNames( ctx, object,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        libwebkit3.JSObjectCopyPropertyNames.restype = _JSPropertyNameArray
        libwebkit3.JSObjectCopyPropertyNames.argtypes = [_JSContext,_JSObject]
        return libwebkit3.JSObjectCopyPropertyNames(ctx, object, )

    @staticmethod
    def JSObjectMake( ctx, jsClass, data,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if jsClass : jsClass = jsClass._object
        else : jsClass = c_void_p()
        libwebkit3.JSObjectMake.restype = _JSObject
        libwebkit3.JSObjectMake.argtypes = [_JSContext,_JSClass,c_char_p]
        return libwebkit3.JSObjectMake(ctx, jsClass, data, )

    @staticmethod
    def JSObjectIsFunction( ctx, object,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        libwebkit3.JSObjectIsFunction.restype = bool
        libwebkit3.JSObjectIsFunction.argtypes = [_JSContext,_JSObject]
        return libwebkit3.JSObjectIsFunction(ctx, object, )

    @staticmethod
    def JSObjectGetPrototype( ctx, object,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        libwebkit3.JSObjectGetPrototype.restype = _JSValue
        libwebkit3.JSObjectGetPrototype.argtypes = [_JSContext,_JSObject]
        return libwebkit3.JSObjectGetPrototype(ctx, object, )

    @staticmethod
    def JSObjectMakeArray( ctx, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libwebkit3.JSObjectMakeArray.restype = _JSObject
        libwebkit3.JSObjectMakeArray.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        return libwebkit3.JSObjectMakeArray(ctx, argumentCount, arguments, exception, )

    @staticmethod
    def JSPropertyNameArrayGetNameAtIndex( array, index,):
        if array : array = array._object
        else : array = c_void_p()
        libwebkit3.JSPropertyNameArrayGetNameAtIndex.restype = _JSString
        libwebkit3.JSPropertyNameArrayGetNameAtIndex.argtypes = [_JSPropertyNameArray,size_t]
        return libwebkit3.JSPropertyNameArrayGetNameAtIndex(array, index, )

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
        libwebkit3.JSObjectCallAsConstructor.restype = _JSObject
        libwebkit3.JSObjectCallAsConstructor.argtypes = [_JSContext,_JSObject,size_t,_JSValue,_JSValue]
        return libwebkit3.JSObjectCallAsConstructor(ctx, object, argumentCount, arguments, exception, )

    @staticmethod
    def JSObjectMakeRegExp( ctx, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libwebkit3.JSObjectMakeRegExp.restype = _JSObject
        libwebkit3.JSObjectMakeRegExp.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        return libwebkit3.JSObjectMakeRegExp(ctx, argumentCount, arguments, exception, )

    @staticmethod
    def JSClassCreate( definition,):
        if definition : definition = definition._object
        else : definition = c_void_p()
        libwebkit3.JSClassCreate.restype = _JSClass
        libwebkit3.JSClassCreate.argtypes = [POITNER(JSClassDefinition)]
        return libwebkit3.JSClassCreate(definition, )

    @staticmethod
    def JSObjectMakeError( ctx, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libwebkit3.JSObjectMakeError.restype = _JSObject
        libwebkit3.JSObjectMakeError.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        return libwebkit3.JSObjectMakeError(ctx, argumentCount, arguments, exception, )

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
        libwebkit3.JSObjectDeleteProperty.restype = bool
        libwebkit3.JSObjectDeleteProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue]
        return libwebkit3.JSObjectDeleteProperty(ctx, object, propertyName, exception, )

    @staticmethod
    def JSObjectMakeConstructor( ctx, jsClass, callAsConstructor,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if jsClass : jsClass = jsClass._object
        else : jsClass = c_void_p()
        libwebkit3.JSObjectMakeConstructor.restype = _JSObject
        libwebkit3.JSObjectMakeConstructor.argtypes = [_JSContext,_JSClass,JSObjectCallAsConstructorCallback]
        return libwebkit3.JSObjectMakeConstructor(ctx, jsClass, callAsConstructor, )

    @staticmethod
    def JSObjectMakeFunction( ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if name : name = name._object
        else : name = c_void_p()
        if parameterCount : parameterCount = parameterCount._object
        else : parameterCount = c_void_p()
        if parameterNames : parameterNames = parameterNames._object
        else : parameterNames = c_void_p()
        if body : body = body._object
        else : body = c_void_p()
        if sourceURL : sourceURL = sourceURL._object
        else : sourceURL = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libwebkit3.JSObjectMakeFunction.restype = _JSObject
        libwebkit3.JSObjectMakeFunction.argtypes = [_JSContext,_JSString,unsigned,_JSString,_JSString,_JSString,int,_JSValue]
        return libwebkit3.JSObjectMakeFunction(ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception, )

    @staticmethod
    def JSObjectGetPropertyAtIndex( ctx, object, propertyIndex, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if propertyIndex : propertyIndex = propertyIndex._object
        else : propertyIndex = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libwebkit3.JSObjectGetPropertyAtIndex.restype = _JSValue
        libwebkit3.JSObjectGetPropertyAtIndex.argtypes = [_JSContext,_JSObject,unsigned,_JSValue]
        return libwebkit3.JSObjectGetPropertyAtIndex(ctx, object, propertyIndex, exception, )

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
        libwebkit3.JSObjectGetProperty.restype = _JSValue
        libwebkit3.JSObjectGetProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue]
        return libwebkit3.JSObjectGetProperty(ctx, object, propertyName, exception, )

    @staticmethod
    def JSObjectHasProperty( ctx, object, propertyName,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        if propertyName : propertyName = propertyName._object
        else : propertyName = c_void_p()
        libwebkit3.JSObjectHasProperty.restype = bool
        libwebkit3.JSObjectHasProperty.argtypes = [_JSContext,_JSObject,_JSString]
        return libwebkit3.JSObjectHasProperty(ctx, object, propertyName, )

    @staticmethod
    def JSObjectIsConstructor( ctx, object,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if object : object = object._object
        else : object = c_void_p()
        libwebkit3.JSObjectIsConstructor.restype = bool
        libwebkit3.JSObjectIsConstructor.argtypes = [_JSContext,_JSObject]
        return libwebkit3.JSObjectIsConstructor(ctx, object, )

    @staticmethod
    def JSObjectMakeDate( ctx, argumentCount, arguments, exception,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        if arguments : arguments = arguments._object
        else : arguments = c_void_p()
        if exception : exception = exception._object
        else : exception = c_void_p()
        libwebkit3.JSObjectMakeDate.restype = _JSObject
        libwebkit3.JSObjectMakeDate.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        return libwebkit3.JSObjectMakeDate(ctx, argumentCount, arguments, exception, )

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
        libwebkit3.JSObjectCallAsFunction.restype = _JSValue
        libwebkit3.JSObjectCallAsFunction.argtypes = [_JSContext,_JSObject,_JSObject,size_t,_JSValue,_JSValue]
        return libwebkit3.JSObjectCallAsFunction(ctx, object, thisObject, argumentCount, arguments, exception, )

    @staticmethod
    def JSPropertyNameArrayGetCount( array,):
        if array : array = array._object
        else : array = c_void_p()
        libwebkit3.JSPropertyNameArrayGetCount.restype = size_t
        libwebkit3.JSPropertyNameArrayGetCount.argtypes = [_JSPropertyNameArray]
        return libwebkit3.JSPropertyNameArrayGetCount(array, )

