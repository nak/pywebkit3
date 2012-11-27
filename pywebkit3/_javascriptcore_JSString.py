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
__JSString = c_void_p
_JSChar = c_void_p
_JSString = c_void_p
"""Enumerations"""

import _javascriptcore_JSObject
class JSString( _javascriptcore_JSObject.JSObject):
    """Class JSString Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def JSStringGetCharactersPtr(self, ):

        libjavascriptcore.JSStringGetCharactersPtr.restype = _JSChar
        libjavascriptcore.JSStringGetCharactersPtr.argtypes = [c_void_p]
        
        return libjavascriptcore.JSStringGetCharactersPtr(self._object, )

    def JSStringIsEqual(self,  b,):
        if b : b = b._object
        else : b = c_void_p()

        libjavascriptcore.JSStringIsEqual.restype = bool
        libjavascriptcore.JSStringIsEqual.argtypes = [c_void_p, _JSString]
        
        return libjavascriptcore.JSStringIsEqual(self._object,  b,)

    def JSStringRetain(self, ):

        libjavascriptcore.JSStringRetain.restype = _JSString
        libjavascriptcore.JSStringRetain.argtypes = [c_void_p]
        from pywebkit3.javascriptcore import JSString
        return JSString(None, obj=libjavascriptcore.JSStringRetain(self._object, )  or c_void_p())

    def JSStringIsEqualToUTF8CString(self,  b,):

        libjavascriptcore.JSStringIsEqualToUTF8CString.restype = bool
        libjavascriptcore.JSStringIsEqualToUTF8CString.argtypes = [c_void_p, c_char_p]
        
        return libjavascriptcore.JSStringIsEqualToUTF8CString(self._object,  b,)

    def JSStringGetUTF8CString(self,  buffer, bufferSize,):

        libjavascriptcore.JSStringGetUTF8CString.restype = size_t
        libjavascriptcore.JSStringGetUTF8CString.argtypes = [c_void_p, c_char_p,size_t]
        
        return libjavascriptcore.JSStringGetUTF8CString(self._object,  buffer, bufferSize,)

    def JSStringGetMaximumUTF8CStringSize(self, ):

        libjavascriptcore.JSStringGetMaximumUTF8CStringSize.restype = size_t
        libjavascriptcore.JSStringGetMaximumUTF8CStringSize.argtypes = [c_void_p]
        
        return libjavascriptcore.JSStringGetMaximumUTF8CStringSize(self._object, )

    def JSStringGetLength(self, ):

        libjavascriptcore.JSStringGetLength.restype = size_t
        libjavascriptcore.JSStringGetLength.argtypes = [c_void_p]
        
        return libjavascriptcore.JSStringGetLength(self._object, )

    @staticmethod
    def JSStringCreateWithCharacters( chars, numChars,):
        if chars : chars = chars._object
        else : chars = c_void_p()
        libjavascriptcore.JSStringCreateWithCharacters.restype = _JSString
        libjavascriptcore.JSStringCreateWithCharacters.argtypes = [POITNER(JSChar),size_t]
        return libjavascriptcore.JSStringCreateWithCharacters(chars, numChars, )

    @staticmethod
    def JSStringCreateWithUTF8CString( string,):
        libjavascriptcore.JSStringCreateWithUTF8CString.restype = _JSString
        libjavascriptcore.JSStringCreateWithUTF8CString.argtypes = [c_char_p]
        return libjavascriptcore.JSStringCreateWithUTF8CString(string, )

