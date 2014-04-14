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
_WebKitWebWindowFeatures = POINTER(c_int)
_void = POINTER(c_int)
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
_PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
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
_cairo_region_t = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
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

try:
    libgtk3.gtk_label_set_attributes.restype = None
    libgtk3.gtk_label_set_attributes.argtypes = [_GtkLabel,_PangoAttrList]
except:
   pass
try:
    libgtk3.gtk_label_get_line_wrap_mode.restype = PangoWrapMode
    libgtk3.gtk_label_get_line_wrap_mode.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_use_underline.restype = None
    libgtk3.gtk_label_set_use_underline.argtypes = [_GtkLabel,gboolean]
except:
   pass
try:
    libgtk3.gtk_label_get_selectable.restype = gboolean
    libgtk3.gtk_label_get_selectable.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_single_line_mode.restype = None
    libgtk3.gtk_label_set_single_line_mode.argtypes = [_GtkLabel,gboolean]
except:
   pass
try:
    libgtk3.gtk_label_get_mnemonic_keyval.restype = guint
    libgtk3.gtk_label_get_mnemonic_keyval.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_text_with_mnemonic.restype = None
    libgtk3.gtk_label_set_text_with_mnemonic.argtypes = [_GtkLabel,Asciifier]
except:
   pass
try:
    libgtk3.gtk_label_get_track_visited_links.restype = gboolean
    libgtk3.gtk_label_get_track_visited_links.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_get_mnemonic_widget.restype = _GtkWidget
    libgtk3.gtk_label_get_mnemonic_widget.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_get_ellipsize.restype = PangoEllipsizeMode
    libgtk3.gtk_label_get_ellipsize.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_get_text.restype = c_char_p
    libgtk3.gtk_label_get_text.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_get_attributes.restype = _PangoAttrList
    libgtk3.gtk_label_get_attributes.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_label.restype = None
    libgtk3.gtk_label_set_label.argtypes = [_GtkLabel,Asciifier]
except:
   pass
try:
    libgtk3.gtk_label_get_max_width_chars.restype = gint
    libgtk3.gtk_label_get_max_width_chars.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_use_markup.restype = None
    libgtk3.gtk_label_set_use_markup.argtypes = [_GtkLabel,gboolean]
except:
   pass
try:
    libgtk3.gtk_label_get_label.restype = c_char_p
    libgtk3.gtk_label_get_label.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_get_line_wrap.restype = gboolean
    libgtk3.gtk_label_get_line_wrap.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_get_width_chars.restype = gint
    libgtk3.gtk_label_get_width_chars.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_markup_with_mnemonic.restype = None
    libgtk3.gtk_label_set_markup_with_mnemonic.argtypes = [_GtkLabel,Asciifier]
except:
   pass
try:
    libgtk3.gtk_label_set_text.restype = None
    libgtk3.gtk_label_set_text.argtypes = [_GtkLabel,Asciifier]
except:
   pass
try:
    libgtk3.gtk_label_set_ellipsize.restype = None
    libgtk3.gtk_label_set_ellipsize.argtypes = [_GtkLabel,PangoEllipsizeMode]
except:
   pass
