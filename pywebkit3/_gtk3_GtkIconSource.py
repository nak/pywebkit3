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
_GtkIconSource = c_void_p
_gchar = c_void_p
_GdkPixbuf = c_void_p
__GdkPixbuf = c_void_p
"""Enumerations"""

import _gobject_GObject
class GtkIconSource( _gobject_GObject.GObject):
    """Class GtkIconSource Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_icon_source_new.restype = c_void_p

        libgtk3.gtk_icon_source_new.argtypes = []
        self._object = libgtk3.gtk_icon_source_new()

    """Methods"""
    def get_pixbuf(self, ):

        libgtk3.gtk_icon_source_get_pixbuf.restype = _GdkPixbuf
        libgtk3.gtk_icon_source_get_pixbuf.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_source_get_pixbuf(self._object, ) or c_void_p())

    def get_size_wildcarded(self, ):

        libgtk3.gtk_icon_source_get_size_wildcarded.restype = gboolean
        libgtk3.gtk_icon_source_get_size_wildcarded.argtypes = [c_void_p]
        
        return libgtk3.gtk_icon_source_get_size_wildcarded(self._object, )

    def set_direction(self,  direction,):

        libgtk3.gtk_icon_source_set_direction.argtypes = [c_void_p, GtkTextDirection]
        
        libgtk3.gtk_icon_source_set_direction(self._object,  direction,)

    def free(self, ):

        libgtk3.gtk_icon_source_free.argtypes = [c_void_p]
        
        libgtk3.gtk_icon_source_free(self._object, )

    def get_direction(self, ):

        libgtk3.gtk_icon_source_get_direction.restype = GtkTextDirection
        libgtk3.gtk_icon_source_get_direction.argtypes = [c_void_p]
        
        return libgtk3.gtk_icon_source_get_direction(self._object, )

    def set_state_wildcarded(self,  setting,):

        libgtk3.gtk_icon_source_set_state_wildcarded.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_icon_source_set_state_wildcarded(self._object,  setting,)

    def get_state_wildcarded(self, ):

        libgtk3.gtk_icon_source_get_state_wildcarded.restype = gboolean
        libgtk3.gtk_icon_source_get_state_wildcarded.argtypes = [c_void_p]
        
        return libgtk3.gtk_icon_source_get_state_wildcarded(self._object, )

    def set_direction_wildcarded(self,  setting,):

        libgtk3.gtk_icon_source_set_direction_wildcarded.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_icon_source_set_direction_wildcarded(self._object,  setting,)

    def copy(self, ):

        libgtk3.gtk_icon_source_copy.restype = _GtkIconSource
        libgtk3.gtk_icon_source_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkIconSource
        return GtkIconSource(None, obj=libgtk3.gtk_icon_source_copy(self._object, ) or c_void_p())

    def set_state(self,  state,):

        libgtk3.gtk_icon_source_set_state.argtypes = [c_void_p, GtkStateType]
        
        libgtk3.gtk_icon_source_set_state(self._object,  state,)

    def get_size(self, ):

        libgtk3.gtk_icon_source_get_size.restype = GtkIconSize
        libgtk3.gtk_icon_source_get_size.argtypes = [c_void_p]
        
        return libgtk3.gtk_icon_source_get_size(self._object, )

    def set_pixbuf(self,  pixbuf,):
        if pixbuf : pixbuf = pixbuf._object
        else : pixbuf = c_void_p()

        libgtk3.gtk_icon_source_set_pixbuf.argtypes = [c_void_p, _GdkPixbuf]
        
        libgtk3.gtk_icon_source_set_pixbuf(self._object,  pixbuf,)

    def get_icon_name(self, ):

        libgtk3.gtk_icon_source_get_icon_name.restype = _gchar
        libgtk3.gtk_icon_source_get_icon_name.argtypes = [c_void_p]
        
        return libgtk3.gtk_icon_source_get_icon_name(self._object, )

    def set_icon_name(self,  icon_name,):

        libgtk3.gtk_icon_source_set_icon_name.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_icon_source_set_icon_name(self._object,  icon_name,)

    def get_direction_wildcarded(self, ):

        libgtk3.gtk_icon_source_get_direction_wildcarded.restype = gboolean
        libgtk3.gtk_icon_source_get_direction_wildcarded.argtypes = [c_void_p]
        
        return libgtk3.gtk_icon_source_get_direction_wildcarded(self._object, )

    def set_size_wildcarded(self,  setting,):

        libgtk3.gtk_icon_source_set_size_wildcarded.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_icon_source_set_size_wildcarded(self._object,  setting,)

    def set_size(self,  size,):

        libgtk3.gtk_icon_source_set_size.argtypes = [c_void_p, GtkIconSize]
        
        libgtk3.gtk_icon_source_set_size(self._object,  size,)

    def get_state(self, ):

        libgtk3.gtk_icon_source_get_state.restype = GtkStateType
        libgtk3.gtk_icon_source_get_state.argtypes = [c_void_p]
        
        return libgtk3.gtk_icon_source_get_state(self._object, )

