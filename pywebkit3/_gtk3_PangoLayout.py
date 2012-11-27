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
_PangoLayoutIter = c_void_p
_PangoContext = c_void_p
__PangoContext = c_void_p
__PangoLogAttr = c_void_p
_PangoLayout = c_void_p
__gunichar = c_void_p
_PangoLayoutLine = c_void_p
_GSList = c_void_p
__PangoRectangle = c_void_p
_char = c_void_p
__PangoFontDescription = c_void_p
_PangoFontDescription = c_void_p
_PangoTabArray = c_void_p
__PangoLayout = c_void_p
__PangoAttrList = c_void_p
_PangoLogAttr = c_void_p
__PangoTabArray = c_void_p
_PangoLayoutRun = c_void_p
_PangoAttrList = c_void_p
"""Enumerations"""
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int

import _gobject_GObject
class PangoLayout( _gobject_GObject.GObject):
    """Class PangoLayout Constructors"""
    def __init__( self, context,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.pango_layout_new.restype = c_void_p
        if context : context = context._object
        else : context = c_void_p()

        libgtk3.pango_layout_new.argtypes = [_PangoContext]
        self._object = libgtk3.pango_layout_new(context, )

    """Methods"""
    def get_justify(self, ):

        libgtk3.pango_layout_get_justify.restype = gboolean
        libgtk3.pango_layout_get_justify.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_justify(self._object, )

    def get_unknown_glyphs_count(self, ):

        libgtk3.pango_layout_get_unknown_glyphs_count.restype = int
        libgtk3.pango_layout_get_unknown_glyphs_count.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_unknown_glyphs_count(self._object, )

    def set_height(self,  height,):

        libgtk3.pango_layout_set_height.argtypes = [c_void_p, int]
        
        libgtk3.pango_layout_set_height(self._object,  height,)

    def copy(self, ):

        libgtk3.pango_layout_copy.restype = _PangoLayout
        libgtk3.pango_layout_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLayout
        return PangoLayout(None, obj=libgtk3.pango_layout_copy(self._object, )  or c_void_p())

    def set_markup(self,  markup, length,):

        libgtk3.pango_layout_set_markup.argtypes = [c_void_p, c_char_p,int]
        
        libgtk3.pango_layout_set_markup(self._object,  markup, length,)

    def get_attributes(self, ):

        libgtk3.pango_layout_get_attributes.restype = _PangoAttrList
        libgtk3.pango_layout_get_attributes.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoAttrList
        return PangoAttrList( obj=libgtk3.pango_layout_get_attributes(self._object, )  or c_void_p())

    def get_context(self, ):

        libgtk3.pango_layout_get_context.restype = _PangoContext
        libgtk3.pango_layout_get_context.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoContext
        return PangoContext(None, obj=libgtk3.pango_layout_get_context(self._object, )  or c_void_p())

    def set_wrap(self,  wrap,):

        libgtk3.pango_layout_set_wrap.argtypes = [c_void_p, PangoWrapMode]
        
        libgtk3.pango_layout_set_wrap(self._object,  wrap,)

    def get_alignment(self, ):

        libgtk3.pango_layout_get_alignment.restype = PangoAlignment
        libgtk3.pango_layout_get_alignment.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_alignment(self._object, )

    def index_to_pos(self,  index_, pos,):
        if pos : pos = pos._object
        else : pos = c_void_p()

        libgtk3.pango_layout_index_to_pos.argtypes = [c_void_p, int,_PangoRectangle]
        
        libgtk3.pango_layout_index_to_pos(self._object,  index_, pos,)

    def move_cursor_visually(self,  strong, old_index, old_trailing, direction, new_index, new_trailing,):
        if new_index : new_index = new_index._object
        else : new_index = c_void_p()
        if new_trailing : new_trailing = new_trailing._object
        else : new_trailing = c_void_p()

        libgtk3.pango_layout_move_cursor_visually.argtypes = [c_void_p, gboolean,int,int,int,POITNER(int),POITNER(int)]
        
        libgtk3.pango_layout_move_cursor_visually(self._object,  strong, old_index, old_trailing, direction, new_index, new_trailing,)

    def get_indent(self, ):

        libgtk3.pango_layout_get_indent.restype = int
        libgtk3.pango_layout_get_indent.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_indent(self._object, )

    def get_single_paragraph_mode(self, ):

        libgtk3.pango_layout_get_single_paragraph_mode.restype = gboolean
        libgtk3.pango_layout_get_single_paragraph_mode.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_single_paragraph_mode(self._object, )

    def get_line_count(self, ):

        libgtk3.pango_layout_get_line_count.restype = int
        libgtk3.pango_layout_get_line_count.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_line_count(self._object, )

    def is_wrapped(self, ):

        libgtk3.pango_layout_is_wrapped.restype = gboolean
        libgtk3.pango_layout_is_wrapped.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_is_wrapped(self._object, )

    def get_pixel_size(self,  width, height,):
        if width : width = width._object
        else : width = c_void_p()
        if height : height = height._object
        else : height = c_void_p()

        libgtk3.pango_layout_get_pixel_size.argtypes = [c_void_p, POITNER(int),POITNER(int)]
        
        libgtk3.pango_layout_get_pixel_size(self._object,  width, height,)

    def get_lines(self, ):

        libgtk3.pango_layout_get_lines.restype = _GSList
        libgtk3.pango_layout_get_lines.argtypes = [c_void_p]
        from pywebkit3.gobject import GSList
        return GSList( obj=libgtk3.pango_layout_get_lines(self._object, ) or c_void_p())

    def set_ellipsize(self,  ellipsize,):

        libgtk3.pango_layout_set_ellipsize.argtypes = [c_void_p, PangoEllipsizeMode]
        
        libgtk3.pango_layout_set_ellipsize(self._object,  ellipsize,)

    def get_cursor_pos(self,  index_, strong_pos, weak_pos,):
        if strong_pos : strong_pos = strong_pos._object
        else : strong_pos = c_void_p()
        if weak_pos : weak_pos = weak_pos._object
        else : weak_pos = c_void_p()

        libgtk3.pango_layout_get_cursor_pos.argtypes = [c_void_p, int,_PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_get_cursor_pos(self._object,  index_, strong_pos, weak_pos,)

    def get_wrap(self, ):

        libgtk3.pango_layout_get_wrap.restype = PangoWrapMode
        libgtk3.pango_layout_get_wrap.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_wrap(self._object, )

    def get_baseline(self, ):

        libgtk3.pango_layout_get_baseline.restype = int
        libgtk3.pango_layout_get_baseline.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_baseline(self._object, )

    def set_text(self,  text, length,):

        libgtk3.pango_layout_set_text.argtypes = [c_void_p, c_char_p,int]
        
        libgtk3.pango_layout_set_text(self._object,  text, length,)

    def set_font_description(self,  desc,):
        if desc : desc = desc._object
        else : desc = c_void_p()

        libgtk3.pango_layout_set_font_description.argtypes = [c_void_p, _PangoFontDescription]
        
        libgtk3.pango_layout_set_font_description(self._object,  desc,)

    def get_size(self,  width, height,):
        if width : width = width._object
        else : width = c_void_p()
        if height : height = height._object
        else : height = c_void_p()

        libgtk3.pango_layout_get_size.argtypes = [c_void_p, POITNER(int),POITNER(int)]
        
        libgtk3.pango_layout_get_size(self._object,  width, height,)

    def set_spacing(self,  spacing,):

        libgtk3.pango_layout_set_spacing.argtypes = [c_void_p, int]
        
        libgtk3.pango_layout_set_spacing(self._object,  spacing,)

    def get_character_count(self, ):

        libgtk3.pango_layout_get_character_count.restype = gint
        libgtk3.pango_layout_get_character_count.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_character_count(self._object, )

    def get_log_attrs(self,  attrs, n_attrs,):
        if attrs : attrs = attrs._object
        else : attrs = c_void_p()
        if n_attrs : n_attrs = n_attrs._object
        else : n_attrs = c_void_p()

        libgtk3.pango_layout_get_log_attrs.argtypes = [c_void_p, _PangoLogAttr,POITNER(gint)]
        
        libgtk3.pango_layout_get_log_attrs(self._object,  attrs, n_attrs,)

    def get_text(self, ):

        libgtk3.pango_layout_get_text.restype = _char
        libgtk3.pango_layout_get_text.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_text(self._object, )

    def get_tabs(self, ):

        libgtk3.pango_layout_get_tabs.restype = _PangoTabArray
        libgtk3.pango_layout_get_tabs.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoTabArray
        return PangoTabArray( obj=libgtk3.pango_layout_get_tabs(self._object, )  or c_void_p())

    def get_extents(self,  ink_rect, logical_rect,):
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_get_extents.argtypes = [c_void_p, _PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_get_extents(self._object,  ink_rect, logical_rect,)

    def xy_to_index(self,  x, y, index_, trailing,):
        if index_ : index_ = index_._object
        else : index_ = c_void_p()
        if trailing : trailing = trailing._object
        else : trailing = c_void_p()

        libgtk3.pango_layout_xy_to_index.restype = gboolean
        libgtk3.pango_layout_xy_to_index.argtypes = [c_void_p, int,int,POITNER(int),POITNER(int)]
        
        return libgtk3.pango_layout_xy_to_index(self._object,  x, y, index_, trailing,)

    def get_height(self, ):

        libgtk3.pango_layout_get_height.restype = int
        libgtk3.pango_layout_get_height.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_height(self._object, )

    def set_single_paragraph_mode(self,  setting,):

        libgtk3.pango_layout_set_single_paragraph_mode.argtypes = [c_void_p, gboolean]
        
        libgtk3.pango_layout_set_single_paragraph_mode(self._object,  setting,)

    def get_width(self, ):

        libgtk3.pango_layout_get_width.restype = int
        libgtk3.pango_layout_get_width.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_width(self._object, )

    def get_pixel_extents(self,  ink_rect, logical_rect,):
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_get_pixel_extents.argtypes = [c_void_p, _PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_get_pixel_extents(self._object,  ink_rect, logical_rect,)

    def set_indent(self,  indent,):

        libgtk3.pango_layout_set_indent.argtypes = [c_void_p, int]
        
        libgtk3.pango_layout_set_indent(self._object,  indent,)

    def get_line_readonly(self,  line,):

        libgtk3.pango_layout_get_line_readonly.restype = _PangoLayoutLine
        libgtk3.pango_layout_get_line_readonly.argtypes = [c_void_p, int]
        from pywebkit3.gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libgtk3.pango_layout_get_line_readonly(self._object,  line,)  or c_void_p())

    def set_attributes(self,  attrs,):
        if attrs : attrs = attrs._object
        else : attrs = c_void_p()

        libgtk3.pango_layout_set_attributes.argtypes = [c_void_p, _PangoAttrList]
        
        libgtk3.pango_layout_set_attributes(self._object,  attrs,)

    def get_lines_readonly(self, ):

        libgtk3.pango_layout_get_lines_readonly.restype = _GSList
        libgtk3.pango_layout_get_lines_readonly.argtypes = [c_void_p]
        from pywebkit3.gobject import GSList
        return GSList( obj=libgtk3.pango_layout_get_lines_readonly(self._object, ) or c_void_p())

    def context_changed(self, ):

        libgtk3.pango_layout_context_changed.argtypes = [c_void_p]
        
        libgtk3.pango_layout_context_changed(self._object, )

    def set_tabs(self,  tabs,):
        if tabs : tabs = tabs._object
        else : tabs = c_void_p()

        libgtk3.pango_layout_set_tabs.argtypes = [c_void_p, _PangoTabArray]
        
        libgtk3.pango_layout_set_tabs(self._object,  tabs,)

    def set_width(self,  width,):

        libgtk3.pango_layout_set_width.argtypes = [c_void_p, int]
        
        libgtk3.pango_layout_set_width(self._object,  width,)

    def get_log_attrs_readonly(self,  n_attrs,):
        if n_attrs : n_attrs = n_attrs._object
        else : n_attrs = c_void_p()

        libgtk3.pango_layout_get_log_attrs_readonly.restype = _PangoLogAttr
        libgtk3.pango_layout_get_log_attrs_readonly.argtypes = [c_void_p, POITNER(gint)]
        from pywebkit3.gtk3 import PangoLogAttr
        return PangoLogAttr( obj=libgtk3.pango_layout_get_log_attrs_readonly(self._object,  n_attrs,)  or c_void_p())

    def set_markup_with_accel(self,  markup, length, accel_marker, accel_char,):
        if accel_marker : accel_marker = accel_marker._object
        else : accel_marker = c_void_p()
        if accel_char : accel_char = accel_char._object
        else : accel_char = c_void_p()

        libgtk3.pango_layout_set_markup_with_accel.argtypes = [c_void_p, c_char_p,int,gunichar,_gunichar]
        
        libgtk3.pango_layout_set_markup_with_accel(self._object,  markup, length, accel_marker, accel_char,)

    def get_auto_dir(self, ):

        libgtk3.pango_layout_get_auto_dir.restype = gboolean
        libgtk3.pango_layout_get_auto_dir.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_auto_dir(self._object, )

    def set_auto_dir(self,  auto_dir,):

        libgtk3.pango_layout_set_auto_dir.argtypes = [c_void_p, gboolean]
        
        libgtk3.pango_layout_set_auto_dir(self._object,  auto_dir,)

    def get_font_description(self, ):

        libgtk3.pango_layout_get_font_description.restype = _PangoFontDescription
        libgtk3.pango_layout_get_font_description.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libgtk3.pango_layout_get_font_description(self._object, )  or c_void_p())

    def get_line(self,  line,):

        libgtk3.pango_layout_get_line.restype = _PangoLayoutLine
        libgtk3.pango_layout_get_line.argtypes = [c_void_p, int]
        from pywebkit3.gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libgtk3.pango_layout_get_line(self._object,  line,)  or c_void_p())

    def index_to_line_x(self,  index_, trailing, line, x_pos,):
        if line : line = line._object
        else : line = c_void_p()
        if x_pos : x_pos = x_pos._object
        else : x_pos = c_void_p()

        libgtk3.pango_layout_index_to_line_x.argtypes = [c_void_p, int,gboolean,POITNER(int),POITNER(int)]
        
        libgtk3.pango_layout_index_to_line_x(self._object,  index_, trailing, line, x_pos,)

    def is_ellipsized(self, ):

        libgtk3.pango_layout_is_ellipsized.restype = gboolean
        libgtk3.pango_layout_is_ellipsized.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_is_ellipsized(self._object, )

    def set_alignment(self,  alignment,):

        libgtk3.pango_layout_set_alignment.argtypes = [c_void_p, PangoAlignment]
        
        libgtk3.pango_layout_set_alignment(self._object,  alignment,)

    def get_spacing(self, ):

        libgtk3.pango_layout_get_spacing.restype = int
        libgtk3.pango_layout_get_spacing.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_spacing(self._object, )

    def get_ellipsize(self, ):

        libgtk3.pango_layout_get_ellipsize.restype = PangoEllipsizeMode
        libgtk3.pango_layout_get_ellipsize.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_get_ellipsize(self._object, )

    def set_justify(self,  justify,):

        libgtk3.pango_layout_set_justify.argtypes = [c_void_p, gboolean]
        
        libgtk3.pango_layout_set_justify(self._object,  justify,)

