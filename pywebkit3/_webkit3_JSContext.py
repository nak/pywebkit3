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
__WebKitWebWindowFeatures = c_void_p
_WebKitWebHistoryItem = c_void_p
__GdkEventButton = c_void_p
__JSContextGroup = c_void_p
_JSObject = c_void_p
_WebKitViewportAttributes = c_void_p
_WebKitWebInspector = c_void_p
__GError = c_void_p
__WebKitWebSettings = c_void_p
_gchar = c_void_p
__WebKitWebView = c_void_p
_guchar = c_void_p
_WebKitHitTestResult = c_void_p
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

import _javascriptcore_JSObject
class JSContext( _javascriptcore_JSObject.JSObject):
    """Class JSContext Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def JSGlobalContextRelease(self,  ctx,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()

        libwebkit3.JSGlobalContextRelease.argtypes = [c_void_p, _JSGlobalContext]
        
        libwebkit3.JSGlobalContextRelease(self._object,  ctx,)

    def JSContextGroupRelease(self,  group,):
        if group : group = group._object
        else : group = c_void_p()

        libwebkit3.JSContextGroupRelease.argtypes = [c_void_p, _JSContextGroup]
        
        libwebkit3.JSContextGroupRelease(self._object,  group,)

    def JSContextGetGroup(self, ):

        libwebkit3.JSContextGetGroup.restype = _JSContextGroup
        libwebkit3.JSContextGetGroup.argtypes = [c_void_p]
        from pywebkit3.javascriptcore import JSContextGroup
        return JSContextGroup( obj=libwebkit3.JSContextGetGroup(self._object, )  or c_void_p())

    def JSContextGetGlobalObject(self, ):

        libwebkit3.JSContextGetGlobalObject.restype = _JSObject
        libwebkit3.JSContextGetGlobalObject.argtypes = [c_void_p]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=libwebkit3.JSContextGetGlobalObject(self._object, )  or c_void_p())

    @staticmethod
    def JSGlobalContextCreate( globalObjectClass,):
        if globalObjectClass : globalObjectClass = globalObjectClass._object
        else : globalObjectClass = c_void_p()
        libwebkit3.JSGlobalContextCreate.restype = _JSGlobalContext
        libwebkit3.JSGlobalContextCreate.argtypes = [_JSClass]
        return libwebkit3.JSGlobalContextCreate(globalObjectClass, )

    @staticmethod
    def JSGlobalContextCreateInGroup( group, globalObjectClass,):
        if group : group = group._object
        else : group = c_void_p()
        if globalObjectClass : globalObjectClass = globalObjectClass._object
        else : globalObjectClass = c_void_p()
        libwebkit3.JSGlobalContextCreateInGroup.restype = _JSGlobalContext
        libwebkit3.JSGlobalContextCreateInGroup.argtypes = [_JSContextGroup,_JSClass]
        return libwebkit3.JSGlobalContextCreateInGroup(group, globalObjectClass, )

    @staticmethod
    def JSContextGroupRetain( group,):
        if group : group = group._object
        else : group = c_void_p()
        libwebkit3.JSContextGroupRetain.restype = _JSContextGroup
        libwebkit3.JSContextGroupRetain.argtypes = [_JSContextGroup]
        return libwebkit3.JSContextGroupRetain(group, )

    @staticmethod
    def JSGlobalContextRetain( ctx,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        libwebkit3.JSGlobalContextRetain.restype = _JSGlobalContext
        libwebkit3.JSGlobalContextRetain.argtypes = [_JSGlobalContext]
        return libwebkit3.JSGlobalContextRetain(ctx, )

