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
_GdkEvent = c_void_p
__GdkWindow = c_void_p
__cairo_font_options_t = c_void_p
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

import _gobject_GObject
class GdkDisplay( _gobject_GObject.GObject):
    """Class GdkDisplay Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def flush(self, ):

        libgtk3.gdk_display_flush.argtypes = [c_void_p]
        
        libgtk3.gdk_display_flush(self._object, )

    def get_screen(self,  screen_num,):

        libgtk3.gdk_display_get_screen.restype = _GdkScreen
        libgtk3.gdk_display_get_screen.argtypes = [c_void_p, gint]
        from pywebkit3.gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gdk_display_get_screen(self._object,  screen_num,) or c_void_p())

    def get_default_cursor_size(self, ):

        libgtk3.gdk_display_get_default_cursor_size.restype = guint
        libgtk3.gdk_display_get_default_cursor_size.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_get_default_cursor_size(self._object, )

    def is_closed(self, ):

        libgtk3.gdk_display_is_closed.restype = gboolean
        libgtk3.gdk_display_is_closed.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_is_closed(self._object, )

    def store_clipboard(self,  clipboard_window, time_, targets, n_targets,):
        if clipboard_window : clipboard_window = clipboard_window._object
        else : clipboard_window = c_void_p()
        if targets : targets = targets._object
        else : targets = c_void_p()

        libgtk3.gdk_display_store_clipboard.argtypes = [c_void_p, _GdkWindow,guint32,_GdkAtom,gint]
        
        libgtk3.gdk_display_store_clipboard(self._object,  clipboard_window, time_, targets, n_targets,)

    def set_double_click_distance(self,  distance,):

        libgtk3.gdk_display_set_double_click_distance.argtypes = [c_void_p, guint]
        
        libgtk3.gdk_display_set_double_click_distance(self._object,  distance,)

    def peek_event(self, ):

        libgtk3.gdk_display_peek_event.restype = _GdkEvent
        libgtk3.gdk_display_peek_event.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_peek_event(self._object, )

    def get_n_screens(self, ):

        libgtk3.gdk_display_get_n_screens.restype = gint
        libgtk3.gdk_display_get_n_screens.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_get_n_screens(self._object, )

    def close(self, ):

        libgtk3.gdk_display_close.argtypes = [c_void_p]
        
        libgtk3.gdk_display_close(self._object, )

    def get_maximal_cursor_size(self,  width, height,):
        if width : width = width._object
        else : width = c_void_p()
        if height : height = height._object
        else : height = c_void_p()

        libgtk3.gdk_display_get_maximal_cursor_size.argtypes = [c_void_p, POITNER(guint),POITNER(guint)]
        
        libgtk3.gdk_display_get_maximal_cursor_size(self._object,  width, height,)

    def set_double_click_time(self,  msec,):

        libgtk3.gdk_display_set_double_click_time.argtypes = [c_void_p, guint]
        
        libgtk3.gdk_display_set_double_click_time(self._object,  msec,)

    def supports_input_shapes(self, ):

        libgtk3.gdk_display_supports_input_shapes.restype = gboolean
        libgtk3.gdk_display_supports_input_shapes.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_supports_input_shapes(self._object, )

    def put_event(self,  event,):
        if event : event = event._object
        else : event = c_void_p()

        libgtk3.gdk_display_put_event.argtypes = [c_void_p, POITNER(GdkEvent)]
        
        libgtk3.gdk_display_put_event(self._object,  event,)

    def supports_cursor_alpha(self, ):

        libgtk3.gdk_display_supports_cursor_alpha.restype = gboolean
        libgtk3.gdk_display_supports_cursor_alpha.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_supports_cursor_alpha(self._object, )

    def notify_startup_complete(self,  startup_id,):

        libgtk3.gdk_display_notify_startup_complete.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gdk_display_notify_startup_complete(self._object,  startup_id,)

    def supports_cursor_color(self, ):

        libgtk3.gdk_display_supports_cursor_color.restype = gboolean
        libgtk3.gdk_display_supports_cursor_color.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_supports_cursor_color(self._object, )

    def list_devices(self, ):

        libgtk3.gdk_display_list_devices.restype = _GList
        libgtk3.gdk_display_list_devices.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gdk_display_list_devices(self._object, ) or c_void_p())

    def has_pending(self, ):

        libgtk3.gdk_display_has_pending.restype = gboolean
        libgtk3.gdk_display_has_pending.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_has_pending(self._object, )

    def beep(self, ):

        libgtk3.gdk_display_beep.argtypes = [c_void_p]
        
        libgtk3.gdk_display_beep(self._object, )

    def get_default_group(self, ):

        libgtk3.gdk_display_get_default_group.restype = _GdkWindow
        libgtk3.gdk_display_get_default_group.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gdk_display_get_default_group(self._object, ) or c_void_p())

    def get_event(self, ):

        libgtk3.gdk_display_get_event.restype = _GdkEvent
        libgtk3.gdk_display_get_event.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_get_event(self._object, )

    def supports_shapes(self, ):

        libgtk3.gdk_display_supports_shapes.restype = gboolean
        libgtk3.gdk_display_supports_shapes.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_supports_shapes(self._object, )

    def get_window_at_pointer(self,  win_x, win_y,):
        if win_x : win_x = win_x._object
        else : win_x = c_void_p()
        if win_y : win_y = win_y._object
        else : win_y = c_void_p()

        libgtk3.gdk_display_get_window_at_pointer.restype = _GdkWindow
        libgtk3.gdk_display_get_window_at_pointer.argtypes = [c_void_p, POITNER(gint),POITNER(gint)]
        from pywebkit3.gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gdk_display_get_window_at_pointer(self._object,  win_x, win_y,) or c_void_p())

    def supports_composite(self, ):

        libgtk3.gdk_display_supports_composite.restype = gboolean
        libgtk3.gdk_display_supports_composite.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_supports_composite(self._object, )

    def pointer_is_grabbed(self, ):

        libgtk3.gdk_display_pointer_is_grabbed.restype = gboolean
        libgtk3.gdk_display_pointer_is_grabbed.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_pointer_is_grabbed(self._object, )

    def supports_selection_notification(self, ):

        libgtk3.gdk_display_supports_selection_notification.restype = gboolean
        libgtk3.gdk_display_supports_selection_notification.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_supports_selection_notification(self._object, )

    def get_app_launch_context(self, ):

        libgtk3.gdk_display_get_app_launch_context.restype = _GdkAppLaunchContext
        libgtk3.gdk_display_get_app_launch_context.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkAppLaunchContext
        return GdkAppLaunchContext(None, obj=libgtk3.gdk_display_get_app_launch_context(self._object, ) or c_void_p())

    def get_name(self, ):

        libgtk3.gdk_display_get_name.restype = _gchar
        libgtk3.gdk_display_get_name.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_get_name(self._object, )

    def get_device_manager(self, ):

        libgtk3.gdk_display_get_device_manager.restype = _GdkDeviceManager
        libgtk3.gdk_display_get_device_manager.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkDeviceManager
        return GdkDeviceManager( obj=libgtk3.gdk_display_get_device_manager(self._object, ) or c_void_p())

    def keyboard_ungrab(self,  time_,):

        libgtk3.gdk_display_keyboard_ungrab.argtypes = [c_void_p, guint32]
        
        libgtk3.gdk_display_keyboard_ungrab(self._object,  time_,)

    def get_default_screen(self, ):

        libgtk3.gdk_display_get_default_screen.restype = _GdkScreen
        libgtk3.gdk_display_get_default_screen.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gdk_display_get_default_screen(self._object, ) or c_void_p())

    def warp_pointer(self,  screen, x, y,):
        if screen : screen = screen._object
        else : screen = c_void_p()

        libgtk3.gdk_display_warp_pointer.argtypes = [c_void_p, _GdkScreen,gint,gint]
        
        libgtk3.gdk_display_warp_pointer(self._object,  screen, x, y,)

    def pointer_ungrab(self,  time_,):

        libgtk3.gdk_display_pointer_ungrab.argtypes = [c_void_p, guint32]
        
        libgtk3.gdk_display_pointer_ungrab(self._object,  time_,)

    def get_pointer(self,  screen, x, y, mask,):
        if screen : screen = screen._object
        else : screen = c_void_p()
        if x : x = x._object
        else : x = c_void_p()
        if y : y = y._object
        else : y = c_void_p()
        if mask : mask = mask._object
        else : mask = c_void_p()

        libgtk3.gdk_display_get_pointer.argtypes = [c_void_p, _GdkScreen,POITNER(gint),POITNER(gint),POITNER(GdkModifierType)]
        
        libgtk3.gdk_display_get_pointer(self._object,  screen, x, y, mask,)

    def device_is_grabbed(self,  device,):
        if device : device = device._object
        else : device = c_void_p()

        libgtk3.gdk_display_device_is_grabbed.restype = gboolean
        libgtk3.gdk_display_device_is_grabbed.argtypes = [c_void_p, _GdkDevice]
        
        return libgtk3.gdk_display_device_is_grabbed(self._object,  device,)

    def supports_clipboard_persistence(self, ):

        libgtk3.gdk_display_supports_clipboard_persistence.restype = gboolean
        libgtk3.gdk_display_supports_clipboard_persistence.argtypes = [c_void_p]
        
        return libgtk3.gdk_display_supports_clipboard_persistence(self._object, )

    def request_selection_notification(self,  selection,):
        if selection : selection = selection._object
        else : selection = c_void_p()

        libgtk3.gdk_display_request_selection_notification.restype = gboolean
        libgtk3.gdk_display_request_selection_notification.argtypes = [c_void_p, c_void_p]
        
        return libgtk3.gdk_display_request_selection_notification(self._object,  selection,)

    def sync(self, ):

        libgtk3.gdk_display_sync.argtypes = [c_void_p]
        
        libgtk3.gdk_display_sync(self._object, )

    @staticmethod
    def open( display_name,):
        libgtk3.gdk_display_open.restype = _GdkDisplay
        libgtk3.gdk_display_open.argtypes = [c_char_p]
        return libgtk3.gdk_display_open(display_name, )

    @staticmethod
    def get_default():
        libgtk3.gdk_display_get_default.restype = _GdkDisplay
        return libgtk3.gdk_display_get_default()

