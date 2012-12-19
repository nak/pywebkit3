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
from gtk3_enums import *
from gtk3_types import *
from gtk3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GIcon = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GtkNumerableIcon = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_GError = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_GSList = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkPixbufSimpleAnim = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_GdkDevice = POINTER(c_int)
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
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int

try:
    libgtk3.pango_matrix_transform_pixel_rectangle.restype = None
    libgtk3.pango_matrix_transform_pixel_rectangle.argtypes = [_PangoMatrix,_PangoRectangle]
except:
   pass
try:
    libgtk3.pango_matrix_rotate.restype = None
    libgtk3.pango_matrix_rotate.argtypes = [_PangoMatrix,double]
except:
   pass
try:
    libgtk3.pango_matrix_transform_distance.restype = None
    libgtk3.pango_matrix_transform_distance.argtypes = [_PangoMatrix,POINTER(double),POINTER(double)]
except:
   pass
try:
    libgtk3.pango_matrix_translate.restype = None
    libgtk3.pango_matrix_translate.argtypes = [_PangoMatrix,gdouble,gdouble]
except:
   pass
try:
    libgtk3.pango_matrix_transform_rectangle.restype = None
    libgtk3.pango_matrix_transform_rectangle.argtypes = [_PangoMatrix,_PangoRectangle]
except:
   pass
try:
    libgtk3.pango_matrix_transform_point.restype = None
    libgtk3.pango_matrix_transform_point.argtypes = [_PangoMatrix,POINTER(double),POINTER(double)]
except:
   pass
try:
    libgtk3.pango_matrix_scale.restype = None
    libgtk3.pango_matrix_scale.argtypes = [_PangoMatrix,double,double]
except:
   pass
try:
    libgtk3.pango_matrix_copy.restype = _PangoMatrix
    libgtk3.pango_matrix_copy.argtypes = [_PangoMatrix]
except:
   pass
try:
    libgtk3.pango_matrix_get_font_scale_factor.restype = double
    libgtk3.pango_matrix_get_font_scale_factor.argtypes = [_PangoMatrix]
except:
   pass
try:
    libgtk3.pango_matrix_free.restype = None
    libgtk3.pango_matrix_free.argtypes = [_PangoMatrix]
except:
   pass
try:
    libgtk3.pango_matrix_concat.restype = None
    libgtk3.pango_matrix_concat.argtypes = [_PangoMatrix,_PangoMatrix]
except:
   pass
import gobject__GBoxed
class PangoMatrix( gobject__GBoxed.GBoxed):
    """Class PangoMatrix Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def transform_pixel_rectangle(  self, rect, ):
        if rect: rect = rect._object
        else: rect = POINTER(c_int)()

        
        libgtk3.pango_matrix_transform_pixel_rectangle( self._object,rect )

    def rotate(  self, degrees, ):

        
        libgtk3.pango_matrix_rotate( self._object,degrees )

    def transform_distance(  self, dx, dy, ):

        
        libgtk3.pango_matrix_transform_distance( self._object,dx,dy )

    def translate(  self, tx, ty, ):

        
        libgtk3.pango_matrix_translate( self._object,tx,ty )

    def transform_rectangle(  self, rect, ):
        if rect: rect = rect._object
        else: rect = POINTER(c_int)()

        
        libgtk3.pango_matrix_transform_rectangle( self._object,rect )

    def transform_point(  self, x, y, ):

        
        libgtk3.pango_matrix_transform_point( self._object,x,y )

    def scale(  self, scale_x, scale_y, ):

        
        libgtk3.pango_matrix_scale( self._object,scale_x,scale_y )

    def copy(  self, ):

        from gtk3 import PangoMatrix
        return PangoMatrix( obj=libgtk3.pango_matrix_copy( self._object )  or POINTER(c_int)())

    def get_font_scale_factor(  self, ):

        
        return libgtk3.pango_matrix_get_font_scale_factor( self._object )

    def free(  self, ):

        
        libgtk3.pango_matrix_free( self._object )

    def concat(  self, new_matrix, ):
        if new_matrix: new_matrix = new_matrix._object
        else: new_matrix = POINTER(c_int)()

        
        libgtk3.pango_matrix_concat( self._object,new_matrix )

