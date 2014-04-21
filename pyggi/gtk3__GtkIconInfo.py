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
_WebKitNetworkResponse = POINTER(c_void_p)
_GtkLabel = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_cairo_matrix_t = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_GtkIconFactory = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GdkTimeCoord = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GClosure = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_GtkDialog = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_void = POINTER(c_void_p)
_GtkIconInfo = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GBytes = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
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
_GtkIconSet = POINTER(c_void_p)
_GtkIconTheme = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_GtkAccelLabel = POINTER(c_void_p)
_JSGlobalContext = POINTER(c_void_p)
_GApplication = POINTER(c_void_p)
_GFileMonitor = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_WebKitHitTestResult = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
_GtkPathPriorityType = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_GdkPoint = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitWebInspector = POINTER(c_void_p)
_GOptionGroup = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_GtkWidgetClass = POINTER(c_void_p)
_GdkEventKey = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_PangoFontMetrics = POINTER(c_void_p)
_cairo_surface_t = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_WebKitWebFrame = POINTER(c_void_p)
_GActionGroup = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_WebKitNetworkRequest = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoLayoutRun = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_WebKitViewportAttributes = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_cairo_t = POINTER(c_void_p)
_GWeakRef = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GdkEventButton = POINTER(c_void_p)
_GCancellable = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_PangoRectangle = POINTER(c_void_p)
_GtkAccelGroup = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GFile = POINTER(c_void_p)
_GtkAllocation = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_PangoLayoutLine = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitDOMDocument = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkPrintOperation = POINTER(c_void_p)
_GtkThemingEngine = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_SoupMessage = POINTER(c_void_p)
_WebKitWebDataSource = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_gunichar = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_WebKitDOMNode = POINTER(c_void_p)
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
_GdkScreen = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GByteArray = POINTER(c_void_p)
_GdkPixbufSimpleAnim = POINTER(c_void_p)
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

try:
    libgtk3.gtk_icon_info_load_symbolic_for_style.restype = _GdkPixbuf
    libgtk3.gtk_icon_info_load_symbolic_for_style.argtypes = [_GtkIconInfo,_GtkStyle,GtkStateType,POINTER(gboolean),_GError]
except:
   pass
try:
    libgtk3.gtk_icon_info_get_embedded_rect.restype = gboolean
    libgtk3.gtk_icon_info_get_embedded_rect.argtypes = [_GtkIconInfo,_GdkRectangle]
except:
   pass
try:
    libgtk3.gtk_icon_info_copy.restype = _GtkIconInfo
    libgtk3.gtk_icon_info_copy.argtypes = [_GtkIconInfo]
except:
   pass
try:
    libgtk3.gtk_icon_info_get_filename.restype = c_char_p
    libgtk3.gtk_icon_info_get_filename.argtypes = [_GtkIconInfo]
except:
   pass
try:
    libgtk3.gtk_icon_info_get_builtin_pixbuf.restype = _GdkPixbuf
    libgtk3.gtk_icon_info_get_builtin_pixbuf.argtypes = [_GtkIconInfo]
except:
   pass
try:
    libgtk3.gtk_icon_info_get_attach_points.restype = gboolean
    libgtk3.gtk_icon_info_get_attach_points.argtypes = [_GtkIconInfo,_GdkPoint,POINTER(gint)]
except:
   pass
try:
    libgtk3.gtk_icon_info_load_symbolic.restype = _GdkPixbuf
    libgtk3.gtk_icon_info_load_symbolic.argtypes = [_GtkIconInfo,_GdkRGBA,_GdkRGBA,_GdkRGBA,_GdkRGBA,POINTER(gboolean),_GError]
except:
   pass
try:
    libgtk3.gtk_icon_info_load_symbolic_for_context.restype = _GdkPixbuf
    libgtk3.gtk_icon_info_load_symbolic_for_context.argtypes = [_GtkIconInfo,_GtkStyleContext,POINTER(gboolean),_GError]
except:
   pass
try:
    libgtk3.gtk_icon_info_load_icon.restype = _GdkPixbuf
    libgtk3.gtk_icon_info_load_icon.argtypes = [_GtkIconInfo,_GError]
except:
   pass
