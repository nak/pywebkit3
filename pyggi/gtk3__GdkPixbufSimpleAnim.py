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
_GdkPixbufSimpleAnim = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
"""Enumerations"""

try:
    libgtk3.gdk_pixbuf_simple_anim_add_frame.restype = None
    libgtk3.gdk_pixbuf_simple_anim_add_frame.argtypes = [_GdkPixbufSimpleAnim,_GdkPixbuf]
except:
   pass
try:
    libgtk3.gdk_pixbuf_simple_anim_get_loop.restype = gboolean
    libgtk3.gdk_pixbuf_simple_anim_get_loop.argtypes = [_GdkPixbufSimpleAnim]
except:
   pass
try:
    libgtk3.gdk_pixbuf_simple_anim_set_loop.restype = None
    libgtk3.gdk_pixbuf_simple_anim_set_loop.argtypes = [_GdkPixbufSimpleAnim,gboolean]
except:
   pass
from . import gtk3__GdkPixbufAnimation
class GdkPixbufSimpleAnim( gtk3__GdkPixbufAnimation.GdkPixbufAnimation):
    """Class GdkPixbufSimpleAnim Constructors"""
    def __init__( self, rate,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gdk_pixbuf_simple_anim_new.restype = POINTER(c_void_p)
            
            libgtk3.gdk_pixbuf_simple_anim_new.argtypes = [gfloat]
            self._object = libgtk3.gdk_pixbuf_simple_anim_new(rate, )

    """Methods"""
    def add_frame(  self, pixbuf, ):
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_void_p)()

        
        libgtk3.gdk_pixbuf_simple_anim_add_frame( self._object,pixbuf )

    def get_loop(  self, ):

        
        return libgtk3.gdk_pixbuf_simple_anim_get_loop( self._object )

    def set_loop(  self, loop, ):

        
        libgtk3.gdk_pixbuf_simple_anim_set_loop( self._object,loop )

