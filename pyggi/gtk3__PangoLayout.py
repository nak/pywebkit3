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
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GClosure = POINTER(c_int)
_GIcon = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GtkTextBuffer = POINTER(c_int)
_GtkNumerableIcon = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GObject = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_GScanner = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GParameter = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
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

try:
    libgtk3.pango_layout_get_justify.restype = gboolean
    libgtk3.pango_layout_get_justify.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_unknown_glyphs_count.restype = int
    libgtk3.pango_layout_get_unknown_glyphs_count.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_height.restype = None
    libgtk3.pango_layout_set_height.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libgtk3.pango_layout_copy.restype = _PangoLayout
    libgtk3.pango_layout_copy.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_markup.restype = None
    libgtk3.pango_layout_set_markup.argtypes = [_PangoLayout,c_char_p,int]
except:
   pass
try:
    libgtk3.pango_layout_get_attributes.restype = _PangoAttrList
    libgtk3.pango_layout_get_attributes.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_context.restype = _PangoContext
    libgtk3.pango_layout_get_context.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_wrap.restype = None
    libgtk3.pango_layout_set_wrap.argtypes = [_PangoLayout,PangoWrapMode]
except:
   pass
try:
    libgtk3.pango_layout_get_alignment.restype = PangoAlignment
    libgtk3.pango_layout_get_alignment.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_index_to_pos.restype = None
    libgtk3.pango_layout_index_to_pos.argtypes = [_PangoLayout,int,_PangoRectangle]
except:
   pass
try:
    libgtk3.pango_layout_move_cursor_visually.restype = None
    libgtk3.pango_layout_move_cursor_visually.argtypes = [_PangoLayout,gboolean,int,int,int,POINTER(int),POINTER(int)]
except:
   pass
try:
    libgtk3.pango_layout_get_indent.restype = int
    libgtk3.pango_layout_get_indent.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_single_paragraph_mode.restype = gboolean
    libgtk3.pango_layout_get_single_paragraph_mode.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_line_count.restype = int
    libgtk3.pango_layout_get_line_count.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_is_wrapped.restype = gboolean
    libgtk3.pango_layout_is_wrapped.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_pixel_size.restype = None
    libgtk3.pango_layout_get_pixel_size.argtypes = [_PangoLayout,POINTER(int),POINTER(int)]
except:
   pass
try:
    libgtk3.pango_layout_get_lines.restype = _GSList
    libgtk3.pango_layout_get_lines.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_ellipsize.restype = None
    libgtk3.pango_layout_set_ellipsize.argtypes = [_PangoLayout,PangoEllipsizeMode]
except:
   pass
