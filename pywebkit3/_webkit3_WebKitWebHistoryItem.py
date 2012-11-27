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
_GList = c_void_p
_char = c_void_p
_GtkTargetList = c_void_p
_GtkWidget = c_void_p
_JSGlobalContext = c_void_p
_WebKitSecurityOrigin = c_void_p
__WebKitNetworkRequest = c_void_p
_JSContext = c_void_p
_SoupMessage = c_void_p
_WebKitWebDataSource = c_void_p
_WebKitWebSettings = c_void_p
__WebKitWebHistoryItem = c_void_p
__WebKitWebWindowFeatures = c_void_p
_WebKitWebHistoryItem = c_void_p
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
class WebKitWebHistoryItem( _gobject_GObject.GObject):
    """Class WebKitWebHistoryItem Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libwebkit3.webkit_web_history_item_new.restype = c_void_p

        libwebkit3.webkit_web_history_item_new.argtypes = []
        self._object = libwebkit3.webkit_web_history_item_new()

    """Methods"""
    def get_last_visited_time(self, ):

        libwebkit3.webkit_web_history_item_get_last_visited_time.restype = gdouble
        libwebkit3.webkit_web_history_item_get_last_visited_time.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_history_item_get_last_visited_time(self._object, )

    def get_original_uri(self, ):

        libwebkit3.webkit_web_history_item_get_original_uri.restype = _gchar
        libwebkit3.webkit_web_history_item_get_original_uri.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_history_item_get_original_uri(self._object, )

    def get_title(self, ):

        libwebkit3.webkit_web_history_item_get_title.restype = _gchar
        libwebkit3.webkit_web_history_item_get_title.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_history_item_get_title(self._object, )

    def set_alternate_title(self,  title,):

        libwebkit3.webkit_web_history_item_set_alternate_title.argtypes = [c_void_p, c_char_p]
        
        libwebkit3.webkit_web_history_item_set_alternate_title(self._object,  title,)

    def get_alternate_title(self, ):

        libwebkit3.webkit_web_history_item_get_alternate_title.restype = _gchar
        libwebkit3.webkit_web_history_item_get_alternate_title.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_history_item_get_alternate_title(self._object, )

    def copy(self, ):

        libwebkit3.webkit_web_history_item_copy.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_history_item_copy.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem(None, obj=libwebkit3.webkit_web_history_item_copy(self._object, ) or c_void_p() )

    def get_uri(self, ):

        libwebkit3.webkit_web_history_item_get_uri.restype = _gchar
        libwebkit3.webkit_web_history_item_get_uri.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_history_item_get_uri(self._object, )

    @staticmethod
    def new_with_data( uri, title,):
        libwebkit3.webkit_web_history_item_new_with_data.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_history_item_new_with_data.argtypes = [c_char_p,c_char_p]
        return libwebkit3.webkit_web_history_item_new_with_data(uri, title, )

