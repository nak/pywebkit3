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
__PangoMatrix = c_void_p
__PangoRectangle = c_void_p
_PangoMatrix = c_void_p
"""Enumerations"""

import _gobject_GBoxed
class PangoMatrix( _gobject_GBoxed.GBoxed):
    """Class PangoMatrix Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def transform_pixel_rectangle(self,  rect,):
        if rect : rect = rect._object
        else : rect = c_void_p()

        libgtk3.pango_matrix_transform_pixel_rectangle.argtypes = [c_void_p, _PangoRectangle]
        
        libgtk3.pango_matrix_transform_pixel_rectangle(self._object,  rect,)

    def rotate(self,  degrees,):

        libgtk3.pango_matrix_rotate.argtypes = [c_void_p, double]
        
        libgtk3.pango_matrix_rotate(self._object,  degrees,)

    def transform_distance(self,  dx, dy,):
        if dx : dx = dx._object
        else : dx = c_void_p()
        if dy : dy = dy._object
        else : dy = c_void_p()

        libgtk3.pango_matrix_transform_distance.argtypes = [c_void_p, POITNER(double),POITNER(double)]
        
        libgtk3.pango_matrix_transform_distance(self._object,  dx, dy,)

    def translate(self,  tx, ty,):

        libgtk3.pango_matrix_translate.argtypes = [c_void_p, gdouble,gdouble]
        
        libgtk3.pango_matrix_translate(self._object,  tx, ty,)

    def transform_rectangle(self,  rect,):
        if rect : rect = rect._object
        else : rect = c_void_p()

        libgtk3.pango_matrix_transform_rectangle.argtypes = [c_void_p, _PangoRectangle]
        
        libgtk3.pango_matrix_transform_rectangle(self._object,  rect,)

    def transform_point(self,  x, y,):
        if x : x = x._object
        else : x = c_void_p()
        if y : y = y._object
        else : y = c_void_p()

        libgtk3.pango_matrix_transform_point.argtypes = [c_void_p, POITNER(double),POITNER(double)]
        
        libgtk3.pango_matrix_transform_point(self._object,  x, y,)

    def scale(self,  scale_x, scale_y,):

        libgtk3.pango_matrix_scale.argtypes = [c_void_p, double,double]
        
        libgtk3.pango_matrix_scale(self._object,  scale_x, scale_y,)

    def copy(self, ):

        libgtk3.pango_matrix_copy.restype = _PangoMatrix
        libgtk3.pango_matrix_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoMatrix
        return PangoMatrix(None, obj=libgtk3.pango_matrix_copy(self._object, )  or c_void_p())

    def get_font_scale_factor(self, ):

        libgtk3.pango_matrix_get_font_scale_factor.restype = double
        libgtk3.pango_matrix_get_font_scale_factor.argtypes = [c_void_p]
        
        return libgtk3.pango_matrix_get_font_scale_factor(self._object, )

    def free(self, ):

        libgtk3.pango_matrix_free.argtypes = [c_void_p]
        
        libgtk3.pango_matrix_free(self._object, )

    def concat(self,  new_matrix,):
        if new_matrix : new_matrix = new_matrix._object
        else : new_matrix = c_void_p()

        libgtk3.pango_matrix_concat.argtypes = [c_void_p, _PangoMatrix]
        
        libgtk3.pango_matrix_concat(self._object,  new_matrix,)

