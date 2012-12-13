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
_PangoItem = POINTER(c_int)
__GClosure = POINTER(c_int)
__GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GMainContext = POINTER(c_int)
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
_GtkRequisition = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GString = POINTER(c_int)
__PangoContext = POINTER(c_int)
__JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__PangoFont = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__JSClass = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
__GtkSettings = POINTER(c_int)
_GSource = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
__GSource = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
__GMutex = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
__GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
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
__GPollFD = POINTER(c_int)
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
_PangoFontsetSimple = POINTER(c_int)
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
__GString = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GList = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__GTimeVal = POINTER(c_int)
_GtkInvisible = POINTER(c_int)
__GSourceFuncs = POINTER(c_int)
__JSPropertyNameAccumulator = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
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
_WebKitWebNavigationAction = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GIcon = POINTER(c_int)
__GtkWindow = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
__GSourceCallbackFuncs = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GByteArray = POINTER(c_int)
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
WebKitWebNavigationReason = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int

import gobject__GObject
class GdkScreen( gobject__GObject.GObject):
    """Class GdkScreen Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_monitor_at_point(  self, x, y, ):

        libgtk3.gdk_screen_get_monitor_at_point.restype = gint
        libgtk3.gdk_screen_get_monitor_at_point.argtypes = [_GdkScreen,gint,gint]
        
        return libgtk3.gdk_screen_get_monitor_at_point( self._object,x,y )

    def get_toplevel_windows(  self, ):

        libgtk3.gdk_screen_get_toplevel_windows.restype = _GList
        libgtk3.gdk_screen_get_toplevel_windows.argtypes = [_GdkScreen]
        from gobject import GList
        return GList( obj=libgtk3.gdk_screen_get_toplevel_windows( self._object ) or POINTER(c_int)())

    def is_composited(  self, ):

        libgtk3.gdk_screen_is_composited.restype = gboolean
        libgtk3.gdk_screen_is_composited.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_is_composited( self._object )

    def get_number(  self, ):

        libgtk3.gdk_screen_get_number.restype = gint
        libgtk3.gdk_screen_get_number.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_get_number( self._object )

    def get_monitor_height_mm(  self, monitor_num, ):

        libgtk3.gdk_screen_get_monitor_height_mm.restype = gint
        libgtk3.gdk_screen_get_monitor_height_mm.argtypes = [_GdkScreen,gint]
        
        return libgtk3.gdk_screen_get_monitor_height_mm( self._object,monitor_num )

    def get_monitor_workarea(  self, monitor_num, dest, ):
        if dest: dest = dest._object
        else: dest = POINTER(c_int)()

        libgtk3.gdk_screen_get_monitor_workarea.argtypes = [_GdkScreen,gint,_GdkRectangle]
        
        libgtk3.gdk_screen_get_monitor_workarea( self._object,monitor_num,dest )

    def get_resolution(  self, ):

        libgtk3.gdk_screen_get_resolution.restype = gdouble
        libgtk3.gdk_screen_get_resolution.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_get_resolution( self._object )

    def get_n_monitors(  self, ):

        libgtk3.gdk_screen_get_n_monitors.restype = gint
        libgtk3.gdk_screen_get_n_monitors.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_get_n_monitors( self._object )

    def get_setting(  self, name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        libgtk3.gdk_screen_get_setting.restype = gboolean
        libgtk3.gdk_screen_get_setting.argtypes = [_GdkScreen,c_char_p,_GValue]
        
        return libgtk3.gdk_screen_get_setting( self._object,name,value )

    def get_primary_monitor(  self, ):

        libgtk3.gdk_screen_get_primary_monitor.restype = gint
        libgtk3.gdk_screen_get_primary_monitor.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_get_primary_monitor( self._object )

    def set_font_options(  self, options, ):
        if options: options = options._object
        else: options = POINTER(c_int)()

        libgtk3.gdk_screen_set_font_options.argtypes = [_GdkScreen,_cairo_font_options_t]
        
        libgtk3.gdk_screen_set_font_options( self._object,options )

    def get_display(  self, ):

        libgtk3.gdk_screen_get_display.restype = _GdkDisplay
        libgtk3.gdk_screen_get_display.argtypes = [_GdkScreen]
        from gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gdk_screen_get_display( self._object ) or POINTER(c_int)())

    def make_display_name(  self, ):

        libgtk3.gdk_screen_make_display_name.restype = c_char_p
        libgtk3.gdk_screen_make_display_name.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_make_display_name( self._object )

    def get_monitor_at_window(  self, window, ):
        if window: window = window._object
        else: window = POINTER(c_int)()

        libgtk3.gdk_screen_get_monitor_at_window.restype = gint
        libgtk3.gdk_screen_get_monitor_at_window.argtypes = [_GdkScreen,_GdkWindow]
        
        return libgtk3.gdk_screen_get_monitor_at_window( self._object,window )

    def get_width(  self, ):

        libgtk3.gdk_screen_get_width.restype = gint
        libgtk3.gdk_screen_get_width.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_get_width( self._object )

    def list_visuals(  self, ):

        libgtk3.gdk_screen_list_visuals.restype = _GList
        libgtk3.gdk_screen_list_visuals.argtypes = [_GdkScreen]
        from gobject import GList
        return GList( obj=libgtk3.gdk_screen_list_visuals( self._object ) or POINTER(c_int)())

    def get_monitor_plug_name(  self, monitor_num, ):

        libgtk3.gdk_screen_get_monitor_plug_name.restype = c_char_p
        libgtk3.gdk_screen_get_monitor_plug_name.argtypes = [_GdkScreen,gint]
        
        return libgtk3.gdk_screen_get_monitor_plug_name( self._object,monitor_num )

    def get_monitor_geometry(  self, monitor_num, dest, ):
        if dest: dest = dest._object
        else: dest = POINTER(c_int)()

        libgtk3.gdk_screen_get_monitor_geometry.argtypes = [_GdkScreen,gint,_GdkRectangle]
        
        libgtk3.gdk_screen_get_monitor_geometry( self._object,monitor_num,dest )

    def set_resolution(  self, dpi, ):

        libgtk3.gdk_screen_set_resolution.argtypes = [_GdkScreen,gdouble]
        
        libgtk3.gdk_screen_set_resolution( self._object,dpi )

    def get_root_window(  self, ):

        libgtk3.gdk_screen_get_root_window.restype = _GdkWindow
        libgtk3.gdk_screen_get_root_window.argtypes = [_GdkScreen]
        from gobject import GdkWindow
        return GdkWindow(None,None, obj=libgtk3.gdk_screen_get_root_window( self._object ) or POINTER(c_int)())

    def get_height(  self, ):

        libgtk3.gdk_screen_get_height.restype = gint
        libgtk3.gdk_screen_get_height.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_get_height( self._object )

    def get_monitor_width_mm(  self, monitor_num, ):

        libgtk3.gdk_screen_get_monitor_width_mm.restype = gint
        libgtk3.gdk_screen_get_monitor_width_mm.argtypes = [_GdkScreen,gint]
        
        return libgtk3.gdk_screen_get_monitor_width_mm( self._object,monitor_num )

    def get_height_mm(  self, ):

        libgtk3.gdk_screen_get_height_mm.restype = gint
        libgtk3.gdk_screen_get_height_mm.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_get_height_mm( self._object )

    def get_active_window(  self, ):

        libgtk3.gdk_screen_get_active_window.restype = _GdkWindow
        libgtk3.gdk_screen_get_active_window.argtypes = [_GdkScreen]
        from gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gdk_screen_get_active_window( self._object ) or POINTER(c_int)())

    def get_width_mm(  self, ):

        libgtk3.gdk_screen_get_width_mm.restype = gint
        libgtk3.gdk_screen_get_width_mm.argtypes = [_GdkScreen]
        
        return libgtk3.gdk_screen_get_width_mm( self._object )

    def get_window_stack(  self, ):

        libgtk3.gdk_screen_get_window_stack.restype = _GList
        libgtk3.gdk_screen_get_window_stack.argtypes = [_GdkScreen]
        from gobject import GList
        return GList( obj=libgtk3.gdk_screen_get_window_stack( self._object ) or POINTER(c_int)())

    @staticmethod
    def gdk_visual_get_screen( visual,):
        if visual: visual = visual._object
        else: visual = POINTER(c_int)()
        libgtk3.gdk_visual_get_screen.restype = _GdkScreen
        libgtk3.gdk_visual_get_screen.argtypes = [_GdkVisual]
        from gobject import GdkScreen
        return GdkScreen( obj=    libgtk3.gdk_visual_get_screen(visual, )
 or POINTER(c_int)())
    @staticmethod
    def get_default():
        libgtk3.gdk_screen_get_default.restype = _GdkScreen
        from gobject import GdkScreen
        return GdkScreen( obj=    libgtk3.gdk_screen_get_default()
 or POINTER(c_int)())
