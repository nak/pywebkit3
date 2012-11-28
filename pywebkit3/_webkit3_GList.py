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
_GdkVisual = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GActionGroup = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
_JSContext = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
__GList = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
__GCancellable = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_GBytes = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
__GFile = POINTER(c_int)
__GError = POINTER(c_int)
__GtkPrintOperation = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GByteArray = POINTER(c_int)
"""Enumerations"""
GdkVisualType = c_int
GdkByteOrder = c_int
GApplicationFlags = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitLoadStatus = c_int

class GList( object):
    """Class GList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def copy(  self, ):

        libwebkit3.g_list_copy.restype = _GList
        libwebkit3.g_list_copy.argtypes = [_GList]
        from pywebkit3.gobject import GList
        return GList( obj=libwebkit3.g_list_copy( self._object ) or POINTER(c_int)())

    def remove_all(  self, data, ):

        libwebkit3.g_list_remove_all.restype = _GList
        libwebkit3.g_list_remove_all.argtypes = [_GList,gpointer]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_remove_all( self._object,data ) or POINTER(c_int)())

    def sort_with_data(  self, compare_func, user_data, ):
        if compare_func    : compare_func = compare_func._object
        else    : compare_func = POINTER(c_int)()

        libwebkit3.g_list_sort_with_data.restype = _GList
        libwebkit3.g_list_sort_with_data.argtypes = [_GList,GCompareDataFunc,gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libwebkit3.g_list_sort_with_data( self._object,compare_func,user_data ) or POINTER(c_int)())

    def index(  self, data, ):

        libwebkit3.g_list_index.restype = gint
        libwebkit3.g_list_index.argtypes = [_GList,gpointer]
        
        return libwebkit3.g_list_index( self._object,data )

    def nth_prev(  self, n, ):

        libwebkit3.g_list_nth_prev.restype = _GList
        libwebkit3.g_list_nth_prev.argtypes = [_GList,guint]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_nth_prev( self._object,n ) or POINTER(c_int)())

    def length(  self, ):

        libwebkit3.g_list_length.restype = guint
        libwebkit3.g_list_length.argtypes = [_GList]
        
        return libwebkit3.g_list_length( self._object )

    def insert(  self, data, position, ):

        libwebkit3.g_list_insert.restype = _GList
        libwebkit3.g_list_insert.argtypes = [_GList,gpointer,gint]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libwebkit3.g_list_insert( self._object,data,position ) or POINTER(c_int)())

    def prepend(  self, data, ):

        libwebkit3.g_list_prepend.restype = _GList
        libwebkit3.g_list_prepend.argtypes = [_GList,gpointer]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_prepend( self._object,data ) or POINTER(c_int)())

    def reverse(  self, ):

        libwebkit3.g_list_reverse.restype = _GList
        libwebkit3.g_list_reverse.argtypes = [_GList]
        from pywebkit3.gobject import GList
        return GList( obj=libwebkit3.g_list_reverse( self._object ) or POINTER(c_int)())

    def find(  self, data, ):

        libwebkit3.g_list_find.restype = _GList
        libwebkit3.g_list_find.argtypes = [_GList,gpointer]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_find( self._object,data ) or POINTER(c_int)())

    def remove(  self, data, ):

        libwebkit3.g_list_remove.restype = _GList
        libwebkit3.g_list_remove.argtypes = [_GList,gpointer]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_remove( self._object,data ) or POINTER(c_int)())

    def delete_link(  self, link_, ):
        if link_    : link_ = link_._object
        else    : link_ = POINTER(c_int)()

        libwebkit3.g_list_delete_link.restype = _GList
        libwebkit3.g_list_delete_link.argtypes = [_GList,_GList]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_delete_link( self._object,link_ ) or POINTER(c_int)())

    def append(  self, data, ):

        libwebkit3.g_list_append.restype = _GList
        libwebkit3.g_list_append.argtypes = [_GList,gpointer]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_append( self._object,data ) or POINTER(c_int)())

    def free(  self, ):

        libwebkit3.g_list_free.argtypes = [_GList]
        
        libwebkit3.g_list_free( self._object )

    def remove_link(  self, llink, ):
        if llink    : llink = llink._object
        else    : llink = POINTER(c_int)()

        libwebkit3.g_list_remove_link.restype = _GList
        libwebkit3.g_list_remove_link.argtypes = [_GList,_GList]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_remove_link( self._object,llink ) or POINTER(c_int)())

    def nth_data(  self, n, ):

        libwebkit3.g_list_nth_data.restype = gpointer
        libwebkit3.g_list_nth_data.argtypes = [_GList,guint]
        
        return libwebkit3.g_list_nth_data( self._object,n )

    def nth(  self, n, ):

        libwebkit3.g_list_nth.restype = _GList
        libwebkit3.g_list_nth.argtypes = [_GList,guint]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_nth( self._object,n ) or POINTER(c_int)())

    def insert_sorted(  self, data, func, ):
        if func    : func = func._object
        else    : func = POINTER(c_int)()

        libwebkit3.g_list_insert_sorted.restype = _GList
        libwebkit3.g_list_insert_sorted.argtypes = [_GList,gpointer,GCompareFunc]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libwebkit3.g_list_insert_sorted( self._object,data,func ) or POINTER(c_int)())

    def foreach(  self, func, user_data, ):
        if func    : func = func._object
        else    : func = POINTER(c_int)()

        libwebkit3.g_list_foreach.argtypes = [_GList,GFunc,gpointer]
        
        libwebkit3.g_list_foreach( self._object,func,user_data )

    def concat(  self, list2, ):
        if list2    : list2 = list2._object
        else    : list2 = POINTER(c_int)()

        libwebkit3.g_list_concat.restype = _GList
        libwebkit3.g_list_concat.argtypes = [_GList,_GList]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_concat( self._object,list2 ) or POINTER(c_int)())

    def free_1(  self, ):

        libwebkit3.g_list_free_1.argtypes = [_GList]
        
        libwebkit3.g_list_free_1( self._object )

    def position(  self, llink, ):
        if llink    : llink = llink._object
        else    : llink = POINTER(c_int)()

        libwebkit3.g_list_position.restype = gint
        libwebkit3.g_list_position.argtypes = [_GList,_GList]
        
        return libwebkit3.g_list_position( self._object,llink )

    def find_custom(  self, data, func, ):
        if func    : func = func._object
        else    : func = POINTER(c_int)()

        libwebkit3.g_list_find_custom.restype = _GList
        libwebkit3.g_list_find_custom.argtypes = [_GList,gpointer,GCompareFunc]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libwebkit3.g_list_find_custom( self._object,data,func ) or POINTER(c_int)())

    def last(  self, ):

        libwebkit3.g_list_last.restype = _GList
        libwebkit3.g_list_last.argtypes = [_GList]
        from pywebkit3.gobject import GList
        return GList( obj=libwebkit3.g_list_last( self._object ) or POINTER(c_int)())

    def first(  self, ):

        libwebkit3.g_list_first.restype = _GList
        libwebkit3.g_list_first.argtypes = [_GList]
        from pywebkit3.gobject import GList
        return GList( obj=libwebkit3.g_list_first( self._object ) or POINTER(c_int)())

    def free_full(  self, free_func, ):

        libwebkit3.g_list_free_full.argtypes = [_GList,GDestroyNotify]
        
        libwebkit3.g_list_free_full( self._object,free_func )

    def insert_sorted_with_data(  self, data, func, user_data, ):
        if func    : func = func._object
        else    : func = POINTER(c_int)()

        libwebkit3.g_list_insert_sorted_with_data.restype = _GList
        libwebkit3.g_list_insert_sorted_with_data.argtypes = [_GList,gpointer,GCompareDataFunc,gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None,None, obj=libwebkit3.g_list_insert_sorted_with_data( self._object,data,func,user_data ) or POINTER(c_int)())

    def insert_before(  self, sibling, data, ):
        if sibling    : sibling = sibling._object
        else    : sibling = POINTER(c_int)()

        libwebkit3.g_list_insert_before.restype = _GList
        libwebkit3.g_list_insert_before.argtypes = [_GList,_GList,gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libwebkit3.g_list_insert_before( self._object,sibling,data ) or POINTER(c_int)())

    def sort(  self, compare_func, ):
        if compare_func    : compare_func = compare_func._object
        else    : compare_func = POINTER(c_int)()

        libwebkit3.g_list_sort.restype = _GList
        libwebkit3.g_list_sort.argtypes = [_GList,GCompareFunc]
        from pywebkit3.gobject import GList
        return GList(None, obj=libwebkit3.g_list_sort( self._object,compare_func ) or POINTER(c_int)())

    @staticmethod
    def alloc():
        libwebkit3.g_list_alloc.restype = _GList
        return libwebkit3.g_list_alloc()

