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

import gobject__GObject
class GdkDevice( gobject__GObject.GObject):
    """Class GdkDevice Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def set_mode(  self, mode, ):

        libgtk3.gdk_device_set_mode.restype = gboolean
        libgtk3.gdk_device_set_mode.argtypes = [_GdkDevice,GdkInputMode]
        
        return libgtk3.gdk_device_set_mode( self._object,mode )

    def get_has_cursor(  self, ):

        libgtk3.gdk_device_get_has_cursor.restype = gboolean
        libgtk3.gdk_device_get_has_cursor.argtypes = [_GdkDevice]
        
        return libgtk3.gdk_device_get_has_cursor( self._object )

    def get_n_axes(  self, ):

        libgtk3.gdk_device_get_n_axes.restype = gint
        libgtk3.gdk_device_get_n_axes.argtypes = [_GdkDevice]
        
        return libgtk3.gdk_device_get_n_axes( self._object )

    def get_source(  self, ):

        libgtk3.gdk_device_get_source.restype = GdkInputSource
        libgtk3.gdk_device_get_source.argtypes = [_GdkDevice]
        
        return libgtk3.gdk_device_get_source( self._object )

    def get_history(  self, window, start, stop, events, n_events, ):
        if window: window = window._object
        else: window = POINTER(c_int)()
        if events: events = events._object
        else: events = POINTER(c_int)()

        libgtk3.gdk_device_get_history.restype = gboolean
        libgtk3.gdk_device_get_history.argtypes = [_GdkDevice,_GdkWindow,guint32,guint32,POINTER(_GdkTimeCoord),POINTER(gint)]
        
        return libgtk3.gdk_device_get_history( self._object,window,start,stop,events,n_events )

    def get_mode(  self, ):

        libgtk3.gdk_device_get_mode.restype = GdkInputMode
        libgtk3.gdk_device_get_mode.argtypes = [_GdkDevice]
        
        return libgtk3.gdk_device_get_mode( self._object )

    def get_window_at_position(  self, win_x, win_y, ):

        libgtk3.gdk_device_get_window_at_position.restype = _GdkWindow
        libgtk3.gdk_device_get_window_at_position.argtypes = [_GdkDevice,POINTER(gint),POINTER(gint)]
        from gobject import GdkWindow
        return GdkWindow(None,None, obj=libgtk3.gdk_device_get_window_at_position( self._object,win_x,win_y ) or POINTER(c_int)())

    def get_device_type(  self, ):

        libgtk3.gdk_device_get_device_type.restype = GdkDeviceType
        libgtk3.gdk_device_get_device_type.argtypes = [_GdkDevice]
        
        return libgtk3.gdk_device_get_device_type( self._object )

    def get_axis_value(  self, axes, axis_label, value, ):
        if axis_label: axis_label = axis_label._object
        else: axis_label = POINTER(c_int)()

        libgtk3.gdk_device_get_axis_value.restype = gboolean
        libgtk3.gdk_device_get_axis_value.argtypes = [_GdkDevice,POINTER(gdouble),POINTER(c_int),POINTER(gdouble)]
        
        return libgtk3.gdk_device_get_axis_value( self._object,axes,axis_label,value )

    def set_key(  self, index_, keyval, modifiers, ):

        libgtk3.gdk_device_set_key.argtypes = [_GdkDevice,guint,guint,GdkModifierType]
        
        libgtk3.gdk_device_set_key( self._object,index_,keyval,modifiers )

    def ungrab(  self, time_, ):

        libgtk3.gdk_device_ungrab.argtypes = [_GdkDevice,guint32]
        
        libgtk3.gdk_device_ungrab( self._object,time_ )

    def list_axes(  self, ):

        libgtk3.gdk_device_list_axes.restype = _GList
        libgtk3.gdk_device_list_axes.argtypes = [_GdkDevice]
        from gobject import GList
        return GList( obj=libgtk3.gdk_device_list_axes( self._object ) or POINTER(c_int)())

    def set_axis_use(  self, index_, use, ):

        libgtk3.gdk_device_set_axis_use.argtypes = [_GdkDevice,guint,GdkAxisUse]
        
        libgtk3.gdk_device_set_axis_use( self._object,index_,use )

    def get_n_keys(  self, ):

        libgtk3.gdk_device_get_n_keys.restype = gint
        libgtk3.gdk_device_get_n_keys.argtypes = [_GdkDevice]
        
        return libgtk3.gdk_device_get_n_keys( self._object )

    def warp(  self, screen, x, y, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()

        libgtk3.gdk_device_warp.argtypes = [_GdkDevice,_GdkScreen,gint,gint]
        
        libgtk3.gdk_device_warp( self._object,screen,x,y )

    def get_display(  self, ):

        libgtk3.gdk_device_get_display.restype = _GdkDisplay
        libgtk3.gdk_device_get_display.argtypes = [_GdkDevice]
        from gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gdk_device_get_display( self._object ) or POINTER(c_int)())

    def free_history(  self, events, n_events, ):
        if events: events = events._object
        else: events = POINTER(c_int)()

        libgtk3.gdk_device_free_history.argtypes = [_GdkDevice,_GdkTimeCoord,gint]
        
        libgtk3.gdk_device_free_history( self._object,events,n_events )

    def get_associated_device(  self, ):

        libgtk3.gdk_device_get_associated_device.restype = _GdkDevice
        libgtk3.gdk_device_get_associated_device.argtypes = [_GdkDevice]
        from gobject import GdkDevice
        return GdkDevice( obj=libgtk3.gdk_device_get_associated_device( self._object ) or POINTER(c_int)())

    def get_name(  self, ):

        libgtk3.gdk_device_get_name.restype = c_char_p
        libgtk3.gdk_device_get_name.argtypes = [_GdkDevice]
        
        return libgtk3.gdk_device_get_name( self._object )

    def get_key(  self, index_, keyval, modifiers, ):

        libgtk3.gdk_device_get_key.restype = gboolean
        libgtk3.gdk_device_get_key.argtypes = [_GdkDevice,guint,POINTER(guint),POINTER(GdkModifierType)]
        
        return libgtk3.gdk_device_get_key( self._object,index_,keyval,modifiers )

    def get_position(  self, screen, x, y, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()

        libgtk3.gdk_device_get_position.argtypes = [_GdkDevice,_GdkScreen,POINTER(gint),POINTER(gint)]
        
        libgtk3.gdk_device_get_position( self._object,screen,x,y )

    def get_axis_use(  self, index_, ):

        libgtk3.gdk_device_get_axis_use.restype = GdkAxisUse
        libgtk3.gdk_device_get_axis_use.argtypes = [_GdkDevice,guint]
        
        return libgtk3.gdk_device_get_axis_use( self._object,index_ )

    def get_axis(  self, axes, use, value, ):

        libgtk3.gdk_device_get_axis.restype = gboolean
        libgtk3.gdk_device_get_axis.argtypes = [_GdkDevice,POINTER(gdouble),GdkAxisUse,POINTER(gdouble)]
        
        return libgtk3.gdk_device_get_axis( self._object,axes,use,value )

    def grab(  self, window, grab_ownership, owner_events, event_mask, cursor, time_, ):
        if window: window = window._object
        else: window = POINTER(c_int)()
        if cursor: cursor = cursor._object
        else: cursor = POINTER(c_int)()

        libgtk3.gdk_device_grab.restype = GdkGrabStatus
        libgtk3.gdk_device_grab.argtypes = [_GdkDevice,_GdkWindow,GdkGrabOwnership,gboolean,GdkEventMask,_GdkCursor,guint32]
        
        return libgtk3.gdk_device_grab( self._object,window,grab_ownership,owner_events,event_mask,cursor,time_ )

    def list_slave_devices(  self, ):

        libgtk3.gdk_device_list_slave_devices.restype = _GList
        libgtk3.gdk_device_list_slave_devices.argtypes = [_GdkDevice]
        from gobject import GList
        return GList( obj=libgtk3.gdk_device_list_slave_devices( self._object ) or POINTER(c_int)())

    def get_state(  self, window, axes, mask, ):
        if window: window = window._object
        else: window = POINTER(c_int)()

        libgtk3.gdk_device_get_state.argtypes = [_GdkDevice,_GdkWindow,POINTER(gdouble),POINTER(GdkModifierType)]
        
        libgtk3.gdk_device_get_state( self._object,window,axes,mask )

