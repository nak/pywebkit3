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

import _gobject_GObject
class GdkDevice( _gobject_GObject.GObject):
    """Class GdkDevice Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def set_mode(self,  mode,):

        libgtk3.gdk_device_set_mode.restype = gboolean
        libgtk3.gdk_device_set_mode.argtypes = [c_void_p, GdkInputMode]
        
        return libgtk3.gdk_device_set_mode(self._object,  mode,)

    def get_has_cursor(self, ):

        libgtk3.gdk_device_get_has_cursor.restype = gboolean
        libgtk3.gdk_device_get_has_cursor.argtypes = [c_void_p]
        
        return libgtk3.gdk_device_get_has_cursor(self._object, )

    def get_n_axes(self, ):

        libgtk3.gdk_device_get_n_axes.restype = gint
        libgtk3.gdk_device_get_n_axes.argtypes = [c_void_p]
        
        return libgtk3.gdk_device_get_n_axes(self._object, )

    def get_source(self, ):

        libgtk3.gdk_device_get_source.restype = GdkInputSource
        libgtk3.gdk_device_get_source.argtypes = [c_void_p]
        
        return libgtk3.gdk_device_get_source(self._object, )

    def get_history(self,  window, start, stop, events, n_events,):
        if window : window = window._object
        else : window = c_void_p()
        if events : events = events._object
        else : events = c_void_p()
        if n_events : n_events = n_events._object
        else : n_events = c_void_p()

        libgtk3.gdk_device_get_history.restype = gboolean
        libgtk3.gdk_device_get_history.argtypes = [c_void_p, _GdkWindow,guint32,guint32,POITNER(_GdkTimeCoord),POITNER(gint)]
        
        return libgtk3.gdk_device_get_history(self._object,  window, start, stop, events, n_events,)

    def get_mode(self, ):

        libgtk3.gdk_device_get_mode.restype = GdkInputMode
        libgtk3.gdk_device_get_mode.argtypes = [c_void_p]
        
        return libgtk3.gdk_device_get_mode(self._object, )

    def get_window_at_position(self,  win_x, win_y,):
        if win_x : win_x = win_x._object
        else : win_x = c_void_p()
        if win_y : win_y = win_y._object
        else : win_y = c_void_p()

        libgtk3.gdk_device_get_window_at_position.restype = _GdkWindow
        libgtk3.gdk_device_get_window_at_position.argtypes = [c_void_p, POITNER(gint),POITNER(gint)]
        from pywebkit3.gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gdk_device_get_window_at_position(self._object,  win_x, win_y,) or c_void_p())

    def get_device_type(self, ):

        libgtk3.gdk_device_get_device_type.restype = GdkDeviceType
        libgtk3.gdk_device_get_device_type.argtypes = [c_void_p]
        
        return libgtk3.gdk_device_get_device_type(self._object, )

    def get_axis_value(self,  axes, axis_label, value,):
        if axes : axes = axes._object
        else : axes = c_void_p()
        if axis_label : axis_label = axis_label._object
        else : axis_label = c_void_p()
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.gdk_device_get_axis_value.restype = gboolean
        libgtk3.gdk_device_get_axis_value.argtypes = [c_void_p, POITNER(gdouble),c_void_p,POITNER(gdouble)]
        
        return libgtk3.gdk_device_get_axis_value(self._object,  axes, axis_label, value,)

    def set_key(self,  index_, keyval, modifiers,):

        libgtk3.gdk_device_set_key.argtypes = [c_void_p, guint,guint,GdkModifierType]
        
        libgtk3.gdk_device_set_key(self._object,  index_, keyval, modifiers,)

    def ungrab(self,  time_,):

        libgtk3.gdk_device_ungrab.argtypes = [c_void_p, guint32]
        
        libgtk3.gdk_device_ungrab(self._object,  time_,)

    def list_axes(self, ):

        libgtk3.gdk_device_list_axes.restype = _GList
        libgtk3.gdk_device_list_axes.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gdk_device_list_axes(self._object, ) or c_void_p())

    def set_axis_use(self,  index_, use,):

        libgtk3.gdk_device_set_axis_use.argtypes = [c_void_p, guint,GdkAxisUse]
        
        libgtk3.gdk_device_set_axis_use(self._object,  index_, use,)

    def get_n_keys(self, ):

        libgtk3.gdk_device_get_n_keys.restype = gint
        libgtk3.gdk_device_get_n_keys.argtypes = [c_void_p]
        
        return libgtk3.gdk_device_get_n_keys(self._object, )

    def warp(self,  screen, x, y,):
        if screen : screen = screen._object
        else : screen = c_void_p()

        libgtk3.gdk_device_warp.argtypes = [c_void_p, _GdkScreen,gint,gint]
        
        libgtk3.gdk_device_warp(self._object,  screen, x, y,)

    def get_display(self, ):

        libgtk3.gdk_device_get_display.restype = _GdkDisplay
        libgtk3.gdk_device_get_display.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gdk_device_get_display(self._object, ) or c_void_p())

    def free_history(self,  events, n_events,):
        if events : events = events._object
        else : events = c_void_p()

        libgtk3.gdk_device_free_history.argtypes = [c_void_p, _GdkTimeCoord,gint]
        
        libgtk3.gdk_device_free_history(self._object,  events, n_events,)

    def get_associated_device(self, ):

        libgtk3.gdk_device_get_associated_device.restype = _GdkDevice
        libgtk3.gdk_device_get_associated_device.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkDevice
        return GdkDevice(None, obj=libgtk3.gdk_device_get_associated_device(self._object, ) or c_void_p())

    def get_name(self, ):

        libgtk3.gdk_device_get_name.restype = _gchar
        libgtk3.gdk_device_get_name.argtypes = [c_void_p]
        
        return libgtk3.gdk_device_get_name(self._object, )

    def get_key(self,  index_, keyval, modifiers,):
        if keyval : keyval = keyval._object
        else : keyval = c_void_p()
        if modifiers : modifiers = modifiers._object
        else : modifiers = c_void_p()

        libgtk3.gdk_device_get_key.restype = gboolean
        libgtk3.gdk_device_get_key.argtypes = [c_void_p, guint,POITNER(guint),POITNER(GdkModifierType)]
        
        return libgtk3.gdk_device_get_key(self._object,  index_, keyval, modifiers,)

    def get_position(self,  screen, x, y,):
        if screen : screen = screen._object
        else : screen = c_void_p()
        if x : x = x._object
        else : x = c_void_p()
        if y : y = y._object
        else : y = c_void_p()

        libgtk3.gdk_device_get_position.argtypes = [c_void_p, _GdkScreen,POITNER(gint),POITNER(gint)]
        
        libgtk3.gdk_device_get_position(self._object,  screen, x, y,)

    def get_axis_use(self,  index_,):

        libgtk3.gdk_device_get_axis_use.restype = GdkAxisUse
        libgtk3.gdk_device_get_axis_use.argtypes = [c_void_p, guint]
        
        return libgtk3.gdk_device_get_axis_use(self._object,  index_,)

    def get_axis(self,  axes, use, value,):
        if axes : axes = axes._object
        else : axes = c_void_p()
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.gdk_device_get_axis.restype = gboolean
        libgtk3.gdk_device_get_axis.argtypes = [c_void_p, POITNER(gdouble),GdkAxisUse,POITNER(gdouble)]
        
        return libgtk3.gdk_device_get_axis(self._object,  axes, use, value,)

    def grab(self,  window, grab_ownership, owner_events, event_mask, cursor, time_,):
        if window : window = window._object
        else : window = c_void_p()
        if cursor : cursor = cursor._object
        else : cursor = c_void_p()

        libgtk3.gdk_device_grab.restype = GdkGrabStatus
        libgtk3.gdk_device_grab.argtypes = [c_void_p, _GdkWindow,GdkGrabOwnership,gboolean,GdkEventMask,_GdkCursor,guint32]
        
        return libgtk3.gdk_device_grab(self._object,  window, grab_ownership, owner_events, event_mask, cursor, time_,)

    def list_slave_devices(self, ):

        libgtk3.gdk_device_list_slave_devices.restype = _GList
        libgtk3.gdk_device_list_slave_devices.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gdk_device_list_slave_devices(self._object, ) or c_void_p())

    def get_state(self,  window, axes, mask,):
        if window : window = window._object
        else : window = c_void_p()
        if axes : axes = axes._object
        else : axes = c_void_p()
        if mask : mask = mask._object
        else : mask = c_void_p()

        libgtk3.gdk_device_get_state.argtypes = [c_void_p, _GdkWindow,POITNER(gdouble),POITNER(GdkModifierType)]
        
        libgtk3.gdk_device_get_state(self._object,  window, axes, mask,)

