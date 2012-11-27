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
__GtkRcStyle = c_void_p
__GdkGeometry = c_void_p
_GdkPixbuf = c_void_p
__GtkRequisition = c_void_p
_GtkRcStyle = c_void_p
__GtkRegionFlags = c_void_p
_GdkEvent = c_void_p
_GtkWindow = c_void_p
__cairo_font_options_t = c_void_p
__GdkAtom = c_void_p
__GdkTimeCoord = c_void_p
__GtkWidgetPath = c_void_p
__GClosure = c_void_p
_GdkDisplay = c_void_p
__GtkStyleProvider = c_void_p
_GScanner = c_void_p
_PangoFont = c_void_p
_GtkStyleContext = c_void_p
__GtkTextBuffer = c_void_p
_guchar = c_void_p
_GdkAppLaunchContext = c_void_p
__GObject = c_void_p
__PangoLayout = c_void_p
__GParamSpec = c_void_p
__PangoAttrIterator = c_void_p
__GtkWindow = c_void_p
_GtkSelectionData = c_void_p
_GtkWindowGroup = c_void_p
__PangoContext = c_void_p
__GtkPathPriorityType = c_void_p
__GtkSettings = c_void_p
__PangoFontMap = c_void_p
__PangoAttrList = c_void_p
_PangoMatrix = c_void_p
_GtkApplication = c_void_p
__PangoAnalysis = c_void_p
_PangoFontDescription = c_void_p
__GdkCursor = c_void_p
_guint8 = c_void_p
__GScanner = c_void_p
__GtkWidgetClass = c_void_p
__GdkEventKey = c_void_p
__GdkDisplay = c_void_p
_GtkWidgetPath = c_void_p
_GdkScreen = c_void_p
_PangoFontMetrics = c_void_p
_GdkVisual = c_void_p
_PangoFontMap = c_void_p
_GSList = c_void_p
_GtkWidget = c_void_p
__GdkWindow = c_void_p
__PangoFontFamily = c_void_p
__cairo_region_t = c_void_p
_PangoFontset = c_void_p
_GdkWindow = c_void_p
__PangoFontDescription = c_void_p
__GtkBorder = c_void_p
__GError = c_void_p
__PangoCoverage = c_void_p
__cairo_t = c_void_p
__GWeakRef = c_void_p
__GdkVisual = c_void_p
_GdkDevice = c_void_p
_GList = c_void_p
__GtkAccelGroup = c_void_p
_GObject = c_void_p
_GtkIconSet = c_void_p
__GtkAllocation = c_void_p
__GtkWidget = c_void_p
_gchar = c_void_p
__GValue = c_void_p
_GdkDeviceManager = c_void_p
_GdkCursor = c_void_p
__PangoMatrix = c_void_p
_PangoContext = c_void_p
__GList = c_void_p
_PangoCoverage = c_void_p
_GParamSpec = c_void_p
__PangoRectangle = c_void_p
__GtkIconSource = c_void_p
_char = c_void_p
__PangoGlyphString = c_void_p
__GObjectClass = c_void_p
__GSList = c_void_p
__GdkRGBA = c_void_p
__GdkWindowAttr = c_void_p
__GdkColor = c_void_p
__GdkRectangle = c_void_p
__PangoLanguage = c_void_p
__GdkWMDecoration = c_void_p
__PangoLogAttr = c_void_p
_PangoLayout = c_void_p
_GtkStyle = c_void_p
__GParameter = c_void_p
__GtkStyle = c_void_p
__GIcon = c_void_p
__cairo_pattern_t = c_void_p
__GdkPixbuf = c_void_p
_GtkSettings = c_void_p
__GtkTargetEntry = c_void_p
__GtkApplication = c_void_p
_GtkClipboard = c_void_p
__GdkScreen = c_void_p
_PangoLanguage = c_void_p
__GdkDevice = c_void_p
"""Enumerations"""
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkIconSize = c_int
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
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GdkCursorType = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int

