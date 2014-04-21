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
from .gtk3_types import *
from .gtk3_enums import *
from .gtk3_types import *
from .gtk3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_void_p)
_GdkGeometry = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GdkTimeCoord = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GClosure = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GtkTextBuffer = POINTER(c_void_p)
_GtkNumerableIcon = POINTER(c_void_p)
_GdkAppLaunchContext = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_PangoAttrIterator = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GtkPathPriorityType = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_GtkWidgetClass = POINTER(c_void_p)
_GdkEventKey = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_PangoFontMetrics = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_cairo_t = POINTER(c_void_p)
_GWeakRef = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_PangoRectangle = POINTER(c_void_p)
_GtkAccelGroup = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GtkAllocation = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GParameter = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_pattern_t = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_GdkPixbufSimpleAnim = POINTER(c_void_p)
_WebKitGeolocationPolicyDecision = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
"""Enumerations"""
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
GdkCursorType = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GtkIconSize = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int

try:
    libgtk3.g_object_disconnect.restype = None
    libgtk3.g_object_disconnect.argtypes = [_GObject,Asciifier]
except:
   pass
try:
    libgtk3.g_object_set_qdata_full.restype = None
    libgtk3.g_object_set_qdata_full.argtypes = [_GObject,GQuark,gpointer,GDestroyNotify]
except:
   pass
try:
    libgtk3.g_object_weak_unref.restype = None
    libgtk3.g_object_weak_unref.argtypes = [_GObject,GWeakNotify,gpointer]
except:
   pass
try:
    libgtk3.g_object_steal_data.restype = gpointer
    libgtk3.g_object_steal_data.argtypes = [_GObject,Asciifier]
except:
   pass
try:
    libgtk3.g_object_run_dispose.restype = None
    libgtk3.g_object_run_dispose.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_set_qdata.restype = None
    libgtk3.g_object_set_qdata.argtypes = [_GObject,GQuark,gpointer]
except:
   pass
try:
    libgtk3.g_clear_object.restype = None
    libgtk3.g_clear_object.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_set_data.restype = None
    libgtk3.g_object_set_data.argtypes = [_GObject,Asciifier,gpointer]
except:
   pass
try:
    libgtk3.g_object_ref_sink.restype = gpointer
    libgtk3.g_object_ref_sink.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_connect.restype = gpointer
    libgtk3.g_object_connect.argtypes = [_GObject,Asciifier,]
except:
   pass
try:
    libgtk3.g_object_notify.restype = None
    libgtk3.g_object_notify.argtypes = [_GObject,Asciifier]
except:
   pass
try:
    libgtk3.g_object_class_install_properties.restype = None
    libgtk3.g_object_class_install_properties.argtypes = [_GObject,_GObjectClass,guint,_GParamSpec]
except:
   pass
try:
    libgtk3.g_object_replace_data.restype = gboolean
    libgtk3.g_object_replace_data.argtypes = [_GObject,Asciifier,gpointer,gpointer,GDestroyNotify,POINTER(GDestroyNotify)]
except:
   pass
try:
    libgtk3.g_object_interface_install_property.restype = None
    libgtk3.g_object_interface_install_property.argtypes = [_GObject,gpointer,_GParamSpec]
except:
   pass
try:
    libgtk3.g_object_get_qdata.restype = gpointer
    libgtk3.g_object_get_qdata.argtypes = [_GObject,GQuark]
except:
   pass
try:
    libgtk3.g_object_set_property.restype = None
    libgtk3.g_object_set_property.argtypes = [_GObject,Asciifier,_GValue]
except:
   pass
try:
    libgtk3.g_object_set.restype = None
    libgtk3.g_object_set.argtypes = [_GObject,Asciifier,]
except:
   pass
try:
    libgtk3.g_object_ref.restype = gpointer
    libgtk3.g_object_ref.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_steal_qdata.restype = gpointer
    libgtk3.g_object_steal_qdata.argtypes = [_GObject,GQuark]
except:
   pass
try:
    libgtk3.g_object_add_toggle_ref.restype = None
    libgtk3.g_object_add_toggle_ref.argtypes = [_GObject,GToggleNotify,gpointer]
except:
   pass
