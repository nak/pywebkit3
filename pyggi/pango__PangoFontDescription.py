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
from pango_types import *
from pango_enums import *

    
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
    libpango.pango_font_description_set_family_static.argtypes = [_PangoFontDescription,c_char_p]
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
    libpango.pango_font_description_set_family.argtypes = [_PangoFontDescription,c_char_p]
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
    libpango.pango_font_description_from_string.argtypes = [c_char_p]
except:
   pass
import gobject__GBoxed
class PangoFontDescription( gobject__GBoxed.GBoxed):
    """Class PangoFontDescription Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libpango.pango_font_description_new.restype = POINTER(c_int)
            
            libpango.pango_font_description_new.argtypes = []
            self._object = libpango.pango_font_description_new()

    """Methods"""
    def to_string(  self, ):

        
        return libpango.pango_font_description_to_string( self._object )

    def copy(  self, ):

        from gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libpango.pango_font_description_copy( self._object )  or POINTER(c_int)())

    def equal(  self, desc2, ):
        if desc2: desc2 = desc2._object
        else: desc2 = POINTER(c_int)()

        
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
        else: desc_to_merge = POINTER(c_int)()

        
        libpango.pango_font_description_merge_static( self._object,desc_to_merge,replace_existing )

    def better_match(  self, old_match, new_match, ):
        if old_match: old_match = old_match._object
        else: old_match = POINTER(c_int)()
        if new_match: new_match = new_match._object
        else: new_match = POINTER(c_int)()

        
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

        from gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libpango.pango_font_description_copy_static( self._object )  or POINTER(c_int)())

    def set_absolute_size(  self, size, ):

        
        libpango.pango_font_description_set_absolute_size( self._object,size )

    def merge(  self, desc_to_merge, replace_existing, ):
        if desc_to_merge: desc_to_merge = desc_to_merge._object
        else: desc_to_merge = POINTER(c_int)()

        
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
        from gtk3 import PangoFontDescription
        return PangoFontDescription( obj=    libpango.pango_font_description_from_string(str, )
  or POINTER(c_int)())
