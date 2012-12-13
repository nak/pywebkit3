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
_WebKitWebPolicyDecision = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkBin = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_PangoEngineShape = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
_GtkMessageDialog = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
_GMainLoop = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
_GtkContainer = POINTER(c_int)
_PangoItem = POINTER(c_int)
__GClosure = POINTER(c_int)
_GtkAboutDialog = POINTER(c_int)
__GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
_GtkScrolledWindow = POINTER(c_int)
_GtkDialog = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GBoxed = POINTER(c_int)
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
_GtkAdjustment = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
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
_GdkGeometry = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GtkContainerClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GtkAdjustment = POINTER(c_int)
_GdkDragContext = POINTER(c_int)
_GtkAssistant = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
__GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
__cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
__GActionGroup = POINTER(c_int)
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
_PangoFontFamily = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
__GCancellable = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_GValue = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GPollFD = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__GFile = POINTER(c_int)
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
__GtkTargetList = POINTER(c_int)
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
_GdkAtom = POINTER(c_int)
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
__GdkDragContext = POINTER(c_int)
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
__PangoFontFace = POINTER(c_int)
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
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkLicense = c_int
GtkIconSize = c_int
GtkAssistantPageType = c_int
GApplicationFlags = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
GtkDestDefaults = c_int
GtkTargetFlags = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
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
GtkMessageType = c_int
GtkButtonsType = c_int
WebKitEditingBehavior = c_int
GdkCursorType = c_int
GdkVisualType = c_int
GdkByteOrder = c_int

