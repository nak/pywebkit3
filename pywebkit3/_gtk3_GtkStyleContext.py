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
_GdkPixbuf = c_void_p
__GtkRequisition = c_void_p
_GtkRcStyle = c_void_p
__GtkRegionFlags = c_void_p
_GdkEvent = c_void_p
_GtkWindow = c_void_p
__cairo_font_options_t = c_void_p
__GdkAtom = c_void_p
__GdkTimeCoord = c_void_p
__GtkWidgetPath = c_void_p
_GdkDisplay = c_void_p
__GtkStyleProvider = c_void_p
_PangoFont = c_void_p
_GtkStyleContext = c_void_p
_guchar = c_void_p
_GdkAppLaunchContext = c_void_p
__PangoLayout = c_void_p
__GParamSpec = c_void_p
__PangoAttrIterator = c_void_p
__GtkWindow = c_void_p
_GtkWindowGroup = c_void_p
__PangoContext = c_void_p
__PangoFontMap = c_void_p
__PangoAttrList = c_void_p
_PangoMatrix = c_void_p
_GtkApplication = c_void_p
__PangoAnalysis = c_void_p
_PangoFontDescription = c_void_p
__GdkCursor = c_void_p
__GtkWidgetClass = c_void_p
__GdkEventKey = c_void_p
__GdkDisplay = c_void_p
_GtkWidgetPath = c_void_p
_GdkScreen = c_void_p
_PangoFontMetrics = c_void_p
_GdkVisual = c_void_p
_PangoFontMap = c_void_p
_GtkWidget = c_void_p
__GdkWindow = c_void_p
__PangoFontFamily = c_void_p
__cairo_region_t = c_void_p
_PangoFontset = c_void_p
_GdkWindow = c_void_p
__PangoFontDescription = c_void_p
__GtkBorder = c_void_p
__GError = c_void_p
__PangoCoverage = c_void_p
__cairo_t = c_void_p
__GdkVisual = c_void_p
_GdkDevice = c_void_p
_GList = c_void_p
__GtkAccelGroup = c_void_p
_GtkIconSet = c_void_p
__GtkAllocation = c_void_p
__GtkWidget = c_void_p
_gchar = c_void_p
__GValue = c_void_p
_GdkDeviceManager = c_void_p
_GdkCursor = c_void_p
__PangoMatrix = c_void_p
_PangoContext = c_void_p
__GList = c_void_p
_PangoCoverage = c_void_p
_GParamSpec = c_void_p
__PangoRectangle = c_void_p
__GtkIconSource = c_void_p
_char = c_void_p
__PangoGlyphString = c_void_p
__GdkRGBA = c_void_p
__GdkWindowAttr = c_void_p
__GdkColor = c_void_p
__GdkRectangle = c_void_p
__PangoLanguage = c_void_p
__GdkWMDecoration = c_void_p
__PangoLogAttr = c_void_p
_PangoLayout = c_void_p
_GtkStyle = c_void_p
__GtkStyle = c_void_p
__GIcon = c_void_p
__cairo_pattern_t = c_void_p
__GdkPixbuf = c_void_p
_GtkSettings = c_void_p
__GtkApplication = c_void_p
_GtkClipboard = c_void_p
__GdkScreen = c_void_p
_PangoLanguage = c_void_p
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
GdkVisualType = c_int
GdkByteOrder = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int

