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
__GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
__GClosure = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
__GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
__GObject = POINTER(c_int)
__PangoLayout = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
__GParamSpec = POINTER(c_int)
__PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
__PangoContext = POINTER(c_int)
__JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__JSClass = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
__GtkSettings = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__PangoFontFamily = POINTER(c_int)
__JSContextGroup = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GtkBorder = POINTER(c_int)
__GError = POINTER(c_int)
__PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__JSContext = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
__GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
__PangoTabArray = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
__GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
__PangoMatrix = POINTER(c_int)
__GtkPrintOperation = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GList = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__JSPropertyNameAccumulator = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GSList = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
__GdkColor = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
__gunichar = POINTER(c_int)
__GdkWMDecoration = POINTER(c_int)
__PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
__JSObject = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GIcon = POINTER(c_int)
__GtkWindow = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
__GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
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
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
WebKitLoadStatus = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitEditingBehavior = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GtkDialogFlags = c_int
GtkResponseType = c_int

import gobject__GObject
class GtkStyleContext( gobject__GObject.GObject):
    """Class GtkStyleContext Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_style_context_new.restype = POINTER(c_int)
            
            libgtk3.gtk_style_context_new.argtypes = []
            self._object = libgtk3.gtk_style_context_new()

    """Methods"""
    def remove_provider(  self, provider, ):
        if provider: provider = provider._object
        else: provider = POINTER(c_int)()

        libgtk3.gtk_style_context_remove_provider.argtypes = [_GtkStyleContext,_GtkStyleProvider]
        
        libgtk3.gtk_style_context_remove_provider( self._object,provider )

    def get_junction_sides(  self, ):

        libgtk3.gtk_style_context_get_junction_sides.restype = GtkJunctionSides
        libgtk3.gtk_style_context_get_junction_sides.argtypes = [_GtkStyleContext]
        
        return libgtk3.gtk_style_context_get_junction_sides( self._object )

    def has_class(  self, class_name, ):

        libgtk3.gtk_style_context_has_class.restype = gboolean
        libgtk3.gtk_style_context_has_class.argtypes = [_GtkStyleContext,c_char_p]
        
        return libgtk3.gtk_style_context_has_class( self._object,class_name )

    def add_class(  self, class_name, ):

        libgtk3.gtk_style_context_add_class.argtypes = [_GtkStyleContext,c_char_p]
        
        libgtk3.gtk_style_context_add_class( self._object,class_name )

    def add_region(  self, region_name, flags, ):
        if flags: flags = flags._object
        else: flags = POINTER(c_int)()

        libgtk3.gtk_style_context_add_region.argtypes = [_GtkStyleContext,c_char_p,GtkRegionFlags]
        
        libgtk3.gtk_style_context_add_region( self._object,region_name,flags )

    def push_animatable_region(  self, region_id, ):

        libgtk3.gtk_style_context_push_animatable_region.argtypes = [_GtkStyleContext,gpointer]
        
        libgtk3.gtk_style_context_push_animatable_region( self._object,region_id )

    def set_junction_sides(  self, sides, ):

        libgtk3.gtk_style_context_set_junction_sides.argtypes = [_GtkStyleContext,GtkJunctionSides]
        
        libgtk3.gtk_style_context_set_junction_sides( self._object,sides )

    def scroll_animations(  self, window, dx, dy, ):
        if window: window = window._object
        else: window = POINTER(c_int)()

        libgtk3.gtk_style_context_scroll_animations.argtypes = [_GtkStyleContext,_GdkWindow,gint,gint]
        
        libgtk3.gtk_style_context_scroll_animations( self._object,window,dx,dy )

    def get_state(  self, ):

        libgtk3.gtk_style_context_get_state.restype = GtkStateFlags
        libgtk3.gtk_style_context_get_state.argtypes = [_GtkStyleContext]
        
        return libgtk3.gtk_style_context_get_state( self._object )

    def set_screen(  self, screen, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()

        libgtk3.gtk_style_context_set_screen.argtypes = [_GtkStyleContext,_GdkScreen]
        
        libgtk3.gtk_style_context_set_screen( self._object,screen )

    def get_style_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        libgtk3.gtk_style_context_get_style_property.argtypes = [_GtkStyleContext,c_char_p,_GValue]
        
        libgtk3.gtk_style_context_get_style_property( self._object,property_name,value )

    def list_regions(  self, ):

        libgtk3.gtk_style_context_list_regions.restype = _GList
        libgtk3.gtk_style_context_list_regions.argtypes = [_GtkStyleContext]
        from gobject import GList
        return GList( obj=libgtk3.gtk_style_context_list_regions( self._object ) or POINTER(c_int)())

    def set_background(  self, window, ):
        if window: window = window._object
        else: window = POINTER(c_int)()

        libgtk3.gtk_style_context_set_background.argtypes = [_GtkStyleContext,_GdkWindow]
        
        libgtk3.gtk_style_context_set_background( self._object,window )

    def get_screen(  self, ):

        libgtk3.gtk_style_context_get_screen.restype = _GdkScreen
        libgtk3.gtk_style_context_get_screen.argtypes = [_GtkStyleContext]
        from gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gtk_style_context_get_screen( self._object ) or POINTER(c_int)())

    def save(  self, ):

        libgtk3.gtk_style_context_save.argtypes = [_GtkStyleContext]
        
        libgtk3.gtk_style_context_save( self._object )

    def get_border_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_style_context_get_border_color.argtypes = [_GtkStyleContext,GtkStateFlags,_GdkRGBA]
        
        libgtk3.gtk_style_context_get_border_color( self._object,state,color )

    def get_margin(  self, state, margin, ):
        if margin: margin = margin._object
        else: margin = POINTER(c_int)()

        libgtk3.gtk_style_context_get_margin.argtypes = [_GtkStyleContext,GtkStateFlags,_GtkBorder]
        
        libgtk3.gtk_style_context_get_margin( self._object,state,margin )

    def lookup_icon_set(  self, stock_id, ):

        libgtk3.gtk_style_context_lookup_icon_set.restype = _GtkIconSet
        libgtk3.gtk_style_context_lookup_icon_set.argtypes = [_GtkStyleContext,c_char_p]
        from gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_style_context_lookup_icon_set( self._object,stock_id ) or POINTER(c_int)())

    def get_direction(  self, ):

        libgtk3.gtk_style_context_get_direction.restype = GtkTextDirection
        libgtk3.gtk_style_context_get_direction.argtypes = [_GtkStyleContext]
        
        return libgtk3.gtk_style_context_get_direction( self._object )

    def get_property(  self, property, state, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        libgtk3.gtk_style_context_get_property.argtypes = [_GtkStyleContext,c_char_p,GtkStateFlags,_GValue]
        
        libgtk3.gtk_style_context_get_property( self._object,property,state,value )

    def restore(  self, ):

        libgtk3.gtk_style_context_restore.argtypes = [_GtkStyleContext]
        
        libgtk3.gtk_style_context_restore( self._object )

    def get_font(  self, state, ):

        libgtk3.gtk_style_context_get_font.restype = _PangoFontDescription
        libgtk3.gtk_style_context_get_font.argtypes = [_GtkStyleContext,GtkStateFlags]
        from gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libgtk3.gtk_style_context_get_font( self._object,state )  or POINTER(c_int)())

    def get(  self, state,*args  ):


        def callit( state, *args ):
                libgtk3.gtk_style_context_get.restype = None
                libgtk3.gtk_style_context_get.argtypes = [ POINTER(c_int), GtkStateFlags]
                for arg in args:
                     libgtk3.gtk_style_context_get.argtypes.append(args[1])
                return libgtk3.gtk_style_context_get( state, *args)
    
        return callit( self._object, state,*args )

    def list_classes(  self, ):

        libgtk3.gtk_style_context_list_classes.restype = _GList
        libgtk3.gtk_style_context_list_classes.argtypes = [_GtkStyleContext]
        from gobject import GList
        return GList( obj=libgtk3.gtk_style_context_list_classes( self._object ) or POINTER(c_int)())

    def add_provider(  self, provider, priority, ):
        if provider: provider = provider._object
        else: provider = POINTER(c_int)()

        libgtk3.gtk_style_context_add_provider.argtypes = [_GtkStyleContext,_GtkStyleProvider,guint]
        
        libgtk3.gtk_style_context_add_provider( self._object,provider,priority )

    def state_is_running(  self, state, progress, ):

        libgtk3.gtk_style_context_state_is_running.restype = gboolean
        libgtk3.gtk_style_context_state_is_running.argtypes = [_GtkStyleContext,GtkStateType,POINTER(gdouble)]
        
        return libgtk3.gtk_style_context_state_is_running( self._object,state,progress )

    def set_path(  self, path, ):
        if path: path = path._object
        else: path = POINTER(c_int)()

        libgtk3.gtk_style_context_set_path.argtypes = [_GtkStyleContext,_GtkWidgetPath]
        
        libgtk3.gtk_style_context_set_path( self._object,path )

    def lookup_color(  self, color_name, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_style_context_lookup_color.restype = gboolean
        libgtk3.gtk_style_context_lookup_color.argtypes = [_GtkStyleContext,c_char_p,_GdkRGBA]
        
        return libgtk3.gtk_style_context_lookup_color( self._object,color_name,color )

    def get_border(  self, state, border, ):
        if border: border = border._object
        else: border = POINTER(c_int)()

        libgtk3.gtk_style_context_get_border.argtypes = [_GtkStyleContext,GtkStateFlags,_GtkBorder]
        
        libgtk3.gtk_style_context_get_border( self._object,state,border )

    def remove_class(  self, class_name, ):

        libgtk3.gtk_style_context_remove_class.argtypes = [_GtkStyleContext,c_char_p]
        
        libgtk3.gtk_style_context_remove_class( self._object,class_name )

    def remove_region(  self, region_name, ):

        libgtk3.gtk_style_context_remove_region.argtypes = [_GtkStyleContext,c_char_p]
        
        libgtk3.gtk_style_context_remove_region( self._object,region_name )

    def set_state(  self, flags, ):

        libgtk3.gtk_style_context_set_state.argtypes = [_GtkStyleContext,GtkStateFlags]
        
        libgtk3.gtk_style_context_set_state( self._object,flags )

    def cancel_animations(  self, region_id, ):

        libgtk3.gtk_style_context_cancel_animations.argtypes = [_GtkStyleContext,gpointer]
        
        libgtk3.gtk_style_context_cancel_animations( self._object,region_id )

    def pop_animatable_region(  self, ):

        libgtk3.gtk_style_context_pop_animatable_region.argtypes = [_GtkStyleContext]
        
        libgtk3.gtk_style_context_pop_animatable_region( self._object )

    def invalidate(  self, ):

        libgtk3.gtk_style_context_invalidate.argtypes = [_GtkStyleContext]
        
        libgtk3.gtk_style_context_invalidate( self._object )

    def get_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_style_context_get_color.argtypes = [_GtkStyleContext,GtkStateFlags,_GdkRGBA]
        
        libgtk3.gtk_style_context_get_color( self._object,state,color )

    def set_direction(  self, direction, ):

        libgtk3.gtk_style_context_set_direction.argtypes = [_GtkStyleContext,GtkTextDirection]
        
        libgtk3.gtk_style_context_set_direction( self._object,direction )

    def reset_widgets(  self, screen, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()

        libgtk3.gtk_style_context_reset_widgets.argtypes = [_GtkStyleContext,_GdkScreen]
        
        libgtk3.gtk_style_context_reset_widgets( self._object,screen )

    def get_background_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        libgtk3.gtk_style_context_get_background_color.argtypes = [_GtkStyleContext,GtkStateFlags,_GdkRGBA]
        
        libgtk3.gtk_style_context_get_background_color( self._object,state,color )

    def get_style(  self,*args  ):


        def callit(  *args ):
                libgtk3.gtk_style_context_get_style.restype = None
                libgtk3.gtk_style_context_get_style.argtypes = [ POINTER(c_int)]
                for arg in args:
                     libgtk3.gtk_style_context_get_style.argtypes.append(args[1])
                return libgtk3.gtk_style_context_get_style(  *args)
    
        return callit( self._object,*args )

    def has_region(  self, region_name, flags_return, ):
        if flags_return: flags_return = flags_return._object
        else: flags_return = POINTER(c_int)()

        libgtk3.gtk_style_context_has_region.restype = gboolean
        libgtk3.gtk_style_context_has_region.argtypes = [_GtkStyleContext,c_char_p,_GtkRegionFlags]
        
        return libgtk3.gtk_style_context_has_region( self._object,region_name,flags_return )

    def get_path(  self, ):

        libgtk3.gtk_style_context_get_path.restype = _GtkWidgetPath
        libgtk3.gtk_style_context_get_path.argtypes = [_GtkStyleContext]
        from gtk3 import GtkWidgetPath
        return GtkWidgetPath(None, obj=libgtk3.gtk_style_context_get_path( self._object ) or POINTER(c_int)())

    def notify_state_change(  self, window, region_id, state, state_value, ):
        if window: window = window._object
        else: window = POINTER(c_int)()

        libgtk3.gtk_style_context_notify_state_change.argtypes = [_GtkStyleContext,_GdkWindow,gpointer,GtkStateType,gboolean]
        
        libgtk3.gtk_style_context_notify_state_change( self._object,window,region_id,state,state_value )

    def add_provider_for_screen(  self, screen, provider, priority, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()
        if provider: provider = provider._object
        else: provider = POINTER(c_int)()

        libgtk3.gtk_style_context_add_provider_for_screen.argtypes = [_GtkStyleContext,_GdkScreen,_GtkStyleProvider,guint]
        
        libgtk3.gtk_style_context_add_provider_for_screen( self._object,screen,provider,priority )

    def remove_provider_for_screen(  self, screen, provider, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()
        if provider: provider = provider._object
        else: provider = POINTER(c_int)()

        libgtk3.gtk_style_context_remove_provider_for_screen.argtypes = [_GtkStyleContext,_GdkScreen,_GtkStyleProvider]
        
        libgtk3.gtk_style_context_remove_provider_for_screen( self._object,screen,provider )

    def get_padding(  self, state, padding, ):
        if padding: padding = padding._object
        else: padding = POINTER(c_int)()

        libgtk3.gtk_style_context_get_padding.argtypes = [_GtkStyleContext,GtkStateFlags,_GtkBorder]
        
        libgtk3.gtk_style_context_get_padding( self._object,state,padding )

