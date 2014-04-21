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
from .gtk3_types import *
from .gtk3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_void_p)
_GdkGeometry = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_WebKitNetworkResponse = POINTER(c_void_p)
_GtkLabel = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
_PangoEngineShape = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_GAsyncResult = POINTER(c_void_p)
_cairo_matrix_t = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_JSValue = POINTER(c_void_p)
_GtkIconFactory = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GdkTimeCoord = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GtkContainer = POINTER(c_void_p)
_PangoItem = POINTER(c_void_p)
_GClosure = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GMainContext = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GInterface = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_JSContextGroup = POINTER(c_void_p)
_GFileEnumerator = POINTER(c_void_p)
_GtkDialog = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GtkCssProvider = POINTER(c_void_p)
_GtkSymbolicColor = POINTER(c_void_p)
_void = POINTER(c_void_p)
_GtkStyleProperties = POINTER(c_void_p)
_GInputStream = POINTER(c_void_p)
_GtkIconInfo = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_WebKitWebResource = POINTER(c_void_p)
_GBytes = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GMainContext = POINTER(c_void_p)
_GtkTextBuffer = POINTER(c_void_p)
_GtkTargetList = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
_GtkNumerableIcon = POINTER(c_void_p)
_GdkAppLaunchContext = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GtkSymbolicColor = POINTER(c_void_p)
_WebKitWebBackForwardList = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_GtkOffscreenWindow = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GAppLaunchContext = POINTER(c_void_p)
_PangoAttrIterator = POINTER(c_void_p)
_GFileAttributeMatcher = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GtkIconTheme = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_GtkAccelLabel = POINTER(c_void_p)
_GtkAdjustment = POINTER(c_void_p)
_JSGlobalContext = POINTER(c_void_p)
_GApplication = POINTER(c_void_p)
_GFileMonitor = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_GString = POINTER(c_void_p)
_GFileAttributeMatcher = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_WebKitHitTestResult = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
_GBoxed = POINTER(c_void_p)
_GtkPathPriorityType = POINTER(c_void_p)
_JSClass = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_JSValue = POINTER(c_void_p)
_GdkPoint = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GSource = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GIOStream = POINTER(c_void_p)
_GIOStream = POINTER(c_void_p)
_JSString = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_GOutputStream = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GSource = POINTER(c_void_p)
_GtkMisc = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_GFileInfo = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_GEmblemedIcon = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_WebKitWebInspector = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_GOptionGroup = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_GFileAttributeInfoList = POINTER(c_void_p)
_GCancellable = POINTER(c_void_p)
_GtkWidgetClass = POINTER(c_void_p)
_GtkContainerClass = POINTER(c_void_p)
_GdkEventKey = POINTER(c_void_p)
_GtkAdjustment = POINTER(c_void_p)
_GdkDragContext = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GFileIOStream = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_PangoFontMetrics = POINTER(c_void_p)
_GCond = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_cairo_surface_t = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_WebKitWebFrame = POINTER(c_void_p)
_JSString = POINTER(c_void_p)
_GActionGroup = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_GtkScrolledWindow = POINTER(c_void_p)
_WebKitNetworkRequest = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_GFile = POINTER(c_void_p)
_PangoLayoutIter = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoLayoutRun = POINTER(c_void_p)
_GFileInputStream = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_JSPropertyNameArray = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GtkAboutDialog = POINTER(c_void_p)
_WebKitViewportAttributes = POINTER(c_void_p)
_JSClass = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_cairo_t = POINTER(c_void_p)
_GWeakRef = POINTER(c_void_p)
_GdkPixbufAnimationIter = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GdkEventButton = POINTER(c_void_p)
_GCancellable = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_GMount = POINTER(c_void_p)
_PangoRectangle = POINTER(c_void_p)
_GtkAccelGroup = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_GPollFD = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GFile = POINTER(c_void_p)
_JSContext = POINTER(c_void_p)
_GDrive = POINTER(c_void_p)
_PangoFontsetSimple = POINTER(c_void_p)
_GtkAllocation = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_PangoLayoutLine = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_GMutex = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GtkStatusbar = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitDOMDocument = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkPrintOperation = POINTER(c_void_p)
_GtkThemingEngine = POINTER(c_void_p)
_GString = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GFileInfo = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_GTimeVal = POINTER(c_void_p)
_GtkInvisible = POINTER(c_void_p)
_GSourceFuncs = POINTER(c_void_p)
_JSPropertyNameAccumulator = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_GFileIOStream = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_GtkStylePropertyParser = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_SoupMessage = POINTER(c_void_p)
_WebKitWebDataSource = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GdkPixbufAnimation = POINTER(c_void_p)
_GEmblem = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_gunichar = POINTER(c_void_p)
_GVolume = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GPollFD = POINTER(c_void_p)
_GFileOutputStream = POINTER(c_void_p)
_JSObject = POINTER(c_void_p)
_WebKitDOMNode = POINTER(c_void_p)
_GInputStream = POINTER(c_void_p)
_GtkStyleProperties = POINTER(c_void_p)
_WebKitWebNavigationAction = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GParameter = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_GtkGradient = POINTER(c_void_p)
_cairo_pattern_t = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GMountOperation = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_JSPropertyNameArray = POINTER(c_void_p)
_GSourceCallbackFuncs = POINTER(c_void_p)
_PangoFontFace = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GByteArray = POINTER(c_void_p)
_GdkPixbufSimpleAnim = POINTER(c_void_p)
_JSObject = POINTER(c_void_p)
_WebKitGeolocationPolicyDecision = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
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
    libgtk3.gtk_scrolled_window_get_shadow_type.restype = GtkShadowType
    libgtk3.gtk_scrolled_window_get_shadow_type.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_get_min_content_height.restype = gint
    libgtk3.gtk_scrolled_window_get_min_content_height.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_get_hscrollbar.restype = _GtkWidget
    libgtk3.gtk_scrolled_window_get_hscrollbar.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_get_placement.restype = GtkCornerType
    libgtk3.gtk_scrolled_window_get_placement.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_set_min_content_height.restype = None
    libgtk3.gtk_scrolled_window_set_min_content_height.argtypes = [_GtkScrolledWindow,gint]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_set_min_content_width.restype = None
    libgtk3.gtk_scrolled_window_set_min_content_width.argtypes = [_GtkScrolledWindow,gint]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_set_shadow_type.restype = None
    libgtk3.gtk_scrolled_window_set_shadow_type.argtypes = [_GtkScrolledWindow,GtkShadowType]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_add_with_viewport.restype = None
    libgtk3.gtk_scrolled_window_add_with_viewport.argtypes = [_GtkScrolledWindow,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_get_vscrollbar.restype = _GtkWidget
    libgtk3.gtk_scrolled_window_get_vscrollbar.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_set_placement.restype = None
    libgtk3.gtk_scrolled_window_set_placement.argtypes = [_GtkScrolledWindow,GtkCornerType]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_set_hadjustment.restype = None
    libgtk3.gtk_scrolled_window_set_hadjustment.argtypes = [_GtkScrolledWindow,_GtkAdjustment]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_get_policy.restype = None
    libgtk3.gtk_scrolled_window_get_policy.argtypes = [_GtkScrolledWindow,POINTER(GtkPolicyType),POINTER(GtkPolicyType)]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_get_vadjustment.restype = _GtkAdjustment
    libgtk3.gtk_scrolled_window_get_vadjustment.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_get_min_content_width.restype = gint
    libgtk3.gtk_scrolled_window_get_min_content_width.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_set_vadjustment.restype = None
    libgtk3.gtk_scrolled_window_set_vadjustment.argtypes = [_GtkScrolledWindow,_GtkAdjustment]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_unset_placement.restype = None
    libgtk3.gtk_scrolled_window_unset_placement.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_get_hadjustment.restype = _GtkAdjustment
    libgtk3.gtk_scrolled_window_get_hadjustment.argtypes = [_GtkScrolledWindow]
except:
   pass
try:
    libgtk3.gtk_scrolled_window_set_policy.restype = None
    libgtk3.gtk_scrolled_window_set_policy.argtypes = [_GtkScrolledWindow,GtkPolicyType,GtkPolicyType]
except:
   pass
from . import gtk3__GtkBin
class GtkScrolledWindow( gtk3__GtkBin.GtkBin):
    """Class GtkScrolledWindow Constructors"""
    def __init__( self, hadjustment, vadjustment,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_scrolled_window_new.restype = POINTER(c_void_p)
            
            if hadjustment : hadjustment = hadjustment._object
            else :  hadjustment = POINTER(c_void_p)()

            if vadjustment : vadjustment = vadjustment._object
            else :  vadjustment = POINTER(c_void_p)()

            libgtk3.gtk_scrolled_window_new.argtypes = [_GtkAdjustment,_GtkAdjustment]
            self._object = libgtk3.gtk_scrolled_window_new(hadjustment, vadjustment, )

    """Methods"""
    def get_shadow_type(  self, ):

        
        return libgtk3.gtk_scrolled_window_get_shadow_type( self._object )

    def get_min_content_height(  self, ):

        
        return libgtk3.gtk_scrolled_window_get_min_content_height( self._object )

    def get_hscrollbar(  self, ):

        from .gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_scrolled_window_get_hscrollbar( self._object ) or POINTER(c_void_p)())

    def get_placement(  self, ):

        
        return libgtk3.gtk_scrolled_window_get_placement( self._object )

    def set_min_content_height(  self, height, ):

        
        libgtk3.gtk_scrolled_window_set_min_content_height( self._object,height )

    def set_min_content_width(  self, width, ):

        
        libgtk3.gtk_scrolled_window_set_min_content_width( self._object,width )

    def set_shadow_type(  self, type, ):

        
        libgtk3.gtk_scrolled_window_set_shadow_type( self._object,type )

    def add_with_viewport(  self, child, ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()

        
        libgtk3.gtk_scrolled_window_add_with_viewport( self._object,child )

    def get_vscrollbar(  self, ):

        from .gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_scrolled_window_get_vscrollbar( self._object ) or POINTER(c_void_p)())

    def set_placement(  self, window_placement, ):

        
        libgtk3.gtk_scrolled_window_set_placement( self._object,window_placement )

    def set_hadjustment(  self, hadjustment, ):
        if hadjustment: hadjustment = hadjustment._object
        else: hadjustment = POINTER(c_void_p)()

        
        libgtk3.gtk_scrolled_window_set_hadjustment( self._object,hadjustment )

    def get_policy(  self, hscrollbar_policy, vscrollbar_policy, ):

        
        libgtk3.gtk_scrolled_window_get_policy( self._object,hscrollbar_policy,vscrollbar_policy )

    def get_vadjustment(  self, ):

        from .gtk3 import GtkAdjustment
        return GtkAdjustment(None,None, obj=libgtk3.gtk_scrolled_window_get_vadjustment( self._object ) or POINTER(c_void_p)())

    def get_min_content_width(  self, ):

        
        return libgtk3.gtk_scrolled_window_get_min_content_width( self._object )

    def set_vadjustment(  self, vadjustment, ):
        if vadjustment: vadjustment = vadjustment._object
        else: vadjustment = POINTER(c_void_p)()

        
        libgtk3.gtk_scrolled_window_set_vadjustment( self._object,vadjustment )

    def unset_placement(  self, ):

        
        libgtk3.gtk_scrolled_window_unset_placement( self._object )

    def get_hadjustment(  self, ):

        from .gtk3 import GtkAdjustment
        return GtkAdjustment(None, obj=libgtk3.gtk_scrolled_window_get_hadjustment( self._object ) or POINTER(c_void_p)())

    def set_policy(  self, hscrollbar_policy, vscrollbar_policy, ):

        
        libgtk3.gtk_scrolled_window_set_policy( self._object,hscrollbar_policy,vscrollbar_policy )