try:
    libgtk3.gtk_label_get_current_uri.restype = c_char_p
    libgtk3.gtk_label_get_current_uri.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_get_angle.restype = gdouble
    libgtk3.gtk_label_get_angle.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_get_selection_bounds.restype = gboolean
    libgtk3.gtk_label_get_selection_bounds.argtypes = [_GtkLabel,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gtk_label_get_layout.restype = _PangoLayout
    libgtk3.gtk_label_get_layout.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_justify.restype = None
    libgtk3.gtk_label_set_justify.argtypes = [_GtkLabel,GtkJustification]
except:
   pass
try:
    libgtk3.gtk_label_set_max_width_chars.restype = None
    libgtk3.gtk_label_set_max_width_chars.argtypes = [_GtkLabel,gint]
except:
   pass
try:
    libgtk3.gtk_label_get_layout_offsets.restype = None
    libgtk3.gtk_label_get_layout_offsets.argtypes = [_GtkLabel,POINTER(gint),POINTER(gint)]
except:
   pass
try:
    libgtk3.gtk_label_get_use_markup.restype = gboolean
    libgtk3.gtk_label_get_use_markup.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_line_wrap.restype = None
    libgtk3.gtk_label_set_line_wrap.argtypes = [_GtkLabel,gboolean]
except:
   pass
try:
    libgtk3.gtk_label_get_justify.restype = GtkJustification
    libgtk3.gtk_label_get_justify.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_width_chars.restype = None
    libgtk3.gtk_label_set_width_chars.argtypes = [_GtkLabel,gint]
except:
   pass
try:
    libgtk3.gtk_label_set_mnemonic_widget.restype = None
    libgtk3.gtk_label_set_mnemonic_widget.argtypes = [_GtkLabel,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_label_get_use_underline.restype = gboolean
    libgtk3.gtk_label_get_use_underline.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_select_region.restype = None
    libgtk3.gtk_label_select_region.argtypes = [_GtkLabel,gint,gint]
except:
   pass
try:
    libgtk3.gtk_label_set_selectable.restype = None
    libgtk3.gtk_label_set_selectable.argtypes = [_GtkLabel,gboolean]
except:
   pass
try:
    libgtk3.gtk_label_set_line_wrap_mode.restype = None
    libgtk3.gtk_label_set_line_wrap_mode.argtypes = [_GtkLabel,PangoWrapMode]
except:
   pass
try:
    libgtk3.gtk_label_set_angle.restype = None
    libgtk3.gtk_label_set_angle.argtypes = [_GtkLabel,gdouble]
except:
   pass
try:
    libgtk3.gtk_label_get_single_line_mode.restype = gboolean
    libgtk3.gtk_label_get_single_line_mode.argtypes = [_GtkLabel]
except:
   pass
try:
    libgtk3.gtk_label_set_pattern.restype = None
    libgtk3.gtk_label_set_pattern.argtypes = [_GtkLabel,Asciifier]
except:
   pass
try:
    libgtk3.gtk_label_set_markup.restype = None
    libgtk3.gtk_label_set_markup.argtypes = [_GtkLabel,Asciifier]
except:
   pass
try:
    libgtk3.gtk_label_set_track_visited_links.restype = None
    libgtk3.gtk_label_set_track_visited_links.argtypes = [_GtkLabel,gboolean]
except:
   pass
try:
    libgtk3.gtk_label_new_with_mnemonic.restype = _GtkWidget
    libgtk3.gtk_label_new_with_mnemonic.argtypes = [Asciifier]
except:
   pass
from . import gtk3__GtkMisc
class GtkLabel( gtk3__GtkMisc.GtkMisc):
    """Class GtkLabel Constructors"""
    def __init__( self, str,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_label_new.restype = POINTER(c_int)
            
            libgtk3.gtk_label_new.argtypes = [Asciifier]
            self._object = libgtk3.gtk_label_new(str, )

    """Methods"""
    def set_attributes(  self, attrs, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        
        libgtk3.gtk_label_set_attributes( self._object,attrs )

    def get_line_wrap_mode(  self, ):

        
        return libgtk3.gtk_label_get_line_wrap_mode( self._object )

    def set_use_underline(  self, setting, ):

        
        libgtk3.gtk_label_set_use_underline( self._object,setting )

    def get_selectable(  self, ):

        
        return libgtk3.gtk_label_get_selectable( self._object )

    def set_single_line_mode(  self, single_line_mode, ):

        
        libgtk3.gtk_label_set_single_line_mode( self._object,single_line_mode )

    def get_mnemonic_keyval(  self, ):

        
        return libgtk3.gtk_label_get_mnemonic_keyval( self._object )

    def set_text_with_mnemonic(  self, str, ):

        
        libgtk3.gtk_label_set_text_with_mnemonic( self._object,str )

    def get_track_visited_links(  self, ):

        
        return libgtk3.gtk_label_get_track_visited_links( self._object )

    def get_mnemonic_widget(  self, ):

        from .gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_label_get_mnemonic_widget( self._object ) or POINTER(c_int)())

    def get_ellipsize(  self, ):

        
        return libgtk3.gtk_label_get_ellipsize( self._object )

    def get_text(  self, ):

        
        return libgtk3.gtk_label_get_text( self._object )

    def get_attributes(  self, ):

        from .gtk3 import PangoAttrList
        return PangoAttrList( obj=libgtk3.gtk_label_get_attributes( self._object )  or POINTER(c_int)())

    def set_label(  self, str, ):

        
        libgtk3.gtk_label_set_label( self._object,str )

    def get_max_width_chars(  self, ):

        
        return libgtk3.gtk_label_get_max_width_chars( self._object )

    def set_use_markup(  self, setting, ):

        
        libgtk3.gtk_label_set_use_markup( self._object,setting )

    def get_label(  self, ):

        
        return libgtk3.gtk_label_get_label( self._object )

    def get_line_wrap(  self, ):

        
        return libgtk3.gtk_label_get_line_wrap( self._object )

    def get_width_chars(  self, ):

        
        return libgtk3.gtk_label_get_width_chars( self._object )

    def set_markup_with_mnemonic(  self, str, ):

        
        libgtk3.gtk_label_set_markup_with_mnemonic( self._object,str )

    def set_text(  self, str, ):

        
        libgtk3.gtk_label_set_text( self._object,str )

    def set_ellipsize(  self, mode, ):

        
        libgtk3.gtk_label_set_ellipsize( self._object,mode )

    def get_current_uri(  self, ):

        
        return libgtk3.gtk_label_get_current_uri( self._object )

    def get_angle(  self, ):

        
        return libgtk3.gtk_label_get_angle( self._object )

    def get_selection_bounds(  self, start, end, ):

        
        return libgtk3.gtk_label_get_selection_bounds( self._object,start,end )

    def get_layout(  self, ):

        from .gtk3 import PangoLayout
        return PangoLayout(None,None, obj=libgtk3.gtk_label_get_layout( self._object )  or POINTER(c_int)())

    def set_justify(  self, jtype, ):

        
        libgtk3.gtk_label_set_justify( self._object,jtype )

    def set_max_width_chars(  self, n_chars, ):

        
        libgtk3.gtk_label_set_max_width_chars( self._object,n_chars )

    def get_layout_offsets(  self, x, y, ):

        
        libgtk3.gtk_label_get_layout_offsets( self._object,x,y )

    def get_use_markup(  self, ):

        
        return libgtk3.gtk_label_get_use_markup( self._object )

    def set_line_wrap(  self, wrap, ):

        
        libgtk3.gtk_label_set_line_wrap( self._object,wrap )

    def get_justify(  self, ):

        
        return libgtk3.gtk_label_get_justify( self._object )

    def set_width_chars(  self, n_chars, ):

        
        libgtk3.gtk_label_set_width_chars( self._object,n_chars )

    def set_mnemonic_widget(  self, widget, ):
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        libgtk3.gtk_label_set_mnemonic_widget( self._object,widget )

    def get_use_underline(  self, ):

        
        return libgtk3.gtk_label_get_use_underline( self._object )

    def select_region(  self, start_offset, end_offset, ):

        
        libgtk3.gtk_label_select_region( self._object,start_offset,end_offset )

    def set_selectable(  self, setting, ):

        
        libgtk3.gtk_label_set_selectable( self._object,setting )

    def set_line_wrap_mode(  self, wrap_mode, ):

        
        libgtk3.gtk_label_set_line_wrap_mode( self._object,wrap_mode )

    def set_angle(  self, angle, ):

        
        libgtk3.gtk_label_set_angle( self._object,angle )

    def get_single_line_mode(  self, ):

        
        return libgtk3.gtk_label_get_single_line_mode( self._object )

    def set_pattern(  self, pattern, ):

        
        libgtk3.gtk_label_set_pattern( self._object,pattern )

    def set_markup(  self, str, ):

        
        libgtk3.gtk_label_set_markup( self._object,str )

    def set_track_visited_links(  self, track_links, ):

        
        libgtk3.gtk_label_set_track_visited_links( self._object,track_links )

    @staticmethod
    def new_with_mnemonic( str,):
        from .gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_label_new_with_mnemonic(str, )
 or POINTER(c_int)())
