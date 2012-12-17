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
_PangoContext = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_GList = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GIcon = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GValue = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkDevice = POINTER(c_int)
"""Enumerations"""
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

libgtk3.gdk_visual_get_colormap_size.restype = gint
libgtk3.gdk_visual_get_colormap_size.argtypes = [_GdkVisual]
libgtk3.gdk_visual_get_green_pixel_details.restype = None
libgtk3.gdk_visual_get_green_pixel_details.argtypes = [_GdkVisual,POINTER(guint32),POINTER(gint),POINTER(gint)]
libgtk3.gdk_query_depths.restype = None
libgtk3.gdk_query_depths.argtypes = [_GdkVisual,POINTER(gint),POINTER(gint)]
libgtk3.gdk_visual_get_depth.restype = gint
libgtk3.gdk_visual_get_depth.argtypes = [_GdkVisual]
libgtk3.gdk_visual_get_visual_type.restype = GdkVisualType
libgtk3.gdk_visual_get_visual_type.argtypes = [_GdkVisual]
libgtk3.gdk_query_visual_types.restype = None
libgtk3.gdk_query_visual_types.argtypes = [_GdkVisual,POINTER(GdkVisualType),POINTER(gint)]
libgtk3.gdk_visual_get_red_pixel_details.restype = None
libgtk3.gdk_visual_get_red_pixel_details.argtypes = [_GdkVisual,POINTER(guint32),POINTER(gint),POINTER(gint)]
libgtk3.gdk_visual_get_bits_per_rgb.restype = gint
libgtk3.gdk_visual_get_bits_per_rgb.argtypes = [_GdkVisual]
libgtk3.gdk_visual_get_blue_pixel_details.restype = None
libgtk3.gdk_visual_get_blue_pixel_details.argtypes = [_GdkVisual,POINTER(guint32),POINTER(gint),POINTER(gint)]
libgtk3.gdk_visual_get_byte_order.restype = GdkByteOrder
libgtk3.gdk_visual_get_byte_order.argtypes = [_GdkVisual]
libgtk3.gdk_screen_get_rgba_visual.restype = _GdkVisual
libgtk3.gdk_screen_get_rgba_visual.argtypes = [_GdkScreen]
libgtk3.gdk_visual_get_best_with_both.restype = _GdkVisual
libgtk3.gdk_visual_get_best_with_both.argtypes = [gint,GdkVisualType]
libgtk3.gdk_visual_get_best_depth.restype = gint
libgtk3.gdk_visual_get_best_depth.argtypes = []
libgtk3.gdk_visual_get_best_with_depth.restype = _GdkVisual
libgtk3.gdk_visual_get_best_with_depth.argtypes = [gint]
libgtk3.gdk_visual_get_system.restype = _GdkVisual
libgtk3.gdk_visual_get_system.argtypes = []
libgtk3.gdk_visual_get_best_with_type.restype = _GdkVisual
libgtk3.gdk_visual_get_best_with_type.argtypes = [GdkVisualType]
libgtk3.gdk_visual_get_best_type.restype = GdkVisualType
libgtk3.gdk_visual_get_best_type.argtypes = []
libgtk3.gdk_visual_get_best.restype = _GdkVisual
libgtk3.gdk_visual_get_best.argtypes = []
libgtk3.gdk_list_visuals.restype = _GList
libgtk3.gdk_list_visuals.argtypes = []
libgtk3.gdk_screen_get_system_visual.restype = _GdkVisual
libgtk3.gdk_screen_get_system_visual.argtypes = [_GdkScreen]
import gobject__GObject
class GdkVisual( gobject__GObject.GObject):
    """Class GdkVisual Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_colormap_size(  self, ):

        
        return libgtk3.gdk_visual_get_colormap_size( self._object )

    def get_green_pixel_details(  self, mask, shift, precision, ):

        
        libgtk3.gdk_visual_get_green_pixel_details( self._object,mask,shift,precision )

    def gdk_query_depths(  self, depths, count, ):

        
        libgtk3.gdk_query_depths( self._object,depths,count )

    def get_depth(  self, ):

        
        return libgtk3.gdk_visual_get_depth( self._object )

    def get_visual_type(  self, ):

        
        return libgtk3.gdk_visual_get_visual_type( self._object )

    def gdk_query_visual_types(  self, visual_types, count, ):

        
        libgtk3.gdk_query_visual_types( self._object,visual_types,count )

    def get_red_pixel_details(  self, mask, shift, precision, ):

        
        libgtk3.gdk_visual_get_red_pixel_details( self._object,mask,shift,precision )

    def get_bits_per_rgb(  self, ):

        
        return libgtk3.gdk_visual_get_bits_per_rgb( self._object )

    def get_blue_pixel_details(  self, mask, shift, precision, ):

        
        libgtk3.gdk_visual_get_blue_pixel_details( self._object,mask,shift,precision )

    def get_byte_order(  self, ):

        
        return libgtk3.gdk_visual_get_byte_order( self._object )

    @staticmethod
    def gdk_screen_get_rgba_visual( screen,):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()
        from gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_screen_get_rgba_visual(screen, )
 or POINTER(c_int)())
    @staticmethod
    def get_best_with_both( depth, visual_type,):
        from gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_best_with_both(depth, visual_type, )
 or POINTER(c_int)())
    @staticmethod
    def get_best_depth():
        
        return     libgtk3.gdk_visual_get_best_depth()

    @staticmethod
    def get_best_with_depth( depth,):
        from gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_best_with_depth(depth, )
 or POINTER(c_int)())
    @staticmethod
    def get_system():
        from gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_system()
 or POINTER(c_int)())
    @staticmethod
    def get_best_with_type( visual_type,):
        from gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_best_with_type(visual_type, )
 or POINTER(c_int)())
    @staticmethod
    def get_best_type():
        
        return     libgtk3.gdk_visual_get_best_type()

    @staticmethod
    def get_best():
        from gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_visual_get_best()
 or POINTER(c_int)())
    @staticmethod
    def gdk_list_visuals():
        from gobject import GList
        return GList( obj=    libgtk3.gdk_list_visuals()
 or POINTER(c_int)())
    @staticmethod
    def gdk_screen_get_system_visual( screen,):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()
        from gobject import GdkVisual
        return GdkVisual( obj=    libgtk3.gdk_screen_get_system_visual(screen, )
 or POINTER(c_int)())
