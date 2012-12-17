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
from gtk3_enums import *
from webkit3_types import *
from webkit3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GClosure = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GObject = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_JSString = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
_GScanner = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkEventButton = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkPrintOperation = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_JSPropertyNameAccumulator = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkColor = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
_JSObject = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GParameter = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
"""Enumerations"""
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkIconSize = c_int
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
GdkVisualType = c_int
GdkByteOrder = c_int
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
WebKitLoadStatus = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitEditingBehavior = c_int

libwebkit3.JSValueIsInstanceOfConstructor.restype = bool
libwebkit3.JSValueIsInstanceOfConstructor.argtypes = [_JSContext,_JSValue,_JSObject,_JSValue]
libwebkit3.JSValueToObject.restype = _JSObject
libwebkit3.JSValueToObject.argtypes = [_JSContext,_JSValue,_JSValue]
libwebkit3.JSValueIsUndefined.restype = bool
libwebkit3.JSValueIsUndefined.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueIsObjectOfClass.restype = bool
libwebkit3.JSValueIsObjectOfClass.argtypes = [_JSContext,_JSValue,_JSClass]
libwebkit3.JSValueIsStrictEqual.restype = bool
libwebkit3.JSValueIsStrictEqual.argtypes = [_JSContext,_JSValue,_JSValue]
libwebkit3.JSValueIsNull.restype = bool
libwebkit3.JSValueIsNull.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueProtect.restype = None
libwebkit3.JSValueProtect.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueIsObject.restype = bool
libwebkit3.JSValueIsObject.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueIsBoolean.restype = bool
libwebkit3.JSValueIsBoolean.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueIsString.restype = bool
libwebkit3.JSValueIsString.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueToStringCopy.restype = _JSString
libwebkit3.JSValueToStringCopy.argtypes = [_JSContext,_JSValue,_JSValue]
libwebkit3.JSValueToBoolean.restype = bool
libwebkit3.JSValueToBoolean.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueIsNumber.restype = bool
libwebkit3.JSValueIsNumber.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueIsEqual.restype = bool
libwebkit3.JSValueIsEqual.argtypes = [_JSContext,_JSValue,_JSValue,_JSValue]
libwebkit3.JSValueCreateJSONString.restype = _JSString
libwebkit3.JSValueCreateJSONString.argtypes = [_JSContext,_JSValue,unsigned,_JSValue]
libwebkit3.JSValueUnprotect.restype = None
libwebkit3.JSValueUnprotect.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueGetType.restype = JSType
libwebkit3.JSValueGetType.argtypes = [_JSContext,_JSValue]
libwebkit3.JSValueToNumber.restype = double
libwebkit3.JSValueToNumber.argtypes = [_JSContext,_JSValue,_JSValue]
import javascriptcore__JSObject
class JSValue( javascriptcore__JSObject.JSObject):
    """Class JSValue Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def IsInstanceOfConstructor(  self, ctx, constructor, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if constructor: constructor = constructor._object
        else: constructor = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        
        return libwebkit3.JSValueIsInstanceOfConstructor( ctx,self._object,constructor,exception )

    def ToObject(  self, ctx, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        from javascriptcore import JSObject
        return JSObject( obj=libwebkit3.JSValueToObject( ctx,self._object,exception )  or POINTER(c_int)())

    def IsUndefined(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libwebkit3.JSValueIsUndefined( ctx,self._object )

    def IsObjectOfClass(  self, ctx, jsClass, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()

        
        return libwebkit3.JSValueIsObjectOfClass( ctx,self._object,jsClass )

    def IsStrictEqual(  self, ctx, b, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if b: b = b._object
        else: b = POINTER(c_int)()

        
        return libwebkit3.JSValueIsStrictEqual( ctx,self._object,b )

    def IsNull(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libwebkit3.JSValueIsNull( ctx,self._object )

    def Protect(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        libwebkit3.JSValueProtect( ctx,self._object )

    def IsObject(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libwebkit3.JSValueIsObject( ctx,self._object )

    def IsBoolean(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libwebkit3.JSValueIsBoolean( ctx,self._object )

    def IsString(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libwebkit3.JSValueIsString( ctx,self._object )

    def ToStringCopy(  self, ctx, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        from javascriptcore import JSString
        return JSString( obj=libwebkit3.JSValueToStringCopy( ctx,self._object,exception )  or POINTER(c_int)())

    def ToBoolean(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libwebkit3.JSValueToBoolean( ctx,self._object )

    def IsNumber(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libwebkit3.JSValueIsNumber( ctx,self._object )

    def IsEqual(  self, ctx, b, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if b: b = b._object
        else: b = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        
        return libwebkit3.JSValueIsEqual( ctx,self._object,b,exception )

    def CreateJSONString(  self, ctx, indent, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        from javascriptcore import JSString
        return JSString( obj=libwebkit3.JSValueCreateJSONString( ctx,self._object,indent,exception )  or POINTER(c_int)())

    def Unprotect(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        libwebkit3.JSValueUnprotect( ctx,self._object )

    def GetType(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libwebkit3.JSValueGetType( ctx,self._object )

    def ToNumber(  self, ctx, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        
        return libwebkit3.JSValueToNumber( ctx,self._object,exception )

    @staticmethod
    def MakeNumber( ctx, number,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeNumber(ctx, number, )
  or POINTER(c_int)())
    @staticmethod
    def MakeUndefined( ctx,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeUndefined(ctx, )
  or POINTER(c_int)())
    @staticmethod
    def MakeNull( ctx,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeNull(ctx, )
  or POINTER(c_int)())
    @staticmethod
    def MakeFromJSONString( ctx, string,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if string: string = string._object
        else: string = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeFromJSONString(ctx, string, )
  or POINTER(c_int)())
    @staticmethod
    def MakeBoolean( ctx, boolean,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeBoolean(ctx, boolean, )
  or POINTER(c_int)())
    @staticmethod
    def MakeString( ctx, string,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if string: string = string._object
        else: string = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libwebkit3.JSValueMakeString(ctx, string, )
  or POINTER(c_int)())
