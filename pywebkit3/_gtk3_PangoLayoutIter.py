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
_PangoLayout = c_void_p
_PangoLayoutLine = c_void_p
__PangoRectangle = c_void_p
__PangoLayout = c_void_p
_PangoLayoutRun = c_void_p
"""Enumerations"""

import _gobject_GBoxed
class PangoLayoutIter( _gobject_GBoxed.GBoxed):
    """Class PangoLayoutIter Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def next_char(self, ):

        libgtk3.pango_layout_iter_next_char.restype = gboolean
        libgtk3.pango_layout_iter_next_char.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_iter_next_char(self._object, )

    def next_run(self, ):

        libgtk3.pango_layout_iter_next_run.restype = gboolean
        libgtk3.pango_layout_iter_next_run.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_iter_next_run(self._object, )

    def get_line_yrange(self,  y0_, y1_,):
        if y0_ : y0_ = y0_._object
        else : y0_ = c_void_p()
        if y1_ : y1_ = y1_._object
        else : y1_ = c_void_p()

        libgtk3.pango_layout_iter_get_line_yrange.argtypes = [c_void_p, POITNER(int),POITNER(int)]
        
        libgtk3.pango_layout_iter_get_line_yrange(self._object,  y0_, y1_,)

    def get_char_extents(self,  logical_rect,):
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_iter_get_char_extents.argtypes = [c_void_p, _PangoRectangle]
        
        libgtk3.pango_layout_iter_get_char_extents(self._object,  logical_rect,)

    def get_cluster_extents(self,  ink_rect, logical_rect,):
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_iter_get_cluster_extents.argtypes = [c_void_p, _PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_iter_get_cluster_extents(self._object,  ink_rect, logical_rect,)

    def at_last_line(self, ):

        libgtk3.pango_layout_iter_at_last_line.restype = gboolean
        libgtk3.pango_layout_iter_at_last_line.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_iter_at_last_line(self._object, )

    def get_line(self, ):

        libgtk3.pango_layout_iter_get_line.restype = _PangoLayoutLine
        libgtk3.pango_layout_iter_get_line.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libgtk3.pango_layout_iter_get_line(self._object, )  or c_void_p())

    def free(self, ):

        libgtk3.pango_layout_iter_free.argtypes = [c_void_p]
        
        libgtk3.pango_layout_iter_free(self._object, )

    def get_line_readonly(self, ):

        libgtk3.pango_layout_iter_get_line_readonly.restype = _PangoLayoutLine
        libgtk3.pango_layout_iter_get_line_readonly.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libgtk3.pango_layout_iter_get_line_readonly(self._object, )  or c_void_p())

    def get_index(self, ):

        libgtk3.pango_layout_iter_get_index.restype = int
        libgtk3.pango_layout_iter_get_index.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_iter_get_index(self._object, )

    def get_layout(self, ):

        libgtk3.pango_layout_iter_get_layout.restype = _PangoLayout
        libgtk3.pango_layout_iter_get_layout.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLayout
        return PangoLayout(None,None, obj=libgtk3.pango_layout_iter_get_layout(self._object, )  or c_void_p())

    def get_run_extents(self,  ink_rect, logical_rect,):
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_iter_get_run_extents.argtypes = [c_void_p, _PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_iter_get_run_extents(self._object,  ink_rect, logical_rect,)

    def next_line(self, ):

        libgtk3.pango_layout_iter_next_line.restype = gboolean
        libgtk3.pango_layout_iter_next_line.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_iter_next_line(self._object, )

    def get_run_readonly(self, ):

        libgtk3.pango_layout_iter_get_run_readonly.restype = _PangoLayoutRun
        libgtk3.pango_layout_iter_get_run_readonly.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLayoutRun
        return PangoLayoutRun( obj=libgtk3.pango_layout_iter_get_run_readonly(self._object, )  or c_void_p())

    def copy(self, ):

        libgtk3.pango_layout_iter_copy.restype = _PangoLayoutIter
        libgtk3.pango_layout_iter_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLayoutIter
        return PangoLayoutIter(None, obj=libgtk3.pango_layout_iter_copy(self._object, )  or c_void_p())

    def next_cluster(self, ):

        libgtk3.pango_layout_iter_next_cluster.restype = gboolean
        libgtk3.pango_layout_iter_next_cluster.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_iter_next_cluster(self._object, )

    def get_run(self, ):

        libgtk3.pango_layout_iter_get_run.restype = _PangoLayoutRun
        libgtk3.pango_layout_iter_get_run.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLayoutRun
        return PangoLayoutRun( obj=libgtk3.pango_layout_iter_get_run(self._object, )  or c_void_p())

    def get_baseline(self, ):

        libgtk3.pango_layout_iter_get_baseline.restype = int
        libgtk3.pango_layout_iter_get_baseline.argtypes = [c_void_p]
        
        return libgtk3.pango_layout_iter_get_baseline(self._object, )

    def get_line_extents(self,  ink_rect, logical_rect,):
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_iter_get_line_extents.argtypes = [c_void_p, _PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_iter_get_line_extents(self._object,  ink_rect, logical_rect,)

    def get_layout_extents(self,  ink_rect, logical_rect,):
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_layout_iter_get_layout_extents.argtypes = [c_void_p, _PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_layout_iter_get_layout_extents(self._object,  ink_rect, logical_rect,)

    @staticmethod
    def pango_layout_get_iter( layout,):
        if layout : layout = layout._object
        else : layout = c_void_p()
        libgtk3.pango_layout_get_iter.restype = _PangoLayoutIter
        libgtk3.pango_layout_get_iter.argtypes = [_PangoLayout]
        return libgtk3.pango_layout_get_iter(layout, )

