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

libgtk3.gdk_app_launch_context_set_icon.restype = None
libgtk3.gdk_app_launch_context_set_icon.argtypes = [_GdkAppLaunchContext,_GIcon]
libgtk3.gdk_app_launch_context_set_timestamp.restype = None
libgtk3.gdk_app_launch_context_set_timestamp.argtypes = [_GdkAppLaunchContext,guint32]
libgtk3.gdk_app_launch_context_set_icon_name.restype = None
libgtk3.gdk_app_launch_context_set_icon_name.argtypes = [_GdkAppLaunchContext,c_char_p]
libgtk3.gdk_app_launch_context_set_display.restype = None
libgtk3.gdk_app_launch_context_set_display.argtypes = [_GdkAppLaunchContext,_GdkDisplay]
libgtk3.gdk_app_launch_context_set_screen.restype = None
libgtk3.gdk_app_launch_context_set_screen.argtypes = [_GdkAppLaunchContext,_GdkScreen]
libgtk3.gdk_app_launch_context_set_desktop.restype = None
libgtk3.gdk_app_launch_context_set_desktop.argtypes = [_GdkAppLaunchContext,gint]
import gobject__GObject
class GdkAppLaunchContext( gobject__GObject.GObject):
    """Class GdkAppLaunchContext Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gdk_app_launch_context_new.restype = POINTER(c_int)
            
            libgtk3.gdk_app_launch_context_new.argtypes = []
            self._object = libgtk3.gdk_app_launch_context_new()

    """Methods"""
    def set_icon(  self, icon, ):
        if icon: icon = icon._object
        else: icon = POINTER(c_int)()

        
        libgtk3.gdk_app_launch_context_set_icon( self._object,icon )

    def set_timestamp(  self, timestamp, ):

        
        libgtk3.gdk_app_launch_context_set_timestamp( self._object,timestamp )

    def set_icon_name(  self, icon_name, ):

        
        libgtk3.gdk_app_launch_context_set_icon_name( self._object,icon_name )

    def set_display(  self, display, ):
        if display: display = display._object
        else: display = POINTER(c_int)()

        
        libgtk3.gdk_app_launch_context_set_display( self._object,display )

    def set_screen(  self, screen, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()

        
        libgtk3.gdk_app_launch_context_set_screen( self._object,screen )

    def set_desktop(  self, desktop, ):

        
        libgtk3.gdk_app_launch_context_set_desktop( self._object,desktop )

