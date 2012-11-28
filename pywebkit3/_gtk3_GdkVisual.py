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
__GdkScreen = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GList = POINTER(c_int)
"""Enumerations"""
GdkVisualType = c_int
GdkByteOrder = c_int

import _gobject_GObject
class GdkVisual( _gobject_GObject.GObject):
    """Class GdkVisual Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_colormap_size(  self, ):

        libgtk3.gdk_visual_get_colormap_size.restype = gint
        libgtk3.gdk_visual_get_colormap_size.argtypes = [_GdkVisual]
        
        return libgtk3.gdk_visual_get_colormap_size( self._object )

    def get_green_pixel_details(  self, mask, shift, precision, ):

        libgtk3.gdk_visual_get_green_pixel_details.argtypes = [_GdkVisual,POINTER(guint32),POINTER(gint),POINTER(gint)]
        
        libgtk3.gdk_visual_get_green_pixel_details( self._object,mask,shift,precision )

    def gdk_query_depths(  self, depths, count, ):

        libgtk3.gdk_query_depths.argtypes = [_GdkVisual,POINTER(gint),POINTER(gint)]
        
        libgtk3.gdk_query_depths( self._object,depths,count )

    def get_depth(  self, ):

        libgtk3.gdk_visual_get_depth.restype = gint
        libgtk3.gdk_visual_get_depth.argtypes = [_GdkVisual]
        
        return libgtk3.gdk_visual_get_depth( self._object )

    def get_visual_type(  self, ):

        libgtk3.gdk_visual_get_visual_type.restype = GdkVisualType
        libgtk3.gdk_visual_get_visual_type.argtypes = [_GdkVisual]
        
        return libgtk3.gdk_visual_get_visual_type( self._object )

    def gdk_query_visual_types(  self, visual_types, count, ):

        libgtk3.gdk_query_visual_types.argtypes = [_GdkVisual,POINTER(GdkVisualType),POINTER(gint)]
        
        libgtk3.gdk_query_visual_types( self._object,visual_types,count )

    def get_red_pixel_details(  self, mask, shift, precision, ):

        libgtk3.gdk_visual_get_red_pixel_details.argtypes = [_GdkVisual,POINTER(guint32),POINTER(gint),POINTER(gint)]
        
        libgtk3.gdk_visual_get_red_pixel_details( self._object,mask,shift,precision )

    def get_bits_per_rgb(  self, ):

        libgtk3.gdk_visual_get_bits_per_rgb.restype = gint
        libgtk3.gdk_visual_get_bits_per_rgb.argtypes = [_GdkVisual]
        
        return libgtk3.gdk_visual_get_bits_per_rgb( self._object )

    def get_blue_pixel_details(  self, mask, shift, precision, ):

        libgtk3.gdk_visual_get_blue_pixel_details.argtypes = [_GdkVisual,POINTER(guint32),POINTER(gint),POINTER(gint)]
        
        libgtk3.gdk_visual_get_blue_pixel_details( self._object,mask,shift,precision )

    def get_byte_order(  self, ):

        libgtk3.gdk_visual_get_byte_order.restype = GdkByteOrder
        libgtk3.gdk_visual_get_byte_order.argtypes = [_GdkVisual]
        
        return libgtk3.gdk_visual_get_byte_order( self._object )

    @staticmethod
    def gdk_screen_get_rgba_visual( screen,):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()
        libgtk3.gdk_screen_get_rgba_visual.restype = _GdkVisual
        libgtk3.gdk_screen_get_rgba_visual.argtypes = [_GdkScreen]
        from pywebkit3.gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_screen_get_rgba_visual(screen, )
 or POINTER(c_int)())
    @staticmethod
    def get_best_with_both( depth, visual_type,):
        libgtk3.gdk_visual_get_best_with_both.restype = _GdkVisual
        libgtk3.gdk_visual_get_best_with_both.argtypes = [gint,GdkVisualType]
        from pywebkit3.gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_best_with_both(depth, visual_type, )
 or POINTER(c_int)())
    @staticmethod
    def get_best_depth():
        libgtk3.gdk_visual_get_best_depth.restype = gint
        
        return     libgtk3.gdk_visual_get_best_depth()

    @staticmethod
    def get_best_with_depth( depth,):
        libgtk3.gdk_visual_get_best_with_depth.restype = _GdkVisual
        libgtk3.gdk_visual_get_best_with_depth.argtypes = [gint]
        from pywebkit3.gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_best_with_depth(depth, )
 or POINTER(c_int)())
    @staticmethod
    def get_system():
        libgtk3.gdk_visual_get_system.restype = _GdkVisual
        from pywebkit3.gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_system()
 or POINTER(c_int)())
    @staticmethod
    def get_best_with_type( visual_type,):
        libgtk3.gdk_visual_get_best_with_type.restype = _GdkVisual
        libgtk3.gdk_visual_get_best_with_type.argtypes = [GdkVisualType]
        from pywebkit3.gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_best_with_type(visual_type, )
 or POINTER(c_int)())
    @staticmethod
    def get_best_type():
        libgtk3.gdk_visual_get_best_type.restype = GdkVisualType
        
        return     libgtk3.gdk_visual_get_best_type()

    @staticmethod
    def get_best():
        libgtk3.gdk_visual_get_best.restype = _GdkVisual
        from pywebkit3.gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_best()
 or POINTER(c_int)())
    @staticmethod
    def gdk_list_visuals():
        libgtk3.gdk_list_visuals.restype = _GList
        from pywebkit3.gobject import GList
        return GList( obj=    libgtk3.gdk_list_visuals()
 or POINTER(c_int)())
    @staticmethod
    def gdk_screen_get_system_visual( screen,):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()
        libgtk3.gdk_screen_get_system_visual.restype = _GdkVisual
        libgtk3.gdk_screen_get_system_visual.argtypes = [_GdkScreen]
        from pywebkit3.gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_screen_get_system_visual(screen, )
 or POINTER(c_int)())
