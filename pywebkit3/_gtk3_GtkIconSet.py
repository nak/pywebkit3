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
__GtkRcStyle = c_void_p
__GdkGeometry = c_void_p
__GParamSpec = c_void_p
_GdkVisual = c_void_p
_GtkWindow = c_void_p
__GList = c_void_p
_GdkPixbuf = c_void_p
_GParamSpec = c_void_p
_GList = c_void_p
__GtkWindow = c_void_p
__GtkRequisition = c_void_p
_GtkRcStyle = c_void_p
_GtkWindowGroup = c_void_p
_GtkWidget = c_void_p
__GdkWindow = c_void_p
_GtkIconSet = c_void_p
__GValue = c_void_p
__cairo_region_t = c_void_p
__GdkColor = c_void_p
_GdkWindow = c_void_p
__PangoFontDescription = c_void_p
__GdkRectangle = c_void_p
_PangoContext = c_void_p
_PangoLayout = c_void_p
__cairo_t = c_void_p
__GdkVisual = c_void_p
_GtkApplication = c_void_p
_GdkDisplay = c_void_p
__GtkIconSource = c_void_p
__GtkAccelGroup = c_void_p
_GtkStyle = c_void_p
__GtkStyle = c_void_p
__GdkRGBA = c_void_p
__GError = c_void_p
__GdkPixbuf = c_void_p
_GtkStyleContext = c_void_p
__GtkAllocation = c_void_p
__GtkWidget = c_void_p
_GtkWidgetPath = c_void_p
_gchar = c_void_p
__GtkWidgetClass = c_void_p
_guchar = c_void_p
_GdkScreen = c_void_p
__GdkEventKey = c_void_p
__GtkApplication = c_void_p
_GtkClipboard = c_void_p
__PangoLayout = c_void_p
__GdkScreen = c_void_p
_GtkSettings = c_void_p
__GdkDevice = c_void_p
"""Enumerations"""
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkIconSize = c_int

import _gobject_GObject
class GtkIconSet( _gobject_GObject.GObject):
    """Class GtkIconSet Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_icon_set_new.restype = c_void_p

        libgtk3.gtk_icon_set_new.argtypes = []
        self._object = libgtk3.gtk_icon_set_new()

    """Methods"""
    def unref(self, ):

        libgtk3.gtk_icon_set_unref.argtypes = [c_void_p]
        
        libgtk3.gtk_icon_set_unref(self._object, )

    def add_source(self,  source,):
        if source : source = source._object
        else : source = c_void_p()

        libgtk3.gtk_icon_set_add_source.argtypes = [c_void_p, _GtkIconSource]
        
        libgtk3.gtk_icon_set_add_source(self._object,  source,)

    def copy(self, ):

        libgtk3.gtk_icon_set_copy.restype = _GtkIconSet
        libgtk3.gtk_icon_set_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_icon_set_copy(self._object, ) or c_void_p())

    def ref(self, ):

        libgtk3.gtk_icon_set_ref.restype = _GtkIconSet
        libgtk3.gtk_icon_set_ref.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_icon_set_ref(self._object, ) or c_void_p())

    def render_icon(self,  style, direction, state, size, widget, detail,):
        if style : style = style._object
        else : style = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_icon_set_render_icon.restype = _GdkPixbuf
        libgtk3.gtk_icon_set_render_icon.argtypes = [c_void_p, _GtkStyle,GtkTextDirection,GtkStateType,GtkIconSize,_GtkWidget,c_char_p]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_icon_set_render_icon(self._object,  style, direction, state, size, widget, detail,) or c_void_p())

    def get_sizes(self,  sizes, n_sizes,):
        if sizes : sizes = sizes._object
        else : sizes = c_void_p()
        if n_sizes : n_sizes = n_sizes._object
        else : n_sizes = c_void_p()

        libgtk3.gtk_icon_set_get_sizes.argtypes = [c_void_p, POITNER(GtkIconSize),POITNER(gint)]
        
        libgtk3.gtk_icon_set_get_sizes(self._object,  sizes, n_sizes,)

    @staticmethod
    def new_from_pixbuf( pixbuf,):
        if pixbuf : pixbuf = pixbuf._object
        else : pixbuf = c_void_p()
        libgtk3.gtk_icon_set_new_from_pixbuf.restype = _GtkIconSet
        libgtk3.gtk_icon_set_new_from_pixbuf.argtypes = [_GdkPixbuf]
        return libgtk3.gtk_icon_set_new_from_pixbuf(pixbuf, )

