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
_GdkDisplay = c_void_p
__GtkStyleProvider = c_void_p
_PangoFont = c_void_p
_GtkStyleContext = c_void_p
_guchar = c_void_p
_GdkAppLaunchContext = c_void_p
__PangoLayout = c_void_p
__GParamSpec = c_void_p
__PangoAttrIterator = c_void_p
__GtkWindow = c_void_p
_GtkWindowGroup = c_void_p
__PangoContext = c_void_p
__PangoFontMap = c_void_p
__PangoAttrList = c_void_p
_PangoMatrix = c_void_p
_GtkApplication = c_void_p
__PangoAnalysis = c_void_p
_PangoFontDescription = c_void_p
__GdkCursor = c_void_p
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
__GdkVisual = c_void_p
_GdkDevice = c_void_p
_GList = c_void_p
__GtkAccelGroup = c_void_p
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
__GdkRGBA = c_void_p
__GdkWindowAttr = c_void_p
__GdkColor = c_void_p
__GdkRectangle = c_void_p
__PangoLanguage = c_void_p
__GdkWMDecoration = c_void_p
__PangoLogAttr = c_void_p
_PangoLayout = c_void_p
_GtkStyle = c_void_p
__GtkStyle = c_void_p
__GIcon = c_void_p
__cairo_pattern_t = c_void_p
__GdkPixbuf = c_void_p
_GtkSettings = c_void_p
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

