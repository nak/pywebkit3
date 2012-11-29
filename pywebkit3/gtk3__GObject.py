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
__GtkRcStyle = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__GdkAtom = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
__GClosure = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
__GtkTextBuffer = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
__GObject = POINTER(c_int)
__PangoLayout = POINTER(c_int)
__GParamSpec = POINTER(c_int)
__PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
__PangoContext = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__GtkSettings = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__PangoFontFamily = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GtkBorder = POINTER(c_int)
__GError = POINTER(c_int)
__PangoCoverage = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
__GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
__PangoMatrix = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GList = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GSList = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
__GdkColor = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__PangoLanguage = POINTER(c_int)
__GdkWMDecoration = POINTER(c_int)
__PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GIcon = POINTER(c_int)
__GtkWindow = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
__GdkDevice = POINTER(c_int)
"""Enumerations"""
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
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
GtkRcFlags = c_int
GtkRcTokenType = c_int

class GObject( object):
    """Class GObject Constructors"""
    def __init__( self, object_type, first_property_name,  obj=None, *args):
        if obj: self._object = obj
        else:
            libgtk3.g_object_new.restype = POINTER(c_int)
            
            libgtk3.g_object_new.argtypes = [GType,c_char_p,]
            self._object = libgtk3.g_object_new(object_type, first_property_name, *args )

    """Methods"""
    def add_toggle_ref(  self, notify, data, ):

        libgtk3.g_object_add_toggle_ref.argtypes = [_GObject,GToggleNotify,gpointer]
        
        libgtk3.g_object_add_toggle_ref( self._object,notify,data )

    def set_qdata_full(  self, quark, data, destroy, ):

        libgtk3.g_object_set_qdata_full.argtypes = [_GObject,GQuark,gpointer,GDestroyNotify]
        
        libgtk3.g_object_set_qdata_full( self._object,quark,data,destroy )

    def weak_unref(  self, notify, data, ):

        libgtk3.g_object_weak_unref.argtypes = [_GObject,GWeakNotify,gpointer]
        
        libgtk3.g_object_weak_unref( self._object,notify,data )

    def steal_data(  self, key, ):

        libgtk3.g_object_steal_data.restype = gpointer
        libgtk3.g_object_steal_data.argtypes = [_GObject,c_char_p]
        
        return libgtk3.g_object_steal_data( self._object,key )

    def run_dispose(  self, ):

        libgtk3.g_object_run_dispose.argtypes = [_GObject]
        
        libgtk3.g_object_run_dispose( self._object )

    def set_qdata(  self, quark, data, ):

        libgtk3.g_object_set_qdata.argtypes = [_GObject,GQuark,gpointer]
        
        libgtk3.g_object_set_qdata( self._object,quark,data )

    def g_clear_object(  self, ):

        libgtk3.g_clear_object.argtypes = [_GObject]
        
        libgtk3.g_clear_object( self._object )

    def set_data(  self, key, data, ):

        libgtk3.g_object_set_data.argtypes = [_GObject,c_char_p,gpointer]
        
        libgtk3.g_object_set_data( self._object,key,data )

    def steal_qdata(  self, quark, ):

        libgtk3.g_object_steal_qdata.restype = gpointer
        libgtk3.g_object_steal_qdata.argtypes = [_GObject,GQuark]
        
        return libgtk3.g_object_steal_qdata( self._object,quark )

    def notify(  self, property_name, ):

        libgtk3.g_object_notify.argtypes = [_GObject,c_char_p]
        
        libgtk3.g_object_notify( self._object,property_name )

    def class_install_properties(  self, oclass, n_pspecs, pspecs, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_int)()
        if pspecs: pspecs = pspecs._object
        else: pspecs = POINTER(c_int)()

        libgtk3.g_object_class_install_properties.argtypes = [_GObject,_GObjectClass,guint,_GParamSpec]
        
        libgtk3.g_object_class_install_properties( self._object,oclass,n_pspecs,pspecs )

    def replace_data(  self, key, oldval, newval, destroy, old_destroy, ):

        libgtk3.g_object_replace_data.restype = gboolean
        libgtk3.g_object_replace_data.argtypes = [_GObject,c_char_p,gpointer,gpointer,GDestroyNotify,POINTER(GDestroyNotify)]
        
        return libgtk3.g_object_replace_data( self._object,key,oldval,newval,destroy,old_destroy )

    def interface_install_property(  self, g_iface, pspec, ):
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        libgtk3.g_object_interface_install_property.argtypes = [_GObject,gpointer,_GParamSpec]
        
        libgtk3.g_object_interface_install_property( self._object,g_iface,pspec )

    def get_qdata(  self, quark, ):

        libgtk3.g_object_get_qdata.restype = gpointer
        libgtk3.g_object_get_qdata.argtypes = [_GObject,GQuark]
        
        return libgtk3.g_object_get_qdata( self._object,quark )

    def set_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        libgtk3.g_object_set_property.argtypes = [_GObject,c_char_p,_GValue]
        
        libgtk3.g_object_set_property( self._object,property_name,value )

    def set(  self, object, first_property_name,*args  ):


        def callit( object, first_property_name, *args ):
                libgtk3.g_object_set.restype = None
                libgtk3.g_object_set.argtypes = [ POINTER(c_int), gpointer, c_char_p]
                for arg in args:
                     libgtk3.g_object_set.argtypes.append(args[1])
                return libgtk3.g_object_set( object, first_property_name, *args)
    
        return callit( self._object, object, first_property_name,*args )

    def disconnect(  self, object, signal_spec,*args  ):


        def callit( object, signal_spec, *args ):
                libgtk3.g_object_disconnect.restype = None
                libgtk3.g_object_disconnect.argtypes = [ POINTER(c_int), gpointer, c_char_p]
                for arg in args:
                     libgtk3.g_object_disconnect.argtypes.append(args[1])
                return libgtk3.g_object_disconnect( object, signal_spec, *args)
    
        return callit( self._object, object, signal_spec,*args )

    def weak_ref(  self, notify, data, ):

        libgtk3.g_object_weak_ref.argtypes = [_GObject,GWeakNotify,gpointer]
        
        libgtk3.g_object_weak_ref( self._object,notify,data )

    def add_weak_pointer(  self, weak_pointer_location, ):

        libgtk3.g_object_add_weak_pointer.argtypes = [_GObject,POINTER(gpointer)]
        
        libgtk3.g_object_add_weak_pointer( self._object,weak_pointer_location )

    def remove_weak_pointer(  self, weak_pointer_location, ):

        libgtk3.g_object_remove_weak_pointer.argtypes = [_GObject,POINTER(gpointer)]
        
        libgtk3.g_object_remove_weak_pointer( self._object,weak_pointer_location )

    def class_install_property(  self, oclass, property_id, pspec, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_int)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        libgtk3.g_object_class_install_property.argtypes = [_GObject,_GObjectClass,guint,_GParamSpec]
        
        libgtk3.g_object_class_install_property( self._object,oclass,property_id,pspec )

    def freeze_notify(  self, ):

        libgtk3.g_object_freeze_notify.argtypes = [_GObject]
        
        libgtk3.g_object_freeze_notify( self._object )

    def notify_by_pspec(  self, pspec, ):
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        libgtk3.g_object_notify_by_pspec.argtypes = [_GObject,_GParamSpec]
        
        libgtk3.g_object_notify_by_pspec( self._object,pspec )

    def remove_toggle_ref(  self, notify, data, ):

        libgtk3.g_object_remove_toggle_ref.argtypes = [_GObject,GToggleNotify,gpointer]
        
        libgtk3.g_object_remove_toggle_ref( self._object,notify,data )

    def thaw_notify(  self, ):

        libgtk3.g_object_thaw_notify.argtypes = [_GObject]
        
        libgtk3.g_object_thaw_notify( self._object )

    def dup_qdata(  self, quark, dup_func, user_data, ):

        libgtk3.g_object_dup_qdata.restype = gpointer
        libgtk3.g_object_dup_qdata.argtypes = [_GObject,GQuark,GDuplicateFunc,gpointer]
        
        return libgtk3.g_object_dup_qdata( self._object,quark,dup_func,user_data )

    def unref(  self, object, ):

        libgtk3.g_object_unref.argtypes = [_GObject,gpointer]
        
        libgtk3.g_object_unref( self._object,object )

    def get(  self, object, first_property_name,*args  ):


        def callit( object, first_property_name, *args ):
                libgtk3.g_object_get.restype = None
                libgtk3.g_object_get.argtypes = [ POINTER(c_int), gpointer, c_char_p]
                for arg in args:
                     libgtk3.g_object_get.argtypes.append(args[1])
                return libgtk3.g_object_get( object, first_property_name, *args)
    
        return callit( self._object, object, first_property_name,*args )

    def g_weak_ref_set(  self, weak_ref, object, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_int)()

        libgtk3.g_weak_ref_set.argtypes = [_GObject,_GWeakRef,gpointer]
        
        libgtk3.g_weak_ref_set( self._object,weak_ref,object )

    def dup_data(  self, key, dup_func, user_data, ):

        libgtk3.g_object_dup_data.restype = gpointer
        libgtk3.g_object_dup_data.argtypes = [_GObject,c_char_p,GDuplicateFunc,gpointer]
        
        return libgtk3.g_object_dup_data( self._object,key,dup_func,user_data )

    def replace_qdata(  self, quark, oldval, newval, destroy, old_destroy, ):

        libgtk3.g_object_replace_qdata.restype = gboolean
        libgtk3.g_object_replace_qdata.argtypes = [_GObject,GQuark,gpointer,gpointer,GDestroyNotify,POINTER(GDestroyNotify)]
        
        return libgtk3.g_object_replace_qdata( self._object,quark,oldval,newval,destroy,old_destroy )

    def get_data(  self, key, ):

        libgtk3.g_object_get_data.restype = gpointer
        libgtk3.g_object_get_data.argtypes = [_GObject,c_char_p]
        
        return libgtk3.g_object_get_data( self._object,key )

    def get_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        libgtk3.g_object_get_property.argtypes = [_GObject,c_char_p,_GValue]
        
        libgtk3.g_object_get_property( self._object,property_name,value )

    def watch_closure(  self, closure, ):
        if closure: closure = closure._object
        else: closure = POINTER(c_int)()

        libgtk3.g_object_watch_closure.argtypes = [_GObject,_GClosure]
        
        libgtk3.g_object_watch_closure( self._object,closure )

    def g_weak_ref_clear(  self, weak_ref, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_int)()

        libgtk3.g_weak_ref_clear.argtypes = [_GObject,_GWeakRef]
        
        libgtk3.g_weak_ref_clear( self._object,weak_ref )

    def set_data_full(  self, key, data, destroy, ):

        libgtk3.g_object_set_data_full.argtypes = [_GObject,c_char_p,gpointer,GDestroyNotify]
        
        libgtk3.g_object_set_data_full( self._object,key,data,destroy )

    def g_weak_ref_init(  self, weak_ref, object, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_int)()

        libgtk3.g_weak_ref_init.argtypes = [_GObject,_GWeakRef,gpointer]
        
        libgtk3.g_weak_ref_init( self._object,weak_ref,object )

    def force_floating(  self, ):

        libgtk3.g_object_force_floating.argtypes = [_GObject]
        
        libgtk3.g_object_force_floating( self._object )

    def class_override_property(  self, oclass, property_id, name, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_int)()

        libgtk3.g_object_class_override_property.argtypes = [_GObject,_GObjectClass,guint,c_char_p]
        
        libgtk3.g_object_class_override_property( self._object,oclass,property_id,name )

    @staticmethod
    def is_floating( object,):
        libgtk3.g_object_is_floating.restype = gboolean
        libgtk3.g_object_is_floating.argtypes = [gpointer]
        
        return     libgtk3.g_object_is_floating(object, )

    @staticmethod
    def class_find_property( oclass, property_name,):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_int)()
        libgtk3.g_object_class_find_property.restype = _GParamSpec
        libgtk3.g_object_class_find_property.argtypes = [_GObjectClass,c_char_p]
        from gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.g_object_class_find_property(oclass, property_name, )
 or POINTER(c_int)())
    @staticmethod
    def interface_list_properties( g_iface, n_properties_p,):
        libgtk3.g_object_interface_list_properties.restype = _GParamSpec
        libgtk3.g_object_interface_list_properties.argtypes = [gpointer,POINTER(guint)]
        from gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.g_object_interface_list_properties(g_iface, n_properties_p, )
 or POINTER(c_int)())
    @staticmethod
    def newv( object_type, n_parameters, parameters,):
        if parameters: parameters = parameters._object
        else: parameters = POINTER(c_int)()
        libgtk3.g_object_newv.restype = gpointer
        libgtk3.g_object_newv.argtypes = [GType,guint,_GParameter]
        
        return     libgtk3.g_object_newv(object_type, n_parameters, parameters, )

    @staticmethod
    def class_list_properties( oclass, n_properties,):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_int)()
        libgtk3.g_object_class_list_properties.restype = _GParamSpec
        libgtk3.g_object_class_list_properties.argtypes = [_GObjectClass,POINTER(guint)]
        from gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.g_object_class_list_properties(oclass, n_properties, )
 or POINTER(c_int)())
    @staticmethod
    def ref( object,):
        libgtk3.g_object_ref.restype = gpointer
        libgtk3.g_object_ref.argtypes = [gpointer]
        
        return     libgtk3.g_object_ref(object, )

    @staticmethod
    def interface_find_property( g_iface, property_name,):
        libgtk3.g_object_interface_find_property.restype = _GParamSpec
        libgtk3.g_object_interface_find_property.argtypes = [gpointer,c_char_p]
        from gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.g_object_interface_find_property(g_iface, property_name, )
 or POINTER(c_int)())
    @staticmethod
    def g_weak_ref_get( weak_ref,):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_int)()
        libgtk3.g_weak_ref_get.restype = gpointer
        libgtk3.g_weak_ref_get.argtypes = [_GWeakRef]
        
        return     libgtk3.g_weak_ref_get(weak_ref, )

    @staticmethod
    def ref_sink( object,):
        libgtk3.g_object_ref_sink.restype = gpointer
        libgtk3.g_object_ref_sink.argtypes = [gpointer]
        
        return     libgtk3.g_object_ref_sink(object, )

    @staticmethod
    def connect( object, signal_spec,*args ):
        libgtk3.g_object_connect.restype = gpointer
        libgtk3.g_object_connect.argtypes = [gpointer,c_char_p,]
        
        return     libgtk3.g_object_connect(object, signal_spec, *args)

