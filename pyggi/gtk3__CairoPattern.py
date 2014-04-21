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
_GtkRcStyle = POINTER(c_void_p)
_GdkGeometry = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_cairo_matrix_t = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_GtkIconFactory = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GdkTimeCoord = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GClosure = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_void = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GtkTextBuffer = POINTER(c_void_p)
_GtkNumerableIcon = POINTER(c_void_p)
_GdkAppLaunchContext = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GtkSymbolicColor = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_GtkOffscreenWindow = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_PangoAttrIterator = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_GFileMonitor = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GtkPathPriorityType = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GOptionGroup = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_GtkWidgetClass = POINTER(c_void_p)
_GdkEventKey = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_PangoFontMetrics = POINTER(c_void_p)
_cairo_surface_t = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_cairo_t = POINTER(c_void_p)
_GWeakRef = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_PangoRectangle = POINTER(c_void_p)
_GtkAccelGroup = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GFile = POINTER(c_void_p)
_GtkAllocation = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_PangoLayoutLine = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_gunichar = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GtkStyleProperties = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GParameter = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_GtkGradient = POINTER(c_void_p)
_cairo_pattern_t = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GdkPixbufSimpleAnim = POINTER(c_void_p)
_WebKitGeolocationPolicyDecision = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
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
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
cairo_extend_t = c_int
cairo_filter_t = c_int
CairoPatternype_t = c_int

try:
    libgtk3.cairo_pattern_get_matrix.restype = None
    libgtk3.cairo_pattern_get_matrix.argtypes = [_CairoPattern,_cairo_matrix_t]
except:
   pass
