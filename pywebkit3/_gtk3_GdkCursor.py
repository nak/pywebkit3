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
__GdkTimeCoord = c_void_p
_GdkPixbuf = c_void_p
_GParamSpec = c_void_p
_GList = c_void_p
__GtkWindow = c_void_p
__GtkRequisition = c_void_p
__GdkDisplay = c_void_p
_GtkRcStyle = c_void_p
_GtkWindowGroup = c_void_p
_GtkWidget = c_void_p
_GdkEvent = c_void_p
__GdkWindow = c_void_p
__cairo_font_options_t = c_void_p
_GdkDevice = c_void_p
__GdkWindowAttr = c_void_p
__GdkAtom = c_void_p
_GtkIconSet = c_void_p
__GValue = c_void_p
__cairo_region_t = c_void_p
__GdkColor = c_void_p
_GdkWindow = c_void_p
__PangoFontDescription = c_void_p
__GdkRectangle = c_void_p
__cairo_pattern_t = c_void_p
_PangoContext = c_void_p
__GdkWMDecoration = c_void_p
_GdkDeviceManager = c_void_p
_PangoLayout = c_void_p
__cairo_t = c_void_p
__GdkVisual = c_void_p
_GtkApplication = c_void_p
__GIcon = c_void_p
_GdkDisplay = c_void_p
__GtkIconSource = c_void_p
__GdkCursor = c_void_p
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
_GdkAppLaunchContext = c_void_p
_GdkCursor = c_void_p
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
GdkWindowType = c_int
GdkWindowWindowClass = c_int
GdkWindowHints = c_int
GdkGravity = c_int
GdkWindowEdgeh = c_int
GdkWindowTypeHint = c_int
GdkWindowAttributesType = c_int
GdkFilterReturn = c_int
GdkModifierType = c_int
GdkWMDecoration = c_int
GdkWMFunction = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GdkCursorType = c_int

import _gobject_GObject
class GdkCursor( _gobject_GObject.GObject):
    """Class GdkCursor Constructors"""
    def __init__( self, cursor_type,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gdk_cursor_new.restype = c_void_p

        libgtk3.gdk_cursor_new.argtypes = [GdkCursorType]
        self._object = libgtk3.gdk_cursor_new(cursor_type, )

    """Methods"""
    def get_cursor_type(self, ):

        libgtk3.gdk_cursor_get_cursor_type.restype = GdkCursorType
        libgtk3.gdk_cursor_get_cursor_type.argtypes = [c_void_p]
        
        return libgtk3.gdk_cursor_get_cursor_type(self._object, )

    def ref(self, ):

        libgtk3.gdk_cursor_ref.restype = _GdkCursor
        libgtk3.gdk_cursor_ref.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkCursor
        return GdkCursor(None, obj=libgtk3.gdk_cursor_ref(self._object, ) or c_void_p())

    def unref(self, ):

        libgtk3.gdk_cursor_unref.argtypes = [c_void_p]
        
        libgtk3.gdk_cursor_unref(self._object, )

    def get_display(self, ):

        libgtk3.gdk_cursor_get_display.restype = _GdkDisplay
        libgtk3.gdk_cursor_get_display.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gdk_cursor_get_display(self._object, ) or c_void_p())

    def get_image(self, ):

        libgtk3.gdk_cursor_get_image.restype = _GdkPixbuf
        libgtk3.gdk_cursor_get_image.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gdk_cursor_get_image(self._object, ) or c_void_p())

    @staticmethod
    def new_from_pixbuf( display, pixbuf, x, y,):
        if display : display = display._object
        else : display = c_void_p()
        if pixbuf : pixbuf = pixbuf._object
        else : pixbuf = c_void_p()
        libgtk3.gdk_cursor_new_from_pixbuf.restype = _GdkCursor
        libgtk3.gdk_cursor_new_from_pixbuf.argtypes = [_GdkDisplay,_GdkPixbuf,gint,gint]
        return libgtk3.gdk_cursor_new_from_pixbuf(display, pixbuf, x, y, )

    @staticmethod
    def new_from_name( display, name,):
        if display : display = display._object
        else : display = c_void_p()
        libgtk3.gdk_cursor_new_from_name.restype = _GdkCursor
        libgtk3.gdk_cursor_new_from_name.argtypes = [_GdkDisplay,c_char_p]
        return libgtk3.gdk_cursor_new_from_name(display, name, )

    @staticmethod
    def new_for_display( display, cursor_type,):
        if display : display = display._object
        else : display = c_void_p()
        libgtk3.gdk_cursor_new_for_display.restype = _GdkCursor
        libgtk3.gdk_cursor_new_for_display.argtypes = [_GdkDisplay,GdkCursorType]
        return libgtk3.gdk_cursor_new_for_display(display, cursor_type, )

