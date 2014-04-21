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

try:
    libgtk3.gtk_rc_set_default_files.restype = None
    libgtk3.gtk_rc_set_default_files.argtypes = [_GtkRcStyle,Asciifier]
except:
   pass
try:
    libgtk3.gtk_rc_parse.restype = None
    libgtk3.gtk_rc_parse.argtypes = [_GtkRcStyle,Asciifier]
except:
   pass
try:
    libgtk3.gtk_rc_style_copy.restype = _GtkRcStyle
    libgtk3.gtk_rc_style_copy.argtypes = [_GtkRcStyle]
except:
   pass
try:
    libgtk3.gtk_rc_reset_styles.restype = None
    libgtk3.gtk_rc_reset_styles.argtypes = [_GtkRcStyle,_GtkSettings]
except:
   pass
try:
    libgtk3.gtk_rc_parse_string.restype = None
    libgtk3.gtk_rc_parse_string.argtypes = [_GtkRcStyle,Asciifier]
except:
   pass
try:
    libgtk3.gtk_rc_add_default_file.restype = None
    libgtk3.gtk_rc_add_default_file.argtypes = [_GtkRcStyle,Asciifier]
except:
   pass
try:
    libgtk3.gtk_rc_parse_state.restype = guint
    libgtk3.gtk_rc_parse_state.argtypes = [_GScanner,POINTER(GtkStateType)]
except:
   pass
try:
    libgtk3.gtk_rc_get_default_files.restype = c_char_p
    libgtk3.gtk_rc_get_default_files.argtypes = []
except:
   pass
try:
    libgtk3.gtk_rc_get_im_module_file.restype = c_char_p
    libgtk3.gtk_rc_get_im_module_file.argtypes = []
except:
   pass
try:
    libgtk3.gtk_rc_parse_color.restype = guint
    libgtk3.gtk_rc_parse_color.argtypes = [_GScanner,_GdkColor]
except:
   pass
try:
    libgtk3.gtk_rc_get_im_module_path.restype = c_char_p
    libgtk3.gtk_rc_get_im_module_path.argtypes = []
except:
   pass
try:
    libgtk3.gtk_rc_parse_color_full.restype = guint
    libgtk3.gtk_rc_parse_color_full.argtypes = [_GScanner,_GtkRcStyle,_GdkColor]
except:
   pass
try:
    libgtk3.gtk_rc_find_module_in_path.restype = c_char_p
    libgtk3.gtk_rc_find_module_in_path.argtypes = [Asciifier]
except:
   pass
try:
    libgtk3.gtk_rc_parse_priority.restype = guint
    libgtk3.gtk_rc_parse_priority.argtypes = [_GScanner,_GtkPathPriorityType]
except:
   pass
try:
    libgtk3.gtk_rc_reparse_all_for_settings.restype = gboolean
    libgtk3.gtk_rc_reparse_all_for_settings.argtypes = [_GtkSettings,gboolean]
except:
   pass
try:
    libgtk3.gtk_rc_get_theme_dir.restype = c_char_p
    libgtk3.gtk_rc_get_theme_dir.argtypes = []
except:
   pass
try:
    libgtk3.gtk_rc_get_style_by_paths.restype = _GtkStyle
    libgtk3.gtk_rc_get_style_by_paths.argtypes = [_GtkSettings,Asciifier,Asciifier,GType]
except:
   pass
try:
    libgtk3.gtk_rc_reparse_all.restype = gboolean
    libgtk3.gtk_rc_reparse_all.argtypes = []
except:
   pass
try:
    libgtk3.gtk_rc_find_pixmap_in_path.restype = c_char_p
    libgtk3.gtk_rc_find_pixmap_in_path.argtypes = [_GtkSettings,_GScanner,Asciifier]
except:
   pass
try:
    libgtk3.gtk_rc_get_module_dir.restype = c_char_p
    libgtk3.gtk_rc_get_module_dir.argtypes = []
except:
   pass
try:
    libgtk3.gtk_rc_get_style.restype = _GtkStyle
    libgtk3.gtk_rc_get_style.argtypes = [_GtkWidget]
except:
   pass
