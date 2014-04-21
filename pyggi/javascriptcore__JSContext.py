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
from .gtk3_enums import *
from .javascriptcore_types import *
from .javascriptcore_enums import *

OPAQUE_PTR = POINTER(c_void_p)
NULL = c_void_p()
    
"""Derived Pointer Types"""
_GtkRcStyle = OPAQUE_PTR
_GdkGeometry = OPAQUE_PTR
_PangoFont = OPAQUE_PTR
_WebKitNetworkResponse = OPAQUE_PTR
_GtkLabel = OPAQUE_PTR
_GdkPixbuf = OPAQUE_PTR
_GtkRequisition = OPAQUE_PTR
_GtkRcStyle = OPAQUE_PTR
_PangoEngineShape = OPAQUE_PTR
_GtkRegionFlags = OPAQUE_PTR
_GAsyncResult = OPAQUE_PTR
_cairo_matrix_t = OPAQUE_PTR
_GtkWindow = OPAQUE_PTR
_cairo_font_options_t = OPAQUE_PTR
_JSValue = OPAQUE_PTR
_JSContext = OPAQUE_PTR
_GtkIconFactory = OPAQUE_PTR
_GdkAtom = OPAQUE_PTR
_GdkTimeCoord = OPAQUE_PTR
_GdkColor = OPAQUE_PTR
_GtkWidgetPath = OPAQUE_PTR
_GtkContainer = OPAQUE_PTR
_PangoItem = OPAQUE_PTR
_GClosure = OPAQUE_PTR
_GIcon = OPAQUE_PTR
_GMainContext = OPAQUE_PTR
_GdkDisplay = OPAQUE_PTR
_GInterface = OPAQUE_PTR
_GtkStyleProvider = OPAQUE_PTR
_JSContextGroup = OPAQUE_PTR
_GFileEnumerator = OPAQUE_PTR
_GtkDialog = OPAQUE_PTR
_WebKitWebWindowFeatures = OPAQUE_PTR
_GtkCssProvider = OPAQUE_PTR
_GtkSymbolicColor = OPAQUE_PTR
_void = OPAQUE_PTR
_GtkStyleProperties = OPAQUE_PTR
_GInputStream = OPAQUE_PTR
_GtkIconInfo = OPAQUE_PTR
_GAppInfo = OPAQUE_PTR
_WebKitWebResource = OPAQUE_PTR
_GBytes = OPAQUE_PTR
_GScanner = OPAQUE_PTR
_PangoFont = OPAQUE_PTR
_GtkStyleContext = OPAQUE_PTR
_GMainContext = OPAQUE_PTR
_GtkTextBuffer = OPAQUE_PTR
_GtkTargetList = OPAQUE_PTR
_WebKitWebSettings = OPAQUE_PTR
_GtkNumerableIcon = OPAQUE_PTR
_GdkAppLaunchContext = OPAQUE_PTR
_GObject = OPAQUE_PTR
_PangoLayout = OPAQUE_PTR
_GtkSymbolicColor = OPAQUE_PTR
_WebKitWebBackForwardList = OPAQUE_PTR
_GtkWidget = OPAQUE_PTR
_GtkOffscreenWindow = OPAQUE_PTR
_GParamSpec = OPAQUE_PTR
_GAppLaunchContext = OPAQUE_PTR
_PangoAttrIterator = OPAQUE_PTR
_GFileAttributeMatcher = OPAQUE_PTR
_GtkRequisition = OPAQUE_PTR
_GtkIconSet = OPAQUE_PTR
_GtkIconTheme = OPAQUE_PTR
_GtkSelectionData = OPAQUE_PTR
_GtkWindowGroup = OPAQUE_PTR
_GtkAccelLabel = OPAQUE_PTR
_GtkAdjustment = OPAQUE_PTR
_JSGlobalContext = OPAQUE_PTR
_GApplication = OPAQUE_PTR
_GFileMonitor = OPAQUE_PTR
_PangoLogAttr = OPAQUE_PTR
_GString = OPAQUE_PTR
_GFileAttributeMatcher = OPAQUE_PTR
_PangoContext = OPAQUE_PTR
_WebKitHitTestResult = OPAQUE_PTR
_WebKitWebSettings = OPAQUE_PTR
_GBoxed = OPAQUE_PTR
_GtkPathPriorityType = OPAQUE_PTR
_JSClass = OPAQUE_PTR
_WebKitWebHistoryItem = OPAQUE_PTR
_JSValue = OPAQUE_PTR
_GdkPoint = OPAQUE_PTR
_GAppInfo = OPAQUE_PTR
_GtkSettings = OPAQUE_PTR
_GSource = OPAQUE_PTR
_PangoFontMap = OPAQUE_PTR
_GIOStream = OPAQUE_PTR
_GIOStream = OPAQUE_PTR
_JSString = OPAQUE_PTR
_PangoAttrList = OPAQUE_PTR
_GOutputStream = OPAQUE_PTR
_PangoMatrix = OPAQUE_PTR
_GSource = OPAQUE_PTR
_GtkMisc = OPAQUE_PTR
_GtkApplication = OPAQUE_PTR
_GFileInfo = OPAQUE_PTR
_PangoAnalysis = OPAQUE_PTR
_GEmblemedIcon = OPAQUE_PTR
_PangoFontDescription = OPAQUE_PTR
_GdkCursor = OPAQUE_PTR
_GtkBorder = OPAQUE_PTR
_WebKitWebInspector = OPAQUE_PTR
_GdkWindowAttr = OPAQUE_PTR
_GOptionGroup = OPAQUE_PTR
_GScanner = OPAQUE_PTR
_GFileAttributeInfoList = OPAQUE_PTR
_GCancellable = OPAQUE_PTR
_GtkWidgetClass = OPAQUE_PTR
_GtkContainerClass = OPAQUE_PTR
_GdkEventKey = OPAQUE_PTR
_GtkAdjustment = OPAQUE_PTR
_GdkDragContext = OPAQUE_PTR
_GdkDisplay = OPAQUE_PTR
_GFileIOStream = OPAQUE_PTR
_GtkSettings = OPAQUE_PTR
_GdkScreen = OPAQUE_PTR
_PangoFontMetrics = OPAQUE_PTR
_GCond = OPAQUE_PTR
_GtkIconSource = OPAQUE_PTR
_cairo_surface_t = OPAQUE_PTR
_GdkVisual = OPAQUE_PTR
_PangoFontMap = OPAQUE_PTR
_GSList = OPAQUE_PTR
_WebKitWebFrame = OPAQUE_PTR
_JSString = OPAQUE_PTR
_GActionGroup = OPAQUE_PTR
_cairo_region_t = OPAQUE_PTR
_GtkScrolledWindow = OPAQUE_PTR
_WebKitNetworkRequest = OPAQUE_PTR
_GdkWindow = OPAQUE_PTR
_PangoFontFamily = OPAQUE_PTR
_JSContextGroup = OPAQUE_PTR
_GFile = OPAQUE_PTR
_PangoLayoutIter = OPAQUE_PTR
_GtkClipboard = OPAQUE_PTR
_PangoLayoutRun = OPAQUE_PTR
_GFileInputStream = OPAQUE_PTR
_PangoFontset = OPAQUE_PTR
_GdkWindow = OPAQUE_PTR
_PangoFontDescription = OPAQUE_PTR
_GtkBorder = OPAQUE_PTR
_JSPropertyNameArray = OPAQUE_PTR
_GError = OPAQUE_PTR
_PangoCoverage = OPAQUE_PTR
_GtkAboutDialog = OPAQUE_PTR
_WebKitViewportAttributes = OPAQUE_PTR
_JSClass = OPAQUE_PTR
_WebKitWebHistoryItem = OPAQUE_PTR
_PangoFontFamily = OPAQUE_PTR
_cairo_t = OPAQUE_PTR
_GWeakRef = OPAQUE_PTR
_GdkPixbufAnimationIter = OPAQUE_PTR
_GdkVisual = OPAQUE_PTR
_GdkEventButton = OPAQUE_PTR
_GCancellable = OPAQUE_PTR
_CairoPattern = OPAQUE_PTR
_GdkDevice = OPAQUE_PTR
_GMount = OPAQUE_PTR
_PangoRectangle = OPAQUE_PTR
_GtkAccelGroup = OPAQUE_PTR
_GObject = OPAQUE_PTR
_GPollFD = OPAQUE_PTR
_GtkIconSource = OPAQUE_PTR
_GFile = OPAQUE_PTR
_JSContext = OPAQUE_PTR
_GDrive = OPAQUE_PTR
_PangoFontsetSimple = OPAQUE_PTR
_GtkAllocation = OPAQUE_PTR
_GtkWidget = OPAQUE_PTR
_PangoLayoutLine = OPAQUE_PTR
_GtkIconSet = OPAQUE_PTR
_WebKitWebView = OPAQUE_PTR
_GMutex = OPAQUE_PTR
_PangoTabArray = OPAQUE_PTR
_GtkStyleContext = OPAQUE_PTR
_GValue = OPAQUE_PTR
_GdkDeviceManager = OPAQUE_PTR
_GtkStatusbar = OPAQUE_PTR
_GdkCursor = OPAQUE_PTR
_WebKitDOMDocument = OPAQUE_PTR
_PangoMatrix = OPAQUE_PTR
_GtkPrintOperation = OPAQUE_PTR
_GtkThemingEngine = OPAQUE_PTR
_GString = OPAQUE_PTR
_PangoContext = OPAQUE_PTR
_GFileInfo = OPAQUE_PTR
_GList = OPAQUE_PTR
_WebKitWebView = OPAQUE_PTR
_WebKitWebWindowFeatures = OPAQUE_PTR
_PangoCoverage = OPAQUE_PTR
_GParamSpec = OPAQUE_PTR
_GList = OPAQUE_PTR
_GdkRGBA = OPAQUE_PTR
_GTimeVal = OPAQUE_PTR
_GtkInvisible = OPAQUE_PTR
_GSourceFuncs = OPAQUE_PTR
_JSPropertyNameAccumulator = OPAQUE_PTR
_PangoGlyphString = OPAQUE_PTR
_JSGlobalContext = OPAQUE_PTR
_GFileIOStream = OPAQUE_PTR
_WebKitSecurityOrigin = OPAQUE_PTR
_GObjectClass = OPAQUE_PTR
_GSList = OPAQUE_PTR
_PangoAnalysis = OPAQUE_PTR
_GtkStylePropertyParser = OPAQUE_PTR
_GdkWindowAttr = OPAQUE_PTR
_SoupMessage = OPAQUE_PTR
_WebKitWebDataSource = OPAQUE_PTR
_GdkColor = OPAQUE_PTR
_GdkPixbufAnimation = OPAQUE_PTR
_GEmblem = OPAQUE_PTR
_GdkRectangle = OPAQUE_PTR
_PangoLanguage = OPAQUE_PTR
_PangoAttrList = OPAQUE_PTR
_gunichar = OPAQUE_PTR
_GVolume = OPAQUE_PTR
_GdkWMDecoration = OPAQUE_PTR
_PangoLogAttr = OPAQUE_PTR
_PangoLayout = OPAQUE_PTR
_GPollFD = OPAQUE_PTR
_GFileOutputStream = OPAQUE_PTR
_JSObject = OPAQUE_PTR
_WebKitDOMNode = OPAQUE_PTR
_GInputStream = OPAQUE_PTR
_GtkStyleProperties = OPAQUE_PTR
_WebKitWebNavigationAction = OPAQUE_PTR
_GtkStyle = OPAQUE_PTR
_GParameter = OPAQUE_PTR
_GtkStyle = OPAQUE_PTR
_GIcon = OPAQUE_PTR
_GtkWindow = OPAQUE_PTR
_GtkGradient = OPAQUE_PTR
_cairo_pattern_t = OPAQUE_PTR
_GdkPixbuf = OPAQUE_PTR
_GdkScreen = OPAQUE_PTR
_GMountOperation = OPAQUE_PTR
_GtkWidgetPath = OPAQUE_PTR
_JSPropertyNameArray = OPAQUE_PTR
_GSourceCallbackFuncs = OPAQUE_PTR
_PangoFontFace = OPAQUE_PTR
_GtkTargetEntry = OPAQUE_PTR
_GtkApplication = OPAQUE_PTR
_CairoPattern = OPAQUE_PTR
_GByteArray = OPAQUE_PTR
_GdkPixbufSimpleAnim = OPAQUE_PTR
_JSObject = OPAQUE_PTR
_WebKitGeolocationPolicyDecision = OPAQUE_PTR
_PangoLanguage = OPAQUE_PTR
_GdkDevice = OPAQUE_PTR
_PangoTabArray = OPAQUE_PTR
"""Enumerations"""
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
GdkCursorType = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GtkIconSize = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
cairo_extend_t = c_int
cairo_filter_t = c_int
CairoPatternype_t = c_int
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
GApplicationFlags = c_int
GtkDialogFlags = c_int
GtkResponseType = c_int
WebKitWebNavigationReason = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GMountMountFlags = c_int
GMountUnmountFlags = c_int
GDriveStartFlags = c_int
GDriveStartStopType = c_int
cairo_extend_t = c_int
cairo_filter_t = c_int
CairoPatternype_t = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkLicense = c_int
GtkIconSize = c_int
GDriveStartFlags = c_int
GDriveStartStopType = c_int

