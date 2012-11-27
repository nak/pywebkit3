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
from webkit3_types import *
    
    
"""Derived Pointer Types"""
_WebKitNetworkResponse = c_void_p
_WebKitWebWindowFeatures = c_void_p
_GdkPixbuf = c_void_p
_WebKitWebFrame = c_void_p
_GList = c_void_p
_char = c_void_p
_GtkTargetList = c_void_p
_GtkWidget = c_void_p
_JSGlobalContext = c_void_p
__WebKitDOMNode = c_void_p
_WebKitSecurityOrigin = c_void_p
__WebKitNetworkRequest = c_void_p
_JSContext = c_void_p
_SoupMessage = c_void_p
_WebKitWebDataSource = c_void_p
_WebKitWebSettings = c_void_p
__WebKitWebHistoryItem = c_void_p
__GList = c_void_p
__WebKitWebWindowFeatures = c_void_p
_WebKitWebHistoryItem = c_void_p
__GdkEventButton = c_void_p
_WebKitViewportAttributes = c_void_p
_WebKitWebInspector = c_void_p
__GError = c_void_p
__WebKitWebSettings = c_void_p
_gchar = c_void_p
__WebKitWebView = c_void_p
_guchar = c_void_p
_WebKitHitTestResult = c_void_p
_WebKitDOMDocument = c_void_p
__GtkPrintOperation = c_void_p
_WebKitWebBackForwardList = c_void_p
_WebKitWebView = c_void_p
"""Enumerations"""
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitLoadStatus = c_int
WebKitEditingBehavior = c_int
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

        libwebkit3.gdk_pixbuf_get_bits_per_sample.restype = int
        libwebkit3.gdk_pixbuf_get_bits_per_sample.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_bits_per_sample(self._object, )

    def get_pixels(self, ):

        libwebkit3.gdk_pixbuf_get_pixels.restype = _guchar
        libwebkit3.gdk_pixbuf_get_pixels.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_pixels(self._object, )

    def get_pixels_with_length(self,  length,):
        if length : length = length._object
        else : length = c_void_p()

        libwebkit3.gdk_pixbuf_get_pixels_with_length.restype = _guchar
        libwebkit3.gdk_pixbuf_get_pixels_with_length.argtypes = [c_void_p, POITNER(guint)]
        
        return libwebkit3.gdk_pixbuf_get_pixels_with_length(self._object,  length,)

    def get_rowstride(self, ):

        libwebkit3.gdk_pixbuf_get_rowstride.restype = int
        libwebkit3.gdk_pixbuf_get_rowstride.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_rowstride(self._object, )

    def get_height(self, ):

        libwebkit3.gdk_pixbuf_get_height.restype = int
        libwebkit3.gdk_pixbuf_get_height.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_height(self._object, )

    def get_byte_length(self, ):

        libwebkit3.gdk_pixbuf_get_byte_length.restype = gsize
        libwebkit3.gdk_pixbuf_get_byte_length.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_byte_length(self._object, )

    def get_n_channels(self, ):

        libwebkit3.gdk_pixbuf_get_n_channels.restype = int
        libwebkit3.gdk_pixbuf_get_n_channels.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_n_channels(self._object, )

    def get_has_alpha(self, ):

        libwebkit3.gdk_pixbuf_get_has_alpha.restype = gboolean
        libwebkit3.gdk_pixbuf_get_has_alpha.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_has_alpha(self._object, )

    def get_width(self, ):

        libwebkit3.gdk_pixbuf_get_width.restype = int
        libwebkit3.gdk_pixbuf_get_width.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_width(self._object, )

    def get_option(self,  key,):

        libwebkit3.gdk_pixbuf_get_option.restype = _gchar
        libwebkit3.gdk_pixbuf_get_option.argtypes = [c_void_p, c_char_p]
        
        return libwebkit3.gdk_pixbuf_get_option(self._object,  key,)

    def get_colorspace(self, ):

        libwebkit3.gdk_pixbuf_get_colorspace.restype = GdkColorspace
        libwebkit3.gdk_pixbuf_get_colorspace.argtypes = [c_void_p]
        
        return libwebkit3.gdk_pixbuf_get_colorspace(self._object, )

