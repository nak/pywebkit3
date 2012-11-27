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
class PangoFontMap( _gobject_GObject.GObject):
    """Class PangoFontMap Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def create_context(self, ):

        libgtk3.pango_font_map_create_context.restype = _PangoContext
        libgtk3.pango_font_map_create_context.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoContext
        return PangoContext( obj=libgtk3.pango_font_map_create_context(self._object, )  or c_void_p())

    def load_font(self,  context, desc,):
        if context : context = context._object
        else : context = c_void_p()
        if desc : desc = desc._object
        else : desc = c_void_p()

        libgtk3.pango_font_map_load_font.restype = _PangoFont
        libgtk3.pango_font_map_load_font.argtypes = [c_void_p, _PangoContext,_PangoFontDescription]
        from pywebkit3.gtk3 import PangoFont
        return PangoFont( obj=libgtk3.pango_font_map_load_font(self._object,  context, desc,)  or c_void_p())

    def list_families(self,  families, n_families,):
        if families : families = families._object
        else : families = c_void_p()
        if n_families : n_families = n_families._object
        else : n_families = c_void_p()

        libgtk3.pango_font_map_list_families.argtypes = [c_void_p, POITNER(_PangoFontFamily),POITNER(int)]
        
        libgtk3.pango_font_map_list_families(self._object,  families, n_families,)

    def get_shape_engine_type(self, ):

        libgtk3.pango_font_map_get_shape_engine_type.restype = _char
        libgtk3.pango_font_map_get_shape_engine_type.argtypes = [c_void_p]
        
        return libgtk3.pango_font_map_get_shape_engine_type(self._object, )

    def load_fontset(self,  context, desc, language,):
        if context : context = context._object
        else : context = c_void_p()
        if desc : desc = desc._object
        else : desc = c_void_p()
        if language : language = language._object
        else : language = c_void_p()

        libgtk3.pango_font_map_load_fontset.restype = _PangoFontset
        libgtk3.pango_font_map_load_fontset.argtypes = [c_void_p, _PangoContext,_PangoFontDescription,_PangoLanguage]
        from pywebkit3.gtk3 import PangoFontset
        return PangoFontset( obj=libgtk3.pango_font_map_load_fontset(self._object,  context, desc, language,)  or c_void_p())

