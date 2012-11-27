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
from gobject_types import *
    
    
"""Derived Pointer Types"""
__GParamSpec = c_void_p
__GWeakRef = c_void_p
_GParamSpec = c_void_p
__GObjectClass = c_void_p
__GValue = c_void_p
__GClosure = c_void_p
__GParameter = c_void_p
_GObject = c_void_p
_GValue = c_void_p
"""Enumerations"""

class GObject( object):
    """Class GObject Constructors"""
    def __init__( self, object_type, first_property_name,  obj=None, *args):
        if obj: self._object = obj
        else:
            libgobject.g_object_new.restype = c_void_p

        libgobject.g_object_new.argtypes = [GType,c_char_p,]
        self._object = libgobject.g_object_new(object_type, first_property_name, *args )

    """Methods"""
    def add_toggle_ref(self,  notify, data,):

        libgobject.g_object_add_toggle_ref.argtypes = [c_void_p, GToggleNotify,gpointer]
        
        libgobject.g_object_add_toggle_ref(self._object,  notify, data,)

    def set_qdata_full(self,  quark, data, destroy,):

        libgobject.g_object_set_qdata_full.argtypes = [c_void_p, GQuark,gpointer,GDestroyNotify]
        
        libgobject.g_object_set_qdata_full(self._object,  quark, data, destroy,)

    def weak_unref(self,  notify, data,):

        libgobject.g_object_weak_unref.argtypes = [c_void_p, GWeakNotify,gpointer]
        
        libgobject.g_object_weak_unref(self._object,  notify, data,)

    def steal_data(self,  key,):

        libgobject.g_object_steal_data.restype = gpointer
        libgobject.g_object_steal_data.argtypes = [c_void_p, c_char_p]
        
        return libgobject.g_object_steal_data(self._object,  key,)

    def run_dispose(self, ):

        libgobject.g_object_run_dispose.argtypes = [c_void_p]
        
        libgobject.g_object_run_dispose(self._object, )

    def set_qdata(self,  quark, data,):

        libgobject.g_object_set_qdata.argtypes = [c_void_p, GQuark,gpointer]
        
        libgobject.g_object_set_qdata(self._object,  quark, data,)

    def g_clear_object(self, ):

        libgobject.g_clear_object.argtypes = [c_void_p]
        
        libgobject.g_clear_object(self._object, )

    def set_data(self,  key, data,):

        libgobject.g_object_set_data.argtypes = [c_void_p, c_char_p,gpointer]
        
        libgobject.g_object_set_data(self._object,  key, data,)

    def steal_qdata(self,  quark,):

        libgobject.g_object_steal_qdata.restype = gpointer
        libgobject.g_object_steal_qdata.argtypes = [c_void_p, GQuark]
        
        return libgobject.g_object_steal_qdata(self._object,  quark,)

    def notify(self,  property_name,):

        libgobject.g_object_notify.argtypes = [c_void_p, c_char_p]
        
        libgobject.g_object_notify(self._object,  property_name,)

    def class_install_properties(self,  oclass, n_pspecs, pspecs,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()
        if pspecs : pspecs = pspecs._object
        else : pspecs = c_void_p()

        libgobject.g_object_class_install_properties.argtypes = [c_void_p, _GObjectClass,guint,_GParamSpec]
        
        libgobject.g_object_class_install_properties(self._object,  oclass, n_pspecs, pspecs,)

    def replace_data(self,  key, oldval, newval, destroy, old_destroy,):
        if old_destroy : old_destroy = old_destroy._object
        else : old_destroy = c_void_p()

        libgobject.g_object_replace_data.restype = gboolean
        libgobject.g_object_replace_data.argtypes = [c_void_p, c_char_p,gpointer,gpointer,GDestroyNotify,POITNER(GDestroyNotify)]
        
        return libgobject.g_object_replace_data(self._object,  key, oldval, newval, destroy, old_destroy,)

    def interface_install_property(self,  g_iface, pspec,):
        if pspec : pspec = pspec._object
        else : pspec = c_void_p()

        libgobject.g_object_interface_install_property.argtypes = [c_void_p, gpointer,_GParamSpec]
        
        libgobject.g_object_interface_install_property(self._object,  g_iface, pspec,)

    def get_qdata(self,  quark,):

        libgobject.g_object_get_qdata.restype = gpointer
        libgobject.g_object_get_qdata.argtypes = [c_void_p, GQuark]
        
        return libgobject.g_object_get_qdata(self._object,  quark,)

    def set_property(self,  property_name, value,):
        if value : value = value._object
        else : value = c_void_p()

        libgobject.g_object_set_property.argtypes = [c_void_p, c_char_p,_GValue]
        
        libgobject.g_object_set_property(self._object,  property_name, value,)

    def set(self,  object, first_property_name,*args ):


        def callit( object, first_property_name, *args ):
                libgobject.g_object_set.restype = None
                libgobject.g_object_set.argtypes = [c_void_p, c_void_p, gpointer, c_char_p]
                for arg in args:
                     libgobject.g_object_set.argtypes.append(args[1])
                return libgobject.g_object_set(self._object, object, first_property_name, *args)
    
        return callit( object, first_property_name,*args )

    def disconnect(self,  object, signal_spec,*args ):


        def callit( object, signal_spec, *args ):
                libgobject.g_object_disconnect.restype = None
                libgobject.g_object_disconnect.argtypes = [c_void_p, c_void_p, gpointer, c_char_p]
                for arg in args:
                     libgobject.g_object_disconnect.argtypes.append(args[1])
                return libgobject.g_object_disconnect(self._object, object, signal_spec, *args)
    
        return callit( object, signal_spec,*args )

    def weak_ref(self,  notify, data,):

        libgobject.g_object_weak_ref.argtypes = [c_void_p, GWeakNotify,gpointer]
        
        libgobject.g_object_weak_ref(self._object,  notify, data,)

    def add_weak_pointer(self,  weak_pointer_location,):
        if weak_pointer_location : weak_pointer_location = weak_pointer_location._object
        else : weak_pointer_location = c_void_p()

        libgobject.g_object_add_weak_pointer.argtypes = [c_void_p, POITNER(gpointer)]
        
        libgobject.g_object_add_weak_pointer(self._object,  weak_pointer_location,)

    def remove_weak_pointer(self,  weak_pointer_location,):
        if weak_pointer_location : weak_pointer_location = weak_pointer_location._object
        else : weak_pointer_location = c_void_p()

        libgobject.g_object_remove_weak_pointer.argtypes = [c_void_p, POITNER(gpointer)]
        
        libgobject.g_object_remove_weak_pointer(self._object,  weak_pointer_location,)

    def class_install_property(self,  oclass, property_id, pspec,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()
        if pspec : pspec = pspec._object
        else : pspec = c_void_p()

        libgobject.g_object_class_install_property.argtypes = [c_void_p, _GObjectClass,guint,_GParamSpec]
        
        libgobject.g_object_class_install_property(self._object,  oclass, property_id, pspec,)

    def freeze_notify(self, ):

        libgobject.g_object_freeze_notify.argtypes = [c_void_p]
        
        libgobject.g_object_freeze_notify(self._object, )

    def notify_by_pspec(self,  pspec,):
        if pspec : pspec = pspec._object
        else : pspec = c_void_p()

        libgobject.g_object_notify_by_pspec.argtypes = [c_void_p, _GParamSpec]
        
        libgobject.g_object_notify_by_pspec(self._object,  pspec,)

    def remove_toggle_ref(self,  notify, data,):

        libgobject.g_object_remove_toggle_ref.argtypes = [c_void_p, GToggleNotify,gpointer]
        
        libgobject.g_object_remove_toggle_ref(self._object,  notify, data,)

    def thaw_notify(self, ):

        libgobject.g_object_thaw_notify.argtypes = [c_void_p]
        
        libgobject.g_object_thaw_notify(self._object, )

    def dup_qdata(self,  quark, dup_func, user_data,):

        libgobject.g_object_dup_qdata.restype = gpointer
        libgobject.g_object_dup_qdata.argtypes = [c_void_p, GQuark,GDuplicateFunc,gpointer]
        
        return libgobject.g_object_dup_qdata(self._object,  quark, dup_func, user_data,)

    def unref(self,  object,):

        libgobject.g_object_unref.argtypes = [c_void_p, gpointer]
        
        libgobject.g_object_unref(self._object,  object,)

    def get(self,  object, first_property_name,*args ):


        def callit( object, first_property_name, *args ):
                libgobject.g_object_get.restype = None
                libgobject.g_object_get.argtypes = [c_void_p, c_void_p, gpointer, c_char_p]
                for arg in args:
                     libgobject.g_object_get.argtypes.append(args[1])
                return libgobject.g_object_get(self._object, object, first_property_name, *args)
    
        return callit( object, first_property_name,*args )

    def g_weak_ref_set(self,  weak_ref, object,):
        if weak_ref : weak_ref = weak_ref._object
        else : weak_ref = c_void_p()

        libgobject.g_weak_ref_set.argtypes = [c_void_p, _GWeakRef,gpointer]
        
        libgobject.g_weak_ref_set(self._object,  weak_ref, object,)

    def dup_data(self,  key, dup_func, user_data,):

        libgobject.g_object_dup_data.restype = gpointer
        libgobject.g_object_dup_data.argtypes = [c_void_p, c_char_p,GDuplicateFunc,gpointer]
        
        return libgobject.g_object_dup_data(self._object,  key, dup_func, user_data,)

    def replace_qdata(self,  quark, oldval, newval, destroy, old_destroy,):
        if old_destroy : old_destroy = old_destroy._object
        else : old_destroy = c_void_p()

        libgobject.g_object_replace_qdata.restype = gboolean
        libgobject.g_object_replace_qdata.argtypes = [c_void_p, GQuark,gpointer,gpointer,GDestroyNotify,POITNER(GDestroyNotify)]
        
        return libgobject.g_object_replace_qdata(self._object,  quark, oldval, newval, destroy, old_destroy,)

    def get_data(self,  key,):

        libgobject.g_object_get_data.restype = gpointer
        libgobject.g_object_get_data.argtypes = [c_void_p, c_char_p]
        
        return libgobject.g_object_get_data(self._object,  key,)

    def get_property(self,  property_name, value,):
        if value : value = value._object
        else : value = c_void_p()

        libgobject.g_object_get_property.argtypes = [c_void_p, c_char_p,_GValue]
        
        libgobject.g_object_get_property(self._object,  property_name, value,)

    def watch_closure(self,  closure,):
        if closure : closure = closure._object
        else : closure = c_void_p()

        libgobject.g_object_watch_closure.argtypes = [c_void_p, _GClosure]
        
        libgobject.g_object_watch_closure(self._object,  closure,)

    def g_weak_ref_clear(self,  weak_ref,):
        if weak_ref : weak_ref = weak_ref._object
        else : weak_ref = c_void_p()

        libgobject.g_weak_ref_clear.argtypes = [c_void_p, _GWeakRef]
        
        libgobject.g_weak_ref_clear(self._object,  weak_ref,)

    def set_data_full(self,  key, data, destroy,):

        libgobject.g_object_set_data_full.argtypes = [c_void_p, c_char_p,gpointer,GDestroyNotify]
        
        libgobject.g_object_set_data_full(self._object,  key, data, destroy,)

    def force_floating(self, ):

        libgobject.g_object_force_floating.argtypes = [c_void_p]
        
        libgobject.g_object_force_floating(self._object, )

    def class_override_property(self,  oclass, property_id, name,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()

        libgobject.g_object_class_override_property.argtypes = [c_void_p, _GObjectClass,guint,c_char_p]
        
        libgobject.g_object_class_override_property(self._object,  oclass, property_id, name,)

    @staticmethod
    def is_floating( object,):
        libgobject.g_object_is_floating.restype = gboolean
        libgobject.g_object_is_floating.argtypes = [gpointer]
        return libgobject.g_object_is_floating(object, )

    @staticmethod
    def class_find_property( oclass, property_name,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()
        libgobject.g_object_class_find_property.restype = _GParamSpec
        libgobject.g_object_class_find_property.argtypes = [_GObjectClass,c_char_p]
        return libgobject.g_object_class_find_property(oclass, property_name, )

    @staticmethod
    def interface_list_properties( g_iface, n_properties_p,):
        if n_properties_p : n_properties_p = n_properties_p._object
        else : n_properties_p = c_void_p()
        libgobject.g_object_interface_list_properties.restype = _GParamSpec
        libgobject.g_object_interface_list_properties.argtypes = [gpointer,POITNER(guint)]
        return libgobject.g_object_interface_list_properties(g_iface, n_properties_p, )

    @staticmethod
    def newv( object_type, n_parameters, parameters,):
        if parameters : parameters = parameters._object
        else : parameters = c_void_p()
        libgobject.g_object_newv.restype = gpointer
        libgobject.g_object_newv.argtypes = [GType,guint,_GParameter]
        return libgobject.g_object_newv(object_type, n_parameters, parameters, )

    @staticmethod
    def pspec():
        libgobject.pspec.restype = property_id,
        return libgobject.pspec()

    @staticmethod
    def class_list_properties( oclass, n_properties,):
        if oclass : oclass = oclass._object
        else : oclass = c_void_p()
        if n_properties : n_properties = n_properties._object
        else : n_properties = c_void_p()
        libgobject.g_object_class_list_properties.restype = _GParamSpec
        libgobject.g_object_class_list_properties.argtypes = [_GObjectClass,POITNER(guint)]
        return libgobject.g_object_class_list_properties(oclass, n_properties, )

    @staticmethod
    def ref( object,):
        libgobject.g_object_ref.restype = gpointer
        libgobject.g_object_ref.argtypes = [gpointer]
        return libgobject.g_object_ref(object, )

    @staticmethod
    def interface_find_property( g_iface, property_name,):
        libgobject.g_object_interface_find_property.restype = _GParamSpec
        libgobject.g_object_interface_find_property.argtypes = [gpointer,c_char_p]
        return libgobject.g_object_interface_find_property(g_iface, property_name, )

    @staticmethod
    def g_weak_ref_get( weak_ref,):
        if weak_ref : weak_ref = weak_ref._object
        else : weak_ref = c_void_p()
        libgobject.g_weak_ref_get.restype = gpointer
        libgobject.g_weak_ref_get.argtypes = [_GWeakRef]
        return libgobject.g_weak_ref_get(weak_ref, )

    @staticmethod
    def ref_sink( object,):
        libgobject.g_object_ref_sink.restype = gpointer
        libgobject.g_object_ref_sink.argtypes = [gpointer]
        return libgobject.g_object_ref_sink(object, )

    @staticmethod
    def connect( object, signal_spec,*args ):
        libgobject.g_object_connect.restype = gpointer
        libgobject.g_object_connect.argtypes = [gpointer,c_char_p,]
        return libgobject.g_object_connect(object, signal_spec, *args)


    _cfuncs=[]

    def connect(self,  name, func, *args):
        cfunc = None
        def C_Callable():
            func(*args)
            GObject._cfuncs.remove(cfunc)
        cfunc = CFUNCTYPE(None)(C_Callable)
        #prevent from gonig out of scope:
        GObject._cfuncs.append(cfunc)
        libgobject.g_signal_connect_data.restype = c_ulong
        libgobject.g_signal_connect_data.argtypes = [c_void_p, c_char_p, CFUNCTYPE(None), c_void_p, c_void_p, c_int]
        return libgobject.g_signal_connect_data(self._object, name, cfunc, 0,0,0)


    def disconnect(self, handlerid):
        libgobject.g_signal_handler_disconnect.restype = None
        libgobject.g_signal_handler_disconnect.argtypes = [c_void_p, c_ulong]
        libgobject.g_signal_handler_disconnect(self._object, handlerid)
    	

    def __del__(self):
        if self._object:
           libgobject.g_object_unref.argtypes=[c_void_p]
           libgobject.g_object_unref( self._object )

        self._object = None
