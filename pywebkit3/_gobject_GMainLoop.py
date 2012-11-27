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
_GMainLoop = c_void_p
_GMainContext = c_void_p
__GMainContext = c_void_p
"""Enumerations"""

import _gobject_GObject
class GMainLoop( _gobject_GObject.GObject):
    """Class GMainLoop Constructors"""
    def __init__( self, is_running,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_main_loop_new.restype = c_void_p

        libgobject.g_main_loop_new.argtypes = [gboolean]
        self._object = libgobject.g_main_loop_new(is_running, )

    """Methods"""
    def is_running(self, ):

        libgobject.g_main_loop_is_running.restype = gboolean
        libgobject.g_main_loop_is_running.argtypes = [c_void_p]
        
        return libgobject.g_main_loop_is_running(self._object, )

    def get_context(self, ):

        libgobject.g_main_loop_get_context.restype = _GMainContext
        libgobject.g_main_loop_get_context.argtypes = [c_void_p]
        from pywebkit3.gobject import GMainContext
        return GMainContext(None,None, obj=libgobject.g_main_loop_get_context(self._object, ) or c_void_p())

    def quit(self, ):

        libgobject.g_main_loop_quit.argtypes = [c_void_p]
        
        libgobject.g_main_loop_quit(self._object, )

    def ref(self, ):

        libgobject.g_main_loop_ref.restype = _GMainLoop
        libgobject.g_main_loop_ref.argtypes = [c_void_p]
        from pywebkit3.gobject import GMainLoop
        return GMainLoop(None, obj=libgobject.g_main_loop_ref(self._object, ) or c_void_p())

    def unref(self, ):

        libgobject.g_main_loop_unref.argtypes = [c_void_p]
        
        libgobject.g_main_loop_unref(self._object, )

    def run(self, ):

        libgobject.g_main_loop_run.argtypes = [c_void_p]
        
        libgobject.g_main_loop_run(self._object, )

cfuncs = []

from .gobject import GMainContextd
def idle_add( func , *args):
    cfunc = c_void_p()
    def C_Callable( param ):
        func( *args )
        cfuncs.remove(cfunc)
        return 0
    cfunc = GSourceFunc(C_Callable)
    cfuncs.append(cfunc)
    GMainContext.g_idle_add(cfunc, cfunc )
    
