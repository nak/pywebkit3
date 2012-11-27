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
__GSList = c_void_p
_GSList = c_void_p
"""Enumerations"""

class GSList( object):
    """Class GSList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def g_slist_insert_before(self,  sibling, data,):
        if sibling : sibling = sibling._object
        else : sibling = c_void_p()

        libgobject.g_slist_insert_before.restype = _GSList
        libgobject.g_slist_insert_before.argtypes = [c_void_p, _GSList,gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None,None, obj=libgobject.g_slist_insert_before(self._object,  sibling, data,) or c_void_p())

    def g_slist_free(self, ):

        libgobject.g_slist_free.argtypes = [c_void_p]
        
        libgobject.g_slist_free(self._object, )

    def g_slist_insert_sorted_with_data(self,  data, func, user_data,):
        if func : func = func._object
        else : func = c_void_p()

        libgobject.g_slist_insert_sorted_with_data.restype = _GSList
        libgobject.g_slist_insert_sorted_with_data.argtypes = [c_void_p, gpointer,GCompareDataFunc,gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None,None,None, obj=libgobject.g_slist_insert_sorted_with_data(self._object,  data, func, user_data,) or c_void_p())

    def g_slist_copy(self, ):

        libgobject.g_slist_copy.restype = _GSList
        libgobject.g_slist_copy.argtypes = [c_void_p]
        from pywebkit3.gobject import GSList
        return GSList(None, obj=libgobject.g_slist_copy(self._object, ) or c_void_p())

    def g_slist_concat(self,  list2,):
        if list2 : list2 = list2._object
        else : list2 = c_void_p()

        libgobject.g_slist_concat.restype = _GSList
        libgobject.g_slist_concat.argtypes = [c_void_p, _GSList]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_concat(self._object,  list2,) or c_void_p())

    def g_slist_nth(self,  n,):

        libgobject.g_slist_nth.restype = _GSList
        libgobject.g_slist_nth.argtypes = [c_void_p, guint]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_nth(self._object,  n,) or c_void_p())

    def g_slist_free_full(self,  free_func,):

        libgobject.g_slist_free_full.argtypes = [c_void_p, GDestroyNotify]
        
        libgobject.g_slist_free_full(self._object,  free_func,)

    def g_slist_position(self,  llink,):
        if llink : llink = llink._object
        else : llink = c_void_p()

        libgobject.g_slist_position.restype = gint
        libgobject.g_slist_position.argtypes = [c_void_p, _GSList]
        
        return libgobject.g_slist_position(self._object,  llink,)

    def g_slist_remove(self,  data,):

        libgobject.g_slist_remove.restype = _GSList
        libgobject.g_slist_remove.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_remove(self._object,  data,) or c_void_p())

    def g_slist_insert(self,  data, position,):

        libgobject.g_slist_insert.restype = _GSList
        libgobject.g_slist_insert.argtypes = [c_void_p, gpointer,gint]
        from pywebkit3.gobject import GSList
        return GSList(None,None,None, obj=libgobject.g_slist_insert(self._object,  data, position,) or c_void_p())

    def g_slist_last(self, ):

        libgobject.g_slist_last.restype = _GSList
        libgobject.g_slist_last.argtypes = [c_void_p]
        from pywebkit3.gobject import GSList
        return GSList(None, obj=libgobject.g_slist_last(self._object, ) or c_void_p())

    def g_slist_reverse(self, ):

        libgobject.g_slist_reverse.restype = _GSList
        libgobject.g_slist_reverse.argtypes = [c_void_p]
        from pywebkit3.gobject import GSList
        return GSList(None, obj=libgobject.g_slist_reverse(self._object, ) or c_void_p())

    def g_slist_find_custom(self,  data, func,):
        if func : func = func._object
        else : func = c_void_p()

        libgobject.g_slist_find_custom.restype = _GSList
        libgobject.g_slist_find_custom.argtypes = [c_void_p, gpointer,GCompareFunc]
        from pywebkit3.gobject import GSList
        return GSList(None,None,None, obj=libgobject.g_slist_find_custom(self._object,  data, func,) or c_void_p())

    def g_slist_sort(self,  compare_func,):
        if compare_func : compare_func = compare_func._object
        else : compare_func = c_void_p()

        libgobject.g_slist_sort.restype = _GSList
        libgobject.g_slist_sort.argtypes = [c_void_p, GCompareFunc]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_sort(self._object,  compare_func,) or c_void_p())

    def g_slist_delete_link(self,  link_,):
        if link_ : link_ = link_._object
        else : link_ = c_void_p()

        libgobject.g_slist_delete_link.restype = _GSList
        libgobject.g_slist_delete_link.argtypes = [c_void_p, _GSList]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_delete_link(self._object,  link_,) or c_void_p())

    def g_slist_length(self, ):

        libgobject.g_slist_length.restype = guint
        libgobject.g_slist_length.argtypes = [c_void_p]
        
        return libgobject.g_slist_length(self._object, )

    def g_slist_free_1(self, ):

        libgobject.g_slist_free_1.argtypes = [c_void_p]
        
        libgobject.g_slist_free_1(self._object, )

    def g_slist_insert_sorted(self,  data, func,):
        if func : func = func._object
        else : func = c_void_p()

        libgobject.g_slist_insert_sorted.restype = _GSList
        libgobject.g_slist_insert_sorted.argtypes = [c_void_p, gpointer,GCompareFunc]
        from pywebkit3.gobject import GSList
        return GSList(None,None,None, obj=libgobject.g_slist_insert_sorted(self._object,  data, func,) or c_void_p())

    def g_slist_remove_all(self,  data,):

        libgobject.g_slist_remove_all.restype = _GSList
        libgobject.g_slist_remove_all.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_remove_all(self._object,  data,) or c_void_p())

    def g_slist_sort_with_data(self,  compare_func, user_data,):
        if compare_func : compare_func = compare_func._object
        else : compare_func = c_void_p()

        libgobject.g_slist_sort_with_data.restype = _GSList
        libgobject.g_slist_sort_with_data.argtypes = [c_void_p, GCompareDataFunc,gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None,None, obj=libgobject.g_slist_sort_with_data(self._object,  compare_func, user_data,) or c_void_p())

    def g_slist_find(self,  data,):

        libgobject.g_slist_find.restype = _GSList
        libgobject.g_slist_find.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_find(self._object,  data,) or c_void_p())

    def g_slist_append(self,  data,):

        libgobject.g_slist_append.restype = _GSList
        libgobject.g_slist_append.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_append(self._object,  data,) or c_void_p())

    def g_slist_remove_link(self,  link_,):
        if link_ : link_ = link_._object
        else : link_ = c_void_p()

        libgobject.g_slist_remove_link.restype = _GSList
        libgobject.g_slist_remove_link.argtypes = [c_void_p, _GSList]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_remove_link(self._object,  link_,) or c_void_p())

    def g_slist_copy_deep(self,  func, user_data,):
        if func : func = func._object
        else : func = c_void_p()

        libgobject.g_slist_copy_deep.restype = _GSList
        libgobject.g_slist_copy_deep.argtypes = [c_void_p, GCopyFunc,gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None,None, obj=libgobject.g_slist_copy_deep(self._object,  func, user_data,) or c_void_p())

    def g_slist_prepend(self,  data,):

        libgobject.g_slist_prepend.restype = _GSList
        libgobject.g_slist_prepend.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_prepend(self._object,  data,) or c_void_p())

    def g_slist_index(self,  data,):

        libgobject.g_slist_index.restype = gint
        libgobject.g_slist_index.argtypes = [c_void_p, gpointer]
        
        return libgobject.g_slist_index(self._object,  data,)

    def g_slist_nth_data(self,  n,):

        libgobject.g_slist_nth_data.restype = gpointer
        libgobject.g_slist_nth_data.argtypes = [c_void_p, guint]
        
        return libgobject.g_slist_nth_data(self._object,  n,)

    def g_slist_foreach(self,  func, user_data,):
        if func : func = func._object
        else : func = c_void_p()

        libgobject.g_slist_foreach.argtypes = [c_void_p, GFunc,gpointer]
        
        libgobject.g_slist_foreach(self._object,  func, user_data,)

    @staticmethod
    def g_slist_alloc():
        libgobject.g_slist_alloc.restype = _GSList
        return libgobject.g_slist_alloc()

