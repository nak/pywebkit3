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
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GValue = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
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

libgtk3.gdk_pixbuf_get_bits_per_sample.restype = int
libgtk3.gdk_pixbuf_get_bits_per_sample.argtypes = [_GdkPixbuf]
libgtk3.gdk_pixbuf_get_pixels.restype = POINTER(guchar)
libgtk3.gdk_pixbuf_get_pixels.argtypes = [_GdkPixbuf]
libgtk3.gdk_pixbuf_get_pixels_with_length.restype = POINTER(guchar)
libgtk3.gdk_pixbuf_get_pixels_with_length.argtypes = [_GdkPixbuf,POINTER(guint)]
libgtk3.gdk_pixbuf_get_rowstride.restype = int
libgtk3.gdk_pixbuf_get_rowstride.argtypes = [_GdkPixbuf]
libgtk3.gdk_pixbuf_get_height.restype = int
libgtk3.gdk_pixbuf_get_height.argtypes = [_GdkPixbuf]
libgtk3.gdk_pixbuf_get_byte_length.restype = gsize
libgtk3.gdk_pixbuf_get_byte_length.argtypes = [_GdkPixbuf]
libgtk3.gdk_pixbuf_get_n_channels.restype = int
libgtk3.gdk_pixbuf_get_n_channels.argtypes = [_GdkPixbuf]
libgtk3.gdk_pixbuf_get_has_alpha.restype = gboolean
libgtk3.gdk_pixbuf_get_has_alpha.argtypes = [_GdkPixbuf]
libgtk3.gdk_pixbuf_get_width.restype = int
libgtk3.gdk_pixbuf_get_width.argtypes = [_GdkPixbuf]
libgtk3.gdk_pixbuf_get_option.restype = c_char_p
libgtk3.gdk_pixbuf_get_option.argtypes = [_GdkPixbuf,c_char_p]
libgtk3.gdk_pixbuf_get_colorspace.restype = GdkColorspace
libgtk3.gdk_pixbuf_get_colorspace.argtypes = [_GdkPixbuf]
import gobject__GObject
class GdkPixbuf( gobject__GObject.GObject):
    """Class GdkPixbuf Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_bits_per_sample(  self, ):

        
        return libgtk3.gdk_pixbuf_get_bits_per_sample( self._object )

    def get_pixels(  self, ):

        
        return libgtk3.gdk_pixbuf_get_pixels( self._object )

    def get_pixels_with_length(  self, length, ):

        
        return libgtk3.gdk_pixbuf_get_pixels_with_length( self._object,length )

    def get_rowstride(  self, ):

        
        return libgtk3.gdk_pixbuf_get_rowstride( self._object )

    def get_height(  self, ):

        
        return libgtk3.gdk_pixbuf_get_height( self._object )

    def get_byte_length(  self, ):

        
        return libgtk3.gdk_pixbuf_get_byte_length( self._object )

    def get_n_channels(  self, ):

        
        return libgtk3.gdk_pixbuf_get_n_channels( self._object )

    def get_has_alpha(  self, ):

        
        return libgtk3.gdk_pixbuf_get_has_alpha( self._object )

    def get_width(  self, ):

        
        return libgtk3.gdk_pixbuf_get_width( self._object )

    def get_option(  self, key, ):

        
        return libgtk3.gdk_pixbuf_get_option( self._object,key )

    def get_colorspace(  self, ):

        
        return libgtk3.gdk_pixbuf_get_colorspace( self._object )

