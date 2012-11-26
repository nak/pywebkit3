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
from javascriptcore_types import *


"""Derived Pointer Types"""
_JSObject = c_void_p
_JSGlobalContext = c_void_p
_JSContext = c_void_p
_JSClass = c_void_p
_JSContextGroup = c_void_p
"""Enumerations"""

import _javascriptcore_JSObject
class JSContextGroup( _javascriptcore_JSObject.JSObject):
    """Class JSContextGroup Constructors"""

    """Methods"""
    def JSGlobalContextCreateInGroup(self,  globalObjectClass,):
        if globalObjectClass : globalObjectClass = globalObjectClass._object
        else : globalObjectClass = c_void_p()

        libjavascriptcore.JSGlobalContextCreateInGroup.restype = _JSGlobalContext
        libjavascriptcore.JSGlobalContextCreateInGroup.argtypes = [c_void_p, _JSClass]
        return libjavascriptcore.JSGlobalContextCreateInGroup(self._object, globalObjectClass, )

    def JSGlobalContextRelease(self,  ctx,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()

        libjavascriptcore.JSGlobalContextRelease.argtypes = [c_void_p, _JSGlobalContext]
        libjavascriptcore.JSGlobalContextRelease(self._object, ctx, )

    def JSContextGroupRelease(self, ):

        libjavascriptcore.JSContextGroupRelease(self._object, )

    def JSContextGroupRetain(self, ):

        libjavascriptcore.JSContextGroupRetain.restype = _JSContextGroup
        return libjavascriptcore.JSContextGroupRetain(self._object, )

    @staticmethod
    def JSGlobalContextCreate( globalObjectClass,):
        if globalObjectClass : globalObjectClass = globalObjectClass._object
        else : globalObjectClass = c_void_p()
        libjavascriptcore.JSGlobalContextCreate.restype = _JSGlobalContext
        libjavascriptcore.JSGlobalContextCreate.argtypes = [_JSClass]
        return libjavascriptcore.JSGlobalContextCreate(globalObjectClass, )

    @staticmethod
    def JSContextGetGroup( ctx,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        libjavascriptcore.JSContextGetGroup.restype = _JSContextGroup
        libjavascriptcore.JSContextGetGroup.argtypes = [_JSContext]
        return libjavascriptcore.JSContextGetGroup(ctx, )

    @staticmethod
    def JSContextGetGlobalObject( ctx,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        libjavascriptcore.JSContextGetGlobalObject.restype = _JSObject
        libjavascriptcore.JSContextGetGlobalObject.argtypes = [_JSContext]
        return libjavascriptcore.JSContextGetGlobalObject(ctx, )

    @staticmethod
    def JSGlobalContextRetain( ctx,):
        if ctx : ctx = ctx._object
        else : ctx = c_void_p()
        libjavascriptcore.JSGlobalContextRetain.restype = _JSGlobalContext
        libjavascriptcore.JSGlobalContextRetain.argtypes = [_JSGlobalContext]
        return libjavascriptcore.JSGlobalContextRetain(ctx, )

