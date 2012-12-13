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
_WebKitWebPolicyDecision = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkBin = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_PangoEngineShape = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
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

import gtk3__GtkContainer
class WebKitWebView( gtk3__GtkContainer.GtkContainer):
    """Class WebKitWebView Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libwebkit3.webkit_web_view_new.restype = POINTER(c_int)
            
            libwebkit3.webkit_web_view_new.argtypes = []
            self._object = libwebkit3.webkit_web_view_new()

    """Methods"""
    def zoom_in(  self, ):

        libwebkit3.webkit_web_view_zoom_in.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_zoom_in( self._object )

    def can_copy_clipboard(  self, ):

        libwebkit3.webkit_web_view_can_copy_clipboard.restype = gboolean
        libwebkit3.webkit_web_view_can_copy_clipboard.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_can_copy_clipboard( self._object )

    def get_uri(  self, ):

        libwebkit3.webkit_web_view_get_uri.restype = c_char_p
        libwebkit3.webkit_web_view_get_uri.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_uri( self._object )

    def has_selection(  self, ):

        libwebkit3.webkit_web_view_has_selection.restype = gboolean
        libwebkit3.webkit_web_view_has_selection.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_has_selection( self._object )

    def reload_bypass_cache(  self, ):

        libwebkit3.webkit_web_view_reload_bypass_cache.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_reload_bypass_cache( self._object )

    def load_string(  self, content, mime_type, encoding, base_uri, ):

        libwebkit3.webkit_web_view_load_string.argtypes = [_WebKitWebView,c_char_p,c_char_p,c_char_p,c_char_p]
        
        libwebkit3.webkit_web_view_load_string( self._object,content,mime_type,encoding,base_uri )

    def get_full_content_zoom(  self, ):

        libwebkit3.webkit_web_view_get_full_content_zoom.restype = gboolean
        libwebkit3.webkit_web_view_get_full_content_zoom.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_full_content_zoom( self._object )

    def can_paste_clipboard(  self, ):

        libwebkit3.webkit_web_view_can_paste_clipboard.restype = gboolean
        libwebkit3.webkit_web_view_can_paste_clipboard.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_can_paste_clipboard( self._object )

    def get_encoding(  self, ):

        libwebkit3.webkit_web_view_get_encoding.restype = c_char_p
        libwebkit3.webkit_web_view_get_encoding.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_encoding( self._object )

    def set_custom_encoding(  self, encoding, ):

        libwebkit3.webkit_web_view_set_custom_encoding.argtypes = [_WebKitWebView,c_char_p]
        
        libwebkit3.webkit_web_view_set_custom_encoding( self._object,encoding )

    def set_view_mode(  self, mode, ):

        libwebkit3.webkit_web_view_set_view_mode.argtypes = [_WebKitWebView,WebKitWebViewViewMode]
        
        libwebkit3.webkit_web_view_set_view_mode( self._object,mode )

    def undo(  self, ):

        libwebkit3.webkit_web_view_undo.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_undo( self._object )

    def set_settings(  self, settings, ):
        if settings: settings = settings._object
        else: settings = POINTER(c_int)()

        libwebkit3.webkit_web_view_set_settings.argtypes = [_WebKitWebView,_WebKitWebSettings]
        
        libwebkit3.webkit_web_view_set_settings( self._object,settings )

    def set_highlight_text_matches(  self, highlight, ):

        libwebkit3.webkit_web_view_set_highlight_text_matches.argtypes = [_WebKitWebView,gboolean]
        
        libwebkit3.webkit_web_view_set_highlight_text_matches( self._object,highlight )

    def get_paste_target_list(  self, ):

        libwebkit3.webkit_web_view_get_paste_target_list.restype = _GtkTargetList
        libwebkit3.webkit_web_view_get_paste_target_list.argtypes = [_WebKitWebView]
        from gtk3 import GtkTargetList
        return GtkTargetList( obj=libwebkit3.webkit_web_view_get_paste_target_list( self._object ) or POINTER(c_int)())

    def get_dom_document(  self, ):

        libwebkit3.webkit_web_view_get_dom_document.restype = _WebKitDOMDocument
        libwebkit3.webkit_web_view_get_dom_document.argtypes = [_WebKitWebView]
        from webkit3 import WebKitDOMDocument
        return WebKitDOMDocument( obj=libwebkit3.webkit_web_view_get_dom_document( self._object ) or POINTER(c_int)() )

    def can_cut_clipboard(  self, ):

        libwebkit3.webkit_web_view_can_cut_clipboard.restype = gboolean
        libwebkit3.webkit_web_view_can_cut_clipboard.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_can_cut_clipboard( self._object )

    def reload(  self, ):

        libwebkit3.webkit_web_view_reload.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_reload( self._object )

    def set_transparent(  self, flag, ):

        libwebkit3.webkit_web_view_set_transparent.argtypes = [_WebKitWebView,gboolean]
        
        libwebkit3.webkit_web_view_set_transparent( self._object,flag )

    def unmark_text_matches(  self, ):

        libwebkit3.webkit_web_view_unmark_text_matches.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_unmark_text_matches( self._object )

    def get_view_source_mode(  self, ):

        libwebkit3.webkit_web_view_get_view_source_mode.restype = gboolean
        libwebkit3.webkit_web_view_get_view_source_mode.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_view_source_mode( self._object )

    def go_back_or_forward(  self, steps, ):

        libwebkit3.webkit_web_view_go_back_or_forward.argtypes = [_WebKitWebView,gint]
        
        libwebkit3.webkit_web_view_go_back_or_forward( self._object,steps )

    def copy_clipboard(  self, ):

        libwebkit3.webkit_web_view_copy_clipboard.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_copy_clipboard( self._object )

    def get_zoom_level(  self, ):

        libwebkit3.webkit_web_view_get_zoom_level.restype = gfloat
        libwebkit3.webkit_web_view_get_zoom_level.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_zoom_level( self._object )

    def get_load_status(  self, ):

        libwebkit3.webkit_web_view_get_load_status.restype = WebKitLoadStatus
        libwebkit3.webkit_web_view_get_load_status.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_load_status( self._object )

    def get_icon_uri(  self, ):

        libwebkit3.webkit_web_view_get_icon_uri.restype = c_char_p
        libwebkit3.webkit_web_view_get_icon_uri.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_icon_uri( self._object )

    def set_editable(  self, flag, ):

        libwebkit3.webkit_web_view_set_editable.argtypes = [_WebKitWebView,gboolean]
        
        libwebkit3.webkit_web_view_set_editable( self._object,flag )

    def move_cursor(  self, step, count, ):
        if step: step = step._object
        else: step = POINTER(c_int)()

        libwebkit3.webkit_web_view_move_cursor.argtypes = [_WebKitWebView,GtkMovementStep,gint]
        
        libwebkit3.webkit_web_view_move_cursor( self._object,step,count )

    def load_html_string(  self, content, base_uri, ):

        libwebkit3.webkit_web_view_load_html_string.argtypes = [_WebKitWebView,c_char_p,c_char_p]
        
        libwebkit3.webkit_web_view_load_html_string( self._object,content,base_uri )

    def paste_clipboard(  self, ):

        libwebkit3.webkit_web_view_paste_clipboard.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_paste_clipboard( self._object )

    def get_title(  self, ):

        libwebkit3.webkit_web_view_get_title.restype = c_char_p
        libwebkit3.webkit_web_view_get_title.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_title( self._object )

    def go_back(  self, ):

        libwebkit3.webkit_web_view_go_back.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_go_back( self._object )

    def redo(  self, ):

        libwebkit3.webkit_web_view_redo.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_redo( self._object )

    def go_forward(  self, ):

        libwebkit3.webkit_web_view_go_forward.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_go_forward( self._object )

    def set_maintains_back_forward_list(  self, flag, ):

        libwebkit3.webkit_web_view_set_maintains_back_forward_list.argtypes = [_WebKitWebView,gboolean]
        
        libwebkit3.webkit_web_view_set_maintains_back_forward_list( self._object,flag )

    def get_focused_frame(  self, ):

        libwebkit3.webkit_web_view_get_focused_frame.restype = _WebKitWebFrame
        libwebkit3.webkit_web_view_get_focused_frame.argtypes = [_WebKitWebView]
        from webkit3 import WebKitWebFrame
        return WebKitWebFrame(None,None, obj=libwebkit3.webkit_web_view_get_focused_frame( self._object ) or POINTER(c_int)() )

    def can_show_mime_type(  self, mime_type, ):

        libwebkit3.webkit_web_view_can_show_mime_type.restype = gboolean
        libwebkit3.webkit_web_view_can_show_mime_type.argtypes = [_WebKitWebView,c_char_p]
        
        return libwebkit3.webkit_web_view_can_show_mime_type( self._object,mime_type )

    def get_window_features(  self, ):

        libwebkit3.webkit_web_view_get_window_features.restype = _WebKitWebWindowFeatures
        libwebkit3.webkit_web_view_get_window_features.argtypes = [_WebKitWebView]
        from webkit3 import WebKitWebWindowFeatures
        return WebKitWebWindowFeatures(None, obj=libwebkit3.webkit_web_view_get_window_features( self._object ) or POINTER(c_int)() )

    def get_back_forward_list(  self, ):

        libwebkit3.webkit_web_view_get_back_forward_list.restype = _WebKitWebBackForwardList
        libwebkit3.webkit_web_view_get_back_forward_list.argtypes = [_WebKitWebView]
        from webkit3 import WebKitWebBackForwardList
        return WebKitWebBackForwardList( obj=libwebkit3.webkit_web_view_get_back_forward_list( self._object ) or POINTER(c_int)() )

    def can_go_forward(  self, ):

        libwebkit3.webkit_web_view_can_go_forward.restype = gboolean
        libwebkit3.webkit_web_view_can_go_forward.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_can_go_forward( self._object )

    def get_settings(  self, ):

        libwebkit3.webkit_web_view_get_settings.restype = _WebKitWebSettings
        libwebkit3.webkit_web_view_get_settings.argtypes = [_WebKitWebView]
        from webkit3 import WebKitWebSettings
        return WebKitWebSettings(None, obj=libwebkit3.webkit_web_view_get_settings( self._object ) or POINTER(c_int)() )

    def execute_script(  self, script, ):
        
        libwebkit3.webkit_web_view_execute_script.restype = None
        libwebkit3.webkit_web_view_execute_script.argtypes = [_WebKitWebView,c_char_p]
        return libwebkit3.webkit_web_view_execute_script( self._object,c_char_p(script ))
      
    def cut_clipboard(  self, ):

        libwebkit3.webkit_web_view_cut_clipboard.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_cut_clipboard( self._object )

    def get_inspector(  self, ):

        libwebkit3.webkit_web_view_get_inspector.restype = _WebKitWebInspector
        libwebkit3.webkit_web_view_get_inspector.argtypes = [_WebKitWebView]
        from webkit3 import WebKitWebInspector
        return WebKitWebInspector( obj=libwebkit3.webkit_web_view_get_inspector( self._object ) or POINTER(c_int)() )

    def get_transparent(  self, ):

        libwebkit3.webkit_web_view_get_transparent.restype = gboolean
        libwebkit3.webkit_web_view_get_transparent.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_transparent( self._object )

    def get_custom_encoding(  self, ):

        libwebkit3.webkit_web_view_get_custom_encoding.restype = c_char_p
        libwebkit3.webkit_web_view_get_custom_encoding.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_custom_encoding( self._object )

    def get_icon_pixbuf(  self, ):

        libwebkit3.webkit_web_view_get_icon_pixbuf.restype = _GdkPixbuf
        libwebkit3.webkit_web_view_get_icon_pixbuf.argtypes = [_WebKitWebView]
        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libwebkit3.webkit_web_view_get_icon_pixbuf( self._object ) or POINTER(c_int)())

    def can_undo(  self, ):

        libwebkit3.webkit_web_view_can_undo.restype = gboolean
        libwebkit3.webkit_web_view_can_undo.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_can_undo( self._object )

    def get_view_mode(  self, ):

        libwebkit3.webkit_web_view_get_view_mode.restype = WebKitWebViewViewMode
        libwebkit3.webkit_web_view_get_view_mode.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_view_mode( self._object )

    def set_zoom_level(  self, zoom_level, ):

        libwebkit3.webkit_web_view_set_zoom_level.argtypes = [_WebKitWebView,gfloat]
        
        libwebkit3.webkit_web_view_set_zoom_level( self._object,zoom_level )

    def search_text(  self, text, case_sensitive, forward, wrap, ):

        libwebkit3.webkit_web_view_search_text.restype = gboolean
        libwebkit3.webkit_web_view_search_text.argtypes = [_WebKitWebView,c_char_p,gboolean,gboolean,gboolean]
        
        return libwebkit3.webkit_web_view_search_text( self._object,text,case_sensitive,forward,wrap )

    def load_uri(  self, uri, ):

        libwebkit3.webkit_web_view_load_uri.argtypes = [_WebKitWebView,c_char_p]
        
        libwebkit3.webkit_web_view_load_uri( self._object,uri )

    def get_editable(  self, ):

        libwebkit3.webkit_web_view_get_editable.restype = gboolean
        libwebkit3.webkit_web_view_get_editable.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_editable( self._object )

    def get_main_frame(  self, ):
        #workaround since it appears calling get_main_frame twice on
        #same webview casesu SIGSEGV(!)????
        if hasattr(self,'_main_frame'):
            return self._main_frame
        libwebkit3.webkit_web_view_get_main_frame.restype = _WebKitWebFrame
        libwebkit3.webkit_web_view_get_main_frame.argtypes = [_WebKitWebView]
        from webkit3 import WebKitWebFrame
        self._main_frame =  WebKitWebFrame(None, obj=libwebkit3.webkit_web_view_get_main_frame( self._object ) or POINTER(c_int)() )
        return self._main_frame

    def get_progress(  self, ):

        libwebkit3.webkit_web_view_get_progress.restype = gdouble
        libwebkit3.webkit_web_view_get_progress.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_get_progress( self._object )

    def open(  self, uri, ):

        libwebkit3.webkit_web_view_open.argtypes = [_WebKitWebView,c_char_p]
        
        libwebkit3.webkit_web_view_open( self._object,uri )

    def set_full_content_zoom(  self, full_content_zoom, ):

        libwebkit3.webkit_web_view_set_full_content_zoom.argtypes = [_WebKitWebView,gboolean]
        
        libwebkit3.webkit_web_view_set_full_content_zoom( self._object,full_content_zoom )

    def delete_selection(  self, ):

        libwebkit3.webkit_web_view_delete_selection.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_delete_selection( self._object )

    def select_all(  self, ):

        libwebkit3.webkit_web_view_select_all.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_select_all( self._object )

    def try_get_favicon_pixbuf(  self, width, height, ):

        libwebkit3.webkit_web_view_try_get_favicon_pixbuf.restype = _GdkPixbuf
        libwebkit3.webkit_web_view_try_get_favicon_pixbuf.argtypes = [_WebKitWebView,guint,guint]
        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libwebkit3.webkit_web_view_try_get_favicon_pixbuf( self._object,width,height ) or POINTER(c_int)())

    def get_hit_test_result(  self, event, ):
        if event: event = event._object
        else: event = POINTER(c_int)()

        libwebkit3.webkit_web_view_get_hit_test_result.restype = _WebKitHitTestResult
        libwebkit3.webkit_web_view_get_hit_test_result.argtypes = [_WebKitWebView,_GdkEventButton]
        from webkit3 import WebKitHitTestResult
        return WebKitHitTestResult( obj=libwebkit3.webkit_web_view_get_hit_test_result( self._object,event ) or POINTER(c_int)() )

    def mark_text_matches(  self, string, case_sensitive, limit, ):

        libwebkit3.webkit_web_view_mark_text_matches.restype = guint
        libwebkit3.webkit_web_view_mark_text_matches.argtypes = [_WebKitWebView,c_char_p,gboolean,guint]
        
        return libwebkit3.webkit_web_view_mark_text_matches( self._object,string,case_sensitive,limit )

    def zoom_out(  self, ):

        libwebkit3.webkit_web_view_zoom_out.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_zoom_out( self._object )

    def can_redo(  self, ):

        libwebkit3.webkit_web_view_can_redo.restype = gboolean
        libwebkit3.webkit_web_view_can_redo.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_can_redo( self._object )

    def load_request(  self, request, ):
        if request: request = request._object
        else: request = POINTER(c_int)()

        libwebkit3.webkit_web_view_load_request.argtypes = [_WebKitWebView,_WebKitNetworkRequest]
        
        libwebkit3.webkit_web_view_load_request( self._object,request )

    def stop_loading(  self, ):

        libwebkit3.webkit_web_view_stop_loading.argtypes = [_WebKitWebView]
        
        libwebkit3.webkit_web_view_stop_loading( self._object )

    def get_copy_target_list(  self, ):

        libwebkit3.webkit_web_view_get_copy_target_list.restype = _GtkTargetList
        libwebkit3.webkit_web_view_get_copy_target_list.argtypes = [_WebKitWebView]
        from gtk3 import GtkTargetList
        return GtkTargetList( obj=libwebkit3.webkit_web_view_get_copy_target_list( self._object ) or POINTER(c_int)())

    def get_viewport_attributes(  self, ):

        libwebkit3.webkit_web_view_get_viewport_attributes.restype = _WebKitViewportAttributes
        libwebkit3.webkit_web_view_get_viewport_attributes.argtypes = [_WebKitWebView]
        from webkit3 import WebKitViewportAttributes
        return WebKitViewportAttributes( obj=libwebkit3.webkit_web_view_get_viewport_attributes( self._object ) or POINTER(c_int)() )

    def can_go_back_or_forward(  self, steps, ):

        libwebkit3.webkit_web_view_can_go_back_or_forward.restype = gboolean
        libwebkit3.webkit_web_view_can_go_back_or_forward.argtypes = [_WebKitWebView,gint]
        
        return libwebkit3.webkit_web_view_can_go_back_or_forward( self._object,steps )

    def go_to_back_forward_item(  self, item, ):
        if item: item = item._object
        else: item = POINTER(c_int)()

        libwebkit3.webkit_web_view_go_to_back_forward_item.restype = gboolean
        libwebkit3.webkit_web_view_go_to_back_forward_item.argtypes = [_WebKitWebView,_WebKitWebHistoryItem]
        
        return libwebkit3.webkit_web_view_go_to_back_forward_item( self._object,item )

    def set_view_source_mode(  self, view_source_mode, ):

        libwebkit3.webkit_web_view_set_view_source_mode.argtypes = [_WebKitWebView,gboolean]
        
        libwebkit3.webkit_web_view_set_view_source_mode( self._object,view_source_mode )

    def can_go_back(  self, ):

        libwebkit3.webkit_web_view_can_go_back.restype = gboolean
        libwebkit3.webkit_web_view_can_go_back.argtypes = [_WebKitWebView]
        
        return libwebkit3.webkit_web_view_can_go_back( self._object )

    def get_javascript_global_context(  self, ):

        libwebkit3.webkit_web_view_get_javascript_global_context.restype = _JSContext
        libwebkit3.webkit_web_view_get_javascript_global_context.argtypes = [_WebKitWebView]
        from javascriptcore import JSContext
        return JSContext( obj=libwebkit3.webkit_web_view_get_javascript_global_context( self._object )  or POINTER(c_int)())

    ##add-ons/overrides
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libwebkit3.webkit_web_view_new.restype = POINTER(c_int)
            
            libwebkit3.webkit_web_view_new.argtypes = []
            self._object = libwebkit3.webkit_web_view_new()
        from javascript import ScriptEnv
        self._env = ScriptEnv(self)
        
    def get_context(self):
        return self.get_main_frame().get_global_context()
    
    def get_env(self):
        return self._env
    
    def get_execution_env(self):
        return self._env.execution()
    
    def on_resource_load_finished(self, func, *args ):
        from gobject import GObject
        def WebView_C_Callable( _webview, _webframe, _webresource, data):
            from .webkit3__WebKitWebFrame import WebKitWebFrame
            from .webkit3__WebKitWebResource import WebKitWebResource
            func( self, self.get_main_frame(), WebKitWebResource(None, obj=_webresource), *args)#WebKitWebFrame(None,obj=_webframe), WebKitWebResource(None,obj=_webresource), *args)
            return None
        CFUNC = CFUNCTYPE(None, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int))
        GObject.connect( self, 'resource-load-finished', func, *args, cfunc = (CFUNC(WebView_C_Callable),CFUNC))
        
    def on_view_ready(self, func, *args):
        from gobject import GObject
        GObject.connect( self, 'load-finished', func, *args)

        