import gobject__GObject
class GdkDisplay( gobject__GObject.GObject):
    """Class GdkDisplay Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def flush(  self, ):

        libgtk3.gdk_display_flush.argtypes = [_GdkDisplay]
        
        libgtk3.gdk_display_flush( self._object )

    def get_screen(  self, screen_num, ):

        libgtk3.gdk_display_get_screen.restype = _GdkScreen
        libgtk3.gdk_display_get_screen.argtypes = [_GdkDisplay,gint]
        from gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gdk_display_get_screen( self._object,screen_num ) or POINTER(c_int)())

    def get_default_cursor_size(  self, ):

        libgtk3.gdk_display_get_default_cursor_size.restype = guint
        libgtk3.gdk_display_get_default_cursor_size.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_get_default_cursor_size( self._object )

    def is_closed(  self, ):

        libgtk3.gdk_display_is_closed.restype = gboolean
        libgtk3.gdk_display_is_closed.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_is_closed( self._object )

    def store_clipboard(  self, clipboard_window, time_, targets, n_targets, ):
        if clipboard_window: clipboard_window = clipboard_window._object
        else: clipboard_window = POINTER(c_int)()
        if targets: targets = targets._object
        else: targets = POINTER(c_int)()

        libgtk3.gdk_display_store_clipboard.argtypes = [_GdkDisplay,_GdkWindow,guint32,_GdkAtom,gint]
        
        libgtk3.gdk_display_store_clipboard( self._object,clipboard_window,time_,targets,n_targets )

    def set_double_click_distance(  self, distance, ):

        libgtk3.gdk_display_set_double_click_distance.argtypes = [_GdkDisplay,guint]
        
        libgtk3.gdk_display_set_double_click_distance( self._object,distance )

    def peek_event(  self, ):

        libgtk3.gdk_display_peek_event.restype = POINTER(GdkEvent)
        libgtk3.gdk_display_peek_event.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_peek_event( self._object )

    def get_n_screens(  self, ):

        libgtk3.gdk_display_get_n_screens.restype = gint
        libgtk3.gdk_display_get_n_screens.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_get_n_screens( self._object )

    def close(  self, ):

        libgtk3.gdk_display_close.argtypes = [_GdkDisplay]
        
        libgtk3.gdk_display_close( self._object )

    def get_maximal_cursor_size(  self, width, height, ):

        libgtk3.gdk_display_get_maximal_cursor_size.argtypes = [_GdkDisplay,POINTER(guint),POINTER(guint)]
        
        libgtk3.gdk_display_get_maximal_cursor_size( self._object,width,height )

    def set_double_click_time(  self, msec, ):

        libgtk3.gdk_display_set_double_click_time.argtypes = [_GdkDisplay,guint]
        
        libgtk3.gdk_display_set_double_click_time( self._object,msec )

    def supports_input_shapes(  self, ):

        libgtk3.gdk_display_supports_input_shapes.restype = gboolean
        libgtk3.gdk_display_supports_input_shapes.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_supports_input_shapes( self._object )

    def put_event(  self, event, ):

        libgtk3.gdk_display_put_event.argtypes = [_GdkDisplay,POINTER(GdkEvent)]
        
        libgtk3.gdk_display_put_event( self._object,event )

    def supports_cursor_alpha(  self, ):

        libgtk3.gdk_display_supports_cursor_alpha.restype = gboolean
        libgtk3.gdk_display_supports_cursor_alpha.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_supports_cursor_alpha( self._object )

    def notify_startup_complete(  self, startup_id, ):

        libgtk3.gdk_display_notify_startup_complete.argtypes = [_GdkDisplay,c_char_p]
        
        libgtk3.gdk_display_notify_startup_complete( self._object,startup_id )

    def supports_cursor_color(  self, ):

        libgtk3.gdk_display_supports_cursor_color.restype = gboolean
        libgtk3.gdk_display_supports_cursor_color.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_supports_cursor_color( self._object )

    def list_devices(  self, ):

        libgtk3.gdk_display_list_devices.restype = _GList
        libgtk3.gdk_display_list_devices.argtypes = [_GdkDisplay]
        from gobject import GList
        return GList( obj=libgtk3.gdk_display_list_devices( self._object ) or POINTER(c_int)())

    def has_pending(  self, ):

        libgtk3.gdk_display_has_pending.restype = gboolean
        libgtk3.gdk_display_has_pending.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_has_pending( self._object )

    def beep(  self, ):

        libgtk3.gdk_display_beep.argtypes = [_GdkDisplay]
        
        libgtk3.gdk_display_beep( self._object )

    def get_default_group(  self, ):

        libgtk3.gdk_display_get_default_group.restype = _GdkWindow
        libgtk3.gdk_display_get_default_group.argtypes = [_GdkDisplay]
        from gobject import GdkWindow
        return GdkWindow(None,None, obj=libgtk3.gdk_display_get_default_group( self._object ) or POINTER(c_int)())

    def get_event(  self, ):

        libgtk3.gdk_display_get_event.restype = POINTER(GdkEvent)
        libgtk3.gdk_display_get_event.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_get_event( self._object )

    def supports_shapes(  self, ):

        libgtk3.gdk_display_supports_shapes.restype = gboolean
        libgtk3.gdk_display_supports_shapes.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_supports_shapes( self._object )

    def get_window_at_pointer(  self, win_x, win_y, ):

        libgtk3.gdk_display_get_window_at_pointer.restype = _GdkWindow
        libgtk3.gdk_display_get_window_at_pointer.argtypes = [_GdkDisplay,POINTER(gint),POINTER(gint)]
        from gobject import GdkWindow
        return GdkWindow(None, obj=libgtk3.gdk_display_get_window_at_pointer( self._object,win_x,win_y ) or POINTER(c_int)())

    def supports_composite(  self, ):

        libgtk3.gdk_display_supports_composite.restype = gboolean
        libgtk3.gdk_display_supports_composite.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_supports_composite( self._object )

    def pointer_is_grabbed(  self, ):

        libgtk3.gdk_display_pointer_is_grabbed.restype = gboolean
        libgtk3.gdk_display_pointer_is_grabbed.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_pointer_is_grabbed( self._object )

    def supports_selection_notification(  self, ):

        libgtk3.gdk_display_supports_selection_notification.restype = gboolean
        libgtk3.gdk_display_supports_selection_notification.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_supports_selection_notification( self._object )

    def get_app_launch_context(  self, ):

        libgtk3.gdk_display_get_app_launch_context.restype = _GdkAppLaunchContext
        libgtk3.gdk_display_get_app_launch_context.argtypes = [_GdkDisplay]
        from gobject import GdkAppLaunchContext
        return GdkAppLaunchContext(None, obj=libgtk3.gdk_display_get_app_launch_context( self._object ) or POINTER(c_int)())

    def get_name(  self, ):

        libgtk3.gdk_display_get_name.restype = c_char_p
        libgtk3.gdk_display_get_name.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_get_name( self._object )

    def get_device_manager(  self, ):

        libgtk3.gdk_display_get_device_manager.restype = _GdkDeviceManager
        libgtk3.gdk_display_get_device_manager.argtypes = [_GdkDisplay]
        from gobject import GdkDeviceManager
        return GdkDeviceManager( obj=libgtk3.gdk_display_get_device_manager( self._object ) or POINTER(c_int)())

    def keyboard_ungrab(  self, time_, ):

        libgtk3.gdk_display_keyboard_ungrab.argtypes = [_GdkDisplay,guint32]
        
        libgtk3.gdk_display_keyboard_ungrab( self._object,time_ )

    def get_default_screen(  self, ):

        libgtk3.gdk_display_get_default_screen.restype = _GdkScreen
        libgtk3.gdk_display_get_default_screen.argtypes = [_GdkDisplay]
        from gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gdk_display_get_default_screen( self._object ) or POINTER(c_int)())

    def warp_pointer(  self, screen, x, y, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()

        libgtk3.gdk_display_warp_pointer.argtypes = [_GdkDisplay,_GdkScreen,gint,gint]
        
        libgtk3.gdk_display_warp_pointer( self._object,screen,x,y )

    def pointer_ungrab(  self, time_, ):

        libgtk3.gdk_display_pointer_ungrab.argtypes = [_GdkDisplay,guint32]
        
        libgtk3.gdk_display_pointer_ungrab( self._object,time_ )

    def get_pointer(  self, screen, x, y, mask, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()

        libgtk3.gdk_display_get_pointer.argtypes = [_GdkDisplay,_GdkScreen,POINTER(gint),POINTER(gint),POINTER(GdkModifierType)]
        
        libgtk3.gdk_display_get_pointer( self._object,screen,x,y,mask )

    def device_is_grabbed(  self, device, ):
        if device: device = device._object
        else: device = POINTER(c_int)()

        libgtk3.gdk_display_device_is_grabbed.restype = gboolean
        libgtk3.gdk_display_device_is_grabbed.argtypes = [_GdkDisplay,_GdkDevice]
        
        return libgtk3.gdk_display_device_is_grabbed( self._object,device )

    def supports_clipboard_persistence(  self, ):

        libgtk3.gdk_display_supports_clipboard_persistence.restype = gboolean
        libgtk3.gdk_display_supports_clipboard_persistence.argtypes = [_GdkDisplay]
        
        return libgtk3.gdk_display_supports_clipboard_persistence( self._object )

    def request_selection_notification(  self, selection, ):
        if selection: selection = selection._object
        else: selection = POINTER(c_int)()

        libgtk3.gdk_display_request_selection_notification.restype = gboolean
        libgtk3.gdk_display_request_selection_notification.argtypes = [_GdkDisplay,POINTER(c_int)]
        
        return libgtk3.gdk_display_request_selection_notification( self._object,selection )

    def sync(  self, ):

        libgtk3.gdk_display_sync.argtypes = [_GdkDisplay]
        
        libgtk3.gdk_display_sync( self._object )

    @staticmethod
    def open( display_name,):
        libgtk3.gdk_display_open.restype = _GdkDisplay
        libgtk3.gdk_display_open.argtypes = [c_char_p]
        from gobject import GdkDisplay
        return GdkDisplay( obj=    libgtk3.gdk_display_open(display_name, )
 or POINTER(c_int)())
    @staticmethod
    def get_default():
        libgtk3.gdk_display_get_default.restype = _GdkDisplay
        from gobject import GdkDisplay
        return GdkDisplay( obj=    libgtk3.gdk_display_get_default()
 or POINTER(c_int)())
