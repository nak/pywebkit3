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

try:
    libgtk3.gdk_window_get_geometry.restype = None
    libgtk3.gdk_window_get_geometry.argtypes = [_GdkWindow,POINTER(gint),POINTER(gint),POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gdk_window_set_background_rgba.restype = None
    libgtk3.gdk_window_set_background_rgba.argtypes = [_GdkWindow,_GdkRGBA]
except:
   pass
try:
    libgtk3.gdk_window_get_screen.restype = _GdkScreen
    libgtk3.gdk_window_get_screen.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_has_native.restype = gboolean
    libgtk3.gdk_window_has_native.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_constrain_size.restype = None
    libgtk3.gdk_window_constrain_size.argtypes = [_GdkWindow,_GdkGeometry,guint,gint,gint,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gdk_window_set_urgency_hint.restype = None
    libgtk3.gdk_window_set_urgency_hint.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_is_input_only.restype = gboolean
    libgtk3.gdk_window_is_input_only.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_lower.restype = None
    libgtk3.gdk_window_lower.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_composited.restype = None
    libgtk3.gdk_window_set_composited.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_set_icon_list.restype = None
    libgtk3.gdk_window_set_icon_list.argtypes = [_GdkWindow,_GList]
except:
   pass
try:
    libgtk3.gdk_window_enable_synchronized_configure.restype = None
    libgtk3.gdk_window_enable_synchronized_configure.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_iconify.restype = None
    libgtk3.gdk_window_iconify.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_decorations.restype = None
    libgtk3.gdk_window_set_decorations.argtypes = [_GdkWindow,GdkWMDecoration]
except:
   pass
try:
    libgtk3.gdk_window_set_source_events.restype = None
    libgtk3.gdk_window_set_source_events.argtypes = [_GdkWindow,GdkInputSource,GdkEventMask]
except:
   pass
try:
    libgtk3.gdk_window_set_user_data.restype = None
    libgtk3.gdk_window_set_user_data.argtypes = [_GdkWindow,gpointer]
except:
   pass
try:
    libgtk3.gdk_window_is_shaped.restype = gboolean
    libgtk3.gdk_window_is_shaped.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_override_redirect.restype = None
    libgtk3.gdk_window_set_override_redirect.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_set_support_multidevice.restype = None
    libgtk3.gdk_window_set_support_multidevice.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_withdraw.restype = None
    libgtk3.gdk_window_withdraw.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_begin_paint_rect.restype = None
    libgtk3.gdk_window_begin_paint_rect.argtypes = [_GdkWindow,_GdkRectangle]
except:
   pass
try:
    libgtk3.gdk_window_register_dnd.restype = None
    libgtk3.gdk_window_register_dnd.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_begin_resize_drag.restype = None
    libgtk3.gdk_window_begin_resize_drag.argtypes = [_GdkWindow,GdkWindowEdge,gint,gint,gint,guint32]
except:
   pass
try:
    libgtk3.gdk_window_set_accept_focus.restype = None
    libgtk3.gdk_window_set_accept_focus.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_get_support_multidevice.restype = gboolean
    libgtk3.gdk_window_get_support_multidevice.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_move_region.restype = None
    libgtk3.gdk_window_move_region.argtypes = [_GdkWindow,_cairo_region_t,gint,gint]
except:
   pass
try:
    libgtk3.gdk_window_get_device_events.restype = GdkEventMask
    libgtk3.gdk_window_get_device_events.argtypes = [_GdkWindow,_GdkDevice]
except:
   pass
try:
    libgtk3.gdk_window_set_focus_on_map.restype = None
    libgtk3.gdk_window_set_focus_on_map.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_set_icon_name.restype = None
    libgtk3.gdk_window_set_icon_name.argtypes = [_GdkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gdk_window_is_viewable.restype = gboolean
    libgtk3.gdk_window_is_viewable.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_events.restype = GdkEventMask
    libgtk3.gdk_window_get_events.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_accept_focus.restype = gboolean
    libgtk3.gdk_window_get_accept_focus.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_transient_for.restype = None
    libgtk3.gdk_window_set_transient_for.argtypes = [_GdkWindow,_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_destroy.restype = None
    libgtk3.gdk_window_destroy.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_focus_on_map.restype = gboolean
    libgtk3.gdk_window_get_focus_on_map.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_resize.restype = None
    libgtk3.gdk_window_resize.argtypes = [_GdkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gdk_window_get_device_cursor.restype = _GdkCursor
    libgtk3.gdk_window_get_device_cursor.argtypes = [_GdkWindow,_GdkDevice]
except:
   pass
try:
    libgtk3.gdk_window_move_resize.restype = None
    libgtk3.gdk_window_move_resize.argtypes = [_GdkWindow,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gdk_window_set_modal_hint.restype = None
    libgtk3.gdk_window_set_modal_hint.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_get_state.restype = GdkWindowState
    libgtk3.gdk_window_get_state.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_invalidate_maybe_recurse.restype = None
    libgtk3.gdk_window_invalidate_maybe_recurse.argtypes = [_GdkWindow,_cairo_region_t,GdkWindowChildFunc,gpointer]
except:
   pass
try:
    libgtk3.gdk_window_get_composited.restype = gboolean
    libgtk3.gdk_window_get_composited.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_end_paint.restype = None
    libgtk3.gdk_window_end_paint.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_height.restype = int
    libgtk3.gdk_window_get_height.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_move.restype = None
    libgtk3.gdk_window_move.argtypes = [_GdkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gdk_window_configure_finished.restype = None
    libgtk3.gdk_window_configure_finished.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_visual.restype = _GdkVisual
    libgtk3.gdk_window_get_visual.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_maximize.restype = None
    libgtk3.gdk_window_maximize.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_root_origin.restype = None
    libgtk3.gdk_window_get_root_origin.argtypes = [_GdkWindow,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gdk_window_set_skip_pager_hint.restype = None
    libgtk3.gdk_window_set_skip_pager_hint.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_begin_move_drag.restype = None
    libgtk3.gdk_window_begin_move_drag.argtypes = [_GdkWindow,gint,gint,gint,guint32]
except:
   pass
try:
    libgtk3.gdk_window_peek_children.restype = _GList
    libgtk3.gdk_window_peek_children.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_beep.restype = None
    libgtk3.gdk_window_beep.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_cursor.restype = None
    libgtk3.gdk_window_set_cursor.argtypes = [_GdkWindow,_GdkCursor]
except:
   pass
try:
    libgtk3.gdk_window_unfullscreen.restype = None
    libgtk3.gdk_window_unfullscreen.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_freeze_updates.restype = None
    libgtk3.gdk_window_freeze_updates.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_children.restype = _GList
    libgtk3.gdk_window_get_children.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_remove_filter.restype = None
    libgtk3.gdk_window_remove_filter.argtypes = [_GdkWindow,GdkFilterFunc,gpointer]
except:
   pass
try:
    libgtk3.gdk_window_begin_move_drag_for_device.restype = None
    libgtk3.gdk_window_begin_move_drag_for_device.argtypes = [_GdkWindow,_GdkDevice,gint,gint,gint,guint32]
except:
   pass
try:
    libgtk3.gdk_window_get_pointer.restype = _GdkWindow
    libgtk3.gdk_window_get_pointer.argtypes = [_GdkWindow,POINTER(gint),POINTER(gint),POINTER(GdkModifierType)]
except:
   pass
try:
    libgtk3.gdk_window_get_decorations.restype = gboolean
    libgtk3.gdk_window_get_decorations.argtypes = [_GdkWindow,POINTER(GdkWMDecoration)]
except:
   pass
try:
    libgtk3.gdk_window_set_skip_taskbar_hint.restype = None
    libgtk3.gdk_window_set_skip_taskbar_hint.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_invalidate_rect.restype = None
    libgtk3.gdk_window_invalidate_rect.argtypes = [_GdkWindow,_GdkRectangle,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_set_geometry_hints.restype = None
    libgtk3.gdk_window_set_geometry_hints.argtypes = [_GdkWindow,_GdkGeometry,GdkWindowHints]
except:
   pass
try:
    libgtk3.gdk_window_set_group.restype = None
    libgtk3.gdk_window_set_group.argtypes = [_GdkWindow,_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_hide.restype = None
    libgtk3.gdk_window_hide.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_reparent.restype = None
    libgtk3.gdk_window_reparent.argtypes = [_GdkWindow,_GdkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gdk_window_get_modal_hint.restype = gboolean
    libgtk3.gdk_window_get_modal_hint.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_static_gravities.restype = gboolean
    libgtk3.gdk_window_set_static_gravities.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_deiconify.restype = None
    libgtk3.gdk_window_deiconify.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_input_shape_combine_region.restype = None
    libgtk3.gdk_window_input_shape_combine_region.argtypes = [_GdkWindow,_cairo_region_t,gint,gint]
except:
   pass
try:
    libgtk3.gdk_window_ensure_native.restype = gboolean
    libgtk3.gdk_window_ensure_native.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_root_coords.restype = None
    libgtk3.gdk_window_get_root_coords.argtypes = [_GdkWindow,gint,gint,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gdk_window_set_title.restype = None
    libgtk3.gdk_window_set_title.argtypes = [_GdkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gdk_window_get_origin.restype = gint
    libgtk3.gdk_window_get_origin.argtypes = [_GdkWindow,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gdk_window_flush.restype = None
    libgtk3.gdk_window_flush.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_source_events.restype = GdkEventMask
    libgtk3.gdk_window_get_source_events.argtypes = [_GdkWindow,GdkInputSource]
except:
   pass
try:
    libgtk3.gdk_window_set_device_cursor.restype = None
    libgtk3.gdk_window_set_device_cursor.argtypes = [_GdkWindow,_GdkDevice,_GdkCursor]
except:
   pass
try:
    libgtk3.gdk_window_add_filter.restype = None
    libgtk3.gdk_window_add_filter.argtypes = [_GdkWindow,GdkFilterFunc,gpointer]
except:
   pass
try:
    libgtk3.gdk_window_set_opacity.restype = None
    libgtk3.gdk_window_set_opacity.argtypes = [_GdkWindow,gdouble]
except:
   pass
try:
    libgtk3.gdk_window_fullscreen.restype = None
    libgtk3.gdk_window_fullscreen.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_startup_id.restype = None
    libgtk3.gdk_window_set_startup_id.argtypes = [_GdkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gdk_window_get_window_type.restype = GdkWindowType
    libgtk3.gdk_window_get_window_type.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_coords_to_parent.restype = None
    libgtk3.gdk_window_coords_to_parent.argtypes = [_GdkWindow,gdouble,gdouble,POINTER(gdouble),POINTER(gdouble)]
except:
   pass
try:
    libgtk3.gdk_window_coords_from_parent.restype = None
    libgtk3.gdk_window_coords_from_parent.argtypes = [_GdkWindow,gdouble,gdouble,POINTER(gdouble),POINTER(gdouble)]
except:
   pass
try:
    libgtk3.gdk_window_get_user_data.restype = None
    libgtk3.gdk_window_get_user_data.argtypes = [_GdkWindow,POINTER(gpointer)]
except:
   pass
try:
    libgtk3.gdk_window_set_keep_below.restype = None
    libgtk3.gdk_window_set_keep_below.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_get_effective_toplevel.restype = _GdkWindow
    libgtk3.gdk_window_get_effective_toplevel.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_offscreen_window_get_embedder.restype = _GdkWindow
    libgtk3.gdk_offscreen_window_get_embedder.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_toplevel.restype = _GdkWindow
    libgtk3.gdk_window_get_toplevel.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_begin_resize_drag_for_device.restype = None
    libgtk3.gdk_window_begin_resize_drag_for_device.argtypes = [_GdkWindow,GdkWindowEdge,_GdkDevice,gint,gint,gint,guint32]
except:
   pass
try:
    libgtk3.gdk_window_stick.restype = None
    libgtk3.gdk_window_stick.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_scroll.restype = None
    libgtk3.gdk_window_scroll.argtypes = [_GdkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gdk_offscreen_window_set_embedder.restype = None
    libgtk3.gdk_offscreen_window_set_embedder.argtypes = [_GdkWindow,_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_unmaximize.restype = None
    libgtk3.gdk_window_unmaximize.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_background.restype = None
    libgtk3.gdk_window_set_background.argtypes = [_GdkWindow,_GdkColor]
except:
   pass
try:
    libgtk3.gdk_window_process_updates.restype = None
    libgtk3.gdk_window_process_updates.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_focus.restype = None
    libgtk3.gdk_window_focus.argtypes = [_GdkWindow,guint32]
except:
   pass
try:
    libgtk3.gdk_window_raise.restype = None
    libgtk3.gdk_window_raise.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_display.restype = _GdkDisplay
    libgtk3.gdk_window_get_display.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_frame_extents.restype = None
    libgtk3.gdk_window_get_frame_extents.argtypes = [_GdkWindow,_GdkRectangle]
except:
   pass
try:
    libgtk3.gdk_window_set_events.restype = None
    libgtk3.gdk_window_set_events.argtypes = [_GdkWindow,GdkEventMask]
except:
   pass
try:
    libgtk3.gdk_window_set_keep_above.restype = None
    libgtk3.gdk_window_set_keep_above.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_set_role.restype = None
    libgtk3.gdk_window_set_role.argtypes = [_GdkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gdk_window_set_background_pattern.restype = None
    libgtk3.gdk_window_set_background_pattern.argtypes = [_GdkWindow,_cairo_pattern_t]
except:
   pass
try:
    libgtk3.gdk_window_set_debug_updates.restype = None
    libgtk3.gdk_window_set_debug_updates.argtypes = [_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_get_cursor.restype = _GdkCursor
    libgtk3.gdk_window_get_cursor.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_is_visible.restype = gboolean
    libgtk3.gdk_window_is_visible.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_merge_child_shapes.restype = None
    libgtk3.gdk_window_merge_child_shapes.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_geometry_changed.restype = None
    libgtk3.gdk_window_geometry_changed.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_type_hint.restype = GdkWindowTypeHint
    libgtk3.gdk_window_get_type_hint.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_child_input_shapes.restype = None
    libgtk3.gdk_window_set_child_input_shapes.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_device_events.restype = None
    libgtk3.gdk_window_set_device_events.argtypes = [_GdkWindow,_GdkDevice,GdkEventMask]
except:
   pass
try:
    libgtk3.gdk_window_restack.restype = None
    libgtk3.gdk_window_restack.argtypes = [_GdkWindow,_GdkWindow,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_merge_child_input_shapes.restype = None
    libgtk3.gdk_window_merge_child_input_shapes.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_width.restype = int
    libgtk3.gdk_window_get_width.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_unstick.restype = None
    libgtk3.gdk_window_unstick.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_show_unraised.restype = None
    libgtk3.gdk_window_show_unraised.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_is_destroyed.restype = gboolean
    libgtk3.gdk_window_is_destroyed.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_effective_parent.restype = _GdkWindow
    libgtk3.gdk_window_get_effective_parent.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_device_position.restype = _GdkWindow
    libgtk3.gdk_window_get_device_position.argtypes = [_GdkWindow,_GdkDevice,POINTER(gint),POINTER(gint),POINTER(GdkModifierType)]
except:
   pass
try:
    libgtk3.gdk_window_get_group.restype = _GdkWindow
    libgtk3.gdk_window_get_group.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_get_position.restype = None
    libgtk3.gdk_window_get_position.argtypes = [_GdkWindow,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gdk_window_show.restype = None
    libgtk3.gdk_window_show.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_functions.restype = None
    libgtk3.gdk_window_set_functions.argtypes = [_GdkWindow,GdkWMFunction]
except:
   pass
try:
    libgtk3.gdk_window_begin_paint_region.restype = None
    libgtk3.gdk_window_begin_paint_region.argtypes = [_GdkWindow,_cairo_region_t]
except:
   pass
try:
    libgtk3.gdk_window_shape_combine_region.restype = None
    libgtk3.gdk_window_shape_combine_region.argtypes = [_GdkWindow,_cairo_region_t,gint,gint]
except:
   pass
try:
    libgtk3.gdk_window_thaw_updates.restype = None
    libgtk3.gdk_window_thaw_updates.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_invalidate_region.restype = None
    libgtk3.gdk_window_invalidate_region.argtypes = [_GdkWindow,_cairo_region_t,gboolean]
except:
   pass
try:
    libgtk3.gdk_window_get_parent.restype = _GdkWindow
    libgtk3.gdk_window_get_parent.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_child_shapes.restype = None
    libgtk3.gdk_window_set_child_shapes.argtypes = [_GdkWindow]
except:
   pass
try:
    libgtk3.gdk_window_set_type_hint.restype = None
    libgtk3.gdk_window_set_type_hint.argtypes = [_GdkWindow,GdkWindowTypeHint]
except:
   pass
try:
    libgtk3.gdk_window_at_pointer.restype = _GdkWindow
    libgtk3.gdk_window_at_pointer.argtypes = [POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gdk_window_process_all_updates.restype = None
    libgtk3.gdk_window_process_all_updates.argtypes = []
except:
   pass
try:
    libgtk3.gdk_get_default_root_window.restype = _GdkWindow
    libgtk3.gdk_get_default_root_window.argtypes = []
except:
   pass
from . import gobject__GObject
class GdkWindow( gobject__GObject.GObject):
    """Class GdkWindow Constructors"""
    def __init__( self, attributes_mask,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gdk_window_new.restype = POINTER(c_void_p)
            
            libgtk3.gdk_window_new.argtypes = [gint]
            self._object = libgtk3.gdk_window_new(attributes_mask, )

    """Methods"""
    def get_geometry(  self, x, y, width, height, ):

        
        libgtk3.gdk_window_get_geometry( self._object,x,y,width,height )

    def set_background_rgba(  self, rgba, ):
        if rgba: rgba = rgba._object
        else: rgba = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_background_rgba( self._object,rgba )

    def get_screen(  self, ):

        from .gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gdk_window_get_screen( self._object ) or POINTER(c_void_p)())

    def has_native(  self, ):

        
        return libgtk3.gdk_window_has_native( self._object )

    def constrain_size(  self, geometry, flags, width, height, new_width, new_height, ):
        if geometry: geometry = geometry._object
        else: geometry = POINTER(c_void_p)()

        
        libgtk3.gdk_window_constrain_size( self._object,geometry,flags,width,height,new_width,new_height )

    def set_urgency_hint(  self, urgent, ):

        
        libgtk3.gdk_window_set_urgency_hint( self._object,urgent )

    def is_input_only(  self, ):

        
        return libgtk3.gdk_window_is_input_only( self._object )

    def lower(  self, ):

        
        libgtk3.gdk_window_lower( self._object )

    def set_composited(  self, composited, ):

        
        libgtk3.gdk_window_set_composited( self._object,composited )

    def set_icon_list(  self, pixbufs, ):
        if pixbufs: pixbufs = pixbufs._object
        else: pixbufs = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_icon_list( self._object,pixbufs )

    def enable_synchronized_configure(  self, ):

        
        libgtk3.gdk_window_enable_synchronized_configure( self._object )

    def iconify(  self, ):

        
        libgtk3.gdk_window_iconify( self._object )

    def set_decorations(  self, decorations, ):

        
        libgtk3.gdk_window_set_decorations( self._object,decorations )

    def set_source_events(  self, source, event_mask, ):

        
        libgtk3.gdk_window_set_source_events( self._object,source,event_mask )

    def set_user_data(  self, user_data, ):

        
        libgtk3.gdk_window_set_user_data( self._object,user_data )

    def is_shaped(  self, ):

        
        return libgtk3.gdk_window_is_shaped( self._object )

    def set_override_redirect(  self, override_redirect, ):

        
        libgtk3.gdk_window_set_override_redirect( self._object,override_redirect )

    def set_support_multidevice(  self, support_multidevice, ):

        
        libgtk3.gdk_window_set_support_multidevice( self._object,support_multidevice )

    def withdraw(  self, ):

        
        libgtk3.gdk_window_withdraw( self._object )

    def begin_paint_rect(  self, rectangle, ):
        if rectangle: rectangle = rectangle._object
        else: rectangle = POINTER(c_void_p)()

        
        libgtk3.gdk_window_begin_paint_rect( self._object,rectangle )

    def register_dnd(  self, ):

        
        libgtk3.gdk_window_register_dnd( self._object )

    def begin_resize_drag(  self, edge, button, root_x, root_y, timestamp, ):
        if edge: edge = edge._object
        else: edge = POINTER(c_void_p)()

        
        libgtk3.gdk_window_begin_resize_drag( self._object,edge,button,root_x,root_y,timestamp )

    def set_accept_focus(  self, accept_focus, ):

        
        libgtk3.gdk_window_set_accept_focus( self._object,accept_focus )

    def get_support_multidevice(  self, ):

        
        return libgtk3.gdk_window_get_support_multidevice( self._object )

    def move_region(  self, region, dx, dy, ):
        if region: region = region._object
        else: region = POINTER(c_void_p)()

        
        libgtk3.gdk_window_move_region( self._object,region,dx,dy )

    def get_device_events(  self, device, ):
        if device: device = device._object
        else: device = POINTER(c_void_p)()

        
        return libgtk3.gdk_window_get_device_events( self._object,device )

    def set_focus_on_map(  self, focus_on_map, ):

        
        libgtk3.gdk_window_set_focus_on_map( self._object,focus_on_map )

    def set_icon_name(  self, name, ):

        
        libgtk3.gdk_window_set_icon_name( self._object,name )

    def is_viewable(  self, ):

        
        return libgtk3.gdk_window_is_viewable( self._object )

    def get_events(  self, ):

        
        return libgtk3.gdk_window_get_events( self._object )

    def get_accept_focus(  self, ):

        
        return libgtk3.gdk_window_get_accept_focus( self._object )

    def set_transient_for(  self, parent, ):
        if parent: parent = parent._object
        else: parent = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_transient_for( self._object,parent )

    def destroy(  self, ):

        
        libgtk3.gdk_window_destroy( self._object )

    def get_focus_on_map(  self, ):

        
        return libgtk3.gdk_window_get_focus_on_map( self._object )

    def resize(  self, width, height, ):

        
        libgtk3.gdk_window_resize( self._object,width,height )

    def get_device_cursor(  self, device, ):
        if device: device = device._object
        else: device = POINTER(c_void_p)()

        from .gobject import GdkCursor
        return GdkCursor(None,None, obj=libgtk3.gdk_window_get_device_cursor( self._object,device ) or POINTER(c_void_p)())

    def move_resize(  self, x, y, width, height, ):

        
        libgtk3.gdk_window_move_resize( self._object,x,y,width,height )

    def set_modal_hint(  self, modal, ):

        
        libgtk3.gdk_window_set_modal_hint( self._object,modal )

    def get_state(  self, ):

        
        return libgtk3.gdk_window_get_state( self._object )

    def invalidate_maybe_recurse(  self, region, child_func, user_data, ):
        if region: region = region._object
        else: region = POINTER(c_void_p)()
        if child_func: child_func = child_func._object
        else: child_func = POINTER(c_void_p)()

        
        libgtk3.gdk_window_invalidate_maybe_recurse( self._object,region,child_func,user_data )

    def get_composited(  self, ):

        
        return libgtk3.gdk_window_get_composited( self._object )

    def end_paint(  self, ):

        
        libgtk3.gdk_window_end_paint( self._object )

    def get_height(  self, ):

        
        return libgtk3.gdk_window_get_height( self._object )

    def move(  self, x, y, ):

        
        libgtk3.gdk_window_move( self._object,x,y )

    def configure_finished(  self, ):

        
        libgtk3.gdk_window_configure_finished( self._object )

    def get_visual(  self, ):

        from .gobject import GdkVisual
        return GdkVisual( obj=libgtk3.gdk_window_get_visual( self._object ) or POINTER(c_void_p)())

    def maximize(  self, ):

        
        libgtk3.gdk_window_maximize( self._object )

    def get_root_origin(  self, x, y, ):

        
        libgtk3.gdk_window_get_root_origin( self._object,x,y )

    def set_skip_pager_hint(  self, skips_pager, ):

        
        libgtk3.gdk_window_set_skip_pager_hint( self._object,skips_pager )

    def begin_move_drag(  self, button, root_x, root_y, timestamp, ):

        
        libgtk3.gdk_window_begin_move_drag( self._object,button,root_x,root_y,timestamp )

    def peek_children(  self, ):

        from .gobject import GList
        return GList( obj=libgtk3.gdk_window_peek_children( self._object ) or POINTER(c_void_p)())

    def beep(  self, ):

        
        libgtk3.gdk_window_beep( self._object )

    def set_cursor(  self, cursor, ):
        if cursor: cursor = cursor._object
        else: cursor = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_cursor( self._object,cursor )

    def unfullscreen(  self, ):

        
        libgtk3.gdk_window_unfullscreen( self._object )

    def freeze_updates(  self, ):

        
        libgtk3.gdk_window_freeze_updates( self._object )

    def get_children(  self, ):

        from .gobject import GList
        return GList( obj=libgtk3.gdk_window_get_children( self._object ) or POINTER(c_void_p)())

    def remove_filter(  self, function, data, ):
        if function: function = function._object
        else: function = POINTER(c_void_p)()

        
        libgtk3.gdk_window_remove_filter( self._object,function,data )

    def begin_move_drag_for_device(  self, device, button, root_x, root_y, timestamp, ):
        if device: device = device._object
        else: device = POINTER(c_void_p)()

        
        libgtk3.gdk_window_begin_move_drag_for_device( self._object,device,button,root_x,root_y,timestamp )

    def get_pointer(  self, x, y, mask, ):

        from .gobject import GdkWindow
        return GdkWindow(None,None,None, obj=libgtk3.gdk_window_get_pointer( self._object,x,y,mask ) or POINTER(c_void_p)())

    def get_decorations(  self, decorations, ):

        
        return libgtk3.gdk_window_get_decorations( self._object,decorations )

    def set_skip_taskbar_hint(  self, skips_taskbar, ):

        
        libgtk3.gdk_window_set_skip_taskbar_hint( self._object,skips_taskbar )

    def invalidate_rect(  self, rect, invalidate_children, ):
        if rect: rect = rect._object
        else: rect = POINTER(c_void_p)()

        
        libgtk3.gdk_window_invalidate_rect( self._object,rect,invalidate_children )

    def set_geometry_hints(  self, geometry, geom_mask, ):
        if geometry: geometry = geometry._object
        else: geometry = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_geometry_hints( self._object,geometry,geom_mask )

    def set_group(  self, leader, ):
        if leader: leader = leader._object
        else: leader = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_group( self._object,leader )

    def hide(  self, ):

        
        libgtk3.gdk_window_hide( self._object )

    def reparent(  self, new_parent, x, y, ):
        if new_parent: new_parent = new_parent._object
        else: new_parent = POINTER(c_void_p)()

        
        libgtk3.gdk_window_reparent( self._object,new_parent,x,y )

    def get_modal_hint(  self, ):

        
        return libgtk3.gdk_window_get_modal_hint( self._object )

    def set_static_gravities(  self, use_static, ):

        
        return libgtk3.gdk_window_set_static_gravities( self._object,use_static )

    def deiconify(  self, ):

        
        libgtk3.gdk_window_deiconify( self._object )

    def input_shape_combine_region(  self, shape_region, offset_x, offset_y, ):
        if shape_region: shape_region = shape_region._object
        else: shape_region = POINTER(c_void_p)()

        
        libgtk3.gdk_window_input_shape_combine_region( self._object,shape_region,offset_x,offset_y )

    def ensure_native(  self, ):

        
        return libgtk3.gdk_window_ensure_native( self._object )

    def get_root_coords(  self, x, y, root_x, root_y, ):

        
        libgtk3.gdk_window_get_root_coords( self._object,x,y,root_x,root_y )

    def set_title(  self, title, ):

        
        libgtk3.gdk_window_set_title( self._object,title )

    def get_origin(  self, x, y, ):

        
        return libgtk3.gdk_window_get_origin( self._object,x,y )

    def flush(  self, ):

        
        libgtk3.gdk_window_flush( self._object )

    def get_source_events(  self, source, ):

        
        return libgtk3.gdk_window_get_source_events( self._object,source )

    def set_device_cursor(  self, device, cursor, ):
        if device: device = device._object
        else: device = POINTER(c_void_p)()
        if cursor: cursor = cursor._object
        else: cursor = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_device_cursor( self._object,device,cursor )

    def add_filter(  self, function, data, ):
        if function: function = function._object
        else: function = POINTER(c_void_p)()

        
        libgtk3.gdk_window_add_filter( self._object,function,data )

    def set_opacity(  self, opacity, ):

        
        libgtk3.gdk_window_set_opacity( self._object,opacity )

    def fullscreen(  self, ):

        
        libgtk3.gdk_window_fullscreen( self._object )

    def set_startup_id(  self, startup_id, ):

        
        libgtk3.gdk_window_set_startup_id( self._object,startup_id )

    def get_window_type(  self, ):

        
        return libgtk3.gdk_window_get_window_type( self._object )

    def coords_to_parent(  self, x, y, parent_x, parent_y, ):

        
        libgtk3.gdk_window_coords_to_parent( self._object,x,y,parent_x,parent_y )

    def coords_from_parent(  self, parent_x, parent_y, x, y, ):

        
        libgtk3.gdk_window_coords_from_parent( self._object,parent_x,parent_y,x,y )

    def get_user_data(  self, data, ):

        
        libgtk3.gdk_window_get_user_data( self._object,data )

    def set_keep_below(  self, setting, ):

        
        libgtk3.gdk_window_set_keep_below( self._object,setting )

    def get_effective_toplevel(  self, ):

        from .gobject import GdkWindow
        return GdkWindow( obj=libgtk3.gdk_window_get_effective_toplevel( self._object ) or POINTER(c_void_p)())

    def gdk_offscreen_window_get_embedder(  self, ):

        from .gobject import GdkWindow
        return GdkWindow( obj=libgtk3.gdk_offscreen_window_get_embedder( self._object ) or POINTER(c_void_p)())

    def get_toplevel(  self, ):

        from .gobject import GdkWindow
        return GdkWindow( obj=libgtk3.gdk_window_get_toplevel( self._object ) or POINTER(c_void_p)())

    def begin_resize_drag_for_device(  self, edge, device, button, root_x, root_y, timestamp, ):
        if edge: edge = edge._object
        else: edge = POINTER(c_void_p)()
        if device: device = device._object
        else: device = POINTER(c_void_p)()

        
        libgtk3.gdk_window_begin_resize_drag_for_device( self._object,edge,device,button,root_x,root_y,timestamp )

    def stick(  self, ):

        
        libgtk3.gdk_window_stick( self._object )

    def scroll(  self, dx, dy, ):

        
        libgtk3.gdk_window_scroll( self._object,dx,dy )

    def gdk_offscreen_window_set_embedder(  self, embedder, ):
        if embedder: embedder = embedder._object
        else: embedder = POINTER(c_void_p)()

        
        libgtk3.gdk_offscreen_window_set_embedder( self._object,embedder )

    def unmaximize(  self, ):

        
        libgtk3.gdk_window_unmaximize( self._object )

    def set_background(  self, color, ):
        if color: color = color._object
        else: color = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_background( self._object,color )

    def process_updates(  self, update_children, ):

        
        libgtk3.gdk_window_process_updates( self._object,update_children )

    def focus(  self, timestamp, ):

        
        libgtk3.gdk_window_focus( self._object,timestamp )

    def py_raise(  self, ):

        
        libgtk3.gdk_window_raise( self._object )

    def get_display(  self, ):

        from .gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gdk_window_get_display( self._object ) or POINTER(c_void_p)())

    def get_frame_extents(  self, rect, ):
        if rect: rect = rect._object
        else: rect = POINTER(c_void_p)()

        
        libgtk3.gdk_window_get_frame_extents( self._object,rect )

    def set_events(  self, event_mask, ):

        
        libgtk3.gdk_window_set_events( self._object,event_mask )

    def set_keep_above(  self, setting, ):

        
        libgtk3.gdk_window_set_keep_above( self._object,setting )

    def set_role(  self, role, ):

        
        libgtk3.gdk_window_set_role( self._object,role )

    def set_background_pattern(  self, pattern, ):
        if pattern: pattern = pattern._object
        else: pattern = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_background_pattern( self._object,pattern )

    def set_debug_updates(  self, setting, ):

        
        libgtk3.gdk_window_set_debug_updates( self._object,setting )

    def get_cursor(  self, ):

        from .gobject import GdkCursor
        return GdkCursor(None, obj=libgtk3.gdk_window_get_cursor( self._object ) or POINTER(c_void_p)())

    def is_visible(  self, ):

        
        return libgtk3.gdk_window_is_visible( self._object )

    def merge_child_shapes(  self, ):

        
        libgtk3.gdk_window_merge_child_shapes( self._object )

    def geometry_changed(  self, ):

        
        libgtk3.gdk_window_geometry_changed( self._object )

    def get_type_hint(  self, ):

        
        return libgtk3.gdk_window_get_type_hint( self._object )

    def set_child_input_shapes(  self, ):

        
        libgtk3.gdk_window_set_child_input_shapes( self._object )

    def set_device_events(  self, device, event_mask, ):
        if device: device = device._object
        else: device = POINTER(c_void_p)()

        
        libgtk3.gdk_window_set_device_events( self._object,device,event_mask )

    def restack(  self, sibling, above, ):
        if sibling: sibling = sibling._object
        else: sibling = POINTER(c_void_p)()

        
        libgtk3.gdk_window_restack( self._object,sibling,above )

    def merge_child_input_shapes(  self, ):

        
        libgtk3.gdk_window_merge_child_input_shapes( self._object )

    def get_width(  self, ):

        
        return libgtk3.gdk_window_get_width( self._object )

    def unstick(  self, ):

        
        libgtk3.gdk_window_unstick( self._object )

    def show_unraised(  self, ):

        
        libgtk3.gdk_window_show_unraised( self._object )

    def is_destroyed(  self, ):

        
        return libgtk3.gdk_window_is_destroyed( self._object )

    def get_effective_parent(  self, ):

        from .gobject import GdkWindow
        return GdkWindow( obj=libgtk3.gdk_window_get_effective_parent( self._object ) or POINTER(c_void_p)())

    def get_device_position(  self, device, x, y, mask, ):
        if device: device = device._object
        else: device = POINTER(c_void_p)()

        from .gobject import GdkWindow
        return GdkWindow(None,None,None,None, obj=libgtk3.gdk_window_get_device_position( self._object,device,x,y,mask ) or POINTER(c_void_p)())

    def get_group(  self, ):

        from .gobject import GdkWindow
        return GdkWindow( obj=libgtk3.gdk_window_get_group( self._object ) or POINTER(c_void_p)())

    def get_position(  self, x, y, ):

        
        libgtk3.gdk_window_get_position( self._object,x,y )

    def show(  self, ):

        
        libgtk3.gdk_window_show( self._object )

    def set_functions(  self, functions, ):

        
        libgtk3.gdk_window_set_functions( self._object,functions )

    def begin_paint_region(  self, region, ):
        if region: region = region._object
        else: region = POINTER(c_void_p)()

        
        libgtk3.gdk_window_begin_paint_region( self._object,region )

    def shape_combine_region(  self, shape_region, offset_x, offset_y, ):
        if shape_region: shape_region = shape_region._object
        else: shape_region = POINTER(c_void_p)()

        
        libgtk3.gdk_window_shape_combine_region( self._object,shape_region,offset_x,offset_y )

    def thaw_updates(  self, ):

        
        libgtk3.gdk_window_thaw_updates( self._object )

    def invalidate_region(  self, region, invalidate_children, ):
        if region: region = region._object
        else: region = POINTER(c_void_p)()

        
        libgtk3.gdk_window_invalidate_region( self._object,region,invalidate_children )

    def get_parent(  self, ):

        from .gobject import GdkWindow
        return GdkWindow( obj=libgtk3.gdk_window_get_parent( self._object ) or POINTER(c_void_p)())

    def set_child_shapes(  self, ):

        
        libgtk3.gdk_window_set_child_shapes( self._object )

    def set_type_hint(  self, hint, ):

        
        libgtk3.gdk_window_set_type_hint( self._object,hint )

    @staticmethod
    def at_pointer( win_x, win_y,):
        from .gobject import GdkWindow
        return GdkWindow(None, obj=    libgtk3.gdk_window_at_pointer(win_x, win_y, )
 or POINTER(c_void_p)())
    @staticmethod
    def process_all_updates():
        
            libgtk3.gdk_window_process_all_updates()

    @staticmethod
    def gdk_get_default_root_window():
        from .gobject import GdkWindow
        return GdkWindow(None, obj=    libgtk3.gdk_get_default_root_window()
 or POINTER(c_void_p)())
