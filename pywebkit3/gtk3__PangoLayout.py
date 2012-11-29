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
from gtk3_types import *
    
    
"""Derived Pointer Types"""
__GtkRcStyle = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
__GClosure = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
__GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
__GObject = POINTER(c_int)
__PangoLayout = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
__GParamSpec = POINTER(c_int)
__PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
__PangoContext = POINTER(c_int)
__JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__PangoFont = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__JSClass = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
__GtkSettings = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__PangoFontFamily = POINTER(c_int)
__JSContextGroup = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GtkBorder = POINTER(c_int)
__GError = POINTER(c_int)
__PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__JSContext = POINTER(c_int)
_PangoFontsetSimple = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
__GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
__PangoTabArray = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
__GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
__PangoMatrix = POINTER(c_int)
__GtkPrintOperation = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GList = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__JSPropertyNameAccumulator = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
__GdkColor = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
__gunichar = POINTER(c_int)
__GdkWMDecoration = POINTER(c_int)
__PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
__JSObject = POINTER(c_int)
_WebKitWebNavigationAction = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GIcon = POINTER(c_int)
__GtkWindow = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GByteArray = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
__GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
"""Enumerations"""
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkIconSize = c_int
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
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GdkCursorType = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
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
GtkDialogFlags = c_int
GtkResponseType = c_int
WebKitWebNavigationReason = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int

