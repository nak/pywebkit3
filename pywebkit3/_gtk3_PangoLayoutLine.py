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
_PangoLayoutLine = c_void_p
__PangoRectangle = c_void_p
"""Enumerations"""

import _gobject_GBoxed
class PangoLayoutLine( _gobject_GBoxed.GBoxed):
    """Class PangoLayoutLine Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def index_to_x(self,  index_, trailing, x_pos,):
        if x_pos : x_pos = x_pos._object
        else : x_pos = c_void_p()

        libgtk3.pango_layout_line_index_to_x.argtypes = [c_void_p, int,gboolean,POITNER(int)]
        
        libgtk3.pango_layout_line_index_to_x(self._object,  index_, trailing, x_pos,)

    def get_extents(self,  ink_rect, logical_rect,):
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_line_get_extents.argtypes = [c_void_p, _PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_line_get_extents(self._object,  ink_rect, logical_rect,)

    def x_to_index(self,  x_pos, index_, trailing,):
        if index_ : index_ = index_._object
        else : index_ = c_void_p()
        if trailing : trailing = trailing._object
        else : trailing = c_void_p()

        libgtk3.pango_layout_line_x_to_index.restype = gboolean
        libgtk3.pango_layout_line_x_to_index.argtypes = [c_void_p, int,POITNER(int),POITNER(int)]
        
        return libgtk3.pango_layout_line_x_to_index(self._object,  x_pos, index_, trailing,)

    def unref(self, ):

        libgtk3.pango_layout_line_unref.argtypes = [c_void_p]
        
        libgtk3.pango_layout_line_unref(self._object, )

    def get_x_ranges(self,  start_index, end_index, ranges, n_ranges,):
        if ranges : ranges = ranges._object
        else : ranges = c_void_p()
        if n_ranges : n_ranges = n_ranges._object
        else : n_ranges = c_void_p()

        libgtk3.pango_layout_line_get_x_ranges.argtypes = [c_void_p, int,int,POITNER(int),POITNER(int)]
        
        libgtk3.pango_layout_line_get_x_ranges(self._object,  start_index, end_index, ranges, n_ranges,)

    def ref(self, ):

        libgtk3.pango_layout_line_ref.restype = _PangoLayoutLine
        libgtk3.pango_layout_line_ref.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLayoutLine
        return PangoLayoutLine(None, obj=libgtk3.pango_layout_line_ref(self._object, )  or c_void_p())

    def get_pixel_extents(self,  ink_rect, logical_rect,):
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_line_get_pixel_extents.argtypes = [c_void_p, _PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_line_get_pixel_extents(self._object,  ink_rect, logical_rect,)

