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
__GtkRcStyle = c_void_p
__GdkGeometry = c_void_p
__GParamSpec = c_void_p
_GdkVisual = c_void_p
_GtkWindow = c_void_p
__GList = c_void_p
__GdkTimeCoord = c_void_p
_GdkPixbuf = c_void_p
_GParamSpec = c_void_p
_GList = c_void_p
__GtkWindow = c_void_p
__GtkRequisition = c_void_p
__GdkDisplay = c_void_p
_GtkRcStyle = c_void_p
_GtkWindowGroup = c_void_p
_GtkWidget = c_void_p
_GdkEvent = c_void_p
__GdkWindow = c_void_p
__cairo_font_options_t = c_void_p
_GdkDevice = c_void_p
__GdkWindowAttr = c_void_p
__GdkAtom = c_void_p
_GtkIconSet = c_void_p
__GValue = c_void_p
__cairo_region_t = c_void_p
__GdkColor = c_void_p
_GdkWindow = c_void_p
__PangoFontDescription = c_void_p
__GdkRectangle = c_void_p
__cairo_pattern_t = c_void_p
_PangoContext = c_void_p
__GdkWMDecoration = c_void_p
_GdkDeviceManager = c_void_p
_PangoLayout = c_void_p
__cairo_t = c_void_p
__GdkVisual = c_void_p
_GtkApplication = c_void_p
__GIcon = c_void_p
_GdkDisplay = c_void_p
__GtkIconSource = c_void_p
__GdkCursor = c_void_p
__GtkAccelGroup = c_void_p
_GtkStyle = c_void_p
__GtkStyle = c_void_p
__GdkRGBA = c_void_p
__GError = c_void_p
__GdkPixbuf = c_void_p
_GtkStyleContext = c_void_p
__GtkAllocation = c_void_p
__GtkWidget = c_void_p
_GtkWidgetPath = c_void_p
_gchar = c_void_p
__GtkWidgetClass = c_void_p
_guchar = c_void_p
_GdkScreen = c_void_p
__GdkEventKey = c_void_p
__GtkApplication = c_void_p
_GtkClipboard = c_void_p
_GdkAppLaunchContext = c_void_p
_GdkCursor = c_void_p
__PangoLayout = c_void_p
__GdkScreen = c_void_p
_GtkSettings = c_void_p
__GdkDevice = c_void_p
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

