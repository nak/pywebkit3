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
_GValue = c_void_p
__GValue = c_void_p
_gchar = c_void_p
"""Enumerations"""

class GValue( object):
    """Class GValue Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def g_strdup_value_contents(self, ):

        libgobject.g_strdup_value_contents.restype = _gchar
        libgobject.g_strdup_value_contents.argtypes = [c_void_p]
        
        return libgobject.g_strdup_value_contents(self._object, )

    def copy(self,  dest_value,):
        if dest_value : dest_value = dest_value._object
        else : dest_value = c_void_p()

        libgobject.g_value_copy.argtypes = [c_void_p, _GValue]
        
        libgobject.g_value_copy(self._object,  dest_value,)

    def transform(self,  dest_value,):
        if dest_value : dest_value = dest_value._object
        else : dest_value = c_void_p()

        libgobject.g_value_transform.restype = gboolean
        libgobject.g_value_transform.argtypes = [c_void_p, _GValue]
        
        return libgobject.g_value_transform(self._object,  dest_value,)

    def unset(self, ):

        libgobject.g_value_unset.argtypes = [c_void_p]
        
        libgobject.g_value_unset(self._object, )

    def init(self,  g_type,):

        libgobject.g_value_init.restype = _GValue
        libgobject.g_value_init.argtypes = [c_void_p, GType]
        from pywebkit3.gobject import GValue
        libgobject.g_value_init(self._object,  g_type)

    def peek_pointer(self, ):

        libgobject.g_value_peek_pointer.restype = gpointer
        libgobject.g_value_peek_pointer.argtypes = [c_void_p]
        
        return libgobject.g_value_peek_pointer(self._object, )

    def register_transform_func(self,  src_type, dest_type, transform_func,):

        libgobject.g_value_register_transform_func.argtypes = [c_void_p, GType,GType,GValueTransform]
        
        libgobject.g_value_register_transform_func(self._object,  src_type, dest_type, transform_func,)

    def reset(self, ):

        libgobject.g_value_reset.restype = _GValue
        libgobject.g_value_reset.argtypes = [c_void_p]
        from pywebkit3.gobject import GValue
        return GValue(obj=libgobject.g_value_reset(self._object, ) or c_void_p())

    def set_instance(self,  instance,):

        libgobject.g_value_set_instance.argtypes = [c_void_p, gpointer]
        
        libgobject.g_value_set_instance(self._object,  instance,)

    def set_int(self,  val,):

        libgobject.g_value_set_int.argtypes = [c_void_p, gint]
        
        libgobject.g_value_set_int(self._object,  val,)

    def fits_pointer(self, ):

        libgobject.g_value_fits_pointer.restype = gboolean
        libgobject.g_value_fits_pointer.argtypes = [c_void_p]
        
        return libgobject.g_value_fits_pointer(self._object, )

    @staticmethod
    def type_compatible( src_type, dest_type,):
        libgobject.g_value_type_compatible.restype = gboolean
        libgobject.g_value_type_compatible.argtypes = [GType,GType]
        return libgobject.g_value_type_compatible(src_type, dest_type, )

    @staticmethod
    def type_transformable( src_type, dest_type,):
        libgobject.g_value_type_transformable.restype = gboolean
        libgobject.g_value_type_transformable.argtypes = [GType,GType]
        return libgobject.g_value_type_transformable(src_type, dest_type, )

    def __init__(self, type, obj=None):
        cdll.LoadLibrary('libc.so.6')
        libc = CDLL('libc.so.6')
        libc.restype = c_void_p
        self._object = libc.malloc(64)
        libc.memset.argtypes = [c_void_p, c_int, c_int]
        libc.memset( self._object, 0, 64)
        self.init( libgobject.g_type_fundamental( type )  )
