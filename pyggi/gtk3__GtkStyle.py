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
GdkCursorType = c_int
GdkVisualType = c_int
GdkByteOrder = c_int

try:
    libgtk3.gtk_paint_slider.restype = None
    libgtk3.gtk_paint_slider.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint,GtkOrientation]
except:
   pass
try:
    libgtk3.gtk_paint_resize_grip.restype = None
    libgtk3.gtk_paint_resize_grip.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,Asciifier,GdkWindowEdge,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_arrow.restype = None
    libgtk3.gtk_paint_arrow.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,GtkArrowType,gboolean,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_get_style_property.restype = None
    libgtk3.gtk_style_get_style_property.argtypes = [_GtkStyle,GType,Asciifier,_GValue]
except:
   pass
try:
    libgtk3.gtk_paint_expander.restype = None
    libgtk3.gtk_paint_expander.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,Asciifier,gint,gint,GtkExpanderStyle]
except:
   pass
try:
    libgtk3.gtk_paint_flat_box.restype = None
    libgtk3.gtk_paint_flat_box.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_get.restype = None
    libgtk3.gtk_style_get.argtypes = [_GtkStyle,GType,Asciifier,]
except:
   pass
try:
    libgtk3.gtk_style_render_icon.restype = _GdkPixbuf
    libgtk3.gtk_style_render_icon.argtypes = [_GtkStyle,_GtkIconSource,GtkTextDirection,GtkStateType,GtkIconSize,_GtkWidget,Asciifier]
except:
   pass
try:
    libgtk3.gtk_style_has_context.restype = gboolean
    libgtk3.gtk_style_has_context.argtypes = [_GtkStyle]
except:
   pass
try:
    libgtk3.gtk_style_lookup_icon_set.restype = _GtkIconSet
    libgtk3.gtk_style_lookup_icon_set.argtypes = [_GtkStyle,Asciifier]
except:
   pass
try:
    libgtk3.gtk_paint_shadow_gap.restype = None
    libgtk3.gtk_paint_shadow_gap.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint,GtkPositionType,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_check.restype = None
    libgtk3.gtk_paint_check.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_hline.restype = None
    libgtk3.gtk_paint_hline.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,Asciifier,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_shadow.restype = None
    libgtk3.gtk_paint_shadow.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_diamond.restype = None
    libgtk3.gtk_paint_diamond.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_detach.restype = None
    libgtk3.gtk_style_detach.argtypes = [_GtkStyle]
except:
   pass
try:
    libgtk3.gtk_style_lookup_color.restype = gboolean
    libgtk3.gtk_style_lookup_color.argtypes = [_GtkStyle,Asciifier,_GdkColor]
except:
   pass
try:
    libgtk3.gtk_style_attach.restype = _GtkStyle
    libgtk3.gtk_style_attach.argtypes = [_GtkStyle,_GdkWindow]
except:
   pass
try:
    libgtk3.gtk_paint_box_gap.restype = None
    libgtk3.gtk_paint_box_gap.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint,GtkPositionType,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_tab.restype = None
    libgtk3.gtk_paint_tab.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_spinner.restype = None
    libgtk3.gtk_paint_spinner.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,Asciifier,guint,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_layout.restype = None
    libgtk3.gtk_paint_layout.argtypes = [_GtkStyle,_cairo_t,GtkStateType,gboolean,_GtkWidget,Asciifier,gint,gint,_PangoLayout]
except:
   pass
try:
    libgtk3.gtk_draw_insertion_cursor.restype = None
    libgtk3.gtk_draw_insertion_cursor.argtypes = [_GtkStyle,_GtkWidget,_cairo_t,_GdkRectangle,gboolean,GtkTextDirection,gboolean]
except:
   pass
try:
    libgtk3.gtk_style_apply_default_background.restype = None
    libgtk3.gtk_style_apply_default_background.argtypes = [_GtkStyle,_cairo_t,_GdkWindow,GtkStateType,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_focus.restype = None
    libgtk3.gtk_paint_focus.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,Asciifier,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_extension.restype = None
    libgtk3.gtk_paint_extension.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint,GtkPositionType]
except:
   pass
try:
    libgtk3.gtk_style_copy.restype = _GtkStyle
    libgtk3.gtk_style_copy.argtypes = [_GtkStyle]
except:
   pass
try:
    libgtk3.gtk_paint_vline.restype = None
    libgtk3.gtk_paint_vline.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,Asciifier,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_handle.restype = None
    libgtk3.gtk_paint_handle.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint,GtkOrientation]
except:
   pass
try:
    libgtk3.gtk_paint_box.restype = None
    libgtk3.gtk_paint_box.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_set_background.restype = None
    libgtk3.gtk_style_set_background.argtypes = [_GtkStyle,_GdkWindow,GtkStateType]
except:
   pass
try:
    libgtk3.gtk_paint_option.restype = None
    libgtk3.gtk_paint_option.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,Asciifier,gint,gint,gint,gint]
except:
   pass