try:
    libjavascriptcore.JSGlobalContextRelease.restype = None
    libjavascriptcore.JSGlobalContextRelease.argtypes = [_JSContext,_JSGlobalContext]
except:
   pass
try:
    libjavascriptcore.JSContextGroupRelease.restype = None
    libjavascriptcore.JSContextGroupRelease.argtypes = [_JSContext,_JSContextGroup]
except:
   pass
try:
    libjavascriptcore.JSContextGetGroup.restype = _JSContextGroup
    libjavascriptcore.JSContextGetGroup.argtypes = [_JSContext]
except:
   pass
try:
    libjavascriptcore.JSContextGetGlobalObject.restype = _JSObject
    libjavascriptcore.JSContextGetGlobalObject.argtypes = [_JSContext]
except:
   pass
try:
    libjavascriptcore.JSGlobalContextCreate.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextCreate.argtypes = [_JSClass]
except:
   pass
try:
    libjavascriptcore.JSGlobalContextCreateInGroup.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextCreateInGroup.argtypes = [_JSContextGroup,_JSClass]
except:
   pass
try:
    libjavascriptcore.JSContextGroupRetain.restype = _JSContextGroup
    libjavascriptcore.JSContextGroupRetain.argtypes = [_JSContextGroup]
except:
   pass
