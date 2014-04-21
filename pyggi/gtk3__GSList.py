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
_GdkGeometry = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GdkTimeCoord = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_cairo_pattern_t = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GtkNumerableIcon = POINTER(c_void_p)
_GdkAppLaunchContext = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GdkPixbufSimpleAnim = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
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

try:
    libgtk3.g_slist_insert_before.restype = _GSList
    libgtk3.g_slist_insert_before.argtypes = [_GSList,_GSList,gpointer]
except:
   pass
try:
    libgtk3.g_slist_free.restype = None
    libgtk3.g_slist_free.argtypes = [_GSList]
except:
   pass
try:
    libgtk3.g_slist_insert_sorted_with_data.restype = _GSList
    libgtk3.g_slist_insert_sorted_with_data.argtypes = [_GSList,gpointer,GCompareDataFunc,gpointer]
except:
   pass
try:
    libgtk3.g_slist_copy.restype = _GSList
    libgtk3.g_slist_copy.argtypes = [_GSList]
except:
   pass
try:
    libgtk3.g_slist_concat.restype = _GSList
    libgtk3.g_slist_concat.argtypes = [_GSList,_GSList]
except:
   pass
try:
    libgtk3.g_slist_nth.restype = _GSList
    libgtk3.g_slist_nth.argtypes = [_GSList,guint]
except:
   pass
try:
    libgtk3.g_slist_free_full.restype = None
    libgtk3.g_slist_free_full.argtypes = [_GSList,GDestroyNotify]
except:
   pass
try:
    libgtk3.g_slist_position.restype = gint
    libgtk3.g_slist_position.argtypes = [_GSList,_GSList]
except:
   pass
try:
    libgtk3.g_slist_remove.restype = _GSList
    libgtk3.g_slist_remove.argtypes = [_GSList,gconstpointer]
except:
   pass
try:
    libgtk3.g_slist_insert.restype = _GSList
    libgtk3.g_slist_insert.argtypes = [_GSList,gpointer,gint]
except:
   pass
try:
    libgtk3.g_slist_last.restype = _GSList
    libgtk3.g_slist_last.argtypes = [_GSList]
except:
   pass
try:
    libgtk3.g_slist_reverse.restype = _GSList
    libgtk3.g_slist_reverse.argtypes = [_GSList]
except:
   pass
try:
    libgtk3.g_slist_find_custom.restype = _GSList
    libgtk3.g_slist_find_custom.argtypes = [_GSList,gconstpointer,GCompareFunc]
except:
   pass
try:
    libgtk3.g_slist_sort.restype = _GSList
    libgtk3.g_slist_sort.argtypes = [_GSList,GCompareFunc]
except:
   pass
try:
    libgtk3.g_slist_delete_link.restype = _GSList
    libgtk3.g_slist_delete_link.argtypes = [_GSList,_GSList]
except:
   pass
try:
    libgtk3.g_slist_length.restype = guint
    libgtk3.g_slist_length.argtypes = [_GSList]
except:
   pass
try:
    libgtk3.g_slist_free_1.restype = None
    libgtk3.g_slist_free_1.argtypes = [_GSList]
except:
   pass
try:
    libgtk3.g_slist_insert_sorted.restype = _GSList
    libgtk3.g_slist_insert_sorted.argtypes = [_GSList,gpointer,GCompareFunc]
except:
   pass
try:
    libgtk3.g_slist_remove_all.restype = _GSList
    libgtk3.g_slist_remove_all.argtypes = [_GSList,gconstpointer]
except:
   pass
try:
    libgtk3.g_slist_sort_with_data.restype = _GSList
    libgtk3.g_slist_sort_with_data.argtypes = [_GSList,GCompareDataFunc,gpointer]
except:
   pass
try:
    libgtk3.g_slist_find.restype = _GSList
    libgtk3.g_slist_find.argtypes = [_GSList,gconstpointer]
except:
   pass
try:
    libgtk3.g_slist_append.restype = _GSList
    libgtk3.g_slist_append.argtypes = [_GSList,gpointer]
except:
   pass
try:
    libgtk3.g_slist_remove_link.restype = _GSList
    libgtk3.g_slist_remove_link.argtypes = [_GSList,_GSList]
except:
   pass
try:
    libgtk3.g_slist_copy_deep.restype = _GSList
    libgtk3.g_slist_copy_deep.argtypes = [_GSList,GCopyFunc,gpointer]
except:
   pass
try:
    libgtk3.g_slist_prepend.restype = _GSList
    libgtk3.g_slist_prepend.argtypes = [_GSList,gpointer]
except:
   pass
try:
    libgtk3.g_slist_index.restype = gint
    libgtk3.g_slist_index.argtypes = [_GSList,gconstpointer]
except:
   pass
try:
    libgtk3.g_slist_nth_data.restype = gpointer
    libgtk3.g_slist_nth_data.argtypes = [_GSList,guint]
except:
   pass
