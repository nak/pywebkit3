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
from .gtk3_types import *
from .gtk3_enums import *
from .gtk3_types import *
from .gtk3_enums import *

    
"""Derived Pointer Types"""
_GdkPixbuf = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GdkPixbufSimpleAnim = POINTER(c_void_p)
_GtkNumerableIcon = POINTER(c_void_p)
"""Enumerations"""

try:
    libgtk3.gtk_numerable_icon_set_background_icon_name.restype = None
    libgtk3.gtk_numerable_icon_set_background_icon_name.argtypes = [_GtkNumerableIcon,Asciifier]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_set_label.restype = None
    libgtk3.gtk_numerable_icon_set_label.argtypes = [_GtkNumerableIcon,Asciifier]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_set_style_context.restype = None
    libgtk3.gtk_numerable_icon_set_style_context.argtypes = [_GtkNumerableIcon,_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_get_label.restype = c_char_p
    libgtk3.gtk_numerable_icon_get_label.argtypes = [_GtkNumerableIcon]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_set_background_gicon.restype = None
    libgtk3.gtk_numerable_icon_set_background_gicon.argtypes = [_GtkNumerableIcon,_GIcon]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_get_count.restype = gint
    libgtk3.gtk_numerable_icon_get_count.argtypes = [_GtkNumerableIcon]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_set_count.restype = None
    libgtk3.gtk_numerable_icon_set_count.argtypes = [_GtkNumerableIcon,gint]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_get_background_icon_name.restype = c_char_p
    libgtk3.gtk_numerable_icon_get_background_icon_name.argtypes = [_GtkNumerableIcon]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_get_background_gicon.restype = _GIcon
    libgtk3.gtk_numerable_icon_get_background_gicon.argtypes = [_GtkNumerableIcon]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_get_style_context.restype = _GtkStyleContext
    libgtk3.gtk_numerable_icon_get_style_context.argtypes = [_GtkNumerableIcon]
except:
   pass
try:
    libgtk3.gtk_numerable_icon_new_with_style_context.restype = _GIcon
    libgtk3.gtk_numerable_icon_new_with_style_context.argtypes = [_GIcon,_GtkStyleContext]
except:
   pass
from . import gobject__GEmblemedIcon
class GtkNumerableIcon( gobject__GEmblemedIcon.GEmblemedIcon):
    """Class GtkNumerableIcon Constructors"""
    def __init__( self, base_icon,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_numerable_icon_new.restype = POINTER(c_void_p)
            
            if base_icon : base_icon = base_icon._object
            else :  base_icon = POINTER(c_void_p)()

            libgtk3.gtk_numerable_icon_new.argtypes = [_GIcon]
            self._object = libgtk3.gtk_numerable_icon_new(base_icon, )

    """Methods"""
    def set_background_icon_name(  self, icon_name, ):

        
        libgtk3.gtk_numerable_icon_set_background_icon_name( self._object,icon_name )

    def set_label(  self, label, ):

        
        libgtk3.gtk_numerable_icon_set_label( self._object,label )

    def set_style_context(  self, style, ):
        if style: style = style._object
        else: style = POINTER(c_void_p)()

        
        libgtk3.gtk_numerable_icon_set_style_context( self._object,style )

    def get_label(  self, ):

        
        return libgtk3.gtk_numerable_icon_get_label( self._object )

    def set_background_gicon(  self, icon, ):
        if icon: icon = icon._object
        else: icon = POINTER(c_void_p)()

        
        libgtk3.gtk_numerable_icon_set_background_gicon( self._object,icon )

    def get_count(  self, ):

        
        return libgtk3.gtk_numerable_icon_get_count( self._object )

    def set_count(  self, count, ):

        
        libgtk3.gtk_numerable_icon_set_count( self._object,count )

    def get_background_icon_name(  self, ):

        
        return libgtk3.gtk_numerable_icon_get_background_icon_name( self._object )

    def get_background_gicon(  self, ):

        from .gobject import GIcon
        return GIcon( obj=libgtk3.gtk_numerable_icon_get_background_gicon( self._object ) or POINTER(c_void_p)())

    def get_style_context(  self, ):

        from .gtk3 import GtkStyleContext
        return GtkStyleContext(None, obj=libgtk3.gtk_numerable_icon_get_style_context( self._object ) or POINTER(c_void_p)())

    @staticmethod
    def new_with_style_context( base_icon, context,):
        if base_icon: base_icon = base_icon._object
        else: base_icon = POINTER(c_void_p)()
        if context: context = context._object
        else: context = POINTER(c_void_p)()
        from .gobject import GIcon
        return GIcon( obj=    libgtk3.gtk_numerable_icon_new_with_style_context(base_icon, context, )
 or POINTER(c_void_p)())