try:
    libgtk3.g_object_weak_ref.restype = None
    libgtk3.g_object_weak_ref.argtypes = [_GObject,GWeakNotify,gpointer]
except:
   pass
try:
    libgtk3.g_object_add_weak_pointer.restype = None
    libgtk3.g_object_add_weak_pointer.argtypes = [_GObject,POINTER(gpointer)]
except:
   pass
try:
    libgtk3.g_object_remove_weak_pointer.restype = None
    libgtk3.g_object_remove_weak_pointer.argtypes = [_GObject,POINTER(gpointer)]
except:
   pass
try:
    libgtk3.g_object_class_install_property.restype = None
    libgtk3.g_object_class_install_property.argtypes = [_GObject,_GObjectClass,guint,_GParamSpec]
except:
   pass
try:
    libgtk3.g_object_freeze_notify.restype = None
    libgtk3.g_object_freeze_notify.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_notify_by_pspec.restype = None
    libgtk3.g_object_notify_by_pspec.argtypes = [_GObject,_GParamSpec]
except:
   pass
try:
    libgtk3.g_object_remove_toggle_ref.restype = None
    libgtk3.g_object_remove_toggle_ref.argtypes = [_GObject,GToggleNotify,gpointer]
except:
   pass
try:
    libgtk3.g_object_thaw_notify.restype = None
    libgtk3.g_object_thaw_notify.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_is_floating.restype = gboolean
    libgtk3.g_object_is_floating.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_dup_qdata.restype = gpointer
    libgtk3.g_object_dup_qdata.argtypes = [_GObject,GQuark,GDuplicateFunc,gpointer]
except:
   pass
try:
    libgtk3.g_object_unref.restype = None
    libgtk3.g_object_unref.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_get.restype = None
    libgtk3.g_object_get.argtypes = [_GObject,Asciifier,]
except:
   pass
try:
    libgtk3.g_weak_ref_set.restype = None
    libgtk3.g_weak_ref_set.argtypes = [_GObject,_GWeakRef,gpointer]
except:
   pass
try:
    libgtk3.g_object_dup_data.restype = gpointer
    libgtk3.g_object_dup_data.argtypes = [_GObject,Asciifier,GDuplicateFunc,gpointer]
except:
   pass
try:
    libgtk3.g_object_replace_qdata.restype = gboolean
    libgtk3.g_object_replace_qdata.argtypes = [_GObject,GQuark,gpointer,gpointer,GDestroyNotify,POINTER(GDestroyNotify)]
except:
   pass
try:
    libgtk3.g_object_get_data.restype = gpointer
    libgtk3.g_object_get_data.argtypes = [_GObject,Asciifier]
except:
   pass
try:
    libgtk3.g_object_get_property.restype = None
    libgtk3.g_object_get_property.argtypes = [_GObject,Asciifier,_GValue]
except:
   pass
try:
    libgtk3.g_object_watch_closure.restype = None
    libgtk3.g_object_watch_closure.argtypes = [_GObject,_GClosure]
except:
   pass
try:
    libgtk3.g_weak_ref_clear.restype = None
    libgtk3.g_weak_ref_clear.argtypes = [_GObject,_GWeakRef]
except:
   pass
try:
    libgtk3.g_object_set_data_full.restype = None
    libgtk3.g_object_set_data_full.argtypes = [_GObject,Asciifier,gpointer,GDestroyNotify]
except:
   pass
try:
    libgtk3.g_weak_ref_init.restype = None
    libgtk3.g_weak_ref_init.argtypes = [_GObject,_GWeakRef,gpointer]
except:
   pass
try:
    libgtk3.g_object_force_floating.restype = None
    libgtk3.g_object_force_floating.argtypes = [_GObject]
except:
   pass
try:
    libgtk3.g_object_class_override_property.restype = None
    libgtk3.g_object_class_override_property.argtypes = [_GObject,_GObjectClass,guint,Asciifier]
except:
   pass
try:
    libgtk3.g_object_class_find_property.restype = _GParamSpec
    libgtk3.g_object_class_find_property.argtypes = [_GObjectClass,Asciifier]
except:
   pass
try:
    libgtk3.g_object_interface_list_properties.restype = _GParamSpec
    libgtk3.g_object_interface_list_properties.argtypes = [gpointer,POINTER(guint)]
