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
_PangoContext = POINTER(c_int)
__GParamSpec = POINTER(c_int)
_GdkVisual = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
__GList = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
__GdkColor = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__GdkWMDecoration = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_PangoLayout = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GdkVisual = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__GdkCursor = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GtkWindow = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
_GdkScreen = POINTER(c_int)
__GValue = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GdkCursor = POINTER(c_int)
__PangoLayout = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
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

class GList( object):
    """Class GList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def copy(  self, ):

        libgtk3.g_list_copy.restype = _GList
        libgtk3.g_list_copy.argtypes = [_GList]
        from gobject import GList
        return GList( obj=libgtk3.g_list_copy( self._object ) or POINTER(c_int)())

    def remove_all(  self, data, ):

        libgtk3.g_list_remove_all.restype = _GList
        libgtk3.g_list_remove_all.argtypes = [_GList,gpointer]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_remove_all( self._object,data ) or POINTER(c_int)())

    def sort_with_data(  self, compare_func, user_data, ):
        if compare_func: compare_func = compare_func._object
        else: compare_func = POINTER(c_int)()

        libgtk3.g_list_sort_with_data.restype = _GList
        libgtk3.g_list_sort_with_data.argtypes = [_GList,GCompareDataFunc,gpointer]
        from gobject import GList
        return GList(None,None, obj=libgtk3.g_list_sort_with_data( self._object,compare_func,user_data ) or POINTER(c_int)())

    def index(  self, data, ):

        libgtk3.g_list_index.restype = gint
        libgtk3.g_list_index.argtypes = [_GList,gpointer]
        
        return libgtk3.g_list_index( self._object,data )

    def nth_prev(  self, n, ):

        libgtk3.g_list_nth_prev.restype = _GList
        libgtk3.g_list_nth_prev.argtypes = [_GList,guint]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_nth_prev( self._object,n ) or POINTER(c_int)())

    def length(  self, ):

        libgtk3.g_list_length.restype = guint
        libgtk3.g_list_length.argtypes = [_GList]
        
        return libgtk3.g_list_length( self._object )

    def insert(  self, data, position, ):

        libgtk3.g_list_insert.restype = _GList
        libgtk3.g_list_insert.argtypes = [_GList,gpointer,gint]
        from gobject import GList
        return GList(None,None, obj=libgtk3.g_list_insert( self._object,data,position ) or POINTER(c_int)())

    def prepend(  self, data, ):

        libgtk3.g_list_prepend.restype = _GList
        libgtk3.g_list_prepend.argtypes = [_GList,gpointer]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_prepend( self._object,data ) or POINTER(c_int)())

    def reverse(  self, ):

        libgtk3.g_list_reverse.restype = _GList
        libgtk3.g_list_reverse.argtypes = [_GList]
        from gobject import GList
        return GList( obj=libgtk3.g_list_reverse( self._object ) or POINTER(c_int)())

    def find(  self, data, ):

        libgtk3.g_list_find.restype = _GList
        libgtk3.g_list_find.argtypes = [_GList,gpointer]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_find( self._object,data ) or POINTER(c_int)())

    def remove(  self, data, ):

        libgtk3.g_list_remove.restype = _GList
        libgtk3.g_list_remove.argtypes = [_GList,gpointer]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_remove( self._object,data ) or POINTER(c_int)())

    def delete_link(  self, link_, ):
        if link_: link_ = link_._object
        else: link_ = POINTER(c_int)()

        libgtk3.g_list_delete_link.restype = _GList
        libgtk3.g_list_delete_link.argtypes = [_GList,_GList]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_delete_link( self._object,link_ ) or POINTER(c_int)())

    def append(  self, data, ):

        libgtk3.g_list_append.restype = _GList
        libgtk3.g_list_append.argtypes = [_GList,gpointer]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_append( self._object,data ) or POINTER(c_int)())

    def free(  self, ):

        libgtk3.g_list_free.argtypes = [_GList]
        
        libgtk3.g_list_free( self._object )

    def remove_link(  self, llink, ):
        if llink: llink = llink._object
        else: llink = POINTER(c_int)()

        libgtk3.g_list_remove_link.restype = _GList
        libgtk3.g_list_remove_link.argtypes = [_GList,_GList]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_remove_link( self._object,llink ) or POINTER(c_int)())

    def nth_data(  self, n, ):

        libgtk3.g_list_nth_data.restype = gpointer
        libgtk3.g_list_nth_data.argtypes = [_GList,guint]
        
        return libgtk3.g_list_nth_data( self._object,n )

    def nth(  self, n, ):

        libgtk3.g_list_nth.restype = _GList
        libgtk3.g_list_nth.argtypes = [_GList,guint]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_nth( self._object,n ) or POINTER(c_int)())

    def insert_sorted(  self, data, func, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgtk3.g_list_insert_sorted.restype = _GList
        libgtk3.g_list_insert_sorted.argtypes = [_GList,gpointer,GCompareFunc]
        from gobject import GList
        return GList(None,None, obj=libgtk3.g_list_insert_sorted( self._object,data,func ) or POINTER(c_int)())

    def foreach(  self, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgtk3.g_list_foreach.argtypes = [_GList,GFunc,gpointer]
        
        libgtk3.g_list_foreach( self._object,func,user_data )

    def concat(  self, list2, ):
        if list2: list2 = list2._object
        else: list2 = POINTER(c_int)()

        libgtk3.g_list_concat.restype = _GList
        libgtk3.g_list_concat.argtypes = [_GList,_GList]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_concat( self._object,list2 ) or POINTER(c_int)())

    def free_1(  self, ):

        libgtk3.g_list_free_1.argtypes = [_GList]
        
        libgtk3.g_list_free_1( self._object )

    def position(  self, llink, ):
        if llink: llink = llink._object
        else: llink = POINTER(c_int)()

        libgtk3.g_list_position.restype = gint
        libgtk3.g_list_position.argtypes = [_GList,_GList]
        
        return libgtk3.g_list_position( self._object,llink )

    def find_custom(  self, data, func, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgtk3.g_list_find_custom.restype = _GList
        libgtk3.g_list_find_custom.argtypes = [_GList,gpointer,GCompareFunc]
        from gobject import GList
        return GList(None,None, obj=libgtk3.g_list_find_custom( self._object,data,func ) or POINTER(c_int)())

    def last(  self, ):

        libgtk3.g_list_last.restype = _GList
        libgtk3.g_list_last.argtypes = [_GList]
        from gobject import GList
        return GList( obj=libgtk3.g_list_last( self._object ) or POINTER(c_int)())

    def first(  self, ):

        libgtk3.g_list_first.restype = _GList
        libgtk3.g_list_first.argtypes = [_GList]
        from gobject import GList
        return GList( obj=libgtk3.g_list_first( self._object ) or POINTER(c_int)())

    def free_full(  self, free_func, ):

        libgtk3.g_list_free_full.argtypes = [_GList,GDestroyNotify]
        
        libgtk3.g_list_free_full( self._object,free_func )

    def insert_sorted_with_data(  self, data, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgtk3.g_list_insert_sorted_with_data.restype = _GList
        libgtk3.g_list_insert_sorted_with_data.argtypes = [_GList,gpointer,GCompareDataFunc,gpointer]
        from gobject import GList
        return GList(None,None,None, obj=libgtk3.g_list_insert_sorted_with_data( self._object,data,func,user_data ) or POINTER(c_int)())

    def insert_before(  self, sibling, data, ):
        if sibling: sibling = sibling._object
        else: sibling = POINTER(c_int)()

        libgtk3.g_list_insert_before.restype = _GList
        libgtk3.g_list_insert_before.argtypes = [_GList,_GList,gpointer]
        from gobject import GList
        return GList(None,None, obj=libgtk3.g_list_insert_before( self._object,sibling,data ) or POINTER(c_int)())

    def sort(  self, compare_func, ):
        if compare_func: compare_func = compare_func._object
        else: compare_func = POINTER(c_int)()

        libgtk3.g_list_sort.restype = _GList
        libgtk3.g_list_sort.argtypes = [_GList,GCompareFunc]
        from gobject import GList
        return GList(None, obj=libgtk3.g_list_sort( self._object,compare_func ) or POINTER(c_int)())

    @staticmethod
    def alloc():
        libgtk3.g_list_alloc.restype = _GList
        from gobject import GList
        return GList( obj=    libgtk3.g_list_alloc()
 or POINTER(c_int)())
