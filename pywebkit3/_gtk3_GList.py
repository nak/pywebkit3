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
_PangoContext = c_void_p
_PangoFontMap = c_void_p
__PangoAttrList = c_void_p
__GList = c_void_p
__PangoAttrIterator = c_void_p
_GSList = c_void_p
__PangoRectangle = c_void_p
_char = c_void_p
__PangoGlyphString = c_void_p
_PangoLogAttr = c_void_p
_PangoLayoutIter = c_void_p
__PangoFontFamily = c_void_p
__PangoContext = c_void_p
_PangoFontset = c_void_p
__PangoFontDescription = c_void_p
__PangoFontMap = c_void_p
__PangoLanguage = c_void_p
_PangoAttrList = c_void_p
__gunichar = c_void_p
__PangoLogAttr = c_void_p
_PangoLayout = c_void_p
_PangoMatrix = c_void_p
__PangoAnalysis = c_void_p
_PangoFontDescription = c_void_p
_GList = c_void_p
_PangoLayoutRun = c_void_p
_PangoFont = c_void_p
_PangoLayoutLine = c_void_p
__PangoTabArray = c_void_p
__PangoLayout = c_void_p
__PangoMatrix = c_void_p
_PangoLanguage = c_void_p
_PangoTabArray = c_void_p
_PangoFontMetrics = c_void_p
"""Enumerations"""
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int

