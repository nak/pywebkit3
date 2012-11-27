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
__GdkPixbuf = c_void_p
_GdkDevice = c_void_p
__GdkDragContext = c_void_p
__GtkTargetList = c_void_p
__GtkWidget = c_void_p
_GdkDragContext = c_void_p
__GIcon = c_void_p
__GtkTargetEntry = c_void_p
_GtkTargetList = c_void_p
_GtkWidget = c_void_p
_GdkEvent = c_void_p
__cairo_surface_t = c_void_p
_GOptionGroup = c_void_p
_PangoLanguage = c_void_p
__GdkDevice = c_void_p
__GdkWindow = c_void_p
"""Enumerations"""
GtkDestDefaults = c_int
GtkTargetFlags = c_int


def gtk_key_snooper_install( snooper, func_data,):
    if snooper : snooper = snooper._object
    else : snooper = c_void_p()
    libgtk3.gtk_key_snooper_install.restype = guint
    libgtk3.gtk_key_snooper_install.argtypes = [GtkKeySnoopFunc,gpointer]
    return libgtk3.gtk_key_snooper_install( snooper, func_data,)


def gtk_get_option_group( open_default_display,):
    libgtk3.gtk_get_option_group.restype = _GOptionGroup
    libgtk3.gtk_get_option_group.argtypes = [gboolean]
    return libgtk3.gtk_get_option_group( open_default_display,)


def gtk_drag_dest_find_target( widget, context, target_list,):
    if widget : widget = widget._object
    else : widget = c_void_p()
    if context : context = context._object
    else : context = c_void_p()
    if target_list : target_list = target_list._object
    else : target_list = c_void_p()
    libgtk3.gtk_drag_dest_find_target.restype = GdkAtom
    libgtk3.gtk_drag_dest_find_target.argtypes = [_GtkWidget,_GdkDragContext,_GtkTargetList]
    return libgtk3.gtk_drag_dest_find_target( widget, context, target_list,)


def gtk_main_iteration_do( blocking,):
    libgtk3.gtk_main_iteration_do.restype = gboolean
    libgtk3.gtk_main_iteration_do.argtypes = [gboolean]
    return libgtk3.gtk_main_iteration_do( blocking,)


def gtk_drag_dest_get_track_motion( widget,):
    if widget : widget = widget._object
    else : widget = c_void_p()
    libgtk3.gtk_drag_dest_get_track_motion.restype = gboolean
    libgtk3.gtk_drag_dest_get_track_motion.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_dest_get_track_motion( widget,)


def gtk_get_event_widget( event,):
    if event : event = event._object
    else : event = c_void_p()
    libgtk3.gtk_get_event_widget.restype = _GtkWidget
    libgtk3.gtk_get_event_widget.argtypes = [POITNER(GdkEvent)]
    return libgtk3.gtk_get_event_widget( event,)


def gtk_get_current_event_state( state,):
    if state : state = state._object
    else : state = c_void_p()
    libgtk3.gtk_get_current_event_state.restype = gboolean
    libgtk3.gtk_get_current_event_state.argtypes = [POITNER(GdkModifierType)]
    return libgtk3.gtk_get_current_event_state( state,)


def gtk_drag_get_source_widget( context,):
    if context : context = context._object
    else : context = c_void_p()
    libgtk3.gtk_drag_get_source_widget.restype = _GtkWidget
    libgtk3.gtk_drag_get_source_widget.argtypes = [_GdkDragContext]
    return libgtk3.gtk_drag_get_source_widget( context,)


def gtk_drag_source_get_target_list( widget,):
    if widget : widget = widget._object
    else : widget = c_void_p()
    libgtk3.gtk_drag_source_get_target_list.restype = _GtkTargetList
    libgtk3.gtk_drag_source_get_target_list.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_source_get_target_list( widget,)


def gtk_drag_dest_get_target_list( widget,):
    if widget : widget = widget._object
    else : widget = c_void_p()
    libgtk3.gtk_drag_dest_get_target_list.restype = _GtkTargetList
    libgtk3.gtk_drag_dest_get_target_list.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_dest_get_target_list( widget,)


def gtk_drag_check_threshold( widget, start_x, start_y, current_x, current_y,):
    if widget : widget = widget._object
    else : widget = c_void_p()
    libgtk3.gtk_drag_check_threshold.restype = gboolean
    libgtk3.gtk_drag_check_threshold.argtypes = [_GtkWidget,gint,gint,gint,gint]
    return libgtk3.gtk_drag_check_threshold( widget, start_x, start_y, current_x, current_y,)


def gtk_drag_begin( widget, targets, actions, button, event,):
    if widget : widget = widget._object
    else : widget = c_void_p()
    if targets : targets = targets._object
    else : targets = c_void_p()
    if actions : actions = actions._object
    else : actions = c_void_p()
    if event : event = event._object
    else : event = c_void_p()
    libgtk3.gtk_drag_begin.restype = _GdkDragContext
    libgtk3.gtk_drag_begin.argtypes = [_GtkWidget,_GtkTargetList,GdkDragAction,gint,POITNER(GdkEvent)]
    return libgtk3.gtk_drag_begin( widget, targets, actions, button, event,)

