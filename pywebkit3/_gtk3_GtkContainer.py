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
__GParamSpec = c_void_p
_GtkAdjustment = c_void_p
__GtkWidget = c_void_p
__cairo_t = c_void_p
__GtkContainerClass = c_void_p
__GValue = c_void_p
_GList = c_void_p
_GParamSpec = c_void_p
__GObjectClass = c_void_p
__GList = c_void_p
__GtkAdjustment = c_void_p
_GtkWidget = c_void_p
_GtkWidgetPath = c_void_p
"""Enumerations"""

import _gtk3_GtkWidget
class GtkContainer( _gtk3_GtkWidget.GtkWidget):
    """Class GtkContainer Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def unset_focus_chain(self, ):

        libgtk3.gtk_container_unset_focus_chain.argtypes = [c_void_p]
        
        libgtk3.gtk_container_unset_focus_chain(self._object, )

    def add_with_properties(self,  widget, first_prop_name,*args ):
        if widget : widget = widget._object
        else : widget = c_void_p()


        def callit( widget, first_prop_name, *args ):
                libgtk3.gtk_container_add_with_properties.restype = None
                libgtk3.gtk_container_add_with_properties.argtypes = [c_void_p, c_void_p, _GtkWidget, c_char_p]
                for arg in args:
                     libgtk3.gtk_container_add_with_properties.argtypes.append(args[1])
                return libgtk3.gtk_container_add_with_properties(self._object, widget, first_prop_name, *args)
    
        return callit( widget, first_prop_name,*args )

    def child_notify(self,  child, child_property,):
        if child : child = child._object
        else : child = c_void_p()

        libgtk3.gtk_container_child_notify.argtypes = [c_void_p, _GtkWidget,c_char_p]
        
        libgtk3.gtk_container_child_notify(self._object,  child, child_property,)

    def propagate_draw(self,  child, cr,):
        if child : child = child._object
        else : child = c_void_p()
        if cr : cr = cr._object
        else : cr = c_void_p()

        libgtk3.gtk_container_propagate_draw.argtypes = [c_void_p, _GtkWidget,_cairo_t]
        
        libgtk3.gtk_container_propagate_draw(self._object,  child, cr,)

    def set_focus_hadjustment(self,  adjustment,):
        if adjustment : adjustment = adjustment._object
        else : adjustment = c_void_p()

        libgtk3.gtk_container_set_focus_hadjustment.argtypes = [c_void_p, _GtkAdjustment]
        
        libgtk3.gtk_container_set_focus_hadjustment(self._object,  adjustment,)

    def forall(self,  callback, callback_data,):
        if callback : callback = callback._object
        else : callback = c_void_p()

        libgtk3.gtk_container_forall.argtypes = [c_void_p, GtkCallback,gpointer]
        
        libgtk3.gtk_container_forall(self._object,  callback, callback_data,)

    def resize_children(self, ):

        libgtk3.gtk_container_resize_children.argtypes = [c_void_p]
        
        libgtk3.gtk_container_resize_children(self._object, )

    def child_set_property(self,  child, property_name, value,):
        if child : child = child._object
        else : child = c_void_p()
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.gtk_container_child_set_property.argtypes = [c_void_p, _GtkWidget,c_char_p,_GValue]
        
        libgtk3.gtk_container_child_set_property(self._object,  child, property_name, value,)

    def set_resize_mode(self,  resize_mode,):

        libgtk3.gtk_container_set_resize_mode.argtypes = [c_void_p, GtkResizeMode]
        
        libgtk3.gtk_container_set_resize_mode(self._object,  resize_mode,)

    def get_border_width(self, ):

        libgtk3.gtk_container_get_border_width.restype = guint
        libgtk3.gtk_container_get_border_width.argtypes = [c_void_p]
        
        return libgtk3.gtk_container_get_border_width(self._object, )

    def set_border_width(self,  border_width,):

        libgtk3.gtk_container_set_border_width.argtypes = [c_void_p, guint]
        
        libgtk3.gtk_container_set_border_width(self._object,  border_width,)

    def check_resize(self, ):

        libgtk3.gtk_container_check_resize.argtypes = [c_void_p]
        
        libgtk3.gtk_container_check_resize(self._object, )

    def child_get_property(self,  child, property_name, value,):
        if child : child = child._object
        else : child = c_void_p()
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.gtk_container_child_get_property.argtypes = [c_void_p, _GtkWidget,c_char_p,_GValue]
        
        libgtk3.gtk_container_child_get_property(self._object,  child, property_name, value,)

    def set_focus_chain(self,  focusable_widgets,):
        if focusable_widgets : focusable_widgets = focusable_widgets._object
        else : focusable_widgets = c_void_p()

        libgtk3.gtk_container_set_focus_chain.argtypes = [c_void_p, _GList]
        
        libgtk3.gtk_container_set_focus_chain(self._object,  focusable_widgets,)

    def class_handle_border_width(self,  klass,):
        if klass : klass = klass._object
        else : klass = c_void_p()

        libgtk3.gtk_container_class_handle_border_width.argtypes = [c_void_p, _GtkContainerClass]
        
        libgtk3.gtk_container_class_handle_border_width(self._object,  klass,)

    def get_focus_chain(self,  focusable_widgets,):
        if focusable_widgets : focusable_widgets = focusable_widgets._object
        else : focusable_widgets = c_void_p()

        libgtk3.gtk_container_get_focus_chain.restype = gboolean
        libgtk3.gtk_container_get_focus_chain.argtypes = [c_void_p, _GList]
        
        return libgtk3.gtk_container_get_focus_chain(self._object,  focusable_widgets,)

    def set_focus_child(self,  child,):
        if child : child = child._object
        else : child = c_void_p()

        libgtk3.gtk_container_set_focus_child.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_container_set_focus_child(self._object,  child,)

    def set_reallocate_redraws(self,  needs_redraws,):

        libgtk3.gtk_container_set_reallocate_redraws.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_container_set_reallocate_redraws(self._object,  needs_redraws,)

    def child_get(self,  child, first_prop_name,*args ):
        if child : child = child._object
        else : child = c_void_p()


        def callit( child, first_prop_name, *args ):
                libgtk3.gtk_container_child_get.restype = None
                libgtk3.gtk_container_child_get.argtypes = [c_void_p, c_void_p, _GtkWidget, c_char_p]
                for arg in args:
                     libgtk3.gtk_container_child_get.argtypes.append(args[1])
                return libgtk3.gtk_container_child_get(self._object, child, first_prop_name, *args)
    
        return callit( child, first_prop_name,*args )

    def get_path_for_child(self,  child,):
        if child : child = child._object
        else : child = c_void_p()

        libgtk3.gtk_container_get_path_for_child.restype = _GtkWidgetPath
        libgtk3.gtk_container_get_path_for_child.argtypes = [c_void_p, _GtkWidget]
        from pywebkit3.gtk3 import GtkWidgetPath
        return GtkWidgetPath(None, obj=libgtk3.gtk_container_get_path_for_child(self._object,  child,) or c_void_p())

    def foreach(self,  callback, callback_data,):
        if callback : callback = callback._object
        else : callback = c_void_p()

        libgtk3.gtk_container_foreach.argtypes = [c_void_p, GtkCallback,gpointer]
        
        libgtk3.gtk_container_foreach(self._object,  callback, callback_data,)

    def class_install_child_property(self,  cclass, property_id, pspec,):
        if cclass : cclass = cclass._object
        else : cclass = c_void_p()
        if pspec : pspec = pspec._object
        else : pspec = c_void_p()

        libgtk3.gtk_container_class_install_child_property.argtypes = [c_void_p, _GtkContainerClass,guint,_GParamSpec]
        
        libgtk3.gtk_container_class_install_child_property(self._object,  cclass, property_id, pspec,)

    def add(self,  widget,):
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_container_add.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_container_add(self._object,  widget,)

    def get_resize_mode(self, ):

        libgtk3.gtk_container_get_resize_mode.restype = GtkResizeMode
        libgtk3.gtk_container_get_resize_mode.argtypes = [c_void_p]
        
        return libgtk3.gtk_container_get_resize_mode(self._object, )

    def get_focus_vadjustment(self, ):

        libgtk3.gtk_container_get_focus_vadjustment.restype = _GtkAdjustment
        libgtk3.gtk_container_get_focus_vadjustment.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkAdjustment
        return GtkAdjustment(None,None, obj=libgtk3.gtk_container_get_focus_vadjustment(self._object, ) or c_void_p())

    def set_focus_vadjustment(self,  adjustment,):
        if adjustment : adjustment = adjustment._object
        else : adjustment = c_void_p()

        libgtk3.gtk_container_set_focus_vadjustment.argtypes = [c_void_p, _GtkAdjustment]
        
        libgtk3.gtk_container_set_focus_vadjustment(self._object,  adjustment,)

    def child_type(self, ):

        libgtk3.gtk_container_child_type.restype = GType
        libgtk3.gtk_container_child_type.argtypes = [c_void_p]
        
        return libgtk3.gtk_container_child_type(self._object, )

    def remove(self,  widget,):
        if widget : widget = widget._object
        else : widget = c_void_p()

        libgtk3.gtk_container_remove.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_container_remove(self._object,  widget,)

    def child_set(self,  child, first_prop_name,*args ):
        if child : child = child._object
        else : child = c_void_p()


        def callit( child, first_prop_name, *args ):
                libgtk3.gtk_container_child_set.restype = None
                libgtk3.gtk_container_child_set.argtypes = [c_void_p, c_void_p, _GtkWidget, c_char_p]
                for arg in args:
                     libgtk3.gtk_container_child_set.argtypes.append(args[1])
                return libgtk3.gtk_container_child_set(self._object, child, first_prop_name, *args)
    
        return callit( child, first_prop_name,*args )

    def get_focus_hadjustment(self, ):

        libgtk3.gtk_container_get_focus_hadjustment.restype = _GtkAdjustment
        libgtk3.gtk_container_get_focus_hadjustment.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkAdjustment
        return GtkAdjustment(None, obj=libgtk3.gtk_container_get_focus_hadjustment(self._object, ) or c_void_p())

    def get_children(self, ):

        libgtk3.gtk_container_get_children.restype = _GList
        libgtk3.gtk_container_get_children.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.gtk_container_get_children(self._object, ) or c_void_p())

    def get_focus_child(self, ):

        libgtk3.gtk_container_get_focus_child.restype = _GtkWidget
        libgtk3.gtk_container_get_focus_child.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_container_get_focus_child(self._object, ) or c_void_p())

    @staticmethod
    def class_list_child_properties( cclass, n_properties,):
        if cclass : cclass = cclass._object
        else : cclass = c_void_p()
        if n_properties : n_properties = n_properties._object
        else : n_properties = c_void_p()
        libgtk3.gtk_container_class_list_child_properties.restype = _GParamSpec
        libgtk3.gtk_container_class_list_child_properties.argtypes = [_GObjectClass,POITNER(guint)]
        return libgtk3.gtk_container_class_list_child_properties(cclass, n_properties, )

    @staticmethod
    def class_find_child_property( cclass, property_name,):
        if cclass : cclass = cclass._object
        else : cclass = c_void_p()
        libgtk3.gtk_container_class_find_child_property.restype = _GParamSpec
        libgtk3.gtk_container_class_find_child_property.argtypes = [_GObjectClass,c_char_p]
        return libgtk3.gtk_container_class_find_child_property(cclass, property_name, )