import _gobject_GObject
class GdkVisual( _gobject_GObject.GObject):
    """Class GdkVisual Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_colormap_size(self, ):

        libgtk3.gdk_visual_get_colormap_size.restype = gint
        libgtk3.gdk_visual_get_colormap_size.argtypes = [c_void_p]
        
        return libgtk3.gdk_visual_get_colormap_size(self._object, )

    def get_green_pixel_details(self,  mask, shift, precision,):
        if mask : mask = mask._object
        else : mask = c_void_p()
        if shift : shift = shift._object
        else : shift = c_void_p()
        if precision : precision = precision._object
        else : precision = c_void_p()

        libgtk3.gdk_visual_get_green_pixel_details.argtypes = [c_void_p, POITNER(guint32),POITNER(gint),POITNER(gint)]
        
        libgtk3.gdk_visual_get_green_pixel_details(self._object,  mask, shift, precision,)

    def gdk_query_depths(self,  depths, count,):
        if depths : depths = depths._object
        else : depths = c_void_p()
        if count : count = count._object
        else : count = c_void_p()

        libgtk3.gdk_query_depths.argtypes = [c_void_p, POITNER(gint),POITNER(gint)]
        
        libgtk3.gdk_query_depths(self._object,  depths, count,)

    def get_depth(self, ):

        libgtk3.gdk_visual_get_depth.restype = gint
        libgtk3.gdk_visual_get_depth.argtypes = [c_void_p]
        
        return libgtk3.gdk_visual_get_depth(self._object, )

    def get_visual_type(self, ):

        libgtk3.gdk_visual_get_visual_type.restype = GdkVisualType
        libgtk3.gdk_visual_get_visual_type.argtypes = [c_void_p]
        
        return libgtk3.gdk_visual_get_visual_type(self._object, )

    def gdk_query_visual_types(self,  visual_types, count,):
        if visual_types : visual_types = visual_types._object
        else : visual_types = c_void_p()
        if count : count = count._object
        else : count = c_void_p()

        libgtk3.gdk_query_visual_types.argtypes = [c_void_p, POITNER(GdkVisualType),POITNER(gint)]
        
        libgtk3.gdk_query_visual_types(self._object,  visual_types, count,)

    def get_red_pixel_details(self,  mask, shift, precision,):
        if mask : mask = mask._object
        else : mask = c_void_p()
        if shift : shift = shift._object
        else : shift = c_void_p()
        if precision : precision = precision._object
        else : precision = c_void_p()

        libgtk3.gdk_visual_get_red_pixel_details.argtypes = [c_void_p, POITNER(guint32),POITNER(gint),POITNER(gint)]
        
        libgtk3.gdk_visual_get_red_pixel_details(self._object,  mask, shift, precision,)

    def get_bits_per_rgb(self, ):

        libgtk3.gdk_visual_get_bits_per_rgb.restype = gint
        libgtk3.gdk_visual_get_bits_per_rgb.argtypes = [c_void_p]
        
        return libgtk3.gdk_visual_get_bits_per_rgb(self._object, )

    def get_blue_pixel_details(self,  mask, shift, precision,):
        if mask : mask = mask._object
        else : mask = c_void_p()
        if shift : shift = shift._object
        else : shift = c_void_p()
        if precision : precision = precision._object
        else : precision = c_void_p()

        libgtk3.gdk_visual_get_blue_pixel_details.argtypes = [c_void_p, POITNER(guint32),POITNER(gint),POITNER(gint)]
        
        libgtk3.gdk_visual_get_blue_pixel_details(self._object,  mask, shift, precision,)

    def get_byte_order(self, ):

        libgtk3.gdk_visual_get_byte_order.restype = GdkByteOrder
        libgtk3.gdk_visual_get_byte_order.argtypes = [c_void_p]
        
        return libgtk3.gdk_visual_get_byte_order(self._object, )

    @staticmethod
    def gdk_screen_get_rgba_visual( screen,):
        if screen : screen = screen._object
        else : screen = c_void_p()
        libgtk3.gdk_screen_get_rgba_visual.restype = _GdkVisual
        libgtk3.gdk_screen_get_rgba_visual.argtypes = [_GdkScreen]
        return libgtk3.gdk_screen_get_rgba_visual(screen, )

    @staticmethod
    def get_best_with_both( depth, visual_type,):
        libgtk3.gdk_visual_get_best_with_both.restype = _GdkVisual
        libgtk3.gdk_visual_get_best_with_both.argtypes = [gint,GdkVisualType]
        return libgtk3.gdk_visual_get_best_with_both(depth, visual_type, )

    @staticmethod
    def get_best_depth():
        libgtk3.gdk_visual_get_best_depth.restype = gint
        return libgtk3.gdk_visual_get_best_depth()

    @staticmethod
    def get_best_with_depth( depth,):
        libgtk3.gdk_visual_get_best_with_depth.restype = _GdkVisual
        libgtk3.gdk_visual_get_best_with_depth.argtypes = [gint]
        return libgtk3.gdk_visual_get_best_with_depth(depth, )

    @staticmethod
    def get_system():
        libgtk3.gdk_visual_get_system.restype = _GdkVisual
        return libgtk3.gdk_visual_get_system()

    @staticmethod
    def get_best_with_type( visual_type,):
        libgtk3.gdk_visual_get_best_with_type.restype = _GdkVisual
        libgtk3.gdk_visual_get_best_with_type.argtypes = [GdkVisualType]
        return libgtk3.gdk_visual_get_best_with_type(visual_type, )

    @staticmethod
    def get_best_type():
        libgtk3.gdk_visual_get_best_type.restype = GdkVisualType
        return libgtk3.gdk_visual_get_best_type()

    @staticmethod
    def get_best():
        libgtk3.gdk_visual_get_best.restype = _GdkVisual
        return libgtk3.gdk_visual_get_best()

    @staticmethod
    def gdk_list_visuals():
        libgtk3.gdk_list_visuals.restype = _GList
        return libgtk3.gdk_list_visuals()

    @staticmethod
    def gdk_screen_get_system_visual( screen,):
        if screen : screen = screen._object
        else : screen = c_void_p()
        libgtk3.gdk_screen_get_system_visual.restype = _GdkVisual
        libgtk3.gdk_screen_get_system_visual.argtypes = [_GdkScreen]
        return libgtk3.gdk_screen_get_system_visual(screen, )

