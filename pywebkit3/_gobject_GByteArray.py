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
_gchar = c_void_p
_GBytes = c_void_p
_GString = c_void_p
__GString = c_void_p
_GByteArray = c_void_p
_guint8 = c_void_p
"""Enumerations"""

class GByteArray( object):
    """Class GByteArray Constructors"""
    def __init__( self, reserved_size,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_byte_array_sized_new.restype = c_void_p

        libgobject.g_byte_array_sized_new.argtypes = [guint]
        self._object = libgobject.g_byte_array_sized_new(reserved_size, )

    """Methods"""
    def ref(self, ):

        libgobject.g_byte_array_ref.restype = _GByteArray
        libgobject.g_byte_array_ref.argtypes = [c_void_p]
        from pywebkit3.gobject import GByteArray
        return GByteArray(None, obj=libgobject.g_byte_array_ref(self._object, ) or c_void_p())

    def set_size(self,  length,):

        libgobject.g_byte_array_set_size.restype = _GByteArray
        libgobject.g_byte_array_set_size.argtypes = [c_void_p, guint]
        from pywebkit3.gobject import GByteArray
        return GByteArray(None,None, obj=libgobject.g_byte_array_set_size(self._object,  length,) or c_void_p())

    def remove_index_fast(self,  index_,):

        libgobject.g_byte_array_remove_index_fast.restype = _GByteArray
        libgobject.g_byte_array_remove_index_fast.argtypes = [c_void_p, guint]
        from pywebkit3.gobject import GByteArray
        return GByteArray(None,None, obj=libgobject.g_byte_array_remove_index_fast(self._object,  index_,) or c_void_p())

    def sort_with_data(self,  compare_func, user_data,):
        if compare_func : compare_func = compare_func._object
        else : compare_func = c_void_p()

        libgobject.g_byte_array_sort_with_data.argtypes = [c_void_p, GCompareDataFunc,gpointer]
        
        libgobject.g_byte_array_sort_with_data(self._object,  compare_func, user_data,)

    def sort(self,  compare_func,):
        if compare_func : compare_func = compare_func._object
        else : compare_func = c_void_p()

        libgobject.g_byte_array_sort.argtypes = [c_void_p, GCompareFunc]
        
        libgobject.g_byte_array_sort(self._object,  compare_func,)

    def unref(self, ):

        libgobject.g_byte_array_unref.argtypes = [c_void_p]
        
        libgobject.g_byte_array_unref(self._object, )

    def append(self,  data, len,):
        if data : data = data._object
        else : data = c_void_p()

        libgobject.g_byte_array_append.restype = _GByteArray
        libgobject.g_byte_array_append.argtypes = [c_void_p, POITNER(guint8),guint]
        from pywebkit3.gobject import GByteArray
        return GByteArray(None,None,None, obj=libgobject.g_byte_array_append(self._object,  data, len,) or c_void_p())

    def free(self,  free_segment,):

        libgobject.g_byte_array_free.restype = _guint8
        libgobject.g_byte_array_free.argtypes = [c_void_p, gboolean]
        
        return libgobject.g_byte_array_free(self._object,  free_segment,)

    def remove_index(self,  index_,):

        libgobject.g_byte_array_remove_index.restype = _GByteArray
        libgobject.g_byte_array_remove_index.argtypes = [c_void_p, guint]
        from pywebkit3.gobject import GByteArray
        return GByteArray(None,None, obj=libgobject.g_byte_array_remove_index(self._object,  index_,) or c_void_p())

    def remove_range(self,  index_, length,):

        libgobject.g_byte_array_remove_range.restype = _GByteArray
        libgobject.g_byte_array_remove_range.argtypes = [c_void_p, guint,guint]
        from pywebkit3.gobject import GByteArray
        return GByteArray(None,None,None, obj=libgobject.g_byte_array_remove_range(self._object,  index_, length,) or c_void_p())

    def prepend(self,  data, len,):
        if data : data = data._object
        else : data = c_void_p()

        libgobject.g_byte_array_prepend.restype = _GByteArray
        libgobject.g_byte_array_prepend.argtypes = [c_void_p, POITNER(guint8),guint]
        from pywebkit3.gobject import GByteArray
        return GByteArray(None,None,None, obj=libgobject.g_byte_array_prepend(self._object,  data, len,) or c_void_p())

    @staticmethod
    def new_take( data, len,):
        if data : data = data._object
        else : data = c_void_p()
        libgobject.g_byte_array_new_take.restype = _GByteArray
        libgobject.g_byte_array_new_take.argtypes = [POITNER(guint8),gsize]
        return libgobject.g_byte_array_new_take(data, len, )

