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
from gtk3_enums import *
from gtk3_types import *
from gtk3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_GList = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GIcon = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GValue = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkDevice = POINTER(c_int)
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

libgtk3.gdk_cursor_get_cursor_type.restype = GdkCursorType
libgtk3.gdk_cursor_get_cursor_type.argtypes = [_GdkCursor]
libgtk3.gdk_cursor_ref.restype = _GdkCursor
libgtk3.gdk_cursor_ref.argtypes = [_GdkCursor]
libgtk3.gdk_cursor_unref.restype = None
libgtk3.gdk_cursor_unref.argtypes = [_GdkCursor]
libgtk3.gdk_cursor_get_display.restype = _GdkDisplay
libgtk3.gdk_cursor_get_display.argtypes = [_GdkCursor]
libgtk3.gdk_cursor_get_image.restype = _GdkPixbuf
libgtk3.gdk_cursor_get_image.argtypes = [_GdkCursor]
libgtk3.gdk_cursor_new_from_pixbuf.restype = _GdkCursor
libgtk3.gdk_cursor_new_from_pixbuf.argtypes = [_GdkDisplay,_GdkPixbuf,gint,gint]
libgtk3.gdk_cursor_new_from_name.restype = _GdkCursor
libgtk3.gdk_cursor_new_from_name.argtypes = [_GdkDisplay,c_char_p]
libgtk3.gdk_cursor_new_for_display.restype = _GdkCursor
libgtk3.gdk_cursor_new_for_display.argtypes = [_GdkDisplay,GdkCursorType]
import gobject__GObject
class GdkCursor( gobject__GObject.GObject):
    """Class GdkCursor Constructors"""
    def __init__( self, cursor_type,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gdk_cursor_new.restype = POINTER(c_int)
            
            libgtk3.gdk_cursor_new.argtypes = [GdkCursorType]
            self._object = libgtk3.gdk_cursor_new(cursor_type, )

    """Methods"""
    def get_cursor_type(  self, ):

        
        return libgtk3.gdk_cursor_get_cursor_type( self._object )

    def ref(  self, ):

        from gobject import GdkCursor
        return GdkCursor( obj=libgtk3.gdk_cursor_ref( self._object ) or POINTER(c_int)())

    def unref(  self, ):

        
        libgtk3.gdk_cursor_unref( self._object )

    def get_display(  self, ):

        from gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gdk_cursor_get_display( self._object ) or POINTER(c_int)())

    def get_image(  self, ):

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gdk_cursor_get_image( self._object ) or POINTER(c_int)())

    @staticmethod
    def new_from_pixbuf( display, pixbuf, x, y,):
        if display: display = display._object
        else: display = POINTER(c_int)()
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_int)()
        from gobject import GdkCursor
        return GdkCursor(None, obj=    libgtk3.gdk_cursor_new_from_pixbuf(display, pixbuf, x, y, )
 or POINTER(c_int)())
    @staticmethod
    def new_from_name( display, name,):
        if display: display = display._object
        else: display = POINTER(c_int)()
        from gobject import GdkCursor
        return GdkCursor(None, obj=    libgtk3.gdk_cursor_new_from_name(display, name, )
 or POINTER(c_int)())
    @staticmethod
    def new_for_display( display, cursor_type,):
        if display: display = display._object
        else: display = POINTER(c_int)()
        from gobject import GdkCursor
        return GdkCursor(None, obj=    libgtk3.gdk_cursor_new_for_display(display, cursor_type, )
 or POINTER(c_int)())
