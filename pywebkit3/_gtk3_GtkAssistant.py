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
__GdkPixbuf = c_void_p
_gchar = c_void_p
_GdkPixbuf = c_void_p
_GtkWidget = c_void_p
__GtkWidget = c_void_p
"""Enumerations"""
GtkAssistantPageType = c_int

import _gtk3_GtkWindow
class GtkAssistant( _gtk3_GtkWindow.GtkWindow):
    """Class GtkAssistant Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_assistant_new.restype = c_void_p

        libgtk3.gtk_assistant_new.argtypes = []
        self._object = libgtk3.gtk_assistant_new()

    """Methods"""
    def set_current_page(self,  page_num,):

        libgtk3.gtk_assistant_set_current_page.argtypes = [c_void_p, gint]
        
        libgtk3.gtk_assistant_set_current_page(self._object,  page_num,)

    def append_page(self,  page,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_append_page.restype = gint
        libgtk3.gtk_assistant_append_page.argtypes = [c_void_p, _GtkWidget]
        
        return libgtk3.gtk_assistant_append_page(self._object,  page,)

    def set_page_complete(self,  page, complete,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_set_page_complete.argtypes = [c_void_p, _GtkWidget,gboolean]
        
        libgtk3.gtk_assistant_set_page_complete(self._object,  page, complete,)

    def next_page(self, ):

        libgtk3.gtk_assistant_next_page.argtypes = [c_void_p]
        
        libgtk3.gtk_assistant_next_page(self._object, )

    def get_page_type(self,  page,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_get_page_type.restype = GtkAssistantPageType
        libgtk3.gtk_assistant_get_page_type.argtypes = [c_void_p, _GtkWidget]
        
        return libgtk3.gtk_assistant_get_page_type(self._object,  page,)

    def insert_page(self,  page, position,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_insert_page.restype = gint
        libgtk3.gtk_assistant_insert_page.argtypes = [c_void_p, _GtkWidget,gint]
        
        return libgtk3.gtk_assistant_insert_page(self._object,  page, position,)

    def set_page_header_image(self,  page, pixbuf,):
        if page : page = page._object
        else : page = c_void_p()
        if pixbuf : pixbuf = pixbuf._object
        else : pixbuf = c_void_p()

        libgtk3.gtk_assistant_set_page_header_image.argtypes = [c_void_p, _GtkWidget,_GdkPixbuf]
        
        libgtk3.gtk_assistant_set_page_header_image(self._object,  page, pixbuf,)

    def commit(self, ):

        libgtk3.gtk_assistant_commit.argtypes = [c_void_p]
        
        libgtk3.gtk_assistant_commit(self._object, )

    def set_page_side_image(self,  page, pixbuf,):
        if page : page = page._object
        else : page = c_void_p()
        if pixbuf : pixbuf = pixbuf._object
        else : pixbuf = c_void_p()

        libgtk3.gtk_assistant_set_page_side_image.argtypes = [c_void_p, _GtkWidget,_GdkPixbuf]
        
        libgtk3.gtk_assistant_set_page_side_image(self._object,  page, pixbuf,)

    def get_page_header_image(self,  page,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_get_page_header_image.restype = _GdkPixbuf
        libgtk3.gtk_assistant_get_page_header_image.argtypes = [c_void_p, _GtkWidget]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_assistant_get_page_header_image(self._object,  page,) or c_void_p())

    def add_action_widget(self,  child,):
        if child : child = child._object
        else : child = c_void_p()

        libgtk3.gtk_assistant_add_action_widget.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_assistant_add_action_widget(self._object,  child,)

    def get_current_page(self, ):

        libgtk3.gtk_assistant_get_current_page.restype = gint
        libgtk3.gtk_assistant_get_current_page.argtypes = [c_void_p]
        
        return libgtk3.gtk_assistant_get_current_page(self._object, )

    def set_forward_page_func(self,  page_func, data, destroy,):
        if page_func : page_func = page_func._object
        else : page_func = c_void_p()

        libgtk3.gtk_assistant_set_forward_page_func.argtypes = [c_void_p, GtkAssistantPageFunc,gpointer,GDestroyNotify]
        
        libgtk3.gtk_assistant_set_forward_page_func(self._object,  page_func, data, destroy,)

    def remove_page(self,  page_num,):

        libgtk3.gtk_assistant_remove_page.argtypes = [c_void_p, gint]
        
        libgtk3.gtk_assistant_remove_page(self._object,  page_num,)

    def previous_page(self, ):

        libgtk3.gtk_assistant_previous_page.argtypes = [c_void_p]
        
        libgtk3.gtk_assistant_previous_page(self._object, )

    def set_page_title(self,  page, title,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_set_page_title.argtypes = [c_void_p, _GtkWidget,c_char_p]
        
        libgtk3.gtk_assistant_set_page_title(self._object,  page, title,)

    def get_n_pages(self, ):

        libgtk3.gtk_assistant_get_n_pages.restype = gint
        libgtk3.gtk_assistant_get_n_pages.argtypes = [c_void_p]
        
        return libgtk3.gtk_assistant_get_n_pages(self._object, )

    def update_buttons_state(self, ):

        libgtk3.gtk_assistant_update_buttons_state.argtypes = [c_void_p]
        
        libgtk3.gtk_assistant_update_buttons_state(self._object, )

    def get_page_title(self,  page,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_get_page_title.restype = _gchar
        libgtk3.gtk_assistant_get_page_title.argtypes = [c_void_p, _GtkWidget]
        
        return libgtk3.gtk_assistant_get_page_title(self._object,  page,)

    def get_page_side_image(self,  page,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_get_page_side_image.restype = _GdkPixbuf
        libgtk3.gtk_assistant_get_page_side_image.argtypes = [c_void_p, _GtkWidget]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_assistant_get_page_side_image(self._object,  page,) or c_void_p())

    def prepend_page(self,  page,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_prepend_page.restype = gint
        libgtk3.gtk_assistant_prepend_page.argtypes = [c_void_p, _GtkWidget]
        
        return libgtk3.gtk_assistant_prepend_page(self._object,  page,)

    def get_page_complete(self,  page,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_get_page_complete.restype = gboolean
        libgtk3.gtk_assistant_get_page_complete.argtypes = [c_void_p, _GtkWidget]
        
        return libgtk3.gtk_assistant_get_page_complete(self._object,  page,)

    def get_nth_page(self,  page_num,):

        libgtk3.gtk_assistant_get_nth_page.restype = _GtkWidget
        libgtk3.gtk_assistant_get_nth_page.argtypes = [c_void_p, gint]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_assistant_get_nth_page(self._object,  page_num,) or c_void_p())

    def set_page_type(self,  page, type,):
        if page : page = page._object
        else : page = c_void_p()

        libgtk3.gtk_assistant_set_page_type.argtypes = [c_void_p, _GtkWidget,GtkAssistantPageType]
        
        libgtk3.gtk_assistant_set_page_type(self._object,  page, type,)

    def remove_action_widget(self,  child,):
        if child : child = child._object
        else : child = c_void_p()

        libgtk3.gtk_assistant_remove_action_widget.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_assistant_remove_action_widget(self._object,  child,)

