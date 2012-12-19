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
from gtk3_types import *
from gtk3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkMessageDialog = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GtkLabel = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkBin = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_WebKitWebPolicyDecision = POINTER(c_int)
_PangoEngineShape = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_GAsyncResult = POINTER(c_int)
_cairo_matrix_t = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_JSValue = POINTER(c_int)
_GtkProgressBar = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GMainLoop = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkContainer = POINTER(c_int)
_PangoItem = POINTER(c_int)
_GClosure = POINTER(c_int)
_GIcon = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GInterface = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
_GFileEnumerator = POINTER(c_int)
_GtkDialog = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GtkCssProvider = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_void = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_GInputStream = POINTER(c_int)
_GtkIconInfo = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_WebKitWebResource = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkNumerableIcon = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GObject = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GAppLaunchContext = POINTER(c_int)
_PangoAttrIterator = POINTER(c_int)
_GFileAttributeMatcher = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkIconTheme = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAccelLabel = POINTER(c_int)
_GtkAdjustment = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GString = POINTER(c_int)
_GFileAttributeMatcher = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GBoxed = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
_GdkPoint = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GSource = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GIOStream = POINTER(c_int)
_GIOStream = POINTER(c_int)
_JSString = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_GOutputStream = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GSource = POINTER(c_int)
_GtkMisc = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_GFileInfo = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_GEmblemedIcon = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_GAppLauncContext = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
_GScanner = POINTER(c_int)
_GFileAttributeInfoList = POINTER(c_int)
_GCancellable = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GtkContainerClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GtkAdjustment = POINTER(c_int)
_GdkDragContext = POINTER(c_int)
_GtkAssistant = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_GAppLaunchContext = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
_GActionGroup = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_GtkScrolledWindow = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
_GFile = POINTER(c_int)
_PangoLayoutIter = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
_GFileInputStream = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_GdkPixbufAnimation = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GtkAboutDialog = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkPixbufAnimationIter = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkEventButton = POINTER(c_int)
_GCancellable = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_GMount = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GPollFD = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GFile = POINTER(c_int)
_JSContext = POINTER(c_int)
_GDrive = POINTER(c_int)
_PangoFontsetSimple = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_GMutex = POINTER(c_int)
_GtkImage = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GtkStatusbar = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkPrintOperation = POINTER(c_int)
_GtkThemingEngine = POINTER(c_int)
_GString = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
_GFileInfo = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_GTimeVal = POINTER(c_int)
_GtkInvisible = POINTER(c_int)
_GSourceFuncs = POINTER(c_int)
_JSPropertyNameAccumulator = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_GtkStylePropertyParser = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GtkBox = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkPixbufAnimation = POINTER(c_int)
_GEmblem = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GVolume = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GPollFD = POINTER(c_int)
_GFileOutputStream = POINTER(c_int)
_JSObject = POINTER(c_int)
_GdkDragContext = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
_GInputStream = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_WebKitWebNavigationAction = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GParameter = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkGradient = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkPackType = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GMountOperation = POINTER(c_int)
_GValue = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
_GSourceCallbackFuncs = POINTER(c_int)
_PangoFontFace = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_GtkCssSection = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GByteArray = POINTER(c_int)
_GdkPixbufSimpleAnim = POINTER(c_int)
_JSObject = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
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
    libgtk3.gtk_paint_slider.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkOrientation]
except:
   pass
try:
    libgtk3.gtk_paint_resize_grip.restype = None
    libgtk3.gtk_paint_resize_grip.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,c_char_p,GdkWindowEdge,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_arrow.restype = None
    libgtk3.gtk_paint_arrow.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,GtkArrowType,gboolean,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_get_style_property.restype = None
    libgtk3.gtk_style_get_style_property.argtypes = [_GtkStyle,GType,c_char_p,_GValue]
except:
   pass
try:
    libgtk3.gtk_paint_expander.restype = None
    libgtk3.gtk_paint_expander.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,c_char_p,gint,gint,GtkExpanderStyle]
except:
   pass
try:
    libgtk3.gtk_paint_flat_box.restype = None
    libgtk3.gtk_paint_flat_box.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_get.restype = None
    libgtk3.gtk_style_get.argtypes = [_GtkStyle,GType,c_char_p,]
except:
   pass
try:
    libgtk3.gtk_style_render_icon.restype = _GdkPixbuf
    libgtk3.gtk_style_render_icon.argtypes = [_GtkStyle,_GtkIconSource,GtkTextDirection,GtkStateType,GtkIconSize,_GtkWidget,c_char_p]
