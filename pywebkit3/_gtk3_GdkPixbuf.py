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
_GdkPixbuf = c_void_p
_GParamSpec = c_void_p
_GList = c_void_p
__GtkWindow = c_void_p
__GtkRequisition = c_void_p
_GtkRcStyle = c_void_p
_GtkWindowGroup = c_void_p
_GtkWidget = c_void_p
__GdkWindow = c_void_p
_GtkIconSet = c_void_p
__GValue = c_void_p
__cairo_region_t = c_void_p
__GdkColor = c_void_p
_GdkWindow = c_void_p
__PangoFontDescription = c_void_p
__GdkRectangle = c_void_p
_PangoContext = c_void_p
_PangoLayout = c_void_p
__cairo_t = c_void_p
__GdkVisual = c_void_p
_GtkApplication = c_void_p
_GdkDisplay = c_void_p
__GtkIconSource = c_void_p
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

import _gobject_GObject
class GdkPixbuf( _gobject_GObject.GObject):
    """Class GdkPixbuf Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_bits_per_sample(self, ):

        libgtk3.gdk_pixbuf_get_bits_per_sample.restype = int
        libgtk3.gdk_pixbuf_get_bits_per_sample.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_bits_per_sample(self._object, )

    def get_pixels(self, ):

        libgtk3.gdk_pixbuf_get_pixels.restype = _guchar
        libgtk3.gdk_pixbuf_get_pixels.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_pixels(self._object, )

    def get_pixels_with_length(self,  length,):
        if length : length = length._object
        else : length = c_void_p()

        libgtk3.gdk_pixbuf_get_pixels_with_length.restype = _guchar
        libgtk3.gdk_pixbuf_get_pixels_with_length.argtypes = [c_void_p, POITNER(guint)]
        
        return libgtk3.gdk_pixbuf_get_pixels_with_length(self._object,  length,)

    def get_rowstride(self, ):

        libgtk3.gdk_pixbuf_get_rowstride.restype = int
        libgtk3.gdk_pixbuf_get_rowstride.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_rowstride(self._object, )

    def get_height(self, ):

        libgtk3.gdk_pixbuf_get_height.restype = int
        libgtk3.gdk_pixbuf_get_height.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_height(self._object, )

    def get_byte_length(self, ):

        libgtk3.gdk_pixbuf_get_byte_length.restype = gsize
        libgtk3.gdk_pixbuf_get_byte_length.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_byte_length(self._object, )

    def get_n_channels(self, ):

        libgtk3.gdk_pixbuf_get_n_channels.restype = int
        libgtk3.gdk_pixbuf_get_n_channels.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_n_channels(self._object, )

    def get_has_alpha(self, ):

        libgtk3.gdk_pixbuf_get_has_alpha.restype = gboolean
        libgtk3.gdk_pixbuf_get_has_alpha.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_has_alpha(self._object, )

    def get_width(self, ):

        libgtk3.gdk_pixbuf_get_width.restype = int
        libgtk3.gdk_pixbuf_get_width.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_width(self._object, )

    def get_option(self,  key,):

        libgtk3.gdk_pixbuf_get_option.restype = _gchar
        libgtk3.gdk_pixbuf_get_option.argtypes = [c_void_p, c_char_p]
        
        return libgtk3.gdk_pixbuf_get_option(self._object,  key,)

    def get_colorspace(self, ):

        libgtk3.gdk_pixbuf_get_colorspace.restype = GdkColorspace
        libgtk3.gdk_pixbuf_get_colorspace.argtypes = [c_void_p]
        
        return libgtk3.gdk_pixbuf_get_colorspace(self._object, )

