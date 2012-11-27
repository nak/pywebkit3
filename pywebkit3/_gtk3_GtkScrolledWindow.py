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
__GtkAdjustment = c_void_p
_GtkAdjustment = c_void_p
_GtkWidget = c_void_p
__GtkWidget = c_void_p
"""Enumerations"""

import _gtk3_GtkBin
class GtkScrolledWindow( _gtk3_GtkBin.GtkBin):
    """Class GtkScrolledWindow Constructors"""
    def __init__( self, hadjustment, vadjustment,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_scrolled_window_new.restype = c_void_p
        if hadjustment : hadjustment = hadjustment._object
        else : hadjustment = c_void_p()
        if vadjustment : vadjustment = vadjustment._object
        else : vadjustment = c_void_p()

        libgtk3.gtk_scrolled_window_new.argtypes = [_GtkAdjustment,_GtkAdjustment]
        self._object = libgtk3.gtk_scrolled_window_new(hadjustment, vadjustment, )

    """Methods"""
    def get_shadow_type(self, ):

        libgtk3.gtk_scrolled_window_get_shadow_type.restype = GtkShadowType
        libgtk3.gtk_scrolled_window_get_shadow_type.argtypes = [c_void_p]
        
        return libgtk3.gtk_scrolled_window_get_shadow_type(self._object, )

    def get_min_content_height(self, ):

        libgtk3.gtk_scrolled_window_get_min_content_height.restype = gint
        libgtk3.gtk_scrolled_window_get_min_content_height.argtypes = [c_void_p]
        
        return libgtk3.gtk_scrolled_window_get_min_content_height(self._object, )

    def get_hscrollbar(self, ):

        libgtk3.gtk_scrolled_window_get_hscrollbar.restype = _GtkWidget
        libgtk3.gtk_scrolled_window_get_hscrollbar.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_scrolled_window_get_hscrollbar(self._object, ) or c_void_p())

    def get_placement(self, ):

        libgtk3.gtk_scrolled_window_get_placement.restype = GtkCornerType
        libgtk3.gtk_scrolled_window_get_placement.argtypes = [c_void_p]
        
        return libgtk3.gtk_scrolled_window_get_placement(self._object, )

    def set_min_content_height(self,  height,):

        libgtk3.gtk_scrolled_window_set_min_content_height.argtypes = [c_void_p, gint]
        
        libgtk3.gtk_scrolled_window_set_min_content_height(self._object,  height,)

    def set_min_content_width(self,  width,):

        libgtk3.gtk_scrolled_window_set_min_content_width.argtypes = [c_void_p, gint]
        
        libgtk3.gtk_scrolled_window_set_min_content_width(self._object,  width,)

    def set_shadow_type(self,  type,):

        libgtk3.gtk_scrolled_window_set_shadow_type.argtypes = [c_void_p, GtkShadowType]
        
        libgtk3.gtk_scrolled_window_set_shadow_type(self._object,  type,)

    def add_with_viewport(self,  child,):
        if child : child = child._object
        else : child = c_void_p()

        libgtk3.gtk_scrolled_window_add_with_viewport.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_scrolled_window_add_with_viewport(self._object,  child,)

    def get_vscrollbar(self, ):

        libgtk3.gtk_scrolled_window_get_vscrollbar.restype = _GtkWidget
        libgtk3.gtk_scrolled_window_get_vscrollbar.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_scrolled_window_get_vscrollbar(self._object, ) or c_void_p())

    def set_placement(self,  window_placement,):

        libgtk3.gtk_scrolled_window_set_placement.argtypes = [c_void_p, GtkCornerType]
        
        libgtk3.gtk_scrolled_window_set_placement(self._object,  window_placement,)

    def set_hadjustment(self,  hadjustment,):
        if hadjustment : hadjustment = hadjustment._object
        else : hadjustment = c_void_p()

        libgtk3.gtk_scrolled_window_set_hadjustment.argtypes = [c_void_p, _GtkAdjustment]
        
        libgtk3.gtk_scrolled_window_set_hadjustment(self._object,  hadjustment,)

    def get_policy(self,  hscrollbar_policy, vscrollbar_policy,):
        if hscrollbar_policy : hscrollbar_policy = hscrollbar_policy._object
        else : hscrollbar_policy = c_void_p()
        if vscrollbar_policy : vscrollbar_policy = vscrollbar_policy._object
        else : vscrollbar_policy = c_void_p()

        libgtk3.gtk_scrolled_window_get_policy.argtypes = [c_void_p, POITNER(GtkPolicyType),POITNER(GtkPolicyType)]
        
        libgtk3.gtk_scrolled_window_get_policy(self._object,  hscrollbar_policy, vscrollbar_policy,)

    def get_vadjustment(self, ):

        libgtk3.gtk_scrolled_window_get_vadjustment.restype = _GtkAdjustment
        libgtk3.gtk_scrolled_window_get_vadjustment.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkAdjustment
        return GtkAdjustment(None,None, obj=libgtk3.gtk_scrolled_window_get_vadjustment(self._object, ) or c_void_p())

    def get_min_content_width(self, ):

        libgtk3.gtk_scrolled_window_get_min_content_width.restype = gint
        libgtk3.gtk_scrolled_window_get_min_content_width.argtypes = [c_void_p]
        
        return libgtk3.gtk_scrolled_window_get_min_content_width(self._object, )

    def set_vadjustment(self,  vadjustment,):
        if vadjustment : vadjustment = vadjustment._object
        else : vadjustment = c_void_p()

        libgtk3.gtk_scrolled_window_set_vadjustment.argtypes = [c_void_p, _GtkAdjustment]
        
        libgtk3.gtk_scrolled_window_set_vadjustment(self._object,  vadjustment,)

    def unset_placement(self, ):

        libgtk3.gtk_scrolled_window_unset_placement.argtypes = [c_void_p]
        
        libgtk3.gtk_scrolled_window_unset_placement(self._object, )

    def get_hadjustment(self, ):

        libgtk3.gtk_scrolled_window_get_hadjustment.restype = _GtkAdjustment
        libgtk3.gtk_scrolled_window_get_hadjustment.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkAdjustment
        return GtkAdjustment(None, obj=libgtk3.gtk_scrolled_window_get_hadjustment(self._object, ) or c_void_p())

    def set_policy(self,  hscrollbar_policy, vscrollbar_policy,):

        libgtk3.gtk_scrolled_window_set_policy.argtypes = [c_void_p, GtkPolicyType,GtkPolicyType]
        
        libgtk3.gtk_scrolled_window_set_policy(self._object,  hscrollbar_policy, vscrollbar_policy,)