except:
   pass
try:
    libgtk3.g_object_newv.restype = gpointer
    libgtk3.g_object_newv.argtypes = [GType,guint,_GParameter]
except:
   pass
try:
    libgtk3.g_object_class_list_properties.restype = _GParamSpec
    libgtk3.g_object_class_list_properties.argtypes = [_GObjectClass,POINTER(guint)]
except:
   pass
try:
    libgtk3.g_object_interface_find_property.restype = _GParamSpec
    libgtk3.g_object_interface_find_property.argtypes = [gpointer,Asciifier]
except:
   pass
try:
    libgtk3.g_weak_ref_get.restype = gpointer
    libgtk3.g_weak_ref_get.argtypes = [_GWeakRef]
except:
   pass
class GObject( object):
    """Class GObject Constructors"""
    def __init__( self, object_type, first_property_name,  obj=None, *args):
        if obj: self._object = obj
        else:
            libgtk3.g_object_new.restype = POINTER(c_void_p)
            
            libgtk3.g_object_new.argtypes = [GType,Asciifier,]
            self._object = libgtk3.g_object_new(object_type, first_property_name, *args )

    """Methods"""
    def disconnect(  self, signal_spec, ):

        
        libgtk3.g_object_disconnect( self._object,signal_spec )

    def set_qdata_full(  self, quark, data, destroy, ):

        
        libgtk3.g_object_set_qdata_full( self._object,quark,data,destroy )

    def weak_unref(  self, notify, data, ):

        
        libgtk3.g_object_weak_unref( self._object,notify,data )

    def steal_data(  self, key, ):

        
        return libgtk3.g_object_steal_data( self._object,key )

    def run_dispose(  self, ):

        
        libgtk3.g_object_run_dispose( self._object )

    def set_qdata(  self, quark, data, ):

        
        libgtk3.g_object_set_qdata( self._object,quark,data )

    def g_clear_object(  self, ):

        
        libgtk3.g_clear_object( self._object )

    def set_data(  self, key, data, ):

        
        libgtk3.g_object_set_data( self._object,key,data )

    def ref_sink(  self, ):

        
        return libgtk3.g_object_ref_sink( self._object )

    def connect(  self, signal_spec,*args  ):


        def callit( signal_spec, *args ):
                for arg in args:
                     libgtk3.g_object_connect.argtypes.append(args[1])
                return libgtk3.g_object_connect( signal_spec, *args)
    
        return callit( self._object, signal_spec,*args )

    def notify(  self, property_name, ):

        
        libgtk3.g_object_notify( self._object,property_name )

    def class_install_properties(  self, oclass, n_pspecs, pspecs, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()
        if pspecs: pspecs = pspecs._object
        else: pspecs = POINTER(c_void_p)()

        
        libgtk3.g_object_class_install_properties( self._object,oclass,n_pspecs,pspecs )

    def replace_data(  self, key, oldval, newval, destroy, old_destroy, ):

        
        return libgtk3.g_object_replace_data( self._object,key,oldval,newval,destroy,old_destroy )

    def interface_install_property(  self, g_iface, pspec, ):
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_void_p)()

        
        libgtk3.g_object_interface_install_property( self._object,g_iface,pspec )

    def get_qdata(  self, quark, ):

        
        return libgtk3.g_object_get_qdata( self._object,quark )

    def set_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgtk3.g_object_set_property( self._object,property_name,value )

    def set(  self, first_property_name,*args  ):


        def callit( first_property_name, *args ):
                for arg in args:
                     libgtk3.g_object_set.argtypes.append(args[1])
                return libgtk3.g_object_set( first_property_name, *args)
    
        return callit( self._object, first_property_name,*args )

    def ref(  self, ):

        
        return libgtk3.g_object_ref( self._object )

    def steal_qdata(  self, quark, ):

        
        return libgtk3.g_object_steal_qdata( self._object,quark )

    def add_toggle_ref(  self, notify, data, ):

        
        libgtk3.g_object_add_toggle_ref( self._object,notify,data )

    def weak_ref(  self, notify, data, ):

        
        libgtk3.g_object_weak_ref( self._object,notify,data )

    def add_weak_pointer(  self, weak_pointer_location, ):

        
        libgtk3.g_object_add_weak_pointer( self._object,weak_pointer_location )

    def remove_weak_pointer(  self, weak_pointer_location, ):

        
        libgtk3.g_object_remove_weak_pointer( self._object,weak_pointer_location )

    def class_install_property(  self, oclass, property_id, pspec, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_void_p)()

        
        libgtk3.g_object_class_install_property( self._object,oclass,property_id,pspec )

    def freeze_notify(  self, ):

        
        libgtk3.g_object_freeze_notify( self._object )

    def notify_by_pspec(  self, pspec, ):
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_void_p)()

        
        libgtk3.g_object_notify_by_pspec( self._object,pspec )

    def remove_toggle_ref(  self, notify, data, ):

        
        libgtk3.g_object_remove_toggle_ref( self._object,notify,data )

    def thaw_notify(  self, ):

        
        libgtk3.g_object_thaw_notify( self._object )

    def is_floating(  self, ):

        
        return libgtk3.g_object_is_floating( self._object )

    def dup_qdata(  self, quark, dup_func, user_data, ):

        
        return libgtk3.g_object_dup_qdata( self._object,quark,dup_func,user_data )

    def unref(  self, ):

        
        libgtk3.g_object_unref( self._object )

    def get(  self, first_property_name,*args  ):


        def callit( first_property_name, *args ):
                for arg in args:
                     libgtk3.g_object_get.argtypes.append(args[1])
                return libgtk3.g_object_get( first_property_name, *args)
    
        return callit( self._object, first_property_name,*args )

    def g_weak_ref_set(  self, weak_ref, object, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_void_p)()

        
        libgtk3.g_weak_ref_set( self._object,weak_ref,object )

    def dup_data(  self, key, dup_func, user_data, ):

        
        return libgtk3.g_object_dup_data( self._object,key,dup_func,user_data )

    def replace_qdata(  self, quark, oldval, newval, destroy, old_destroy, ):

        
        return libgtk3.g_object_replace_qdata( self._object,quark,oldval,newval,destroy,old_destroy )

    def get_data(  self, key, ):

        
        return libgtk3.g_object_get_data( self._object,key )

    def get_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgtk3.g_object_get_property( self._object,property_name,value )

    def watch_closure(  self, closure, ):
        if closure: closure = closure._object
        else: closure = POINTER(c_void_p)()

        
        libgtk3.g_object_watch_closure( self._object,closure )

    def g_weak_ref_clear(  self, weak_ref, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_void_p)()

        
        libgtk3.g_weak_ref_clear( self._object,weak_ref )

    def set_data_full(  self, key, data, destroy, ):

        
        libgtk3.g_object_set_data_full( self._object,key,data,destroy )

    def g_weak_ref_init(  self, weak_ref, object, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_void_p)()

        
        libgtk3.g_weak_ref_init( self._object,weak_ref,object )

    def force_floating(  self, ):

        
        libgtk3.g_object_force_floating( self._object )

    def class_override_property(  self, oclass, property_id, name, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()

        
        libgtk3.g_object_class_override_property( self._object,oclass,property_id,name )

    @staticmethod
    def class_find_property( oclass, property_name,):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.g_object_class_find_property(oclass, property_name, )
 or POINTER(c_void_p)())
    @staticmethod
    def interface_list_properties( g_iface, n_properties_p,):
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.g_object_interface_list_properties(g_iface, n_properties_p, )
 or POINTER(c_void_p)())
    @staticmethod
    def newv( object_type, n_parameters, parameters,):
        if parameters: parameters = parameters._object
        else: parameters = POINTER(c_void_p)()
        
        return     libgtk3.g_object_newv(object_type, n_parameters, parameters, )

    @staticmethod
    def class_list_properties( oclass, n_properties,):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.g_object_class_list_properties(oclass, n_properties, )
 or POINTER(c_void_p)())
    @staticmethod
    def interface_find_property( g_iface, property_name,):
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.g_object_interface_find_property(g_iface, property_name, )
 or POINTER(c_void_p)())
    @staticmethod
    def g_weak_ref_get( weak_ref,):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_void_p)()
        
        return     libgtk3.g_weak_ref_get(weak_ref, )

