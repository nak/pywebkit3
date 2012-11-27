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
_PangoCoverage = c_void_p
__PangoAnalysis = c_void_p
_PangoFontDescription = c_void_p
_GList = c_void_p
_PangoLayoutRun = c_void_p
_PangoFont = c_void_p
_PangoLayoutLine = c_void_p
__PangoTabArray = c_void_p
__PangoCoverage = c_void_p
__PangoLayout = c_void_p
__PangoMatrix = c_void_p
_PangoLanguage = c_void_p
_PangoTabArray = c_void_p
_PangoFontMetrics = c_void_p
"""Enumerations"""
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int

import _gobject_GObject
class PangoCoverage( _gobject_GObject.GObject):
    """Class PangoCoverage Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.pango_coverage_new.restype = c_void_p

        libgtk3.pango_coverage_new.argtypes = []
        self._object = libgtk3.pango_coverage_new()

    """Methods"""
    def unref(self, ):

        libgtk3.pango_coverage_unref.argtypes = [c_void_p]
        
        libgtk3.pango_coverage_unref(self._object, )

    def copy(self, ):

        libgtk3.pango_coverage_copy.restype = _PangoCoverage
        libgtk3.pango_coverage_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoCoverage
        return PangoCoverage(None, obj=libgtk3.pango_coverage_copy(self._object, )  or c_void_p())

    def set(self,  index_, level,):

        libgtk3.pango_coverage_set.argtypes = [c_void_p, int,PangoCoverageLevel]
        
        libgtk3.pango_coverage_set(self._object,  index_, level,)

    def ref(self, ):

        libgtk3.pango_coverage_ref.restype = _PangoCoverage
        libgtk3.pango_coverage_ref.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoCoverage
        return PangoCoverage(None, obj=libgtk3.pango_coverage_ref(self._object, )  or c_void_p())

    def get(self,  index_,):

        libgtk3.pango_coverage_get.restype = PangoCoverageLevel
        libgtk3.pango_coverage_get.argtypes = [c_void_p, int]
        
        return libgtk3.pango_coverage_get(self._object,  index_,)

    def max(self,  other,):
        if other : other = other._object
        else : other = c_void_p()

        libgtk3.pango_coverage_max.argtypes = [c_void_p, _PangoCoverage]
        
        libgtk3.pango_coverage_max(self._object,  other,)

    def to_bytes(self,  bytes, n_bytes,):
        if bytes : bytes = bytes._object
        else : bytes = c_void_p()
        if n_bytes : n_bytes = n_bytes._object
        else : n_bytes = c_void_p()

        libgtk3.pango_coverage_to_bytes.argtypes = [c_void_p, POITNER(guchar),POITNER(int)]
        
        libgtk3.pango_coverage_to_bytes(self._object,  bytes, n_bytes,)

    @staticmethod
    def from_bytes( bytes, n_bytes,):
        if bytes : bytes = bytes._object
        else : bytes = c_void_p()
        libgtk3.pango_coverage_from_bytes.restype = _PangoCoverage
        libgtk3.pango_coverage_from_bytes.argtypes = [POITNER(guchar),int]
        return libgtk3.pango_coverage_from_bytes(bytes, n_bytes, )

