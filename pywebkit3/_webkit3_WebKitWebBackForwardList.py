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
class WebKitWebBackForwardList( _gobject_GObject.GObject):
    """Class WebKitWebBackForwardList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def set_limit(self,  limit,):

        libwebkit3.webkit_web_back_forward_list_set_limit.argtypes = [c_void_p, gint]
        
        libwebkit3.webkit_web_back_forward_list_set_limit(self._object,  limit,)

    def add_item(self,  history_item,):
        if history_item : history_item = history_item._object
        else : history_item = c_void_p()

        libwebkit3.webkit_web_back_forward_list_add_item.argtypes = [c_void_p, _WebKitWebHistoryItem]
        
        libwebkit3.webkit_web_back_forward_list_add_item(self._object,  history_item,)

    def get_back_length(self, ):

        libwebkit3.webkit_web_back_forward_list_get_back_length.restype = gint
        libwebkit3.webkit_web_back_forward_list_get_back_length.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_back_forward_list_get_back_length(self._object, )

    def go_back(self, ):

        libwebkit3.webkit_web_back_forward_list_go_back.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_back_forward_list_go_back(self._object, )

    def get_back_item(self, ):

        libwebkit3.webkit_web_back_forward_list_get_back_item.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_back_forward_list_get_back_item.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem(None, obj=libwebkit3.webkit_web_back_forward_list_get_back_item(self._object, ) or c_void_p() )

    def get_forward_list_with_limit(self,  limit,):

        libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit.restype = _GList
        libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit.argtypes = [c_void_p, gint]
        from pywebkit3.gobject import GList
        return GList( obj=libwebkit3.webkit_web_back_forward_list_get_forward_list_with_limit(self._object,  limit,) or c_void_p())

    def get_current_item(self, ):

        libwebkit3.webkit_web_back_forward_list_get_current_item.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_back_forward_list_get_current_item.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_current_item(self._object, ) or c_void_p() )

    def go_to_item(self,  history_item,):
        if history_item : history_item = history_item._object
        else : history_item = c_void_p()

        libwebkit3.webkit_web_back_forward_list_go_to_item.argtypes = [c_void_p, _WebKitWebHistoryItem]
        
        libwebkit3.webkit_web_back_forward_list_go_to_item(self._object,  history_item,)

    def get_back_list_with_limit(self,  limit,):

        libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit.restype = _GList
        libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit.argtypes = [c_void_p, gint]
        from pywebkit3.gobject import GList
        return GList( obj=libwebkit3.webkit_web_back_forward_list_get_back_list_with_limit(self._object,  limit,) or c_void_p())

    def get_forward_length(self, ):

        libwebkit3.webkit_web_back_forward_list_get_forward_length.restype = gint
        libwebkit3.webkit_web_back_forward_list_get_forward_length.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_back_forward_list_get_forward_length(self._object, )

    def get_forward_item(self, ):

        libwebkit3.webkit_web_back_forward_list_get_forward_item.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_back_forward_list_get_forward_item.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_forward_item(self._object, ) or c_void_p() )

    def contains_item(self,  history_item,):
        if history_item : history_item = history_item._object
        else : history_item = c_void_p()

        libwebkit3.webkit_web_back_forward_list_contains_item.restype = gboolean
        libwebkit3.webkit_web_back_forward_list_contains_item.argtypes = [c_void_p, _WebKitWebHistoryItem]
        
        return libwebkit3.webkit_web_back_forward_list_contains_item(self._object,  history_item,)

    def get_nth_item(self,  index,):

        libwebkit3.webkit_web_back_forward_list_get_nth_item.restype = _WebKitWebHistoryItem
        libwebkit3.webkit_web_back_forward_list_get_nth_item.argtypes = [c_void_p, gint]
        from pywebkit3.webkit3 import WebKitWebHistoryItem
        return WebKitWebHistoryItem( obj=libwebkit3.webkit_web_back_forward_list_get_nth_item(self._object,  index,) or c_void_p() )

    def go_forward(self, ):

        libwebkit3.webkit_web_back_forward_list_go_forward.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_back_forward_list_go_forward(self._object, )

    def clear(self, ):

        libwebkit3.webkit_web_back_forward_list_clear.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_back_forward_list_clear(self._object, )

    def get_limit(self, ):

        libwebkit3.webkit_web_back_forward_list_get_limit.restype = gint
        libwebkit3.webkit_web_back_forward_list_get_limit.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_back_forward_list_get_limit(self._object, )

    @staticmethod
    def new_with_web_view( web_view,):
        if web_view : web_view = web_view._object
        else : web_view = c_void_p()
        libwebkit3.webkit_web_back_forward_list_new_with_web_view.restype = _WebKitWebBackForwardList
        libwebkit3.webkit_web_back_forward_list_new_with_web_view.argtypes = [_WebKitWebView]
        return libwebkit3.webkit_web_back_forward_list_new_with_web_view(web_view, )

