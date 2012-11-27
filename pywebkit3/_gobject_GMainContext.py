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
__GCond = c_void_p
__GMutex = c_void_p
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
class GMainContext( _gobject_GObject.GObject):
    """Class GMainContext Constructors"""
    def __init__( self, pid,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_child_watch_source_new.restype = c_void_p
        if pid : pid = pid._object
        else : pid = c_void_p()

        libgobject.g_child_watch_source_new.argtypes = [GPid]
        self._object = libgobject.g_child_watch_source_new(pid, )

    """Methods"""
    def find_source_by_funcs_user_data(self,  funcs, user_data,):
        if funcs : funcs = funcs._object
        else : funcs = c_void_p()

        libgobject.g_main_context_find_source_by_funcs_user_data.restype = _GSource
        libgobject.g_main_context_find_source_by_funcs_user_data.argtypes = [c_void_p, _GSourceFuncs,gpointer]
        from pywebkit3.gobject import GSource
        return GSource(None, obj=libgobject.g_main_context_find_source_by_funcs_user_data(self._object,  funcs, user_data,) or c_void_p())

    def pending(self, ):

        libgobject.g_main_context_pending.restype = gboolean
        libgobject.g_main_context_pending.argtypes = [c_void_p]
        
        return libgobject.g_main_context_pending(self._object, )

    def remove_poll(self,  fd,):
        if fd : fd = fd._object
        else : fd = c_void_p()

        libgobject.g_main_context_remove_poll.argtypes = [c_void_p, _GPollFD]
        
        libgobject.g_main_context_remove_poll(self._object,  fd,)

    def add_poll(self,  fd, priority,):
        if fd : fd = fd._object
        else : fd = c_void_p()

        libgobject.g_main_context_add_poll.argtypes = [c_void_p, _GPollFD,gint]
        
        libgobject.g_main_context_add_poll(self._object,  fd, priority,)

    def query(self,  max_priority, timeout_, fds, n_fds,):
        if timeout_ : timeout_ = timeout_._object
        else : timeout_ = c_void_p()
        if fds : fds = fds._object
        else : fds = c_void_p()

        libgobject.g_main_context_query.restype = gint
        libgobject.g_main_context_query.argtypes = [c_void_p, gint,POITNER(gint),_GPollFD,gint]
        
        return libgobject.g_main_context_query(self._object,  max_priority, timeout_, fds, n_fds,)

    def dispatch(self, ):

        libgobject.g_main_context_dispatch.argtypes = [c_void_p]
        
        libgobject.g_main_context_dispatch(self._object, )

    def push_thread_default(self, ):

        libgobject.g_main_context_push_thread_default.argtypes = [c_void_p]
        
        libgobject.g_main_context_push_thread_default(self._object, )

    def invoke(self,  function, data,):

        libgobject.g_main_context_invoke.argtypes = [c_void_p, GSourceFunc,gpointer]
        
        libgobject.g_main_context_invoke(self._object,  function, data,)

    def find_source_by_id(self,  source_id,):

        libgobject.g_main_context_find_source_by_id.restype = _GSource
        libgobject.g_main_context_find_source_by_id.argtypes = [c_void_p, guint]
        from pywebkit3.gobject import GSource
        return GSource(None, obj=libgobject.g_main_context_find_source_by_id(self._object,  source_id,) or c_void_p())

    def check(self,  max_priority, fds, n_fds,):
        if fds : fds = fds._object
        else : fds = c_void_p()

        libgobject.g_main_context_check.restype = gint
        libgobject.g_main_context_check.argtypes = [c_void_p, gint,_GPollFD,gint]
        
        return libgobject.g_main_context_check(self._object,  max_priority, fds, n_fds,)

    def prepare(self,  priority,):
        if priority : priority = priority._object
        else : priority = c_void_p()

        libgobject.g_main_context_prepare.restype = gboolean
        libgobject.g_main_context_prepare.argtypes = [c_void_p, POITNER(gint)]
        
        return libgobject.g_main_context_prepare(self._object,  priority,)

    def get_poll_func(self, ):

        libgobject.g_main_context_get_poll_func.restype = GPollFunc
        libgobject.g_main_context_get_poll_func.argtypes = [c_void_p]
        
        return libgobject.g_main_context_get_poll_func(self._object, )

    def pop_thread_default(self, ):

        libgobject.g_main_context_pop_thread_default.argtypes = [c_void_p]
        
        libgobject.g_main_context_pop_thread_default(self._object, )

    def set_poll_func(self,  func,):

        libgobject.g_main_context_set_poll_func.argtypes = [c_void_p, GPollFunc]
        
        libgobject.g_main_context_set_poll_func(self._object,  func,)

    def wakeup(self, ):

        libgobject.g_main_context_wakeup.argtypes = [c_void_p]
        
        libgobject.g_main_context_wakeup(self._object, )

    def ref(self, ):

        libgobject.g_main_context_ref.restype = _GMainContext
        libgobject.g_main_context_ref.argtypes = [c_void_p]
        from pywebkit3.gobject import GMainContext
        return GMainContext(None, obj=libgobject.g_main_context_ref(self._object, ) or c_void_p())

    def wait(self,  cond, mutex,):
        if cond : cond = cond._object
        else : cond = c_void_p()
        if mutex : mutex = mutex._object
        else : mutex = c_void_p()

        libgobject.g_main_context_wait.restype = gboolean
        libgobject.g_main_context_wait.argtypes = [c_void_p, _GCond,_GMutex]
        
        return libgobject.g_main_context_wait(self._object,  cond, mutex,)

    def acquire(self, ):

        libgobject.g_main_context_acquire.restype = gboolean
        libgobject.g_main_context_acquire.argtypes = [c_void_p]
        
        return libgobject.g_main_context_acquire(self._object, )

    def release(self, ):

        libgobject.g_main_context_release.argtypes = [c_void_p]
        
        libgobject.g_main_context_release(self._object, )

    def unref(self, ):

        libgobject.g_main_context_unref.argtypes = [c_void_p]
        
        libgobject.g_main_context_unref(self._object, )

    def is_owner(self, ):

        libgobject.g_main_context_is_owner.restype = gboolean
        libgobject.g_main_context_is_owner.argtypes = [c_void_p]
        
        return libgobject.g_main_context_is_owner(self._object, )

    def iteration(self,  may_block,):

        libgobject.g_main_context_iteration.restype = gboolean
        libgobject.g_main_context_iteration.argtypes = [c_void_p, gboolean]
        
        return libgobject.g_main_context_iteration(self._object,  may_block,)

    def invoke_full(self,  priority, function, data, notify,):

        libgobject.g_main_context_invoke_full.argtypes = [c_void_p, gint,GSourceFunc,gpointer,GDestroyNotify]
        
        libgobject.g_main_context_invoke_full(self._object,  priority, function, data, notify,)

    def find_source_by_user_data(self,  user_data,):

        libgobject.g_main_context_find_source_by_user_data.restype = _GSource
        libgobject.g_main_context_find_source_by_user_data.argtypes = [c_void_p, gpointer]
        from pywebkit3.gobject import GSource
        return GSource(None, obj=libgobject.g_main_context_find_source_by_user_data(self._object,  user_data,) or c_void_p())

    @staticmethod
    def g_main_depth():
        libgobject.g_main_depth.restype = gint
        return libgobject.g_main_depth()

    @staticmethod
    def g_idle_add( function, data,):
        libgobject.g_idle_add.restype = guint
        libgobject.g_idle_add.argtypes = [GSourceFunc,gpointer]
        return libgobject.g_idle_add(function, data, )

    @staticmethod
    def g_timeout_add_seconds( interval, function, data,):
        libgobject.g_timeout_add_seconds.restype = guint
        libgobject.g_timeout_add_seconds.argtypes = [guint,GSourceFunc,gpointer]
        return libgobject.g_timeout_add_seconds(interval, function, data, )

    @staticmethod
    def g_main_current_source():
        libgobject.g_main_current_source.restype = _GSource
        return libgobject.g_main_current_source()

    @staticmethod
    def g_idle_source_new():
        libgobject.g_idle_source_new.restype = _GSource
        return libgobject.g_idle_source_new()

    @staticmethod
    def g_timeout_add_full( priority, interval, function, data, notify,):
        libgobject.g_timeout_add_full.restype = guint
        libgobject.g_timeout_add_full.argtypes = [gint,guint,GSourceFunc,gpointer,GDestroyNotify]
        return libgobject.g_timeout_add_full(priority, interval, function, data, notify, )

    @staticmethod
    def default():
        libgobject.g_main_context_default.restype = _GMainContext
        return libgobject.g_main_context_default()

    @staticmethod
    def g_timeout_add( interval, function, data,):
        libgobject.g_timeout_add.restype = guint
        libgobject.g_timeout_add.argtypes = [guint,GSourceFunc,gpointer]
        return libgobject.g_timeout_add(interval, function, data, )

    @staticmethod
    def g_idle_remove_by_data( data,):
        libgobject.g_idle_remove_by_data.restype = gboolean
        libgobject.g_idle_remove_by_data.argtypes = [gpointer]
        return libgobject.g_idle_remove_by_data(data, )

    @staticmethod
    def g_child_watch_add_full( priority, pid, function, data, notify,):
        if pid : pid = pid._object
        else : pid = c_void_p()
        if function : function = function._object
        else : function = c_void_p()
        libgobject.g_child_watch_add_full.restype = guint
        libgobject.g_child_watch_add_full.argtypes = [gint,GPid,GChildWatchFunc,gpointer,GDestroyNotify]
        return libgobject.g_child_watch_add_full(priority, pid, function, data, notify, )

    @staticmethod
    def g_timeout_source_new_seconds( interval,):
        libgobject.g_timeout_source_new_seconds.restype = _GSource
        libgobject.g_timeout_source_new_seconds.argtypes = [guint]
        return libgobject.g_timeout_source_new_seconds(interval, )

    @staticmethod
    def g_timeout_add_seconds_full( priority, interval, function, data, notify,):
        libgobject.g_timeout_add_seconds_full.restype = guint
        libgobject.g_timeout_add_seconds_full.argtypes = [gint,guint,GSourceFunc,gpointer,GDestroyNotify]
        return libgobject.g_timeout_add_seconds_full(priority, interval, function, data, notify, )

    @staticmethod
    def g_idle_add_full( priority, function, data, notify,):
        libgobject.g_idle_add_full.restype = guint
        libgobject.g_idle_add_full.argtypes = [gint,GSourceFunc,gpointer,GDestroyNotify]
        return libgobject.g_idle_add_full(priority, function, data, notify, )

    @staticmethod
    def g_child_watch_add( pid, function, data,):
        if pid : pid = pid._object
        else : pid = c_void_p()
        if function : function = function._object
        else : function = c_void_p()
        libgobject.g_child_watch_add.restype = guint
        libgobject.g_child_watch_add.argtypes = [GPid,GChildWatchFunc,gpointer]
        return libgobject.g_child_watch_add(pid, function, data, )

    @staticmethod
    def get_thread_default():
        libgobject.g_main_context_get_thread_default.restype = _GMainContext
        return libgobject.g_main_context_get_thread_default()

    @staticmethod
    def ref_thread_default():
        libgobject.g_main_context_ref_thread_default.restype = _GMainContext
        return libgobject.g_main_context_ref_thread_default()

