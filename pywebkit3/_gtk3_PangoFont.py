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
class PangoFont( _gobject_GObject.GObject):
    """Class PangoFont Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_font_map(self, ):

        libgtk3.pango_font_get_font_map.restype = _PangoFontMap
        libgtk3.pango_font_get_font_map.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontMap
        return PangoFontMap( obj=libgtk3.pango_font_get_font_map(self._object, )  or c_void_p())

    def get_glyph_extents(self,  glyph, ink_rect, logical_rect,):
        if glyph : glyph = glyph._object
        else : glyph = c_void_p()
        if ink_rect : ink_rect = ink_rect._object
        else : ink_rect = c_void_p()
        if logical_rect : logical_rect = logical_rect._object
        else : logical_rect = c_void_p()

        libgtk3.pango_font_get_glyph_extents.argtypes = [c_void_p, PangoGlyph,_PangoRectangle,_PangoRectangle]
        
        libgtk3.pango_font_get_glyph_extents(self._object,  glyph, ink_rect, logical_rect,)

    def get_coverage(self,  language,):
        if language : language = language._object
        else : language = c_void_p()

        libgtk3.pango_font_get_coverage.restype = _PangoCoverage
        libgtk3.pango_font_get_coverage.argtypes = [c_void_p, _PangoLanguage]
        from pywebkit3.gtk3 import PangoCoverage
        return PangoCoverage(None, obj=libgtk3.pango_font_get_coverage(self._object,  language,)  or c_void_p())

    def describe(self, ):

        libgtk3.pango_font_describe.restype = _PangoFontDescription
        libgtk3.pango_font_describe.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libgtk3.pango_font_describe(self._object, )  or c_void_p())

    def get_metrics(self,  language,):
        if language : language = language._object
        else : language = c_void_p()

        libgtk3.pango_font_get_metrics.restype = _PangoFontMetrics
        libgtk3.pango_font_get_metrics.argtypes = [c_void_p, _PangoLanguage]
        from pywebkit3.gtk3 import PangoFontMetrics
        return PangoFontMetrics( obj=libgtk3.pango_font_get_metrics(self._object,  language,)  or c_void_p())

    def describe_with_absolute_size(self, ):

        libgtk3.pango_font_describe_with_absolute_size.restype = _PangoFontDescription
        libgtk3.pango_font_describe_with_absolute_size.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libgtk3.pango_font_describe_with_absolute_size(self._object, )  or c_void_p())

