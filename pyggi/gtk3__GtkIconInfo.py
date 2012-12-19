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
_WebKitNetworkResponse = POINTER(c_int)
_GtkLabel = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_cairo_matrix_t = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GClosure = POINTER(c_int)
_GIcon = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_void = POINTER(c_int)
_GtkIconInfo = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
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
_GtkIconSet = POINTER(c_int)
_GtkIconTheme = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAccelLabel = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_GdkPoint = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
_GScanner = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_GActionGroup = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkEventButton = POINTER(c_int)
_GCancellable = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GFile = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkPrintOperation = POINTER(c_int)
_GtkThemingEngine = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
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
_GdkScreen = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GByteArray = POINTER(c_int)
_GdkPixbufSimpleAnim = POINTER(c_int)
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
        else: style = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_load_symbolic_for_style( self._object,style,state,was_symbolic,error ) or POINTER(c_int)())

    def get_embedded_rect(  self, rectangle, ):
        if rectangle: rectangle = rectangle._object
        else: rectangle = POINTER(c_int)()

        
        return libgtk3.gtk_icon_info_get_embedded_rect( self._object,rectangle )

    def copy(  self, ):

        from gtk3 import GtkIconInfo
        return GtkIconInfo( obj=libgtk3.gtk_icon_info_copy( self._object ) or POINTER(c_int)())

    def get_filename(  self, ):

        
        return libgtk3.gtk_icon_info_get_filename( self._object )

    def get_builtin_pixbuf(  self, ):

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_get_builtin_pixbuf( self._object ) or POINTER(c_int)())

    def get_attach_points(  self, points, n_points, ):
        if points: points = points._object
        else: points = POINTER(c_int)()

        
        return libgtk3.gtk_icon_info_get_attach_points( self._object,points,n_points )

    def load_symbolic(  self, fg, success_color, warning_color, error_color, was_symbolic, error, ):
        if fg: fg = fg._object
        else: fg = POINTER(c_int)()
        if success_color: success_color = success_color._object
        else: success_color = POINTER(c_int)()
        if warning_color: warning_color = warning_color._object
        else: warning_color = POINTER(c_int)()
        if error_color: error_color = error_color._object
        else: error_color = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_load_symbolic( self._object,fg,success_color,warning_color,error_color,was_symbolic,error ) or POINTER(c_int)())

    def load_symbolic_for_context(  self, context, was_symbolic, error, ):
        if context: context = context._object
        else: context = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_load_symbolic_for_context( self._object,context,was_symbolic,error ) or POINTER(c_int)())

    def load_icon(  self, error, ):
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_info_load_icon( self._object,error ) or POINTER(c_int)())

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
        else: icon_theme = POINTER(c_int)()
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_int)()
        from gtk3 import GtkIconInfo
        return GtkIconInfo( obj=    libgtk3.gtk_icon_info_new_for_pixbuf(icon_theme, pixbuf, )
 or POINTER(c_int)())
