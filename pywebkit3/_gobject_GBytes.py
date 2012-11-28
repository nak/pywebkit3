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
from gobject_types import *
    
    
"""Derived Pointer Types"""
__GdkPixbuf = POINTER(c_int)
_GdkVisual = POINTER(c_int)
__GtkWidget = POINTER(c_int)
__GList = POINTER(c_int)
__GtkIconSet = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GList = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__GtkStyle = POINTER(c_int)
_GBytes = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_GByteArray = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
"""Enumerations"""
GdkVisualType = c_int
GdkByteOrder = c_int
GtkIconSize = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int

class GBytes( object):
    """Class GBytes Constructors"""
    def __init__( self, size,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_bytes_new.restype = POINTER(c_int)
            
            libgobject.g_bytes_new.argtypes = [gsize]
            self._object = libgobject.g_bytes_new(size, )

    """Methods"""
    def unref(  self, ):

        libgobject.g_bytes_unref.argtypes = [_GBytes]
        
        libgobject.g_bytes_unref( self._object )

    def get_data(  self, size, ):

        libgobject.g_bytes_get_data.restype = gpointer
        libgobject.g_bytes_get_data.argtypes = [_GBytes,POINTER(gsize)]
        
        return libgobject.g_bytes_get_data( self._object,size )

    def ref(  self, ):

        libgobject.g_bytes_ref.restype = _GBytes
        libgobject.g_bytes_ref.argtypes = [_GBytes]
        from pywebkit3.gobject import GBytes
        return GBytes( obj=libgobject.g_bytes_ref( self._object ) or POINTER(c_int)())

    def new_from_bytes(  self, offset, length, ):

        libgobject.g_bytes_new_from_bytes.restype = _GBytes
        libgobject.g_bytes_new_from_bytes.argtypes = [_GBytes,gsize,gsize]
        from pywebkit3.gobject import GBytes
        return GBytes(None,None, obj=libgobject.g_bytes_new_from_bytes( self._object,offset,length ) or POINTER(c_int)())

    def get_size(  self, ):

        libgobject.g_bytes_get_size.restype = gsize
        libgobject.g_bytes_get_size.argtypes = [_GBytes]
        
        return libgobject.g_bytes_get_size( self._object )

    def unref_to_array(  self, ):

        libgobject.g_bytes_unref_to_array.restype = _GByteArray
        libgobject.g_bytes_unref_to_array.argtypes = [_GBytes]
        from pywebkit3.gobject import GByteArray
        return GByteArray(None,None, obj=libgobject.g_bytes_unref_to_array( self._object ) or POINTER(c_int)())

    def unref_to_data(  self, size, ):

        libgobject.g_bytes_unref_to_data.restype = gpointer
        libgobject.g_bytes_unref_to_data.argtypes = [_GBytes,POINTER(gsize)]
        
        return libgobject.g_bytes_unref_to_data( self._object,size )

    @staticmethod
    def new_static( data, size,):
        libgobject.g_bytes_new_static.restype = _GBytes
        libgobject.g_bytes_new_static.argtypes = [gpointer,gsize]
        from pywebkit3.gobject import GBytes
        return GBytes(None, obj=    libgobject.g_bytes_new_static(data, size, )
 or POINTER(c_int)())
    @staticmethod
    def hash( bytes,):
        libgobject.g_bytes_hash.restype = guint
        libgobject.g_bytes_hash.argtypes = [gpointer]
        
        return     libgobject.g_bytes_hash(bytes, )

    @staticmethod
    def new_take( data, size,):
        libgobject.g_bytes_new_take.restype = _GBytes
        libgobject.g_bytes_new_take.argtypes = [gpointer,gsize]
        from pywebkit3.gobject import GBytes
        return GBytes(None, obj=    libgobject.g_bytes_new_take(data, size, )
 or POINTER(c_int)())
    @staticmethod
    def new_with_free_func( data, size, free_func, user_data,):
        libgobject.g_bytes_new_with_free_func.restype = _GBytes
        libgobject.g_bytes_new_with_free_func.argtypes = [gpointer,gsize,GDestroyNotify,gpointer]
        from pywebkit3.gobject import GBytes
        return GBytes(None, obj=    libgobject.g_bytes_new_with_free_func(data, size, free_func, user_data, )
 or POINTER(c_int)())
    @staticmethod
    def compare( bytes1, bytes2,):
        libgobject.g_bytes_compare.restype = gint
        libgobject.g_bytes_compare.argtypes = [gpointer,gpointer]
        
        return     libgobject.g_bytes_compare(bytes1, bytes2, )

    @staticmethod
    def equal( bytes1, bytes2,):
        libgobject.g_bytes_equal.restype = gboolean
        libgobject.g_bytes_equal.argtypes = [gpointer,gpointer]
        
        return     libgobject.g_bytes_equal(bytes1, bytes2, )

