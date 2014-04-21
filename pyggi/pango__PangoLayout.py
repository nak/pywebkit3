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
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int

try:
    libpango.pango_layout_get_justify.restype = gboolean
    libpango.pango_layout_get_justify.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_unknown_glyphs_count.restype = int
    libpango.pango_layout_get_unknown_glyphs_count.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_height.restype = None
    libpango.pango_layout_set_height.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libpango.pango_layout_copy.restype = _PangoLayout
    libpango.pango_layout_copy.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_markup.restype = None
    libpango.pango_layout_set_markup.argtypes = [_PangoLayout,Asciifier,int]
except:
   pass
try:
    libpango.pango_layout_get_attributes.restype = _PangoAttrList
    libpango.pango_layout_get_attributes.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_context.restype = _PangoContext
    libpango.pango_layout_get_context.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_wrap.restype = None
    libpango.pango_layout_set_wrap.argtypes = [_PangoLayout,PangoWrapMode]
except:
   pass
try:
    libpango.pango_layout_get_alignment.restype = PangoAlignment
    libpango.pango_layout_get_alignment.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_index_to_pos.restype = None
    libpango.pango_layout_index_to_pos.argtypes = [_PangoLayout,int,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_move_cursor_visually.restype = None
    libpango.pango_layout_move_cursor_visually.argtypes = [_PangoLayout,gboolean,int,int,int,POINTER(int),POINTER(int)]
except:
   pass
try:
    libpango.pango_layout_get_indent.restype = int
    libpango.pango_layout_get_indent.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_single_paragraph_mode.restype = gboolean
    libpango.pango_layout_get_single_paragraph_mode.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_line_count.restype = int
    libpango.pango_layout_get_line_count.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_is_wrapped.restype = gboolean
    libpango.pango_layout_is_wrapped.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_pixel_size.restype = None
    libpango.pango_layout_get_pixel_size.argtypes = [_PangoLayout,POINTER(int),POINTER(int)]
except:
   pass
try:
    libpango.pango_layout_get_lines.restype = _GSList
    libpango.pango_layout_get_lines.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_ellipsize.restype = None
    libpango.pango_layout_set_ellipsize.argtypes = [_PangoLayout,PangoEllipsizeMode]
except:
   pass
try:
    libpango.pango_layout_get_cursor_pos.restype = None
    libpango.pango_layout_get_cursor_pos.argtypes = [_PangoLayout,int,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_get_wrap.restype = PangoWrapMode
    libpango.pango_layout_get_wrap.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_baseline.restype = int
    libpango.pango_layout_get_baseline.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_text.restype = None
    libpango.pango_layout_set_text.argtypes = [_PangoLayout,Asciifier,int]
except:
   pass
try:
    libpango.pango_layout_set_font_description.restype = None
    libpango.pango_layout_set_font_description.argtypes = [_PangoLayout,_PangoFontDescription]
except:
   pass
try:
    libpango.pango_layout_get_size.restype = None
    libpango.pango_layout_get_size.argtypes = [_PangoLayout,POINTER(int),POINTER(int)]
except:
   pass
try:
    libpango.pango_layout_set_spacing.restype = None
    libpango.pango_layout_set_spacing.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libpango.pango_layout_get_character_count.restype = gint
    libpango.pango_layout_get_character_count.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_log_attrs.restype = None
    libpango.pango_layout_get_log_attrs.argtypes = [_PangoLayout,_PangoLogAttr,POINTER(gint)]
except:
   pass
try:
    libpango.pango_layout_get_text.restype = c_char_p
    libpango.pango_layout_get_text.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_tabs.restype = _PangoTabArray
    libpango.pango_layout_get_tabs.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_extents.restype = None
    libpango.pango_layout_get_extents.argtypes = [_PangoLayout,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_xy_to_index.restype = gboolean
    libpango.pango_layout_xy_to_index.argtypes = [_PangoLayout,int,int,POINTER(int),POINTER(int)]
except:
   pass
try:
    libpango.pango_layout_get_height.restype = int
    libpango.pango_layout_get_height.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_single_paragraph_mode.restype = None
    libpango.pango_layout_set_single_paragraph_mode.argtypes = [_PangoLayout,gboolean]
except:
   pass
try:
    libpango.pango_layout_get_width.restype = int
    libpango.pango_layout_get_width.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_pixel_extents.restype = None
    libpango.pango_layout_get_pixel_extents.argtypes = [_PangoLayout,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_set_indent.restype = None
    libpango.pango_layout_set_indent.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libpango.pango_layout_get_line_readonly.restype = _PangoLayoutLine
    libpango.pango_layout_get_line_readonly.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libpango.pango_layout_set_attributes.restype = None
    libpango.pango_layout_set_attributes.argtypes = [_PangoLayout,_PangoAttrList]
except:
   pass
try:
    libpango.pango_layout_get_lines_readonly.restype = _GSList
    libpango.pango_layout_get_lines_readonly.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_context_changed.restype = None
    libpango.pango_layout_context_changed.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_tabs.restype = None
    libpango.pango_layout_set_tabs.argtypes = [_PangoLayout,_PangoTabArray]
except:
   pass
try:
    libpango.pango_layout_set_width.restype = None
    libpango.pango_layout_set_width.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libpango.pango_layout_get_log_attrs_readonly.restype = _PangoLogAttr
    libpango.pango_layout_get_log_attrs_readonly.argtypes = [_PangoLayout,POINTER(gint)]
except:
   pass
try:
    libpango.pango_layout_set_markup_with_accel.restype = None
    libpango.pango_layout_set_markup_with_accel.argtypes = [_PangoLayout,Asciifier,int,gunichar,_gunichar]
except:
   pass
try:
    libpango.pango_layout_get_auto_dir.restype = gboolean
    libpango.pango_layout_get_auto_dir.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_auto_dir.restype = None
    libpango.pango_layout_set_auto_dir.argtypes = [_PangoLayout,gboolean]
except:
   pass
try:
    libpango.pango_layout_get_font_description.restype = _PangoFontDescription
    libpango.pango_layout_get_font_description.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_line.restype = _PangoLayoutLine
    libpango.pango_layout_get_line.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libpango.pango_layout_index_to_line_x.restype = None
    libpango.pango_layout_index_to_line_x.argtypes = [_PangoLayout,int,gboolean,POINTER(int),POINTER(int)]
except:
   pass
try:
    libpango.pango_layout_is_ellipsized.restype = gboolean
    libpango.pango_layout_is_ellipsized.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_alignment.restype = None
    libpango.pango_layout_set_alignment.argtypes = [_PangoLayout,PangoAlignment]
except:
   pass
try:
    libpango.pango_layout_get_spacing.restype = int
    libpango.pango_layout_get_spacing.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_get_ellipsize.restype = PangoEllipsizeMode
    libpango.pango_layout_get_ellipsize.argtypes = [_PangoLayout]
except:
   pass
try:
    libpango.pango_layout_set_justify.restype = None
    libpango.pango_layout_set_justify.argtypes = [_PangoLayout,gboolean]
except:
   pass
from . import gobject__GObject
class PangoLayout( gobject__GObject.GObject):
    """Class PangoLayout Constructors"""
    def __init__( self, context,  obj = None):
        if obj: self._object = obj
        else:
            libpango.pango_layout_new.restype = POINTER(c_void_p)
            
            if context : context = context._object
            else :  context = POINTER(c_void_p)()

            libpango.pango_layout_new.argtypes = [_PangoContext]
            self._object = libpango.pango_layout_new(context, )

    """Methods"""
    def get_justify(  self, ):

        
        return libpango.pango_layout_get_justify( self._object )

    def get_unknown_glyphs_count(  self, ):

        
        return libpango.pango_layout_get_unknown_glyphs_count( self._object )

    def set_height(  self, height, ):

        
        libpango.pango_layout_set_height( self._object,height )

    def copy(  self, ):

        from .gtk3 import PangoLayout
        return PangoLayout( obj=libpango.pango_layout_copy( self._object )  or POINTER(c_void_p)())

    def set_markup(  self, markup, length, ):

        
        libpango.pango_layout_set_markup( self._object,markup,length )

    def get_attributes(  self, ):

        from .gtk3 import PangoAttrList
        return PangoAttrList( obj=libpango.pango_layout_get_attributes( self._object )  or POINTER(c_void_p)())

    def get_context(  self, ):

        from .gtk3 import PangoContext
        return PangoContext(None, obj=libpango.pango_layout_get_context( self._object )  or POINTER(c_void_p)())

    def set_wrap(  self, wrap, ):

        
        libpango.pango_layout_set_wrap( self._object,wrap )

    def get_alignment(  self, ):

        
        return libpango.pango_layout_get_alignment( self._object )

    def index_to_pos(  self, index_, pos, ):
        if pos: pos = pos._object
        else: pos = POINTER(c_void_p)()

        
        libpango.pango_layout_index_to_pos( self._object,index_,pos )

    def move_cursor_visually(  self, strong, old_index, old_trailing, direction, new_index, new_trailing, ):

        
        libpango.pango_layout_move_cursor_visually( self._object,strong,old_index,old_trailing,direction,new_index,new_trailing )

    def get_indent(  self, ):

        
        return libpango.pango_layout_get_indent( self._object )

    def get_single_paragraph_mode(  self, ):

        
        return libpango.pango_layout_get_single_paragraph_mode( self._object )

    def get_line_count(  self, ):

        
        return libpango.pango_layout_get_line_count( self._object )

    def is_wrapped(  self, ):

        
        return libpango.pango_layout_is_wrapped( self._object )

    def get_pixel_size(  self, width, height, ):

        
        libpango.pango_layout_get_pixel_size( self._object,width,height )

    def get_lines(  self, ):

        from .gobject import GSList
        return GSList( obj=libpango.pango_layout_get_lines( self._object ) or POINTER(c_void_p)())

    def set_ellipsize(  self, ellipsize, ):

        
        libpango.pango_layout_set_ellipsize( self._object,ellipsize )

    def get_cursor_pos(  self, index_, strong_pos, weak_pos, ):
        if strong_pos: strong_pos = strong_pos._object
        else: strong_pos = POINTER(c_void_p)()
        if weak_pos: weak_pos = weak_pos._object
        else: weak_pos = POINTER(c_void_p)()

        
        libpango.pango_layout_get_cursor_pos( self._object,index_,strong_pos,weak_pos )

    def get_wrap(  self, ):

        
        return libpango.pango_layout_get_wrap( self._object )

    def get_baseline(  self, ):

        
        return libpango.pango_layout_get_baseline( self._object )

    def set_text(  self, text, length, ):

        
        libpango.pango_layout_set_text( self._object,text,length )

    def set_font_description(  self, desc, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_void_p)()

        
        libpango.pango_layout_set_font_description( self._object,desc )

    def get_size(  self, width, height, ):

        
        libpango.pango_layout_get_size( self._object,width,height )

    def set_spacing(  self, spacing, ):

        
        libpango.pango_layout_set_spacing( self._object,spacing )

    def get_character_count(  self, ):

        
        return libpango.pango_layout_get_character_count( self._object )

    def get_log_attrs(  self, attrs, n_attrs, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_void_p)()

        
        libpango.pango_layout_get_log_attrs( self._object,attrs,n_attrs )

    def get_text(  self, ):

        
        return libpango.pango_layout_get_text( self._object )

    def get_tabs(  self, ):

        from .gtk3 import PangoTabArray
        return PangoTabArray( obj=libpango.pango_layout_get_tabs( self._object )  or POINTER(c_void_p)())

    def get_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_void_p)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_void_p)()

        
        libpango.pango_layout_get_extents( self._object,ink_rect,logical_rect )

    def xy_to_index(  self, x, y, index_, trailing, ):

        
        return libpango.pango_layout_xy_to_index( self._object,x,y,index_,trailing )

    def get_height(  self, ):

        
        return libpango.pango_layout_get_height( self._object )

    def set_single_paragraph_mode(  self, setting, ):

        
        libpango.pango_layout_set_single_paragraph_mode( self._object,setting )

    def get_width(  self, ):

        
        return libpango.pango_layout_get_width( self._object )

    def get_pixel_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_void_p)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_void_p)()

        
        libpango.pango_layout_get_pixel_extents( self._object,ink_rect,logical_rect )

    def set_indent(  self, indent, ):

        
        libpango.pango_layout_set_indent( self._object,indent )

    def get_line_readonly(  self, line, ):

        from .gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libpango.pango_layout_get_line_readonly( self._object,line )  or POINTER(c_void_p)())

    def set_attributes(  self, attrs, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_void_p)()

        
        libpango.pango_layout_set_attributes( self._object,attrs )

    def get_lines_readonly(  self, ):

        from .gobject import GSList
        return GSList( obj=libpango.pango_layout_get_lines_readonly( self._object ) or POINTER(c_void_p)())

    def context_changed(  self, ):

        
        libpango.pango_layout_context_changed( self._object )

    def set_tabs(  self, tabs, ):
        if tabs: tabs = tabs._object
        else: tabs = POINTER(c_void_p)()

        
        libpango.pango_layout_set_tabs( self._object,tabs )

    def set_width(  self, width, ):

        
        libpango.pango_layout_set_width( self._object,width )

    def get_log_attrs_readonly(  self, n_attrs, ):

        from .gtk3 import PangoLogAttr
        return PangoLogAttr( obj=libpango.pango_layout_get_log_attrs_readonly( self._object,n_attrs )  or POINTER(c_void_p)())

    def set_markup_with_accel(  self, markup, length, accel_marker, accel_char, ):
        if accel_marker: accel_marker = accel_marker._object
        else: accel_marker = POINTER(c_void_p)()
        if accel_char: accel_char = accel_char._object
        else: accel_char = POINTER(c_void_p)()

        
        libpango.pango_layout_set_markup_with_accel( self._object,markup,length,accel_marker,accel_char )

    def get_auto_dir(  self, ):

        
        return libpango.pango_layout_get_auto_dir( self._object )

    def set_auto_dir(  self, auto_dir, ):

        
        libpango.pango_layout_set_auto_dir( self._object,auto_dir )

    def get_font_description(  self, ):

        from .gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libpango.pango_layout_get_font_description( self._object )  or POINTER(c_void_p)())

    def get_line(  self, line, ):

        from .gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libpango.pango_layout_get_line( self._object,line )  or POINTER(c_void_p)())

    def index_to_line_x(  self, index_, trailing, line, x_pos, ):

        
        libpango.pango_layout_index_to_line_x( self._object,index_,trailing,line,x_pos )

    def is_ellipsized(  self, ):

        
        return libpango.pango_layout_is_ellipsized( self._object )

    def set_alignment(  self, alignment, ):

        
        libpango.pango_layout_set_alignment( self._object,alignment )

    def get_spacing(  self, ):

        
        return libpango.pango_layout_get_spacing( self._object )

    def get_ellipsize(  self, ):

        
        return libpango.pango_layout_get_ellipsize( self._object )

    def set_justify(  self, justify, ):

        
        libpango.pango_layout_set_justify( self._object,justify )

