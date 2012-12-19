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
GtkRcFlags = c_int
GtkRcTokenType = c_int

try:
    libgtk3.gtk_rc_set_default_files.restype = None
    libgtk3.gtk_rc_set_default_files.argtypes = [_GtkRcStyle,c_char_p]
except:
   pass
try:
    libgtk3.gtk_rc_parse.restype = None
    libgtk3.gtk_rc_parse.argtypes = [_GtkRcStyle,c_char_p]
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
    libgtk3.gtk_rc_parse_string.argtypes = [_GtkRcStyle,c_char_p]
except:
   pass
try:
    libgtk3.gtk_rc_add_default_file.restype = None
    libgtk3.gtk_rc_add_default_file.argtypes = [_GtkRcStyle,c_char_p]
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
    libgtk3.gtk_rc_find_module_in_path.argtypes = [c_char_p]
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
    libgtk3.gtk_rc_get_style_by_paths.argtypes = [_GtkSettings,c_char_p,c_char_p,GType]
except:
   pass
try:
    libgtk3.gtk_rc_reparse_all.restype = gboolean
    libgtk3.gtk_rc_reparse_all.argtypes = []
except:
   pass
try:
    libgtk3.gtk_rc_find_pixmap_in_path.restype = c_char_p
    libgtk3.gtk_rc_find_pixmap_in_path.argtypes = [_GtkSettings,_GScanner,c_char_p]
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
import gobject__GObject
class GtkRcStyle( gobject__GObject.GObject):
    """Class GtkRcStyle Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_rc_style_new.restype = POINTER(c_int)
            
            libgtk3.gtk_rc_style_new.argtypes = []
            self._object = libgtk3.gtk_rc_style_new()

    """Methods"""
    def gtk_rc_set_default_files(  self, filenames, ):

        
        libgtk3.gtk_rc_set_default_files( self._object,filenames )

    def gtk_rc_parse(  self, filename, ):

        
        libgtk3.gtk_rc_parse( self._object,filename )

    def copy(  self, ):

        from gtk3 import GtkRcStyle
        return GtkRcStyle( obj=libgtk3.gtk_rc_style_copy( self._object ) or POINTER(c_int)())

    def gtk_rc_reset_styles(  self, settings, ):
        if settings: settings = settings._object
        else: settings = POINTER(c_int)()

        
        libgtk3.gtk_rc_reset_styles( self._object,settings )

    def gtk_rc_parse_string(  self, rc_string, ):

        
        libgtk3.gtk_rc_parse_string( self._object,rc_string )

    def gtk_rc_add_default_file(  self, filename, ):

        
        libgtk3.gtk_rc_add_default_file( self._object,filename )

    @staticmethod
    def gtk_rc_parse_state( scanner, state,):
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_int)()
        
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
        else: scanner = POINTER(c_int)()
        if color: color = color._object
        else: color = POINTER(c_int)()
        
        return     libgtk3.gtk_rc_parse_color(scanner, color, )

    @staticmethod
    def gtk_rc_get_im_module_path():
        
        return     libgtk3.gtk_rc_get_im_module_path()

    @staticmethod
    def gtk_rc_parse_color_full( scanner, style, color,):
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_int)()
        if style: style = style._object
        else: style = POINTER(c_int)()
        if color: color = color._object
        else: color = POINTER(c_int)()
        
        return     libgtk3.gtk_rc_parse_color_full(scanner, style, color, )

    @staticmethod
    def gtk_rc_find_module_in_path( module_file,):
        
        return     libgtk3.gtk_rc_find_module_in_path(module_file, )

    @staticmethod
    def gtk_rc_parse_priority( scanner, priority,):
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_int)()
        if priority: priority = priority._object
        else: priority = POINTER(c_int)()
        
        return     libgtk3.gtk_rc_parse_priority(scanner, priority, )

    @staticmethod
    def gtk_rc_reparse_all_for_settings( settings, force_load,):
        if settings: settings = settings._object
        else: settings = POINTER(c_int)()
        
        return     libgtk3.gtk_rc_reparse_all_for_settings(settings, force_load, )

    @staticmethod
    def gtk_rc_get_theme_dir():
        
        return     libgtk3.gtk_rc_get_theme_dir()

    @staticmethod
    def gtk_rc_get_style_by_paths( settings, widget_path, class_path, type,):
        if settings: settings = settings._object
        else: settings = POINTER(c_int)()
        from gtk3 import GtkStyle
        return GtkStyle(None, obj=    libgtk3.gtk_rc_get_style_by_paths(settings, widget_path, class_path, type, )
 or POINTER(c_int)())
    @staticmethod
    def gtk_rc_reparse_all():
        
        return     libgtk3.gtk_rc_reparse_all()

    @staticmethod
    def gtk_rc_find_pixmap_in_path( settings, scanner, pixmap_file,):
        if settings: settings = settings._object
        else: settings = POINTER(c_int)()
        if scanner: scanner = scanner._object
        else: scanner = POINTER(c_int)()
        
        return     libgtk3.gtk_rc_find_pixmap_in_path(settings, scanner, pixmap_file, )

    @staticmethod
    def gtk_rc_get_module_dir():
        
        return     libgtk3.gtk_rc_get_module_dir()

    @staticmethod
    def gtk_rc_get_style( widget,):
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        from gtk3 import GtkStyle
        return GtkStyle( obj=    libgtk3.gtk_rc_get_style(widget, )
 or POINTER(c_int)())