class GObject( object):
    """Class GObject Constructors"""
    def __init__( self, object_type, first_property_name,  obj=None, *args):
        if obj: self._object = obj
        else:
            libgtk3.g_object_new.restype = c_void_p

        libgtk3.g_object_new.argtypes = [GType,c_char_p,]
        self._object = libgtk3.g_object_new(object_type, first_property_name, *args )

    """Methods"""
    def add_toggle_ref(self,  notify, data,):

        libgtk3.g_object_add_toggle_ref.argtypes = [c_void_p, GToggleNotify,gpointer]
        
        libgtk3.g_object_add_toggle_ref(self._object,  notify, data,)

    def set_qdata_full(self,  quark, data, destroy,):

        libgtk3.g_object_set_qdata_full.argtypes = [c_void_p, GQuark,gpointer,GDestroyNotify]
        
        libgtk3.g_object_set_qdata_full(self._object,  quark, data, destroy,)

    def weak_unref(self,  notify, data,):

        libgtk3.g_object_weak_unref.argtypes = [c_void_p, GWeakNotify,gpointer]
        
        libgtk3.g_object_weak_unref(self._object,  notify, data,)

    def steal_data(self,  key,):

        libgtk3.g_object_steal_data.restype = gpointer
        libgtk3.g_object_steal_data.argtypes = [c_void_p, c_char_p]
        
        return libgtk3.g_object_steal_data(self._object,  key,)

    def run_dispose(self, ):

        libgtk3.g_object_run_dispose.argtypes = [c_void_p]
        
        libgtk3.g_object_run_dispose(self._object, )

    def set_qdata(self,  quark, data,):

        libgtk3.g_object_set_qdata.argtypes = [c_void_p, GQuark,gpointer]
        
        libgtk3.g_object_set_qdata(self._object,  quark, data,)

    def g_clear_object(self, ):

        libgtk3.g_clear_object.argtypes = [c_void_p]
        
        libgtk3.g_clear_object(self._object, )

    def set_data(self,  key, data,):

        libgtk3.g_object_set_data.argtypes = [c_void_p, c_char_p,gpointer]
        
        libgtk3.g_object_set_data(self._object,  key, data,)

    def steal_qdata(self,  quark,):

        libgtk3.g_object_steal_qdata.restype = gpointer
        libgtk3.g_object_steal_qdata.argtypes = [c_void_p, GQuark]
        
        return libgtk3.g_object_steal_qdata(self._object,  quark,)

    def notify(self,  property_name,):

        libgtk3.g_object_notify.argtypes = [c_void_p, c_char_p]
        
        libgtk3.g_object_notify(self._object,  property_name,)

    def class_install_properties(self,  oclass, n_pspecs, pspecs,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()
        if pspecs : pspecs = pspecs._object
        else : pspecs = c_void_p()

        libgtk3.g_object_class_install_properties.argtypes = [c_void_p, _GObjectClass,guint,_GParamSpec]
        
        libgtk3.g_object_class_install_properties(self._object,  oclass, n_pspecs, pspecs,)

    def replace_data(self,  key, oldval, newval, destroy, old_destroy,):
        if old_destroy : old_destroy = old_destroy._object
        else : old_destroy = c_void_p()

        libgtk3.g_object_replace_data.restype = gboolean
        libgtk3.g_object_replace_data.argtypes = [c_void_p, c_char_p,gpointer,gpointer,GDestroyNotify,POITNER(GDestroyNotify)]
        
        return libgtk3.g_object_replace_data(self._object,  key, oldval, newval, destroy, old_destroy,)

    def interface_install_property(self,  g_iface, pspec,):
        if pspec : pspec = pspec._object
        else : pspec = c_void_p()

        libgtk3.g_object_interface_install_property.argtypes = [c_void_p, gpointer,_GParamSpec]
        
        libgtk3.g_object_interface_install_property(self._object,  g_iface, pspec,)

    def get_qdata(self,  quark,):

        libgtk3.g_object_get_qdata.restype = gpointer
        libgtk3.g_object_get_qdata.argtypes = [c_void_p, GQuark]
        
        return libgtk3.g_object_get_qdata(self._object,  quark,)

    def set_property(self,  property_name, value,):
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.g_object_set_property.argtypes = [c_void_p, c_char_p,_GValue]
        
        libgtk3.g_object_set_property(self._object,  property_name, value,)

    def set(self,  object, first_property_name,*args ):


        def callit( object, first_property_name, *args ):
                libgtk3.g_object_set.restype = None
                libgtk3.g_object_set.argtypes = [c_void_p, c_void_p, gpointer, c_char_p]
                for arg in args:
                     libgtk3.g_object_set.argtypes.append(args[1])
                return libgtk3.g_object_set(self._object, object, first_property_name, *args)
    
        return callit( object, first_property_name,*args )

    def disconnect(self,  object, signal_spec,*args ):


        def callit( object, signal_spec, *args ):
                libgtk3.g_object_disconnect.restype = None
                libgtk3.g_object_disconnect.argtypes = [c_void_p, c_void_p, gpointer, c_char_p]
                for arg in args:
                     libgtk3.g_object_disconnect.argtypes.append(args[1])
                return libgtk3.g_object_disconnect(self._object, object, signal_spec, *args)
    
        return callit( object, signal_spec,*args )

    def weak_ref(self,  notify, data,):

        libgtk3.g_object_weak_ref.argtypes = [c_void_p, GWeakNotify,gpointer]
        
        libgtk3.g_object_weak_ref(self._object,  notify, data,)

    def add_weak_pointer(self,  weak_pointer_location,):
        if weak_pointer_location : weak_pointer_location = weak_pointer_location._object
        else : weak_pointer_location = c_void_p()

        libgtk3.g_object_add_weak_pointer.argtypes = [c_void_p, POITNER(gpointer)]
        
        libgtk3.g_object_add_weak_pointer(self._object,  weak_pointer_location,)

    def remove_weak_pointer(self,  weak_pointer_location,):
        if weak_pointer_location : weak_pointer_location = weak_pointer_location._object
        else : weak_pointer_location = c_void_p()

        libgtk3.g_object_remove_weak_pointer.argtypes = [c_void_p, POITNER(gpointer)]
        
        libgtk3.g_object_remove_weak_pointer(self._object,  weak_pointer_location,)

    def class_install_property(self,  oclass, property_id, pspec,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()
        if pspec : pspec = pspec._object
        else : pspec = c_void_p()

        libgtk3.g_object_class_install_property.argtypes = [c_void_p, _GObjectClass,guint,_GParamSpec]
        
        libgtk3.g_object_class_install_property(self._object,  oclass, property_id, pspec,)

    def freeze_notify(self, ):

        libgtk3.g_object_freeze_notify.argtypes = [c_void_p]
        
        libgtk3.g_object_freeze_notify(self._object, )

    def notify_by_pspec(self,  pspec,):
        if pspec : pspec = pspec._object
        else : pspec = c_void_p()

        libgtk3.g_object_notify_by_pspec.argtypes = [c_void_p, _GParamSpec]
        
        libgtk3.g_object_notify_by_pspec(self._object,  pspec,)

    def remove_toggle_ref(self,  notify, data,):

        libgtk3.g_object_remove_toggle_ref.argtypes = [c_void_p, GToggleNotify,gpointer]
        
        libgtk3.g_object_remove_toggle_ref(self._object,  notify, data,)

    def thaw_notify(self, ):

        libgtk3.g_object_thaw_notify.argtypes = [c_void_p]
        
        libgtk3.g_object_thaw_notify(self._object, )

    def dup_qdata(self,  quark, dup_func, user_data,):

        libgtk3.g_object_dup_qdata.restype = gpointer
        libgtk3.g_object_dup_qdata.argtypes = [c_void_p, GQuark,GDuplicateFunc,gpointer]
        
        return libgtk3.g_object_dup_qdata(self._object,  quark, dup_func, user_data,)

    def unref(self,  object,):

        libgtk3.g_object_unref.argtypes = [c_void_p, gpointer]
        
        libgtk3.g_object_unref(self._object,  object,)

    def get(self,  object, first_property_name,*args ):


        def callit( object, first_property_name, *args ):
                libgtk3.g_object_get.restype = None
                libgtk3.g_object_get.argtypes = [c_void_p, c_void_p, gpointer, c_char_p]
                for arg in args:
                     libgtk3.g_object_get.argtypes.append(args[1])
                return libgtk3.g_object_get(self._object, object, first_property_name, *args)
    
        return callit( object, first_property_name,*args )

    def g_weak_ref_set(self,  weak_ref, object,):
        if weak_ref : weak_ref = weak_ref._object
        else : weak_ref = c_void_p()

        libgtk3.g_weak_ref_set.argtypes = [c_void_p, _GWeakRef,gpointer]
        
        libgtk3.g_weak_ref_set(self._object,  weak_ref, object,)

    def dup_data(self,  key, dup_func, user_data,):

        libgtk3.g_object_dup_data.restype = gpointer
        libgtk3.g_object_dup_data.argtypes = [c_void_p, c_char_p,GDuplicateFunc,gpointer]
        
        return libgtk3.g_object_dup_data(self._object,  key, dup_func, user_data,)

    def replace_qdata(self,  quark, oldval, newval, destroy, old_destroy,):
        if old_destroy : old_destroy = old_destroy._object
        else : old_destroy = c_void_p()

        libgtk3.g_object_replace_qdata.restype = gboolean
        libgtk3.g_object_replace_qdata.argtypes = [c_void_p, GQuark,gpointer,gpointer,GDestroyNotify,POITNER(GDestroyNotify)]
        
        return libgtk3.g_object_replace_qdata(self._object,  quark, oldval, newval, destroy, old_destroy,)

    def get_data(self,  key,):

        libgtk3.g_object_get_data.restype = gpointer
        libgtk3.g_object_get_data.argtypes = [c_void_p, c_char_p]
        
        return libgtk3.g_object_get_data(self._object,  key,)

    def get_property(self,  property_name, value,):
        if value : value = value._object
        else : value = c_void_p()

        libgtk3.g_object_get_property.argtypes = [c_void_p, c_char_p,_GValue]
        
        libgtk3.g_object_get_property(self._object,  property_name, value,)

    def watch_closure(self,  closure,):
        if closure : closure = closure._object
        else : closure = c_void_p()

        libgtk3.g_object_watch_closure.argtypes = [c_void_p, _GClosure]
        
        libgtk3.g_object_watch_closure(self._object,  closure,)

    def g_weak_ref_clear(self,  weak_ref,):
        if weak_ref : weak_ref = weak_ref._object
        else : weak_ref = c_void_p()

        libgtk3.g_weak_ref_clear.argtypes = [c_void_p, _GWeakRef]
        
        libgtk3.g_weak_ref_clear(self._object,  weak_ref,)

    def set_data_full(self,  key, data, destroy,):

        libgtk3.g_object_set_data_full.argtypes = [c_void_p, c_char_p,gpointer,GDestroyNotify]
        
        libgtk3.g_object_set_data_full(self._object,  key, data, destroy,)

    def force_floating(self, ):

        libgtk3.g_object_force_floating.argtypes = [c_void_p]
        
        libgtk3.g_object_force_floating(self._object, )

    def class_override_property(self,  oclass, property_id, name,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()

        libgtk3.g_object_class_override_property.argtypes = [c_void_p, _GObjectClass,guint,c_char_p]
        
        libgtk3.g_object_class_override_property(self._object,  oclass, property_id, name,)

    @staticmethod
    def is_floating( object,):
        libgtk3.g_object_is_floating.restype = gboolean
        libgtk3.g_object_is_floating.argtypes = [gpointer]
        return libgtk3.g_object_is_floating(object, )

    @staticmethod
    def class_find_property( oclass, property_name,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()
        libgtk3.g_object_class_find_property.restype = _GParamSpec
        libgtk3.g_object_class_find_property.argtypes = [_GObjectClass,c_char_p]
        return libgtk3.g_object_class_find_property(oclass, property_name, )

    @staticmethod
    def interface_list_properties( g_iface, n_properties_p,):
        if n_properties_p : n_properties_p = n_properties_p._object
        else : n_properties_p = c_void_p()
        libgtk3.g_object_interface_list_properties.restype = _GParamSpec
        libgtk3.g_object_interface_list_properties.argtypes = [gpointer,POITNER(guint)]
        return libgtk3.g_object_interface_list_properties(g_iface, n_properties_p, )

    @staticmethod
    def newv( object_type, n_parameters, parameters,):
        if parameters : parameters = parameters._object
        else : parameters = c_void_p()
        libgtk3.g_object_newv.restype = gpointer
        libgtk3.g_object_newv.argtypes = [GType,guint,_GParameter]
        return libgtk3.g_object_newv(object_type, n_parameters, parameters, )

    @staticmethod
    def pspec():
        libgtk3.pspec.restype = property_id,
        return libgtk3.pspec()

    @staticmethod
    def class_list_properties( oclass, n_properties,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()
        if n_properties : n_properties = n_properties._object
        else : n_properties = c_void_p()
        libgtk3.g_object_class_list_properties.restype = _GParamSpec
        libgtk3.g_object_class_list_properties.argtypes = [_GObjectClass,POITNER(guint)]
        return libgtk3.g_object_class_list_properties(oclass, n_properties, )

    @staticmethod
    def ref( object,):
        libgtk3.g_object_ref.restype = gpointer
        libgtk3.g_object_ref.argtypes = [gpointer]
        return libgtk3.g_object_ref(object, )

    @staticmethod
    def interface_find_property( g_iface, property_name,):
        libgtk3.g_object_interface_find_property.restype = _GParamSpec
        libgtk3.g_object_interface_find_property.argtypes = [gpointer,c_char_p]
        return libgtk3.g_object_interface_find_property(g_iface, property_name, )

    @staticmethod
    def g_weak_ref_get( weak_ref,):
        if weak_ref : weak_ref = weak_ref._object
        else : weak_ref = c_void_p()
        libgtk3.g_weak_ref_get.restype = gpointer
        libgtk3.g_weak_ref_get.argtypes = [_GWeakRef]
        return libgtk3.g_weak_ref_get(weak_ref, )

    @staticmethod
    def ref_sink( object,):
        libgtk3.g_object_ref_sink.restype = gpointer
        libgtk3.g_object_ref_sink.argtypes = [gpointer]
        return libgtk3.g_object_ref_sink(object, )

    @staticmethod
    def connect( object, signal_spec,*args ):
        libgtk3.g_object_connect.restype = gpointer
        libgtk3.g_object_connect.argtypes = [gpointer,c_char_p,]
        return libgtk3.g_object_connect(object, signal_spec, *args)

