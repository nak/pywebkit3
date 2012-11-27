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
class PangoContext( _gobject_GObject.GObject):
    """Class PangoContext Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.pango_context_new.restype = c_void_p

        libgtk3.pango_context_new.argtypes = []
        self._object = libgtk3.pango_context_new()

    """Methods"""
    def pango_find_paragraph_boundary(self,  text, length, paragraph_delimiter_index, next_paragraph_start,):
        if paragraph_delimiter_index : paragraph_delimiter_index = paragraph_delimiter_index._object
        else : paragraph_delimiter_index = c_void_p()
        if next_paragraph_start : next_paragraph_start = next_paragraph_start._object
        else : next_paragraph_start = c_void_p()

        libgtk3.pango_find_paragraph_boundary.argtypes = [c_void_p, c_char_p,gint,POITNER(gint),POITNER(gint)]
        
        libgtk3.pango_find_paragraph_boundary(self._object,  text, length, paragraph_delimiter_index, next_paragraph_start,)

    def set_language(self,  language,):
        if language : language = language._object
        else : language = c_void_p()

        libgtk3.pango_context_set_language.argtypes = [c_void_p, _PangoLanguage]
        
        libgtk3.pango_context_set_language(self._object,  language,)

    def pango_itemize(self,  text, start_index, length, attrs, cached_iter,):
        if attrs : attrs = attrs._object
        else : attrs = c_void_p()
        if cached_iter : cached_iter = cached_iter._object
        else : cached_iter = c_void_p()

        libgtk3.pango_itemize.restype = _GList
        libgtk3.pango_itemize.argtypes = [c_void_p, c_char_p,int,int,_PangoAttrList,_PangoAttrIterator]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.pango_itemize(self._object,  text, start_index, length, attrs, cached_iter,) or c_void_p())

    def pango_shape_full(self,  item_text, item_length, paragraph_text, paragraph_length, analysis, glyphs,):
        if analysis : analysis = analysis._object
        else : analysis = c_void_p()
        if glyphs : glyphs = glyphs._object
        else : glyphs = c_void_p()

        libgtk3.pango_shape_full.argtypes = [c_void_p, c_char_p,gint,c_char_p,gint,_PangoAnalysis,_PangoGlyphString]
        
        libgtk3.pango_shape_full(self._object,  item_text, item_length, paragraph_text, paragraph_length, analysis, glyphs,)

    def set_base_dir(self,  direction,):

        libgtk3.pango_context_set_base_dir.argtypes = [c_void_p, PangoDirection]
        
        libgtk3.pango_context_set_base_dir(self._object,  direction,)

    def pango_get_log_attrs(self,  text, length, level, language, log_attrs, attrs_len,):
        if language : language = language._object
        else : language = c_void_p()
        if log_attrs : log_attrs = log_attrs._object
        else : log_attrs = c_void_p()

        libgtk3.pango_get_log_attrs.argtypes = [c_void_p, c_char_p,int,int,_PangoLanguage,_PangoLogAttr,int]
        
        libgtk3.pango_get_log_attrs(self._object,  text, length, level, language, log_attrs, attrs_len,)

    def set_matrix(self,  matrix,):
        if matrix : matrix = matrix._object
        else : matrix = c_void_p()

        libgtk3.pango_context_set_matrix.argtypes = [c_void_p, _PangoMatrix]
        
        libgtk3.pango_context_set_matrix(self._object,  matrix,)

    def get_matrix(self, ):

        libgtk3.pango_context_get_matrix.restype = _PangoMatrix
        libgtk3.pango_context_get_matrix.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoMatrix
        return PangoMatrix( obj=libgtk3.pango_context_get_matrix(self._object, )  or c_void_p())

    def set_font_description(self,  desc,):
        if desc : desc = desc._object
        else : desc = c_void_p()

        libgtk3.pango_context_set_font_description.argtypes = [c_void_p, _PangoFontDescription]
        
        libgtk3.pango_context_set_font_description(self._object,  desc,)

    def get_base_gravity(self, ):

        libgtk3.pango_context_get_base_gravity.restype = PangoGravity
        libgtk3.pango_context_get_base_gravity.argtypes = [c_void_p]
        
        return libgtk3.pango_context_get_base_gravity(self._object, )

    def load_fontset(self,  desc, language,):
        if desc : desc = desc._object
        else : desc = c_void_p()
        if language : language = language._object
        else : language = c_void_p()

        libgtk3.pango_context_load_fontset.restype = _PangoFontset
        libgtk3.pango_context_load_fontset.argtypes = [c_void_p, _PangoFontDescription,_PangoLanguage]
        from pywebkit3.gtk3 import PangoFontset
        return PangoFontset( obj=libgtk3.pango_context_load_fontset(self._object,  desc, language,)  or c_void_p())

    def pango_default_break(self,  text, length, analysis, attrs, attrs_len,):
        if analysis : analysis = analysis._object
        else : analysis = c_void_p()
        if attrs : attrs = attrs._object
        else : attrs = c_void_p()

        libgtk3.pango_default_break.argtypes = [c_void_p, c_char_p,int,_PangoAnalysis,_PangoLogAttr,int]
        
        libgtk3.pango_default_break(self._object,  text, length, analysis, attrs, attrs_len,)

    def set_base_gravity(self,  gravity,):

        libgtk3.pango_context_set_base_gravity.argtypes = [c_void_p, PangoGravity]
        
        libgtk3.pango_context_set_base_gravity(self._object,  gravity,)

    def pango_itemize_with_base_dir(self,  base_dir, text, start_index, length, attrs, cached_iter,):
        if attrs : attrs = attrs._object
        else : attrs = c_void_p()
        if cached_iter : cached_iter = cached_iter._object
        else : cached_iter = c_void_p()

        libgtk3.pango_itemize_with_base_dir.restype = _GList
        libgtk3.pango_itemize_with_base_dir.argtypes = [c_void_p, PangoDirection,c_char_p,int,int,_PangoAttrList,_PangoAttrIterator]
        from pywebkit3.gobject import GList
        return GList( obj=libgtk3.pango_itemize_with_base_dir(self._object,  base_dir, text, start_index, length, attrs, cached_iter,) or c_void_p())

    def list_families(self,  families, n_families,):
        if families : families = families._object
        else : families = c_void_p()
        if n_families : n_families = n_families._object
        else : n_families = c_void_p()

        libgtk3.pango_context_list_families.argtypes = [c_void_p, POITNER(_PangoFontFamily),POITNER(int)]
        
        libgtk3.pango_context_list_families(self._object,  families, n_families,)

    def set_font_map(self,  font_map,):
        if font_map : font_map = font_map._object
        else : font_map = c_void_p()

        libgtk3.pango_context_set_font_map.argtypes = [c_void_p, _PangoFontMap]
        
        libgtk3.pango_context_set_font_map(self._object,  font_map,)

    def get_language(self, ):

        libgtk3.pango_context_get_language.restype = _PangoLanguage
        libgtk3.pango_context_get_language.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoLanguage
        return PangoLanguage( obj=libgtk3.pango_context_get_language(self._object, )  or c_void_p())

    def get_font_map(self, ):

        libgtk3.pango_context_get_font_map.restype = _PangoFontMap
        libgtk3.pango_context_get_font_map.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontMap
        return PangoFontMap( obj=libgtk3.pango_context_get_font_map(self._object, )  or c_void_p())

    def pango_shape(self,  text, length, analysis, glyphs,):
        if analysis : analysis = analysis._object
        else : analysis = c_void_p()
        if glyphs : glyphs = glyphs._object
        else : glyphs = c_void_p()

        libgtk3.pango_shape.argtypes = [c_void_p, c_char_p,gint,_PangoAnalysis,_PangoGlyphString]
        
        libgtk3.pango_shape(self._object,  text, length, analysis, glyphs,)

    def get_base_dir(self, ):

        libgtk3.pango_context_get_base_dir.restype = PangoDirection
        libgtk3.pango_context_get_base_dir.argtypes = [c_void_p]
        
        return libgtk3.pango_context_get_base_dir(self._object, )

    def set_gravity_hint(self,  hint,):

        libgtk3.pango_context_set_gravity_hint.argtypes = [c_void_p, PangoGravityHint]
        
        libgtk3.pango_context_set_gravity_hint(self._object,  hint,)

    def get_gravity(self, ):

        libgtk3.pango_context_get_gravity.restype = PangoGravity
        libgtk3.pango_context_get_gravity.argtypes = [c_void_p]
        
        return libgtk3.pango_context_get_gravity(self._object, )

    def get_font_description(self, ):

        libgtk3.pango_context_get_font_description.restype = _PangoFontDescription
        libgtk3.pango_context_get_font_description.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libgtk3.pango_context_get_font_description(self._object, )  or c_void_p())

    def get_metrics(self,  desc, language,):
        if desc : desc = desc._object
        else : desc = c_void_p()
        if language : language = language._object
        else : language = c_void_p()

        libgtk3.pango_context_get_metrics.restype = _PangoFontMetrics
        libgtk3.pango_context_get_metrics.argtypes = [c_void_p, _PangoFontDescription,_PangoLanguage]
        from pywebkit3.gtk3 import PangoFontMetrics
        return PangoFontMetrics( obj=libgtk3.pango_context_get_metrics(self._object,  desc, language,)  or c_void_p())

    def get_gravity_hint(self, ):

        libgtk3.pango_context_get_gravity_hint.restype = PangoGravityHint
        libgtk3.pango_context_get_gravity_hint.argtypes = [c_void_p]
        
        return libgtk3.pango_context_get_gravity_hint(self._object, )

    def pango_break(self,  text, length, analysis, attrs, attrs_len,):
        if analysis : analysis = analysis._object
        else : analysis = c_void_p()
        if attrs : attrs = attrs._object
        else : attrs = c_void_p()

        libgtk3.pango_break.argtypes = [c_void_p, c_char_p,int,_PangoAnalysis,_PangoLogAttr,int]
        
        libgtk3.pango_break(self._object,  text, length, analysis, attrs, attrs_len,)

    def load_font(self,  desc,):
        if desc : desc = desc._object
        else : desc = c_void_p()

        libgtk3.pango_context_load_font.restype = _PangoFont
        libgtk3.pango_context_load_font.argtypes = [c_void_p, _PangoFontDescription]
        from pywebkit3.gtk3 import PangoFont
        return PangoFont( obj=libgtk3.pango_context_load_font(self._object,  desc,)  or c_void_p())

    @staticmethod
    def pango_reorder_items( logical_items,):
        if logical_items : logical_items = logical_items._object
        else : logical_items = c_void_p()
        libgtk3.pango_reorder_items.restype = _GList
        libgtk3.pango_reorder_items.argtypes = [_GList]
        return libgtk3.pango_reorder_items(logical_items, )

