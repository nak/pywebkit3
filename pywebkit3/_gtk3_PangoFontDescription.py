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
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int

import _gobject_GBoxed
class PangoFontDescription( _gobject_GBoxed.GBoxed):
    """Class PangoFontDescription Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.pango_font_description_new.restype = c_void_p

        libgtk3.pango_font_description_new.argtypes = []
        self._object = libgtk3.pango_font_description_new()

    """Methods"""
    def to_string(self, ):

        libgtk3.pango_font_description_to_string.restype = _char
        libgtk3.pango_font_description_to_string.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_to_string(self._object, )

    def copy(self, ):

        libgtk3.pango_font_description_copy.restype = _PangoFontDescription
        libgtk3.pango_font_description_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libgtk3.pango_font_description_copy(self._object, )  or c_void_p())

    def equal(self,  desc2,):
        if desc2 : desc2 = desc2._object
        else : desc2 = c_void_p()

        libgtk3.pango_font_description_equal.restype = gboolean
        libgtk3.pango_font_description_equal.argtypes = [c_void_p, _PangoFontDescription]
        
        return libgtk3.pango_font_description_equal(self._object,  desc2,)

    def set_family_static(self,  family,):

        libgtk3.pango_font_description_set_family_static.argtypes = [c_void_p, c_char_p]
        
        libgtk3.pango_font_description_set_family_static(self._object,  family,)

    def get_set_fields(self, ):

        libgtk3.pango_font_description_get_set_fields.restype = PangoFontMask
        libgtk3.pango_font_description_get_set_fields.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_set_fields(self._object, )

    def set_variant(self,  variant,):

        libgtk3.pango_font_description_set_variant.argtypes = [c_void_p, PangoVariant]
        
        libgtk3.pango_font_description_set_variant(self._object,  variant,)

    def set_size(self,  size,):

        libgtk3.pango_font_description_set_size.argtypes = [c_void_p, gint]
        
        libgtk3.pango_font_description_set_size(self._object,  size,)

    def get_size_is_absolute(self, ):

        libgtk3.pango_font_description_get_size_is_absolute.restype = gboolean
        libgtk3.pango_font_description_get_size_is_absolute.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_size_is_absolute(self._object, )

    def unset_fields(self,  to_unset,):

        libgtk3.pango_font_description_unset_fields.argtypes = [c_void_p, PangoFontMask]
        
        libgtk3.pango_font_description_unset_fields(self._object,  to_unset,)

    def set_weight(self,  weight,):

        libgtk3.pango_font_description_set_weight.argtypes = [c_void_p, PangoWeight]
        
        libgtk3.pango_font_description_set_weight(self._object,  weight,)

    def get_style(self, ):

        libgtk3.pango_font_description_get_style.restype = PangoStyle
        libgtk3.pango_font_description_get_style.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_style(self._object, )

    def get_weight(self, ):

        libgtk3.pango_font_description_get_weight.restype = PangoWeight
        libgtk3.pango_font_description_get_weight.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_weight(self._object, )

    def set_style(self,  style,):

        libgtk3.pango_font_description_set_style.argtypes = [c_void_p, PangoStyle]
        
        libgtk3.pango_font_description_set_style(self._object,  style,)

    def get_gravity(self, ):

        libgtk3.pango_font_description_get_gravity.restype = PangoGravity
        libgtk3.pango_font_description_get_gravity.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_gravity(self._object, )

    def get_size(self, ):

        libgtk3.pango_font_description_get_size.restype = gint
        libgtk3.pango_font_description_get_size.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_size(self._object, )

    def merge_static(self,  desc_to_merge, replace_existing,):
        if desc_to_merge : desc_to_merge = desc_to_merge._object
        else : desc_to_merge = c_void_p()

        libgtk3.pango_font_description_merge_static.argtypes = [c_void_p, _PangoFontDescription,gboolean]
        
        libgtk3.pango_font_description_merge_static(self._object,  desc_to_merge, replace_existing,)

    def better_match(self,  old_match, new_match,):
        if old_match : old_match = old_match._object
        else : old_match = c_void_p()
        if new_match : new_match = new_match._object
        else : new_match = c_void_p()

        libgtk3.pango_font_description_better_match.restype = gboolean
        libgtk3.pango_font_description_better_match.argtypes = [c_void_p, _PangoFontDescription,_PangoFontDescription]
        
        return libgtk3.pango_font_description_better_match(self._object,  old_match, new_match,)

    def set_stretch(self,  stretch,):

        libgtk3.pango_font_description_set_stretch.argtypes = [c_void_p, PangoStretch]
        
        libgtk3.pango_font_description_set_stretch(self._object,  stretch,)

    def hash(self, ):

        libgtk3.pango_font_description_hash.restype = guint
        libgtk3.pango_font_description_hash.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_hash(self._object, )

    def set_family(self,  family,):

        libgtk3.pango_font_description_set_family.argtypes = [c_void_p, c_char_p]
        
        libgtk3.pango_font_description_set_family(self._object,  family,)

    def get_stretch(self, ):

        libgtk3.pango_font_description_get_stretch.restype = PangoStretch
        libgtk3.pango_font_description_get_stretch.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_stretch(self._object, )

    def pango_font_descriptions_free(self,  n_descs,):

        libgtk3.pango_font_descriptions_free.argtypes = [c_void_p, int]
        
        libgtk3.pango_font_descriptions_free(self._object,  n_descs,)

    def get_family(self, ):

        libgtk3.pango_font_description_get_family.restype = _char
        libgtk3.pango_font_description_get_family.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_family(self._object, )

    def copy_static(self, ):

        libgtk3.pango_font_description_copy_static.restype = _PangoFontDescription
        libgtk3.pango_font_description_copy_static.argtypes = [c_void_p]
        from pywebkit3.gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libgtk3.pango_font_description_copy_static(self._object, )  or c_void_p())

    def set_absolute_size(self,  size,):

        libgtk3.pango_font_description_set_absolute_size.argtypes = [c_void_p, double]
        
        libgtk3.pango_font_description_set_absolute_size(self._object,  size,)

    def merge(self,  desc_to_merge, replace_existing,):
        if desc_to_merge : desc_to_merge = desc_to_merge._object
        else : desc_to_merge = c_void_p()

        libgtk3.pango_font_description_merge.argtypes = [c_void_p, _PangoFontDescription,gboolean]
        
        libgtk3.pango_font_description_merge(self._object,  desc_to_merge, replace_existing,)

    def to_filename(self, ):

        libgtk3.pango_font_description_to_filename.restype = _char
        libgtk3.pango_font_description_to_filename.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_to_filename(self._object, )

    def set_gravity(self,  gravity,):

        libgtk3.pango_font_description_set_gravity.argtypes = [c_void_p, PangoGravity]
        
        libgtk3.pango_font_description_set_gravity(self._object,  gravity,)

    def get_variant(self, ):

        libgtk3.pango_font_description_get_variant.restype = PangoVariant
        libgtk3.pango_font_description_get_variant.argtypes = [c_void_p]
        
        return libgtk3.pango_font_description_get_variant(self._object, )

    def free(self, ):

        libgtk3.pango_font_description_free.argtypes = [c_void_p]
        
        libgtk3.pango_font_description_free(self._object, )

    @staticmethod
    def from_string( str,):
        libgtk3.pango_font_description_from_string.restype = _PangoFontDescription
        libgtk3.pango_font_description_from_string.argtypes = [c_char_p]
        return libgtk3.pango_font_description_from_string(str, )