try:
    libgtk3.gtk_icon_info_set_raw_coordinates.restype = None
    libgtk3.gtk_icon_info_set_raw_coordinates.argtypes = [_GtkIconInfo,gboolean]
except:
   pass
try:
    libgtk3.gtk_icon_info_get_base_size.restype = gint
    libgtk3.gtk_icon_info_get_base_size.argtypes = [_GtkIconInfo]
except:
   pass
try:
    libgtk3.gtk_icon_info_get_display_name.restype = c_char_p
    libgtk3.gtk_icon_info_get_display_name.argtypes = [_GtkIconInfo]
except:
   pass
try:
    libgtk3.gtk_icon_info_free.restype = None
    libgtk3.gtk_icon_info_free.argtypes = [_GtkIconInfo]
except:
   pass
try:
    libgtk3.gtk_icon_info_new_for_pixbuf.restype = _GtkIconInfo
    libgtk3.gtk_icon_info_new_for_pixbuf.argtypes = [_GtkIconTheme,_GdkPixbuf]
except:
   pass
class GtkIconInfo( object):
    """Class GtkIconInfo Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def load_symbolic_for_style(  self, style, state, was_symbolic, error, ):
        if style: style = style._object
        else: style = POINTER(c_void_p)()
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_load_symbolic_for_style( self._object,style,state,was_symbolic,error ) or POINTER(c_void_p)())

    def get_embedded_rect(  self, rectangle, ):
        if rectangle: rectangle = rectangle._object
        else: rectangle = POINTER(c_void_p)()

        
        return libgtk3.gtk_icon_info_get_embedded_rect( self._object,rectangle )

    def copy(  self, ):

        from .gtk3 import GtkIconInfo
        return GtkIconInfo( obj=libgtk3.gtk_icon_info_copy( self._object ) or POINTER(c_void_p)())

    def get_filename(  self, ):

        
        return libgtk3.gtk_icon_info_get_filename( self._object )

    def get_builtin_pixbuf(  self, ):

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_get_builtin_pixbuf( self._object ) or POINTER(c_void_p)())

    def get_attach_points(  self, points, n_points, ):
        if points: points = points._object
        else: points = POINTER(c_void_p)()

        
        return libgtk3.gtk_icon_info_get_attach_points( self._object,points,n_points )

    def load_symbolic(  self, fg, success_color, warning_color, error_color, was_symbolic, error, ):
        if fg: fg = fg._object
        else: fg = POINTER(c_void_p)()
        if success_color: success_color = success_color._object
        else: success_color = POINTER(c_void_p)()
        if warning_color: warning_color = warning_color._object
        else: warning_color = POINTER(c_void_p)()
        if error_color: error_color = error_color._object
        else: error_color = POINTER(c_void_p)()
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_load_symbolic( self._object,fg,success_color,warning_color,error_color,was_symbolic,error ) or POINTER(c_void_p)())

    def load_symbolic_for_context(  self, context, was_symbolic, error, ):
        if context: context = context._object
        else: context = POINTER(c_void_p)()
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_load_symbolic_for_context( self._object,context,was_symbolic,error ) or POINTER(c_void_p)())

    def load_icon(  self, error, ):
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_load_icon( self._object,error ) or POINTER(c_void_p)())

    def set_raw_coordinates(  self, raw_coordinates, ):

        
        libgtk3.gtk_icon_info_set_raw_coordinates( self._object,raw_coordinates )

    def get_base_size(  self, ):

        
        return libgtk3.gtk_icon_info_get_base_size( self._object )

    def get_display_name(  self, ):

        
        return libgtk3.gtk_icon_info_get_display_name( self._object )

    def free(  self, ):

        
        libgtk3.gtk_icon_info_free( self._object )

    @staticmethod
    def new_for_pixbuf( icon_theme, pixbuf,):
        if icon_theme: icon_theme = icon_theme._object
        else: icon_theme = POINTER(c_void_p)()
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_void_p)()
        from .gtk3 import GtkIconInfo
        return GtkIconInfo( obj=    libgtk3.gtk_icon_info_new_for_pixbuf(icon_theme, pixbuf, )
 or POINTER(c_void_p)())
