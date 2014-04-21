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
_GValue = POINTER(c_void_p)
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
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int

try:
    libgtk3.gtk_window_activate_focus.restype = gboolean
    libgtk3.gtk_window_activate_focus.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_skip_pager_hint.restype = None
    libgtk3.gtk_window_set_skip_pager_hint.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_set_geometry_hints.restype = None
    libgtk3.gtk_window_set_geometry_hints.argtypes = [_GtkWindow,_GtkWidget,_GdkGeometry,GdkWindowHints]
except:
   pass
try:
    libgtk3.gtk_window_get_group.restype = _GtkWindowGroup
    libgtk3.gtk_window_get_group.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_has_resize_grip.restype = None
    libgtk3.gtk_window_set_has_resize_grip.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_get_skip_pager_hint.restype = gboolean
    libgtk3.gtk_window_get_skip_pager_hint.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_maximize.restype = None
    libgtk3.gtk_window_maximize.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_icon_from_file.restype = gboolean
    libgtk3.gtk_window_set_icon_from_file.argtypes = [_GtkWindow,Asciifier,_GError]
except:
   pass
try:
    libgtk3.gtk_window_get_urgency_hint.restype = gboolean
    libgtk3.gtk_window_get_urgency_hint.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_propagate_key_event.restype = gboolean
    libgtk3.gtk_window_propagate_key_event.argtypes = [_GtkWindow,_GdkEventKey]
except:
   pass
try:
    libgtk3.gtk_window_get_opacity.restype = gdouble
    libgtk3.gtk_window_get_opacity.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_resize_grip_area.restype = gboolean
    libgtk3.gtk_window_get_resize_grip_area.argtypes = [_GtkWindow,_GdkRectangle]
except:
   pass
try:
    libgtk3.gtk_window_unmaximize.restype = None
    libgtk3.gtk_window_unmaximize.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_screen.restype = None
    libgtk3.gtk_window_set_screen.argtypes = [_GtkWindow,_GdkScreen]
except:
   pass
