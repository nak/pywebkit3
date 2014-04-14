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
from cairo_types import *
from cairo_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GtkLabel = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_GAsyncResult = POINTER(c_int)
_cairo_matrix_t = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GClosure = POINTER(c_int)
_GIcon = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
_GFileEnumerator = POINTER(c_int)
_GtkDialog = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_void = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_GtkIconInfo = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkNumerableIcon = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GObject = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GAppLaunchContext = POINTER(c_int)
_PangoAttrIterator = POINTER(c_int)
_GFileAttributeMatcher = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkIconTheme = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAccelLabel = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GString = POINTER(c_int)
_GFileAttributeMatcher = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_GdkPoint = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GSource = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_JSString = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GSource = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_GFileInfo = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_GEmblemedIcon = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
_GScanner = POINTER(c_int)
_GFileAttributeInfoList = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
_GActionGroup = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GFile = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
_GFileInputStream = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkPixbufAnimationIter = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkEventButton = POINTER(c_int)
_GCancellable = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_GMount = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GFile = POINTER(c_int)
_GDrive = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_GMutex = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GtkStatusbar = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkPrintOperation = POINTER(c_int)
_GtkThemingEngine = POINTER(c_int)
_GString = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GFileInfo = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_GTimeVal = POINTER(c_int)
_GSourceFuncs = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_GtkStylePropertyParser = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkPixbufAnimation = POINTER(c_int)
_GEmblem = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GVolume = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_GPollFD = POINTER(c_int)
_GFileOutputStream = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_WebKitWebNavigationAction = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GParameter = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkGradient = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GMountOperation = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GSourceCallbackFuncs = POINTER(c_int)
_PangoFontFace = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GByteArray = POINTER(c_int)
_GdkPixbufSimpleAnim = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
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
WebKitLoadStatus = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitEditingBehavior = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GApplicationFlags = c_int
GtkDialogFlags = c_int
GtkResponseType = c_int
WebKitWebNavigationReason = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GMountMountFlags = c_int
GMountUnmountFlags = c_int
GDriveStartFlags = c_int
GDriveStartStopType = c_int
cairo_extend_t = c_int
cairo_filter_t = c_int
CairoPatternype_t = c_int

try:
    libcairo.cairo_pattern_get_matrix.restype = None
    libcairo.cairo_pattern_get_matrix.argtypes = [_CairoPattern,_cairo_matrix_t]
except:
   pass