import _gobject_GObject
class GtkStyleContext( _gobject_GObject.GObject):
    """Class GtkStyleContext Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_style_context_new.restype = c_void_p

        libgtk3.gtk_style_context_new.argtypes = []
        self._object = libgtk3.gtk_style_context_new()

    """Methods"""
    def remove_provider(self,  provider,):
        if provider : provider = provider._object
        else : provider = c_void_p()

        libgtk3.gtk_style_context_remove_provider.argtypes = [c_void_p, _GtkStyleProvider]
        
        libgtk3.gtk_style_context_remove_provider(self._object,  provider,)

    def get_junction_sides(self, ):

        libgtk3.gtk_style_context_get_junction_sides.restype = GtkJunctionSides
        libgtk3.gtk_style_context_get_junction_sides.argtypes = [c_void_p]
        
        return libgtk3.gtk_style_context_get_junction_sides(self._object, )

    def has_class(self,  class_name,):

        libgtk3.gtk_style_context_has_class.restype = gboolean
        libgtk3.gtk_style_context_has_class.argtypes = [c_void_p, c_char_p]
        
        return libgtk3.gtk_style_context_has_class(self._object,  class_name,)

    def add_class(self,  class_name,):

        libgtk3.gtk_style_context_add_class.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_style_context_add_class(self._object,  class_name,)

    def add_region(self,  region_name, flags,):
        if flags : flags = flags._object
        else : flags = c_void_p()

        libgtk3.gtk_style_context_add_region.argtypes = [c_void_p, c_char_p,GtkRegionFlags]
        
        libgtk3.gtk_style_context_add_region(self._object,  region_name, flags,)

    def push_animatable_region(self,  region_id,):

        libgtk3.gtk_style_context_push_animatable_region.argtypes = [c_void_p, gpointer]
        
        libgtk3.gtk_style_context_push_animatable_region(self._object,  region_id,)

    def set_junction_sides(self,  sides,):

        libgtk3.gtk_style_context_set_junction_sides.argtypes = [c_void_p, GtkJunctionSides]
        
        libgtk3.gtk_style_context_set_junction_sides(self._object,  sides,)

    def scroll_animations(self,  window, dx, dy,):
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gtk_style_context_scroll_animations.argtypes = [c_void_p, _GdkWindow,gint,gint]
        
        libgtk3.gtk_style_context_scroll_animations(self._object,  window, dx, dy,)

    def get_state(self, ):

        libgtk3.gtk_style_context_get_state.restype = GtkStateFlags
        libgtk3.gtk_style_context_get_state.argtypes = [c_void_p]
        
        return libgtk3.gtk_style_context_get_state(self._object, )

    def set_screen(self,  screen,):
        if screen : screen = screen._object
        else : screen = c_void_p()

        libgtk3.gtk_style_context_set_screen.argtypes = [c_void_p, _GdkScreen]
        
        libgtk3.gtk_style_context_set_screen(self._object,  screen,)

    def get_style_property(self,  property_name, value,):
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.gtk_style_context_get_style_property.argtypes = [c_void_p, c_char_p,_GValue]
        
        libgtk3.gtk_style_context_get_style_property(self._object,  property_name, value,)

    def list_regions(self, ):

        libgtk3.gtk_style_context_list_regions.restype = _GList
        libgtk3.gtk_style_context_list_regions.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gtk_style_context_list_regions(self._object, ) or c_void_p())

    def set_background(self,  window,):
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gtk_style_context_set_background.argtypes = [c_void_p, _GdkWindow]
        
        libgtk3.gtk_style_context_set_background(self._object,  window,)

    def get_screen(self, ):

        libgtk3.gtk_style_context_get_screen.restype = _GdkScreen
        libgtk3.gtk_style_context_get_screen.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gtk_style_context_get_screen(self._object, ) or c_void_p())

    def save(self, ):

        libgtk3.gtk_style_context_save.argtypes = [c_void_p]
        
        libgtk3.gtk_style_context_save(self._object, )

    def get_border_color(self,  state, color,):
        if color : color = color._object
        else : color = c_void_p()

        libgtk3.gtk_style_context_get_border_color.argtypes = [c_void_p, GtkStateFlags,_GdkRGBA]
        
        libgtk3.gtk_style_context_get_border_color(self._object,  state, color,)

    def get_margin(self,  state, margin,):
        if margin : margin = margin._object
        else : margin = c_void_p()

        libgtk3.gtk_style_context_get_margin.argtypes = [c_void_p, GtkStateFlags,_GtkBorder]
        
        libgtk3.gtk_style_context_get_margin(self._object,  state, margin,)

    def lookup_icon_set(self,  stock_id,):

        libgtk3.gtk_style_context_lookup_icon_set.restype = _GtkIconSet
        libgtk3.gtk_style_context_lookup_icon_set.argtypes = [c_void_p, c_char_p]
        from pywebkit3.gtk3 import GtkIconSet
        return GtkIconSet( obj=libgtk3.gtk_style_context_lookup_icon_set(self._object,  stock_id,) or c_void_p())

    def get_direction(self, ):

        libgtk3.gtk_style_context_get_direction.restype = GtkTextDirection
        libgtk3.gtk_style_context_get_direction.argtypes = [c_void_p]
        
        return libgtk3.gtk_style_context_get_direction(self._object, )

    def get_property(self,  property, state, value,):
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.gtk_style_context_get_property.argtypes = [c_void_p, c_char_p,GtkStateFlags,_GValue]
        
        libgtk3.gtk_style_context_get_property(self._object,  property, state, value,)

    def restore(self, ):

        libgtk3.gtk_style_context_restore.argtypes = [c_void_p]
        
        libgtk3.gtk_style_context_restore(self._object, )

    def get_font(self,  state,):

        libgtk3.gtk_style_context_get_font.restype = _PangoFontDescription
        libgtk3.gtk_style_context_get_font.argtypes = [c_void_p, GtkStateFlags]
        from pywebkit3.gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libgtk3.gtk_style_context_get_font(self._object,  state,)  or c_void_p())

    def get(self,  state,*args ):


        def callit( state, *args ):
                libgtk3.gtk_style_context_get.restype = None
                libgtk3.gtk_style_context_get.argtypes = [c_void_p, c_void_p, GtkStateFlags]
                for arg in args:
                     libgtk3.gtk_style_context_get.argtypes.append(args[1])
                return libgtk3.gtk_style_context_get(self._object, state, *args)
    
        return callit( state,*args )

    def list_classes(self, ):

        libgtk3.gtk_style_context_list_classes.restype = _GList
        libgtk3.gtk_style_context_list_classes.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gtk_style_context_list_classes(self._object, ) or c_void_p())

    def add_provider(self,  provider, priority,):
        if provider : provider = provider._object
        else : provider = c_void_p()

        libgtk3.gtk_style_context_add_provider.argtypes = [c_void_p, _GtkStyleProvider,guint]
        
        libgtk3.gtk_style_context_add_provider(self._object,  provider, priority,)

    def state_is_running(self,  state, progress,):
        if progress : progress = progress._object
        else : progress = c_void_p()

        libgtk3.gtk_style_context_state_is_running.restype = gboolean
        libgtk3.gtk_style_context_state_is_running.argtypes = [c_void_p, GtkStateType,POITNER(gdouble)]
        
        return libgtk3.gtk_style_context_state_is_running(self._object,  state, progress,)

    def set_path(self,  path,):
        if path : path = path._object
        else : path = c_void_p()

        libgtk3.gtk_style_context_set_path.argtypes = [c_void_p, _GtkWidgetPath]
        
        libgtk3.gtk_style_context_set_path(self._object,  path,)

    def lookup_color(self,  color_name, color,):
        if color : color = color._object
        else : color = c_void_p()

        libgtk3.gtk_style_context_lookup_color.restype = gboolean
        libgtk3.gtk_style_context_lookup_color.argtypes = [c_void_p, c_char_p,_GdkRGBA]
        
        return libgtk3.gtk_style_context_lookup_color(self._object,  color_name, color,)

    def get_border(self,  state, border,):
        if border : border = border._object
        else : border = c_void_p()

        libgtk3.gtk_style_context_get_border.argtypes = [c_void_p, GtkStateFlags,_GtkBorder]
        
        libgtk3.gtk_style_context_get_border(self._object,  state, border,)

    def remove_class(self,  class_name,):

        libgtk3.gtk_style_context_remove_class.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_style_context_remove_class(self._object,  class_name,)

    def remove_region(self,  region_name,):

        libgtk3.gtk_style_context_remove_region.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_style_context_remove_region(self._object,  region_name,)

    def set_state(self,  flags,):

        libgtk3.gtk_style_context_set_state.argtypes = [c_void_p, GtkStateFlags]
        
        libgtk3.gtk_style_context_set_state(self._object,  flags,)

    def cancel_animations(self,  region_id,):

        libgtk3.gtk_style_context_cancel_animations.argtypes = [c_void_p, gpointer]
        
        libgtk3.gtk_style_context_cancel_animations(self._object,  region_id,)

    def pop_animatable_region(self, ):

        libgtk3.gtk_style_context_pop_animatable_region.argtypes = [c_void_p]
        
        libgtk3.gtk_style_context_pop_animatable_region(self._object, )

    def invalidate(self, ):

        libgtk3.gtk_style_context_invalidate.argtypes = [c_void_p]
        
        libgtk3.gtk_style_context_invalidate(self._object, )

    def get_color(self,  state, color,):
        if color : color = color._object
        else : color = c_void_p()

        libgtk3.gtk_style_context_get_color.argtypes = [c_void_p, GtkStateFlags,_GdkRGBA]
        
        libgtk3.gtk_style_context_get_color(self._object,  state, color,)

    def set_direction(self,  direction,):

        libgtk3.gtk_style_context_set_direction.argtypes = [c_void_p, GtkTextDirection]
        
        libgtk3.gtk_style_context_set_direction(self._object,  direction,)

    def reset_widgets(self,  screen,):
        if screen : screen = screen._object
        else : screen = c_void_p()

        libgtk3.gtk_style_context_reset_widgets.argtypes = [c_void_p, _GdkScreen]
        
        libgtk3.gtk_style_context_reset_widgets(self._object,  screen,)

    def get_background_color(self,  state, color,):
        if color : color = color._object
        else : color = c_void_p()

        libgtk3.gtk_style_context_get_background_color.argtypes = [c_void_p, GtkStateFlags,_GdkRGBA]
        
        libgtk3.gtk_style_context_get_background_color(self._object,  state, color,)

    def get_style(self, *args ):


        def callit(  *args ):
                libgtk3.gtk_style_context_get_style.restype = None
                libgtk3.gtk_style_context_get_style.argtypes = [c_void_p, c_void_p]
                for arg in args:
                     libgtk3.gtk_style_context_get_style.argtypes.append(args[1])
                return libgtk3.gtk_style_context_get_style(self._object,  *args)
    
        return callit(*args )

    def has_region(self,  region_name, flags_return,):
        if flags_return : flags_return = flags_return._object
        else : flags_return = c_void_p()

        libgtk3.gtk_style_context_has_region.restype = gboolean
        libgtk3.gtk_style_context_has_region.argtypes = [c_void_p, c_char_p,_GtkRegionFlags]
        
        return libgtk3.gtk_style_context_has_region(self._object,  region_name, flags_return,)

    def get_path(self, ):

        libgtk3.gtk_style_context_get_path.restype = _GtkWidgetPath
        libgtk3.gtk_style_context_get_path.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidgetPath
        return GtkWidgetPath(None, obj=libgtk3.gtk_style_context_get_path(self._object, ) or c_void_p())

    def notify_state_change(self,  window, region_id, state, state_value,):
        if window : window = window._object
        else : window = c_void_p()

        libgtk3.gtk_style_context_notify_state_change.argtypes = [c_void_p, _GdkWindow,gpointer,GtkStateType,gboolean]
        
        libgtk3.gtk_style_context_notify_state_change(self._object,  window, region_id, state, state_value,)

    def add_provider_for_screen(self,  screen, provider, priority,):
        if screen : screen = screen._object
        else : screen = c_void_p()
        if provider : provider = provider._object
        else : provider = c_void_p()

        libgtk3.gtk_style_context_add_provider_for_screen.argtypes = [c_void_p, _GdkScreen,_GtkStyleProvider,guint]
        
        libgtk3.gtk_style_context_add_provider_for_screen(self._object,  screen, provider, priority,)

    def remove_provider_for_screen(self,  screen, provider,):
        if screen : screen = screen._object
        else : screen = c_void_p()
        if provider : provider = provider._object
        else : provider = c_void_p()

        libgtk3.gtk_style_context_remove_provider_for_screen.argtypes = [c_void_p, _GdkScreen,_GtkStyleProvider]
        
        libgtk3.gtk_style_context_remove_provider_for_screen(self._object,  screen, provider,)

    def get_padding(self,  state, padding,):
        if padding : padding = padding._object
        else : padding = c_void_p()

        libgtk3.gtk_style_context_get_padding.argtypes = [c_void_p, GtkStateFlags,_GtkBorder]
        
        libgtk3.gtk_style_context_get_padding(self._object,  state, padding,)

