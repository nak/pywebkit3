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
__cairo_font_options_t = c_void_p
__GdkWindowAttr = c_void_p
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
_PangoLayout = c_void_p
__cairo_t = c_void_p
__GdkVisual = c_void_p
_GtkApplication = c_void_p
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

import _gobject_GObject
class GdkScreen( _gobject_GObject.GObject):
    """Class GdkScreen Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_monitor_at_point(self,  x, y,):

        libgtk3.gdk_screen_get_monitor_at_point.restype = gint
        libgtk3.gdk_screen_get_monitor_at_point.argtypes = [c_void_p, gint,gint]
        
        return libgtk3.gdk_screen_get_monitor_at_point(self._object,  x, y,)

    def get_toplevel_windows(self, ):

        libgtk3.gdk_screen_get_toplevel_windows.restype = _GList
        libgtk3.gdk_screen_get_toplevel_windows.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gdk_screen_get_toplevel_windows(self._object, ) or c_void_p())

    def is_composited(self, ):

        libgtk3.gdk_screen_is_composited.restype = gboolean
        libgtk3.gdk_screen_is_composited.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_is_composited(self._object, )

    def get_number(self, ):

        libgtk3.gdk_screen_get_number.restype = gint
        libgtk3.gdk_screen_get_number.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_get_number(self._object, )

    def get_monitor_height_mm(self,  monitor_num,):

        libgtk3.gdk_screen_get_monitor_height_mm.restype = gint
        libgtk3.gdk_screen_get_monitor_height_mm.argtypes = [c_void_p, gint]
        
        return libgtk3.gdk_screen_get_monitor_height_mm(self._object,  monitor_num,)

    def get_monitor_workarea(self,  monitor_num, dest,):
        if dest : dest = dest._object
        else : dest = c_void_p()

        libgtk3.gdk_screen_get_monitor_workarea.argtypes = [c_void_p, gint,_GdkRectangle]
        
        libgtk3.gdk_screen_get_monitor_workarea(self._object,  monitor_num, dest,)

    def get_resolution(self, ):

        libgtk3.gdk_screen_get_resolution.restype = gdouble
        libgtk3.gdk_screen_get_resolution.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_get_resolution(self._object, )

    def get_n_monitors(self, ):

        libgtk3.gdk_screen_get_n_monitors.restype = gint
        libgtk3.gdk_screen_get_n_monitors.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_get_n_monitors(self._object, )

    def get_setting(self,  name, value,):
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.gdk_screen_get_setting.restype = gboolean
        libgtk3.gdk_screen_get_setting.argtypes = [c_void_p, c_char_p,_GValue]
        
        return libgtk3.gdk_screen_get_setting(self._object,  name, value,)

    def get_primary_monitor(self, ):

        libgtk3.gdk_screen_get_primary_monitor.restype = gint
        libgtk3.gdk_screen_get_primary_monitor.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_get_primary_monitor(self._object, )

    def set_font_options(self,  options,):
        if options : options = options._object
        else : options = c_void_p()

        libgtk3.gdk_screen_set_font_options.argtypes = [c_void_p, _cairo_font_options_t]
        
        libgtk3.gdk_screen_set_font_options(self._object,  options,)

    def get_display(self, ):

        libgtk3.gdk_screen_get_display.restype = _GdkDisplay
        libgtk3.gdk_screen_get_display.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gdk_screen_get_display(self._object, ) or c_void_p())

    def make_display_name(self, ):

        libgtk3.gdk_screen_make_display_name.restype = _gchar
        libgtk3.gdk_screen_make_display_name.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_make_display_name(self._object, )

    def get_monitor_at_window(self,  window,):
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gdk_screen_get_monitor_at_window.restype = gint
        libgtk3.gdk_screen_get_monitor_at_window.argtypes = [c_void_p, _GdkWindow]
        
        return libgtk3.gdk_screen_get_monitor_at_window(self._object,  window,)

    def get_width(self, ):

        libgtk3.gdk_screen_get_width.restype = gint
        libgtk3.gdk_screen_get_width.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_get_width(self._object, )

    def list_visuals(self, ):

        libgtk3.gdk_screen_list_visuals.restype = _GList
        libgtk3.gdk_screen_list_visuals.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gdk_screen_list_visuals(self._object, ) or c_void_p())

    def get_monitor_plug_name(self,  monitor_num,):

        libgtk3.gdk_screen_get_monitor_plug_name.restype = _gchar
        libgtk3.gdk_screen_get_monitor_plug_name.argtypes = [c_void_p, gint]
        
        return libgtk3.gdk_screen_get_monitor_plug_name(self._object,  monitor_num,)

    def get_monitor_geometry(self,  monitor_num, dest,):
        if dest : dest = dest._object
        else : dest = c_void_p()

        libgtk3.gdk_screen_get_monitor_geometry.argtypes = [c_void_p, gint,_GdkRectangle]
        
        libgtk3.gdk_screen_get_monitor_geometry(self._object,  monitor_num, dest,)

    def set_resolution(self,  dpi,):

        libgtk3.gdk_screen_set_resolution.argtypes = [c_void_p, gdouble]
        
        libgtk3.gdk_screen_set_resolution(self._object,  dpi,)

    def get_root_window(self, ):

        libgtk3.gdk_screen_get_root_window.restype = _GdkWindow
        libgtk3.gdk_screen_get_root_window.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gdk_screen_get_root_window(self._object, ) or c_void_p())

    def get_height(self, ):

        libgtk3.gdk_screen_get_height.restype = gint
        libgtk3.gdk_screen_get_height.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_get_height(self._object, )

    def get_monitor_width_mm(self,  monitor_num,):

        libgtk3.gdk_screen_get_monitor_width_mm.restype = gint
        libgtk3.gdk_screen_get_monitor_width_mm.argtypes = [c_void_p, gint]
        
        return libgtk3.gdk_screen_get_monitor_width_mm(self._object,  monitor_num,)

    def get_height_mm(self, ):

        libgtk3.gdk_screen_get_height_mm.restype = gint
        libgtk3.gdk_screen_get_height_mm.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_get_height_mm(self._object, )

    def get_active_window(self, ):

        libgtk3.gdk_screen_get_active_window.restype = _GdkWindow
        libgtk3.gdk_screen_get_active_window.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gdk_screen_get_active_window(self._object, ) or c_void_p())

    def get_width_mm(self, ):

        libgtk3.gdk_screen_get_width_mm.restype = gint
        libgtk3.gdk_screen_get_width_mm.argtypes = [c_void_p]
        
        return libgtk3.gdk_screen_get_width_mm(self._object, )

    def get_window_stack(self, ):

        libgtk3.gdk_screen_get_window_stack.restype = _GList
        libgtk3.gdk_screen_get_window_stack.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gdk_screen_get_window_stack(self._object, ) or c_void_p())

    @staticmethod
    def gdk_visual_get_screen( visual,):
        if visual : visual = visual._object
        else : visual = c_void_p()
        libgtk3.gdk_visual_get_screen.restype = _GdkScreen
        libgtk3.gdk_visual_get_screen.argtypes = [_GdkVisual]
        return libgtk3.gdk_visual_get_screen(visual, )

    @staticmethod
    def get_default():
        libgtk3.gdk_screen_get_default.restype = _GdkScreen
        return libgtk3.gdk_screen_get_default()

