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
_WebKitWebWindowFeatures = POINTER(c_int)
_void = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GtkTextBuffer = POINTER(c_int)
_GtkNumerableIcon = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GObject = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
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
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkVisual = POINTER(c_int)
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
_WebKitWebDataSource = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
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

try:
    libwebkit3.webkit_web_frame_load_request.restype = None
    libwebkit3.webkit_web_frame_load_request.argtypes = [_WebKitWebFrame,_WebKitNetworkRequest]
except:
   pass
try:
    libwebkit3.webkit_web_frame_load_alternate_string.restype = None
    libwebkit3.webkit_web_frame_load_alternate_string.argtypes = [_WebKitWebFrame,c_char_p,c_char_p,c_char_p]
except:
   pass
try:
    libwebkit3.webkit_web_frame_find_frame.restype = _WebKitWebFrame
    libwebkit3.webkit_web_frame_find_frame.argtypes = [_WebKitWebFrame,c_char_p]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_uri.restype = c_char_p
    libwebkit3.webkit_web_frame_get_uri.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_data_source.restype = _WebKitWebDataSource
    libwebkit3.webkit_web_frame_get_data_source.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_stop_loading.restype = None
    libwebkit3.webkit_web_frame_stop_loading.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_web_view.restype = _WebKitWebView
    libwebkit3.webkit_web_frame_get_web_view.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_horizontal_scrollbar_policy.restype = GtkPolicyType
    libwebkit3.webkit_web_frame_get_horizontal_scrollbar_policy.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_security_origin.restype = _WebKitSecurityOrigin
    libwebkit3.webkit_web_frame_get_security_origin.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_parent.restype = _WebKitWebFrame
    libwebkit3.webkit_web_frame_get_parent.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_network_response.restype = _WebKitNetworkResponse
    libwebkit3.webkit_web_frame_get_network_response.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_print.restype = None
    libwebkit3.webkit_web_frame_print.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_provisional_data_source.restype = _WebKitWebDataSource
    libwebkit3.webkit_web_frame_get_provisional_data_source.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_name.restype = c_char_p
    libwebkit3.webkit_web_frame_get_name.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_load_string.restype = None
    libwebkit3.webkit_web_frame_load_string.argtypes = [_WebKitWebFrame,c_char_p,c_char_p,c_char_p,c_char_p]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_dom_document.restype = _WebKitDOMDocument
    libwebkit3.webkit_web_frame_get_dom_document.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_reload.restype = None
    libwebkit3.webkit_web_frame_reload.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_global_context.restype = _JSGlobalContext
    libwebkit3.webkit_web_frame_get_global_context.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_vertical_scrollbar_policy.restype = GtkPolicyType
    libwebkit3.webkit_web_frame_get_vertical_scrollbar_policy.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_print_full.restype = GtkPrintOperationResult
    libwebkit3.webkit_web_frame_print_full.argtypes = [_WebKitWebFrame,_GtkPrintOperation,GtkPrintOperationAction,_GError]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_load_status.restype = WebKitLoadStatus
    libwebkit3.webkit_web_frame_get_load_status.argtypes = [_WebKitWebFrame]
except:
   pass
try:
    libwebkit3.webkit_web_frame_load_uri.restype = None
    libwebkit3.webkit_web_frame_load_uri.argtypes = [_WebKitWebFrame,c_char_p]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_title.restype = c_char_p
    libwebkit3.webkit_web_frame_get_title.argtypes = [_WebKitWebFrame]
except:
   pass