except:
   pass
try:
    libgtk3.gtk_style_has_context.restype = gboolean
    libgtk3.gtk_style_has_context.argtypes = [_GtkStyle]
except:
   pass
try:
    libgtk3.gtk_style_lookup_icon_set.restype = _GtkIconSet
    libgtk3.gtk_style_lookup_icon_set.argtypes = [_GtkStyle,c_char_p]
except:
   pass
try:
    libgtk3.gtk_paint_shadow_gap.restype = None
    libgtk3.gtk_paint_shadow_gap.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkPositionType,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_check.restype = None
    libgtk3.gtk_paint_check.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_hline.restype = None
    libgtk3.gtk_paint_hline.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,c_char_p,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_shadow.restype = None
    libgtk3.gtk_paint_shadow.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_diamond.restype = None
    libgtk3.gtk_paint_diamond.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_detach.restype = None
    libgtk3.gtk_style_detach.argtypes = [_GtkStyle]
except:
   pass
try:
    libgtk3.gtk_style_lookup_color.restype = gboolean
    libgtk3.gtk_style_lookup_color.argtypes = [_GtkStyle,c_char_p,_GdkColor]
except:
   pass
try:
    libgtk3.gtk_style_attach.restype = _GtkStyle
    libgtk3.gtk_style_attach.argtypes = [_GtkStyle,_GdkWindow]
except:
   pass
try:
    libgtk3.gtk_paint_box_gap.restype = None
    libgtk3.gtk_paint_box_gap.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkPositionType,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_tab.restype = None
    libgtk3.gtk_paint_tab.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_spinner.restype = None
    libgtk3.gtk_paint_spinner.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,c_char_p,guint,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_layout.restype = None
    libgtk3.gtk_paint_layout.argtypes = [_GtkStyle,_cairo_t,GtkStateType,gboolean,_GtkWidget,c_char_p,gint,gint,_PangoLayout]
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
    libgtk3.gtk_paint_focus.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,c_char_p,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_extension.restype = None
    libgtk3.gtk_paint_extension.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkPositionType]
except:
   pass
try:
    libgtk3.gtk_style_copy.restype = _GtkStyle
    libgtk3.gtk_style_copy.argtypes = [_GtkStyle]
except:
   pass
try:
    libgtk3.gtk_paint_vline.restype = None
    libgtk3.gtk_paint_vline.argtypes = [_GtkStyle,_cairo_t,GtkStateType,_GtkWidget,c_char_p,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_paint_handle.restype = None
    libgtk3.gtk_paint_handle.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkOrientation]
except:
   pass
try:
    libgtk3.gtk_paint_box.restype = None
    libgtk3.gtk_paint_box.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_set_background.restype = None
    libgtk3.gtk_style_set_background.argtypes = [_GtkStyle,_GdkWindow,GtkStateType]
except:
   pass
