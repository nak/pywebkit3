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
from .gtk3_types import *
from .javascriptcore_types import *
    
    
"""Derived Pointer Types"""
__GtkRcStyle = POINTER(c_void_p)
__GdkGeometry = POINTER(c_void_p)
_WebKitNetworkResponse = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
__GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
__GtkRegionFlags = POINTER(c_void_p)
__WebKitDOMNode = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
__cairo_font_options_t = POINTER(c_void_p)
__JSValue = POINTER(c_void_p)
_JSContext = POINTER(c_void_p)
_GtkIconFactory = POINTER(c_void_p)
__GdkAtom = POINTER(c_void_p)
__GdkTimeCoord = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
__GtkWidgetPath = POINTER(c_void_p)
_PangoItem = POINTER(c_void_p)
__GClosure = POINTER(c_void_p)
_GtkAboutDialog = POINTER(c_void_p)
__GMainContext = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
__GtkStyleProvider = POINTER(c_void_p)
_GtkDialog = POINTER(c_void_p)
__WebKitWebWindowFeatures = POINTER(c_void_p)
_JSObject = POINTER(c_void_p)
_GBytes = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GMainContext = POINTER(c_void_p)
_GBoxed = POINTER(c_void_p)
__GtkTextBuffer = POINTER(c_void_p)
_GtkTargetList = POINTER(c_void_p)
__WebKitWebSettings = POINTER(c_void_p)
_GdkAppLaunchContext = POINTER(c_void_p)
__GObject = POINTER(c_void_p)
__PangoLayout = POINTER(c_void_p)
_WebKitWebBackForwardList = POINTER(c_void_p)
_GtkOffscreenWindow = POINTER(c_void_p)
__GParamSpec = POINTER(c_void_p)
__PangoAttrIterator = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_JSGlobalContext = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_GString = POINTER(c_void_p)
__PangoContext = POINTER(c_void_p)
__JSPropertyNameArray = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
__PangoFont = POINTER(c_void_p)
__GtkPathPriorityType = POINTER(c_void_p)
__JSClass = POINTER(c_void_p)
__WebKitWebHistoryItem = POINTER(c_void_p)
_JSValue = POINTER(c_void_p)
__GtkSettings = POINTER(c_void_p)
_GSource = POINTER(c_void_p)
__PangoFontMap = POINTER(c_void_p)
__JSString = POINTER(c_void_p)
__PangoAttrList = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
__GSource = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
__PangoAnalysis = POINTER(c_void_p)
__GMutex = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
__GdkCursor = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_WebKitWebInspector = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_GOptionGroup = POINTER(c_void_p)
__GScanner = POINTER(c_void_p)
__GtkWidgetClass = POINTER(c_void_p)
__GdkEventKey = POINTER(c_void_p)
_GdkDragContext = POINTER(c_void_p)
__GdkDisplay = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_PangoFontMetrics = POINTER(c_void_p)
__GCond = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_WebKitWebFrame = POINTER(c_void_p)
_JSString = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
__WebKitNetworkRequest = POINTER(c_void_p)
__GdkWindow = POINTER(c_void_p)
__PangoFontFamily = POINTER(c_void_p)
__JSContextGroup = POINTER(c_void_p)
__GPollFD = POINTER(c_void_p)
__cairo_region_t = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
__PangoFontDescription = POINTER(c_void_p)
__GtkBorder = POINTER(c_void_p)
__GError = POINTER(c_void_p)
__PangoCoverage = POINTER(c_void_p)
_WebKitViewportAttributes = POINTER(c_void_p)
_JSClass = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
__cairo_t = POINTER(c_void_p)
__GWeakRef = POINTER(c_void_p)
__GdkVisual = POINTER(c_void_p)
__GdkEventButton = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
__PangoRectangle = POINTER(c_void_p)
__GtkAccelGroup = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
__GtkIconSource = POINTER(c_void_p)
__JSContext = POINTER(c_void_p)
_PangoFontsetSimple = POINTER(c_void_p)
__GtkAllocation = POINTER(c_void_p)
__GtkWidget = POINTER(c_void_p)
_PangoLayoutLine = POINTER(c_void_p)
__GtkIconSet = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
__PangoTabArray = POINTER(c_void_p)
_WebKitHitTestResult = POINTER(c_void_p)
__GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitDOMDocument = POINTER(c_void_p)
__PangoMatrix = POINTER(c_void_p)
__GtkPrintOperation = POINTER(c_void_p)
__GString = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
__GList = POINTER(c_void_p)
__WebKitWebView = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
__GdkRGBA = POINTER(c_void_p)
__GTimeVal = POINTER(c_void_p)
_GtkInvisible = POINTER(c_void_p)
__GSourceFuncs = POINTER(c_void_p)
__JSPropertyNameAccumulator = POINTER(c_void_p)
__PangoGlyphString = POINTER(c_void_p)
__JSGlobalContext = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
__GObjectClass = POINTER(c_void_p)
__GSList = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
__GdkWindowAttr = POINTER(c_void_p)
_SoupMessage = POINTER(c_void_p)
_WebKitWebDataSource = POINTER(c_void_p)
__GdkColor = POINTER(c_void_p)
_JSContextGroup = POINTER(c_void_p)
__GdkRectangle = POINTER(c_void_p)
__PangoLanguage = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
__gunichar = POINTER(c_void_p)
__GdkWMDecoration = POINTER(c_void_p)
__PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_JSPropertyNameArray = POINTER(c_void_p)
__JSObject = POINTER(c_void_p)
_WebKitWebNavigationAction = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
__GParameter = POINTER(c_void_p)
__GtkStyle = POINTER(c_void_p)
__GIcon = POINTER(c_void_p)
__GtkWindow = POINTER(c_void_p)
_PangoLayoutRun = POINTER(c_void_p)
__cairo_pattern_t = POINTER(c_void_p)
__GdkPixbuf = POINTER(c_void_p)
_WebKitGeolocationPolicyDecision = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
__GSourceCallbackFuncs = POINTER(c_void_p)
__PangoFontFace = POINTER(c_void_p)
__GtkTargetEntry = POINTER(c_void_p)
__GtkApplication = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_GByteArray = POINTER(c_void_p)
__GdkScreen = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
__GdkDevice = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
"""Enumerations"""
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
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
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GtkDialogFlags = c_int
GtkResponseType = c_int
WebKitWebNavigationReason = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkLicense = c_int
GtkIconSize = c_int

