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
_gchar = c_void_p
"""Enumerations"""
WebKitWebNavigationReason = c_int

import _gobject_GObject
class WebKitWebNavigationAction( _gobject_GObject.GObject):
    """Class WebKitWebNavigationAction Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_original_uri(self, ):

        libwebkit3.webkit_web_navigation_action_get_original_uri.restype = _gchar
        libwebkit3.webkit_web_navigation_action_get_original_uri.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_navigation_action_get_original_uri(self._object, )

    def get_button(self, ):

        libwebkit3.webkit_web_navigation_action_get_button.restype = gint
        libwebkit3.webkit_web_navigation_action_get_button.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_navigation_action_get_button(self._object, )

    def get_target_frame(self, ):

        libwebkit3.webkit_web_navigation_action_get_target_frame.restype = _gchar
        libwebkit3.webkit_web_navigation_action_get_target_frame.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_navigation_action_get_target_frame(self._object, )

    def set_original_uri(self,  originalUri,):

        libwebkit3.webkit_web_navigation_action_set_original_uri.argtypes = [c_void_p, c_char_p]
        
        libwebkit3.webkit_web_navigation_action_set_original_uri(self._object,  originalUri,)

    def get_modifier_state(self, ):

        libwebkit3.webkit_web_navigation_action_get_modifier_state.restype = gint
        libwebkit3.webkit_web_navigation_action_get_modifier_state.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_navigation_action_get_modifier_state(self._object, )

    def get_reason(self, ):

        libwebkit3.webkit_web_navigation_action_get_reason.restype = WebKitWebNavigationReason
        libwebkit3.webkit_web_navigation_action_get_reason.argtypes = [c_void_p]
        
        return libwebkit3.webkit_web_navigation_action_get_reason(self._object, )

    def set_reason(self,  reason,):

        libwebkit3.webkit_web_navigation_action_set_reason.argtypes = [c_void_p, WebKitWebNavigationReason]
        
        libwebkit3.webkit_web_navigation_action_set_reason(self._object,  reason,)

