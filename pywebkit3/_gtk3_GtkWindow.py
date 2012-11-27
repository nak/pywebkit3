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
_GdkScreen = c_void_p
__GError = c_void_p
"""Enumerations"""

import _gtk3_GtkBin
class GtkWindow( _gtk3_GtkBin.GtkBin):
    """Class GtkWindow Constructors"""
    def __init__( self, type,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_window_new.restype = c_void_p

        libgtk3.gtk_window_new.argtypes = [GtkWindowType]
        self._object = libgtk3.gtk_window_new(type, )

    """Methods"""
    def activate_focus(self, ):

        libgtk3.gtk_window_activate_focus.restype = gboolean
        libgtk3.gtk_window_activate_focus.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_activate_focus(self._object, )

    def set_skip_pager_hint(self,  setting,):

        libgtk3.gtk_window_set_skip_pager_hint.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_skip_pager_hint(self._object,  setting,)

    def set_geometry_hints(self,  geometry_widget, geometry, geom_mask,):
        if geometry_widget : geometry_widget = geometry_widget._object
        else : geometry_widget = c_void_p()
        if geometry : geometry = geometry._object
        else : geometry = c_void_p()
        if geom_mask : geom_mask = geom_mask._object
        else : geom_mask = c_void_p()

        libgtk3.gtk_window_set_geometry_hints.argtypes = [c_void_p, _GtkWidget,_GdkGeometry,GdkWindowHints]
        
        libgtk3.gtk_window_set_geometry_hints(self._object,  geometry_widget, geometry, geom_mask,)

    def get_group(self, ):

        libgtk3.gtk_window_get_group.restype = _GtkWindowGroup
        libgtk3.gtk_window_get_group.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWindowGroup
        return GtkWindowGroup(None, obj=libgtk3.gtk_window_get_group(self._object, ) or c_void_p())

    def set_has_resize_grip(self,  value,):

        libgtk3.gtk_window_set_has_resize_grip.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_has_resize_grip(self._object,  value,)

    def get_skip_pager_hint(self, ):

        libgtk3.gtk_window_get_skip_pager_hint.restype = gboolean
        libgtk3.gtk_window_get_skip_pager_hint.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_skip_pager_hint(self._object, )

    def maximize(self, ):

        libgtk3.gtk_window_maximize.argtypes = [c_void_p]
        
        libgtk3.gtk_window_maximize(self._object, )

    def set_icon_from_file(self,  filename, err,):
        if err : err = err._object
        else : err = c_void_p()

        libgtk3.gtk_window_set_icon_from_file.restype = gboolean
        libgtk3.gtk_window_set_icon_from_file.argtypes = [c_void_p, c_char_p,_GError]
        
        return libgtk3.gtk_window_set_icon_from_file(self._object,  filename, err,)

    def get_urgency_hint(self, ):

        libgtk3.gtk_window_get_urgency_hint.restype = gboolean
        libgtk3.gtk_window_get_urgency_hint.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_urgency_hint(self._object, )

    def propagate_key_event(self,  event,):
        if event : event = event._object
        else : event = c_void_p()

        libgtk3.gtk_window_propagate_key_event.restype = gboolean
        libgtk3.gtk_window_propagate_key_event.argtypes = [c_void_p, _GdkEventKey]
        
        return libgtk3.gtk_window_propagate_key_event(self._object,  event,)

    def get_opacity(self, ):

        libgtk3.gtk_window_get_opacity.restype = gdouble
        libgtk3.gtk_window_get_opacity.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_opacity(self._object, )

    def get_resize_grip_area(self,  rect,):
        if rect : rect = rect._object
        else : rect = c_void_p()

        libgtk3.gtk_window_get_resize_grip_area.restype = gboolean
        libgtk3.gtk_window_get_resize_grip_area.argtypes = [c_void_p, _GdkRectangle]
        
        return libgtk3.gtk_window_get_resize_grip_area(self._object,  rect,)

    def unmaximize(self, ):

        libgtk3.gtk_window_unmaximize.argtypes = [c_void_p]
        
        libgtk3.gtk_window_unmaximize(self._object, )

    def set_screen(self,  screen,):
        if screen : screen = screen._object
        else : screen = c_void_p()

        libgtk3.gtk_window_set_screen.argtypes = [c_void_p, _GdkScreen]
        
        libgtk3.gtk_window_set_screen(self._object,  screen,)

    def get_position(self,  root_x, root_y,):
        if root_x : root_x = root_x._object
        else : root_x = c_void_p()
        if root_y : root_y = root_y._object
        else : root_y = c_void_p()

        libgtk3.gtk_window_get_position.argtypes = [c_void_p, POITNER(gint),POITNER(gint)]
        
        libgtk3.gtk_window_get_position(self._object,  root_x, root_y,)

    def set_default_size(self,  width, height,):

        libgtk3.gtk_window_set_default_size.argtypes = [c_void_p, gint,gint]
        
        libgtk3.gtk_window_set_default_size(self._object,  width, height,)

    def is_active(self, ):

        libgtk3.gtk_window_is_active.restype = gboolean
        libgtk3.gtk_window_is_active.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_is_active(self._object, )

    def set_focus_on_map(self,  setting,):

        libgtk3.gtk_window_set_focus_on_map.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_focus_on_map(self._object,  setting,)

    def move(self,  x, y,):

        libgtk3.gtk_window_move.argtypes = [c_void_p, gint,gint]
        
        libgtk3.gtk_window_move(self._object,  x, y,)

    def set_position(self,  position,):
        if position : position = position._object
        else : position = c_void_p()

        libgtk3.gtk_window_set_position.argtypes = [c_void_p, GtkWindowPosition]
        
        libgtk3.gtk_window_set_position(self._object,  position,)

    def set_destroy_with_parent(self,  setting,):

        libgtk3.gtk_window_set_destroy_with_parent.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_destroy_with_parent(self._object,  setting,)

    def resize_to_geometry(self,  width, height,):

        libgtk3.gtk_window_resize_to_geometry.argtypes = [c_void_p, gint,gint]
        
        libgtk3.gtk_window_resize_to_geometry(self._object,  width, height,)

    def set_focus_visible(self,  setting,):

        libgtk3.gtk_window_set_focus_visible.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_focus_visible(self._object,  setting,)

    def set_mnemonics_visible(self,  setting,):

        libgtk3.gtk_window_set_mnemonics_visible.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_mnemonics_visible(self._object,  setting,)

    def has_toplevel_focus(self, ):

        libgtk3.gtk_window_has_toplevel_focus.restype = gboolean
        libgtk3.gtk_window_has_toplevel_focus.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_has_toplevel_focus(self._object, )

    def stick(self, ):

        libgtk3.gtk_window_stick.argtypes = [c_void_p]
        
        libgtk3.gtk_window_stick(self._object, )

    def get_title(self, ):

        libgtk3.gtk_window_get_title.restype = _gchar
        libgtk3.gtk_window_get_title.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_title(self._object, )

    def set_resizable(self,  resizable,):

        libgtk3.gtk_window_set_resizable.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_resizable(self._object,  resizable,)

    def get_size(self,  width, height,):
        if width : width = width._object
        else : width = c_void_p()
        if height : height = height._object
        else : height = c_void_p()

        libgtk3.gtk_window_get_size.argtypes = [c_void_p, POITNER(gint),POITNER(gint)]
        
        libgtk3.gtk_window_get_size(self._object,  width, height,)

    def set_default(self,  default_widget,):
        if default_widget : default_widget = default_widget._object
        else : default_widget = c_void_p()

        libgtk3.gtk_window_set_default.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_window_set_default(self._object,  default_widget,)

    def get_deletable(self, ):

        libgtk3.gtk_window_get_deletable.restype = gboolean
        libgtk3.gtk_window_get_deletable.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_deletable(self._object, )

    def begin_move_drag(self,  button, root_x, root_y, timestamp,):

        libgtk3.gtk_window_begin_move_drag.argtypes = [c_void_p, gint,gint,gint,guint32]
        
        libgtk3.gtk_window_begin_move_drag(self._object,  button, root_x, root_y, timestamp,)

    def get_gravity(self, ):

        libgtk3.gtk_window_get_gravity.restype = GdkGravity
        libgtk3.gtk_window_get_gravity.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_gravity(self._object, )

    def set_icon(self,  icon,):
        if icon : icon = icon._object
        else : icon = c_void_p()

        libgtk3.gtk_window_set_icon.argtypes = [c_void_p, _GdkPixbuf]
        
        libgtk3.gtk_window_set_icon(self._object,  icon,)

    def mnemonic_activate(self,  keyval, modifier,):

        libgtk3.gtk_window_mnemonic_activate.restype = gboolean
        libgtk3.gtk_window_mnemonic_activate.argtypes = [c_void_p, guint,GdkModifierType]
        
        return libgtk3.gtk_window_mnemonic_activate(self._object,  keyval, modifier,)

    def get_skip_taskbar_hint(self, ):

        libgtk3.gtk_window_get_skip_taskbar_hint.restype = gboolean
        libgtk3.gtk_window_get_skip_taskbar_hint.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_skip_taskbar_hint(self._object, )

    def get_focus_visible(self, ):

        libgtk3.gtk_window_get_focus_visible.restype = gboolean
        libgtk3.gtk_window_get_focus_visible.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_focus_visible(self._object, )

    def present(self, ):

        libgtk3.gtk_window_present.argtypes = [c_void_p]
        
        libgtk3.gtk_window_present(self._object, )

    def unfullscreen(self, ):

        libgtk3.gtk_window_unfullscreen.argtypes = [c_void_p]
        
        libgtk3.gtk_window_unfullscreen(self._object, )

    def set_keep_below(self,  setting,):

        libgtk3.gtk_window_set_keep_below.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_keep_below(self._object,  setting,)

    def resize_grip_is_visible(self, ):

        libgtk3.gtk_window_resize_grip_is_visible.restype = gboolean
        libgtk3.gtk_window_resize_grip_is_visible.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_resize_grip_is_visible(self._object, )

    def deiconify(self, ):

        libgtk3.gtk_window_deiconify.argtypes = [c_void_p]
        
        libgtk3.gtk_window_deiconify(self._object, )

    def resize(self,  width, height,):

        libgtk3.gtk_window_resize.argtypes = [c_void_p, gint,gint]
        
        libgtk3.gtk_window_resize(self._object,  width, height,)

    def get_role(self, ):

        libgtk3.gtk_window_get_role.restype = _gchar
        libgtk3.gtk_window_get_role.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_role(self._object, )

    def get_focus(self, ):

        libgtk3.gtk_window_get_focus.restype = _GtkWidget
        libgtk3.gtk_window_get_focus.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_window_get_focus(self._object, ) or c_void_p())

    def set_auto_startup_notification(self,  setting,):

        libgtk3.gtk_window_set_auto_startup_notification.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_auto_startup_notification(self._object,  setting,)

    def get_mnemonics_visible(self, ):

        libgtk3.gtk_window_get_mnemonics_visible.restype = gboolean
        libgtk3.gtk_window_get_mnemonics_visible.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_mnemonics_visible(self._object, )

    def get_mnemonic_modifier(self, ):

        libgtk3.gtk_window_get_mnemonic_modifier.restype = GdkModifierType
        libgtk3.gtk_window_get_mnemonic_modifier.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_mnemonic_modifier(self._object, )

    def set_application(self,  application,):
        if application : application = application._object
        else : application = c_void_p()

        libgtk3.gtk_window_set_application.argtypes = [c_void_p, _GtkApplication]
        
        libgtk3.gtk_window_set_application(self._object,  application,)

    def set_default_icon(self,  icon,):
        if icon : icon = icon._object
        else : icon = c_void_p()

        libgtk3.gtk_window_set_default_icon.argtypes = [c_void_p, _GdkPixbuf]
        
        libgtk3.gtk_window_set_default_icon(self._object,  icon,)

    def set_default_geometry(self,  width, height,):

        libgtk3.gtk_window_set_default_geometry.argtypes = [c_void_p, gint,gint]
        
        libgtk3.gtk_window_set_default_geometry(self._object,  width, height,)

    def get_icon(self, ):

        libgtk3.gtk_window_get_icon.restype = _GdkPixbuf
        libgtk3.gtk_window_get_icon.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_window_get_icon(self._object, ) or c_void_p())

    def set_role(self,  role,):

        libgtk3.gtk_window_set_role.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_window_set_role(self._object,  role,)

    def set_skip_taskbar_hint(self,  setting,):

        libgtk3.gtk_window_set_skip_taskbar_hint.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_skip_taskbar_hint(self._object,  setting,)

    def activate_default(self, ):

        libgtk3.gtk_window_activate_default.restype = gboolean
        libgtk3.gtk_window_activate_default.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_activate_default(self._object, )

    def has_group(self, ):

        libgtk3.gtk_window_has_group.restype = gboolean
        libgtk3.gtk_window_has_group.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_has_group(self._object, )

    def get_modal(self, ):

        libgtk3.gtk_window_get_modal.restype = gboolean
        libgtk3.gtk_window_get_modal.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_modal(self._object, )

    def set_title(self,  title,):

        libgtk3.gtk_window_set_title.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_window_set_title(self._object,  title,)

    def set_transient_for(self,  parent,):
        if parent : parent = parent._object
        else : parent = c_void_p()

        libgtk3.gtk_window_set_transient_for.argtypes = [c_void_p, _GtkWindow]
        
        libgtk3.gtk_window_set_transient_for(self._object,  parent,)

    def set_icon_list(self,  list,):
        if list : list = list._object
        else : list = c_void_p()

        libgtk3.gtk_window_set_icon_list.argtypes = [c_void_p, _GList]
        
        libgtk3.gtk_window_set_icon_list(self._object,  list,)

    def set_icon_name(self,  name,):

        libgtk3.gtk_window_set_icon_name.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_window_set_icon_name(self._object,  name,)

    def set_urgency_hint(self,  setting,):

        libgtk3.gtk_window_set_urgency_hint.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_urgency_hint(self._object,  setting,)

    def get_icon_name(self, ):

        libgtk3.gtk_window_get_icon_name.restype = _gchar
        libgtk3.gtk_window_get_icon_name.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_icon_name(self._object, )

    def set_opacity(self,  opacity,):

        libgtk3.gtk_window_set_opacity.argtypes = [c_void_p, gdouble]
        
        libgtk3.gtk_window_set_opacity(self._object,  opacity,)

    def iconify(self, ):

        libgtk3.gtk_window_iconify.argtypes = [c_void_p]
        
        libgtk3.gtk_window_iconify(self._object, )

    def get_transient_for(self, ):

        libgtk3.gtk_window_get_transient_for.restype = _GtkWindow
        libgtk3.gtk_window_get_transient_for.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWindow
        return GtkWindow(None, obj=libgtk3.gtk_window_get_transient_for(self._object, ) or c_void_p())

    def get_window_type(self, ):

        libgtk3.gtk_window_get_window_type.restype = GtkWindowType
        libgtk3.gtk_window_get_window_type.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_window_type(self._object, )

    def remove_mnemonic(self,  keyval, target,):
        if target : target = target._object
        else : target = c_void_p()

        libgtk3.gtk_window_remove_mnemonic.argtypes = [c_void_p, guint,_GtkWidget]
        
        libgtk3.gtk_window_remove_mnemonic(self._object,  keyval, target,)

    def get_resizable(self, ):

        libgtk3.gtk_window_get_resizable.restype = gboolean
        libgtk3.gtk_window_get_resizable.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_resizable(self._object, )

    def get_decorated(self, ):

        libgtk3.gtk_window_get_decorated.restype = gboolean
        libgtk3.gtk_window_get_decorated.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_decorated(self._object, )

    def parse_geometry(self,  geometry,):

        libgtk3.gtk_window_parse_geometry.restype = gboolean
        libgtk3.gtk_window_parse_geometry.argtypes = [c_void_p, c_char_p]
        
        return libgtk3.gtk_window_parse_geometry(self._object,  geometry,)

    def get_application(self, ):

        libgtk3.gtk_window_get_application.restype = _GtkApplication
        libgtk3.gtk_window_get_application.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkApplication
        return GtkApplication(None,None, obj=libgtk3.gtk_window_get_application(self._object, ) or c_void_p())

    def get_default_widget(self, ):

        libgtk3.gtk_window_get_default_widget.restype = _GtkWidget
        libgtk3.gtk_window_get_default_widget.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_window_get_default_widget(self._object, ) or c_void_p())

    def set_mnemonic_modifier(self,  modifier,):

        libgtk3.gtk_window_set_mnemonic_modifier.argtypes = [c_void_p, GdkModifierType]
        
        libgtk3.gtk_window_set_mnemonic_modifier(self._object,  modifier,)

    def set_startup_id(self,  startup_id,):

        libgtk3.gtk_window_set_startup_id.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_window_set_startup_id(self._object,  startup_id,)

    def set_default_icon_list(self,  list,):
        if list : list = list._object
        else : list = c_void_p()

        libgtk3.gtk_window_set_default_icon_list.argtypes = [c_void_p, _GList]
        
        libgtk3.gtk_window_set_default_icon_list(self._object,  list,)

    def set_modal(self,  modal,):

        libgtk3.gtk_window_set_modal.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_modal(self._object,  modal,)

    def get_screen(self, ):

        libgtk3.gtk_window_get_screen.restype = _GdkScreen
        libgtk3.gtk_window_get_screen.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gtk_window_get_screen(self._object, ) or c_void_p())

    def set_wmclass(self,  wmclass_name, wmclass_class,):

        libgtk3.gtk_window_set_wmclass.argtypes = [c_void_p, c_char_p,c_char_p]
        
        libgtk3.gtk_window_set_wmclass(self._object,  wmclass_name, wmclass_class,)

    def get_accept_focus(self, ):

        libgtk3.gtk_window_get_accept_focus.restype = gboolean
        libgtk3.gtk_window_get_accept_focus.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_accept_focus(self._object, )

    def get_focus_on_map(self, ):

        libgtk3.gtk_window_get_focus_on_map.restype = gboolean
        libgtk3.gtk_window_get_focus_on_map.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_focus_on_map(self._object, )

    def set_type_hint(self,  hint,):

        libgtk3.gtk_window_set_type_hint.argtypes = [c_void_p, GdkWindowTypeHint]
        
        libgtk3.gtk_window_set_type_hint(self._object,  hint,)

    def begin_resize_drag(self,  edge, button, root_x, root_y, timestamp,):
        if edge : edge = edge._object
        else : edge = c_void_p()

        libgtk3.gtk_window_begin_resize_drag.argtypes = [c_void_p, GdkWindowEdge,gint,gint,gint,guint32]
        
        libgtk3.gtk_window_begin_resize_drag(self._object,  edge, button, root_x, root_y, timestamp,)

    def unstick(self, ):

        libgtk3.gtk_window_unstick.argtypes = [c_void_p]
        
        libgtk3.gtk_window_unstick(self._object, )

    def get_destroy_with_parent(self, ):

        libgtk3.gtk_window_get_destroy_with_parent.restype = gboolean
        libgtk3.gtk_window_get_destroy_with_parent.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_destroy_with_parent(self._object, )

    def get_has_resize_grip(self, ):

        libgtk3.gtk_window_get_has_resize_grip.restype = gboolean
        libgtk3.gtk_window_get_has_resize_grip.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_has_resize_grip(self._object, )

    def set_gravity(self,  gravity,):

        libgtk3.gtk_window_set_gravity.argtypes = [c_void_p, GdkGravity]
        
        libgtk3.gtk_window_set_gravity(self._object,  gravity,)

    def add_accel_group(self,  accel_group,):
        if accel_group : accel_group = accel_group._object
        else : accel_group = c_void_p()

        libgtk3.gtk_window_add_accel_group.argtypes = [c_void_p, _GtkAccelGroup]
        
        libgtk3.gtk_window_add_accel_group(self._object,  accel_group,)

    def set_default_icon_name(self,  name,):

        libgtk3.gtk_window_set_default_icon_name.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_window_set_default_icon_name(self._object,  name,)

    def get_icon_list(self, ):

        libgtk3.gtk_window_get_icon_list.restype = _GList
        libgtk3.gtk_window_get_icon_list.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gtk_window_get_icon_list(self._object, ) or c_void_p())

    def set_keep_above(self,  setting,):

        libgtk3.gtk_window_set_keep_above.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_keep_above(self._object,  setting,)

    def set_has_user_ref_count(self,  setting,):

        libgtk3.gtk_window_set_has_user_ref_count.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_has_user_ref_count(self._object,  setting,)

    def get_type_hint(self, ):

        libgtk3.gtk_window_get_type_hint.restype = GdkWindowTypeHint
        libgtk3.gtk_window_get_type_hint.argtypes = [c_void_p]
        
        return libgtk3.gtk_window_get_type_hint(self._object, )

    def set_decorated(self,  setting,):

        libgtk3.gtk_window_set_decorated.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_decorated(self._object,  setting,)

    def fullscreen(self, ):

        libgtk3.gtk_window_fullscreen.argtypes = [c_void_p]
        
        libgtk3.gtk_window_fullscreen(self._object, )

    def activate_key(self,  event,):
        if event : event = event._object
        else : event = c_void_p()

        libgtk3.gtk_window_activate_key.restype = gboolean
        libgtk3.gtk_window_activate_key.argtypes = [c_void_p, _GdkEventKey]
        
        return libgtk3.gtk_window_activate_key(self._object,  event,)

    def set_deletable(self,  setting,):

        libgtk3.gtk_window_set_deletable.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_deletable(self._object,  setting,)

    def present_with_time(self,  timestamp,):

        libgtk3.gtk_window_present_with_time.argtypes = [c_void_p, guint32]
        
        libgtk3.gtk_window_present_with_time(self._object,  timestamp,)

    def get_default_size(self,  width, height,):
        if width : width = width._object
        else : width = c_void_p()
        if height : height = height._object
        else : height = c_void_p()

        libgtk3.gtk_window_get_default_size.argtypes = [c_void_p, POITNER(gint),POITNER(gint)]
        
        libgtk3.gtk_window_get_default_size(self._object,  width, height,)

    def set_focus(self,  focus,):
        if focus : focus = focus._object
        else : focus = c_void_p()

        libgtk3.gtk_window_set_focus.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_window_set_focus(self._object,  focus,)

    def add_mnemonic(self,  keyval, target,):
        if target : target = target._object
        else : target = c_void_p()

        libgtk3.gtk_window_add_mnemonic.argtypes = [c_void_p, guint,_GtkWidget]
        
        libgtk3.gtk_window_add_mnemonic(self._object,  keyval, target,)

    def remove_accel_group(self,  accel_group,):
        if accel_group : accel_group = accel_group._object
        else : accel_group = c_void_p()

        libgtk3.gtk_window_remove_accel_group.argtypes = [c_void_p, _GtkAccelGroup]
        
        libgtk3.gtk_window_remove_accel_group(self._object,  accel_group,)

    def set_accept_focus(self,  setting,):

        libgtk3.gtk_window_set_accept_focus.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_window_set_accept_focus(self._object,  setting,)

    def reshow_with_initial_size(self, ):

        libgtk3.gtk_window_reshow_with_initial_size.argtypes = [c_void_p]
        
        libgtk3.gtk_window_reshow_with_initial_size(self._object, )

    @staticmethod
    def set_default_icon_from_file( filename, err,):
        if err : err = err._object
        else : err = c_void_p()
        libgtk3.gtk_window_set_default_icon_from_file.restype = gboolean
        libgtk3.gtk_window_set_default_icon_from_file.argtypes = [c_char_p,_GError]
        return libgtk3.gtk_window_set_default_icon_from_file(filename, err, )

    @staticmethod
    def get_default_icon_name():
        libgtk3.gtk_window_get_default_icon_name.restype = _gchar
        return libgtk3.gtk_window_get_default_icon_name()

    @staticmethod
    def get_default_icon_list():
        libgtk3.gtk_window_get_default_icon_list.restype = _GList
        return libgtk3.gtk_window_get_default_icon_list()

    @staticmethod
    def list_toplevels():
        libgtk3.gtk_window_list_toplevels.restype = _GList
        return libgtk3.gtk_window_list_toplevels()

