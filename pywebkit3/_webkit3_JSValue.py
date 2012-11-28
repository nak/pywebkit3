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
__GtkRcStyle = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
_GtkBin = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
__GClosure = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
__GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GtkContainer = POINTER(c_int)
__PangoLayout = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
__GParamSpec = POINTER(c_int)
__PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAdjustment = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
__PangoContext = POINTER(c_int)
__JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__JSClass = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
__GtkSettings = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__GObject = POINTER(c_int)
__GtkContainerClass = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GtkAdjustment = POINTER(c_int)
_GdkDragContext = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
__GActionGroup = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__PangoFontFamily = POINTER(c_int)
__JSContextGroup = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GtkBorder = POINTER(c_int)
__GError = POINTER(c_int)
__PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
__GCancellable = POINTER(c_int)
__GIcon = POINTER(c_int)
_GList = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__GFile = POINTER(c_int)
__JSContext = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
__GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
__PangoTabArray = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
__GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
__PangoMatrix = POINTER(c_int)
__GtkPrintOperation = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GList = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__JSPropertyNameAccumulator = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GSList = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkAtom = POINTER(c_int)
__GdkColor = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
__gunichar = POINTER(c_int)
__GdkWMDecoration = POINTER(c_int)
__PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
__JSObject = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__GtkWindow = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
__GdkDevice = POINTER(c_int)
_GByteArray = POINTER(c_int)
"""Enumerations"""
GdkVisualType = c_int
GdkByteOrder = c_int
GtkIconSize = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GdkWindowType = c_int
GdkWindowWindowClass = c_int
GdkWindowHints = c_int
GdkGravity = c_int
GdkWindowEdgeh = c_int
GdkWindowTypeHint = c_int
GdkWindowAttributesType = c_int
GdkFilterReturn = c_int
GdkModifierType = c_int
GdkWMDecoration = c_int
GdkWMFunction = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GdkCursorType = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GApplicationFlags = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitLoadStatus = c_int
WebKitEditingBehavior = c_int

