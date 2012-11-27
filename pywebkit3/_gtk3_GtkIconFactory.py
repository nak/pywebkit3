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
__GtkIconSet = c_void_p
_GtkIconFactory = c_void_p
_GtkIconSet = c_void_p
"""Enumerations"""

import _gobject_GObject
class GtkIconFactory( _gobject_GObject.GObject):
    """Class GtkIconFactory Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_icon_factory_new.restype = c_void_p

        libgtk3.gtk_icon_factory_new.argtypes = []
        self._object = libgtk3.gtk_icon_factory_new()

    """Methods"""
    def remove_default(self, ):

        libgtk3.gtk_icon_factory_remove_default.argtypes = [c_void_p]
        
        libgtk3.gtk_icon_factory_remove_default(self._object, )

    def add(self,  stock_id, icon_set,):
        if icon_set : icon_set = icon_set._object
        else : icon_set = c_void_p()

        libgtk3.gtk_icon_factory_add.argtypes = [c_void_p, c_char_p,_GtkIconSet]
        
        libgtk3.gtk_icon_factory_add(self._object,  stock_id, icon_set,)

    def add_default(self, ):

        libgtk3.gtk_icon_factory_add_default.argtypes = [c_void_p]
        
        libgtk3.gtk_icon_factory_add_default(self._object, )

    def lookup(self,  stock_id,):

        libgtk3.gtk_icon_factory_lookup.restype = _GtkIconSet
        libgtk3.gtk_icon_factory_lookup.argtypes = [c_void_p, c_char_p]
        from pywebkit3.gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_icon_factory_lookup(self._object,  stock_id,) or c_void_p())

    @staticmethod
    def lookup_default( stock_id,):
        libgtk3.gtk_icon_factory_lookup_default.restype = _GtkIconSet
        libgtk3.gtk_icon_factory_lookup_default.argtypes = [c_char_p]
        return libgtk3.gtk_icon_factory_lookup_default(stock_id, )