libjavascriptcore.JSValueToObject.restype = _JSObject
libjavascriptcore.JSValueToObject.argtypes = [_JSContext,_JSValue,_JSValue]
libjavascriptcore.JSValueIsUndefined.restype = bool
libjavascriptcore.JSValueIsUndefined.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueIsObjectOfClass.restype = bool
libjavascriptcore.JSValueIsObjectOfClass.argtypes = [_JSContext,_JSValue,_JSClass]
libjavascriptcore.JSValueIsStrictEqual.restype = bool
libjavascriptcore.JSValueIsStrictEqual.argtypes = [_JSContext,_JSValue,_JSValue]
libjavascriptcore.JSValueIsNull.restype = bool
libjavascriptcore.JSValueIsNull.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueProtect.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueIsObject.restype = bool
libjavascriptcore.JSValueIsObject.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueIsBoolean.restype = bool
libjavascriptcore.JSValueIsBoolean.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueIsString.restype = bool
libjavascriptcore.JSValueIsString.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueToStringCopy.restype = _JSString
libjavascriptcore.JSValueToStringCopy.argtypes = [_JSContext,_JSValue,_JSValue]
libjavascriptcore.JSValueToBoolean.restype = bool
libjavascriptcore.JSValueToBoolean.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueIsEqual.restype = bool
libjavascriptcore.JSValueIsEqual.argtypes = [_JSContext,_JSValue,_JSValue,_JSValue]
libjavascriptcore.JSValueCreateJSONString.restype = _JSString
libjavascriptcore.JSValueCreateJSONString.argtypes = [_JSContext,_JSValue,unsigned,_JSValue]
libjavascriptcore.JSValueUnprotect.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueGetType.restype = JSType
libjavascriptcore.JSValueGetType.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueToNumber.restype = double
libjavascriptcore.JSValueToNumber.argtypes = [_JSContext,_JSValue,_JSValue]
libjavascriptcore.JSValueMakeNumber.restype = _JSValue
libjavascriptcore.JSValueMakeNumber.argtypes = [_JSContext,c_double]
libjavascriptcore.JSValueMakeUndefined.restype = _JSValue
libjavascriptcore.JSValueMakeUndefined.argtypes = [_JSContext]
libjavascriptcore.JSValueMakeNull.restype = _JSValue
libjavascriptcore.JSValueMakeNull.argtypes = [_JSContext]
libjavascriptcore.JSValueMakeBoolean.restype = _JSValue
libjavascriptcore.JSValueMakeBoolean.argtypes = [_JSContext,c_char]
libjavascriptcore.JSValueMakeString.restype = _JSValue
libjavascriptcore.JSValueMakeString.argtypes = [_JSContext,_JSString]
libjavascriptcore.JSValueUnprotect.argtypes = [_JSContext,_JSValue]
libjavascriptcore.JSValueIsInstanceOfConstructor.restype = c_char
libjavascriptcore.JSValueIsInstanceOfConstructor.argtypes = [_JSContext,_JSValue,_JSObject,_JSValue]
libjavascriptcore.JSValueIsNumber.restype = c_char
libjavascriptcore.JSValueIsNumber.argtypes = [_JSContext,_JSValue]

