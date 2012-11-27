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
__WebKitNetworkRequest = c_void_p
_WebKitViewportAttributes = c_void_p
_JSContext = c_void_p
__WebKitWebSettings = c_void_p
_gchar = c_void_p
_GdkPixbuf = c_void_p
__GdkEventButton = c_void_p
_WebKitWebFrame = c_void_p
_WebKitWebWindowFeatures = c_void_p
__WebKitWebHistoryItem = c_void_p
_char = c_void_p
_WebKitHitTestResult = c_void_p
_GtkTargetList = c_void_p
_GtkWidget = c_void_p
_WebKitWebSettings = c_void_p
_WebKitDOMDocument = c_void_p
_WebKitWebBackForwardList = c_void_p
_WebKitWebInspector = c_void_p
"""Enumerations"""
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int

import _gtk3_GtkContainer
class WebKitWebView( _gtk3_GtkContainer.GtkContainer):
    """Class WebKitWebView Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libwebkit3.webkit_web_view_new.restype = c_void_p

        libwebkit3.webkit_web_view_new.argtypes = []
        self._object = libwebkit3.webkit_web_view_new()

    """Methods"""
    def zoom_in(self, ):

        libwebkit3.webkit_web_view_zoom_in.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_zoom_in(self._object, )

    def can_copy_clipboard(self, ):

        libwebkit3.webkit_web_view_can_copy_clipboard.restype = gboolean
        libwebkit3.webkit_web_view_can_copy_clipboard.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_can_copy_clipboard(self._object, )

    def get_uri(self, ):

        libwebkit3.webkit_web_view_get_uri.restype = _gchar
        libwebkit3.webkit_web_view_get_uri.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_uri(self._object, )

    def has_selection(self, ):

        libwebkit3.webkit_web_view_has_selection.restype = gboolean
        libwebkit3.webkit_web_view_has_selection.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_has_selection(self._object, )

    def reload_bypass_cache(self, ):

        libwebkit3.webkit_web_view_reload_bypass_cache.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_reload_bypass_cache(self._object, )

    def load_string(self,  content, mime_type, encoding, base_uri,):

        libwebkit3.webkit_web_view_load_string.argtypes = [c_void_p, c_char_p,c_char_p,c_char_p,c_char_p]
        
        libwebkit3.webkit_web_view_load_string(self._object,  content, mime_type, encoding, base_uri,)

    def get_full_content_zoom(self, ):

        libwebkit3.webkit_web_view_get_full_content_zoom.restype = gboolean
        libwebkit3.webkit_web_view_get_full_content_zoom.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_full_content_zoom(self._object, )

    def can_paste_clipboard(self, ):

        libwebkit3.webkit_web_view_can_paste_clipboard.restype = gboolean
        libwebkit3.webkit_web_view_can_paste_clipboard.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_can_paste_clipboard(self._object, )

    def get_encoding(self, ):

        libwebkit3.webkit_web_view_get_encoding.restype = _gchar
        libwebkit3.webkit_web_view_get_encoding.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_encoding(self._object, )

    def set_custom_encoding(self,  encoding,):

        libwebkit3.webkit_web_view_set_custom_encoding.argtypes = [c_void_p, c_char_p]
        
        libwebkit3.webkit_web_view_set_custom_encoding(self._object,  encoding,)

    def set_view_mode(self,  mode,):

        libwebkit3.webkit_web_view_set_view_mode.argtypes = [c_void_p, WebKitWebViewViewMode]
        
        libwebkit3.webkit_web_view_set_view_mode(self._object,  mode,)

    def undo(self, ):

        libwebkit3.webkit_web_view_undo.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_undo(self._object, )

    def set_settings(self,  settings,):
        if settings : settings = settings._object
        else : settings = c_void_p()

        libwebkit3.webkit_web_view_set_settings.argtypes = [c_void_p, _WebKitWebSettings]
        
        libwebkit3.webkit_web_view_set_settings(self._object,  settings,)

    def set_highlight_text_matches(self,  highlight,):

        libwebkit3.webkit_web_view_set_highlight_text_matches.argtypes = [c_void_p, gboolean]
        
        libwebkit3.webkit_web_view_set_highlight_text_matches(self._object,  highlight,)

    def get_paste_target_list(self, ):

        libwebkit3.webkit_web_view_get_paste_target_list.restype = _GtkTargetList
        libwebkit3.webkit_web_view_get_paste_target_list.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkTargetList
        return GtkTargetList( obj=libwebkit3.webkit_web_view_get_paste_target_list(self._object, ) or c_void_p())

    def get_dom_document(self, ):

        libwebkit3.webkit_web_view_get_dom_document.restype = _WebKitDOMDocument
        libwebkit3.webkit_web_view_get_dom_document.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitDOMDocument
        return WebKitDOMDocument( obj=libwebkit3.webkit_web_view_get_dom_document(self._object, ) or c_void_p() )

    def can_cut_clipboard(self, ):

        libwebkit3.webkit_web_view_can_cut_clipboard.restype = gboolean
        libwebkit3.webkit_web_view_can_cut_clipboard.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_can_cut_clipboard(self._object, )

    def reload(self, ):

        libwebkit3.webkit_web_view_reload.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_reload(self._object, )

    def set_transparent(self,  flag,):

        libwebkit3.webkit_web_view_set_transparent.argtypes = [c_void_p, gboolean]
        
        libwebkit3.webkit_web_view_set_transparent(self._object,  flag,)

    def unmark_text_matches(self, ):

        libwebkit3.webkit_web_view_unmark_text_matches.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_unmark_text_matches(self._object, )

    def get_view_source_mode(self, ):

        libwebkit3.webkit_web_view_get_view_source_mode.restype = gboolean
        libwebkit3.webkit_web_view_get_view_source_mode.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_view_source_mode(self._object, )

    def go_back_or_forward(self,  steps,):

        libwebkit3.webkit_web_view_go_back_or_forward.argtypes = [c_void_p, gint]
        
        libwebkit3.webkit_web_view_go_back_or_forward(self._object,  steps,)

    def copy_clipboard(self, ):

        libwebkit3.webkit_web_view_copy_clipboard.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_copy_clipboard(self._object, )

    def get_zoom_level(self, ):

        libwebkit3.webkit_web_view_get_zoom_level.restype = gfloat
        libwebkit3.webkit_web_view_get_zoom_level.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_zoom_level(self._object, )

    def get_load_status(self, ):

        libwebkit3.webkit_web_view_get_load_status.restype = WebKitLoadStatus
        libwebkit3.webkit_web_view_get_load_status.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_load_status(self._object, )

    def get_icon_uri(self, ):

        libwebkit3.webkit_web_view_get_icon_uri.restype = _gchar
        libwebkit3.webkit_web_view_get_icon_uri.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_icon_uri(self._object, )

    def set_editable(self,  flag,):

        libwebkit3.webkit_web_view_set_editable.argtypes = [c_void_p, gboolean]
        
        libwebkit3.webkit_web_view_set_editable(self._object,  flag,)

    def move_cursor(self,  step, count,):
        if step : step = step._object
        else : step = c_void_p()

        libwebkit3.webkit_web_view_move_cursor.argtypes = [c_void_p, GtkMovementStep,gint]
        
        libwebkit3.webkit_web_view_move_cursor(self._object,  step, count,)

    def load_html_string(self,  content, base_uri,):

        libwebkit3.webkit_web_view_load_html_string.argtypes = [c_void_p, c_char_p,c_char_p]
        
        libwebkit3.webkit_web_view_load_html_string(self._object,  content, base_uri,)

    def paste_clipboard(self, ):

        libwebkit3.webkit_web_view_paste_clipboard.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_paste_clipboard(self._object, )

    def get_title(self, ):

        libwebkit3.webkit_web_view_get_title.restype = _gchar
        libwebkit3.webkit_web_view_get_title.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_title(self._object, )

    def go_back(self, ):

        libwebkit3.webkit_web_view_go_back.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_go_back(self._object, )

    def redo(self, ):

        libwebkit3.webkit_web_view_redo.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_redo(self._object, )

    def go_forward(self, ):

        libwebkit3.webkit_web_view_go_forward.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_go_forward(self._object, )

    def set_maintains_back_forward_list(self,  flag,):

        libwebkit3.webkit_web_view_set_maintains_back_forward_list.argtypes = [c_void_p, gboolean]
        
        libwebkit3.webkit_web_view_set_maintains_back_forward_list(self._object,  flag,)

    def get_focused_frame(self, ):

        libwebkit3.webkit_web_view_get_focused_frame.restype = _WebKitWebFrame
        libwebkit3.webkit_web_view_get_focused_frame.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebFrame
        return WebKitWebFrame(None,None, obj=libwebkit3.webkit_web_view_get_focused_frame(self._object, ) or c_void_p() )

    def can_show_mime_type(self,  mime_type,):

        libwebkit3.webkit_web_view_can_show_mime_type.restype = gboolean
        libwebkit3.webkit_web_view_can_show_mime_type.argtypes = [c_void_p, c_char_p]
        
        return libwebkit3.webkit_web_view_can_show_mime_type(self._object,  mime_type,)

    def get_window_features(self, ):

        libwebkit3.webkit_web_view_get_window_features.restype = _WebKitWebWindowFeatures
        libwebkit3.webkit_web_view_get_window_features.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebWindowFeatures
        return WebKitWebWindowFeatures(None, obj=libwebkit3.webkit_web_view_get_window_features(self._object, ) or c_void_p() )

    def get_back_forward_list(self, ):

        libwebkit3.webkit_web_view_get_back_forward_list.restype = _WebKitWebBackForwardList
        libwebkit3.webkit_web_view_get_back_forward_list.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebBackForwardList
        return WebKitWebBackForwardList( obj=libwebkit3.webkit_web_view_get_back_forward_list(self._object, ) or c_void_p() )

    def can_go_forward(self, ):

        libwebkit3.webkit_web_view_can_go_forward.restype = gboolean
        libwebkit3.webkit_web_view_can_go_forward.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_can_go_forward(self._object, )

    def get_settings(self, ):

        libwebkit3.webkit_web_view_get_settings.restype = _WebKitWebSettings
        libwebkit3.webkit_web_view_get_settings.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebSettings
        return WebKitWebSettings(None, obj=libwebkit3.webkit_web_view_get_settings(self._object, ) or c_void_p() )

    def execute_script(self,  script,):

        libwebkit3.webkit_web_view_execute_script.argtypes = [c_void_p, c_char_p]
        
        libwebkit3.webkit_web_view_execute_script(self._object,  script,)

    def cut_clipboard(self, ):

        libwebkit3.webkit_web_view_cut_clipboard.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_cut_clipboard(self._object, )

    def get_inspector(self, ):

        libwebkit3.webkit_web_view_get_inspector.restype = _WebKitWebInspector
        libwebkit3.webkit_web_view_get_inspector.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebInspector
        return WebKitWebInspector( obj=libwebkit3.webkit_web_view_get_inspector(self._object, ) or c_void_p() )

    def get_transparent(self, ):

        libwebkit3.webkit_web_view_get_transparent.restype = gboolean
        libwebkit3.webkit_web_view_get_transparent.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_transparent(self._object, )

    def get_custom_encoding(self, ):

        libwebkit3.webkit_web_view_get_custom_encoding.restype = _char
        libwebkit3.webkit_web_view_get_custom_encoding.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_custom_encoding(self._object, )

    def get_icon_pixbuf(self, ):

        libwebkit3.webkit_web_view_get_icon_pixbuf.restype = _GdkPixbuf
        libwebkit3.webkit_web_view_get_icon_pixbuf.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libwebkit3.webkit_web_view_get_icon_pixbuf(self._object, ) or c_void_p())

    def can_undo(self, ):

        libwebkit3.webkit_web_view_can_undo.restype = gboolean
        libwebkit3.webkit_web_view_can_undo.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_can_undo(self._object, )

    def get_view_mode(self, ):

        libwebkit3.webkit_web_view_get_view_mode.restype = WebKitWebViewViewMode
        libwebkit3.webkit_web_view_get_view_mode.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_view_mode(self._object, )

    def set_zoom_level(self,  zoom_level,):

        libwebkit3.webkit_web_view_set_zoom_level.argtypes = [c_void_p, gfloat]
        
        libwebkit3.webkit_web_view_set_zoom_level(self._object,  zoom_level,)

    def search_text(self,  text, case_sensitive, forward, wrap,):

        libwebkit3.webkit_web_view_search_text.restype = gboolean
        libwebkit3.webkit_web_view_search_text.argtypes = [c_void_p, c_char_p,gboolean,gboolean,gboolean]
        
        return libwebkit3.webkit_web_view_search_text(self._object,  text, case_sensitive, forward, wrap,)

    def load_uri(self,  uri,):

        libwebkit3.webkit_web_view_load_uri.argtypes = [c_void_p, c_char_p]
        
        libwebkit3.webkit_web_view_load_uri(self._object,  uri,)

    def get_editable(self, ):

        libwebkit3.webkit_web_view_get_editable.restype = gboolean
        libwebkit3.webkit_web_view_get_editable.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_editable(self._object, )

    def get_main_frame(self, ):

        libwebkit3.webkit_web_view_get_main_frame.restype = _WebKitWebFrame
        libwebkit3.webkit_web_view_get_main_frame.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitWebFrame
        return WebKitWebFrame(None, obj=libwebkit3.webkit_web_view_get_main_frame(self._object, ) or c_void_p() )

    def get_progress(self, ):

        libwebkit3.webkit_web_view_get_progress.restype = gdouble
        libwebkit3.webkit_web_view_get_progress.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_get_progress(self._object, )

    def open(self,  uri,):

        libwebkit3.webkit_web_view_open.argtypes = [c_void_p, c_char_p]
        
        libwebkit3.webkit_web_view_open(self._object,  uri,)

    def set_full_content_zoom(self,  full_content_zoom,):

        libwebkit3.webkit_web_view_set_full_content_zoom.argtypes = [c_void_p, gboolean]
        
        libwebkit3.webkit_web_view_set_full_content_zoom(self._object,  full_content_zoom,)

    def delete_selection(self, ):

        libwebkit3.webkit_web_view_delete_selection.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_delete_selection(self._object, )

    def select_all(self, ):

        libwebkit3.webkit_web_view_select_all.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_select_all(self._object, )

    def try_get_favicon_pixbuf(self,  width, height,):

        libwebkit3.webkit_web_view_try_get_favicon_pixbuf.restype = _GdkPixbuf
        libwebkit3.webkit_web_view_try_get_favicon_pixbuf.argtypes = [c_void_p, guint,guint]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libwebkit3.webkit_web_view_try_get_favicon_pixbuf(self._object,  width, height,) or c_void_p())

    def get_hit_test_result(self,  event,):
        if event : event = event._object
        else : event = c_void_p()

        libwebkit3.webkit_web_view_get_hit_test_result.restype = _WebKitHitTestResult
        libwebkit3.webkit_web_view_get_hit_test_result.argtypes = [c_void_p, _GdkEventButton]
        from pywebkit3.webkit3 import WebKitHitTestResult
        return WebKitHitTestResult( obj=libwebkit3.webkit_web_view_get_hit_test_result(self._object,  event,) or c_void_p() )

    def mark_text_matches(self,  string, case_sensitive, limit,):

        libwebkit3.webkit_web_view_mark_text_matches.restype = guint
        libwebkit3.webkit_web_view_mark_text_matches.argtypes = [c_void_p, c_char_p,gboolean,guint]
        
        return libwebkit3.webkit_web_view_mark_text_matches(self._object,  string, case_sensitive, limit,)

    def zoom_out(self, ):

        libwebkit3.webkit_web_view_zoom_out.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_zoom_out(self._object, )

    def can_redo(self, ):

        libwebkit3.webkit_web_view_can_redo.restype = gboolean
        libwebkit3.webkit_web_view_can_redo.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_can_redo(self._object, )

    def load_request(self,  request,):
        if request : request = request._object
        else : request = c_void_p()

        libwebkit3.webkit_web_view_load_request.argtypes = [c_void_p, _WebKitNetworkRequest]
        
        libwebkit3.webkit_web_view_load_request(self._object,  request,)

    def stop_loading(self, ):

        libwebkit3.webkit_web_view_stop_loading.argtypes = [c_void_p]
        
        libwebkit3.webkit_web_view_stop_loading(self._object, )

    def get_copy_target_list(self, ):

        libwebkit3.webkit_web_view_get_copy_target_list.restype = _GtkTargetList
        libwebkit3.webkit_web_view_get_copy_target_list.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkTargetList
        return GtkTargetList( obj=libwebkit3.webkit_web_view_get_copy_target_list(self._object, ) or c_void_p())

    def get_viewport_attributes(self, ):

        libwebkit3.webkit_web_view_get_viewport_attributes.restype = _WebKitViewportAttributes
        libwebkit3.webkit_web_view_get_viewport_attributes.argtypes = [c_void_p]
        from pywebkit3.webkit3 import WebKitViewportAttributes
        return WebKitViewportAttributes( obj=libwebkit3.webkit_web_view_get_viewport_attributes(self._object, ) or c_void_p() )

    def can_go_back_or_forward(self,  steps,):

        libwebkit3.webkit_web_view_can_go_back_or_forward.restype = gboolean
        libwebkit3.webkit_web_view_can_go_back_or_forward.argtypes = [c_void_p, gint]
        
        return libwebkit3.webkit_web_view_can_go_back_or_forward(self._object,  steps,)

    def go_to_back_forward_item(self,  item,):
        if item : item = item._object
        else : item = c_void_p()

        libwebkit3.webkit_web_view_go_to_back_forward_item.restype = gboolean
        libwebkit3.webkit_web_view_go_to_back_forward_item.argtypes = [c_void_p, _WebKitWebHistoryItem]
        
        return libwebkit3.webkit_web_view_go_to_back_forward_item(self._object,  item,)

    def set_view_source_mode(self,  view_source_mode,):

        libwebkit3.webkit_web_view_set_view_source_mode.argtypes = [c_void_p, gboolean]
        
        libwebkit3.webkit_web_view_set_view_source_mode(self._object,  view_source_mode,)

    def can_go_back(self, ):

        libwebkit3.webkit_web_view_can_go_back.restype = gboolean
        libwebkit3.webkit_web_view_can_go_back.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_view_can_go_back(self._object, )

    def get_javascript_global_context(self, ):

        libwebkit3.webkit_web_view_get_javascript_global_context.restype = _JSContext
        libwebkit3.webkit_web_view_get_javascript_global_context.argtypes = [c_void_p]
        from pywebkit3.javascriptcore import JSContext
        return JSContext( obj=libwebkit3.webkit_web_view_get_javascript_global_context(self._object, )  or c_void_p())

