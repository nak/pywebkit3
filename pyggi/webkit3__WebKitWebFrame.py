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
from .gtk3_types import *
from .gtk3_enums import *
from .webkit3_types import *
from .webkit3_enums import *

OPAQUE_PTR = POINTER(c_void_p)
NULL = OPAQUE_PTR()

"""Derived Pointer Types"""
_GtkRcStyle = OPAQUE_PTR
_GdkGeometry = OPAQUE_PTR
_WebKitNetworkResponse = OPAQUE_PTR
_GdkPixbuf = OPAQUE_PTR
_GtkRequisition = OPAQUE_PTR
_GtkRcStyle = OPAQUE_PTR
_GtkRegionFlags = OPAQUE_PTR
_cairo_matrix_t = OPAQUE_PTR
_GtkWindow = OPAQUE_PTR
_cairo_font_options_t = OPAQUE_PTR
_GtkIconFactory = OPAQUE_PTR
_GdkAtom = OPAQUE_PTR
_GdkTimeCoord = OPAQUE_PTR
_GdkColor = OPAQUE_PTR
_GtkWidgetPath = OPAQUE_PTR
_GClosure = OPAQUE_PTR
_GIcon = OPAQUE_PTR
_GdkDisplay = OPAQUE_PTR
_GtkStyleProvider = OPAQUE_PTR
_WebKitWebWindowFeatures = OPAQUE_PTR
_void = OPAQUE_PTR
_GScanner = OPAQUE_PTR
_PangoFont = OPAQUE_PTR
_GtkStyleContext = OPAQUE_PTR
_GtkTextBuffer = OPAQUE_PTR
_GtkNumerableIcon = OPAQUE_PTR
_GdkAppLaunchContext = OPAQUE_PTR
_GObject = OPAQUE_PTR
_PangoLayout = OPAQUE_PTR
_GtkSymbolicColor = OPAQUE_PTR
_GtkWidget = OPAQUE_PTR
_GtkOffscreenWindow = OPAQUE_PTR
_GParamSpec = OPAQUE_PTR
_PangoAttrIterator = OPAQUE_PTR
_GtkIconSet = OPAQUE_PTR
_GtkSelectionData = OPAQUE_PTR
_GtkWindowGroup = OPAQUE_PTR
_JSGlobalContext = OPAQUE_PTR
_GFileMonitor = OPAQUE_PTR
_PangoLogAttr = OPAQUE_PTR
_PangoContext = OPAQUE_PTR
_GtkPathPriorityType = OPAQUE_PTR
_GtkSettings = OPAQUE_PTR
_PangoFontMap = OPAQUE_PTR
_PangoAttrList = OPAQUE_PTR
_PangoMatrix = OPAQUE_PTR
_GtkApplication = OPAQUE_PTR
_PangoAnalysis = OPAQUE_PTR
_PangoFontDescription = OPAQUE_PTR
_GdkCursor = OPAQUE_PTR
_GOptionGroup = OPAQUE_PTR
_GScanner = OPAQUE_PTR
_GtkWidgetClass = OPAQUE_PTR
_GdkEventKey = OPAQUE_PTR
_GdkDisplay = OPAQUE_PTR
_GtkSettings = OPAQUE_PTR
_GdkScreen = OPAQUE_PTR
_PangoFontMetrics = OPAQUE_PTR
_cairo_surface_t = OPAQUE_PTR
_GdkVisual = OPAQUE_PTR
_PangoFontMap = OPAQUE_PTR
_GSList = OPAQUE_PTR
_WebKitWebFrame = OPAQUE_PTR
_cairo_region_t = OPAQUE_PTR
_WebKitNetworkRequest = OPAQUE_PTR
_GdkWindow = OPAQUE_PTR
_PangoFontFamily = OPAQUE_PTR
_GtkClipboard = OPAQUE_PTR
_PangoFontset = OPAQUE_PTR
_GdkWindow = OPAQUE_PTR
_PangoFontDescription = OPAQUE_PTR
_GtkBorder = OPAQUE_PTR
_GError = OPAQUE_PTR
_PangoCoverage = OPAQUE_PTR
_cairo_t = OPAQUE_PTR
_GWeakRef = OPAQUE_PTR
_GdkVisual = OPAQUE_PTR
_CairoPattern = OPAQUE_PTR
_GdkDevice = OPAQUE_PTR
_PangoRectangle = OPAQUE_PTR
_GtkAccelGroup = OPAQUE_PTR
_GObject = OPAQUE_PTR
_GtkIconSource = OPAQUE_PTR
_GFile = OPAQUE_PTR
_GtkAllocation = OPAQUE_PTR
_GtkWidget = OPAQUE_PTR
_PangoLayoutLine = OPAQUE_PTR
_GtkIconSet = OPAQUE_PTR
_WebKitWebView = OPAQUE_PTR
_PangoTabArray = OPAQUE_PTR
_GtkStyleContext = OPAQUE_PTR
_GValue = OPAQUE_PTR
_GdkDeviceManager = OPAQUE_PTR
_GdkCursor = OPAQUE_PTR
_WebKitDOMDocument = OPAQUE_PTR
_PangoMatrix = OPAQUE_PTR
_GtkPrintOperation = OPAQUE_PTR
_PangoContext = OPAQUE_PTR
_GList = OPAQUE_PTR
_WebKitWebView = OPAQUE_PTR
_WebKitWebWindowFeatures = OPAQUE_PTR
_PangoCoverage = OPAQUE_PTR
_GParamSpec = OPAQUE_PTR
_GList = OPAQUE_PTR
_GdkRGBA = OPAQUE_PTR
_PangoGlyphString = OPAQUE_PTR
_WebKitSecurityOrigin = OPAQUE_PTR
_GObjectClass = OPAQUE_PTR
_GSList = OPAQUE_PTR
_GdkWindowAttr = OPAQUE_PTR
_WebKitWebDataSource = OPAQUE_PTR
_GdkColor = OPAQUE_PTR
_GdkRectangle = OPAQUE_PTR
_PangoLanguage = OPAQUE_PTR
_PangoAttrList = OPAQUE_PTR
_gunichar = OPAQUE_PTR
_GdkWMDecoration = OPAQUE_PTR
_PangoLogAttr = OPAQUE_PTR
_PangoLayout = OPAQUE_PTR
_GtkStyleProperties = OPAQUE_PTR
_GtkStyle = OPAQUE_PTR
_GParameter = OPAQUE_PTR
_GtkStyle = OPAQUE_PTR
_GIcon = OPAQUE_PTR
_GtkWindow = OPAQUE_PTR
_GtkGradient = OPAQUE_PTR
_cairo_pattern_t = OPAQUE_PTR
_GdkPixbuf = OPAQUE_PTR
_GdkScreen = OPAQUE_PTR
_GtkWidgetPath = OPAQUE_PTR
_GtkTargetEntry = OPAQUE_PTR
_GtkApplication = OPAQUE_PTR
_CairoPattern = OPAQUE_PTR
_GdkPixbufSimpleAnim = OPAQUE_PTR
_WebKitGeolocationPolicyDecision = OPAQUE_PTR
_PangoLanguage = OPAQUE_PTR
_GdkDevice = OPAQUE_PTR
_PangoTabArray = OPAQUE_PTR
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
    libwebkit3.webkit_web_frame_load_alternate_string.argtypes = [_WebKitWebFrame,Asciifier,Asciifier,Asciifier]
