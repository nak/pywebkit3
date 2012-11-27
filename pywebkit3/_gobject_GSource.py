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
_GMainContext = c_void_p
__GPollFD = c_void_p
__GSource = c_void_p
__GSourceFuncs = c_void_p
__GSourceCallbackFuncs = c_void_p
_char = c_void_p
__GTimeVal = c_void_p
__GMainContext = c_void_p
_GSource = c_void_p
"""Enumerations"""

import _gobject_GObject
class GSource( _gobject_GObject.GObject):
    """Class GSource Constructors"""
    def __init__( self, struct_size,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_source_new.restype = c_void_p

        libgobject.g_source_new.argtypes = [guint]
        self._object = libgobject.g_source_new(struct_size, )

    """Methods"""
    def remove_poll(self,  fd,):
        if fd : fd = fd._object
        else : fd = c_void_p()

        libgobject.g_source_remove_poll.argtypes = [c_void_p, _GPollFD]
        
        libgobject.g_source_remove_poll(self._object,  fd,)

    def set_callback_indirect(self,  callback_data, callback_funcs,):
        if callback_funcs : callback_funcs = callback_funcs._object
        else : callback_funcs = c_void_p()

        libgobject.g_source_set_callback_indirect.argtypes = [c_void_p, gpointer,_GSourceCallbackFuncs]
        
        libgobject.g_source_set_callback_indirect(self._object,  callback_data, callback_funcs,)

    def destroy(self, ):

        libgobject.g_source_destroy.argtypes = [c_void_p]
        
        libgobject.g_source_destroy(self._object, )

    def get_id(self, ):

        libgobject.g_source_get_id.restype = guint
        libgobject.g_source_get_id.argtypes = [c_void_p]
        
        return libgobject.g_source_get_id(self._object, )

    def get_context(self, ):

        libgobject.g_source_get_context.restype = _GMainContext
        libgobject.g_source_get_context.argtypes = [c_void_p]
        from pywebkit3.gobject import GMainContext
        return GMainContext(None,None, obj=libgobject.g_source_get_context(self._object, ) or c_void_p())

    def set_can_recurse(self,  can_recurse,):

        libgobject.g_source_set_can_recurse.argtypes = [c_void_p, gboolean]
        
        libgobject.g_source_set_can_recurse(self._object,  can_recurse,)

    def get_name(self, ):

        libgobject.g_source_get_name.restype = _char
        libgobject.g_source_get_name.argtypes = [c_void_p]
        
        return libgobject.g_source_get_name(self._object, )

    def get_priority(self, ):

        libgobject.g_source_get_priority.restype = gint
        libgobject.g_source_get_priority.argtypes = [c_void_p]
        
        return libgobject.g_source_get_priority(self._object, )

    def ref(self, ):

        libgobject.g_source_ref.restype = _GSource
        libgobject.g_source_ref.argtypes = [c_void_p]
        from pywebkit3.gobject import GSource
        return GSource(None, obj=libgobject.g_source_ref(self._object, ) or c_void_p())

    def remove_child_source(self,  child_source,):
        if child_source : child_source = child_source._object
        else : child_source = c_void_p()

        libgobject.g_source_remove_child_source.argtypes = [c_void_p, _GSource]
        
        libgobject.g_source_remove_child_source(self._object,  child_source,)

    def add_child_source(self,  child_source,):
        if child_source : child_source = child_source._object
        else : child_source = c_void_p()

        libgobject.g_source_add_child_source.argtypes = [c_void_p, _GSource]
        
        libgobject.g_source_add_child_source(self._object,  child_source,)

    def set_name(self,  name,):

        libgobject.g_source_set_name.argtypes = [c_void_p, c_char_p]
        
        libgobject.g_source_set_name(self._object,  name,)

    def get_can_recurse(self, ):

        libgobject.g_source_get_can_recurse.restype = gboolean
        libgobject.g_source_get_can_recurse.argtypes = [c_void_p]
        
        return libgobject.g_source_get_can_recurse(self._object, )

    def get_current_time(self,  timeval,):
        if timeval : timeval = timeval._object
        else : timeval = c_void_p()

        libgobject.g_source_get_current_time.argtypes = [c_void_p, _GTimeVal]
        
        libgobject.g_source_get_current_time(self._object,  timeval,)

    def is_destroyed(self, ):

        libgobject.g_source_is_destroyed.restype = gboolean
        libgobject.g_source_is_destroyed.argtypes = [c_void_p]
        
        return libgobject.g_source_is_destroyed(self._object, )

    def unref(self, ):

        libgobject.g_source_unref.argtypes = [c_void_p]
        
        libgobject.g_source_unref(self._object, )

    def add_poll(self,  fd,):
        if fd : fd = fd._object
        else : fd = c_void_p()

        libgobject.g_source_add_poll.argtypes = [c_void_p, _GPollFD]
        
        libgobject.g_source_add_poll(self._object,  fd,)

    def set_priority(self,  priority,):

        libgobject.g_source_set_priority.argtypes = [c_void_p, gint]
        
        libgobject.g_source_set_priority(self._object,  priority,)

    def set_funcs(self,  funcs,):
        if funcs : funcs = funcs._object
        else : funcs = c_void_p()

        libgobject.g_source_set_funcs.argtypes = [c_void_p, _GSourceFuncs]
        
        libgobject.g_source_set_funcs(self._object,  funcs,)

    def get_time(self, ):

        libgobject.g_source_get_time.restype = gint64
        libgobject.g_source_get_time.argtypes = [c_void_p]
        
        return libgobject.g_source_get_time(self._object, )

    def set_name_by_id(self,  tag, name,):

        libgobject.g_source_set_name_by_id.argtypes = [c_void_p, guint,c_char_p]
        
        libgobject.g_source_set_name_by_id(self._object,  tag, name,)

    def set_callback(self,  func, data, notify,):

        libgobject.g_source_set_callback.argtypes = [c_void_p, GSourceFunc,gpointer,GDestroyNotify]
        
        libgobject.g_source_set_callback(self._object,  func, data, notify,)

    def attach(self,  context,):
        if context : context = context._object
        else : context = c_void_p()

        libgobject.g_source_attach.restype = guint
        libgobject.g_source_attach.argtypes = [c_void_p, _GMainContext]
        
        return libgobject.g_source_attach(self._object,  context,)

    @staticmethod
    def remove_by_user_data( user_data,):
        libgobject.g_source_remove_by_user_data.restype = gboolean
        libgobject.g_source_remove_by_user_data.argtypes = [gpointer]
        return libgobject.g_source_remove_by_user_data(user_data, )

    @staticmethod
    def remove( tag,):
        libgobject.g_source_remove.restype = gboolean
        libgobject.g_source_remove.argtypes = [guint]
        return libgobject.g_source_remove(tag, )

    @staticmethod
    def remove_by_funcs_user_data( funcs, user_data,):
        if funcs : funcs = funcs._object
        else : funcs = c_void_p()
        libgobject.g_source_remove_by_funcs_user_data.restype = gboolean
        libgobject.g_source_remove_by_funcs_user_data.argtypes = [_GSourceFuncs,gpointer]
        return libgobject.g_source_remove_by_funcs_user_data(funcs, user_data, )

