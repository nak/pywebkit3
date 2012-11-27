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
__GdkGeometry = c_void_p
__GdkPixbuf = c_void_p
_GtkWindow = c_void_p
__GtkWidget = c_void_p
__GList = c_void_p
_gchar = c_void_p
_GdkPixbuf = c_void_p
_GtkApplication = c_void_p
_GList = c_void_p
__GtkWindow = c_void_p
__GdkEventKey = c_void_p
__GtkApplication = c_void_p
_GtkWindowGroup = c_void_p
_GtkWidget = c_void_p
__GtkAccelGroup = c_void_p
__GdkRectangle = c_void_p
__GdkScreen = c_void_p
__GdkDevice = c_void_p
_GdkScreen = c_void_p
__GError = c_void_p
"""Enumerations"""

import _gobject_GObject
class GtkWindowGroup( _gobject_GObject.GObject):
    """Class GtkWindowGroup Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_window_group_new.restype = c_void_p

        libgtk3.gtk_window_group_new.argtypes = []
        self._object = libgtk3.gtk_window_group_new()

    """Methods"""
    def get_current_grab(self, ):

        libgtk3.gtk_window_group_get_current_grab.restype = _GtkWidget
        libgtk3.gtk_window_group_get_current_grab.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_window_group_get_current_grab(self._object, ) or c_void_p())

    def add_window(self,  window,):
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gtk_window_group_add_window.argtypes = [c_void_p, _GtkWindow]
        
        libgtk3.gtk_window_group_add_window(self._object,  window,)

    def list_windows(self, ):

        libgtk3.gtk_window_group_list_windows.restype = _GList
        libgtk3.gtk_window_group_list_windows.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gtk_window_group_list_windows(self._object, ) or c_void_p())

    def get_current_device_grab(self,  device,):
        if device : device = device._object
        else : device = c_void_p()

        libgtk3.gtk_window_group_get_current_device_grab.restype = _GtkWidget
        libgtk3.gtk_window_group_get_current_device_grab.argtypes = [c_void_p, _GdkDevice]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_window_group_get_current_device_grab(self._object,  device,) or c_void_p())

    def remove_window(self,  window,):
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gtk_window_group_remove_window.argtypes = [c_void_p, _GtkWindow]
        
        libgtk3.gtk_window_group_remove_window(self._object,  window,)

