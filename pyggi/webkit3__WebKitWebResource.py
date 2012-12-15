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
_WebKitWebResource = POINTER(c_int)
"""Enumerations"""

import gobject__GObject
class WebKitWebResource( gobject__GObject.GObject):
    """Class WebKitWebResource Constructors"""
    def __init__( self, frame_name,  obj = None):
        if obj: self._object = obj
        else:
            libwebkit3.webkit_web_resource_new.restype = POINTER(c_int)
            
            libwebkit3.webkit_web_resource_new.argtypes = [c_char_p]
            self._object = libwebkit3.webkit_web_resource_new(frame_name, )

    """Methods"""
    def get_frame_name(  self, ):

        libwebkit3.webkit_web_resource_get_frame_name.restype = c_char_p
        libwebkit3.webkit_web_resource_get_frame_name.argtypes = [_WebKitWebResource]
        
        return libwebkit3.webkit_web_resource_get_frame_name( self._object )

    def get_mime_type(  self, ):

        libwebkit3.webkit_web_resource_get_mime_type.restype = c_char_p
        libwebkit3.webkit_web_resource_get_mime_type.argtypes = [_WebKitWebResource]
        
        return libwebkit3.webkit_web_resource_get_mime_type( self._object )

    def get_encoding(  self, ):

        libwebkit3.webkit_web_resource_get_encoding.restype = c_char_p
        libwebkit3.webkit_web_resource_get_encoding.argtypes = [_WebKitWebResource]
        
        return libwebkit3.webkit_web_resource_get_encoding( self._object )

    def get_uri(  self, ):

        libwebkit3.webkit_web_resource_get_uri.restype = c_char_p
        libwebkit3.webkit_web_resource_get_uri.argtypes = [_WebKitWebResource]
        
        return libwebkit3.webkit_web_resource_get_uri( self._object )