class GList( object):
    """Class GList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def copy(self, ):

        libgtk3.g_list_copy.restype = _GList
        libgtk3.g_list_copy.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList(None, obj=libgtk3.g_list_copy(self._object, ) or c_void_p())

    def remove_all(self,  data,):

        libgtk3.g_list_remove_all.restype = _GList
        libgtk3.g_list_remove_all.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_remove_all(self._object,  data,) or c_void_p())

    def sort_with_data(self,  compare_func, user_data,):
        if compare_func : compare_func = compare_func._object
        else : compare_func = c_void_p()

        libgtk3.g_list_sort_with_data.restype = _GList
        libgtk3.g_list_sort_with_data.argtypes = [c_void_p, GCompareDataFunc,gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None,None, obj=libgtk3.g_list_sort_with_data(self._object,  compare_func, user_data,) or c_void_p())

    def index(self,  data,):

        libgtk3.g_list_index.restype = gint
        libgtk3.g_list_index.argtypes = [c_void_p, gpointer]
        
        return libgtk3.g_list_index(self._object,  data,)

    def nth_prev(self,  n,):

        libgtk3.g_list_nth_prev.restype = _GList
        libgtk3.g_list_nth_prev.argtypes = [c_void_p, guint]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_nth_prev(self._object,  n,) or c_void_p())

    def length(self, ):

        libgtk3.g_list_length.restype = guint
        libgtk3.g_list_length.argtypes = [c_void_p]
        
        return libgtk3.g_list_length(self._object, )

    def insert(self,  data, position,):

        libgtk3.g_list_insert.restype = _GList
        libgtk3.g_list_insert.argtypes = [c_void_p, gpointer,gint]
        from pywebkit3.gobject import GList
        return GList(None,None,None, obj=libgtk3.g_list_insert(self._object,  data, position,) or c_void_p())

    def prepend(self,  data,):

        libgtk3.g_list_prepend.restype = _GList
        libgtk3.g_list_prepend.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_prepend(self._object,  data,) or c_void_p())

    def reverse(self, ):

        libgtk3.g_list_reverse.restype = _GList
        libgtk3.g_list_reverse.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList(None, obj=libgtk3.g_list_reverse(self._object, ) or c_void_p())

    def find(self,  data,):

        libgtk3.g_list_find.restype = _GList
        libgtk3.g_list_find.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_find(self._object,  data,) or c_void_p())

    def remove(self,  data,):

        libgtk3.g_list_remove.restype = _GList
        libgtk3.g_list_remove.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_remove(self._object,  data,) or c_void_p())

    def delete_link(self,  link_,):
        if link_ : link_ = link_._object
        else : link_ = c_void_p()

        libgtk3.g_list_delete_link.restype = _GList
        libgtk3.g_list_delete_link.argtypes = [c_void_p, _GList]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_delete_link(self._object,  link_,) or c_void_p())

    def append(self,  data,):

        libgtk3.g_list_append.restype = _GList
        libgtk3.g_list_append.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_append(self._object,  data,) or c_void_p())

    def free(self, ):

        libgtk3.g_list_free.argtypes = [c_void_p]
        
        libgtk3.g_list_free(self._object, )

    def remove_link(self,  llink,):
        if llink : llink = llink._object
        else : llink = c_void_p()

        libgtk3.g_list_remove_link.restype = _GList
        libgtk3.g_list_remove_link.argtypes = [c_void_p, _GList]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_remove_link(self._object,  llink,) or c_void_p())

    def nth_data(self,  n,):

        libgtk3.g_list_nth_data.restype = gpointer
        libgtk3.g_list_nth_data.argtypes = [c_void_p, guint]
        
        return libgtk3.g_list_nth_data(self._object,  n,)

    def nth(self,  n,):

        libgtk3.g_list_nth.restype = _GList
        libgtk3.g_list_nth.argtypes = [c_void_p, guint]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_nth(self._object,  n,) or c_void_p())

    def insert_sorted(self,  data, func,):
        if func : func = func._object
        else : func = c_void_p()

        libgtk3.g_list_insert_sorted.restype = _GList
        libgtk3.g_list_insert_sorted.argtypes = [c_void_p, gpointer,GCompareFunc]
        from pywebkit3.gobject import GList
        return GList(None,None,None, obj=libgtk3.g_list_insert_sorted(self._object,  data, func,) or c_void_p())

    def foreach(self,  func, user_data,):
        if func : func = func._object
        else : func = c_void_p()

        libgtk3.g_list_foreach.argtypes = [c_void_p, GFunc,gpointer]
        
        libgtk3.g_list_foreach(self._object,  func, user_data,)

    def concat(self,  list2,):
        if list2 : list2 = list2._object
        else : list2 = c_void_p()

        libgtk3.g_list_concat.restype = _GList
        libgtk3.g_list_concat.argtypes = [c_void_p, _GList]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_concat(self._object,  list2,) or c_void_p())

    def free_1(self, ):

        libgtk3.g_list_free_1.argtypes = [c_void_p]
        
        libgtk3.g_list_free_1(self._object, )

    def position(self,  llink,):
        if llink : llink = llink._object
        else : llink = c_void_p()

        libgtk3.g_list_position.restype = gint
        libgtk3.g_list_position.argtypes = [c_void_p, _GList]
        
        return libgtk3.g_list_position(self._object,  llink,)

    def find_custom(self,  data, func,):
        if func : func = func._object
        else : func = c_void_p()

        libgtk3.g_list_find_custom.restype = _GList
        libgtk3.g_list_find_custom.argtypes = [c_void_p, gpointer,GCompareFunc]
        from pywebkit3.gobject import GList
        return GList(None,None,None, obj=libgtk3.g_list_find_custom(self._object,  data, func,) or c_void_p())

    def last(self, ):

        libgtk3.g_list_last.restype = _GList
        libgtk3.g_list_last.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList(None, obj=libgtk3.g_list_last(self._object, ) or c_void_p())

    def first(self, ):

        libgtk3.g_list_first.restype = _GList
        libgtk3.g_list_first.argtypes = [c_void_p]
        from pywebkit3.gobject import GList
        return GList(None, obj=libgtk3.g_list_first(self._object, ) or c_void_p())

    def free_full(self,  free_func,):

        libgtk3.g_list_free_full.argtypes = [c_void_p, GDestroyNotify]
        
        libgtk3.g_list_free_full(self._object,  free_func,)

    def insert_sorted_with_data(self,  data, func, user_data,):
        if func : func = func._object
        else : func = c_void_p()

        libgtk3.g_list_insert_sorted_with_data.restype = _GList
        libgtk3.g_list_insert_sorted_with_data.argtypes = [c_void_p, gpointer,GCompareDataFunc,gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None,None,None, obj=libgtk3.g_list_insert_sorted_with_data(self._object,  data, func, user_data,) or c_void_p())

    def insert_before(self,  sibling, data,):
        if sibling : sibling = sibling._object
        else : sibling = c_void_p()

        libgtk3.g_list_insert_before.restype = _GList
        libgtk3.g_list_insert_before.argtypes = [c_void_p, _GList,gpointer]
        from pywebkit3.gobject import GList
        return GList(None,None,None, obj=libgtk3.g_list_insert_before(self._object,  sibling, data,) or c_void_p())

    def sort(self,  compare_func,):
        if compare_func : compare_func = compare_func._object
        else : compare_func = c_void_p()

        libgtk3.g_list_sort.restype = _GList
        libgtk3.g_list_sort.argtypes = [c_void_p, GCompareFunc]
        from pywebkit3.gobject import GList
        return GList(None,None, obj=libgtk3.g_list_sort(self._object,  compare_func,) or c_void_p())

    @staticmethod
    def alloc():
        libgtk3.g_list_alloc.restype = _GList
        return libgtk3.g_list_alloc()

