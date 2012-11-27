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
_WebKitNetworkResponse = c_void_p
_WebKitWebWindowFeatures = c_void_p
_GdkPixbuf = c_void_p
_WebKitWebFrame = c_void_p
_char = c_void_p
_GtkTargetList = c_void_p
_GtkWidget = c_void_p
_JSGlobalContext = c_void_p
_WebKitSecurityOrigin = c_void_p
__WebKitNetworkRequest = c_void_p
_JSContext = c_void_p
_WebKitWebDataSource = c_void_p
_WebKitWebSettings = c_void_p
__WebKitWebHistoryItem = c_void_p
__GdkEventButton = c_void_p
_WebKitViewportAttributes = c_void_p
_WebKitWebInspector = c_void_p
__GError = c_void_p
__WebKitWebSettings = c_void_p
_gchar = c_void_p
__WebKitWebView = c_void_p
_WebKitHitTestResult = c_void_p
_WebKitDOMDocument = c_void_p
__GtkPrintOperation = c_void_p
_WebKitWebBackForwardList = c_void_p
_WebKitWebView = c_void_p
"""Enumerations"""
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitLoadStatus = c_int

import _gobject_GObject
class WebKitWebFrame( _gobject_GObject.GObject):
    """Class WebKitWebFrame Constructors"""
    def __init__( self, web_view,  obj = None):
        if obj: self._object = obj
        else:
            libwebkit3.webkit_web_frame_new.restype = c_void_p
        if web_view : web_view = web_view._object
        else : web_view = c_void_p()

        libwebkit3.webkit_web_frame_new.argtypes = [_WebKitWebView]
        self._object = libwebkit3.webkit_web_frame_new(web_view, )

    """Methods"""
    def load_request(self,  request,):
        if request : request = request._object
        else : request = c_void_p()

        libwebkit3.webkit_web_frame_load_request.argtypes = [c_void_p, _WebKitNetworkRequest]
        
        libwebkit3.webkit_web_frame_load_request(self._object,  request,)

    def load_alternate_string(self,  content, base_url, unreachable_url,):

        libwebkit3.webkit_web_frame_load_alternate_string.argtypes = [c_void_p, c_char_p,c_char_p,c_char_p]
        
        libwebkit3.webkit_web_frame_load_alternate_string(self._object,  content, base_url, unreachable_url,)

    def find_frame(self,  name,):

        libwebkit3.webkit_web_frame_find_frame.restype = _WebKitWebFrame
        libwebkit3.webkit_web_frame_find_frame.argtypes = [c_void_p, c_char_p]
        from pywebkit3.webkit3 import WebKitWebFrame
        return WebKitWebFrame(None,None, obj=libwebkit3.webkit_web_frame_find_frame(self._object,  name,) or c_void_p() )

    def get_uri(self, ):

        libwebkit3.webkit_web_frame_get_uri.restype = _gchar
        libwebkit3.webkit_web_frame_get_uri.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_frame_get_uri(self._object, )

    def get_data_source(self, ):

        libwebkit3.webkit_web_frame_get_data_source.restype = _WebKitWebDataSource
        libwebkit3.webkit_web_frame_get_data_source.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebDataSource
        return WebKitWebDataSource( obj=libwebkit3.webkit_web_frame_get_data_source(self._object, ) or c_void_p() )

    def stop_loading(self, ):

        libwebkit3.webkit_web_frame_stop_loading.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_frame_stop_loading(self._object, )

    def get_web_view(self, ):

        libwebkit3.webkit_web_frame_get_web_view.restype = _WebKitWebView
        libwebkit3.webkit_web_frame_get_web_view.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebView
        return WebKitWebView( obj=libwebkit3.webkit_web_frame_get_web_view(self._object, ) or c_void_p() )

    def get_horizontal_scrollbar_policy(self, ):

        libwebkit3.webkit_web_frame_get_horizontal_scrollbar_policy.restype = GtkPolicyType
        libwebkit3.webkit_web_frame_get_horizontal_scrollbar_policy.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_frame_get_horizontal_scrollbar_policy(self._object, )

    def get_security_origin(self, ):

        libwebkit3.webkit_web_frame_get_security_origin.restype = _WebKitSecurityOrigin
        libwebkit3.webkit_web_frame_get_security_origin.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitSecurityOrigin
        return WebKitSecurityOrigin( obj=libwebkit3.webkit_web_frame_get_security_origin(self._object, ) or c_void_p() )

    def get_parent(self, ):

        libwebkit3.webkit_web_frame_get_parent.restype = _WebKitWebFrame
        libwebkit3.webkit_web_frame_get_parent.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebFrame
        return WebKitWebFrame(None, obj=libwebkit3.webkit_web_frame_get_parent(self._object, ) or c_void_p() )

    def get_network_response(self, ):

        libwebkit3.webkit_web_frame_get_network_response.restype = _WebKitNetworkResponse
        libwebkit3.webkit_web_frame_get_network_response.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitNetworkResponse
        return WebKitNetworkResponse( obj=libwebkit3.webkit_web_frame_get_network_response(self._object, ) or c_void_p() )

    def py_print(self, ):

        libwebkit3.webkit_web_frame_print.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_frame_print(self._object, )

    def get_provisional_data_source(self, ):

        libwebkit3.webkit_web_frame_get_provisional_data_source.restype = _WebKitWebDataSource
        libwebkit3.webkit_web_frame_get_provisional_data_source.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebDataSource
        return WebKitWebDataSource( obj=libwebkit3.webkit_web_frame_get_provisional_data_source(self._object, ) or c_void_p() )

    def get_name(self, ):

        libwebkit3.webkit_web_frame_get_name.restype = _gchar
        libwebkit3.webkit_web_frame_get_name.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_frame_get_name(self._object, )

    def load_string(self,  content, mime_type, encoding, base_uri,):

        libwebkit3.webkit_web_frame_load_string.argtypes = [c_void_p, c_char_p,c_char_p,c_char_p,c_char_p]
        
        libwebkit3.webkit_web_frame_load_string(self._object,  content, mime_type, encoding, base_uri,)

    def get_dom_document(self, ):

        libwebkit3.webkit_web_frame_get_dom_document.restype = _WebKitDOMDocument
        libwebkit3.webkit_web_frame_get_dom_document.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitDOMDocument
        return WebKitDOMDocument( obj=libwebkit3.webkit_web_frame_get_dom_document(self._object, ) or c_void_p() )

    def reload(self, ):

        libwebkit3.webkit_web_frame_reload.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_frame_reload(self._object, )

    def get_global_context(self, ):

        libwebkit3.webkit_web_frame_get_global_context.restype = _JSGlobalContext
        libwebkit3.webkit_web_frame_get_global_context.argtypes = [c_void_p]
        from pywebkit3.javascriptcore import JSGlobalContext
        return JSGlobalContext( obj=libwebkit3.webkit_web_frame_get_global_context(self._object, )  or c_void_p())

    def get_vertical_scrollbar_policy(self, ):

        libwebkit3.webkit_web_frame_get_vertical_scrollbar_policy.restype = GtkPolicyType
        libwebkit3.webkit_web_frame_get_vertical_scrollbar_policy.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_frame_get_vertical_scrollbar_policy(self._object, )

    def print_full(self,  operation, action, error,):
        if operation : operation = operation._object
        else : operation = c_void_p()
        if action : action = action._object
        else : action = c_void_p()
        if error : error = error._object
        else : error = c_void_p()

        libwebkit3.webkit_web_frame_print_full.restype = GtkPrintOperationResult
        libwebkit3.webkit_web_frame_print_full.argtypes = [c_void_p, _GtkPrintOperation,GtkPrintOperationAction,_GError]
        
        return libwebkit3.webkit_web_frame_print_full(self._object,  operation, action, error,)

    def get_load_status(self, ):

        libwebkit3.webkit_web_frame_get_load_status.restype = WebKitLoadStatus
        libwebkit3.webkit_web_frame_get_load_status.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_frame_get_load_status(self._object, )

    def load_uri(self,  uri,):

        libwebkit3.webkit_web_frame_load_uri.argtypes = [c_void_p, c_char_p]
        
        libwebkit3.webkit_web_frame_load_uri(self._object,  uri,)

    def get_title(self, ):

        libwebkit3.webkit_web_frame_get_title.restype = _gchar
        libwebkit3.webkit_web_frame_get_title.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_frame_get_title(self._object, )