try:
    libjavascriptcore.JSGlobalContextRetain.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextRetain.argtypes = [_JSGlobalContext]
except:
   pass
from . import javascriptcore__JSObject

import weakref

class JSContext( javascriptcore__JSObject.JSObject):
    """Class JSContext Constructors"""
        
    """Methods"""
    def JSGlobalContextRelease(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()

        
        libjavascriptcore.JSGlobalContextRelease( self._object(),ctx )

    def GroupRelease(  self, group, ):
        if group: group = group._object()
        else: group = OPAQUE_PTR()

        
        libjavascriptcore.JSContextGroupRelease( self._object(),group )

    def GetGroup(  self, ):

        from .javascriptcore import JSContextGroup
        return JSContextGroup( obj=libjavascriptcore.JSContextGetGroup( self._object() )  or OPAQUE_PTR())

    def GetGlobalObject(  self, ):

        from .javascriptcore import JSObject
        return JSObject( obj=libjavascriptcore.JSContextGetGlobalObject( self._object() )  or OPAQUE_PTR())

    @staticmethod
    def JSGlobalContextCreate( globalObjectClass,):
        if globalObjectClass: globalObjectClass = globalObjectClass._object()
        else: globalObjectClass = OPAQUE_PTR()
        from .javascriptcore import JSGlobalContext
        return JSGlobalContext( obj=    libjavascriptcore.JSGlobalContextCreate(globalObjectClass, )
  or OPAQUE_PTR())
    @staticmethod
    def JSGlobalContextCreateInGroup( group, globalObjectClass,):
        if group: group = group._object()
        else: group = OPAQUE_PTR()
        if globalObjectClass: globalObjectClass = globalObjectClass._object()
        else: globalObjectClass = OPAQUE_PTR()
        from .javascriptcore import JSGlobalContext
        return JSGlobalContext( obj=    libjavascriptcore.JSGlobalContextCreateInGroup(group, globalObjectClass, )
  or OPAQUE_PTR())
    @staticmethod
    def GroupRetain( group,):
        if group: group = group._object()
        else: group = OPAQUE_PTR()
        from .javascriptcore import JSContextGroup
        return JSContextGroup( obj=    libjavascriptcore.JSContextGroupRetain(group, )
  or OPAQUE_PTR())
    @staticmethod
    def JSGlobalContextRetain( ctx,):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        from .javascriptcore import JSGlobalContext
        return JSGlobalContext( obj = libjavascriptcore.JSGlobalContextRetain(ctx, )
  or OPAQUE_PTR())

    def __init__(self, obj = None):
        javascriptcore__JSObject.JSObject.__init__(self, obj, None)
        self._global = None

    def GetGlobalObject(  self, ):
       if not self._global:
           from .javascriptcore import JSObject
           self._global = JSObject( obj=libjavascriptcore.JSContextGetGlobalObject( self._object() ), context = self)
       return self._global


    def get_jsobject(context, name , can_call=False):
        from .javascript import strid, JavascriptClass, JSString, JSFunction
        ident = strid(context)
        import logging
        retval = JavascriptClass._globalobjects.get(ident + name)
        
        if retval is None:
            names = name.split('.')
            obj = JSContext.GetGlobalObject(context)
            import logging
            for n in names:
                text = JSString.CreateWithUTF8CString( n )
                obj = obj.GetProperty( text, NULL)
                text.Release()
                if not obj:
                    break
            if obj:
                valtype = obj.GetType( context )
                if valtype == kJSTypeObject.value:
                    retval = obj.ToObject( context, NULL )
                    can_call = retval.IsFunction(context)
                    if can_call:
                        retval = JSFunction( context, obj = retval, thisobj = None, name = name)
                elif valtype == kJSTypeNull.value or valtype == kJSTypeUndefined.value:
                    retval = None#obj.ToObject(context, NULL)
                elif valtype == kJSTypeNumber.value:
                    retval = obj.ToNumber( context, NULL )
                elif valtype == kJSTypeBoolean.value:
                    retval = obj.ToBoolean( context )
                elif valtype == kJSTypeString.value:
                    retval = obj.ToStringCopy(context, NULL )
                else:
                    logging.error("Invalid javascript value type encountered!: %d" % valtype)
                    retval = None
            if retval:
                JavascriptClass._globalobjects[ident + name] = retval
            #self._webview.execute_script("python.export_to_python(%s,'%s', %s);" % (name, name, int(can_call)))
            retval = JavascriptClass._globalobjects.get(ident + name)
            if not retval:
                raise Exception("Unknown javascript object by name %s" % name)
        JavascriptClass._globalobjects[ident + name] = retval
        return retval


