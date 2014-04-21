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
_GtkMessageDialog = POINTER(c_void_p)
_WebKitNetworkResponse = POINTER(c_void_p)
_GtkLabel = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkBin = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
_WebKitWebPolicyDecision = POINTER(c_void_p)
_PangoEngineShape = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_GAsyncResult = POINTER(c_void_p)
_cairo_matrix_t = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_JSValue = POINTER(c_void_p)
_GtkProgressBar = POINTER(c_void_p)
_JSContext = POINTER(c_void_p)
_GtkIconFactory = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GMainLoop = POINTER(c_void_p)
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
_GdkGeometry = POINTER(c_void_p)
_GAppLauncContext = POINTER(c_void_p)
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
_GtkAssistant = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GFileIOStream = POINTER(c_void_p)
_GAppLaunchContext = POINTER(c_void_p)
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
_JSContextGroup = POINTER(c_void_p)
_GFile = POINTER(c_void_p)
_PangoLayoutIter = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoLayoutRun = POINTER(c_void_p)
_GFileInputStream = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_GdkPixbufAnimation = POINTER(c_void_p)
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
_GtkImage = POINTER(c_void_p)
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
_GtkTargetList = POINTER(c_void_p)
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
_JSGlobalContext = POINTER(c_void_p)
_GFileIOStream = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_GtkStylePropertyParser = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_SoupMessage = POINTER(c_void_p)
_WebKitWebDataSource = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GtkBox = POINTER(c_void_p)
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
_GdkDragContext = POINTER(c_void_p)
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
_GtkPackType = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GMountOperation = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_JSPropertyNameArray = POINTER(c_void_p)
_GSourceCallbackFuncs = POINTER(c_void_p)
_PangoFontFace = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_GtkCssSection = POINTER(c_void_p)
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
GtkAssistantPageType = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
GtkDestDefaults = c_int
GtkTargetFlags = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
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
GtkMessageType = c_int
GtkButtonsType = c_int
WebKitEditingBehavior = c_int

try:
    libgtk3.gtk_image_set_from_icon_set.restype = None
    libgtk3.gtk_image_set_from_icon_set.argtypes = [_GtkImage,_GtkIconSet,GtkIconSize]
except:
   pass
try:
    libgtk3.gtk_image_set_from_animation.restype = None
    libgtk3.gtk_image_set_from_animation.argtypes = [_GtkImage,_GdkPixbufAnimation]
except:
   pass
try:
    libgtk3.gtk_image_set_from_pixbuf.restype = None
    libgtk3.gtk_image_set_from_pixbuf.argtypes = [_GtkImage,_GdkPixbuf]
except:
   pass
try:
    libgtk3.gtk_image_get_icon_set.restype = None
    libgtk3.gtk_image_get_icon_set.argtypes = [_GtkImage,_GtkIconSet,POINTER(GtkIconSize)]
except:
   pass
try:
    libgtk3.gtk_image_get_icon_name.restype = None
    libgtk3.gtk_image_get_icon_name.argtypes = [_GtkImage,Asciifier,POINTER(GtkIconSize)]
except:
   pass
try:
    libgtk3.gtk_image_set_from_stock.restype = None
    libgtk3.gtk_image_set_from_stock.argtypes = [_GtkImage,Asciifier,GtkIconSize]
except:
   pass
try:
    libgtk3.gtk_image_get_storage_type.restype = GtkImageType
    libgtk3.gtk_image_get_storage_type.argtypes = [_GtkImage]
except:
   pass
try:
    libgtk3.gtk_image_set_from_gicon.restype = None
    libgtk3.gtk_image_set_from_gicon.argtypes = [_GtkImage,_GIcon,GtkIconSize]
except:
   pass
try:
    libgtk3.gtk_image_set_from_icon_name.restype = None
    libgtk3.gtk_image_set_from_icon_name.argtypes = [_GtkImage,Asciifier,GtkIconSize]
except:
   pass
try:
    libgtk3.gtk_image_get_stock.restype = None
    libgtk3.gtk_image_get_stock.argtypes = [_GtkImage,Asciifier,POINTER(GtkIconSize)]