class GtkWidgetPath( object):
    """Class GtkWidgetPath Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_widget_path_new.restype = c_void_p

        libgtk3.gtk_widget_path_new.argtypes = []
        self._object = libgtk3.gtk_widget_path_new()

    """Methods"""
    def iter_has_qname(self,  pos, qname,):

        libgtk3.gtk_widget_path_iter_has_qname.restype = gboolean
        libgtk3.gtk_widget_path_iter_has_qname.argtypes = [c_void_p, gint,GQuark]
        
        return libgtk3.gtk_widget_path_iter_has_qname(self._object,  pos, qname,)

    def iter_add_region(self,  pos, name, flags,):
        if flags : flags = flags._object
        else : flags = c_void_p()

        libgtk3.gtk_widget_path_iter_add_region.argtypes = [c_void_p, gint,c_char_p,GtkRegionFlags]
        
        libgtk3.gtk_widget_path_iter_add_region(self._object,  pos, name, flags,)

    def iter_clear_regions(self,  pos,):

        libgtk3.gtk_widget_path_iter_clear_regions.argtypes = [c_void_p, gint]
        
        libgtk3.gtk_widget_path_iter_clear_regions(self._object,  pos,)

    def iter_has_name(self,  pos, name,):

        libgtk3.gtk_widget_path_iter_has_name.restype = gboolean
        libgtk3.gtk_widget_path_iter_has_name.argtypes = [c_void_p, gint,c_char_p]
        
        return libgtk3.gtk_widget_path_iter_has_name(self._object,  pos, name,)

    def iter_has_qregion(self,  pos, qname, flags,):
        if flags : flags = flags._object
        else : flags = c_void_p()

        libgtk3.gtk_widget_path_iter_has_qregion.restype = gboolean
        libgtk3.gtk_widget_path_iter_has_qregion.argtypes = [c_void_p, gint,GQuark,_GtkRegionFlags]
        
        return libgtk3.gtk_widget_path_iter_has_qregion(self._object,  pos, qname, flags,)

    def iter_remove_region(self,  pos, name,):

        libgtk3.gtk_widget_path_iter_remove_region.argtypes = [c_void_p, gint,c_char_p]
        
        libgtk3.gtk_widget_path_iter_remove_region(self._object,  pos, name,)

    def is_type(self,  type,):

        libgtk3.gtk_widget_path_is_type.restype = gboolean
        libgtk3.gtk_widget_path_is_type.argtypes = [c_void_p, GType]
        
        return libgtk3.gtk_widget_path_is_type(self._object,  type,)

    def has_parent(self,  type,):

        libgtk3.gtk_widget_path_has_parent.restype = gboolean
        libgtk3.gtk_widget_path_has_parent.argtypes = [c_void_p, GType]
        
        return libgtk3.gtk_widget_path_has_parent(self._object,  type,)

    def iter_get_name(self,  pos,):

        libgtk3.gtk_widget_path_iter_get_name.restype = _gchar
        libgtk3.gtk_widget_path_iter_get_name.argtypes = [c_void_p, gint]
        
        return libgtk3.gtk_widget_path_iter_get_name(self._object,  pos,)

    def iter_has_qclass(self,  pos, qname,):

        libgtk3.gtk_widget_path_iter_has_qclass.restype = gboolean
        libgtk3.gtk_widget_path_iter_has_qclass.argtypes = [c_void_p, gint,GQuark]
        
        return libgtk3.gtk_widget_path_iter_has_qclass(self._object,  pos, qname,)

    def iter_clear_classes(self,  pos,):

        libgtk3.gtk_widget_path_iter_clear_classes.argtypes = [c_void_p, gint]
        
        libgtk3.gtk_widget_path_iter_clear_classes(self._object,  pos,)

    def free(self, ):

        libgtk3.gtk_widget_path_free.argtypes = [c_void_p]
        
        libgtk3.gtk_widget_path_free(self._object, )

    def prepend_type(self,  type,):

        libgtk3.gtk_widget_path_prepend_type.argtypes = [c_void_p, GType]
        
        libgtk3.gtk_widget_path_prepend_type(self._object,  type,)

    def iter_get_object_type(self,  pos,):

        libgtk3.gtk_widget_path_iter_get_object_type.restype = GType
        libgtk3.gtk_widget_path_iter_get_object_type.argtypes = [c_void_p, gint]
        
        return libgtk3.gtk_widget_path_iter_get_object_type(self._object,  pos,)

    def append_type(self,  type,):

        libgtk3.gtk_widget_path_append_type.restype = gint
        libgtk3.gtk_widget_path_append_type.argtypes = [c_void_p, GType]
        
        return libgtk3.gtk_widget_path_append_type(self._object,  type,)

    def iter_set_object_type(self,  pos, type,):

        libgtk3.gtk_widget_path_iter_set_object_type.argtypes = [c_void_p, gint,GType]
        
        libgtk3.gtk_widget_path_iter_set_object_type(self._object,  pos, type,)

    def iter_remove_class(self,  pos, name,):

        libgtk3.gtk_widget_path_iter_remove_class.argtypes = [c_void_p, gint,c_char_p]
        
        libgtk3.gtk_widget_path_iter_remove_class(self._object,  pos, name,)

    def iter_list_regions(self,  pos,):

        libgtk3.gtk_widget_path_iter_list_regions.restype = _GSList
        libgtk3.gtk_widget_path_iter_list_regions.argtypes = [c_void_p, gint]
        from pywebkit3.gobject import GSList
        return GSList( obj=libgtk3.gtk_widget_path_iter_list_regions(self._object,  pos,) or c_void_p())

    def iter_has_region(self,  pos, name, flags,):
        if flags : flags = flags._object
        else : flags = c_void_p()

        libgtk3.gtk_widget_path_iter_has_region.restype = gboolean
        libgtk3.gtk_widget_path_iter_has_region.argtypes = [c_void_p, gint,c_char_p,_GtkRegionFlags]
        
        return libgtk3.gtk_widget_path_iter_has_region(self._object,  pos, name, flags,)

    def iter_set_name(self,  pos, name,):

        libgtk3.gtk_widget_path_iter_set_name.argtypes = [c_void_p, gint,c_char_p]
        
        libgtk3.gtk_widget_path_iter_set_name(self._object,  pos, name,)

    def get_object_type(self, ):

        libgtk3.gtk_widget_path_get_object_type.restype = GType
        libgtk3.gtk_widget_path_get_object_type.argtypes = [c_void_p]
        
        return libgtk3.gtk_widget_path_get_object_type(self._object, )

    def iter_list_classes(self,  pos,):

        libgtk3.gtk_widget_path_iter_list_classes.restype = _GSList
        libgtk3.gtk_widget_path_iter_list_classes.argtypes = [c_void_p, gint]
        from pywebkit3.gobject import GSList
        return GSList( obj=libgtk3.gtk_widget_path_iter_list_classes(self._object,  pos,) or c_void_p())

    def iter_add_class(self,  pos, name,):

        libgtk3.gtk_widget_path_iter_add_class.argtypes = [c_void_p, gint,c_char_p]
        
        libgtk3.gtk_widget_path_iter_add_class(self._object,  pos, name,)

    def iter_has_class(self,  pos, name,):

        libgtk3.gtk_widget_path_iter_has_class.restype = gboolean
        libgtk3.gtk_widget_path_iter_has_class.argtypes = [c_void_p, gint,c_char_p]
        
        return libgtk3.gtk_widget_path_iter_has_class(self._object,  pos, name,)

    def copy(self, ):

        libgtk3.gtk_widget_path_copy.restype = _GtkWidgetPath
        libgtk3.gtk_widget_path_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidgetPath
        return GtkWidgetPath(None, obj=libgtk3.gtk_widget_path_copy(self._object, ) or c_void_p())

    def length(self, ):

        libgtk3.gtk_widget_path_length.restype = gint
        libgtk3.gtk_widget_path_length.argtypes = [c_void_p]
        
        return libgtk3.gtk_widget_path_length(self._object, )

