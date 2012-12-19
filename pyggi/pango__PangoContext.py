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
_WebKitNetworkResponse = POINTER(c_int)
_GtkLabel = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
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

try:
    libpango.pango_find_paragraph_boundary.restype = None
    libpango.pango_find_paragraph_boundary.argtypes = [_PangoContext,c_char_p,gint,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libpango.pango_context_set_language.restype = None
    libpango.pango_context_set_language.argtypes = [_PangoContext,_PangoLanguage]
except:
   pass
try:
    libpango.pango_itemize.restype = _GList
    libpango.pango_itemize.argtypes = [_PangoContext,c_char_p,gint,gint,_PangoAttrList,_PangoAttrIterator]
except:
   pass
try:
    libpango.pango_shape_full.restype = None
    libpango.pango_shape_full.argtypes = [_PangoContext,c_char_p,gint,c_char_p,gint,_PangoAnalysis,_PangoGlyphString]
except:
   pass
try:
    libpango.pango_context_set_base_dir.restype = None
    libpango.pango_context_set_base_dir.argtypes = [_PangoContext,PangoDirection]
except:
   pass
try:
    libpango.pango_get_log_attrs.restype = None
    libpango.pango_get_log_attrs.argtypes = [_PangoContext,c_char_p,gint,gint,_PangoLanguage,_PangoLogAttr,gint]
except:
   pass
try:
    libpango.pango_context_set_matrix.restype = None
    libpango.pango_context_set_matrix.argtypes = [_PangoContext,_PangoMatrix]
except:
   pass
try:
    libpango.pango_context_get_matrix.restype = _PangoMatrix
    libpango.pango_context_get_matrix.argtypes = [_PangoContext]
except:
   pass
try:
    libpango.pango_context_set_font_description.restype = None
    libpango.pango_context_set_font_description.argtypes = [_PangoContext,_PangoFontDescription]
except:
   pass
try:
    libpango.pango_context_get_base_gravity.restype = PangoGravity
    libpango.pango_context_get_base_gravity.argtypes = [_PangoContext]
except:
   pass
try:
    libpango.pango_context_load_fontset.restype = _PangoFontset
    libpango.pango_context_load_fontset.argtypes = [_PangoContext,_PangoFontDescription,_PangoLanguage]
except:
   pass
try:
    libpango.pango_default_break.restype = None
    libpango.pango_default_break.argtypes = [_PangoContext,c_char_p,gint,_PangoAnalysis,_PangoLogAttr,gint]
except:
   pass
try:
    libpango.pango_context_set_base_gravity.restype = None
    libpango.pango_context_set_base_gravity.argtypes = [_PangoContext,PangoGravity]
except:
   pass
try:
    libpango.pango_itemize_with_base_dir.restype = _GList
    libpango.pango_itemize_with_base_dir.argtypes = [_PangoContext,PangoDirection,c_char_p,gint,gint,_PangoAttrList,_PangoAttrIterator]
except:
   pass
try:
    libpango.pango_context_list_families.restype = None
    libpango.pango_context_list_families.argtypes = [_PangoContext,POINTER(_PangoFontFamily),POINTER(gint)]
except:
   pass
try:
    libpango.pango_context_set_font_map.restype = None
    libpango.pango_context_set_font_map.argtypes = [_PangoContext,_PangoFontMap]
except:
   pass
try:
    libpango.pango_context_get_language.restype = _PangoLanguage
    libpango.pango_context_get_language.argtypes = [_PangoContext]
except:
   pass
try:
    libpango.pango_context_get_font_map.restype = _PangoFontMap
    libpango.pango_context_get_font_map.argtypes = [_PangoContext]
except:
   pass
try:
    libpango.pango_shape.restype = None
    libpango.pango_shape.argtypes = [_PangoContext,c_char_p,gint,_PangoAnalysis,_PangoGlyphString]
except:
   pass
try:
    libpango.pango_context_get_base_dir.restype = PangoDirection
    libpango.pango_context_get_base_dir.argtypes = [_PangoContext]
except:
   pass
try:
    libpango.pango_context_set_gravity_hint.restype = None
    libpango.pango_context_set_gravity_hint.argtypes = [_PangoContext,PangoGravityHint]
except:
   pass
try:
    libpango.pango_context_get_gravity.restype = PangoGravity
    libpango.pango_context_get_gravity.argtypes = [_PangoContext]
except:
   pass
try:
    libpango.pango_context_get_font_description.restype = _PangoFontDescription
    libpango.pango_context_get_font_description.argtypes = [_PangoContext]
except:
   pass
try:
    libpango.pango_context_get_metrics.restype = _PangoFontMetrics
    libpango.pango_context_get_metrics.argtypes = [_PangoContext,_PangoFontDescription,_PangoLanguage]
except:
   pass
try:
    libpango.pango_context_get_gravity_hint.restype = PangoGravityHint
    libpango.pango_context_get_gravity_hint.argtypes = [_PangoContext]
except:
   pass
try:
    libpango.pango_break.restype = None
    libpango.pango_break.argtypes = [_PangoContext,c_char_p,gint,_PangoAnalysis,_PangoLogAttr,gint]
except:
   pass
try:
    libpango.pango_context_load_font.restype = _PangoFont
    libpango.pango_context_load_font.argtypes = [_PangoContext,_PangoFontDescription]
except:
   pass
try:
    libpango.pango_reorder_items.restype = _GList
    libpango.pango_reorder_items.argtypes = [_GList]
except:
   pass
import gobject__GObject
class PangoContext( gobject__GObject.GObject):
    """Class PangoContext Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libpango.pango_context_new.restype = POINTER(c_int)
            
            libpango.pango_context_new.argtypes = []
            self._object = libpango.pango_context_new()

    """Methods"""
    def pango_find_paragraph_boundary(  self, text, length, paragraph_delimiter_index, next_paragraph_start, ):

        
        libpango.pango_find_paragraph_boundary( self._object,text,length,paragraph_delimiter_index,next_paragraph_start )

    def set_language(  self, language, ):
        if language: language = language._object
        else: language = POINTER(c_int)()

        
        libpango.pango_context_set_language( self._object,language )

    def pango_itemize(  self, text, start_index, length, attrs, cached_iter, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()
        if cached_iter: cached_iter = cached_iter._object
        else: cached_iter = POINTER(c_int)()

        from gobject import GList
        return GList( obj=libpango.pango_itemize( self._object,text,start_index,length,attrs,cached_iter ) or POINTER(c_int)())

    def pango_shape_full(  self, item_text, item_length, paragraph_text, paragraph_length, analysis, glyphs, ):
        if analysis: analysis = analysis._object
        else: analysis = POINTER(c_int)()
        if glyphs: glyphs = glyphs._object
        else: glyphs = POINTER(c_int)()

        
        libpango.pango_shape_full( self._object,item_text,item_length,paragraph_text,paragraph_length,analysis,glyphs )

    def set_base_dir(  self, direction, ):

        
        libpango.pango_context_set_base_dir( self._object,direction )

    def pango_get_log_attrs(  self, text, length, level, language, log_attrs, attrs_len, ):
        if language: language = language._object
        else: language = POINTER(c_int)()
        if log_attrs: log_attrs = log_attrs._object
        else: log_attrs = POINTER(c_int)()

        
        libpango.pango_get_log_attrs( self._object,text,length,level,language,log_attrs,attrs_len )

    def set_matrix(  self, matrix, ):
        if matrix: matrix = matrix._object
        else: matrix = POINTER(c_int)()

        
        libpango.pango_context_set_matrix( self._object,matrix )

    def get_matrix(  self, ):

        from gtk3 import PangoMatrix
        return PangoMatrix( obj=libpango.pango_context_get_matrix( self._object )  or POINTER(c_int)())

    def set_font_description(  self, desc, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()

        
        libpango.pango_context_set_font_description( self._object,desc )

    def get_base_gravity(  self, ):

        
        return libpango.pango_context_get_base_gravity( self._object )

    def load_fontset(  self, desc, language, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()
        if language: language = language._object
        else: language = POINTER(c_int)()

        from gtk3 import PangoFontset
        return PangoFontset( obj=libpango.pango_context_load_fontset( self._object,desc,language )  or POINTER(c_int)())

    def pango_default_break(  self, text, length, analysis, attrs, attrs_len, ):
        if analysis: analysis = analysis._object
        else: analysis = POINTER(c_int)()
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        
        libpango.pango_default_break( self._object,text,length,analysis,attrs,attrs_len )

    def set_base_gravity(  self, gravity, ):

        
        libpango.pango_context_set_base_gravity( self._object,gravity )

    def pango_itemize_with_base_dir(  self, base_dir, text, start_index, length, attrs, cached_iter, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()
        if cached_iter: cached_iter = cached_iter._object
        else: cached_iter = POINTER(c_int)()

        from gobject import GList
        return GList( obj=libpango.pango_itemize_with_base_dir( self._object,base_dir,text,start_index,length,attrs,cached_iter ) or POINTER(c_int)())

    def list_families(  self, families, n_families, ):
        if families: families = families._object
        else: families = POINTER(c_int)()

        
        libpango.pango_context_list_families( self._object,families,n_families )

    def set_font_map(  self, font_map, ):
        if font_map: font_map = font_map._object
        else: font_map = POINTER(c_int)()

        
        libpango.pango_context_set_font_map( self._object,font_map )

    def get_language(  self, ):

        from gtk3 import PangoLanguage
        return PangoLanguage( obj=libpango.pango_context_get_language( self._object )  or POINTER(c_int)())

    def get_font_map(  self, ):

        from gtk3 import PangoFontMap
        return PangoFontMap( obj=libpango.pango_context_get_font_map( self._object )  or POINTER(c_int)())

    def pango_shape(  self, text, length, analysis, glyphs, ):
        if analysis: analysis = analysis._object
        else: analysis = POINTER(c_int)()
        if glyphs: glyphs = glyphs._object
        else: glyphs = POINTER(c_int)()

        
        libpango.pango_shape( self._object,text,length,analysis,glyphs )

    def get_base_dir(  self, ):

        
        return libpango.pango_context_get_base_dir( self._object )

    def set_gravity_hint(  self, hint, ):

        
        libpango.pango_context_set_gravity_hint( self._object,hint )

    def get_gravity(  self, ):

        
        return libpango.pango_context_get_gravity( self._object )

    def get_font_description(  self, ):

        from gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libpango.pango_context_get_font_description( self._object )  or POINTER(c_int)())

    def get_metrics(  self, desc, language, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()
        if language: language = language._object
        else: language = POINTER(c_int)()

        from gtk3 import PangoFontMetrics
        return PangoFontMetrics( obj=libpango.pango_context_get_metrics( self._object,desc,language )  or POINTER(c_int)())

    def get_gravity_hint(  self, ):

        
        return libpango.pango_context_get_gravity_hint( self._object )

    def pango_break(  self, text, length, analysis, attrs, attrs_len, ):
        if analysis: analysis = analysis._object
        else: analysis = POINTER(c_int)()
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        
        libpango.pango_break( self._object,text,length,analysis,attrs,attrs_len )

    def load_font(  self, desc, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()

        from gtk3 import PangoFont
        return PangoFont( obj=libpango.pango_context_load_font( self._object,desc )  or POINTER(c_int)())

    @staticmethod
    def pango_reorder_items( logical_items,):
        if logical_items: logical_items = logical_items._object
        else: logical_items = POINTER(c_int)()
        from gobject import GList
        return GList( obj=    libpango.pango_reorder_items(logical_items, )
 or POINTER(c_int)())
