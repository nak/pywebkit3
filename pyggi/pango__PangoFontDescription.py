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
from .pango_types import *
from .pango_enums import *

    
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
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int

try:
    libpango.pango_font_description_to_string.restype = c_char_p
    libpango.pango_font_description_to_string.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_copy.restype = _PangoFontDescription
    libpango.pango_font_description_copy.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_equal.restype = gboolean
    libpango.pango_font_description_equal.argtypes = [_PangoFontDescription,_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_set_family_static.restype = None
    libpango.pango_font_description_set_family_static.argtypes = [_PangoFontDescription,Asciifier]
except:
   pass
try:
    libpango.pango_font_description_get_set_fields.restype = PangoFontMask
    libpango.pango_font_description_get_set_fields.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_set_variant.restype = None
    libpango.pango_font_description_set_variant.argtypes = [_PangoFontDescription,PangoVariant]
except:
   pass
try:
    libpango.pango_font_description_set_size.restype = None
    libpango.pango_font_description_set_size.argtypes = [_PangoFontDescription,gint]
except:
   pass
try:
    libpango.pango_font_description_get_size_is_absolute.restype = gboolean
    libpango.pango_font_description_get_size_is_absolute.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_unset_fields.restype = None
    libpango.pango_font_description_unset_fields.argtypes = [_PangoFontDescription,PangoFontMask]
except:
   pass
try:
    libpango.pango_font_description_set_weight.restype = None
    libpango.pango_font_description_set_weight.argtypes = [_PangoFontDescription,PangoWeight]
except:
   pass
try:
    libpango.pango_font_description_get_style.restype = PangoStyle
    libpango.pango_font_description_get_style.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_get_weight.restype = PangoWeight
    libpango.pango_font_description_get_weight.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_set_style.restype = None
    libpango.pango_font_description_set_style.argtypes = [_PangoFontDescription,PangoStyle]
except:
   pass
try:
    libpango.pango_font_description_get_gravity.restype = PangoGravity
    libpango.pango_font_description_get_gravity.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_get_size.restype = gint
    libpango.pango_font_description_get_size.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_merge_static.restype = None
    libpango.pango_font_description_merge_static.argtypes = [_PangoFontDescription,_PangoFontDescription,gboolean]
except:
   pass
try:
    libpango.pango_font_description_better_match.restype = gboolean
    libpango.pango_font_description_better_match.argtypes = [_PangoFontDescription,_PangoFontDescription,_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_set_stretch.restype = None
    libpango.pango_font_description_set_stretch.argtypes = [_PangoFontDescription,PangoStretch]
except:
   pass
try:
    libpango.pango_font_description_hash.restype = guint
    libpango.pango_font_description_hash.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_set_family.restype = None
    libpango.pango_font_description_set_family.argtypes = [_PangoFontDescription,Asciifier]
except:
   pass
try:
    libpango.pango_font_description_get_stretch.restype = PangoStretch
    libpango.pango_font_description_get_stretch.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_descriptions_free.restype = None
    libpango.pango_font_descriptions_free.argtypes = [_PangoFontDescription,int]
except:
   pass
try:
    libpango.pango_font_description_get_family.restype = c_char_p
    libpango.pango_font_description_get_family.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_copy_static.restype = _PangoFontDescription
    libpango.pango_font_description_copy_static.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_set_absolute_size.restype = None
    libpango.pango_font_description_set_absolute_size.argtypes = [_PangoFontDescription,double]
except:
   pass
try:
    libpango.pango_font_description_merge.restype = None
    libpango.pango_font_description_merge.argtypes = [_PangoFontDescription,_PangoFontDescription,gboolean]
except:
   pass
try:
    libpango.pango_font_description_to_filename.restype = c_char_p
    libpango.pango_font_description_to_filename.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_set_gravity.restype = None
    libpango.pango_font_description_set_gravity.argtypes = [_PangoFontDescription,PangoGravity]
except:
   pass
try:
    libpango.pango_font_description_get_variant.restype = PangoVariant
    libpango.pango_font_description_get_variant.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_free.restype = None
    libpango.pango_font_description_free.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libpango.pango_font_description_from_string.restype = _PangoFontDescription
    libpango.pango_font_description_from_string.argtypes = [Asciifier]
except:
   pass
from . import gobject__GBoxed
class PangoFontDescription( gobject__GBoxed.GBoxed):
    """Class PangoFontDescription Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libpango.pango_font_description_new.restype = POINTER(c_void_p)
            
            libpango.pango_font_description_new.argtypes = []
            self._object = libpango.pango_font_description_new()

    """Methods"""
    def to_string(  self, ):

        
        return libpango.pango_font_description_to_string( self._object )

    def copy(  self, ):

        from .gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libpango.pango_font_description_copy( self._object )  or POINTER(c_void_p)())

    def equal(  self, desc2, ):
        if desc2: desc2 = desc2._object
        else: desc2 = POINTER(c_void_p)()

        
        return libpango.pango_font_description_equal( self._object,desc2 )

    def set_family_static(  self, family, ):

        
        libpango.pango_font_description_set_family_static( self._object,family )

    def get_set_fields(  self, ):

        
        return libpango.pango_font_description_get_set_fields( self._object )

    def set_variant(  self, variant, ):

        
        libpango.pango_font_description_set_variant( self._object,variant )

    def set_size(  self, size, ):

        
        libpango.pango_font_description_set_size( self._object,size )

    def get_size_is_absolute(  self, ):

        
        return libpango.pango_font_description_get_size_is_absolute( self._object )

    def unset_fields(  self, to_unset, ):

        
        libpango.pango_font_description_unset_fields( self._object,to_unset )

    def set_weight(  self, weight, ):

        
        libpango.pango_font_description_set_weight( self._object,weight )

    def get_style(  self, ):

        
        return libpango.pango_font_description_get_style( self._object )

    def get_weight(  self, ):

        
        return libpango.pango_font_description_get_weight( self._object )

    def set_style(  self, style, ):

        
        libpango.pango_font_description_set_style( self._object,style )

    def get_gravity(  self, ):

        
        return libpango.pango_font_description_get_gravity( self._object )

    def get_size(  self, ):

        
        return libpango.pango_font_description_get_size( self._object )

    def merge_static(  self, desc_to_merge, replace_existing, ):
        if desc_to_merge: desc_to_merge = desc_to_merge._object
        else: desc_to_merge = POINTER(c_void_p)()

        
        libpango.pango_font_description_merge_static( self._object,desc_to_merge,replace_existing )

    def better_match(  self, old_match, new_match, ):
        if old_match: old_match = old_match._object
        else: old_match = POINTER(c_void_p)()
        if new_match: new_match = new_match._object
        else: new_match = POINTER(c_void_p)()

        
        return libpango.pango_font_description_better_match( self._object,old_match,new_match )

    def set_stretch(  self, stretch, ):

        
        libpango.pango_font_description_set_stretch( self._object,stretch )

    def hash(  self, ):

        
        return libpango.pango_font_description_hash( self._object )

    def set_family(  self, family, ):

        
        libpango.pango_font_description_set_family( self._object,family )

    def get_stretch(  self, ):

        
        return libpango.pango_font_description_get_stretch( self._object )

    def pango_font_descriptions_free(  self, n_descs, ):

        
        libpango.pango_font_descriptions_free( self._object,n_descs )

    def get_family(  self, ):

        
        return libpango.pango_font_description_get_family( self._object )

    def copy_static(  self, ):

        from .gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libpango.pango_font_description_copy_static( self._object )  or POINTER(c_void_p)())

    def set_absolute_size(  self, size, ):

        
        libpango.pango_font_description_set_absolute_size( self._object,size )

    def merge(  self, desc_to_merge, replace_existing, ):
        if desc_to_merge: desc_to_merge = desc_to_merge._object
        else: desc_to_merge = POINTER(c_void_p)()

        
        libpango.pango_font_description_merge( self._object,desc_to_merge,replace_existing )

    def to_filename(  self, ):

        
        return libpango.pango_font_description_to_filename( self._object )

    def set_gravity(  self, gravity, ):

        
        libpango.pango_font_description_set_gravity( self._object,gravity )

    def get_variant(  self, ):

        
        return libpango.pango_font_description_get_variant( self._object )

    def free(  self, ):

        
        libpango.pango_font_description_free( self._object )

    @staticmethod
    def from_string( str,):
        from .gtk3 import PangoFontDescription
        return PangoFontDescription( obj=    libpango.pango_font_description_from_string(str, )
  or POINTER(c_void_p)())