try:
    libgtk3.cairo_pattern_get_rgba.restype = gint
    libgtk3.cairo_pattern_get_rgba.argtypes = [_CairoPattern,POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_line_to.restype = None
    libgtk3.cairo_mesh_pattern_line_to.argtypes = [_CairoPattern,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_set_extend.restype = None
    libgtk3.cairo_pattern_set_extend.argtypes = [_CairoPattern,cairo_extend_t]
except:
   pass
try:
    libgtk3.cairo_pattern_set_filter.restype = None
    libgtk3.cairo_pattern_set_filter.argtypes = [_CairoPattern,cairo_filter_t]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_begin_patch.restype = None
    libgtk3.cairo_mesh_pattern_begin_patch.argtypes = [_CairoPattern]
except:
   pass
try:
    libgtk3.cairo_pattern_destroy.restype = None
    libgtk3.cairo_pattern_destroy.argtypes = [_CairoPattern]
except:
   pass
try:
    libgtk3.cairo_pattern_get_radial_circles.restype = gint
    libgtk3.cairo_pattern_get_radial_circles.argtypes = [_CairoPattern,POINTER(double),POINTER(double),POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_get_corner_color_rgba.restype = gint
    libgtk3.cairo_mesh_pattern_get_corner_color_rgba.argtypes = [_CairoPattern,unsigned,unsigned,POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libgtk3.cairo_pattern_get_color_stop_rgba.restype = gint
    libgtk3.cairo_pattern_get_color_stop_rgba.argtypes = [_CairoPattern,int,POINTER(double),POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libgtk3.cairo_pattern_status.restype = gint
    libgtk3.cairo_pattern_status.argtypes = [_CairoPattern]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_curve_to.restype = None
    libgtk3.cairo_mesh_pattern_curve_to.argtypes = [_CairoPattern,double,double,double,double,double,double]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_set_corner_color_rgb.restype = None
    libgtk3.cairo_mesh_pattern_set_corner_color_rgb.argtypes = [_CairoPattern,unsigned,double,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_get_surface.restype = gint
    libgtk3.cairo_pattern_get_surface.argtypes = [_CairoPattern,_cairo_surface_t]
except:
   pass
try:
    libgtk3.cairo_pattern_get_filter.restype = cairo_filter_t
    libgtk3.cairo_pattern_get_filter.argtypes = [_CairoPattern]
except:
   pass
try:
    libgtk3.cairo_pattern_add_color_stop_rgba.restype = None
    libgtk3.cairo_pattern_add_color_stop_rgba.argtypes = [_CairoPattern,double,double,double,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_get_type.restype = CairoPatternype_t
    libgtk3.cairo_pattern_get_type.argtypes = [_CairoPattern]
except:
   pass
try:
    libgtk3.cairo_pattern_reference.restype = _CairoPattern
    libgtk3.cairo_pattern_reference.argtypes = [_CairoPattern]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_set_corner_color_rgba.restype = None
    libgtk3.cairo_mesh_pattern_set_corner_color_rgba.argtypes = [_CairoPattern,unsigned,double,double,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_set_matrix.restype = None
    libgtk3.cairo_pattern_set_matrix.argtypes = [_CairoPattern,_cairo_matrix_t]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_get_control_point.restype = gint
    libgtk3.cairo_mesh_pattern_get_control_point.argtypes = [_CairoPattern,unsigned,unsigned,POINTER(double),POINTER(double)]
except:
   pass
try:
    libgtk3.cairo_pattern_get_linear_points.restype = gint
    libgtk3.cairo_pattern_get_linear_points.argtypes = [_CairoPattern,POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_end_patch.restype = None
    libgtk3.cairo_mesh_pattern_end_patch.argtypes = [_CairoPattern]
except:
   pass
try:
    libgtk3.cairo_pattern_get_color_stop_count.restype = gint
    libgtk3.cairo_pattern_get_color_stop_count.argtypes = [_CairoPattern,POINTER(int)]
except:
   pass
try:
    libgtk3.cairo_pattern_get_user_data.restype = _void
    libgtk3.cairo_pattern_get_user_data.argtypes = [_CairoPattern,gpointer]
except:
   pass
try:
    libgtk3.cairo_pattern_get_extend.restype = cairo_extend_t
    libgtk3.cairo_pattern_get_extend.argtypes = [_CairoPattern]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_get_path.restype = c_char_p
    libgtk3.cairo_mesh_pattern_get_path.argtypes = [_CairoPattern,unsigned]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_move_to.restype = None
    libgtk3.cairo_mesh_pattern_move_to.argtypes = [_CairoPattern,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_add_color_stop_rgb.restype = None
    libgtk3.cairo_pattern_add_color_stop_rgb.argtypes = [_CairoPattern,double,double,double,double]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_get_patch_count.restype = gint
    libgtk3.cairo_mesh_pattern_get_patch_count.argtypes = [_CairoPattern,unsigned]
except:
   pass
try:
    libgtk3.cairo_mesh_pattern_set_control_point.restype = None
    libgtk3.cairo_mesh_pattern_set_control_point.argtypes = [_CairoPattern,unsigned,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_create_rgb.restype = _CairoPattern
    libgtk3.cairo_pattern_create_rgb.argtypes = [double,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_create_linear.restype = _CairoPattern
    libgtk3.cairo_pattern_create_linear.argtypes = [double,double,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_create_for_surface.restype = _CairoPattern
    libgtk3.cairo_pattern_create_for_surface.argtypes = [_cairo_surface_t]
except:
   pass
try:
    libgtk3.cairo_pattern_create_mesh.restype = _CairoPattern
    libgtk3.cairo_pattern_create_mesh.argtypes = []
except:
   pass
try:
    libgtk3.cairo_pattern_create_radial.restype = _CairoPattern
    libgtk3.cairo_pattern_create_radial.argtypes = [double,double,double,double,double,double]
except:
   pass
try:
    libgtk3.cairo_pattern_create_rgba.restype = _CairoPattern
    libgtk3.cairo_pattern_create_rgba.argtypes = [double,double,double,double]
except:
   pass
class CairoPattern( object):
    """Class CairoPattern Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_matrix(  self, matrix, ):
        if matrix: matrix = matrix._object
        else: matrix = POINTER(c_void_p)()

        
        libgtk3.cairo_pattern_get_matrix( self._object,matrix )

    def get_rgba(  self, red, green, blue, alpha, ):

        
        return libgtk3.cairo_pattern_get_rgba( self._object,red,green,blue,alpha )

    def cairo_mesh_pattern_line_to(  self, x, y, ):

        
        libgtk3.cairo_mesh_pattern_line_to( self._object,x,y )

    def set_extend(  self, extend, ):

        
        libgtk3.cairo_pattern_set_extend( self._object,extend )

    def set_filter(  self, filter, ):

        
        libgtk3.cairo_pattern_set_filter( self._object,filter )

    def cairo_mesh_pattern_begin_patch(  self, ):

        
        libgtk3.cairo_mesh_pattern_begin_patch( self._object )

    def destroy(  self, ):

        
        libgtk3.cairo_pattern_destroy( self._object )

    def get_radial_circles(  self, x0, y0, r0, x1, y1, r1, ):

        
        return libgtk3.cairo_pattern_get_radial_circles( self._object,x0,y0,r0,x1,y1,r1 )

    def cairo_mesh_pattern_get_corner_color_rgba(  self, patch_num, corner_num, red, green, blue, alpha, ):

        
        return libgtk3.cairo_mesh_pattern_get_corner_color_rgba( self._object,patch_num,corner_num,red,green,blue,alpha )

    def get_color_stop_rgba(  self, index, offset, red, green, blue, alpha, ):

        
        return libgtk3.cairo_pattern_get_color_stop_rgba( self._object,index,offset,red,green,blue,alpha )

    def status(  self, ):

        
        return libgtk3.cairo_pattern_status( self._object )

    def cairo_mesh_pattern_curve_to(  self, x1, y1, x2, y2, x3, y3, ):

        
        libgtk3.cairo_mesh_pattern_curve_to( self._object,x1,y1,x2,y2,x3,y3 )

    def cairo_mesh_pattern_set_corner_color_rgb(  self, corner_num, red, green, blue, ):

        
        libgtk3.cairo_mesh_pattern_set_corner_color_rgb( self._object,corner_num,red,green,blue )

    def get_surface(  self, surface, ):
        if surface: surface = surface._object
        else: surface = POINTER(c_void_p)()

        
        return libgtk3.cairo_pattern_get_surface( self._object,surface )

    def get_filter(  self, ):

        
        return libgtk3.cairo_pattern_get_filter( self._object )

    def add_color_stop_rgba(  self, offset, red, green, blue, alpha, ):

        
        libgtk3.cairo_pattern_add_color_stop_rgba( self._object,offset,red,green,blue,alpha )

    def get_type(  self, ):

        
        return libgtk3.cairo_pattern_get_type( self._object )

    def reference(  self, ):

        
        return libgtk3.cairo_pattern_reference( self._object )

    def cairo_mesh_pattern_set_corner_color_rgba(  self, corner_num, red, green, blue, alpha, ):

        
        libgtk3.cairo_mesh_pattern_set_corner_color_rgba( self._object,corner_num,red,green,blue,alpha )

    def set_matrix(  self, matrix, ):
        if matrix: matrix = matrix._object
        else: matrix = POINTER(c_void_p)()

        
        libgtk3.cairo_pattern_set_matrix( self._object,matrix )

    def cairo_mesh_pattern_get_control_point(  self, patch_num, point_num, x, y, ):

        
        return libgtk3.cairo_mesh_pattern_get_control_point( self._object,patch_num,point_num,x,y )

    def get_linear_points(  self, x0, y0, x1, y1, ):

        
        return libgtk3.cairo_pattern_get_linear_points( self._object,x0,y0,x1,y1 )

    def cairo_mesh_pattern_end_patch(  self, ):

        
        libgtk3.cairo_mesh_pattern_end_patch( self._object )

    def get_color_stop_count(  self, count, ):

        
        return libgtk3.cairo_pattern_get_color_stop_count( self._object,count )

    def get_user_data(  self, key, ):

        
        libgtk3.cairo_pattern_get_user_data( self._object,key )

    def get_extend(  self, ):

        
        return libgtk3.cairo_pattern_get_extend( self._object )

    def cairo_mesh_pattern_get_path(  self, patch_num, ):

        
        return libgtk3.cairo_mesh_pattern_get_path( self._object,patch_num )

    def cairo_mesh_pattern_move_to(  self, x, y, ):

        
        libgtk3.cairo_mesh_pattern_move_to( self._object,x,y )

    def add_color_stop_rgb(  self, offset, red, green, blue, ):

        
        libgtk3.cairo_pattern_add_color_stop_rgb( self._object,offset,red,green,blue )

    def cairo_mesh_pattern_get_patch_count(  self, count, ):

        
        return libgtk3.cairo_mesh_pattern_get_patch_count( self._object,count )

    def cairo_mesh_pattern_set_control_point(  self, point_num, x, y, ):

        
        libgtk3.cairo_mesh_pattern_set_control_point( self._object,point_num,x,y )

    @staticmethod
    def create_rgb( red, green, blue,):
        
        return     libgtk3.cairo_pattern_create_rgb(red, green, blue, )

    @staticmethod
    def create_linear( x0, y0, x1, y1,):
        
        return     libgtk3.cairo_pattern_create_linear(x0, y0, x1, y1, )

    @staticmethod
    def create_for_surface( surface,):
        if surface: surface = surface._object
        else: surface = POINTER(c_void_p)()
        
        return     libgtk3.cairo_pattern_create_for_surface(surface, )

    @staticmethod
    def create_mesh():
        
        return     libgtk3.cairo_pattern_create_mesh()

    @staticmethod
    def create_radial( cx0, cy0, radius0, cx1, cy1, radius1,):
        
        return     libgtk3.cairo_pattern_create_radial(cx0, cy0, radius0, cx1, cy1, radius1, )

    @staticmethod
    def create_rgba( red, green, blue, alpha,):
        
        return     libgtk3.cairo_pattern_create_rgba(red, green, blue, alpha, )