import _javascriptcore_JSObject
class JSValue( _javascriptcore_JSObject.JSObject):
    """Class JSValue Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def IsInstanceOfConstructor(  self, ctx, ructor, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if ructor: ructor = ructor._object
        else: ructor = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSValueIsInstanceOfConstructor.restype = bool
        libwebkit3.JSValueIsInstanceOfConstructor.argtypes = [_JSContext,_JSValue,_JSObject,_JSValue]
        
        return libwebkit3.JSValueIsInstanceOfConstructor( ctx,self._object,ructor,exception )

    def ToObject(  self, ctx, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSValueToObject.restype = _JSObject
        libwebkit3.JSValueToObject.argtypes = [_JSContext,_JSValue,_JSValue]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=libwebkit3.JSValueToObject( ctx,self._object,exception )  or POINTER(c_int)())

    def IsUndefined(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueIsUndefined.restype = bool
        libwebkit3.JSValueIsUndefined.argtypes = [_JSContext,_JSValue]
        
        return libwebkit3.JSValueIsUndefined( ctx,self._object )

    def IsObjectOfClass(  self, ctx, jsClass, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()

        libwebkit3.JSValueIsObjectOfClass.restype = bool
        libwebkit3.JSValueIsObjectOfClass.argtypes = [_JSContext,_JSValue,_JSClass]
        
        return libwebkit3.JSValueIsObjectOfClass( ctx,self._object,jsClass )

    def IsStrictEqual(  self, ctx, b, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if b: b = b._object
        else: b = POINTER(c_int)()

        libwebkit3.JSValueIsStrictEqual.restype = bool
        libwebkit3.JSValueIsStrictEqual.argtypes = [_JSContext,_JSValue,_JSValue]
        
        return libwebkit3.JSValueIsStrictEqual( ctx,self._object,b )

    def IsNull(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueIsNull.restype = bool
        libwebkit3.JSValueIsNull.argtypes = [_JSContext,_JSValue]
        
        return libwebkit3.JSValueIsNull( ctx,self._object )

    def Protect(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueProtect.argtypes = [_JSContext,_JSValue]
        
        libwebkit3.JSValueProtect( ctx,self._object )

    def IsObject(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueIsObject.restype = bool
        libwebkit3.JSValueIsObject.argtypes = [_JSContext,_JSValue]
        
        return libwebkit3.JSValueIsObject( ctx,self._object )

    def IsBoolean(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueIsBoolean.restype = bool
        libwebkit3.JSValueIsBoolean.argtypes = [_JSContext,_JSValue]
        
        return libwebkit3.JSValueIsBoolean( ctx,self._object )

    def IsString(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueIsString.restype = bool
        libwebkit3.JSValueIsString.argtypes = [_JSContext,_JSValue]
        
        return libwebkit3.JSValueIsString( ctx,self._object )

    def ToStringCopy(  self, ctx, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSValueToStringCopy.restype = _JSString
        libwebkit3.JSValueToStringCopy.argtypes = [_JSContext,_JSValue,_JSValue]
        from pywebkit3.javascriptcore import JSString
        return JSString( obj=libwebkit3.JSValueToStringCopy( ctx,self._object,exception )  or POINTER(c_int)())

    def ToBoolean(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueToBoolean.restype = bool
        libwebkit3.JSValueToBoolean.argtypes = [_JSContext,_JSValue]
        
        return libwebkit3.JSValueToBoolean( ctx,self._object )

    def IsNumber(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueIsNumber.restype = bool
        libwebkit3.JSValueIsNumber.argtypes = [_JSContext,_JSValue]
        
        return libwebkit3.JSValueIsNumber( ctx,self._object )

    def IsEqual(  self, ctx, b, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if b: b = b._object
        else: b = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSValueIsEqual.restype = bool
        libwebkit3.JSValueIsEqual.argtypes = [_JSContext,_JSValue,_JSValue,_JSValue]
        
        return libwebkit3.JSValueIsEqual( ctx,self._object,b,exception )

    def CreateJSONString(  self, ctx, indent, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if indent: indent = indent._object
        else: indent = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSValueCreateJSONString.restype = _JSString
        libwebkit3.JSValueCreateJSONString.argtypes = [_JSContext,_JSValue,unsigned,_JSValue]
        from pywebkit3.javascriptcore import JSString
        return JSString( obj=libwebkit3.JSValueCreateJSONString( ctx,self._object,indent,exception )  or POINTER(c_int)())

    def Unprotect(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueUnprotect.argtypes = [_JSContext,_JSValue]
        
        libwebkit3.JSValueUnprotect( ctx,self._object )

    def GetType(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSValueGetType.restype = JSType
        libwebkit3.JSValueGetType.argtypes = [_JSContext,_JSValue]
        
        return libwebkit3.JSValueGetType( ctx,self._object )

    def ToNumber(  self, ctx, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSValueToNumber.restype = double
        libwebkit3.JSValueToNumber.argtypes = [_JSContext,_JSValue,_JSValue]
        
        return libwebkit3.JSValueToNumber( ctx,self._object,exception )

    @staticmethod
    def MakeNumber( ctx, number,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        libwebkit3.JSValueMakeNumber.restype = _JSValue
        libwebkit3.JSValueMakeNumber.argtypes = [_JSContext,double]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeNumber(ctx, number, )
  or POINTER(c_int)())
    @staticmethod
    def MakeUndefined( ctx,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        libwebkit3.JSValueMakeUndefined.restype = _JSValue
        libwebkit3.JSValueMakeUndefined.argtypes = [_JSContext]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeUndefined(ctx, )
  or POINTER(c_int)())
    @staticmethod
    def MakeNull( ctx,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        libwebkit3.JSValueMakeNull.restype = _JSValue
        libwebkit3.JSValueMakeNull.argtypes = [_JSContext]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeNull(ctx, )
  or POINTER(c_int)())
    @staticmethod
    def MakeFromJSONString( ctx, string,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if string: string = string._object
        else: string = POINTER(c_int)()
        libwebkit3.JSValueMakeFromJSONString.restype = _JSValue
        libwebkit3.JSValueMakeFromJSONString.argtypes = [_JSContext,_JSString]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeFromJSONString(ctx, string, )
  or POINTER(c_int)())
    @staticmethod
    def MakeBoolean( ctx, boolean,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        libwebkit3.JSValueMakeBoolean.restype = _JSValue
        libwebkit3.JSValueMakeBoolean.argtypes = [_JSContext,bool]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeBoolean(ctx, boolean, )
  or POINTER(c_int)())
    @staticmethod
    def MakeString( ctx, string,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if string: string = string._object
        else: string = POINTER(c_int)()
        libwebkit3.JSValueMakeString.restype = _JSValue
        libwebkit3.JSValueMakeString.argtypes = [_JSContext,_JSString]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeString(ctx, string, )
  or POINTER(c_int)())
