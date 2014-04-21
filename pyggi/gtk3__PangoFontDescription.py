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
from .gtk3_types import *
from .gtk3_enums import *
from .gtk3_types import *
from .gtk3_enums import *

    
"""Derived Pointer Types"""
_GdkGeometry = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GdkTimeCoord = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_cairo_pattern_t = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GtkNumerableIcon = POINTER(c_void_p)
_GdkAppLaunchContext = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GdkPixbufSimpleAnim = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
"""Enumerations"""
GdkWindowType = c_int
GdkWindowWindowClass = c_int
GdkWindowHints = c_int
GdkGravity = c_int
GdkWindowEdgeh = c_int
GdkWindowTypeHint = c_int
GdkWindowAttributesType = c_int
GdkFilterReturn = c_int
GdkModifierType = c_int
GdkWMDecoration = c_int
GdkWMFunction = c_int
GdkCursorType = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GtkIconSize = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int

try:
    libgtk3.pango_font_description_to_string.restype = c_char_p
    libgtk3.pango_font_description_to_string.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_copy.restype = _PangoFontDescription
    libgtk3.pango_font_description_copy.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_equal.restype = gboolean
    libgtk3.pango_font_description_equal.argtypes = [_PangoFontDescription,_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_set_family_static.restype = None
    libgtk3.pango_font_description_set_family_static.argtypes = [_PangoFontDescription,Asciifier]
except:
   pass
try:
    libgtk3.pango_font_description_get_set_fields.restype = PangoFontMask
    libgtk3.pango_font_description_get_set_fields.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_set_variant.restype = None
    libgtk3.pango_font_description_set_variant.argtypes = [_PangoFontDescription,PangoVariant]
except:
   pass
try:
    libgtk3.pango_font_description_set_size.restype = None
    libgtk3.pango_font_description_set_size.argtypes = [_PangoFontDescription,gint]
except:
   pass
try:
    libgtk3.pango_font_description_get_size_is_absolute.restype = gboolean
    libgtk3.pango_font_description_get_size_is_absolute.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_unset_fields.restype = None
    libgtk3.pango_font_description_unset_fields.argtypes = [_PangoFontDescription,PangoFontMask]
except:
   pass
try:
    libgtk3.pango_font_description_set_weight.restype = None
    libgtk3.pango_font_description_set_weight.argtypes = [_PangoFontDescription,PangoWeight]
except:
   pass
try:
    libgtk3.pango_font_description_get_style.restype = PangoStyle
    libgtk3.pango_font_description_get_style.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_get_weight.restype = PangoWeight
    libgtk3.pango_font_description_get_weight.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_set_style.restype = None
    libgtk3.pango_font_description_set_style.argtypes = [_PangoFontDescription,PangoStyle]
except:
   pass
try:
    libgtk3.pango_font_description_get_gravity.restype = PangoGravity
    libgtk3.pango_font_description_get_gravity.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_get_size.restype = gint
    libgtk3.pango_font_description_get_size.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_merge_static.restype = None
    libgtk3.pango_font_description_merge_static.argtypes = [_PangoFontDescription,_PangoFontDescription,gboolean]
except:
   pass
try:
    libgtk3.pango_font_description_better_match.restype = gboolean
    libgtk3.pango_font_description_better_match.argtypes = [_PangoFontDescription,_PangoFontDescription,_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_set_stretch.restype = None
    libgtk3.pango_font_description_set_stretch.argtypes = [_PangoFontDescription,PangoStretch]
except:
   pass
try:
    libgtk3.pango_font_description_hash.restype = guint
    libgtk3.pango_font_description_hash.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_set_family.restype = None
    libgtk3.pango_font_description_set_family.argtypes = [_PangoFontDescription,Asciifier]
except:
   pass
try:
    libgtk3.pango_font_description_get_stretch.restype = PangoStretch
    libgtk3.pango_font_description_get_stretch.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_descriptions_free.restype = None
    libgtk3.pango_font_descriptions_free.argtypes = [_PangoFontDescription,int]
except:
   pass
try:
    libgtk3.pango_font_description_get_family.restype = c_char_p
    libgtk3.pango_font_description_get_family.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_copy_static.restype = _PangoFontDescription
    libgtk3.pango_font_description_copy_static.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_set_absolute_size.restype = None
    libgtk3.pango_font_description_set_absolute_size.argtypes = [_PangoFontDescription,double]
except:
   pass
try:
    libgtk3.pango_font_description_merge.restype = None
    libgtk3.pango_font_description_merge.argtypes = [_PangoFontDescription,_PangoFontDescription,gboolean]
except:
   pass
try:
    libgtk3.pango_font_description_to_filename.restype = c_char_p
    libgtk3.pango_font_description_to_filename.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_set_gravity.restype = None
    libgtk3.pango_font_description_set_gravity.argtypes = [_PangoFontDescription,PangoGravity]
except:
   pass
try:
    libgtk3.pango_font_description_get_variant.restype = PangoVariant
    libgtk3.pango_font_description_get_variant.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_free.restype = None
    libgtk3.pango_font_description_free.argtypes = [_PangoFontDescription]
except:
   pass
try:
    libgtk3.pango_font_description_from_string.restype = _PangoFontDescription
    libgtk3.pango_font_description_from_string.argtypes = [Asciifier]
except:
   pass
from . import gobject__GBoxed
class PangoFontDescription( gobject__GBoxed.GBoxed):
    """Class PangoFontDescription Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.pango_font_description_new.restype = POINTER(c_void_p)
            
            libgtk3.pango_font_description_new.argtypes = []
            self._object = libgtk3.pango_font_description_new()

    """Methods"""
    def to_string(  self, ):

        
        return libgtk3.pango_font_description_to_string( self._object )

    def copy(  self, ):

        from .gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libgtk3.pango_font_description_copy( self._object )  or POINTER(c_void_p)())

    def equal(  self, desc2, ):
        if desc2: desc2 = desc2._object
        else: desc2 = POINTER(c_void_p)()

        
        return libgtk3.pango_font_description_equal( self._object,desc2 )

    def set_family_static(  self, family, ):

        
        libgtk3.pango_font_description_set_family_static( self._object,family )

    def get_set_fields(  self, ):

        
        return libgtk3.pango_font_description_get_set_fields( self._object )

    def set_variant(  self, variant, ):

        
        libgtk3.pango_font_description_set_variant( self._object,variant )

    def set_size(  self, size, ):

        
        libgtk3.pango_font_description_set_size( self._object,size )

    def get_size_is_absolute(  self, ):

        
        return libgtk3.pango_font_description_get_size_is_absolute( self._object )

    def unset_fields(  self, to_unset, ):

        
        libgtk3.pango_font_description_unset_fields( self._object,to_unset )

    def set_weight(  self, weight, ):

        
        libgtk3.pango_font_description_set_weight( self._object,weight )

    def get_style(  self, ):

        
        return libgtk3.pango_font_description_get_style( self._object )

    def get_weight(  self, ):

        
        return libgtk3.pango_font_description_get_weight( self._object )

    def set_style(  self, style, ):

        
        libgtk3.pango_font_description_set_style( self._object,style )

    def get_gravity(  self, ):

        
        return libgtk3.pango_font_description_get_gravity( self._object )

    def get_size(  self, ):

        
        return libgtk3.pango_font_description_get_size( self._object )

    def merge_static(  self, desc_to_merge, replace_existing, ):
        if desc_to_merge: desc_to_merge = desc_to_merge._object
        else: desc_to_merge = POINTER(c_void_p)()

        
        libgtk3.pango_font_description_merge_static( self._object,desc_to_merge,replace_existing )

    def better_match(  self, old_match, new_match, ):
        if old_match: old_match = old_match._object
        else: old_match = POINTER(c_void_p)()
        if new_match: new_match = new_match._object
        else: new_match = POINTER(c_void_p)()

        
        return libgtk3.pango_font_description_better_match( self._object,old_match,new_match )

    def set_stretch(  self, stretch, ):

        
        libgtk3.pango_font_description_set_stretch( self._object,stretch )

    def hash(  self, ):

        
        return libgtk3.pango_font_description_hash( self._object )

    def set_family(  self, family, ):

        
        libgtk3.pango_font_description_set_family( self._object,family )

    def get_stretch(  self, ):

        
        return libgtk3.pango_font_description_get_stretch( self._object )

    def pango_font_descriptions_free(  self, n_descs, ):

        
        libgtk3.pango_font_descriptions_free( self._object,n_descs )

    def get_family(  self, ):

        
        return libgtk3.pango_font_description_get_family( self._object )

    def copy_static(  self, ):

        from .gtk3 import PangoFontDescription
        return PangoFontDescription( obj=libgtk3.pango_font_description_copy_static( self._object )  or POINTER(c_void_p)())

    def set_absolute_size(  self, size, ):

        
        libgtk3.pango_font_description_set_absolute_size( self._object,size )

    def merge(  self, desc_to_merge, replace_existing, ):
        if desc_to_merge: desc_to_merge = desc_to_merge._object
        else: desc_to_merge = POINTER(c_void_p)()

        
        libgtk3.pango_font_description_merge( self._object,desc_to_merge,replace_existing )

    def to_filename(  self, ):

        
        return libgtk3.pango_font_description_to_filename( self._object )

    def set_gravity(  self, gravity, ):

        
        libgtk3.pango_font_description_set_gravity( self._object,gravity )

    def get_variant(  self, ):

        
        return libgtk3.pango_font_description_get_variant( self._object )

    def free(  self, ):

        
        libgtk3.pango_font_description_free( self._object )

    @staticmethod
    def from_string( str,):
        from .gtk3 import PangoFontDescription
        return PangoFontDescription( obj=    libgtk3.pango_font_description_from_string(str, )
  or POINTER(c_void_p)())
