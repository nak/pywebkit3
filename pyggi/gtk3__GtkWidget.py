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
__GtkRcStyle = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GParamSpec = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
__GdkColor = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_PangoLayout = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GdkVisual = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GtkWindow = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
_GdkScreen = POINTER(c_int)
__GValue = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
__GdkDevice = POINTER(c_int)
"""Enumerations"""
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int

import gobject__GObject
class GtkWidget( gobject__GObject.GObject):
    """Class GtkWidget Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_widget_new.restype = POINTER(c_int)
            
            libgtk3.gtk_widget_new.argtypes = []
            self._object = libgtk3.gtk_widget_new()

    """Methods"""
    def set_device_enabled(  self, device, enabled, ):
        if device: device = device._object
        else: device = POINTER(c_int)()

        libgtk3.gtk_widget_set_device_enabled.argtypes = [_GtkWidget,_GdkDevice,gboolean]
        
        libgtk3.gtk_widget_set_device_enabled( self._object,device,enabled )

    def modify_text(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_widget_modify_text.argtypes = [_GtkWidget,GtkStateType,_GdkColor]
        
        libgtk3.gtk_widget_modify_text( self._object,state,color )

    def set_tooltip_text(  self, text, ):

        libgtk3.gtk_widget_set_tooltip_text.argtypes = [_GtkWidget,c_char_p]
        
        libgtk3.gtk_widget_set_tooltip_text( self._object,text )

    def get_style(  self, ):

        libgtk3.gtk_widget_get_style.restype = _GtkStyle
        libgtk3.gtk_widget_get_style.argtypes = [_GtkWidget]
        from gtk3 import GtkStyle
        return GtkStyle(None, obj=libgtk3.gtk_widget_get_style( self._object ) or POINTER(c_int)())

    def set_composite_name(  self, name, ):

        libgtk3.gtk_widget_set_composite_name.argtypes = [_GtkWidget,c_char_p]
        
        libgtk3.gtk_widget_set_composite_name( self._object,name )

    def get_parent_window(  self, ):

        libgtk3.gtk_widget_get_parent_window.restype = _GdkWindow
        libgtk3.gtk_widget_get_parent_window.argtypes = [_GtkWidget]
        from gobject import GdkWindow
        return GdkWindow(None,None, obj=libgtk3.gtk_widget_get_parent_window( self._object ) or POINTER(c_int)())

    def is_toplevel(  self, ):

        libgtk3.gtk_widget_is_toplevel.restype = gboolean
        libgtk3.gtk_widget_is_toplevel.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_is_toplevel( self._object )

    def set_app_paintable(  self, app_paintable, ):

        libgtk3.gtk_widget_set_app_paintable.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_app_paintable( self._object,app_paintable )

    def set_receives_default(  self, receives_default, ):

        libgtk3.gtk_widget_set_receives_default.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_receives_default( self._object,receives_default )

    def class_set_accessible_role(  self, widget_class, role, ):
        if widget_class: widget_class = widget_class._object
        else: widget_class = POINTER(c_int)()
        if role: role = role._object
        else: role = POINTER(c_int)()

        libgtk3.gtk_widget_class_set_accessible_role.argtypes = [_GtkWidget,_GtkWidgetClass,AtkRole]
        
        libgtk3.gtk_widget_class_set_accessible_role( self._object,widget_class,role )

    def get_state(  self, ):

        libgtk3.gtk_widget_get_state.restype = GtkStateType
        libgtk3.gtk_widget_get_state.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_state( self._object )

    def override_background_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_widget_override_background_color.argtypes = [_GtkWidget,GtkStateFlags,_GdkRGBA]
        
        libgtk3.gtk_widget_override_background_color( self._object,state,color )

    def set_tooltip_markup(  self, markup, ):

        libgtk3.gtk_widget_set_tooltip_markup.argtypes = [_GtkWidget,c_char_p]
        
        libgtk3.gtk_widget_set_tooltip_markup( self._object,markup )

    def has_default(  self, ):

        libgtk3.gtk_widget_has_default.restype = gboolean
        libgtk3.gtk_widget_has_default.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_has_default( self._object )

    def has_grab(  self, ):

        libgtk3.gtk_widget_has_grab.restype = gboolean
        libgtk3.gtk_widget_has_grab.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_has_grab( self._object )

    def get_has_tooltip(  self, ):

        libgtk3.gtk_widget_get_has_tooltip.restype = gboolean
        libgtk3.gtk_widget_get_has_tooltip.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_has_tooltip( self._object )

    def set_halign(  self, align, ):

        libgtk3.gtk_widget_set_halign.argtypes = [_GtkWidget,GtkAlign]
        
        libgtk3.gtk_widget_set_halign( self._object,align )

    def get_preferred_width_for_height(  self, height, minimum_width, natural_width, ):

        libgtk3.gtk_widget_get_preferred_width_for_height.argtypes = [_GtkWidget,gint,POINTER(gint),POINTER(gint)]
        
        libgtk3.gtk_widget_get_preferred_width_for_height( self._object,height,minimum_width,natural_width )

    def get_hexpand_set(  self, ):

        libgtk3.gtk_widget_get_hexpand_set.restype = gboolean
        libgtk3.gtk_widget_get_hexpand_set.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_hexpand_set( self._object )

    def override_font(  self, font_desc, ):
        if font_desc: font_desc = font_desc._object
        else: font_desc = POINTER(c_int)()

        libgtk3.gtk_widget_override_font.argtypes = [_GtkWidget,_PangoFontDescription]
        
        libgtk3.gtk_widget_override_font( self._object,font_desc )

    def get_preferred_height_for_width(  self, width, minimum_height, natural_height, ):

        libgtk3.gtk_widget_get_preferred_height_for_width.argtypes = [_GtkWidget,gint,POINTER(gint),POINTER(gint)]
        
        libgtk3.gtk_widget_get_preferred_height_for_width( self._object,width,minimum_height,natural_height )

    def set_window(  self, window, ):
        if window: window = window._object
        else: window = POINTER(c_int)()

        libgtk3.gtk_widget_set_window.argtypes = [_GtkWidget,_GdkWindow]
        
        libgtk3.gtk_widget_set_window( self._object,window )

    def get_allocated_width(  self, ):

        libgtk3.gtk_widget_get_allocated_width.restype = int
        libgtk3.gtk_widget_get_allocated_width.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_allocated_width( self._object )

    def get_hexpand(  self, ):

        libgtk3.gtk_widget_get_hexpand.restype = gboolean
        libgtk3.gtk_widget_get_hexpand.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_hexpand( self._object )

    def set_state(  self, state, ):

        libgtk3.gtk_widget_set_state.argtypes = [_GtkWidget,GtkStateType]
        
        libgtk3.gtk_widget_set_state( self._object,state )

    def add_events(  self, events, ):

        libgtk3.gtk_widget_add_events.argtypes = [_GtkWidget,gint]
        
        libgtk3.gtk_widget_add_events( self._object,events )

    def size_allocate(  self, allocation, ):
        if allocation: allocation = allocation._object
        else: allocation = POINTER(c_int)()

        libgtk3.gtk_widget_size_allocate.argtypes = [_GtkWidget,_GtkAllocation]
        
        libgtk3.gtk_widget_size_allocate( self._object,allocation )

    def draw(  self, cr, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()

        libgtk3.gtk_widget_draw.argtypes = [_GtkWidget,_cairo_t]
        
        libgtk3.gtk_widget_draw( self._object,cr )

    def class_install_style_property(  self, klass, pspec, ):
        if klass: klass = klass._object
        else: klass = POINTER(c_int)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        libgtk3.gtk_widget_class_install_style_property.argtypes = [_GtkWidget,_GtkWidgetClass,_GParamSpec]
        
        libgtk3.gtk_widget_class_install_style_property( self._object,klass,pspec )

    def get_vexpand(  self, ):

        libgtk3.gtk_widget_get_vexpand.restype = gboolean
        libgtk3.gtk_widget_get_vexpand.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_vexpand( self._object )

    def queue_resize_no_redraw(  self, ):

        libgtk3.gtk_widget_queue_resize_no_redraw.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_queue_resize_no_redraw( self._object )

    def set_can_focus(  self, can_focus, ):

        libgtk3.gtk_widget_set_can_focus.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_can_focus( self._object,can_focus )

    def unparent(  self, ):

        libgtk3.gtk_widget_unparent.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_unparent( self._object )

    def get_request_mode(  self, ):

        libgtk3.gtk_widget_get_request_mode.restype = GtkSizeRequestMode
        libgtk3.gtk_widget_get_request_mode.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_request_mode( self._object )

    def get_allocated_height(  self, ):

        libgtk3.gtk_widget_get_allocated_height.restype = int
        libgtk3.gtk_widget_get_allocated_height.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_allocated_height( self._object )

    def set_redraw_on_allocate(  self, redraw_on_allocate, ):

        libgtk3.gtk_widget_set_redraw_on_allocate.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_redraw_on_allocate( self._object,redraw_on_allocate )

    def set_realized(  self, realized, ):

        libgtk3.gtk_widget_set_realized.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_realized( self._object,realized )

    def get_preferred_size(  self, minimum_size, natural_size, ):
        if minimum_size: minimum_size = minimum_size._object
        else: minimum_size = POINTER(c_int)()
        if natural_size: natural_size = natural_size._object
        else: natural_size = POINTER(c_int)()

        libgtk3.gtk_widget_get_preferred_size.argtypes = [_GtkWidget,_GtkRequisition,_GtkRequisition]
        
        libgtk3.gtk_widget_get_preferred_size( self._object,minimum_size,natural_size )

    def modify_font(  self, font_desc, ):
        if font_desc: font_desc = font_desc._object
        else: font_desc = POINTER(c_int)()

        libgtk3.gtk_widget_modify_font.argtypes = [_GtkWidget,_PangoFontDescription]
        
        libgtk3.gtk_widget_modify_font( self._object,font_desc )

    def send_expose(  self, event, ):

        libgtk3.gtk_widget_send_expose.restype = gint
        libgtk3.gtk_widget_send_expose.argtypes = [_GtkWidget,POINTER(GdkEvent)]
        
        return libgtk3.gtk_widget_send_expose( self._object,event )

    def set_allocation(  self, allocation, ):
        if allocation: allocation = allocation._object
        else: allocation = POINTER(c_int)()

        libgtk3.gtk_widget_set_allocation.argtypes = [_GtkWidget,_GtkAllocation]
        
        libgtk3.gtk_widget_set_allocation( self._object,allocation )

    def set_sensitive(  self, sensitive, ):

        libgtk3.gtk_widget_set_sensitive.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_sensitive( self._object,sensitive )

    def get_app_paintable(  self, ):

        libgtk3.gtk_widget_get_app_paintable.restype = gboolean
        libgtk3.gtk_widget_get_app_paintable.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_app_paintable( self._object )

    def send_focus_change(  self, event, ):

        libgtk3.gtk_widget_send_focus_change.restype = gboolean
        libgtk3.gtk_widget_send_focus_change.argtypes = [_GtkWidget,POINTER(GdkEvent)]
        
        return libgtk3.gtk_widget_send_focus_change( self._object,event )

    def get_receives_default(  self, ):

        libgtk3.gtk_widget_get_receives_default.restype = gboolean
        libgtk3.gtk_widget_get_receives_default.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_receives_default( self._object )

    def show_now(  self, ):

        libgtk3.gtk_widget_show_now.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_show_now( self._object )

    def get_support_multidevice(  self, ):

        libgtk3.gtk_widget_get_support_multidevice.restype = gboolean
        libgtk3.gtk_widget_get_support_multidevice.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_support_multidevice( self._object )

    def get_events(  self, ):

        libgtk3.gtk_widget_get_events.restype = gint
        libgtk3.gtk_widget_get_events.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_events( self._object )

    def get_vexpand_set(  self, ):

        libgtk3.gtk_widget_get_vexpand_set.restype = gboolean
        libgtk3.gtk_widget_get_vexpand_set.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_vexpand_set( self._object )

    def set_vexpand(  self, expand, ):

        libgtk3.gtk_widget_set_vexpand.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_vexpand( self._object,expand )

    def modify_style(  self, style, ):
        if style: style = style._object
        else: style = POINTER(c_int)()

        libgtk3.gtk_widget_modify_style.argtypes = [_GtkWidget,_GtkRcStyle]
        
        libgtk3.gtk_widget_modify_style( self._object,style )

    def shape_combine_region(  self, region, ):
        if region: region = region._object
        else: region = POINTER(c_int)()

        libgtk3.gtk_widget_shape_combine_region.argtypes = [_GtkWidget,_cairo_region_t]
        
        libgtk3.gtk_widget_shape_combine_region( self._object,region )

    def get_visible(  self, ):

        libgtk3.gtk_widget_get_visible.restype = gboolean
        libgtk3.gtk_widget_get_visible.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_visible( self._object )

    def device_is_shadowed(  self, device, ):
        if device: device = device._object
        else: device = POINTER(c_int)()

        libgtk3.gtk_widget_device_is_shadowed.restype = gboolean
        libgtk3.gtk_widget_device_is_shadowed.argtypes = [_GtkWidget,_GdkDevice]
        
        return libgtk3.gtk_widget_device_is_shadowed( self._object,device )

    def get_preferred_height(  self, minimum_height, natural_height, ):

        libgtk3.gtk_widget_get_preferred_height.argtypes = [_GtkWidget,POINTER(gint),POINTER(gint)]
        
        libgtk3.gtk_widget_get_preferred_height( self._object,minimum_height,natural_height )

    def queue_draw(  self, ):

        libgtk3.gtk_widget_queue_draw.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_queue_draw( self._object )

    def style_attach(  self, ):

        libgtk3.gtk_widget_style_attach.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_style_attach( self._object )

    def get_valign(  self, ):

        libgtk3.gtk_widget_get_valign.restype = GtkAlign
        libgtk3.gtk_widget_get_valign.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_valign( self._object )

    def get_size_request(  self, width, height, ):

        libgtk3.gtk_widget_get_size_request.argtypes = [_GtkWidget,POINTER(gint),POINTER(gint)]
        
        libgtk3.gtk_widget_get_size_request( self._object,width,height )

    def can_activate_accel(  self, signal_id, ):

        libgtk3.gtk_widget_can_activate_accel.restype = gboolean
        libgtk3.gtk_widget_can_activate_accel.argtypes = [_GtkWidget,guint]
        
        return libgtk3.gtk_widget_can_activate_accel( self._object,signal_id )

    def size_request(  self, requisition, ):
        if requisition: requisition = requisition._object
        else: requisition = POINTER(c_int)()

        libgtk3.gtk_widget_size_request.argtypes = [_GtkWidget,_GtkRequisition]
        
        libgtk3.gtk_widget_size_request( self._object,requisition )

    def get_root_window(  self, ):

        libgtk3.gtk_widget_get_root_window.restype = _GdkWindow
        libgtk3.gtk_widget_get_root_window.argtypes = [_GtkWidget]
        from gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gtk_widget_get_root_window( self._object ) or POINTER(c_int)())

    def set_no_show_all(  self, no_show_all, ):

        libgtk3.gtk_widget_set_no_show_all.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_no_show_all( self._object,no_show_all )

    def set_visible(  self, visible, ):

        libgtk3.gtk_widget_set_visible.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_visible( self._object,visible )

    def style_get(  self, first_property_name,*args  ):


        def callit( first_property_name, *args ):
                libgtk3.gtk_widget_style_get.restype = None
                libgtk3.gtk_widget_style_get.argtypes = [ POINTER(c_int), c_char_p]
                for arg in args:
                     libgtk3.gtk_widget_style_get.argtypes.append(args[1])
                return libgtk3.gtk_widget_style_get( first_property_name, *args)
    
        return callit( self._object, first_property_name,*args )

    def set_can_default(  self, can_default, ):

        libgtk3.gtk_widget_set_can_default.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_can_default( self._object,can_default )

    def map(  self, ):

        libgtk3.gtk_widget_map.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_map( self._object )

    def unset_state_flags(  self, flags, ):

        libgtk3.gtk_widget_unset_state_flags.argtypes = [_GtkWidget,GtkStateFlags]
        
        libgtk3.gtk_widget_unset_state_flags( self._object,flags )

    def remove_accelerator(  self, accel_group, accel_key, accel_mods, ):
        if accel_group: accel_group = accel_group._object
        else: accel_group = POINTER(c_int)()

        libgtk3.gtk_widget_remove_accelerator.restype = gboolean
        libgtk3.gtk_widget_remove_accelerator.argtypes = [_GtkWidget,_GtkAccelGroup,guint,GdkModifierType]
        
        return libgtk3.gtk_widget_remove_accelerator( self._object,accel_group,accel_key,accel_mods )

    def modify_cursor(  self, primary, secondary, ):
        if primary: primary = primary._object
        else: primary = POINTER(c_int)()
        if secondary: secondary = secondary._object
        else: secondary = POINTER(c_int)()

        libgtk3.gtk_widget_modify_cursor.argtypes = [_GtkWidget,_GdkColor,_GdkColor]
        
        libgtk3.gtk_widget_modify_cursor( self._object,primary,secondary )

    def reset_style(  self, ):

        libgtk3.gtk_widget_reset_style.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_reset_style( self._object )

    def get_can_default(  self, ):

        libgtk3.gtk_widget_get_can_default.restype = gboolean
        libgtk3.gtk_widget_get_can_default.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_can_default( self._object )

    def queue_draw_region(  self, region, ):
        if region: region = region._object
        else: region = POINTER(c_int)()

        libgtk3.gtk_widget_queue_draw_region.argtypes = [_GtkWidget,_cairo_region_t]
        
        libgtk3.gtk_widget_queue_draw_region( self._object,region )

    def set_child_visible(  self, is_visible, ):

        libgtk3.gtk_widget_set_child_visible.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_child_visible( self._object,is_visible )

    def get_realized(  self, ):

        libgtk3.gtk_widget_get_realized.restype = gboolean
        libgtk3.gtk_widget_get_realized.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_realized( self._object )

    def set_parent_window(  self, parent_window, ):
        if parent_window: parent_window = parent_window._object
        else: parent_window = POINTER(c_int)()

        libgtk3.gtk_widget_set_parent_window.argtypes = [_GtkWidget,_GdkWindow]
        
        libgtk3.gtk_widget_set_parent_window( self._object,parent_window )

    def get_ancestor(  self, widget_type, ):

        libgtk3.gtk_widget_get_ancestor.restype = _GtkWidget
        libgtk3.gtk_widget_get_ancestor.argtypes = [_GtkWidget,GType]
        from gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_widget_get_ancestor( self._object,widget_type ) or POINTER(c_int)())

    def activate(  self, ):

        libgtk3.gtk_widget_activate.restype = gboolean
        libgtk3.gtk_widget_activate.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_activate( self._object )

    def child_notify(  self, child_property, ):

        libgtk3.gtk_widget_child_notify.argtypes = [_GtkWidget,c_char_p]
        
        libgtk3.gtk_widget_child_notify( self._object,child_property )

    def set_tooltip_window(  self, custom_window, ):
        if custom_window: custom_window = custom_window._object
        else: custom_window = POINTER(c_int)()

        libgtk3.gtk_widget_set_tooltip_window.argtypes = [_GtkWidget,_GtkWindow]
        
        libgtk3.gtk_widget_set_tooltip_window( self._object,custom_window )

    def set_margin_left(  self, margin, ):

        libgtk3.gtk_widget_set_margin_left.argtypes = [_GtkWidget,gint]
        
        libgtk3.gtk_widget_set_margin_left( self._object,margin )

    def translate_coordinates(  self, dest_widget, src_x, src_y, dest_x, dest_y, ):
        if dest_widget: dest_widget = dest_widget._object
        else: dest_widget = POINTER(c_int)()

        libgtk3.gtk_widget_translate_coordinates.restype = gboolean
        libgtk3.gtk_widget_translate_coordinates.argtypes = [_GtkWidget,_GtkWidget,gint,gint,POINTER(gint),POINTER(gint)]
        
        return libgtk3.gtk_widget_translate_coordinates( self._object,dest_widget,src_x,src_y,dest_x,dest_y )

    def create_pango_context(  self, ):

        libgtk3.gtk_widget_create_pango_context.restype = _PangoContext
        libgtk3.gtk_widget_create_pango_context.argtypes = [_GtkWidget]
        from gtk3 import PangoContext
        return PangoContext(None, obj=libgtk3.gtk_widget_create_pango_context( self._object )  or POINTER(c_int)())

    def is_sensitive(  self, ):

        libgtk3.gtk_widget_is_sensitive.restype = gboolean
        libgtk3.gtk_widget_is_sensitive.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_is_sensitive( self._object )

    def get_window(  self, ):

        libgtk3.gtk_widget_get_window.restype = _GdkWindow
        libgtk3.gtk_widget_get_window.argtypes = [_GtkWidget]
        from gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gtk_widget_get_window( self._object ) or POINTER(c_int)())

    def get_pointer(  self, x, y, ):

        libgtk3.gtk_widget_get_pointer.argtypes = [_GtkWidget,POINTER(gint),POINTER(gint)]
        
        libgtk3.gtk_widget_get_pointer( self._object,x,y )

    def set_size_request(  self, width, height, ):

        libgtk3.gtk_widget_set_size_request.argtypes = [_GtkWidget,gint,gint]
        
        libgtk3.gtk_widget_set_size_request( self._object,width,height )

    def is_composited(  self, ):

        libgtk3.gtk_widget_is_composited.restype = gboolean
        libgtk3.gtk_widget_is_composited.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_is_composited( self._object )

    def realize(  self, ):

        libgtk3.gtk_widget_realize.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_realize( self._object )

    def unrealize(  self, ):

        libgtk3.gtk_widget_unrealize.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_unrealize( self._object )

    def is_ancestor(  self, ancestor, ):
        if ancestor: ancestor = ancestor._object
        else: ancestor = POINTER(c_int)()

        libgtk3.gtk_widget_is_ancestor.restype = gboolean
        libgtk3.gtk_widget_is_ancestor.argtypes = [_GtkWidget,_GtkWidget]
        
        return libgtk3.gtk_widget_is_ancestor( self._object,ancestor )

    def get_device_enabled(  self, device, ):
        if device: device = device._object
        else: device = POINTER(c_int)()

        libgtk3.gtk_widget_get_device_enabled.restype = gboolean
        libgtk3.gtk_widget_get_device_enabled.argtypes = [_GtkWidget,_GdkDevice]
        
        return libgtk3.gtk_widget_get_device_enabled( self._object,device )

    def show(  self, ):

        libgtk3.gtk_widget_show.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_show( self._object )

    def gtk_cairo_transform_to_window(  self, cr, widget, window, ):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()
        if window: window = window._object
        else: window = POINTER(c_int)()

        libgtk3.gtk_cairo_transform_to_window.argtypes = [_GtkWidget,_cairo_t,_GtkWidget,_GdkWindow]
        
        libgtk3.gtk_cairo_transform_to_window( self._object,cr,widget,window )

    def get_style_context(  self, ):

        libgtk3.gtk_widget_get_style_context.restype = _GtkStyleContext
        libgtk3.gtk_widget_get_style_context.argtypes = [_GtkWidget]
        from gtk3 import GtkStyleContext
        return GtkStyleContext(None, obj=libgtk3.gtk_widget_get_style_context( self._object ) or POINTER(c_int)())

    def modify_bg(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_widget_modify_bg.argtypes = [_GtkWidget,GtkStateType,_GdkColor]
        
        libgtk3.gtk_widget_modify_bg( self._object,state,color )

    def has_visible_focus(  self, ):

        libgtk3.gtk_widget_has_visible_focus.restype = gboolean
        libgtk3.gtk_widget_has_visible_focus.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_has_visible_focus( self._object )

    def error_bell(  self, ):

        libgtk3.gtk_widget_error_bell.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_error_bell( self._object )

    def set_style(  self, style, ):
        if style: style = style._object
        else: style = POINTER(c_int)()

        libgtk3.gtk_widget_set_style.argtypes = [_GtkWidget,_GtkStyle]
        
        libgtk3.gtk_widget_set_style( self._object,style )

    def unmap(  self, ):

        libgtk3.gtk_widget_unmap.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_unmap( self._object )

    def get_visual(  self, ):

        libgtk3.gtk_widget_get_visual.restype = _GdkVisual
        libgtk3.gtk_widget_get_visual.argtypes = [_GtkWidget]
        from gobject import GdkVisual
        return GdkVisual( obj=libgtk3.gtk_widget_get_visual( self._object ) or POINTER(c_int)())

    def set_double_buffered(  self, double_buffered, ):

        libgtk3.gtk_widget_set_double_buffered.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_double_buffered( self._object,double_buffered )

    def get_preferred_width(  self, minimum_width, natural_width, ):

        libgtk3.gtk_widget_get_preferred_width.argtypes = [_GtkWidget,POINTER(gint),POINTER(gint)]
        
        libgtk3.gtk_widget_get_preferred_width( self._object,minimum_width,natural_width )

    def set_support_multidevice(  self, support_multidevice, ):

        libgtk3.gtk_widget_set_support_multidevice.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_support_multidevice( self._object,support_multidevice )

    def destroy(  self, ):

        libgtk3.gtk_widget_destroy.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_destroy( self._object )

    def set_direction(  self, dir, ):

        libgtk3.gtk_widget_set_direction.argtypes = [_GtkWidget,GtkTextDirection]
        
        libgtk3.gtk_widget_set_direction( self._object,dir )

    def get_name(  self, ):

        libgtk3.gtk_widget_get_name.restype = c_char_p
        libgtk3.gtk_widget_get_name.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_name( self._object )

    def intersect(  self, area, intersection, ):
        if area: area = area._object
        else: area = POINTER(c_int)()
        if intersection: intersection = intersection._object
        else: intersection = POINTER(c_int)()

        libgtk3.gtk_widget_intersect.restype = gboolean
        libgtk3.gtk_widget_intersect.argtypes = [_GtkWidget,_GdkRectangle,_GdkRectangle]
        
        return libgtk3.gtk_widget_intersect( self._object,area,intersection )

    def queue_draw_area(  self, x, y, width, height, ):

        libgtk3.gtk_widget_queue_draw_area.argtypes = [_GtkWidget,gint,gint,gint,gint]
        
        libgtk3.gtk_widget_queue_draw_area( self._object,x,y,width,height )

    def queue_compute_expand(  self, ):

        libgtk3.gtk_widget_queue_compute_expand.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_queue_compute_expand( self._object )

    def get_margin_top(  self, ):

        libgtk3.gtk_widget_get_margin_top.restype = gint
        libgtk3.gtk_widget_get_margin_top.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_margin_top( self._object )

    def destroyed(  self, widget_pointer, ):
        if widget_pointer: widget_pointer = widget_pointer._object
        else: widget_pointer = POINTER(c_int)()

        libgtk3.gtk_widget_destroyed.argtypes = [_GtkWidget,_GtkWidget]
        
        libgtk3.gtk_widget_destroyed( self._object,widget_pointer )

    def get_composite_name(  self, ):

        libgtk3.gtk_widget_get_composite_name.restype = c_char_p
        libgtk3.gtk_widget_get_composite_name.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_composite_name( self._object )

    def get_tooltip_window(  self, ):

        libgtk3.gtk_widget_get_tooltip_window.restype = _GtkWindow
        libgtk3.gtk_widget_get_tooltip_window.argtypes = [_GtkWidget]
        from gtk3 import GtkWindow
        return GtkWindow(None,None, obj=libgtk3.gtk_widget_get_tooltip_window( self._object ) or POINTER(c_int)())

    def reset_rc_styles(  self, ):

        libgtk3.gtk_widget_reset_rc_styles.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_reset_rc_styles( self._object )

    def get_child_requisition(  self, requisition, ):
        if requisition: requisition = requisition._object
        else: requisition = POINTER(c_int)()

        libgtk3.gtk_widget_get_child_requisition.argtypes = [_GtkWidget,_GtkRequisition]
        
        libgtk3.gtk_widget_get_child_requisition( self._object,requisition )

    def override_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_widget_override_color.argtypes = [_GtkWidget,GtkStateFlags,_GdkRGBA]
        
        libgtk3.gtk_widget_override_color( self._object,state,color )

    def add_device_events(  self, device, events, ):
        if device: device = device._object
        else: device = POINTER(c_int)()

        libgtk3.gtk_widget_add_device_events.argtypes = [_GtkWidget,_GdkDevice,GdkEventMask]
        
        libgtk3.gtk_widget_add_device_events( self._object,device,events )

    def get_double_buffered(  self, ):

        libgtk3.gtk_widget_get_double_buffered.restype = gboolean
        libgtk3.gtk_widget_get_double_buffered.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_double_buffered( self._object )

    def set_name(  self, name, ):

        libgtk3.gtk_widget_set_name.argtypes = [_GtkWidget,c_char_p]
        
        libgtk3.gtk_widget_set_name( self._object,name )

    def queue_resize(  self, ):

        libgtk3.gtk_widget_queue_resize.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_queue_resize( self._object )

    def get_halign(  self, ):

        libgtk3.gtk_widget_get_halign.restype = GtkAlign
        libgtk3.gtk_widget_get_halign.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_halign( self._object )

    def set_events(  self, events, ):

        libgtk3.gtk_widget_set_events.argtypes = [_GtkWidget,gint]
        
        libgtk3.gtk_widget_set_events( self._object,events )

    def get_parent(  self, ):

        libgtk3.gtk_widget_get_parent.restype = _GtkWidget
        libgtk3.gtk_widget_get_parent.argtypes = [_GtkWidget]
        from gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_widget_get_parent( self._object ) or POINTER(c_int)())

    def is_drawable(  self, ):

        libgtk3.gtk_widget_is_drawable.restype = gboolean
        libgtk3.gtk_widget_is_drawable.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_is_drawable( self._object )

    def has_focus(  self, ):

        libgtk3.gtk_widget_has_focus.restype = gboolean
        libgtk3.gtk_widget_has_focus.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_has_focus( self._object )

    def hide(  self, ):

        libgtk3.gtk_widget_hide.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_hide( self._object )

    def get_can_focus(  self, ):

        libgtk3.gtk_widget_get_can_focus.restype = gboolean
        libgtk3.gtk_widget_get_can_focus.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_can_focus( self._object )

    def mnemonic_activate(  self, group_cycling, ):

        libgtk3.gtk_widget_mnemonic_activate.restype = gboolean
        libgtk3.gtk_widget_mnemonic_activate.argtypes = [_GtkWidget,gboolean]
        
        return libgtk3.gtk_widget_mnemonic_activate( self._object,group_cycling )

    def is_focus(  self, ):

        libgtk3.gtk_widget_is_focus.restype = gboolean
        libgtk3.gtk_widget_is_focus.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_is_focus( self._object )

    def set_has_tooltip(  self, has_tooltip, ):

        libgtk3.gtk_widget_set_has_tooltip.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_has_tooltip( self._object,has_tooltip )

    def render_icon_pixbuf(  self, stock_id, size, ):

        libgtk3.gtk_widget_render_icon_pixbuf.restype = _GdkPixbuf
        libgtk3.gtk_widget_render_icon_pixbuf.argtypes = [_GtkWidget,c_char_p,GtkIconSize]
        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_widget_render_icon_pixbuf( self._object,stock_id,size ) or POINTER(c_int)())

    def ensure_style(  self, ):

        libgtk3.gtk_widget_ensure_style.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_ensure_style( self._object )

    def show_all(  self, ):

        libgtk3.gtk_widget_show_all.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_show_all( self._object )

    def get_mapped(  self, ):

        libgtk3.gtk_widget_get_mapped.restype = gboolean
        libgtk3.gtk_widget_get_mapped.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_mapped( self._object )

    def path(  self, path_length, path, path_reversed, ):

        libgtk3.gtk_widget_path.argtypes = [_GtkWidget,POINTER(guint),c_char_p,c_char_p]
        
        libgtk3.gtk_widget_path( self._object,path_length,path,path_reversed )

    def get_modifier_style(  self, ):

        libgtk3.gtk_widget_get_modifier_style.restype = _GtkRcStyle
        libgtk3.gtk_widget_get_modifier_style.argtypes = [_GtkWidget]
        from gtk3 import GtkRcStyle
        return GtkRcStyle(None, obj=libgtk3.gtk_widget_get_modifier_style( self._object ) or POINTER(c_int)())

    def set_default_direction(  self, dir, ):

        libgtk3.gtk_widget_set_default_direction.argtypes = [_GtkWidget,GtkTextDirection]
        
        libgtk3.gtk_widget_set_default_direction( self._object,dir )

    def set_has_window(  self, has_window, ):

        libgtk3.gtk_widget_set_has_window.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_has_window( self._object,has_window )

    def set_accel_path(  self, accel_path, accel_group, ):
        if accel_group: accel_group = accel_group._object
        else: accel_group = POINTER(c_int)()

        libgtk3.gtk_widget_set_accel_path.argtypes = [_GtkWidget,c_char_p,_GtkAccelGroup]
        
        libgtk3.gtk_widget_set_accel_path( self._object,accel_path,accel_group )

    def child_focus(  self, direction, ):

        libgtk3.gtk_widget_child_focus.restype = gboolean
        libgtk3.gtk_widget_child_focus.argtypes = [_GtkWidget,GtkDirectionType]
        
        return libgtk3.gtk_widget_child_focus( self._object,direction )

    def set_mapped(  self, mapped, ):

        libgtk3.gtk_widget_set_mapped.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_mapped( self._object,mapped )

    def class_set_accessible_type(  self, widget_class, type, ):
        if widget_class: widget_class = widget_class._object
        else: widget_class = POINTER(c_int)()

        libgtk3.gtk_widget_class_set_accessible_type.argtypes = [_GtkWidget,_GtkWidgetClass,GType]
        
        libgtk3.gtk_widget_class_set_accessible_type( self._object,widget_class,type )

    def grab_focus(  self, ):

        libgtk3.gtk_widget_grab_focus.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_grab_focus( self._object )

    def get_screen(  self, ):

        libgtk3.gtk_widget_get_screen.restype = _GdkScreen
        libgtk3.gtk_widget_get_screen.argtypes = [_GtkWidget]
        from gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gtk_widget_get_screen( self._object ) or POINTER(c_int)())

    def compute_expand(  self, orientation, ):

        libgtk3.gtk_widget_compute_expand.restype = gboolean
        libgtk3.gtk_widget_compute_expand.argtypes = [_GtkWidget,GtkOrientation]
        
        return libgtk3.gtk_widget_compute_expand( self._object,orientation )

    def get_margin_bottom(  self, ):

        libgtk3.gtk_widget_get_margin_bottom.restype = gint
        libgtk3.gtk_widget_get_margin_bottom.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_margin_bottom( self._object )

    def add_mnemonic_label(  self, label, ):
        if label: label = label._object
        else: label = POINTER(c_int)()

        libgtk3.gtk_widget_add_mnemonic_label.argtypes = [_GtkWidget,_GtkWidget]
        
        libgtk3.gtk_widget_add_mnemonic_label( self._object,label )

    def get_display(  self, ):

        libgtk3.gtk_widget_get_display.restype = _GdkDisplay
        libgtk3.gtk_widget_get_display.argtypes = [_GtkWidget]
        from gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gtk_widget_get_display( self._object ) or POINTER(c_int)())

    def event(  self, event, ):

        libgtk3.gtk_widget_event.restype = gboolean
        libgtk3.gtk_widget_event.argtypes = [_GtkWidget,POINTER(GdkEvent)]
        
        return libgtk3.gtk_widget_event( self._object,event )

    def thaw_child_notify(  self, ):

        libgtk3.gtk_widget_thaw_child_notify.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_thaw_child_notify( self._object )

    def class_install_style_property_parser(  self, klass, pspec, parser, ):
        if klass: klass = klass._object
        else: klass = POINTER(c_int)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()
        if parser: parser = parser._object
        else: parser = POINTER(c_int)()

        libgtk3.gtk_widget_class_install_style_property_parser.argtypes = [_GtkWidget,_GtkWidgetClass,_GParamSpec,GtkRcPropertyParser]
        
        libgtk3.gtk_widget_class_install_style_property_parser( self._object,klass,pspec,parser )

    def get_toplevel(  self, ):

        libgtk3.gtk_widget_get_toplevel.restype = _GtkWidget
        libgtk3.gtk_widget_get_toplevel.argtypes = [_GtkWidget]
        from gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_widget_get_toplevel( self._object ) or POINTER(c_int)())

    def get_clipboard(  self, selection, ):
        if selection: selection = selection._object
        else: selection = POINTER(c_int)()

        libgtk3.gtk_widget_get_clipboard.restype = _GtkClipboard
        libgtk3.gtk_widget_get_clipboard.argtypes = [_GtkWidget,POINTER(c_int)]
        from gtk3 import GtkClipboard
        return GtkClipboard( obj=libgtk3.gtk_widget_get_clipboard( self._object,selection ) or POINTER(c_int)())

    def list_accel_closures(  self, ):

        libgtk3.gtk_widget_list_accel_closures.restype = _GList
        libgtk3.gtk_widget_list_accel_closures.argtypes = [_GtkWidget]
        from gobject import GList
        return GList( obj=libgtk3.gtk_widget_list_accel_closures( self._object ) or POINTER(c_int)())

    def get_has_window(  self, ):

        libgtk3.gtk_widget_get_has_window.restype = gboolean
        libgtk3.gtk_widget_get_has_window.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_has_window( self._object )

    def override_cursor(  self, cursor, secondary_cursor, ):
        if cursor: cursor = cursor._object
        else: cursor = POINTER(c_int)()
        if secondary_cursor: secondary_cursor = secondary_cursor._object
        else: secondary_cursor = POINTER(c_int)()

        libgtk3.gtk_widget_override_cursor.argtypes = [_GtkWidget,_GdkRGBA,_GdkRGBA]
        
        libgtk3.gtk_widget_override_cursor( self._object,cursor,secondary_cursor )

    def set_margin_top(  self, margin, ):

        libgtk3.gtk_widget_set_margin_top.argtypes = [_GtkWidget,gint]
        
        libgtk3.gtk_widget_set_margin_top( self._object,margin )

    def in_destruction(  self, ):

        libgtk3.gtk_widget_in_destruction.restype = gboolean
        libgtk3.gtk_widget_in_destruction.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_in_destruction( self._object )

    def render_icon(  self, stock_id, size, detail, ):

        libgtk3.gtk_widget_render_icon.restype = _GdkPixbuf
        libgtk3.gtk_widget_render_icon.argtypes = [_GtkWidget,c_char_p,GtkIconSize,c_char_p]
        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_widget_render_icon( self._object,stock_id,size,detail ) or POINTER(c_int)())

    def get_tooltip_text(  self, ):

        libgtk3.gtk_widget_get_tooltip_text.restype = c_char_p
        libgtk3.gtk_widget_get_tooltip_text.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_tooltip_text( self._object )

    def set_hexpand(  self, expand, ):

        libgtk3.gtk_widget_set_hexpand.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_hexpand( self._object,expand )

    def get_child_visible(  self, ):

        libgtk3.gtk_widget_get_child_visible.restype = gboolean
        libgtk3.gtk_widget_get_child_visible.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_child_visible( self._object )

    def get_margin_right(  self, ):

        libgtk3.gtk_widget_get_margin_right.restype = gint
        libgtk3.gtk_widget_get_margin_right.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_margin_right( self._object )

    def get_pango_context(  self, ):

        libgtk3.gtk_widget_get_pango_context.restype = _PangoContext
        libgtk3.gtk_widget_get_pango_context.argtypes = [_GtkWidget]
        from gtk3 import PangoContext
        return PangoContext( obj=libgtk3.gtk_widget_get_pango_context( self._object )  or POINTER(c_int)())

    def get_device_events(  self, device, ):
        if device: device = device._object
        else: device = POINTER(c_int)()

        libgtk3.gtk_widget_get_device_events.restype = GdkEventMask
        libgtk3.gtk_widget_get_device_events.argtypes = [_GtkWidget,_GdkDevice]
        
        return libgtk3.gtk_widget_get_device_events( self._object,device )

    def set_vexpand_set(  self, set, ):

        libgtk3.gtk_widget_set_vexpand_set.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_vexpand_set( self._object,set )

    def set_parent(  self, parent, ):
        if parent: parent = parent._object
        else: parent = POINTER(c_int)()

        libgtk3.gtk_widget_set_parent.argtypes = [_GtkWidget,_GtkWidget]
        
        libgtk3.gtk_widget_set_parent( self._object,parent )

    def add_accelerator(  self, accel_signal, accel_group, accel_key, accel_mods, accel_flags, ):
        if accel_group: accel_group = accel_group._object
        else: accel_group = POINTER(c_int)()
        if accel_flags: accel_flags = accel_flags._object
        else: accel_flags = POINTER(c_int)()

        libgtk3.gtk_widget_add_accelerator.argtypes = [_GtkWidget,c_char_p,_GtkAccelGroup,guint,GdkModifierType,GtkAccelFlags]
        
        libgtk3.gtk_widget_add_accelerator( self._object,accel_signal,accel_group,accel_key,accel_mods,accel_flags )

    def get_state_flags(  self, ):

        libgtk3.gtk_widget_get_state_flags.restype = GtkStateFlags
        libgtk3.gtk_widget_get_state_flags.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_state_flags( self._object )

    def get_sensitive(  self, ):

        libgtk3.gtk_widget_get_sensitive.restype = gboolean
        libgtk3.gtk_widget_get_sensitive.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_sensitive( self._object )

    def hide_on_delete(  self, ):

        libgtk3.gtk_widget_hide_on_delete.restype = gboolean
        libgtk3.gtk_widget_hide_on_delete.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_hide_on_delete( self._object )

    def reparent(  self, new_parent, ):
        if new_parent: new_parent = new_parent._object
        else: new_parent = POINTER(c_int)()

        libgtk3.gtk_widget_reparent.argtypes = [_GtkWidget,_GtkWidget]
        
        libgtk3.gtk_widget_reparent( self._object,new_parent )

    def get_direction(  self, ):

        libgtk3.gtk_widget_get_direction.restype = GtkTextDirection
        libgtk3.gtk_widget_get_direction.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_direction( self._object )

    def set_margin_right(  self, margin, ):

        libgtk3.gtk_widget_set_margin_right.argtypes = [_GtkWidget,gint]
        
        libgtk3.gtk_widget_set_margin_right( self._object,margin )

    def get_allocation(  self, allocation, ):
        if allocation: allocation = allocation._object
        else: allocation = POINTER(c_int)()

        libgtk3.gtk_widget_get_allocation.argtypes = [_GtkWidget,_GtkAllocation]
        
        libgtk3.gtk_widget_get_allocation( self._object,allocation )

    def get_no_show_all(  self, ):

        libgtk3.gtk_widget_get_no_show_all.restype = gboolean
        libgtk3.gtk_widget_get_no_show_all.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_no_show_all( self._object )

    def list_mnemonic_labels(  self, ):

        libgtk3.gtk_widget_list_mnemonic_labels.restype = _GList
        libgtk3.gtk_widget_list_mnemonic_labels.argtypes = [_GtkWidget]
        from gobject import GList
        return GList( obj=libgtk3.gtk_widget_list_mnemonic_labels( self._object ) or POINTER(c_int)())

    def override_symbolic_color(  self, name, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_widget_override_symbolic_color.argtypes = [_GtkWidget,c_char_p,_GdkRGBA]
        
        libgtk3.gtk_widget_override_symbolic_color( self._object,name,color )

    def class_path(  self, path_length, path, path_reversed, ):

        libgtk3.gtk_widget_class_path.argtypes = [_GtkWidget,POINTER(guint),c_char_p,c_char_p]
        
        libgtk3.gtk_widget_class_path( self._object,path_length,path,path_reversed )

    def freeze_child_notify(  self, ):

        libgtk3.gtk_widget_freeze_child_notify.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_freeze_child_notify( self._object )

    def get_margin_left(  self, ):

        libgtk3.gtk_widget_get_margin_left.restype = gint
        libgtk3.gtk_widget_get_margin_left.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_margin_left( self._object )

    def input_shape_combine_region(  self, region, ):
        if region: region = region._object
        else: region = POINTER(c_int)()

        libgtk3.gtk_widget_input_shape_combine_region.argtypes = [_GtkWidget,_cairo_region_t]
        
        libgtk3.gtk_widget_input_shape_combine_region( self._object,region )

    def set_valign(  self, align, ):

        libgtk3.gtk_widget_set_valign.argtypes = [_GtkWidget,GtkAlign]
        
        libgtk3.gtk_widget_set_valign( self._object,align )

    def set_visual(  self, visual, ):
        if visual: visual = visual._object
        else: visual = POINTER(c_int)()

        libgtk3.gtk_widget_set_visual.argtypes = [_GtkWidget,_GdkVisual]
        
        libgtk3.gtk_widget_set_visual( self._object,visual )

    def style_get_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        libgtk3.gtk_widget_style_get_property.argtypes = [_GtkWidget,c_char_p,_GValue]
        
        libgtk3.gtk_widget_style_get_property( self._object,property_name,value )

    def remove_mnemonic_label(  self, label, ):
        if label: label = label._object
        else: label = POINTER(c_int)()

        libgtk3.gtk_widget_remove_mnemonic_label.argtypes = [_GtkWidget,_GtkWidget]
        
        libgtk3.gtk_widget_remove_mnemonic_label( self._object,label )

    def has_screen(  self, ):

        libgtk3.gtk_widget_has_screen.restype = gboolean
        libgtk3.gtk_widget_has_screen.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_has_screen( self._object )

    def grab_default(  self, ):

        libgtk3.gtk_widget_grab_default.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_grab_default( self._object )

    def trigger_tooltip_query(  self, ):

        libgtk3.gtk_widget_trigger_tooltip_query.argtypes = [_GtkWidget]
        
        libgtk3.gtk_widget_trigger_tooltip_query( self._object )

    def set_device_events(  self, device, events, ):
        if device: device = device._object
        else: device = POINTER(c_int)()

        libgtk3.gtk_widget_set_device_events.argtypes = [_GtkWidget,_GdkDevice,GdkEventMask]
        
        libgtk3.gtk_widget_set_device_events( self._object,device,events )

    def get_path(  self, ):

        libgtk3.gtk_widget_get_path.restype = _GtkWidgetPath
        libgtk3.gtk_widget_get_path.argtypes = [_GtkWidget]
        from gtk3 import GtkWidgetPath
        return GtkWidgetPath( obj=libgtk3.gtk_widget_get_path( self._object ) or POINTER(c_int)())

    def keynav_failed(  self, direction, ):

        libgtk3.gtk_widget_keynav_failed.restype = gboolean
        libgtk3.gtk_widget_keynav_failed.argtypes = [_GtkWidget,GtkDirectionType]
        
        return libgtk3.gtk_widget_keynav_failed( self._object,direction )

    def get_settings(  self, ):

        libgtk3.gtk_widget_get_settings.restype = _GtkSettings
        libgtk3.gtk_widget_get_settings.argtypes = [_GtkWidget]
        from gtk3 import GtkSettings
        return GtkSettings( obj=libgtk3.gtk_widget_get_settings( self._object ) or POINTER(c_int)())

    def modify_fg(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_widget_modify_fg.argtypes = [_GtkWidget,GtkStateType,_GdkColor]
        
        libgtk3.gtk_widget_modify_fg( self._object,state,color )

    def set_state_flags(  self, flags, clear, ):

        libgtk3.gtk_widget_set_state_flags.argtypes = [_GtkWidget,GtkStateFlags,gboolean]
        
        libgtk3.gtk_widget_set_state_flags( self._object,flags,clear )

    def modify_base(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_widget_modify_base.argtypes = [_GtkWidget,GtkStateType,_GdkColor]
        
        libgtk3.gtk_widget_modify_base( self._object,state,color )

    def create_pango_layout(  self, text, ):

        libgtk3.gtk_widget_create_pango_layout.restype = _PangoLayout
        libgtk3.gtk_widget_create_pango_layout.argtypes = [_GtkWidget,c_char_p]
        from gtk3 import PangoLayout
        return PangoLayout(None,None, obj=libgtk3.gtk_widget_create_pango_layout( self._object,text )  or POINTER(c_int)())

    def set_hexpand_set(  self, set, ):

        libgtk3.gtk_widget_set_hexpand_set.argtypes = [_GtkWidget,gboolean]
        
        libgtk3.gtk_widget_set_hexpand_set( self._object,set )

    def set_margin_bottom(  self, margin, ):

        libgtk3.gtk_widget_set_margin_bottom.argtypes = [_GtkWidget,gint]
        
        libgtk3.gtk_widget_set_margin_bottom( self._object,margin )

    def get_tooltip_markup(  self, ):

        libgtk3.gtk_widget_get_tooltip_markup.restype = c_char_p
        libgtk3.gtk_widget_get_tooltip_markup.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_get_tooltip_markup( self._object )

    def get_requisition(  self, requisition, ):
        if requisition: requisition = requisition._object
        else: requisition = POINTER(c_int)()

        libgtk3.gtk_widget_get_requisition.argtypes = [_GtkWidget,_GtkRequisition]
        
        libgtk3.gtk_widget_get_requisition( self._object,requisition )

    def has_rc_style(  self, ):

        libgtk3.gtk_widget_has_rc_style.restype = gboolean
        libgtk3.gtk_widget_has_rc_style.argtypes = [_GtkWidget]
        
        return libgtk3.gtk_widget_has_rc_style( self._object )

    @staticmethod
    def gtk_distribute_natural_allocation( extra_space, n_requested_sizes, sizes,):
        libgtk3.gtk_distribute_natural_allocation.restype = gint
        libgtk3.gtk_distribute_natural_allocation.argtypes = [gint,guint,POINTER(GtkRequestedSize)]
        
        return     libgtk3.gtk_distribute_natural_allocation(extra_space, n_requested_sizes, sizes, )

    @staticmethod
    def gtk_cairo_should_draw_window( cr, window,):
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()
        if window: window = window._object
        else: window = POINTER(c_int)()
        libgtk3.gtk_cairo_should_draw_window.restype = gboolean
        libgtk3.gtk_cairo_should_draw_window.argtypes = [_cairo_t,_GdkWindow]
        
        return     libgtk3.gtk_cairo_should_draw_window(cr, window, )

    @staticmethod
    def class_list_style_properties( klass, n_properties,):
        if klass: klass = klass._object
        else: klass = POINTER(c_int)()
        libgtk3.gtk_widget_class_list_style_properties.restype = _GParamSpec
        libgtk3.gtk_widget_class_list_style_properties.argtypes = [_GtkWidgetClass,POINTER(guint)]
        from gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.gtk_widget_class_list_style_properties(klass, n_properties, )
 or POINTER(c_int)())
    @staticmethod
    def get_default_direction():
        libgtk3.gtk_widget_get_default_direction.restype = GtkTextDirection
        
        return     libgtk3.gtk_widget_get_default_direction()

    @staticmethod
    def pop_composite_child():
        
            libgtk3.gtk_widget_pop_composite_child()

    @staticmethod
    def push_composite_child():
        
            libgtk3.gtk_widget_push_composite_child()

    @staticmethod
    def class_find_style_property( klass, property_name,):
        if klass: klass = klass._object
        else: klass = POINTER(c_int)()
        libgtk3.gtk_widget_class_find_style_property.restype = _GParamSpec
        libgtk3.gtk_widget_class_find_style_property.argtypes = [_GtkWidgetClass,c_char_p]
        from gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.gtk_widget_class_find_style_property(klass, property_name, )
 or POINTER(c_int)())
    @staticmethod
    def get_default_style():
        libgtk3.gtk_widget_get_default_style.restype = _GtkStyle
        from gtk3 import GtkStyle
        return GtkStyle( obj=    libgtk3.gtk_widget_get_default_style()
 or POINTER(c_int)())
    def __del__(self):
        libgtk3.gtk_widget_destroy.argtypes=[c_void_p]
        libgtk3.gtk_widget_destroy(self._object)
        self._object = None