try:
    libcairo.cairo_pattern_get_rgba.restype = gint
    libcairo.cairo_pattern_get_rgba.argtypes = [_CairoPattern,POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_line_to.restype = None
    libcairo.cairo_mesh_pattern_line_to.argtypes = [_CairoPattern,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_set_extend.restype = None
    libcairo.cairo_pattern_set_extend.argtypes = [_CairoPattern,cairo_extend_t]
except:
   pass
try:
    libcairo.cairo_pattern_set_filter.restype = None
    libcairo.cairo_pattern_set_filter.argtypes = [_CairoPattern,cairo_filter_t]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_begin_patch.restype = None
    libcairo.cairo_mesh_pattern_begin_patch.argtypes = [_CairoPattern]
except:
   pass
try:
    libcairo.cairo_pattern_destroy.restype = None
    libcairo.cairo_pattern_destroy.argtypes = [_CairoPattern]
except:
   pass
try:
    libcairo.cairo_pattern_get_radial_circles.restype = gint
    libcairo.cairo_pattern_get_radial_circles.argtypes = [_CairoPattern,POINTER(double),POINTER(double),POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_get_corner_color_rgba.restype = gint
    libcairo.cairo_mesh_pattern_get_corner_color_rgba.argtypes = [_CairoPattern,unsigned,unsigned,POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libcairo.cairo_pattern_get_color_stop_rgba.restype = gint
    libcairo.cairo_pattern_get_color_stop_rgba.argtypes = [_CairoPattern,int,POINTER(double),POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libcairo.cairo_pattern_status.restype = gint
    libcairo.cairo_pattern_status.argtypes = [_CairoPattern]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_curve_to.restype = None
    libcairo.cairo_mesh_pattern_curve_to.argtypes = [_CairoPattern,double,double,double,double,double,double]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_set_corner_color_rgb.restype = None
    libcairo.cairo_mesh_pattern_set_corner_color_rgb.argtypes = [_CairoPattern,unsigned,double,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_get_surface.restype = gint
    libcairo.cairo_pattern_get_surface.argtypes = [_CairoPattern,_cairo_surface_t]
except:
   pass
try:
    libcairo.cairo_pattern_get_filter.restype = cairo_filter_t
    libcairo.cairo_pattern_get_filter.argtypes = [_CairoPattern]
except:
   pass
try:
    libcairo.cairo_pattern_add_color_stop_rgba.restype = None
    libcairo.cairo_pattern_add_color_stop_rgba.argtypes = [_CairoPattern,double,double,double,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_get_type.restype = CairoPatternype_t
    libcairo.cairo_pattern_get_type.argtypes = [_CairoPattern]
except:
   pass
try:
    libcairo.cairo_pattern_reference.restype = _CairoPattern
    libcairo.cairo_pattern_reference.argtypes = [_CairoPattern]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_set_corner_color_rgba.restype = None
    libcairo.cairo_mesh_pattern_set_corner_color_rgba.argtypes = [_CairoPattern,unsigned,double,double,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_set_matrix.restype = None
    libcairo.cairo_pattern_set_matrix.argtypes = [_CairoPattern,_cairo_matrix_t]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_get_control_point.restype = gint
    libcairo.cairo_mesh_pattern_get_control_point.argtypes = [_CairoPattern,unsigned,unsigned,POINTER(double),POINTER(double)]
except:
   pass
try:
    libcairo.cairo_pattern_get_linear_points.restype = gint
    libcairo.cairo_pattern_get_linear_points.argtypes = [_CairoPattern,POINTER(double),POINTER(double),POINTER(double),POINTER(double)]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_end_patch.restype = None
    libcairo.cairo_mesh_pattern_end_patch.argtypes = [_CairoPattern]
except:
   pass
try:
    libcairo.cairo_pattern_get_color_stop_count.restype = gint
    libcairo.cairo_pattern_get_color_stop_count.argtypes = [_CairoPattern,POINTER(int)]
except:
   pass
try:
    libcairo.cairo_pattern_get_user_data.restype = _void
    libcairo.cairo_pattern_get_user_data.argtypes = [_CairoPattern,gpointer]
except:
   pass
try:
    libcairo.cairo_pattern_get_extend.restype = cairo_extend_t
    libcairo.cairo_pattern_get_extend.argtypes = [_CairoPattern]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_get_path.restype = c_char_p
    libcairo.cairo_mesh_pattern_get_path.argtypes = [_CairoPattern,unsigned]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_move_to.restype = None
    libcairo.cairo_mesh_pattern_move_to.argtypes = [_CairoPattern,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_add_color_stop_rgb.restype = None
    libcairo.cairo_pattern_add_color_stop_rgb.argtypes = [_CairoPattern,double,double,double,double]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_get_patch_count.restype = gint
    libcairo.cairo_mesh_pattern_get_patch_count.argtypes = [_CairoPattern,unsigned]
except:
   pass
try:
    libcairo.cairo_mesh_pattern_set_control_point.restype = None
    libcairo.cairo_mesh_pattern_set_control_point.argtypes = [_CairoPattern,unsigned,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_create_rgb.restype = _CairoPattern
    libcairo.cairo_pattern_create_rgb.argtypes = [double,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_create_linear.restype = _CairoPattern
    libcairo.cairo_pattern_create_linear.argtypes = [double,double,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_create_for_surface.restype = _CairoPattern
    libcairo.cairo_pattern_create_for_surface.argtypes = [_cairo_surface_t]
except:
   pass
try:
    libcairo.cairo_pattern_create_mesh.restype = _CairoPattern
    libcairo.cairo_pattern_create_mesh.argtypes = []
except:
   pass
try:
    libcairo.cairo_pattern_create_radial.restype = _CairoPattern
    libcairo.cairo_pattern_create_radial.argtypes = [double,double,double,double,double,double]
except:
   pass
try:
    libcairo.cairo_pattern_create_rgba.restype = _CairoPattern
    libcairo.cairo_pattern_create_rgba.argtypes = [double,double,double,double]
except:
   pass
class CairoPattern( object):
    """Class CairoPattern Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_matrix(  self, matrix, ):
        if matrix: matrix = matrix._object
        else: matrix = POINTER(c_int)()

        
        libcairo.cairo_pattern_get_matrix( self._object,matrix )

    def get_rgba(  self, red, green, blue, alpha, ):

        
        return libcairo.cairo_pattern_get_rgba( self._object,red,green,blue,alpha )

    def cairo_mesh_pattern_line_to(  self, x, y, ):

        
        libcairo.cairo_mesh_pattern_line_to( self._object,x,y )

    def set_extend(  self, extend, ):

        
        libcairo.cairo_pattern_set_extend( self._object,extend )

    def set_filter(  self, filter, ):

        
        libcairo.cairo_pattern_set_filter( self._object,filter )

    def cairo_mesh_pattern_begin_patch(  self, ):

        
        libcairo.cairo_mesh_pattern_begin_patch( self._object )

    def destroy(  self, ):

        
        libcairo.cairo_pattern_destroy( self._object )

    def get_radial_circles(  self, x0, y0, r0, x1, y1, r1, ):

        
        return libcairo.cairo_pattern_get_radial_circles( self._object,x0,y0,r0,x1,y1,r1 )

    def cairo_mesh_pattern_get_corner_color_rgba(  self, patch_num, corner_num, red, green, blue, alpha, ):

        
        return libcairo.cairo_mesh_pattern_get_corner_color_rgba( self._object,patch_num,corner_num,red,green,blue,alpha )

    def get_color_stop_rgba(  self, index, offset, red, green, blue, alpha, ):

        
        return libcairo.cairo_pattern_get_color_stop_rgba( self._object,index,offset,red,green,blue,alpha )

    def status(  self, ):

        
        return libcairo.cairo_pattern_status( self._object )

    def cairo_mesh_pattern_curve_to(  self, x1, y1, x2, y2, x3, y3, ):

        
        libcairo.cairo_mesh_pattern_curve_to( self._object,x1,y1,x2,y2,x3,y3 )

    def cairo_mesh_pattern_set_corner_color_rgb(  self, corner_num, red, green, blue, ):

        
        libcairo.cairo_mesh_pattern_set_corner_color_rgb( self._object,corner_num,red,green,blue )

    def get_surface(  self, surface, ):
        if surface: surface = surface._object
        else: surface = POINTER(c_int)()

        
        return libcairo.cairo_pattern_get_surface( self._object,surface )

    def get_filter(  self, ):

        
        return libcairo.cairo_pattern_get_filter( self._object )

    def add_color_stop_rgba(  self, offset, red, green, blue, alpha, ):

        
        libcairo.cairo_pattern_add_color_stop_rgba( self._object,offset,red,green,blue,alpha )

    def get_type(  self, ):

        
        return libcairo.cairo_pattern_get_type( self._object )

    def reference(  self, ):

        
        return libcairo.cairo_pattern_reference( self._object )

    def cairo_mesh_pattern_set_corner_color_rgba(  self, corner_num, red, green, blue, alpha, ):

        
        libcairo.cairo_mesh_pattern_set_corner_color_rgba( self._object,corner_num,red,green,blue,alpha )

    def set_matrix(  self, matrix, ):
        if matrix: matrix = matrix._object
        else: matrix = POINTER(c_int)()

        
        libcairo.cairo_pattern_set_matrix( self._object,matrix )

    def cairo_mesh_pattern_get_control_point(  self, patch_num, point_num, x, y, ):

        
        return libcairo.cairo_mesh_pattern_get_control_point( self._object,patch_num,point_num,x,y )

    def get_linear_points(  self, x0, y0, x1, y1, ):

        
        return libcairo.cairo_pattern_get_linear_points( self._object,x0,y0,x1,y1 )

    def cairo_mesh_pattern_end_patch(  self, ):

        
        libcairo.cairo_mesh_pattern_end_patch( self._object )

    def get_color_stop_count(  self, count, ):

        
        return libcairo.cairo_pattern_get_color_stop_count( self._object,count )

    def get_user_data(  self, key, ):

        
        libcairo.cairo_pattern_get_user_data( self._object,key )

    def get_extend(  self, ):

        
        return libcairo.cairo_pattern_get_extend( self._object )

    def cairo_mesh_pattern_get_path(  self, patch_num, ):

        
        return libcairo.cairo_mesh_pattern_get_path( self._object,patch_num )

    def cairo_mesh_pattern_move_to(  self, x, y, ):

        
        libcairo.cairo_mesh_pattern_move_to( self._object,x,y )

    def add_color_stop_rgb(  self, offset, red, green, blue, ):

        
        libcairo.cairo_pattern_add_color_stop_rgb( self._object,offset,red,green,blue )

    def cairo_mesh_pattern_get_patch_count(  self, count, ):

        
        return libcairo.cairo_mesh_pattern_get_patch_count( self._object,count )

    def cairo_mesh_pattern_set_control_point(  self, point_num, x, y, ):

        
        libcairo.cairo_mesh_pattern_set_control_point( self._object,point_num,x,y )

    @staticmethod
    def create_rgb( red, green, blue,):
        
        return     libcairo.cairo_pattern_create_rgb(red, green, blue, )

    @staticmethod
    def create_linear( x0, y0, x1, y1,):
        
        return     libcairo.cairo_pattern_create_linear(x0, y0, x1, y1, )

    @staticmethod
    def create_for_surface( surface,):
        if surface: surface = surface._object
        else: surface = POINTER(c_int)()
        
        return     libcairo.cairo_pattern_create_for_surface(surface, )

    @staticmethod
    def create_mesh():
        
        return     libcairo.cairo_pattern_create_mesh()

    @staticmethod
    def create_radial( cx0, cy0, radius0, cx1, cy1, radius1,):
        
        return     libcairo.cairo_pattern_create_radial(cx0, cy0, radius0, cx1, cy1, radius1, )

    @staticmethod
    def create_rgba( red, green, blue, alpha,):
        
        return     libcairo.cairo_pattern_create_rgba(red, green, blue, alpha, )

