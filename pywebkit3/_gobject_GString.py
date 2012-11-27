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
__GString = c_void_p
_GString = c_void_p
"""Enumerations"""

class GString( object):
    """Class GString Constructors"""
    def __init__( self, dfl_size,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_string_sized_new.restype = c_void_p

        libgobject.g_string_sized_new.argtypes = [gsize]
        self._object = libgobject.g_string_sized_new(dfl_size, )

    """Methods"""
    def append_c(self,  c,):

        libgobject.g_string_append_c.restype = _GString
        libgobject.g_string_append_c.argtypes = [c_void_p, gchar]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_append_c(self._object,  c,) or c_void_p())

    def prepend_c(self,  c,):

        libgobject.g_string_prepend_c.restype = _GString
        libgobject.g_string_prepend_c.argtypes = [c_void_p, gchar]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_prepend_c(self._object,  c,) or c_void_p())

    def equal(self,  v2,):
        if v2 : v2 = v2._object
        else : v2 = c_void_p()

        libgobject.g_string_equal.restype = gboolean
        libgobject.g_string_equal.argtypes = [c_void_p, _GString]
        
        return libgobject.g_string_equal(self._object,  v2,)

    def insert(self,  pos, val,):
        if pos : pos = pos._object
        else : pos = c_void_p()

        libgobject.g_string_insert.restype = _GString
        libgobject.g_string_insert.argtypes = [c_void_p, gssize,c_char_p]
        from pywebkit3.gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_insert(self._object,  pos, val,) or c_void_p())

    def set_size(self,  len,):

        libgobject.g_string_set_size.restype = _GString
        libgobject.g_string_set_size.argtypes = [c_void_p, gsize]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_set_size(self._object,  len,) or c_void_p())

    def append_printf(self,  format,*args ):


        def callit( format, *args ):
                libgobject.g_string_append_printf.restype = None
                libgobject.g_string_append_printf.argtypes = [c_void_p, c_void_p, c_char_p]
                for arg in args:
                     libgobject.g_string_append_printf.argtypes.append(args[1])
                return libgobject.g_string_append_printf(self._object, format, *args)
    
        return callit( format,*args )

    def free_to_bytes(self, ):

        libgobject.g_string_free_to_bytes.restype = _GBytes
        libgobject.g_string_free_to_bytes.argtypes = [c_void_p]
        from pywebkit3.gobject import GBytes
        return GBytes(None,None, obj=libgobject.g_string_free_to_bytes(self._object, ) or c_void_p())

    def append_uri_escaped(self,  unescaped, reserved_chars_allowed, allow_utf8,):

        libgobject.g_string_append_uri_escaped.restype = _GString
        libgobject.g_string_append_uri_escaped.argtypes = [c_void_p, c_char_p,c_char_p,gboolean]
        from pywebkit3.gobject import GString
        return GString(None,None,None,None, obj=libgobject.g_string_append_uri_escaped(self._object,  unescaped, reserved_chars_allowed, allow_utf8,) or c_void_p())

    def free(self,  free_segment,):

        libgobject.g_string_free.restype = _gchar
        libgobject.g_string_free.argtypes = [c_void_p, gboolean]
        
        return libgobject.g_string_free(self._object,  free_segment,)

    def up(self, ):

        libgobject.g_string_up.restype = _GString
        libgobject.g_string_up.argtypes = [c_void_p]
        from pywebkit3.gobject import GString
        return GString(None, obj=libgobject.g_string_up(self._object, ) or c_void_p())

    def prepend_len(self,  val, len,):
        if len : len = len._object
        else : len = c_void_p()

        libgobject.g_string_prepend_len.restype = _GString
        libgobject.g_string_prepend_len.argtypes = [c_void_p, c_char_p,gssize]
        from pywebkit3.gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_prepend_len(self._object,  val, len,) or c_void_p())

    def overwrite_len(self,  pos, val, len,):
        if len : len = len._object
        else : len = c_void_p()

        libgobject.g_string_overwrite_len.restype = _GString
        libgobject.g_string_overwrite_len.argtypes = [c_void_p, gsize,c_char_p,gssize]
        from pywebkit3.gobject import GString
        return GString(None,None,None,None, obj=libgobject.g_string_overwrite_len(self._object,  pos, val, len,) or c_void_p())

    def assign(self,  rval,):

        libgobject.g_string_assign.restype = _GString
        libgobject.g_string_assign.argtypes = [c_void_p, c_char_p]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_assign(self._object,  rval,) or c_void_p())

    def erase(self,  pos, len,):
        if pos : pos = pos._object
        else : pos = c_void_p()
        if len : len = len._object
        else : len = c_void_p()

        libgobject.g_string_erase.restype = _GString
        libgobject.g_string_erase.argtypes = [c_void_p, gssize,gssize]
        from pywebkit3.gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_erase(self._object,  pos, len,) or c_void_p())

    def down(self, ):

        libgobject.g_string_down.restype = _GString
        libgobject.g_string_down.argtypes = [c_void_p]
        from pywebkit3.gobject import GString
        return GString(None, obj=libgobject.g_string_down(self._object, ) or c_void_p())

    def append_len(self,  val, len,):
        if len : len = len._object
        else : len = c_void_p()

        libgobject.g_string_append_len.restype = _GString
        libgobject.g_string_append_len.argtypes = [c_void_p, c_char_p,gssize]
        from pywebkit3.gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_append_len(self._object,  val, len,) or c_void_p())

    def printf(self,  format,*args ):


        def callit( format, *args ):
                libgobject.g_string_printf.restype = None
                libgobject.g_string_printf.argtypes = [c_void_p, c_void_p, c_char_p]
                for arg in args:
                     libgobject.g_string_printf.argtypes.append(args[1])
                return libgobject.g_string_printf(self._object, format, *args)
    
        return callit( format,*args )

    def truncate(self,  len,):

        libgobject.g_string_truncate.restype = _GString
        libgobject.g_string_truncate.argtypes = [c_void_p, gsize]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_truncate(self._object,  len,) or c_void_p())

    def append(self,  val,):

        libgobject.g_string_append.restype = _GString
        libgobject.g_string_append.argtypes = [c_void_p, c_char_p]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_append(self._object,  val,) or c_void_p())

    def prepend(self,  val,):

        libgobject.g_string_prepend.restype = _GString
        libgobject.g_string_prepend.argtypes = [c_void_p, c_char_p]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_prepend(self._object,  val,) or c_void_p())

    def append_unichar(self,  wc,):
        if wc : wc = wc._object
        else : wc = c_void_p()

        libgobject.g_string_append_unichar.restype = _GString
        libgobject.g_string_append_unichar.argtypes = [c_void_p, gunichar]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_append_unichar(self._object,  wc,) or c_void_p())

    def prepend_unichar(self,  wc,):
        if wc : wc = wc._object
        else : wc = c_void_p()

        libgobject.g_string_prepend_unichar.restype = _GString
        libgobject.g_string_prepend_unichar.argtypes = [c_void_p, gunichar]
        from pywebkit3.gobject import GString
        return GString(None,None, obj=libgobject.g_string_prepend_unichar(self._object,  wc,) or c_void_p())

    def insert_len(self,  pos, val, len,):
        if pos : pos = pos._object
        else : pos = c_void_p()
        if len : len = len._object
        else : len = c_void_p()

        libgobject.g_string_insert_len.restype = _GString
        libgobject.g_string_insert_len.argtypes = [c_void_p, gssize,c_char_p,gssize]
        from pywebkit3.gobject import GString
        return GString(None,None,None,None, obj=libgobject.g_string_insert_len(self._object,  pos, val, len,) or c_void_p())

    def overwrite(self,  pos, val,):

        libgobject.g_string_overwrite.restype = _GString
        libgobject.g_string_overwrite.argtypes = [c_void_p, gsize,c_char_p]
        from pywebkit3.gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_overwrite(self._object,  pos, val,) or c_void_p())

    def insert_c(self,  pos, c,):
        if pos : pos = pos._object
        else : pos = c_void_p()

        libgobject.g_string_insert_c.restype = _GString
        libgobject.g_string_insert_c.argtypes = [c_void_p, gssize,gchar]
        from pywebkit3.gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_insert_c(self._object,  pos, c,) or c_void_p())

    def hash(self, ):

        libgobject.g_string_hash.restype = guint
        libgobject.g_string_hash.argtypes = [c_void_p]
        
        return libgobject.g_string_hash(self._object, )

    def insert_unichar(self,  pos, wc,):
        if pos : pos = pos._object
        else : pos = c_void_p()
        if wc : wc = wc._object
        else : wc = c_void_p()

        libgobject.g_string_insert_unichar.restype = _GString
        libgobject.g_string_insert_unichar.argtypes = [c_void_p, gssize,gunichar]
        from pywebkit3.gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_insert_unichar(self._object,  pos, wc,) or c_void_p())

    @staticmethod
    def new_len( init, len,):
        if len : len = len._object
        else : len = c_void_p()
        libgobject.g_string_new_len.restype = _GString
        libgobject.g_string_new_len.argtypes = [c_char_p,gssize]
        return libgobject.g_string_new_len(init, len, )

