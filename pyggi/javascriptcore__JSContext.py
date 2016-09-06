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
from .javascriptcore_types import *
from . import javascriptcore__JSObject
from ctypes import c_void_p, POINTER

OPAQUE_PTR = POINTER(c_void_p)
NULL = c_void_p()

"""Derived Pointer Types"""
_JSValue = OPAQUE_PTR
_JSContext = OPAQUE_PTR
_JSClass = OPAQUE_PTR
_JSContextGroup = OPAQUE_PTR
_JSPropertyNameAccumulator = OPAQUE_PTR
_JSGlobalContext = OPAQUE_PTR
_JSObject = OPAQUE_PTR

try:
    libjavascriptcore.JSGlobalContextRelease.restype = None
    libjavascriptcore.JSGlobalContextRelease.argtypes = [_JSContext, _JSGlobalContext]
except:
    pass
try:
    libjavascriptcore.JSContextGroupRelease.restype = None
    libjavascriptcore.JSContextGroupRelease.argtypes = [_JSContext, _JSContextGroup]
except:
    pass
try:
    libjavascriptcore.JSContextGetGroup.restype = _JSContextGroup
    libjavascriptcore.JSContextGetGroup.argtypes = [_JSContext]
except:
    pass
try:
    libjavascriptcore.JSContextGetGlobalObject.restype = _JSObject
    libjavascriptcore.JSContextGetGlobalObject.argtypes = [_JSContext]
except:
    pass
try:
    libjavascriptcore.JSGlobalContextCreate.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextCreate.argtypes = [_JSClass]
except:
    pass
try:
    libjavascriptcore.JSGlobalContextCreateInGroup.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextCreateInGroup.argtypes = [_JSContextGroup, _JSClass]
except:
    pass
try:
    libjavascriptcore.JSContextGroupRetain.restype = _JSContextGroup
    libjavascriptcore.JSContextGroupRetain.argtypes = [_JSContextGroup]
except:
    pass
try:
    libjavascriptcore.JSGlobalContextRetain.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextRetain.argtypes = [_JSGlobalContext]
except:
    pass


class JSContext(javascriptcore__JSObject.JSObject):
    """Class JSContext Constructors"""

    """Methods"""

    def JSGlobalContextRelease(self, ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()

        libjavascriptcore.JSGlobalContextRelease(self._object(), ctx)

    def GroupRelease(self, group, ):
        if group:
            group = group._object()
        else:
            group = OPAQUE_PTR()

        libjavascriptcore.JSContextGroupRelease(self._object(), group)

    def GetGroup(self, ):

        from .javascriptcore import JSContextGroup
        return JSContextGroup(obj=libjavascriptcore.JSContextGetGroup(self._object()) or OPAQUE_PTR())

    def GetGlobalObject(self, ):
        from .javascriptcore import JSObject
        return JSObject(obj=libjavascriptcore.JSContextGetGlobalObject(self._object()) or OPAQUE_PTR(),
                        context=None)

    @staticmethod
    def JSGlobalContextCreate(globalObjectClass, ):
        if globalObjectClass:
            globalObjectClass = globalObjectClass._object()
        else:
            globalObjectClass = OPAQUE_PTR()
        from .javascriptcore import JSGlobalContext
        return JSGlobalContext(obj=libjavascriptcore.JSGlobalContextCreate(globalObjectClass)or OPAQUE_PTR())

    @staticmethod
    def JSGlobalContextCreateInGroup(group, globalObjectClass, ):
        if group:
            group = group._object()
        else:
            group = OPAQUE_PTR()
        if globalObjectClass:
            globalObjectClass = globalObjectClass._object()
        else:
            globalObjectClass = OPAQUE_PTR()
        from .javascriptcore import JSGlobalContext
        return JSGlobalContext(obj=libjavascriptcore.JSGlobalContextCreateInGroup(group,
                                                                                  globalObjectClass) or OPAQUE_PTR())

    @staticmethod
    def GroupRetain(group):
        if group:
            group = group._object()
        else:
            group = OPAQUE_PTR()
        from .javascriptcore import JSContextGroup
        return JSContextGroup(obj=libjavascriptcore.JSContextGroupRetain(group) or OPAQUE_PTR())

    @staticmethod
    def JSGlobalContextRetain(ctx, ):
        if ctx:
            ctx = ctx._object()
        else:
            ctx = OPAQUE_PTR()
        from .javascriptcore import JSGlobalContext
        return JSGlobalContext(obj=libjavascriptcore.JSGlobalContextRetain(ctx) or OPAQUE_PTR())

    def __init__(self, obj=None):
        javascriptcore__JSObject.JSObject.__init__(self, obj, None)
        self._global = None

    def GetGlobalObject(self, ):
        if not self._global:
            from .javascriptcore import JSObject
            self._global = JSObject(obj=libjavascriptcore.JSContextGetGlobalObject(self._object()), context=self)
        return self._global

    def get_jsobject(self, name, can_call=False):
        from .javascript import JSString
        names = name.split('.')
        globj = JSContext.GetGlobalObject(self)
        obj = None
        for n in names:
            text = JSString.CreateWithUTF8CString(n)
            obj = globj.GetProperty(text, NULL)
            text.Release()
            if not obj:
                break
        if obj:
            from javascript import get_jsobj
            return_value = get_jsobj(obj.ToObject(self, NULL), self, name=name)
        else:
            raise Exception("Unknown javascript object by name %s" % name)
        return return_value