except:
   pass
try:
    libwebkit3.webkit_web_frame_find_frame.restype = _WebKitWebFrame
    libwebkit3.webkit_web_frame_find_frame.argtypes = [_WebKitWebFrame,Asciifier]
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
    libwebkit3.webkit_web_frame_load_string.argtypes = [_WebKitWebFrame,Asciifier,Asciifier,Asciifier,Asciifier]
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
    libwebkit3.webkit_web_frame_load_uri.argtypes = [_WebKitWebFrame,Asciifier]
except:
   pass
try:
    libwebkit3.webkit_web_frame_get_title.restype = c_char_p
    libwebkit3.webkit_web_frame_get_title.argtypes = [_WebKitWebFrame]
except:
   pass
from . import gobject__GObject
class WebKitWebFrame( gobject__GObject.GObject):
    """Class WebKitWebFrame Constructors"""
    def __init__( self, web_view,  obj = None):
        if obj: self._object = obj
        else:
            libwebkit3.webkit_web_frame_new.restype = OPAQUE_PTR
            
            if web_view : web_view = web_view._object
            else :  web_view = OPAQUE_PTR()

            libwebkit3.webkit_web_frame_new.argtypes = [_WebKitWebView]
            self._object = libwebkit3.webkit_web_frame_new(web_view, )

    """Methods"""
    def load_request(  self, request, ):
        if request: request = request._object
        else: request = OPAQUE_PTR()

        
        libwebkit3.webkit_web_frame_load_request( self._object,request )

    def load_alternate_string(  self, content, base_url, unreachable_url, ):

        
        libwebkit3.webkit_web_frame_load_alternate_string( self._object,content,base_url,unreachable_url )

    def find_frame(  self, name, ):

        from .webkit3 import WebKitWebFrame
        return WebKitWebFrame(None, obj=libwebkit3.webkit_web_frame_find_frame( self._object,name ) or OPAQUE_PTR() )

    def get_uri(  self, ):

        
        return libwebkit3.webkit_web_frame_get_uri( self._object )

    def get_data_source(  self, ):

        from .webkit3 import WebKitWebDataSource
        return WebKitWebDataSource( obj=libwebkit3.webkit_web_frame_get_data_source( self._object ) or OPAQUE_PTR() )

    def stop_loading(  self, ):

        
        libwebkit3.webkit_web_frame_stop_loading( self._object )

    def get_web_view(  self, ):

        from .webkit3 import WebKitWebView
        return WebKitWebView(None, obj=libwebkit3.webkit_web_frame_get_web_view( self._object ) or OPAQUE_PTR() )

    def get_horizontal_scrollbar_policy(  self, ):

        
        return libwebkit3.webkit_web_frame_get_horizontal_scrollbar_policy( self._object )

    def get_security_origin(  self, ):

        from .webkit3 import WebKitSecurityOrigin
        return WebKitSecurityOrigin( obj=libwebkit3.webkit_web_frame_get_security_origin( self._object ) or OPAQUE_PTR() )

    def get_parent(  self, ):

        from .webkit3 import WebKitWebFrame
        return WebKitWebFrame( obj=libwebkit3.webkit_web_frame_get_parent( self._object ) or OPAQUE_PTR() )

    def get_network_response(  self, ):

        from .webkit3 import WebKitNetworkResponse
        return WebKitNetworkResponse( obj=libwebkit3.webkit_web_frame_get_network_response( self._object ) or OPAQUE_PTR() )

    def py_print(  self, ):

        
        libwebkit3.webkit_web_frame_print( self._object )

    def get_provisional_data_source(  self, ):

        from .webkit3 import WebKitWebDataSource
        return WebKitWebDataSource( obj=libwebkit3.webkit_web_frame_get_provisional_data_source( self._object ) or OPAQUE_PTR() )

    def get_name(  self, ):

        
        return libwebkit3.webkit_web_frame_get_name( self._object )

    def load_string(  self, content, mime_type, encoding, base_uri, ):

        
        libwebkit3.webkit_web_frame_load_string( self._object,content,mime_type,encoding,base_uri )

    def get_dom_document(  self, ):

        from .webkit3 import WebKitDOMDocument
        return WebKitDOMDocument( obj=libwebkit3.webkit_web_frame_get_dom_document( self._object ) or OPAQUE_PTR() )

    def reload(  self, ):

        
        libwebkit3.webkit_web_frame_reload( self._object )

    def get_global_context(  self, ):

        from .javascriptcore import JSGlobalContext
        return JSGlobalContext( obj=libwebkit3.webkit_web_frame_get_global_context( self._object )  or OPAQUE_PTR())

    def get_vertical_scrollbar_policy(  self, ):

        
        return libwebkit3.webkit_web_frame_get_vertical_scrollbar_policy( self._object )

    def print_full(  self, operation, action, error, ):
        if operation: operation = operation._object
        else: operation = OPAQUE_PTR()
        if action: action = action._object
        else: action = OPAQUE_PTR()
        if error: error = error._object
        else: error = OPAQUE_PTR()

        
        return libwebkit3.webkit_web_frame_print_full( self._object,operation,action,error )

    def get_load_status(  self, ):

        
        return libwebkit3.webkit_web_frame_get_load_status( self._object )

    def load_uri(  self, uri, ):

        
        libwebkit3.webkit_web_frame_load_uri( self._object,uri )

    def get_title(  self, ):

        
        return libwebkit3.webkit_web_frame_get_title( self._object )