try:
    libgtk3.gtk_paint_option.restype = None
    libgtk3.gtk_paint_option.argtypes = [_GtkStyle,_cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
except:
   pass
import gobject__GObject
class GtkStyle( gobject__GObject.GObject):
    """Class GtkStyle Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_style_new.restype = POINTER(c_int)
            
            libgtk3.gtk_style_new.argtypes = []
            self._object = libgtk3.gtk_style_new()

    """Methods"""
    def gtk_paint_slider(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, orientation, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_slider( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,orientation )

    def gtk_paint_resize_grip(  self, cr, state_type, widget, detail, edge, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        if edge: edge = edge._object
        else: edge = POINTER(c_int)()

        
        libgtk3.gtk_paint_resize_grip( self._object,cr,state_type,widget,detail,edge,x,y,width,height )

    def gtk_paint_arrow(  self, cr, state_type, shadow_type, widget, detail, arrow_type, fill, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        if arrow_type: arrow_type = arrow_type._object
        else: arrow_type = POINTER(c_int)()

        
        libgtk3.gtk_paint_arrow( self._object,cr,state_type,shadow_type,widget,detail,arrow_type,fill,x,y,width,height )

    def get_style_property(  self, widget_type, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        
        libgtk3.gtk_style_get_style_property( self._object,widget_type,property_name,value )

    def gtk_paint_expander(  self, cr, state_type, widget, detail, x, y, expander_style, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_expander( self._object,cr,state_type,widget,detail,x,y,expander_style )

    def gtk_paint_flat_box(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_flat_box( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def get(  self, widget_type, first_property_name,*args  ):


        def callit( widget_type, first_property_name, *args ):
                for arg in args:
                     libgtk3.gtk_style_get.argtypes.append(args[1])
                return libgtk3.gtk_style_get( widget_type, first_property_name, *args)
    
        return callit( self._object, widget_type, first_property_name,*args )

    def render_icon(  self, source, direction, state, size, widget, detail, ):
        if source: source = source._object
        else: source = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_style_render_icon( self._object,source,direction,state,size,widget,detail ) or POINTER(c_int)())

    def has_context(  self, ):

        
        return libgtk3.gtk_style_has_context( self._object )

    def lookup_icon_set(  self, stock_id, ):

        from gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_style_lookup_icon_set( self._object,stock_id ) or POINTER(c_int)())

    def gtk_paint_shadow_gap(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, gap_x, gap_width, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        if gap_side: gap_side = gap_side._object
        else: gap_side = POINTER(c_int)()

        
        libgtk3.gtk_paint_shadow_gap( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,gap_side,gap_x,gap_width )

    def gtk_paint_check(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_check( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def gtk_paint_hline(  self, cr, state_type, widget, detail, x1, x2, y, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_hline( self._object,cr,state_type,widget,detail,x1,x2,y )

    def gtk_paint_shadow(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_shadow( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def gtk_paint_diamond(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_diamond( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def detach(  self, ):

        
        libgtk3.gtk_style_detach( self._object )

    def lookup_color(  self, color_name, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        
        return libgtk3.gtk_style_lookup_color( self._object,color_name,color )

    def attach(  self, window, ):
        if window: window = window._object
        else: window = POINTER(c_int)()

        from gtk3 import GtkStyle
        return GtkStyle(None, obj=libgtk3.gtk_style_attach( self._object,window ) or POINTER(c_int)())

    def gtk_paint_box_gap(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, gap_x, gap_width, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        if gap_side: gap_side = gap_side._object
        else: gap_side = POINTER(c_int)()

        
        libgtk3.gtk_paint_box_gap( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,gap_side,gap_x,gap_width )

    def gtk_paint_tab(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_tab( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def gtk_paint_spinner(  self, cr, state_type, widget, detail, step, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_spinner( self._object,cr,state_type,widget,detail,step,x,y,width,height )

    def gtk_paint_layout(  self, cr, state_type, use_text, widget, detail, x, y, layout, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        if layout: layout = layout._object
        else: layout = POINTER(c_int)()

        
        libgtk3.gtk_paint_layout( self._object,cr,state_type,use_text,widget,detail,x,y,layout )

    def gtk_draw_insertion_cursor(  self, widget, cr, location, is_primary, direction, draw_arrow, ):
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if location: location = location._object
        else: location = POINTER(c_int)()

        
        libgtk3.gtk_draw_insertion_cursor( self._object,widget,cr,location,is_primary,direction,draw_arrow )

    def apply_default_background(  self, cr, window, state_type, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if window: window = window._object
        else: window = POINTER(c_int)()

        
        libgtk3.gtk_style_apply_default_background( self._object,cr,window,state_type,x,y,width,height )

    def gtk_paint_focus(  self, cr, state_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_focus( self._object,cr,state_type,widget,detail,x,y,width,height )

    def gtk_paint_extension(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        if gap_side: gap_side = gap_side._object
        else: gap_side = POINTER(c_int)()

        
        libgtk3.gtk_paint_extension( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,gap_side )

    def copy(  self, ):

        from gtk3 import GtkStyle
        return GtkStyle( obj=libgtk3.gtk_style_copy( self._object ) or POINTER(c_int)())

    def gtk_paint_vline(  self, cr, state_type, widget, detail, y1_, y2_, x, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_vline( self._object,cr,state_type,widget,detail,y1_,y2_,x )

    def gtk_paint_handle(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, orientation, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_handle( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height,orientation )

    def gtk_paint_box(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_box( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

    def set_background(  self, window, state_type, ):
        if window: window = window._object
        else: window = POINTER(c_int)()

        
        libgtk3.gtk_style_set_background( self._object,window,state_type )

    def gtk_paint_option(  self, cr, state_type, shadow_type, widget, detail, x, y, width, height, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_paint_option( self._object,cr,state_type,shadow_type,widget,detail,x,y,width,height )