try:
    libgtk3.gtk_window_get_position.restype = None
    libgtk3.gtk_window_get_position.argtypes = [_GtkWindow,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gtk_window_set_default_size.restype = None
    libgtk3.gtk_window_set_default_size.argtypes = [_GtkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gtk_window_is_active.restype = gboolean
    libgtk3.gtk_window_is_active.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_focus_on_map.restype = None
    libgtk3.gtk_window_set_focus_on_map.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_move.restype = None
    libgtk3.gtk_window_move.argtypes = [_GtkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gtk_window_set_position.restype = None
    libgtk3.gtk_window_set_position.argtypes = [_GtkWindow,GtkWindowPosition]
except:
   pass
try:
    libgtk3.gtk_window_set_destroy_with_parent.restype = None
    libgtk3.gtk_window_set_destroy_with_parent.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_resize_to_geometry.restype = None
    libgtk3.gtk_window_resize_to_geometry.argtypes = [_GtkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gtk_window_set_focus_visible.restype = None
    libgtk3.gtk_window_set_focus_visible.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_set_mnemonics_visible.restype = None
    libgtk3.gtk_window_set_mnemonics_visible.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_has_toplevel_focus.restype = gboolean
    libgtk3.gtk_window_has_toplevel_focus.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_stick.restype = None
    libgtk3.gtk_window_stick.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_title.restype = c_char_p
    libgtk3.gtk_window_get_title.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_resizable.restype = None
    libgtk3.gtk_window_set_resizable.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_get_size.restype = None
    libgtk3.gtk_window_get_size.argtypes = [_GtkWindow,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gtk_window_set_default.restype = None
    libgtk3.gtk_window_set_default.argtypes = [_GtkWindow,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_window_get_deletable.restype = gboolean
    libgtk3.gtk_window_get_deletable.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_begin_move_drag.restype = None
    libgtk3.gtk_window_begin_move_drag.argtypes = [_GtkWindow,gint,gint,gint,guint32]
except:
   pass
try:
    libgtk3.gtk_window_get_gravity.restype = GdkGravity
    libgtk3.gtk_window_get_gravity.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_icon.restype = None
    libgtk3.gtk_window_set_icon.argtypes = [_GtkWindow,_GdkPixbuf]
except:
   pass
try:
    libgtk3.gtk_window_mnemonic_activate.restype = gboolean
    libgtk3.gtk_window_mnemonic_activate.argtypes = [_GtkWindow,guint,GdkModifierType]
except:
   pass
try:
    libgtk3.gtk_window_get_skip_taskbar_hint.restype = gboolean
    libgtk3.gtk_window_get_skip_taskbar_hint.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_focus_visible.restype = gboolean
    libgtk3.gtk_window_get_focus_visible.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_present.restype = None
    libgtk3.gtk_window_present.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_unfullscreen.restype = None
    libgtk3.gtk_window_unfullscreen.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_keep_below.restype = None
    libgtk3.gtk_window_set_keep_below.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_resize_grip_is_visible.restype = gboolean
    libgtk3.gtk_window_resize_grip_is_visible.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_deiconify.restype = None
    libgtk3.gtk_window_deiconify.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_resize.restype = None
    libgtk3.gtk_window_resize.argtypes = [_GtkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gtk_window_get_role.restype = c_char_p
    libgtk3.gtk_window_get_role.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_focus.restype = _GtkWidget
    libgtk3.gtk_window_get_focus.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_auto_startup_notification.restype = None
    libgtk3.gtk_window_set_auto_startup_notification.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_get_mnemonics_visible.restype = gboolean
    libgtk3.gtk_window_get_mnemonics_visible.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_mnemonic_modifier.restype = GdkModifierType
    libgtk3.gtk_window_get_mnemonic_modifier.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_application.restype = None
    libgtk3.gtk_window_set_application.argtypes = [_GtkWindow,_GtkApplication]
except:
   pass
try:
    libgtk3.gtk_window_set_default_icon.restype = None
    libgtk3.gtk_window_set_default_icon.argtypes = [_GtkWindow,_GdkPixbuf]
except:
   pass
try:
    libgtk3.gtk_window_set_default_geometry.restype = None
    libgtk3.gtk_window_set_default_geometry.argtypes = [_GtkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gtk_window_get_icon.restype = _GdkPixbuf
    libgtk3.gtk_window_get_icon.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_role.restype = None
    libgtk3.gtk_window_set_role.argtypes = [_GtkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gtk_window_set_skip_taskbar_hint.restype = None
    libgtk3.gtk_window_set_skip_taskbar_hint.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_activate_default.restype = gboolean
    libgtk3.gtk_window_activate_default.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_has_group.restype = gboolean
    libgtk3.gtk_window_has_group.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_modal.restype = gboolean
    libgtk3.gtk_window_get_modal.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_title.restype = None
    libgtk3.gtk_window_set_title.argtypes = [_GtkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gtk_window_set_transient_for.restype = None
    libgtk3.gtk_window_set_transient_for.argtypes = [_GtkWindow,_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_icon_list.restype = None
    libgtk3.gtk_window_set_icon_list.argtypes = [_GtkWindow,_GList]
except:
   pass
try:
    libgtk3.gtk_window_set_icon_name.restype = None
    libgtk3.gtk_window_set_icon_name.argtypes = [_GtkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gtk_window_set_urgency_hint.restype = None
    libgtk3.gtk_window_set_urgency_hint.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_get_icon_name.restype = c_char_p
    libgtk3.gtk_window_get_icon_name.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_opacity.restype = None
    libgtk3.gtk_window_set_opacity.argtypes = [_GtkWindow,gdouble]
except:
   pass
try:
    libgtk3.gtk_window_iconify.restype = None
    libgtk3.gtk_window_iconify.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_transient_for.restype = _GtkWindow
    libgtk3.gtk_window_get_transient_for.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_window_type.restype = GtkWindowType
    libgtk3.gtk_window_get_window_type.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_remove_mnemonic.restype = None
    libgtk3.gtk_window_remove_mnemonic.argtypes = [_GtkWindow,guint,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_window_get_resizable.restype = gboolean
    libgtk3.gtk_window_get_resizable.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_decorated.restype = gboolean
    libgtk3.gtk_window_get_decorated.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_parse_geometry.restype = gboolean
    libgtk3.gtk_window_parse_geometry.argtypes = [_GtkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gtk_window_get_application.restype = _GtkApplication
    libgtk3.gtk_window_get_application.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_default_widget.restype = _GtkWidget
    libgtk3.gtk_window_get_default_widget.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_mnemonic_modifier.restype = None
    libgtk3.gtk_window_set_mnemonic_modifier.argtypes = [_GtkWindow,GdkModifierType]
except:
   pass
try:
    libgtk3.gtk_window_set_startup_id.restype = None
    libgtk3.gtk_window_set_startup_id.argtypes = [_GtkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gtk_window_set_default_icon_list.restype = None
    libgtk3.gtk_window_set_default_icon_list.argtypes = [_GtkWindow,_GList]
except:
   pass
try:
    libgtk3.gtk_window_set_modal.restype = None
    libgtk3.gtk_window_set_modal.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_get_screen.restype = _GdkScreen
    libgtk3.gtk_window_get_screen.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_wmclass.restype = None
    libgtk3.gtk_window_set_wmclass.argtypes = [_GtkWindow,Asciifier,Asciifier]
except:
   pass
try:
    libgtk3.gtk_window_get_accept_focus.restype = gboolean
    libgtk3.gtk_window_get_accept_focus.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_focus_on_map.restype = gboolean
    libgtk3.gtk_window_get_focus_on_map.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_type_hint.restype = None
    libgtk3.gtk_window_set_type_hint.argtypes = [_GtkWindow,GdkWindowTypeHint]
except:
   pass
try:
    libgtk3.gtk_window_begin_resize_drag.restype = None
    libgtk3.gtk_window_begin_resize_drag.argtypes = [_GtkWindow,GdkWindowEdge,gint,gint,gint,guint32]
except:
   pass
try:
    libgtk3.gtk_window_unstick.restype = None
    libgtk3.gtk_window_unstick.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_destroy_with_parent.restype = gboolean
    libgtk3.gtk_window_get_destroy_with_parent.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_get_has_resize_grip.restype = gboolean
    libgtk3.gtk_window_get_has_resize_grip.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_gravity.restype = None
    libgtk3.gtk_window_set_gravity.argtypes = [_GtkWindow,GdkGravity]
except:
   pass
try:
    libgtk3.gtk_window_add_accel_group.restype = None
    libgtk3.gtk_window_add_accel_group.argtypes = [_GtkWindow,_GtkAccelGroup]
except:
   pass
try:
    libgtk3.gtk_window_set_default_icon_name.restype = None
    libgtk3.gtk_window_set_default_icon_name.argtypes = [_GtkWindow,Asciifier]
except:
   pass
try:
    libgtk3.gtk_window_get_icon_list.restype = _GList
    libgtk3.gtk_window_get_icon_list.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_keep_above.restype = None
    libgtk3.gtk_window_set_keep_above.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_set_has_user_ref_count.restype = None
    libgtk3.gtk_window_set_has_user_ref_count.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_get_type_hint.restype = GdkWindowTypeHint
    libgtk3.gtk_window_get_type_hint.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_decorated.restype = None
    libgtk3.gtk_window_set_decorated.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_fullscreen.restype = None
    libgtk3.gtk_window_fullscreen.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_activate_key.restype = gboolean
    libgtk3.gtk_window_activate_key.argtypes = [_GtkWindow,_GdkEventKey]
except:
   pass
try:
    libgtk3.gtk_window_set_deletable.restype = None
    libgtk3.gtk_window_set_deletable.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_present_with_time.restype = None
    libgtk3.gtk_window_present_with_time.argtypes = [_GtkWindow,guint32]
except:
   pass
try:
    libgtk3.gtk_window_get_default_size.restype = None
    libgtk3.gtk_window_get_default_size.argtypes = [_GtkWindow,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gtk_window_set_focus.restype = None
    libgtk3.gtk_window_set_focus.argtypes = [_GtkWindow,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_window_add_mnemonic.restype = None
    libgtk3.gtk_window_add_mnemonic.argtypes = [_GtkWindow,guint,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_window_remove_accel_group.restype = None
    libgtk3.gtk_window_remove_accel_group.argtypes = [_GtkWindow,_GtkAccelGroup]
except:
   pass
try:
    libgtk3.gtk_window_set_accept_focus.restype = None
    libgtk3.gtk_window_set_accept_focus.argtypes = [_GtkWindow,gboolean]
except:
   pass
try:
    libgtk3.gtk_window_reshow_with_initial_size.restype = None
    libgtk3.gtk_window_reshow_with_initial_size.argtypes = [_GtkWindow]
except:
   pass
try:
    libgtk3.gtk_window_set_default_icon_from_file.restype = gboolean
    libgtk3.gtk_window_set_default_icon_from_file.argtypes = [Asciifier,_GError]
except:
   pass
try:
    libgtk3.gtk_window_get_default_icon_name.restype = c_char_p
    libgtk3.gtk_window_get_default_icon_name.argtypes = []
except:
   pass
try:
    libgtk3.gtk_window_get_default_icon_list.restype = _GList
    libgtk3.gtk_window_get_default_icon_list.argtypes = []
except:
   pass
try:
    libgtk3.gtk_window_list_toplevels.restype = _GList
    libgtk3.gtk_window_list_toplevels.argtypes = []
except:
   pass
from . import gtk3__GtkBin
class GtkWindow( gtk3__GtkBin.GtkBin):
    """Class GtkWindow Constructors"""
    def __init__( self, type,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_window_new.restype = POINTER(c_void_p)
            
            libgtk3.gtk_window_new.argtypes = [GtkWindowType]
            self._object = libgtk3.gtk_window_new(type, )

    """Methods"""
    def activate_focus(  self, ):

        
        return libgtk3.gtk_window_activate_focus( self._object )

    def set_skip_pager_hint(  self, setting, ):

        
        libgtk3.gtk_window_set_skip_pager_hint( self._object,setting )

    def set_geometry_hints(  self, geometry_widget, geometry, geom_mask, ):
        if geometry_widget: geometry_widget = geometry_widget._object
        else: geometry_widget = POINTER(c_void_p)()
        if geometry: geometry = geometry._object
        else: geometry = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_geometry_hints( self._object,geometry_widget,geometry,geom_mask )

    def get_group(  self, ):

        from .gtk3 import GtkWindowGroup
        return GtkWindowGroup(None, obj=libgtk3.gtk_window_get_group( self._object ) or POINTER(c_void_p)())

    def set_has_resize_grip(  self, value, ):

        
        libgtk3.gtk_window_set_has_resize_grip( self._object,value )

    def get_skip_pager_hint(  self, ):

        
        return libgtk3.gtk_window_get_skip_pager_hint( self._object )

    def maximize(  self, ):

        
        libgtk3.gtk_window_maximize( self._object )

    def set_icon_from_file(  self, filename, err, ):
        if err: err = err._object
        else: err = POINTER(c_void_p)()

        
        return libgtk3.gtk_window_set_icon_from_file( self._object,filename,err )

    def get_urgency_hint(  self, ):

        
        return libgtk3.gtk_window_get_urgency_hint( self._object )

    def propagate_key_event(  self, event, ):
        if event: event = event._object
        else: event = POINTER(c_void_p)()

        
        return libgtk3.gtk_window_propagate_key_event( self._object,event )

    def get_opacity(  self, ):

        
        return libgtk3.gtk_window_get_opacity( self._object )

    def get_resize_grip_area(  self, rect, ):
        if rect: rect = rect._object
        else: rect = POINTER(c_void_p)()

        
        return libgtk3.gtk_window_get_resize_grip_area( self._object,rect )

    def unmaximize(  self, ):

        
        libgtk3.gtk_window_unmaximize( self._object )

    def set_screen(  self, screen, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_screen( self._object,screen )

    def get_position(  self, root_x, root_y, ):

        
        libgtk3.gtk_window_get_position( self._object,root_x,root_y )

    def set_default_size(  self, width, height, ):

        
        libgtk3.gtk_window_set_default_size( self._object,width,height )

    def is_active(  self, ):

        
        return libgtk3.gtk_window_is_active( self._object )

    def set_focus_on_map(  self, setting, ):

        
        libgtk3.gtk_window_set_focus_on_map( self._object,setting )

    def move(  self, x, y, ):

        
        libgtk3.gtk_window_move( self._object,x,y )

    def set_position(  self, position, ):
        if position: position = position._object
        else: position = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_position( self._object,position )

    def set_destroy_with_parent(  self, setting, ):

        
        libgtk3.gtk_window_set_destroy_with_parent( self._object,setting )

    def resize_to_geometry(  self, width, height, ):

        
        libgtk3.gtk_window_resize_to_geometry( self._object,width,height )

    def set_focus_visible(  self, setting, ):

        
        libgtk3.gtk_window_set_focus_visible( self._object,setting )

    def set_mnemonics_visible(  self, setting, ):

        
        libgtk3.gtk_window_set_mnemonics_visible( self._object,setting )

    def has_toplevel_focus(  self, ):

        
        return libgtk3.gtk_window_has_toplevel_focus( self._object )

    def stick(  self, ):

        
        libgtk3.gtk_window_stick( self._object )

    def get_title(  self, ):

        
        return libgtk3.gtk_window_get_title( self._object )

    def set_resizable(  self, resizable, ):

        
        libgtk3.gtk_window_set_resizable( self._object,resizable )

    def get_size(  self, width, height, ):

        
        libgtk3.gtk_window_get_size( self._object,width,height )

    def set_default(  self, default_widget, ):
        if default_widget: default_widget = default_widget._object
        else: default_widget = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_default( self._object,default_widget )

    def get_deletable(  self, ):

        
        return libgtk3.gtk_window_get_deletable( self._object )

    def begin_move_drag(  self, button, root_x, root_y, timestamp, ):

        
        libgtk3.gtk_window_begin_move_drag( self._object,button,root_x,root_y,timestamp )

    def get_gravity(  self, ):

        
        return libgtk3.gtk_window_get_gravity( self._object )

    def set_icon(  self, icon, ):
        if icon: icon = icon._object
        else: icon = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_icon( self._object,icon )

    def mnemonic_activate(  self, keyval, modifier, ):

        
        return libgtk3.gtk_window_mnemonic_activate( self._object,keyval,modifier )

    def get_skip_taskbar_hint(  self, ):

        
        return libgtk3.gtk_window_get_skip_taskbar_hint( self._object )

    def get_focus_visible(  self, ):

        
        return libgtk3.gtk_window_get_focus_visible( self._object )

    def present(  self, ):

        
        libgtk3.gtk_window_present( self._object )

    def unfullscreen(  self, ):

        
        libgtk3.gtk_window_unfullscreen( self._object )

    def set_keep_below(  self, setting, ):

        
        libgtk3.gtk_window_set_keep_below( self._object,setting )

    def resize_grip_is_visible(  self, ):

        
        return libgtk3.gtk_window_resize_grip_is_visible( self._object )

    def deiconify(  self, ):

        
        libgtk3.gtk_window_deiconify( self._object )

    def resize(  self, width, height, ):

        
        libgtk3.gtk_window_resize( self._object,width,height )

    def get_role(  self, ):

        
        return libgtk3.gtk_window_get_role( self._object )

    def get_focus(  self, ):

        from .gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_window_get_focus( self._object ) or POINTER(c_void_p)())

    def set_auto_startup_notification(  self, setting, ):

        
        libgtk3.gtk_window_set_auto_startup_notification( self._object,setting )

    def get_mnemonics_visible(  self, ):

        
        return libgtk3.gtk_window_get_mnemonics_visible( self._object )

    def get_mnemonic_modifier(  self, ):

        
        return libgtk3.gtk_window_get_mnemonic_modifier( self._object )

    def set_application(  self, application, ):
        if application: application = application._object
        else: application = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_application( self._object,application )

    def set_default_icon(  self, icon, ):
        if icon: icon = icon._object
        else: icon = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_default_icon( self._object,icon )

    def set_default_geometry(  self, width, height, ):

        
        libgtk3.gtk_window_set_default_geometry( self._object,width,height )

    def get_icon(  self, ):

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_window_get_icon( self._object ) or POINTER(c_void_p)())

    def set_role(  self, role, ):

        
        libgtk3.gtk_window_set_role( self._object,role )

    def set_skip_taskbar_hint(  self, setting, ):

        
        libgtk3.gtk_window_set_skip_taskbar_hint( self._object,setting )

    def activate_default(  self, ):

        
        return libgtk3.gtk_window_activate_default( self._object )

    def has_group(  self, ):

        
        return libgtk3.gtk_window_has_group( self._object )

    def get_modal(  self, ):

        
        return libgtk3.gtk_window_get_modal( self._object )

    def set_title(  self, title, ):

        
        libgtk3.gtk_window_set_title( self._object, str(title).encode('ascii') )

    def set_transient_for(  self, parent, ):
        if parent: parent = parent._object
        else: parent = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_transient_for( self._object,parent )

    def set_icon_list(  self, list, ):
        if list: list = list._object
        else: list = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_icon_list( self._object,list )

    def set_icon_name(  self, name, ):

        
        libgtk3.gtk_window_set_icon_name( self._object,name )

    def set_urgency_hint(  self, setting, ):

        
        libgtk3.gtk_window_set_urgency_hint( self._object,setting )

    def get_icon_name(  self, ):

        
        return libgtk3.gtk_window_get_icon_name( self._object )

    def set_opacity(  self, opacity, ):

        
        libgtk3.gtk_window_set_opacity( self._object,opacity )

    def iconify(  self, ):

        
        libgtk3.gtk_window_iconify( self._object )

    def get_transient_for(  self, ):

        from .gtk3 import GtkWindow
        return GtkWindow( obj=libgtk3.gtk_window_get_transient_for( self._object ) or POINTER(c_void_p)())

    def get_window_type(  self, ):

        
        return libgtk3.gtk_window_get_window_type( self._object )

    def remove_mnemonic(  self, keyval, target, ):
        if target: target = target._object
        else: target = POINTER(c_void_p)()

        
        libgtk3.gtk_window_remove_mnemonic( self._object,keyval,target )

    def get_resizable(  self, ):

        
        return libgtk3.gtk_window_get_resizable( self._object )

    def get_decorated(  self, ):

        
        return libgtk3.gtk_window_get_decorated( self._object )

    def parse_geometry(  self, geometry, ):

        
        return libgtk3.gtk_window_parse_geometry( self._object,geometry )

    def get_application(  self, ):

        from .gtk3 import GtkApplication
        return GtkApplication(None,None, obj=libgtk3.gtk_window_get_application( self._object ) or POINTER(c_void_p)())

    def get_default_widget(  self, ):

        from .gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_window_get_default_widget( self._object ) or POINTER(c_void_p)())

    def set_mnemonic_modifier(  self, modifier, ):

        
        libgtk3.gtk_window_set_mnemonic_modifier( self._object,modifier )

    def set_startup_id(  self, startup_id, ):

        
        libgtk3.gtk_window_set_startup_id( self._object,startup_id )

    def set_default_icon_list(  self, list, ):
        if list: list = list._object
        else: list = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_default_icon_list( self._object,list )

    def set_modal(  self, modal, ):

        
        libgtk3.gtk_window_set_modal( self._object,modal )

    def get_screen(  self, ):

        from .gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gtk_window_get_screen( self._object ) or POINTER(c_void_p)())

    def set_wmclass(  self, wmclass_name, wmclass_class, ):

        
        libgtk3.gtk_window_set_wmclass( self._object,wmclass_name,wmclass_class )

    def get_accept_focus(  self, ):

        
        return libgtk3.gtk_window_get_accept_focus( self._object )

    def get_focus_on_map(  self, ):

        
        return libgtk3.gtk_window_get_focus_on_map( self._object )

    def set_type_hint(  self, hint, ):

        
        libgtk3.gtk_window_set_type_hint( self._object,hint )

    def begin_resize_drag(  self, edge, button, root_x, root_y, timestamp, ):
        if edge: edge = edge._object
        else: edge = POINTER(c_void_p)()

        
        libgtk3.gtk_window_begin_resize_drag( self._object,edge,button,root_x,root_y,timestamp )

    def unstick(  self, ):

        
        libgtk3.gtk_window_unstick( self._object )

    def get_destroy_with_parent(  self, ):

        
        return libgtk3.gtk_window_get_destroy_with_parent( self._object )

    def get_has_resize_grip(  self, ):

        
        return libgtk3.gtk_window_get_has_resize_grip( self._object )

    def set_gravity(  self, gravity, ):

        
        libgtk3.gtk_window_set_gravity( self._object,gravity )

    def add_accel_group(  self, accel_group, ):
        if accel_group: accel_group = accel_group._object
        else: accel_group = POINTER(c_void_p)()

        
        libgtk3.gtk_window_add_accel_group( self._object,accel_group )

    def set_default_icon_name(  self, name, ):

        
        libgtk3.gtk_window_set_default_icon_name( self._object,name )

    def get_icon_list(  self, ):

        from .gobject import GList
        return GList( obj=libgtk3.gtk_window_get_icon_list( self._object ) or POINTER(c_void_p)())

    def set_keep_above(  self, setting, ):

        
        libgtk3.gtk_window_set_keep_above( self._object,setting )

    def set_has_user_ref_count(  self, setting, ):

        
        libgtk3.gtk_window_set_has_user_ref_count( self._object,setting )

    def get_type_hint(  self, ):

        
        return libgtk3.gtk_window_get_type_hint( self._object )

    def set_decorated(  self, setting, ):

        
        libgtk3.gtk_window_set_decorated( self._object,setting )

    def fullscreen(  self, ):

        
        libgtk3.gtk_window_fullscreen( self._object )

    def activate_key(  self, event, ):
        if event: event = event._object
        else: event = POINTER(c_void_p)()

        
        return libgtk3.gtk_window_activate_key( self._object,event )

    def set_deletable(  self, setting, ):

        
        libgtk3.gtk_window_set_deletable( self._object,setting )

    def present_with_time(  self, timestamp, ):

        
        libgtk3.gtk_window_present_with_time( self._object,timestamp )

    def get_default_size(  self, width, height, ):

        
        libgtk3.gtk_window_get_default_size( self._object,width,height )

    def set_focus(  self, focus, ):
        if focus: focus = focus._object
        else: focus = POINTER(c_void_p)()

        
        libgtk3.gtk_window_set_focus( self._object,focus )

    def add_mnemonic(  self, keyval, target, ):
        if target: target = target._object
        else: target = POINTER(c_void_p)()

        
        libgtk3.gtk_window_add_mnemonic( self._object,keyval,target )

    def remove_accel_group(  self, accel_group, ):
        if accel_group: accel_group = accel_group._object
        else: accel_group = POINTER(c_void_p)()

        
        libgtk3.gtk_window_remove_accel_group( self._object,accel_group )

    def set_accept_focus(  self, setting, ):

        
        libgtk3.gtk_window_set_accept_focus( self._object,setting )

    def reshow_with_initial_size(  self, ):

        
        libgtk3.gtk_window_reshow_with_initial_size( self._object )

    @staticmethod
    def set_default_icon_from_file( filename, err,):
        if err: err = err._object
        else: err = POINTER(c_void_p)()
        
        return     libgtk3.gtk_window_set_default_icon_from_file(filename, err, )

    @staticmethod
    def get_default_icon_name():
        
        return     libgtk3.gtk_window_get_default_icon_name()

    @staticmethod
    def get_default_icon_list():
        from .gobject import GList
        return GList( obj=    libgtk3.gtk_window_get_default_icon_list()
 or POINTER(c_void_p)())
    @staticmethod
    def list_toplevels():
        from .gobject import GList
        return GList( obj=    libgtk3.gtk_window_list_toplevels()
 or POINTER(c_void_p)())