try:
    libgtk3.pango_layout_get_cursor_pos.restype = None
    libgtk3.pango_layout_get_cursor_pos.argtypes = [_PangoLayout,int,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libgtk3.pango_layout_get_wrap.restype = PangoWrapMode
    libgtk3.pango_layout_get_wrap.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_baseline.restype = int
    libgtk3.pango_layout_get_baseline.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_text.restype = None
    libgtk3.pango_layout_set_text.argtypes = [_PangoLayout,c_char_p,int]
except:
   pass
try:
    libgtk3.pango_layout_set_font_description.restype = None
    libgtk3.pango_layout_set_font_description.argtypes = [_PangoLayout,_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_layout_get_size.restype = None
    libgtk3.pango_layout_get_size.argtypes = [_PangoLayout,POINTER(int),POINTER(int)]
except:
   pass
try:
    libgtk3.pango_layout_set_spacing.restype = None
    libgtk3.pango_layout_set_spacing.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libgtk3.pango_layout_get_character_count.restype = gint
    libgtk3.pango_layout_get_character_count.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_log_attrs.restype = None
    libgtk3.pango_layout_get_log_attrs.argtypes = [_PangoLayout,_PangoLogAttr,POINTER(gint)]
except:
   pass
try:
    libgtk3.pango_layout_get_text.restype = c_char_p
    libgtk3.pango_layout_get_text.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_tabs.restype = _PangoTabArray
    libgtk3.pango_layout_get_tabs.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_extents.restype = None
    libgtk3.pango_layout_get_extents.argtypes = [_PangoLayout,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libgtk3.pango_layout_xy_to_index.restype = gboolean
    libgtk3.pango_layout_xy_to_index.argtypes = [_PangoLayout,int,int,POINTER(int),POINTER(int)]
except:
   pass
try:
    libgtk3.pango_layout_get_height.restype = int
    libgtk3.pango_layout_get_height.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_single_paragraph_mode.restype = None
    libgtk3.pango_layout_set_single_paragraph_mode.argtypes = [_PangoLayout,gboolean]
except:
   pass
try:
    libgtk3.pango_layout_get_width.restype = int
    libgtk3.pango_layout_get_width.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_pixel_extents.restype = None
    libgtk3.pango_layout_get_pixel_extents.argtypes = [_PangoLayout,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libgtk3.pango_layout_set_indent.restype = None
    libgtk3.pango_layout_set_indent.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libgtk3.pango_layout_get_line_readonly.restype = _PangoLayoutLine
    libgtk3.pango_layout_get_line_readonly.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libgtk3.pango_layout_set_attributes.restype = None
    libgtk3.pango_layout_set_attributes.argtypes = [_PangoLayout,_PangoAttrList]
except:
   pass
try:
    libgtk3.pango_layout_get_lines_readonly.restype = _GSList
    libgtk3.pango_layout_get_lines_readonly.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_context_changed.restype = None
    libgtk3.pango_layout_context_changed.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_tabs.restype = None
    libgtk3.pango_layout_set_tabs.argtypes = [_PangoLayout,_PangoTabArray]
except:
   pass
try:
    libgtk3.pango_layout_set_width.restype = None
    libgtk3.pango_layout_set_width.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libgtk3.pango_layout_get_log_attrs_readonly.restype = _PangoLogAttr
    libgtk3.pango_layout_get_log_attrs_readonly.argtypes = [_PangoLayout,POINTER(gint)]
except:
   pass
try:
    libgtk3.pango_layout_set_markup_with_accel.restype = None
    libgtk3.pango_layout_set_markup_with_accel.argtypes = [_PangoLayout,c_char_p,int,gunichar,_gunichar]
except:
   pass
try:
    libgtk3.pango_layout_get_auto_dir.restype = gboolean
    libgtk3.pango_layout_get_auto_dir.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_auto_dir.restype = None
    libgtk3.pango_layout_set_auto_dir.argtypes = [_PangoLayout,gboolean]
except:
   pass
try:
    libgtk3.pango_layout_get_font_description.restype = _PangoFontDescription
    libgtk3.pango_layout_get_font_description.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_line.restype = _PangoLayoutLine
    libgtk3.pango_layout_get_line.argtypes = [_PangoLayout,int]
except:
   pass
try:
    libgtk3.pango_layout_index_to_line_x.restype = None
    libgtk3.pango_layout_index_to_line_x.argtypes = [_PangoLayout,int,gboolean,POINTER(int),POINTER(int)]
except:
   pass
try:
    libgtk3.pango_layout_is_ellipsized.restype = gboolean
    libgtk3.pango_layout_is_ellipsized.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_alignment.restype = None
    libgtk3.pango_layout_set_alignment.argtypes = [_PangoLayout,PangoAlignment]
except:
   pass
try:
    libgtk3.pango_layout_get_spacing.restype = int
    libgtk3.pango_layout_get_spacing.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_get_ellipsize.restype = PangoEllipsizeMode
    libgtk3.pango_layout_get_ellipsize.argtypes = [_PangoLayout]
except:
   pass
try:
    libgtk3.pango_layout_set_justify.restype = None
    libgtk3.pango_layout_set_justify.argtypes = [_PangoLayout,gboolean]
except:
   pass
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

        
        return libgtk3.pango_layout_get_justify( self._object )

    def get_unknown_glyphs_count(  self, ):

        
        return libgtk3.pango_layout_get_unknown_glyphs_count( self._object )

    def set_height(  self, height, ):

        
        libgtk3.pango_layout_set_height( self._object,height )

    def copy(  self, ):

        from gtk3 import PangoLayout
        return PangoLayout( obj=libgtk3.pango_layout_copy( self._object )  or POINTER(c_int)())

    def set_markup(  self, markup, length, ):

        
        libgtk3.pango_layout_set_markup( self._object,markup,length )

    def get_attributes(  self, ):

        from gtk3 import PangoAttrList
        return PangoAttrList( obj=libgtk3.pango_layout_get_attributes( self._object )  or POINTER(c_int)())

    def get_context(  self, ):

        from gtk3 import PangoContext
        return PangoContext( obj=libgtk3.pango_layout_get_context( self._object )  or POINTER(c_int)())

    def set_wrap(  self, wrap, ):

        
        libgtk3.pango_layout_set_wrap( self._object,wrap )

    def get_alignment(  self, ):

        
        return libgtk3.pango_layout_get_alignment( self._object )

    def index_to_pos(  self, index_, pos, ):
        if pos: pos = pos._object
        else: pos = POINTER(c_int)()

        
        libgtk3.pango_layout_index_to_pos( self._object,index_,pos )

    def move_cursor_visually(  self, strong, old_index, old_trailing, direction, new_index, new_trailing, ):

        
        libgtk3.pango_layout_move_cursor_visually( self._object,strong,old_index,old_trailing,direction,new_index,new_trailing )

    def get_indent(  self, ):

        
        return libgtk3.pango_layout_get_indent( self._object )

    def get_single_paragraph_mode(  self, ):

        
        return libgtk3.pango_layout_get_single_paragraph_mode( self._object )

    def get_line_count(  self, ):

        
        return libgtk3.pango_layout_get_line_count( self._object )

    def is_wrapped(  self, ):

        
        return libgtk3.pango_layout_is_wrapped( self._object )

    def get_pixel_size(  self, width, height, ):

        
        libgtk3.pango_layout_get_pixel_size( self._object,width,height )

    def get_lines(  self, ):

        from gobject import GSList
        return GSList( obj=libgtk3.pango_layout_get_lines( self._object ) or POINTER(c_int)())

    def set_ellipsize(  self, ellipsize, ):

        
        libgtk3.pango_layout_set_ellipsize( self._object,ellipsize )

    def get_cursor_pos(  self, index_, strong_pos, weak_pos, ):
        if strong_pos: strong_pos = strong_pos._object
        else: strong_pos = POINTER(c_int)()
        if weak_pos: weak_pos = weak_pos._object
        else: weak_pos = POINTER(c_int)()

        
        libgtk3.pango_layout_get_cursor_pos( self._object,index_,strong_pos,weak_pos )

    def get_wrap(  self, ):

        
        return libgtk3.pango_layout_get_wrap( self._object )

    def get_baseline(  self, ):

        
        return libgtk3.pango_layout_get_baseline( self._object )

    def set_text(  self, text, length, ):

        
        libgtk3.pango_layout_set_text( self._object,text,length )

    def set_font_description(  self, desc, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()

        
        libgtk3.pango_layout_set_font_description( self._object,desc )

    def get_size(  self, width, height, ):

        
        libgtk3.pango_layout_get_size( self._object,width,height )

    def set_spacing(  self, spacing, ):

        
        libgtk3.pango_layout_set_spacing( self._object,spacing )

    def get_character_count(  self, ):

        
        return libgtk3.pango_layout_get_character_count( self._object )

    def get_log_attrs(  self, attrs, n_attrs, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        
        libgtk3.pango_layout_get_log_attrs( self._object,attrs,n_attrs )

    def get_text(  self, ):

        
        return libgtk3.pango_layout_get_text( self._object )

    def get_tabs(  self, ):

        from gtk3 import PangoTabArray
        return PangoTabArray( obj=libgtk3.pango_layout_get_tabs( self._object )  or POINTER(c_int)())

    def get_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_int)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        
        libgtk3.pango_layout_get_extents( self._object,ink_rect,logical_rect )

    def xy_to_index(  self, x, y, index_, trailing, ):

        
        return libgtk3.pango_layout_xy_to_index( self._object,x,y,index_,trailing )

    def get_height(  self, ):

        
        return libgtk3.pango_layout_get_height( self._object )

    def set_single_paragraph_mode(  self, setting, ):

        
        libgtk3.pango_layout_set_single_paragraph_mode( self._object,setting )

    def get_width(  self, ):

        
        return libgtk3.pango_layout_get_width( self._object )

    def get_pixel_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_int)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        
        libgtk3.pango_layout_get_pixel_extents( self._object,ink_rect,logical_rect )

    def set_indent(  self, indent, ):

        
        libgtk3.pango_layout_set_indent( self._object,indent )

    def get_line_readonly(  self, line, ):

        from gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libgtk3.pango_layout_get_line_readonly( self._object,line )  or POINTER(c_int)())

    def set_attributes(  self, attrs, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        
        libgtk3.pango_layout_set_attributes( self._object,attrs )

    def get_lines_readonly(  self, ):

        from gobject import GSList
        return GSList( obj=libgtk3.pango_layout_get_lines_readonly( self._object ) or POINTER(c_int)())

    def context_changed(  self, ):

        
        libgtk3.pango_layout_context_changed( self._object )

    def set_tabs(  self, tabs, ):
        if tabs: tabs = tabs._object
        else: tabs = POINTER(c_int)()

        
        libgtk3.pango_layout_set_tabs( self._object,tabs )

    def set_width(  self, width, ):

        
        libgtk3.pango_layout_set_width( self._object,width )

    def get_log_attrs_readonly(  self, n_attrs, ):

        from gtk3 import PangoLogAttr
        return PangoLogAttr( obj=libgtk3.pango_layout_get_log_attrs_readonly( self._object,n_attrs )  or POINTER(c_int)())

    def set_markup_with_accel(  self, markup, length, accel_marker, accel_char, ):
        if accel_marker: accel_marker = accel_marker._object
        else: accel_marker = POINTER(c_int)()
        if accel_char: accel_char = accel_char._object
        else: accel_char = POINTER(c_int)()

        
        libgtk3.pango_layout_set_markup_with_accel( self._object,markup,length,accel_marker,accel_char )

    def get_auto_dir(  self, ):

        
        return libgtk3.pango_layout_get_auto_dir( self._object )

    def set_auto_dir(  self, auto_dir, ):

        
        libgtk3.pango_layout_set_auto_dir( self._object,auto_dir )

    def get_font_description(  self, ):

        from gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libgtk3.pango_layout_get_font_description( self._object )  or POINTER(c_int)())

    def get_line(  self, line, ):

        from gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libgtk3.pango_layout_get_line( self._object,line )  or POINTER(c_int)())

    def index_to_line_x(  self, index_, trailing, line, x_pos, ):

        
        libgtk3.pango_layout_index_to_line_x( self._object,index_,trailing,line,x_pos )

    def is_ellipsized(  self, ):

        
        return libgtk3.pango_layout_is_ellipsized( self._object )

    def set_alignment(  self, alignment, ):

        
        libgtk3.pango_layout_set_alignment( self._object,alignment )

    def get_spacing(  self, ):

        
        return libgtk3.pango_layout_get_spacing( self._object )

    def get_ellipsize(  self, ):

        
        return libgtk3.pango_layout_get_ellipsize( self._object )

    def set_justify(  self, justify, ):

        
        libgtk3.pango_layout_set_justify( self._object,justify )

