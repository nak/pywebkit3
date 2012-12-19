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
from gtk3_enums import *
from webkit3_types import *
from webkit3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GtkLabel = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_cairo_matrix_t = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GClosure = POINTER(c_int)
_GIcon = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_void = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkNumerableIcon = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GObject = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GAppLaunchContext = POINTER(c_int)
_PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
_GScanner = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_GActionGroup = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkEventButton = POINTER(c_int)
_GCancellable = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GFile = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkPrintOperation = POINTER(c_int)
_GtkThemingEngine = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GParameter = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkGradient = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GdkPixbufSimpleAnim = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
"""Enumerations"""
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
GdkCursorType = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GtkIconSize = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
cairo_extend_t = c_int
cairo_filter_t = c_int
CairoPatternype_t = c_int
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
GApplicationFlags = c_int
GtkDialogFlags = c_int
GtkResponseType = c_int

try:
    libwebkit3.webkit_web_back_forward_list_set_limit.restype = None
    libwebkit3.webkit_web_back_forward_list_set_limit.argtypes = [_WebKitWebBackForwardList,gint]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_add_item.restype = None
    libwebkit3.webkit_web_back_forward_list_add_item.argtypes = [_WebKitWebBackForwardList,_WebKitWebHistoryItem]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_back_length.restype = gint
    libwebkit3.webkit_web_back_forward_list_get_back_length.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_go_back.restype = None
    libwebkit3.webkit_web_back_forward_list_go_back.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_back_item.restype = _WebKitWebHistoryItem
    libwebkit3.webkit_web_back_forward_list_get_back_item.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit.restype = _GList
    libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit.argtypes = [_WebKitWebBackForwardList,gint]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_current_item.restype = _WebKitWebHistoryItem
    libwebkit3.webkit_web_back_forward_list_get_current_item.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_go_to_item.restype = None
    libwebkit3.webkit_web_back_forward_list_go_to_item.argtypes = [_WebKitWebBackForwardList,_WebKitWebHistoryItem]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit.restype = _GList
    libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit.argtypes = [_WebKitWebBackForwardList,gint]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_forward_length.restype = gint
    libwebkit3.webkit_web_back_forward_list_get_forward_length.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_forward_item.restype = _WebKitWebHistoryItem
    libwebkit3.webkit_web_back_forward_list_get_forward_item.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_contains_item.restype = gboolean
    libwebkit3.webkit_web_back_forward_list_contains_item.argtypes = [_WebKitWebBackForwardList,_WebKitWebHistoryItem]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_nth_item.restype = _WebKitWebHistoryItem
    libwebkit3.webkit_web_back_forward_list_get_nth_item.argtypes = [_WebKitWebBackForwardList,gint]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_go_forward.restype = None
    libwebkit3.webkit_web_back_forward_list_go_forward.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_clear.restype = None
    libwebkit3.webkit_web_back_forward_list_clear.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_get_limit.restype = gint
    libwebkit3.webkit_web_back_forward_list_get_limit.argtypes = [_WebKitWebBackForwardList]
except:
   pass
try:
    libwebkit3.webkit_web_back_forward_list_new_with_web_view.restype = _WebKitWebBackForwardList
    libwebkit3.webkit_web_back_forward_list_new_with_web_view.argtypes = [_WebKitWebView]
except:
   pass
import gobject__GObject
class WebKitWebBackForwardList( gobject__GObject.GObject):
    """Class WebKitWebBackForwardList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def set_limit(  self, limit, ):

        
        libwebkit3.webkit_web_back_forward_list_set_limit( self._object,limit )

    def add_item(  self, history_item, ):
        if history_item: history_item = history_item._object
        else: history_item = POINTER(c_int)()

        
        libwebkit3.webkit_web_back_forward_list_add_item( self._object,history_item )

    def get_back_length(  self, ):

        
        return libwebkit3.webkit_web_back_forward_list_get_back_length( self._object )

    def go_back(  self, ):

        
        libwebkit3.webkit_web_back_forward_list_go_back( self._object )

    def get_back_item(  self, ):

        from webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem(None, obj=libwebkit3.webkit_web_back_forward_list_get_back_item( self._object ) or POINTER(c_int)() )

    def get_forward_list_with_limit(  self, limit, ):

        from gobject import GList
        return GList( obj=libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit( self._object,limit ) or POINTER(c_int)())

    def get_current_item(  self, ):

        from webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_current_item( self._object ) or POINTER(c_int)() )

    def go_to_item(  self, history_item, ):
        if history_item: history_item = history_item._object
        else: history_item = POINTER(c_int)()

        
        libwebkit3.webkit_web_back_forward_list_go_to_item( self._object,history_item )

    def get_back_list_with_limit(  self, limit, ):

        from gobject import GList
        return GList( obj=libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit( self._object,limit ) or POINTER(c_int)())

    def get_forward_length(  self, ):

        
        return libwebkit3.webkit_web_back_forward_list_get_forward_length( self._object )

    def get_forward_item(  self, ):

        from webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_forward_item( self._object ) or POINTER(c_int)() )

    def contains_item(  self, history_item, ):
        if history_item: history_item = history_item._object
        else: history_item = POINTER(c_int)()

        
        return libwebkit3.webkit_web_back_forward_list_contains_item( self._object,history_item )

    def get_nth_item(  self, index, ):

        from webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_nth_item( self._object,index ) or POINTER(c_int)() )

    def go_forward(  self, ):

        
        libwebkit3.webkit_web_back_forward_list_go_forward( self._object )

    def clear(  self, ):

        
        libwebkit3.webkit_web_back_forward_list_clear( self._object )

    def get_limit(  self, ):

        
        return libwebkit3.webkit_web_back_forward_list_get_limit( self._object )

    @staticmethod
    def new_with_web_view( web_view,):
        if web_view: web_view = web_view._object
        else: web_view = POINTER(c_int)()
        from webkit3 import WebKitWebBackForwardList
        return WebKitWebBackForwardList( obj=    libwebkit3.webkit_web_back_forward_list_new_with_web_view(web_view, )
 or POINTER(c_int)() )