try:
    libgtk3.g_slist_foreach.restype = None
    libgtk3.g_slist_foreach.argtypes = [_GSList,GFunc,gpointer]
except:
   pass
try:
    libgtk3.g_slist_alloc.restype = _GSList
    libgtk3.g_slist_alloc.argtypes = []
except:
   pass
class GSList( object):
    """Class GSList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def g_slist_insert_before(  self, sibling, data, ):
        if sibling: sibling = sibling._object
        else: sibling = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None,None, obj=libgtk3.g_slist_insert_before( self._object,sibling,data ) or POINTER(c_void_p)())

    def g_slist_free(  self, ):

        
        libgtk3.g_slist_free( self._object )

    def g_slist_insert_sorted_with_data(  self, data, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None,None,None, obj=libgtk3.g_slist_insert_sorted_with_data( self._object,data,func,user_data ) or POINTER(c_void_p)())

    def g_slist_copy(  self, ):

        from .gobject import GSList
        return GSList( obj=libgtk3.g_slist_copy( self._object ) or POINTER(c_void_p)())

    def g_slist_concat(  self, list2, ):
        if list2: list2 = list2._object
        else: list2 = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_concat( self._object,list2 ) or POINTER(c_void_p)())

    def g_slist_nth(  self, n, ):

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_nth( self._object,n ) or POINTER(c_void_p)())

    def g_slist_free_full(  self, free_func, ):

        
        libgtk3.g_slist_free_full( self._object,free_func )

    def g_slist_position(  self, llink, ):
        if llink: llink = llink._object
        else: llink = POINTER(c_void_p)()

        
        return libgtk3.g_slist_position( self._object,llink )

    def g_slist_remove(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_remove( self._object,data ) or POINTER(c_void_p)())

    def g_slist_insert(  self, data, position, ):

        from .gobject import GSList
        return GSList(None,None, obj=libgtk3.g_slist_insert( self._object,data,position ) or POINTER(c_void_p)())

    def g_slist_last(  self, ):

        from .gobject import GSList
        return GSList( obj=libgtk3.g_slist_last( self._object ) or POINTER(c_void_p)())

    def g_slist_reverse(  self, ):

        from .gobject import GSList
        return GSList( obj=libgtk3.g_slist_reverse( self._object ) or POINTER(c_void_p)())

    def g_slist_find_custom(  self, data, func, ):
        if func: func = func._object
        else: func = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None,None, obj=libgtk3.g_slist_find_custom( self._object,data,func ) or POINTER(c_void_p)())

    def g_slist_sort(  self, compare_func, ):
        if compare_func: compare_func = compare_func._object
        else: compare_func = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_sort( self._object,compare_func ) or POINTER(c_void_p)())

    def g_slist_delete_link(  self, link_, ):
        if link_: link_ = link_._object
        else: link_ = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_delete_link( self._object,link_ ) or POINTER(c_void_p)())

    def g_slist_length(  self, ):

        
        return libgtk3.g_slist_length( self._object )

    def g_slist_free_1(  self, ):

        
        libgtk3.g_slist_free_1( self._object )

    def g_slist_insert_sorted(  self, data, func, ):
        if func: func = func._object
        else: func = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None,None, obj=libgtk3.g_slist_insert_sorted( self._object,data,func ) or POINTER(c_void_p)())

    def g_slist_remove_all(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_remove_all( self._object,data ) or POINTER(c_void_p)())

    def g_slist_sort_with_data(  self, compare_func, user_data, ):
        if compare_func: compare_func = compare_func._object
        else: compare_func = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None,None, obj=libgtk3.g_slist_sort_with_data( self._object,compare_func,user_data ) or POINTER(c_void_p)())

    def g_slist_find(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_find( self._object,data ) or POINTER(c_void_p)())

    def g_slist_append(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_append( self._object,data ) or POINTER(c_void_p)())

    def g_slist_remove_link(  self, link_, ):
        if link_: link_ = link_._object
        else: link_ = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_remove_link( self._object,link_ ) or POINTER(c_void_p)())

    def g_slist_copy_deep(  self, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_void_p)()

        from .gobject import GSList
        return GSList(None,None, obj=libgtk3.g_slist_copy_deep( self._object,func,user_data ) or POINTER(c_void_p)())

    def g_slist_prepend(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgtk3.g_slist_prepend( self._object,data ) or POINTER(c_void_p)())

    def g_slist_index(  self, data, ):

        
        return libgtk3.g_slist_index( self._object,data )

    def g_slist_nth_data(  self, n, ):

        
        return libgtk3.g_slist_nth_data( self._object,n )

    def g_slist_foreach(  self, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_void_p)()

        
        libgtk3.g_slist_foreach( self._object,func,user_data )

    @staticmethod
    def g_slist_alloc():
        from .gobject import GSList
        return GSList( obj=    libgtk3.g_slist_alloc()
 or POINTER(c_void_p)())
