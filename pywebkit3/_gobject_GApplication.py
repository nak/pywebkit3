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
_gchar = c_void_p
__GCancellable = c_void_p
__GActionGroup = c_void_p
_GApplication = c_void_p
__GFile = c_void_p
__GError = c_void_p
"""Enumerations"""
GApplicationFlags = c_int

import _gobject_GObject
class GApplication( _gobject_GObject.GObject):
    """Class GApplication Constructors"""
    def __init__( self, flags,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_application_new.restype = c_void_p

        libgobject.g_application_new.argtypes = [GApplicationFlags]
        self._object = libgobject.g_application_new(flags, )

    """Methods"""
    def activate(self, ):

        libgobject.g_application_activate.argtypes = [c_void_p]
        
        libgobject.g_application_activate(self._object, )

    def hold(self, ):

        libgobject.g_application_hold.argtypes = [c_void_p]
        
        libgobject.g_application_hold(self._object, )

    def get_application_id(self, ):

        libgobject.g_application_get_application_id.restype = _gchar
        libgobject.g_application_get_application_id.argtypes = [c_void_p]
        
        return libgobject.g_application_get_application_id(self._object, )

    def set_default(self, ):

        libgobject.g_application_set_default.argtypes = [c_void_p]
        
        libgobject.g_application_set_default(self._object, )

    def get_flags(self, ):

        libgobject.g_application_get_flags.restype = GApplicationFlags
        libgobject.g_application_get_flags.argtypes = [c_void_p]
        
        return libgobject.g_application_get_flags(self._object, )

    def register(self,  cancellable, error,):
        if cancellable : cancellable = cancellable._object
        else : cancellable = c_void_p()
        if error : error = error._object
        else : error = c_void_p()

        libgobject.g_application_register.restype = gboolean
        libgobject.g_application_register.argtypes = [c_void_p, _GCancellable,_GError]
        
        return libgobject.g_application_register(self._object,  cancellable, error,)

    def set_application_id(self,  application_id,):

        libgobject.g_application_set_application_id.argtypes = [c_void_p, c_char_p]
        
        libgobject.g_application_set_application_id(self._object,  application_id,)

    def release(self, ):

        libgobject.g_application_release.argtypes = [c_void_p]
        
        libgobject.g_application_release(self._object, )

    def set_action_group(self,  action_group,):
        if action_group : action_group = action_group._object
        else : action_group = c_void_p()

        libgobject.g_application_set_action_group.argtypes = [c_void_p, _GActionGroup]
        
        libgobject.g_application_set_action_group(self._object,  action_group,)

    def get_is_remote(self, ):

        libgobject.g_application_get_is_remote.restype = gboolean
        libgobject.g_application_get_is_remote.argtypes = [c_void_p]
        
        return libgobject.g_application_get_is_remote(self._object, )

    def set_inactivity_timeout(self,  inactivity_timeout,):

        libgobject.g_application_set_inactivity_timeout.argtypes = [c_void_p, guint]
        
        libgobject.g_application_set_inactivity_timeout(self._object,  inactivity_timeout,)

    def get_is_registered(self, ):

        libgobject.g_application_get_is_registered.restype = gboolean
        libgobject.g_application_get_is_registered.argtypes = [c_void_p]
        
        return libgobject.g_application_get_is_registered(self._object, )

    def quit(self, ):

        libgobject.g_application_quit.argtypes = [c_void_p]
        
        libgobject.g_application_quit(self._object, )

    def get_inactivity_timeout(self, ):

        libgobject.g_application_get_inactivity_timeout.restype = guint
        libgobject.g_application_get_inactivity_timeout.argtypes = [c_void_p]
        
        return libgobject.g_application_get_inactivity_timeout(self._object, )

    def run(self,  argc, argv,):

        libgobject.g_application_run.restype = int
        libgobject.g_application_run.argtypes = [c_void_p, int,c_char_p]
        
        return libgobject.g_application_run(self._object,  argc, argv,)

    def open(self,  files, n_files, hint,):
        if files : files = files._object
        else : files = c_void_p()

        libgobject.g_application_open.argtypes = [c_void_p, _GFile,gint,c_char_p]
        
        libgobject.g_application_open(self._object,  files, n_files, hint,)

    def set_flags(self,  flags,):

        libgobject.g_application_set_flags.argtypes = [c_void_p, GApplicationFlags]
        
        libgobject.g_application_set_flags(self._object,  flags,)

    @staticmethod
    def get_default():
        libgobject.g_application_get_default.restype = _GApplication
        return libgobject.g_application_get_default()

    @staticmethod
    def id_is_valid( application_id,):
        libgobject.g_application_id_is_valid.restype = gboolean
        libgobject.g_application_id_is_valid.argtypes = [c_char_p]
        return libgobject.g_application_id_is_valid(application_id, )

