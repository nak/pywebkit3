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
from .gtk3_types import *
from .javascriptcore_types import *
from .javascriptcore_enums import *

import weakref

"""Derived Pointer Types"""
_JSString = POINTER(c_void_p)

try:
    libjavascriptcore.JSStringGetCharactersPtr.restype = POINTER(JSChar)
    libjavascriptcore.JSStringGetCharactersPtr.argtypes = [_JSString]
except:
    pass
try:
    libjavascriptcore.JSStringIsEqual.restype = bool
    libjavascriptcore.JSStringIsEqual.argtypes = [_JSString, _JSString]
except:
    pass
try:
    libjavascriptcore.JSStringRetain.restype = _JSString
    libjavascriptcore.JSStringRetain.argtypes = [_JSString]
except:
    pass
try:
    libjavascriptcore.JSStringIsEqualToUTF8CString.restype = bool
    libjavascriptcore.JSStringIsEqualToUTF8CString.argtypes = [_JSString, Asciifier]
except:
    pass
try:
    libjavascriptcore.JSStringGetUTF8CString.restype = size_t
    libjavascriptcore.JSStringGetUTF8CString.argtypes = [_JSString, Asciifier, size_t]
except:
    pass
try:
    libjavascriptcore.JSStringGetMaximumUTF8CStringSize.restype = size_t
    libjavascriptcore.JSStringGetMaximumUTF8CStringSize.argtypes = [_JSString]
except:
    pass
try:
    libjavascriptcore.JSStringGetLength.restype = size_t
    libjavascriptcore.JSStringGetLength.argtypes = [_JSString]
except:
    pass
try:
    libjavascriptcore.JSStringCreateWithCharacters.restype = _JSString
    libjavascriptcore.JSStringCreateWithCharacters.argtypes = [POINTER(JSChar), size_t]
except:
    pass
try:
    libjavascriptcore.JSStringCreateWithUTF8CString.restype = _JSString
    libjavascriptcore.JSStringCreateWithUTF8CString.argtypes = [Asciifier]
except:
    pass
try:
    libjavascriptcore.JSStringRelease.restype = None
    libjavascriptcore.JSStringRelease.argtypes = [_JSString]
except:
    pass


# noinspection PyPep8Naming,PyProtectedMember
class JSString(object):
    """Class JSString Constructors"""

    def __init__(self, obj=None):
        self._object = weakref.ref(obj)
        self._strong_ref = obj

    """Methods"""

    def GetCharactersPtr(self, ):
        return libjavascriptcore.JSStringGetCharactersPtr(self._object())

    def IsEqual(self, b, ):
        if b:
            b = b._object()
        else:
            b = POINTER(c_void_p)()
        return libjavascriptcore.JSStringIsEqual(self._object(), b)

    def Retain(self, ):
        libjavascriptcore.JSStringRetain(self._object())
        return self

    def IsEqualToUTF8CString(self, b, ):
        return libjavascriptcore.JSStringIsEqualToUTF8CString(self._object(),
                                                              str(b).encode('ascii') if b is not None else None)

    def GetUTF8CString(self, buffer_, bufferSize, ):
        if buffer_ is None:
            return None
        libjavascriptcore.JSStringGetUTF8CString(self._object(), buffer_, bufferSize)

    def GetMaximumUTF8CStringSize(self, ):
        return libjavascriptcore.JSStringGetMaximumUTF8CStringSize(self._object())

    def GetLength(self, ):
        return libjavascriptcore.JSStringGetLength(self._object())

    @staticmethod
    def CreateWithCharacters(chars, numChars, ):
        return JSString(obj=libjavascriptcore.JSStringCreateWithCharacters(str(chars).encode('ascii'),
                                                                           numChars, ) or POINTER(c_void_p)())

    @staticmethod
    def CreateWithUTF8CString(string, ):
        string += '\0'
        string2 = libjavascriptcore.JSStringCreateWithUTF8CString(
            str(string).encode('ascii') if string is not None else None)
        return JSString(obj=string2 or POINTER(c_void_p)())

    def Release(self):
        libjavascriptcore.JSStringRelease(self._object())
        self._object = weakref.ref(POINTER(c_int)())
        self._strong_ref = None

    def __del__(self):
        if self._object and cast(self._object(), c_void_p).value is not None:
            self.Release()
        self._object = weakref.ref(POINTER(c_int)())
        self._strong_ref = None