except:
   pass
try:
    libgtk3.gtk_image_set_from_resource.restype = None
    libgtk3.gtk_image_set_from_resource.argtypes = [_GtkImage,Asciifier]
except:
   pass
try:
    libgtk3.gtk_image_get_pixbuf.restype = _GdkPixbuf
    libgtk3.gtk_image_get_pixbuf.argtypes = [_GtkImage]
except:
   pass
try:
    libgtk3.gtk_image_get_pixel_size.restype = gint
    libgtk3.gtk_image_get_pixel_size.argtypes = [_GtkImage]
except:
   pass
try:
    libgtk3.gtk_image_get_animation.restype = _GdkPixbufAnimation
    libgtk3.gtk_image_get_animation.argtypes = [_GtkImage]
except:
   pass
try:
    libgtk3.gtk_image_get_gicon.restype = None
    libgtk3.gtk_image_get_gicon.argtypes = [_GtkImage,_GIcon,POINTER(GtkIconSize)]
except:
   pass
try:
    libgtk3.gtk_image_set_pixel_size.restype = None
    libgtk3.gtk_image_set_pixel_size.argtypes = [_GtkImage,gint]
except:
   pass
try:
    libgtk3.gtk_image_clear.restype = None
    libgtk3.gtk_image_clear.argtypes = [_GtkImage]
except:
   pass
try:
    libgtk3.gtk_image_set_from_file.restype = None
    libgtk3.gtk_image_set_from_file.argtypes = [_GtkImage,Asciifier]
except:
   pass
try:
    libgtk3.gtk_image_new_from_pixbuf.restype = _GtkWidget
    libgtk3.gtk_image_new_from_pixbuf.argtypes = [_GdkPixbuf]
except:
   pass
try:
    libgtk3.gtk_image_new_from_stock.restype = _GtkWidget
    libgtk3.gtk_image_new_from_stock.argtypes = [Asciifier,GtkIconSize]
except:
   pass
try:
    libgtk3.gtk_image_new_from_gicon.restype = _GtkWidget
    libgtk3.gtk_image_new_from_gicon.argtypes = [_GIcon,GtkIconSize]
except:
   pass
try:
    libgtk3.gtk_image_new_from_resource.restype = _GtkWidget
    libgtk3.gtk_image_new_from_resource.argtypes = [Asciifier]
except:
   pass
try:
    libgtk3.gtk_image_new_from_file.restype = _GtkWidget
    libgtk3.gtk_image_new_from_file.argtypes = [Asciifier]
except:
   pass
try:
    libgtk3.gtk_image_new_from_icon_set.restype = _GtkWidget
    libgtk3.gtk_image_new_from_icon_set.argtypes = [_GtkIconSet,GtkIconSize]
except:
   pass
try:
    libgtk3.gtk_image_new_from_animation.restype = _GtkWidget
    libgtk3.gtk_image_new_from_animation.argtypes = [_GdkPixbufAnimation]
except:
   pass
try:
    libgtk3.gtk_image_new_from_icon_name.restype = _GtkWidget
    libgtk3.gtk_image_new_from_icon_name.argtypes = [Asciifier,GtkIconSize]
except:
   pass