import gobject__GObject
class PangoLayout( gobject__GObject.GObject):
    """Class PangoLayout Constructors"""
    def __init__( self, context,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.pango_layout_new.restype = POINTER(c_int)
            
            if context : context = context._object
            else :  context = POINTER(c_int)()

            libgtk3.pango_layout_new.argtypes = [_PangoContext]
            self._object = libgtk3.pango_layout_new(context, )

    """Methods"""
    def get_justify(  self, ):

        libgtk3.pango_layout_get_justify.restype = gboolean
        libgtk3.pango_layout_get_justify.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_justify( self._object )

    def get_unknown_glyphs_count(  self, ):

        libgtk3.pango_layout_get_unknown_glyphs_count.restype = int
        libgtk3.pango_layout_get_unknown_glyphs_count.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_unknown_glyphs_count( self._object )

    def set_height(  self, height, ):

        libgtk3.pango_layout_set_height.argtypes = [_PangoLayout,int]
        
        libgtk3.pango_layout_set_height( self._object,height )

    def copy(  self, ):

        libgtk3.pango_layout_copy.restype = _PangoLayout
        libgtk3.pango_layout_copy.argtypes = [_PangoLayout]
        from gtk3 import PangoLayout
        return PangoLayout( obj=libgtk3.pango_layout_copy( self._object )  or POINTER(c_int)())

    def set_markup(  self, markup, length, ):

        libgtk3.pango_layout_set_markup.argtypes = [_PangoLayout,c_char_p,int]
        
        libgtk3.pango_layout_set_markup( self._object,markup,length )

    def get_attributes(  self, ):

        libgtk3.pango_layout_get_attributes.restype = _PangoAttrList
        libgtk3.pango_layout_get_attributes.argtypes = [_PangoLayout]
        from gtk3 import PangoAttrList
        return PangoAttrList( obj=libgtk3.pango_layout_get_attributes( self._object )  or POINTER(c_int)())

    def get_context(  self, ):

        libgtk3.pango_layout_get_context.restype = _PangoContext
        libgtk3.pango_layout_get_context.argtypes = [_PangoLayout]
        from gtk3 import PangoContext
        return PangoContext(None, obj=libgtk3.pango_layout_get_context( self._object )  or POINTER(c_int)())

    def set_wrap(  self, wrap, ):

        libgtk3.pango_layout_set_wrap.argtypes = [_PangoLayout,PangoWrapMode]
        
        libgtk3.pango_layout_set_wrap( self._object,wrap )

    def get_alignment(  self, ):

        libgtk3.pango_layout_get_alignment.restype = PangoAlignment
        libgtk3.pango_layout_get_alignment.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_alignment( self._object )

    def index_to_pos(  self, index_, pos, ):
        if pos: pos = pos._object
        else: pos = POINTER(c_int)()

        libgtk3.pango_layout_index_to_pos.argtypes = [_PangoLayout,int,_PangoRectangle]
        
        libgtk3.pango_layout_index_to_pos( self._object,index_,pos )

    def move_cursor_visually(  self, strong, old_index, old_trailing, direction, new_index, new_trailing, ):

        libgtk3.pango_layout_move_cursor_visually.argtypes = [_PangoLayout,gboolean,int,int,int,POINTER(int),POINTER(int)]
        
        libgtk3.pango_layout_move_cursor_visually( self._object,strong,old_index,old_trailing,direction,new_index,new_trailing )

    def get_indent(  self, ):

        libgtk3.pango_layout_get_indent.restype = int
        libgtk3.pango_layout_get_indent.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_indent( self._object )

    def get_single_paragraph_mode(  self, ):

        libgtk3.pango_layout_get_single_paragraph_mode.restype = gboolean
        libgtk3.pango_layout_get_single_paragraph_mode.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_single_paragraph_mode( self._object )

    def get_line_count(  self, ):

        libgtk3.pango_layout_get_line_count.restype = int
        libgtk3.pango_layout_get_line_count.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_line_count( self._object )

    def is_wrapped(  self, ):

        libgtk3.pango_layout_is_wrapped.restype = gboolean
        libgtk3.pango_layout_is_wrapped.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_is_wrapped( self._object )

    def get_pixel_size(  self, width, height, ):

        libgtk3.pango_layout_get_pixel_size.argtypes = [_PangoLayout,POINTER(int),POINTER(int)]
        
        libgtk3.pango_layout_get_pixel_size( self._object,width,height )

    def get_lines(  self, ):

        libgtk3.pango_layout_get_lines.restype = _GSList
        libgtk3.pango_layout_get_lines.argtypes = [_PangoLayout]
        from gobject import GSList
        return GSList( obj=libgtk3.pango_layout_get_lines( self._object ) or POINTER(c_int)())

    def set_ellipsize(  self, ellipsize, ):

        libgtk3.pango_layout_set_ellipsize.argtypes = [_PangoLayout,PangoEllipsizeMode]
        
        libgtk3.pango_layout_set_ellipsize( self._object,ellipsize )

    def get_cursor_pos(  self, index_, strong_pos, weak_pos, ):
        if strong_pos: strong_pos = strong_pos._object
        else: strong_pos = POINTER(c_int)()
        if weak_pos: weak_pos = weak_pos._object
        else: weak_pos = POINTER(c_int)()

        libgtk3.pango_layout_get_cursor_pos.argtypes = [_PangoLayout,int,_PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_get_cursor_pos( self._object,index_,strong_pos,weak_pos )

    def get_wrap(  self, ):

        libgtk3.pango_layout_get_wrap.restype = PangoWrapMode
        libgtk3.pango_layout_get_wrap.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_wrap( self._object )

    def get_baseline(  self, ):

        libgtk3.pango_layout_get_baseline.restype = int
        libgtk3.pango_layout_get_baseline.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_baseline( self._object )

    def set_text(  self, text, length, ):

        libgtk3.pango_layout_set_text.argtypes = [_PangoLayout,c_char_p,int]
        
        libgtk3.pango_layout_set_text( self._object,text,length )

    def set_font_description(  self, desc, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()

        libgtk3.pango_layout_set_font_description.argtypes = [_PangoLayout,_PangoFontDescription]
        
        libgtk3.pango_layout_set_font_description( self._object,desc )

    def get_size(  self, width, height, ):

        libgtk3.pango_layout_get_size.argtypes = [_PangoLayout,POINTER(int),POINTER(int)]
        
        libgtk3.pango_layout_get_size( self._object,width,height )

    def set_spacing(  self, spacing, ):

        libgtk3.pango_layout_set_spacing.argtypes = [_PangoLayout,int]
        
        libgtk3.pango_layout_set_spacing( self._object,spacing )

    def get_character_count(  self, ):

        libgtk3.pango_layout_get_character_count.restype = gint
        libgtk3.pango_layout_get_character_count.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_character_count( self._object )

    def get_log_attrs(  self, attrs, n_attrs, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        libgtk3.pango_layout_get_log_attrs.argtypes = [_PangoLayout,_PangoLogAttr,POINTER(gint)]
        
        libgtk3.pango_layout_get_log_attrs( self._object,attrs,n_attrs )

    def get_text(  self, ):

        libgtk3.pango_layout_get_text.restype = c_char_p
        libgtk3.pango_layout_get_text.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_text( self._object )

    def get_tabs(  self, ):

        libgtk3.pango_layout_get_tabs.restype = _PangoTabArray
        libgtk3.pango_layout_get_tabs.argtypes = [_PangoLayout]
        from gtk3 import PangoTabArray
        return PangoTabArray( obj=libgtk3.pango_layout_get_tabs( self._object )  or POINTER(c_int)())

    def get_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_int)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        libgtk3.pango_layout_get_extents.argtypes = [_PangoLayout,_PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_get_extents( self._object,ink_rect,logical_rect )

    def xy_to_index(  self, x, y, index_, trailing, ):

        libgtk3.pango_layout_xy_to_index.restype = gboolean
        libgtk3.pango_layout_xy_to_index.argtypes = [_PangoLayout,int,int,POINTER(int),POINTER(int)]
        
        return libgtk3.pango_layout_xy_to_index( self._object,x,y,index_,trailing )

    def get_height(  self, ):

        libgtk3.pango_layout_get_height.restype = int
        libgtk3.pango_layout_get_height.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_height( self._object )

    def set_single_paragraph_mode(  self, setting, ):

        libgtk3.pango_layout_set_single_paragraph_mode.argtypes = [_PangoLayout,gboolean]
        
        libgtk3.pango_layout_set_single_paragraph_mode( self._object,setting )

    def get_width(  self, ):

        libgtk3.pango_layout_get_width.restype = int
        libgtk3.pango_layout_get_width.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_width( self._object )

    def get_pixel_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_int)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        libgtk3.pango_layout_get_pixel_extents.argtypes = [_PangoLayout,_PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_get_pixel_extents( self._object,ink_rect,logical_rect )

    def set_indent(  self, indent, ):

        libgtk3.pango_layout_set_indent.argtypes = [_PangoLayout,int]
        
        libgtk3.pango_layout_set_indent( self._object,indent )

    def get_line_readonly(  self, line, ):

        libgtk3.pango_layout_get_line_readonly.restype = _PangoLayoutLine
        libgtk3.pango_layout_get_line_readonly.argtypes = [_PangoLayout,int]
        from gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libgtk3.pango_layout_get_line_readonly( self._object,line )  or POINTER(c_int)())

    def set_attributes(  self, attrs, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        libgtk3.pango_layout_set_attributes.argtypes = [_PangoLayout,_PangoAttrList]
        
        libgtk3.pango_layout_set_attributes( self._object,attrs )

    def get_lines_readonly(  self, ):

        libgtk3.pango_layout_get_lines_readonly.restype = _GSList
        libgtk3.pango_layout_get_lines_readonly.argtypes = [_PangoLayout]
        from gobject import GSList
        return GSList( obj=libgtk3.pango_layout_get_lines_readonly( self._object ) or POINTER(c_int)())

    def context_changed(  self, ):

        libgtk3.pango_layout_context_changed.argtypes = [_PangoLayout]
        
        libgtk3.pango_layout_context_changed( self._object )

    def set_tabs(  self, tabs, ):
        if tabs: tabs = tabs._object
        else: tabs = POINTER(c_int)()

        libgtk3.pango_layout_set_tabs.argtypes = [_PangoLayout,_PangoTabArray]
        
        libgtk3.pango_layout_set_tabs( self._object,tabs )

    def set_width(  self, width, ):

        libgtk3.pango_layout_set_width.argtypes = [_PangoLayout,int]
        
        libgtk3.pango_layout_set_width( self._object,width )

    def get_log_attrs_readonly(  self, n_attrs, ):

        libgtk3.pango_layout_get_log_attrs_readonly.restype = _PangoLogAttr
        libgtk3.pango_layout_get_log_attrs_readonly.argtypes = [_PangoLayout,POINTER(gint)]
        from gtk3 import PangoLogAttr
        return PangoLogAttr( obj=libgtk3.pango_layout_get_log_attrs_readonly( self._object,n_attrs )  or POINTER(c_int)())

    def set_markup_with_accel(  self, markup, length, accel_marker, accel_char, ):
        if accel_marker: accel_marker = accel_marker._object
        else: accel_marker = POINTER(c_int)()
        if accel_char: accel_char = accel_char._object
        else: accel_char = POINTER(c_int)()

        libgtk3.pango_layout_set_markup_with_accel.argtypes = [_PangoLayout,c_char_p,int,gunichar,_gunichar]
        
        libgtk3.pango_layout_set_markup_with_accel( self._object,markup,length,accel_marker,accel_char )

    def get_auto_dir(  self, ):

        libgtk3.pango_layout_get_auto_dir.restype = gboolean
        libgtk3.pango_layout_get_auto_dir.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_auto_dir( self._object )

    def set_auto_dir(  self, auto_dir, ):

        libgtk3.pango_layout_set_auto_dir.argtypes = [_PangoLayout,gboolean]
        
        libgtk3.pango_layout_set_auto_dir( self._object,auto_dir )

    def get_font_description(  self, ):

        libgtk3.pango_layout_get_font_description.restype = _PangoFontDescription
        libgtk3.pango_layout_get_font_description.argtypes = [_PangoLayout]
        from gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libgtk3.pango_layout_get_font_description( self._object )  or POINTER(c_int)())

    def get_line(  self, line, ):

        libgtk3.pango_layout_get_line.restype = _PangoLayoutLine
        libgtk3.pango_layout_get_line.argtypes = [_PangoLayout,int]
        from gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libgtk3.pango_layout_get_line( self._object,line )  or POINTER(c_int)())

    def index_to_line_x(  self, index_, trailing, line, x_pos, ):

        libgtk3.pango_layout_index_to_line_x.argtypes = [_PangoLayout,int,gboolean,POINTER(int),POINTER(int)]
        
        libgtk3.pango_layout_index_to_line_x( self._object,index_,trailing,line,x_pos )

    def is_ellipsized(  self, ):

        libgtk3.pango_layout_is_ellipsized.restype = gboolean
        libgtk3.pango_layout_is_ellipsized.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_is_ellipsized( self._object )

    def set_alignment(  self, alignment, ):

        libgtk3.pango_layout_set_alignment.argtypes = [_PangoLayout,PangoAlignment]
        
        libgtk3.pango_layout_set_alignment( self._object,alignment )

    def get_spacing(  self, ):

        libgtk3.pango_layout_get_spacing.restype = int
        libgtk3.pango_layout_get_spacing.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_spacing( self._object )

    def get_ellipsize(  self, ):

        libgtk3.pango_layout_get_ellipsize.restype = PangoEllipsizeMode
        libgtk3.pango_layout_get_ellipsize.argtypes = [_PangoLayout]
        
        return libgtk3.pango_layout_get_ellipsize( self._object )

    def set_justify(  self, justify, ):

        libgtk3.pango_layout_set_justify.argtypes = [_PangoLayout,gboolean]
        
        libgtk3.pango_layout_set_justify( self._object,justify )

