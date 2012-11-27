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

import _gobject_GObject
class GtkStyle( _gobject_GObject.GObject):
    """Class GtkStyle Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_style_new.restype = c_void_p

        libgtk3.gtk_style_new.argtypes = []
        self._object = libgtk3.gtk_style_new()

    """Methods"""
    def gtk_paint_slider(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height, orientation,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_slider.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkOrientation]
        
        libgtk3.gtk_paint_slider(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height, orientation,)

    def gtk_paint_resize_grip(self,  cr, state_type, widget, detail, edge, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()
        if edge : edge = edge._object
        else : edge = c_void_p()

        libgtk3.gtk_paint_resize_grip.argtypes = [c_void_p, _cairo_t,GtkStateType,_GtkWidget,c_char_p,GdkWindowEdge,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_resize_grip(self._object,  cr, state_type, widget, detail, edge, x, y, width, height,)

    def gtk_paint_arrow(self,  cr, state_type, shadow_type, widget, detail, arrow_type, fill, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()
        if arrow_type : arrow_type = arrow_type._object
        else : arrow_type = c_void_p()

        libgtk3.gtk_paint_arrow.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,GtkArrowType,gboolean,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_arrow(self._object,  cr, state_type, shadow_type, widget, detail, arrow_type, fill, x, y, width, height,)

    def get_style_property(self,  widget_type, property_name, value,):
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.gtk_style_get_style_property.argtypes = [c_void_p, GType,c_char_p,_GValue]
        
        libgtk3.gtk_style_get_style_property(self._object,  widget_type, property_name, value,)

    def gtk_paint_expander(self,  cr, state_type, widget, detail, x, y, expander_style,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_expander.argtypes = [c_void_p, _cairo_t,GtkStateType,_GtkWidget,c_char_p,gint,gint,GtkExpanderStyle]
        
        libgtk3.gtk_paint_expander(self._object,  cr, state_type, widget, detail, x, y, expander_style,)

    def gtk_paint_flat_box(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_flat_box.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_flat_box(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height,)

    def get(self,  widget_type, first_property_name,*args ):


        def callit( widget_type, first_property_name, *args ):
                libgtk3.gtk_style_get.restype = None
                libgtk3.gtk_style_get.argtypes = [c_void_p, c_void_p, GType, c_char_p]
                for arg in args:
                     libgtk3.gtk_style_get.argtypes.append(args[1])
                return libgtk3.gtk_style_get(self._object, widget_type, first_property_name, *args)
    
        return callit( widget_type, first_property_name,*args )

    def render_icon(self,  source, direction, state, size, widget, detail,):
        if source : source = source._object
        else : source = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_style_render_icon.restype = _GdkPixbuf
        libgtk3.gtk_style_render_icon.argtypes = [c_void_p, _GtkIconSource,GtkTextDirection,GtkStateType,GtkIconSize,_GtkWidget,c_char_p]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_style_render_icon(self._object,  source, direction, state, size, widget, detail,) or c_void_p())

    def has_context(self, ):

        libgtk3.gtk_style_has_context.restype = gboolean
        libgtk3.gtk_style_has_context.argtypes = [c_void_p]
        
        return libgtk3.gtk_style_has_context(self._object, )

    def lookup_icon_set(self,  stock_id,):

        libgtk3.gtk_style_lookup_icon_set.restype = _GtkIconSet
        libgtk3.gtk_style_lookup_icon_set.argtypes = [c_void_p, c_char_p]
        from pywebkit3.gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_style_lookup_icon_set(self._object,  stock_id,) or c_void_p())

    def gtk_paint_shadow_gap(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, gap_x, gap_width,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()
        if gap_side : gap_side = gap_side._object
        else : gap_side = c_void_p()

        libgtk3.gtk_paint_shadow_gap.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkPositionType,gint,gint]
        
        libgtk3.gtk_paint_shadow_gap(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, gap_x, gap_width,)

    def gtk_paint_check(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_check.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_check(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height,)

    def gtk_paint_hline(self,  cr, state_type, widget, detail, x1, x2, y,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_hline.argtypes = [c_void_p, _cairo_t,GtkStateType,_GtkWidget,c_char_p,gint,gint,gint]
        
        libgtk3.gtk_paint_hline(self._object,  cr, state_type, widget, detail, x1, x2, y,)

    def gtk_paint_shadow(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_shadow.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_shadow(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height,)

    def gtk_paint_diamond(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_diamond.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_diamond(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height,)

    def detach(self, ):

        libgtk3.gtk_style_detach.argtypes = [c_void_p]
        
        libgtk3.gtk_style_detach(self._object, )

    def lookup_color(self,  color_name, color,):
        if color : color = color._object
        else : color = c_void_p()

        libgtk3.gtk_style_lookup_color.restype = gboolean
        libgtk3.gtk_style_lookup_color.argtypes = [c_void_p, c_char_p,_GdkColor]
        
        return libgtk3.gtk_style_lookup_color(self._object,  color_name, color,)

    def attach(self,  window,):
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gtk_style_attach.restype = _GtkStyle
        libgtk3.gtk_style_attach.argtypes = [c_void_p, _GdkWindow]
        from pywebkit3.gtk3 import GtkStyle
        return GtkStyle(None,None, obj=libgtk3.gtk_style_attach(self._object,  window,) or c_void_p())

    def gtk_paint_box_gap(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, gap_x, gap_width,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()
        if gap_side : gap_side = gap_side._object
        else : gap_side = c_void_p()

        libgtk3.gtk_paint_box_gap.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkPositionType,gint,gint]
        
        libgtk3.gtk_paint_box_gap(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side, gap_x, gap_width,)

    def gtk_paint_tab(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_tab.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_tab(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height,)

    def gtk_paint_spinner(self,  cr, state_type, widget, detail, step, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_spinner.argtypes = [c_void_p, _cairo_t,GtkStateType,_GtkWidget,c_char_p,guint,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_spinner(self._object,  cr, state_type, widget, detail, step, x, y, width, height,)

    def gtk_paint_layout(self,  cr, state_type, use_text, widget, detail, x, y, layout,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()
        if layout : layout = layout._object
        else : layout = c_void_p()

        libgtk3.gtk_paint_layout.argtypes = [c_void_p, _cairo_t,GtkStateType,gboolean,_GtkWidget,c_char_p,gint,gint,_PangoLayout]
        
        libgtk3.gtk_paint_layout(self._object,  cr, state_type, use_text, widget, detail, x, y, layout,)

    def gtk_draw_insertion_cursor(self,  widget, cr, location, is_primary, direction, draw_arrow,):
        if widget : widget = widget._object
        else : widget = c_void_p()
        if cr : cr = cr._object
        else : cr = c_void_p()
        if location : location = location._object
        else : location = c_void_p()

        libgtk3.gtk_draw_insertion_cursor.argtypes = [c_void_p, _GtkWidget,_cairo_t,_GdkRectangle,gboolean,GtkTextDirection,gboolean]
        
        libgtk3.gtk_draw_insertion_cursor(self._object,  widget, cr, location, is_primary, direction, draw_arrow,)

    def apply_default_background(self,  cr, window, state_type, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gtk_style_apply_default_background.argtypes = [c_void_p, _cairo_t,_GdkWindow,GtkStateType,gint,gint,gint,gint]
        
        libgtk3.gtk_style_apply_default_background(self._object,  cr, window, state_type, x, y, width, height,)

    def gtk_paint_focus(self,  cr, state_type, widget, detail, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_focus.argtypes = [c_void_p, _cairo_t,GtkStateType,_GtkWidget,c_char_p,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_focus(self._object,  cr, state_type, widget, detail, x, y, width, height,)

    def gtk_paint_extension(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()
        if gap_side : gap_side = gap_side._object
        else : gap_side = c_void_p()

        libgtk3.gtk_paint_extension.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkPositionType]
        
        libgtk3.gtk_paint_extension(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height, gap_side,)

    def copy(self, ):

        libgtk3.gtk_style_copy.restype = _GtkStyle
        libgtk3.gtk_style_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkStyle
        return GtkStyle(None, obj=libgtk3.gtk_style_copy(self._object, ) or c_void_p())

    def gtk_paint_vline(self,  cr, state_type, widget, detail, y1_, y2_, x,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_vline.argtypes = [c_void_p, _cairo_t,GtkStateType,_GtkWidget,c_char_p,gint,gint,gint]
        
        libgtk3.gtk_paint_vline(self._object,  cr, state_type, widget, detail, y1_, y2_, x,)

    def gtk_paint_handle(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height, orientation,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_handle.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint,GtkOrientation]
        
        libgtk3.gtk_paint_handle(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height, orientation,)

    def gtk_paint_box(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_box.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_box(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height,)

    def set_background(self,  window, state_type,):
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gtk_style_set_background.argtypes = [c_void_p, _GdkWindow,GtkStateType]
        
        libgtk3.gtk_style_set_background(self._object,  window, state_type,)

    def gtk_paint_option(self,  cr, state_type, shadow_type, widget, detail, x, y, width, height,):
        if cr : cr = cr._object
        else : cr = c_void_p()
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_paint_option.argtypes = [c_void_p, _cairo_t,GtkStateType,GtkShadowType,_GtkWidget,c_char_p,gint,gint,gint,gint]
        
        libgtk3.gtk_paint_option(self._object,  cr, state_type, shadow_type, widget, detail, x, y, width, height,)