import gobject__GObject
class WebKitWebFrame( gobject__GObject.GObject):
    """Class WebKitWebFrame Constructors"""
    def __init__( self, web_view,  obj = None):
        if obj: self._object = obj
        else:
            libwebkit3.webkit_web_frame_new.restype = POINTER(c_int)
            
            if web_view : web_view = web_view._object
            else :  web_view = POINTER(c_int)()

            libwebkit3.webkit_web_frame_new.argtypes = [_WebKitWebView]
            self._object = libwebkit3.webkit_web_frame_new(web_view, )

    """Methods"""
    def load_request(  self, request, ):
        if request: request = request._object
        else: request = POINTER(c_int)()

        
        libwebkit3.webkit_web_frame_load_request( self._object,request )

    def load_alternate_string(  self, content, base_url, unreachable_url, ):

        
        libwebkit3.webkit_web_frame_load_alternate_string( self._object,content,base_url,unreachable_url )

    def find_frame(  self, name, ):

        from webkit3 import WebKitWebFrame
        return WebKitWebFrame(None, obj=libwebkit3.webkit_web_frame_find_frame( self._object,name ) or POINTER(c_int)() )

    def get_uri(  self, ):

        
        return libwebkit3.webkit_web_frame_get_uri( self._object )

    def get_data_source(  self, ):

        from webkit3 import WebKitWebDataSource
        return WebKitWebDataSource( obj=libwebkit3.webkit_web_frame_get_data_source( self._object ) or POINTER(c_int)() )

    def stop_loading(  self, ):

        
        libwebkit3.webkit_web_frame_stop_loading( self._object )

    def get_web_view(  self, ):

        from webkit3 import WebKitWebView
        return WebKitWebView(None, obj=libwebkit3.webkit_web_frame_get_web_view( self._object ) or POINTER(c_int)() )

    def get_horizontal_scrollbar_policy(  self, ):

        
        return libwebkit3.webkit_web_frame_get_horizontal_scrollbar_policy( self._object )

    def get_security_origin(  self, ):

        from webkit3 import WebKitSecurityOrigin
        return WebKitSecurityOrigin( obj=libwebkit3.webkit_web_frame_get_security_origin( self._object ) or POINTER(c_int)() )

    def get_parent(  self, ):

        from webkit3 import WebKitWebFrame
        return WebKitWebFrame( obj=libwebkit3.webkit_web_frame_get_parent( self._object ) or POINTER(c_int)() )

    def get_network_response(  self, ):

        from webkit3 import WebKitNetworkResponse
        return WebKitNetworkResponse( obj=libwebkit3.webkit_web_frame_get_network_response( self._object ) or POINTER(c_int)() )

    def py_print(  self, ):

        
        libwebkit3.webkit_web_frame_print( self._object )

    def get_provisional_data_source(  self, ):

        from webkit3 import WebKitWebDataSource
        return WebKitWebDataSource( obj=libwebkit3.webkit_web_frame_get_provisional_data_source( self._object ) or POINTER(c_int)() )

    def get_name(  self, ):

        
        return libwebkit3.webkit_web_frame_get_name( self._object )

    def load_string(  self, content, mime_type, encoding, base_uri, ):

        
        libwebkit3.webkit_web_frame_load_string( self._object,content,mime_type,encoding,base_uri )

    def get_dom_document(  self, ):

        from webkit3 import WebKitDOMDocument
        return WebKitDOMDocument( obj=libwebkit3.webkit_web_frame_get_dom_document( self._object ) or POINTER(c_int)() )

    def reload(  self, ):

        
        libwebkit3.webkit_web_frame_reload( self._object )

    def get_global_context(  self, ):

        from javascriptcore import JSGlobalContext
        return JSGlobalContext( obj=libwebkit3.webkit_web_frame_get_global_context( self._object )  or POINTER(c_int)())

    def get_vertical_scrollbar_policy(  self, ):

        
        return libwebkit3.webkit_web_frame_get_vertical_scrollbar_policy( self._object )

    def print_full(  self, operation, action, error, ):
        if operation: operation = operation._object
        else: operation = POINTER(c_int)()
        if action: action = action._object
        else: action = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libwebkit3.webkit_web_frame_print_full( self._object,operation,action,error )

    def get_load_status(  self, ):

        
        return libwebkit3.webkit_web_frame_get_load_status( self._object )

    def load_uri(  self, uri, ):

        
        libwebkit3.webkit_web_frame_load_uri( self._object,uri )

    def get_title(  self, ):

        
        return libwebkit3.webkit_web_frame_get_title( self._object )