from . import gobject__GObject
class GtkRcStyle( gobject__GObject.GObject):
    """Class GtkRcStyle Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_rc_style_new.restype = POINTER(c_void_p)
            
            libgtk3.gtk_rc_style_new.argtypes = []
            self._object = libgtk3.gtk_rc_style_new()

    """Methods"""
    def gtk_rc_set_default_files(  self, filenames, ):

        
        libgtk3.gtk_rc_set_default_files( self._object,filenames )

    def gtk_rc_parse(  self, filename, ):

        
        libgtk3.gtk_rc_parse( self._object,filename )

    def copy(  self, ):

        from .gtk3 import GtkRcStyle
        return GtkRcStyle( obj=libgtk3.gtk_rc_style_copy( self._object ) or POINTER(c_void_p)())

    def gtk_rc_reset_styles(  self, settings, ):
        if settings: settings = settings._object
        else: settings = POINTER(c_void_p)()

        
        libgtk3.gtk_rc_reset_styles( self._object,settings )

    def gtk_rc_parse_string(  self, rc_string, ):

        
        libgtk3.gtk_rc_parse_string( self._object,rc_string )

    def gtk_rc_add_default_file(  self, filename, ):

        
        libgtk3.gtk_rc_add_default_file( self._object,filename )

    @staticmethod
    def gtk_rc_parse_state( scanner, state,):
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_void_p)()
        
        return     libgtk3.gtk_rc_parse_state(scanner, state, )

    @staticmethod
    def gtk_rc_get_default_files():
        
        return     libgtk3.gtk_rc_get_default_files()

    @staticmethod
    def gtk_rc_get_im_module_file():
        
        return     libgtk3.gtk_rc_get_im_module_file()

    @staticmethod
    def gtk_rc_parse_color( scanner, color,):
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_void_p)()
        if color: color = color._object
        else: color = POINTER(c_void_p)()
        
        return     libgtk3.gtk_rc_parse_color(scanner, color, )

    @staticmethod
    def gtk_rc_get_im_module_path():
        
        return     libgtk3.gtk_rc_get_im_module_path()

    @staticmethod
    def gtk_rc_parse_color_full( scanner, style, color,):
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_void_p)()
        if style: style = style._object
        else: style = POINTER(c_void_p)()
        if color: color = color._object
        else: color = POINTER(c_void_p)()
        
        return     libgtk3.gtk_rc_parse_color_full(scanner, style, color, )

    @staticmethod
    def gtk_rc_find_module_in_path( module_file,):
        
        return     libgtk3.gtk_rc_find_module_in_path(module_file, )

    @staticmethod
    def gtk_rc_parse_priority( scanner, priority,):
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_void_p)()
        if priority: priority = priority._object
        else: priority = POINTER(c_void_p)()
        
        return     libgtk3.gtk_rc_parse_priority(scanner, priority, )

    @staticmethod
    def gtk_rc_reparse_all_for_settings( settings, force_load,):
        if settings: settings = settings._object
        else: settings = POINTER(c_void_p)()
        
        return     libgtk3.gtk_rc_reparse_all_for_settings(settings, force_load, )

    @staticmethod
    def gtk_rc_get_theme_dir():
        
        return     libgtk3.gtk_rc_get_theme_dir()

    @staticmethod
    def gtk_rc_get_style_by_paths( settings, widget_path, class_path, type,):
        if settings: settings = settings._object
        else: settings = POINTER(c_void_p)()
        from .gtk3 import GtkStyle
        return GtkStyle(None, obj=    libgtk3.gtk_rc_get_style_by_paths(settings, widget_path, class_path, type, )
 or POINTER(c_void_p)())
    @staticmethod
    def gtk_rc_reparse_all():
        
        return     libgtk3.gtk_rc_reparse_all()

    @staticmethod
    def gtk_rc_find_pixmap_in_path( settings, scanner, pixmap_file,):
        if settings: settings = settings._object
        else: settings = POINTER(c_void_p)()
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_void_p)()
        
        return     libgtk3.gtk_rc_find_pixmap_in_path(settings, scanner, pixmap_file, )

    @staticmethod
    def gtk_rc_get_module_dir():
        
        return     libgtk3.gtk_rc_get_module_dir()

    @staticmethod
    def gtk_rc_get_style( widget,):
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()
        from .gtk3 import GtkStyle
        return GtkStyle( obj=    libgtk3.gtk_rc_get_style(widget, )
 or POINTER(c_void_p)())