import weakref

class JSValue( object ):
    """Class JSValue Constructors"""
    def __init__(self, obj , context ):
        ctx = context
        self._object = weakref.ref(obj)
        self._strongref = obj
        self._context = context
        #import traceback
        #traceback.print_stack()
        #import logging
        #logging.error("=====================")
        from .javascript import JSContext
        assert( isinstance(context, JSContext) or context == None)
        if not isinstance(self, JSContext):
            assert( context )
            libjavascriptcore.JSValueProtect( self._context._object(),
                                              self._object() )   
        
    """Methods"""
    def IsInstanceOfConstructor(  self, ctx, ructor, exception, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()
        if ructor: ructor = ructor._object()
        else: ructor = POINTER(c_void_p)()
        if exception: exception = exception._object()
        else: exception = POINTER(c_void_p)()
        if self._object():
            return libjavascriptcore.JSValueIsInstanceOfConstructor( ctx,self._object(),ructor,exception )

    def ToObject(  self, ctx, exception, ):
        if exception: exception = exception._object()
        else: exception = POINTER(c_void_p)()

        from .javascriptcore import JSObject
        if self._object():
            return JSObject( obj=libjavascriptcore.JSValueToObject( ctx._object(),self._object(),exception ), context = ctx)

    def IsUndefined(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()

        
        if self._object():
            return libjavascriptcore.JSValueIsUndefined( ctx,self._object() )

    def IsObjectOfClass(  self, ctx, jsClass, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()
        if jsClass: jsClass = jsClass._object()
        else: jsClass = POINTER(c_void_p)()
        
        if self._object():
            return libjavascriptcore.JSValueIsObjectOfClass( ctx,self._object(),jsClass )

    def IsStrictEqual(  self, ctx, b, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()
        if b: b = b._object()
        else: b = POINTER(c_void_p)()

       
        if self._object():
            return libjavascriptcore.JSValueIsStrictEqual( ctx,self._object(),b )

    def IsNull(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()

        
        if self._object():
            return libjavascriptcore.JSValueIsNull( ctx,self._object() )

    def Protect(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()
        if self._object():
            libjavascriptcore.JSValueProtect( ctx,self._object() )

    def IsObject(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()

        
        if self._object():
            return libjavascriptcore.JSValueIsObject( ctx,self._object() )

    def IsBoolean(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()

        
        if self._object():
            return libjavascriptcore.JSValueIsBoolean( ctx,self._object() )

    def IsString(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()

        
        if self._object():
            return libjavascriptcore.JSValueIsString( ctx,self._object() )

    def ToStringCopy(  self, ctx, exception, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()
        if exception: exception = exception._object()
        else: exception = POINTER(c_void_p)()

        from .javascriptcore import JSString
        if self._object():
            return JSString( obj=libjavascriptcore.JSValueToStringCopy( ctx,self._object(), exception )  or POINTER(c_void_p)())

    def ToPyString(self , ctx, exception):
        jstext = self.ToStringCopy(ctx, exception)
        length = jstext.GetMaximumUTF8CStringSize()
        cstring = (c_char * (length))()
        jstext.GetUTF8CString(cstring, length)
        jstext.Release()
        return cstring.value
    
    def ToBoolean(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()

        
        if self._object():
            return libjavascriptcore.JSValueToBoolean( ctx,self._object() )

    def IsNumber(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()

        
        if self._object():
            return libjavascriptcore.JSValueIsNumber( ctx,self._object() )

    def IsEqual(  self, ctx, b, exception, ):
        if ctx: ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()
        if b: b = b._object()
        else: b = POINTER(c_void_p)()
        if exception: exception = exception._object()
        else: exception = POINTER(c_void_p)()
        
        if self._object():
            return libjavascriptcore.JSValueIsEqual( ctx,self._object(),b,exception )

    def CreateJSONString(  self, ctx, indent, exception, ):
        if indent: indent = indent._object()
        else: indent = POINTER(c_void_p)()
        if exception: exception = exception._object()
        else: exception = POINTER(c_void_p)()

        from .javascriptcore import JSString
        if self._object():
            return JSString( obj=libjavascriptcore.JSValueCreateJSONString( ctx._object(),self._object(),indent,exception )  or POINTER(c_void_p)())

    def Unprotect(  self, ctx, ):
        if self._object() and ctx._object():
        
            libjavascriptcore.JSValueUnprotect( ctx._object(),self._object() )

    def GetType(  self, ctx, ):
        #import logging,traceback
        #logging.error(traceback.format_stack())
        if ctx:
            if not isinstance(ctx, POINTER(c_void_p)):
                ctx = ctx._object()
        else: ctx = POINTER(c_void_p)()

        if self._object():
            return libjavascriptcore.JSValueGetType( ctx,self._object() )

    def ToNumber(  self, ctx, exception, ):
        if exception: exception = exception._object()
        else: exception = POINTER(c_void_p)()
        if self._object():
           return libjavascriptcore.JSValueToNumber( self._context._object(),self._object(),exception )

    @staticmethod
    def MakeNumber( ctx, number,):
        from .javascriptcore import JSValue
        obj=    libjavascriptcore.JSValueMakeNumber(ctx._object(),
                                                    c_double(number), )
        
        return JSValue( obj, context=ctx)

    @staticmethod
    def MakeUndefined( ctx,):
        from .javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeUndefined(ctx._object(), ), context=ctx)

    @staticmethod
    def MakeNull( ctx,):
        from .javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeNull(ctx._object(), ),
                        context=ctx)

    @staticmethod
    def MakeFromJSONString( ctx, string,):
        if string: string = string._object()
        else: string = POINTER(c_void_p)()
        libjavascriptcore.JSValueMakeFromJSONString.restype = _JSValue
        libjavascriptcore.JSValueMakeFromJSONString.argtypes = [_JSContext,_JSString]
        from .javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeFromJSONString(ctx._object(), string), context=ctx )
  
    @staticmethod
    def MakeBoolean( ctx, boolean,):
        from .javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeBoolean(ctx._object(), boolean), context=ctx )

    @staticmethod
    def MakeString( ctx, string,):
        if string: string = string._object()
        else: string = POINTER(c_void_p)()
        from .javascriptcore import JSValue
        retval =  JSValue( obj=    libjavascriptcore.JSValueMakeString(ctx._object(), string), context=ctx)
        return retval


    def __del__(self):
        try:
            from .javascriptcore import JSContext
            if not isinstance(self, JSContext) and \
                   self._object and self._context \
                   and self._object() and self._context._object():
                libjavascriptcore.JSValueUnprotect( self._context._object(),
                                                    self._object() )
        except:
            import traceback
            traceback.print_stack()
            pass
        self._context = None
        self._strongref = None
        self._object = None
                
