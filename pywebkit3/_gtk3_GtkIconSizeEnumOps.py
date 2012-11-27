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
__GtkSettings = c_void_p
_gchar = c_void_p
"""Enumerations"""

import _gobject_GObject
class GtkIconSizeEnumOps( _gobject_GObject.GObject):
    """Class GtkIconSizeEnumOps Constructors"""
    def __init__(self):
        self._object = None
    """Methods"""
    def gtk_icon_size_register_alias(self,  alias, target,):

        libgtk3.gtk_icon_size_register_alias.argtypes = [c_void_p, c_char_p,GtkIconSize]
        
        libgtk3.gtk_icon_size_register_alias(self._object,  alias, target,)

    @staticmethod
    def gtk_icon_size_lookup( size, width, height,):
        if width : width = width._object
        else : width = c_void_p()
        if height : height = height._object
        else : height = c_void_p()
        libgtk3.gtk_icon_size_lookup.restype = gboolean
        libgtk3.gtk_icon_size_lookup.argtypes = [GtkIconSize,POITNER(gint),POITNER(gint)]
        return libgtk3.gtk_icon_size_lookup(size, width, height, )

    @staticmethod
    def gtk_icon_size_register( name, width, height,):
        libgtk3.gtk_icon_size_register.restype = GtkIconSize
        libgtk3.gtk_icon_size_register.argtypes = [c_char_p,gint,gint]
        return libgtk3.gtk_icon_size_register(name, width, height, )

    @staticmethod
    def gtk_icon_size_get_name( size,):
        libgtk3.gtk_icon_size_get_name.restype = _gchar
        libgtk3.gtk_icon_size_get_name.argtypes = [GtkIconSize]
        return libgtk3.gtk_icon_size_get_name(size, )

    @staticmethod
    def gtk_icon_size_from_name( name,):
        libgtk3.gtk_icon_size_from_name.restype = GtkIconSize
        libgtk3.gtk_icon_size_from_name.argtypes = [c_char_p]
        return libgtk3.gtk_icon_size_from_name(name, )

    @staticmethod
    def gtk_icon_size_lookup_for_settings( settings, size, width, height,):
        if settings : settings = settings._object
        else : settings = c_void_p()
        if width : width = width._object
        else : width = c_void_p()
        if height : height = height._object
        else : height = c_void_p()
        libgtk3.gtk_icon_size_lookup_for_settings.restype = gboolean
        libgtk3.gtk_icon_size_lookup_for_settings.argtypes = [_GtkSettings,GtkIconSize,POITNER(gint),POITNER(gint)]
        return libgtk3.gtk_icon_size_lookup_for_settings(settings, size, width, height, )

