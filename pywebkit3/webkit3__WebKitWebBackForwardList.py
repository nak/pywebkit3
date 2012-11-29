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
from webkit3_types import *
    
    
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
class WebKitWebBackForwardList( gobject__GObject.GObject):
    """Class WebKitWebBackForwardList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def set_limit(  self, limit, ):

        libwebkit3.webkit_web_back_forward_list_set_limit.argtypes = [_WebKitWebBackForwardList,gint]
        
        libwebkit3.webkit_web_back_forward_list_set_limit( self._object,limit )

    def add_item(  self, history_item, ):
        if history_item: history_item = history_item._object
        else: history_item = POINTER(c_int)()

        libwebkit3.webkit_web_back_forward_list_add_item.argtypes = [_WebKitWebBackForwardList,_WebKitWebHistoryItem]
        
        libwebkit3.webkit_web_back_forward_list_add_item( self._object,history_item )

    def get_back_length(  self, ):

        libwebkit3.webkit_web_back_forward_list_get_back_length.restype = gint
        libwebkit3.webkit_web_back_forward_list_get_back_length.argtypes = [_WebKitWebBackForwardList]
        
        return libwebkit3.webkit_web_back_forward_list_get_back_length( self._object )

    def go_back(  self, ):

        libwebkit3.webkit_web_back_forward_list_go_back.argtypes = [_WebKitWebBackForwardList]
        
        libwebkit3.webkit_web_back_forward_list_go_back( self._object )

    def get_back_item(  self, ):

        libwebkit3.webkit_web_back_forward_list_get_back_item.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_back_forward_list_get_back_item.argtypes = [_WebKitWebBackForwardList]
        from webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem(None, obj=libwebkit3.webkit_web_back_forward_list_get_back_item( self._object ) or POINTER(c_int)() )

    def get_forward_list_with_limit(  self, limit, ):

        libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit.restype = _GList
        libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit.argtypes = [_WebKitWebBackForwardList,gint]
        from gobject import GList
        return GList( obj=libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit( self._object,limit ) or POINTER(c_int)())

    def get_current_item(  self, ):

        libwebkit3.webkit_web_back_forward_list_get_current_item.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_back_forward_list_get_current_item.argtypes = [_WebKitWebBackForwardList]
        from webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_current_item( self._object ) or POINTER(c_int)() )

    def go_to_item(  self, history_item, ):
        if history_item: history_item = history_item._object
        else: history_item = POINTER(c_int)()

        libwebkit3.webkit_web_back_forward_list_go_to_item.argtypes = [_WebKitWebBackForwardList,_WebKitWebHistoryItem]
        
        libwebkit3.webkit_web_back_forward_list_go_to_item( self._object,history_item )

    def get_back_list_with_limit(  self, limit, ):

        libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit.restype = _GList
        libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit.argtypes = [_WebKitWebBackForwardList,gint]
        from gobject import GList
        return GList( obj=libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit( self._object,limit ) or POINTER(c_int)())

    def get_forward_length(  self, ):

        libwebkit3.webkit_web_back_forward_list_get_forward_length.restype = gint
        libwebkit3.webkit_web_back_forward_list_get_forward_length.argtypes = [_WebKitWebBackForwardList]
        
        return libwebkit3.webkit_web_back_forward_list_get_forward_length( self._object )

    def get_forward_item(  self, ):

        libwebkit3.webkit_web_back_forward_list_get_forward_item.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_back_forward_list_get_forward_item.argtypes = [_WebKitWebBackForwardList]
        from webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_forward_item( self._object ) or POINTER(c_int)() )

    def contains_item(  self, history_item, ):
        if history_item: history_item = history_item._object
        else: history_item = POINTER(c_int)()

        libwebkit3.webkit_web_back_forward_list_contains_item.restype = gboolean
        libwebkit3.webkit_web_back_forward_list_contains_item.argtypes = [_WebKitWebBackForwardList,_WebKitWebHistoryItem]
        
        return libwebkit3.webkit_web_back_forward_list_contains_item( self._object,history_item )

    def get_nth_item(  self, index, ):

        libwebkit3.webkit_web_back_forward_list_get_nth_item.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_back_forward_list_get_nth_item.argtypes = [_WebKitWebBackForwardList,gint]
        from webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_nth_item( self._object,index ) or POINTER(c_int)() )

    def go_forward(  self, ):

        libwebkit3.webkit_web_back_forward_list_go_forward.argtypes = [_WebKitWebBackForwardList]
        
        libwebkit3.webkit_web_back_forward_list_go_forward( self._object )

    def clear(  self, ):

        libwebkit3.webkit_web_back_forward_list_clear.argtypes = [_WebKitWebBackForwardList]
        
        libwebkit3.webkit_web_back_forward_list_clear( self._object )

    def get_limit(  self, ):

        libwebkit3.webkit_web_back_forward_list_get_limit.restype = gint
        libwebkit3.webkit_web_back_forward_list_get_limit.argtypes = [_WebKitWebBackForwardList]
        
        return libwebkit3.webkit_web_back_forward_list_get_limit( self._object )

    @staticmethod
    def new_with_web_view( web_view,):
        if web_view: web_view = web_view._object
        else: web_view = POINTER(c_int)()
        libwebkit3.webkit_web_back_forward_list_new_with_web_view.restype = _WebKitWebBackForwardList
        libwebkit3.webkit_web_back_forward_list_new_with_web_view.argtypes = [_WebKitWebView]
        from webkit3 import WebKitWebBackForwardList
        return WebKitWebBackForwardList( obj=    libwebkit3.webkit_web_back_forward_list_new_with_web_view(web_view, )
 or POINTER(c_int)() )
