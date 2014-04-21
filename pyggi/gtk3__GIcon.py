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
_GError = POINTER(c_void_p)
"""Enumerations"""

try:
    libgtk3.g_icon_equal.restype = gboolean
    libgtk3.g_icon_equal.argtypes = [_GIcon,_GIcon]
except:
   pass
try:
    libgtk3.g_icon_to_string.restype = c_char_p
    libgtk3.g_icon_to_string.argtypes = [_GIcon]
except:
   pass
try:
    libgtk3.g_icon_new_for_string.restype = _GIcon
    libgtk3.g_icon_new_for_string.argtypes = [Asciifier,_GError]
except:
   pass
try:
    libgtk3.g_icon_hash.restype = guint
    libgtk3.g_icon_hash.argtypes = [gconstpointer]
except:
   pass
from . import gio__GInterface
class GIcon( gio__GInterface.GInterface):
    """Class GIcon Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def equal(  self, icon2, ):
        if icon2: icon2 = icon2._object
        else: icon2 = POINTER(c_void_p)()

        
        return libgtk3.g_icon_equal( self._object,icon2 )

    def to_string(  self, ):

        
        return libgtk3.g_icon_to_string( self._object )

    @staticmethod
    def new_for_string( str, error,):
        if error: error = error._object
        else: error = POINTER(c_void_p)()
        from .gobject import GIcon
        return GIcon( obj=    libgtk3.g_icon_new_for_string(str, error, )
 or POINTER(c_void_p)())
    @staticmethod
    def hash( icon,):
        
        return     libgtk3.g_icon_hash(icon, )