from . import gtk3__GtkMisc
class GtkImage( gtk3__GtkMisc.GtkMisc):
    """Class GtkImage Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_image_new.restype = POINTER(c_void_p)
            
            libgtk3.gtk_image_new.argtypes = []
            self._object = libgtk3.gtk_image_new()

    """Methods"""
    def set_from_icon_set(  self, icon_set, size, ):
        if icon_set: icon_set = icon_set._object
        else: icon_set = POINTER(c_void_p)()

        
        libgtk3.gtk_image_set_from_icon_set( self._object,icon_set,size )

    def set_from_animation(  self, animation, ):
        if animation: animation = animation._object
        else: animation = POINTER(c_void_p)()

        
        libgtk3.gtk_image_set_from_animation( self._object,animation )

    def set_from_pixbuf(  self, pixbuf, ):
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_void_p)()

        
        libgtk3.gtk_image_set_from_pixbuf( self._object,pixbuf )

    def get_icon_set(  self, icon_set, size, ):
        if icon_set: icon_set = icon_set._object
        else: icon_set = POINTER(c_void_p)()

        
        libgtk3.gtk_image_get_icon_set( self._object,icon_set,size )

    def get_icon_name(  self, icon_name, size, ):

        
        libgtk3.gtk_image_get_icon_name( self._object,icon_name,size )

    def set_from_stock(  self, stock_id, size, ):

        
        libgtk3.gtk_image_set_from_stock( self._object,stock_id,size )

    def get_storage_type(  self, ):

        
        return libgtk3.gtk_image_get_storage_type( self._object )

    def set_from_gicon(  self, icon, size, ):
        if icon: icon = icon._object
        else: icon = POINTER(c_void_p)()

        
        libgtk3.gtk_image_set_from_gicon( self._object,icon,size )

    def set_from_icon_name(  self, icon_name, size, ):

        
        libgtk3.gtk_image_set_from_icon_name( self._object,icon_name,size )

    def get_stock(  self, stock_id, size, ):

        
        libgtk3.gtk_image_get_stock( self._object,stock_id,size )

    def set_from_resource(  self, resource_path, ):

        
        libgtk3.gtk_image_set_from_resource( self._object,resource_path )

    def get_pixbuf(  self, ):

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_image_get_pixbuf( self._object ) or POINTER(c_void_p)())

    def get_pixel_size(  self, ):

        
        return libgtk3.gtk_image_get_pixel_size( self._object )

    def get_animation(  self, ):

        from .gobject import GdkPixbufAnimation
        return GdkPixbufAnimation( obj=libgtk3.gtk_image_get_animation( self._object ) or POINTER(c_void_p)())

    def get_gicon(  self, gicon, size, ):
        if gicon: gicon = gicon._object
        else: gicon = POINTER(c_void_p)()

        
        libgtk3.gtk_image_get_gicon( self._object,gicon,size )

    def set_pixel_size(  self, pixel_size, ):

        
        libgtk3.gtk_image_set_pixel_size( self._object,pixel_size )

    def clear(  self, ):

        
        libgtk3.gtk_image_clear( self._object )

    def set_from_file(  self, filename, ):

        
        libgtk3.gtk_image_set_from_file( self._object,filename )

    @staticmethod
    def new_from_pixbuf( pixbuf,):
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_void_p)()
        from .gtk3 import GtkWidget
        return GtkWidget(None, obj=    libgtk3.gtk_image_new_from_pixbuf(pixbuf, )
 or POINTER(c_void_p)())
    @staticmethod
    def new_from_stock( stock_id, size,):
        from .gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_image_new_from_stock(stock_id, size, )
 or POINTER(c_void_p)())
    @staticmethod
    def new_from_gicon( icon, size,):
        if icon: icon = icon._object
        else: icon = POINTER(c_void_p)()
        from .gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_image_new_from_gicon(icon, size, )
 or POINTER(c_void_p)())
    @staticmethod
    def new_from_resource( resource_path,):
        from .gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_image_new_from_resource(resource_path, )
 or POINTER(c_void_p)())
    @staticmethod
    def new_from_file( filename,):
        from .gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_image_new_from_file(filename, )
 or POINTER(c_void_p)())
    @staticmethod
    def new_from_icon_set( icon_set, size,):
        if icon_set: icon_set = icon_set._object
        else: icon_set = POINTER(c_void_p)()
        from .gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_image_new_from_icon_set(icon_set, size, )
 or POINTER(c_void_p)())
    @staticmethod
    def new_from_animation( animation,):
        if animation: animation = animation._object
        else: animation = POINTER(c_void_p)()
        from .gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_image_new_from_animation(animation, )
 or POINTER(c_void_p)())
    @staticmethod
    def new_from_icon_name( icon_name, size,):
        from .gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_image_new_from_icon_name(icon_name, size, )
 or POINTER(c_void_p)())
