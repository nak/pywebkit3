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
__GtkRcStyle = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
_PangoItem = POINTER(c_int)
__GClosure = POINTER(c_int)
_GtkAboutDialog = POINTER(c_int)
__GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GBoxed = POINTER(c_int)
__GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
__GObject = POINTER(c_int)
__PangoLayout = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
__GParamSpec = POINTER(c_int)
__PangoAttrIterator = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GString = POINTER(c_int)
__PangoContext = POINTER(c_int)
__JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__PangoFont = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__JSClass = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
__GtkSettings = POINTER(c_int)
_GSource = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
__GSource = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
__GMutex = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
_GdkDragContext = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
__GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__PangoFontFamily = POINTER(c_int)
__JSContextGroup = POINTER(c_int)
__GPollFD = POINTER(c_int)
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
_PangoFontFamily = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__JSContext = POINTER(c_int)
_PangoFontsetSimple = POINTER(c_int)
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
__GString = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GList = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__GTimeVal = POINTER(c_int)
_GtkInvisible = POINTER(c_int)
__GSourceFuncs = POINTER(c_int)
__JSPropertyNameAccumulator = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
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
_WebKitWebNavigationAction = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GIcon = POINTER(c_int)
__GtkWindow = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
__GSourceCallbackFuncs = POINTER(c_int)
__PangoFontFace = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GByteArray = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
__GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
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
libjavascriptcore.JSValueMakeNumber.argtypes = [_JSContext,double]
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

class JSValue( object ):
    """Class JSValue Constructors"""
    def __init__(self, obj , context ):
        self._object = obj        
        self._context = context
        assert( isinstance(context, POINTER(c_int)) or context == None)
        if context and cast(context, c_void_p).value != None and \
            obj:
            import logging
            libjavascriptcore.JSValueProtect( self._context,self._object )   
            
    """Methods"""
    def IsInstanceOfConstructor(  self, ctx, ructor, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if ructor: ructor = ructor._object
        else: ructor = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        return libjavascriptcore.JSValueIsInstanceOfConstructor( ctx,self._object,ructor,exception )

    def ToObject(  self, ctx, exception, ):
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        from javascriptcore import JSObject
        return JSObject( obj=libjavascriptcore.JSValueToObject( ctx._object,self._object,exception ), context = ctx._object)

    def IsUndefined(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libjavascriptcore.JSValueIsUndefined( ctx,self._object )

    def IsObjectOfClass(  self, ctx, jsClass, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()
        
        return libjavascriptcore.JSValueIsObjectOfClass( ctx,self._object,jsClass )

    def IsStrictEqual(  self, ctx, b, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if b: b = b._object
        else: b = POINTER(c_int)()

       
        return libjavascriptcore.JSValueIsStrictEqual( ctx,self._object,b )

    def IsNull(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libjavascriptcore.JSValueIsNull( ctx,self._object )

    def Protect(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        
        libjavascriptcore.JSValueProtect( ctx,self._object )

    def IsObject(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libjavascriptcore.JSValueIsObject( ctx,self._object )

    def IsBoolean(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libjavascriptcore.JSValueIsBoolean( ctx,self._object )

    def IsString(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libjavascriptcore.JSValueIsString( ctx,self._object )

    def ToStringCopy(  self, ctx, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        from javascriptcore import JSString
        return JSString( obj=libjavascriptcore.JSValueToStringCopy( ctx,self._object,exception )  or POINTER(c_int)())

    def ToPyString(self , ctx, exception):
        jstext = self.ToStringCopy(ctx, exception)
        length = jstext.GetMaximumUTF8CStringSize()
        cstring = (c_char * (length))()
        jstext.GetUTF8CString(cstring, length)
        jstext.Release()
        return cstring.value
    
    def ToBoolean(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libjavascriptcore.JSValueToBoolean( ctx,self._object )

    def IsNumber(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libjavascriptcore.JSValueIsNumber( ctx,self._object )

    def IsEqual(  self, ctx, b, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if b: b = b._object
        else: b = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        
        return libjavascriptcore.JSValueIsEqual( ctx,self._object,b,exception )

    def CreateJSONString(  self, ctx, indent, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if indent: indent = indent._object
        else: indent = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        from javascriptcore import JSString
        return JSString( obj=libjavascriptcore.JSValueCreateJSONString( ctx,self._object,indent,exception )  or POINTER(c_int)())

    def Unprotect(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if cast(ctx, c_void_p).value != None:
        
            libjavascriptcore.JSValueUnprotect( ctx,self._object )

    def GetType(  self, ctx, ):
        #import logging,traceback
        #logging.error(traceback.format_stack())
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        
        return libjavascriptcore.JSValueGetType( ctx,self._object )

    def ToNumber(  self, ctx, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        
        return libjavascriptcore.JSValueToNumber( ctx,self._object,exception )

    @staticmethod
    def MakeNumber( ctx, number,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeNumber(ctx, number, ), context=ctx)

    @staticmethod
    def MakeUndefined( ctx,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeUndefined(ctx, ), context=ctx)

    @staticmethod
    def MakeNull( ctx,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeNull(ctx, ), context=ctx)

    @staticmethod
    def MakeFromJSONString( ctx, string,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if string: string = string._object
        else: string = POINTER(c_int)()
        libjavascriptcore.JSValueMakeFromJSONString.restype = _JSValue
        libjavascriptcore.JSValueMakeFromJSONString.argtypes = [_JSContext,_JSString]
        from javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeFromJSONString(ctx, string), context=ctx )
  
    @staticmethod
    def MakeBoolean( ctx, boolean,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeBoolean(ctx, boolean), context=ctx )

    @staticmethod
    def MakeString( ctx, string,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if string: string = string._object
        else: string = POINTER(c_int)()
        from javascriptcore import JSValue
        return JSValue( obj=    libjavascriptcore.JSValueMakeString(ctx, string), context=ctx)
  


    def __del__(self):
        if self._object and self._context:
            from javascriptcore import JSContext
            if isinstance(self._context, JSContext):
                self._context = self._context._object
            if cast(self._context, c_void_p).value != None:
                libjavascriptcore.JSValueUnprotect( self._context,self._object )           
            
                
        
                