from . import gobject__GObject
class GtkStyle( gobject__GObject.GObject):
    """Class GtkStyle Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_style_new.restype = POINTER(c_void_p)
            
            libgtk3.gtk_style_new.argtypes = []
            self._object = libgtk3.gtk_style_new()

    """Methods"""
    def gtk_paint_slider(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, orientation, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_slider( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,orientation )

    def gtk_paint_resize_grip(  self, cr, state_type, widget, detail, edge, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()
        if edge: edge = edge._object
        else: edge = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_resize_grip( self._object,cr,state_type,widget,detail,edge,x,y,width,height )

    def gtk_paint_arrow(  self, cr, state_type, shadow_type, widget, detail, arrow_type, fill, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()
        if arrow_type: arrow_type = arrow_type._object
        else: arrow_type = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_arrow( self._object,cr,state_type,shadow_type,widget,detail,arrow_type,fill,x,y,width,height )

    def get_style_property(  self, widget_type, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgtk3.gtk_style_get_style_property( self._object,widget_type,property_name,value )

    def gtk_paint_expander(  self, cr, state_type, widget, detail, x, y, expander_style, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_expander( self._object,cr,state_type,widget,detail,x,y,expander_style )

    def gtk_paint_flat_box(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_flat_box( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def get(  self, widget_type, first_property_name,*args  ):


        def callit( widget_type, first_property_name, *args ):
                for arg in args:
                     libgtk3.gtk_style_get.argtypes.append(args[1])
                return libgtk3.gtk_style_get( widget_type, first_property_name, *args)
    
        return callit( self._object, widget_type, first_property_name,*args )

    def render_icon(  self, source, direction, state, size, widget, detail, ):
        if source: source = source._object
        else: source = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_style_render_icon( self._object,source,direction,state,size,widget,detail ) or POINTER(c_void_p)())

    def has_context(  self, ):

        
        return libgtk3.gtk_style_has_context( self._object )

    def lookup_icon_set(  self, stock_id, ):

        from .gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_style_lookup_icon_set( self._object,stock_id ) or POINTER(c_void_p)())

    def gtk_paint_shadow_gap(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, gap_x, gap_width, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()
        if gap_side: gap_side = gap_side._object
        else: gap_side = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_shadow_gap( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,gap_side,gap_x,gap_width )

    def gtk_paint_check(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_check( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def gtk_paint_hline(  self, cr, state_type, widget, detail, x1, x2, y, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_hline( self._object,cr,state_type,widget,detail,x1,x2,y )

    def gtk_paint_shadow(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_shadow( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def gtk_paint_diamond(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_diamond( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def detach(  self, ):

        
        libgtk3.gtk_style_detach( self._object )

    def lookup_color(  self, color_name, color, ):
        if color: color = color._object
        else: color = POINTER(c_void_p)()

        
        return libgtk3.gtk_style_lookup_color( self._object,color_name,color )

    def attach(  self, window, ):
        if window: window = window._object
        else: window = POINTER(c_void_p)()

        from .gtk3 import GtkStyle
        return GtkStyle(None, obj=libgtk3.gtk_style_attach( self._object,window ) or POINTER(c_void_p)())

    def gtk_paint_box_gap(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, gap_x, gap_width, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()
        if gap_side: gap_side = gap_side._object
        else: gap_side = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_box_gap( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,gap_side,gap_x,gap_width )

    def gtk_paint_tab(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_tab( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def gtk_paint_spinner(  self, cr, state_type, widget, detail, step, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_spinner( self._object,cr,state_type,widget,detail,step,x,y,width,height )

    def gtk_paint_layout(  self, cr, state_type, use_text, widget, detail, x, y, layout, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()
        if layout: layout = layout._object
        else: layout = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_layout( self._object,cr,state_type,use_text,widget,detail,x,y,layout )

    def gtk_draw_insertion_cursor(  self, widget, cr, location, is_primary, direction, draw_arrow, ):
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if location: location = location._object
        else: location = POINTER(c_void_p)()

        
        libgtk3.gtk_draw_insertion_cursor( self._object,widget,cr,location,is_primary,direction,draw_arrow )

    def apply_default_background(  self, cr, window, state_type, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if window: window = window._object
        else: window = POINTER(c_void_p)()

        
        libgtk3.gtk_style_apply_default_background( self._object,cr,window,state_type,x,y,width,height )

    def gtk_paint_focus(  self, cr, state_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_focus( self._object,cr,state_type,widget,detail,x,y,width,height )

    def gtk_paint_extension(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()
        if gap_side: gap_side = gap_side._object
        else: gap_side = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_extension( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,gap_side )

    def copy(  self, ):

        from .gtk3 import GtkStyle
        return GtkStyle( obj=libgtk3.gtk_style_copy( self._object ) or POINTER(c_void_p)())

    def gtk_paint_vline(  self, cr, state_type, widget, detail, y1_, y2_, x, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_vline( self._object,cr,state_type,widget,detail,y1_,y2_,x )

    def gtk_paint_handle(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, orientation, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_handle( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,orientation )

    def gtk_paint_box(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_box( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def set_background(  self, window, state_type, ):
        if window: window = window._object
        else: window = POINTER(c_void_p)()

        
        libgtk3.gtk_style_set_background( self._object,window,state_type )

    def gtk_paint_option(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_paint_option( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

