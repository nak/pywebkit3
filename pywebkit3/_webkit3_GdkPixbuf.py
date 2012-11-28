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
_GdkVisual = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GActionGroup = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
_JSContext = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
__GList = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
__GCancellable = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_GBytes = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
__GFile = POINTER(c_int)
__GError = POINTER(c_int)
__GtkPrintOperation = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GByteArray = POINTER(c_int)
"""Enumerations"""
GdkVisualType = c_int
GdkByteOrder = c_int
GApplicationFlags = c_int
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
    def get_bits_per_sample(  self, ):

        libwebkit3.gdk_pixbuf_get_bits_per_sample.restype = int
        libwebkit3.gdk_pixbuf_get_bits_per_sample.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_bits_per_sample( self._object )

    def get_pixels(  self, ):

        libwebkit3.gdk_pixbuf_get_pixels.restype = POINTER(guchar)
        libwebkit3.gdk_pixbuf_get_pixels.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_pixels( self._object )

    def get_pixels_with_length(  self, length, ):

        libwebkit3.gdk_pixbuf_get_pixels_with_length.restype = POINTER(guchar)
        libwebkit3.gdk_pixbuf_get_pixels_with_length.argtypes = [_GdkPixbuf,POINTER(guint)]
        
        return libwebkit3.gdk_pixbuf_get_pixels_with_length( self._object,length )

    def get_rowstride(  self, ):

        libwebkit3.gdk_pixbuf_get_rowstride.restype = int
        libwebkit3.gdk_pixbuf_get_rowstride.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_rowstride( self._object )

    def get_height(  self, ):

        libwebkit3.gdk_pixbuf_get_height.restype = int
        libwebkit3.gdk_pixbuf_get_height.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_height( self._object )

    def get_byte_length(  self, ):

        libwebkit3.gdk_pixbuf_get_byte_length.restype = gsize
        libwebkit3.gdk_pixbuf_get_byte_length.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_byte_length( self._object )

    def get_n_channels(  self, ):

        libwebkit3.gdk_pixbuf_get_n_channels.restype = int
        libwebkit3.gdk_pixbuf_get_n_channels.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_n_channels( self._object )

    def get_has_alpha(  self, ):

        libwebkit3.gdk_pixbuf_get_has_alpha.restype = gboolean
        libwebkit3.gdk_pixbuf_get_has_alpha.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_has_alpha( self._object )

    def get_width(  self, ):

        libwebkit3.gdk_pixbuf_get_width.restype = int
        libwebkit3.gdk_pixbuf_get_width.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_width( self._object )

    def get_option(  self, key, ):

        libwebkit3.gdk_pixbuf_get_option.restype = c_char_p
        libwebkit3.gdk_pixbuf_get_option.argtypes = [_GdkPixbuf,c_char_p]
        
        return libwebkit3.gdk_pixbuf_get_option( self._object,key )

    def get_colorspace(  self, ):

        libwebkit3.gdk_pixbuf_get_colorspace.restype = GdkColorspace
        libwebkit3.gdk_pixbuf_get_colorspace.argtypes = [_GdkPixbuf]
        
        return libwebkit3.gdk_pixbuf_get_colorspace( self._object )

