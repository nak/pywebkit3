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
_WebKitNetworkResponse = POINTER(c_int)
_GtkLabel = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
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
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_void = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
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
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
_GScanner = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_GActionGroup = POINTER(c_int)
_cairo_region_t = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_cairo_t = POINTER(c_int)
_GWeakRef = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_GdkEventButton = POINTER(c_int)
_GCancellable = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GFile = POINTER(c_int)
_GtkAllocation = POINTER(c_int)
_GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkPrintOperation = POINTER(c_int)
_GtkThemingEngine = POINTER(c_int)
_PangoContext = POINTER(c_int)
_GList = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GParameter = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkGradient = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_CairoPattern = POINTER(c_int)
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

try:
    libgtk3.gtk_theming_engine_get_style_property.restype = None
    libgtk3.gtk_theming_engine_get_style_property.argtypes = [_GtkThemingEngine,c_char_p,_GValue]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_padding.restype = None
    libgtk3.gtk_theming_engine_get_padding.argtypes = [_GtkThemingEngine,GtkStateFlags,_GtkBorder]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_font.restype = _PangoFontDescription
    libgtk3.gtk_theming_engine_get_font.argtypes = [_GtkThemingEngine,GtkStateFlags]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_border.restype = None
    libgtk3.gtk_theming_engine_get_border.argtypes = [_GtkThemingEngine,GtkStateFlags,_GtkBorder]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_screen.restype = _GdkScreen
    libgtk3.gtk_theming_engine_get_screen.argtypes = [_GtkThemingEngine]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_style.restype = None
    libgtk3.gtk_theming_engine_get_style.argtypes = [_GtkThemingEngine,]
except:
   pass
try:
    libgtk3.gtk_theming_engine_register_property.restype = None
    libgtk3.gtk_theming_engine_register_property.argtypes = [_GtkThemingEngine,c_char_p,GtkStylePropertyParser,_GParamSpec]
except:
   pass
try:
    libgtk3.gtk_theming_engine_lookup_color.restype = gboolean
    libgtk3.gtk_theming_engine_lookup_color.argtypes = [_GtkThemingEngine,c_char_p,_GdkRGBA]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_background_color.restype = None
    libgtk3.gtk_theming_engine_get_background_color.argtypes = [_GtkThemingEngine,GtkStateFlags,_GdkRGBA]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_property.restype = None
    libgtk3.gtk_theming_engine_get_property.argtypes = [_GtkThemingEngine,c_char_p,GtkStateFlags,_GValue]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_border_color.restype = None
    libgtk3.gtk_theming_engine_get_border_color.argtypes = [_GtkThemingEngine,GtkStateFlags,_GdkRGBA]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_path.restype = _GtkWidgetPath
    libgtk3.gtk_theming_engine_get_path.argtypes = [_GtkThemingEngine]
except:
   pass
try:
    libgtk3.gtk_theming_engine_state_is_running.restype = gboolean
    libgtk3.gtk_theming_engine_state_is_running.argtypes = [_GtkThemingEngine,GtkStateType,POINTER(gdouble)]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_margin.restype = None
    libgtk3.gtk_theming_engine_get_margin.argtypes = [_GtkThemingEngine,GtkStateFlags,_GtkBorder]
except:
   pass
try:
    libgtk3.gtk_theming_engine_has_region.restype = gboolean
    libgtk3.gtk_theming_engine_has_region.argtypes = [_GtkThemingEngine,c_char_p,_GtkRegionFlags]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_state.restype = GtkStateFlags
    libgtk3.gtk_theming_engine_get_state.argtypes = [_GtkThemingEngine]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_junction_sides.restype = GtkJunctionSides
    libgtk3.gtk_theming_engine_get_junction_sides.argtypes = [_GtkThemingEngine]
except:
   pass
try:
    libgtk3.gtk_theming_engine_has_class.restype = gboolean
    libgtk3.gtk_theming_engine_has_class.argtypes = [_GtkThemingEngine,c_char_p]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get.restype = None
    libgtk3.gtk_theming_engine_get.argtypes = [_GtkThemingEngine,GtkStateFlags,]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_color.restype = None
    libgtk3.gtk_theming_engine_get_color.argtypes = [_GtkThemingEngine,GtkStateFlags,_GdkRGBA]
except:
   pass
try:
    libgtk3.gtk_theming_engine_get_direction.restype = GtkTextDirection
    libgtk3.gtk_theming_engine_get_direction.argtypes = [_GtkThemingEngine]
except:
   pass
try:
    libgtk3.gtk_theming_engine_load.restype = _GtkThemingEngine
    libgtk3.gtk_theming_engine_load.argtypes = [c_char_p]
except:
   pass
import gobject__GObject
class GtkThemingEngine( gobject__GObject.GObject):
    """Class GtkThemingEngine Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def get_style_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_get_style_property( self._object,property_name,value )

    def get_padding(  self, state, padding, ):
        if padding: padding = padding._object
        else: padding = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_get_padding( self._object,state,padding )

    def get_font(  self, state, ):

        from gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libgtk3.gtk_theming_engine_get_font( self._object,state )  or POINTER(c_int)())

    def get_border(  self, state, border, ):
        if border: border = border._object
        else: border = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_get_border( self._object,state,border )

    def get_screen(  self, ):

        from gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gtk_theming_engine_get_screen( self._object ) or POINTER(c_int)())

    def get_style(  self,*args  ):


        def callit(  *args ):
                for arg in args:
                     libgtk3.gtk_theming_engine_get_style.argtypes.append(args[1])
                return libgtk3.gtk_theming_engine_get_style(  *args)
    
        return callit( self._object,*args )

    def register_property(  self, name_space, parse_func, pspec, ):
        if parse_func: parse_func = parse_func._object
        else: parse_func = POINTER(c_int)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_register_property( self._object,name_space,parse_func,pspec )

    def lookup_color(  self, color_name, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        
        return libgtk3.gtk_theming_engine_lookup_color( self._object,color_name,color )

    def get_background_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_get_background_color( self._object,state,color )

    def get_property(  self, property, state, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_get_property( self._object,property,state,value )

    def get_border_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_get_border_color( self._object,state,color )

    def get_path(  self, ):

        from gtk3 import GtkWidgetPath
        return GtkWidgetPath(None, obj=libgtk3.gtk_theming_engine_get_path( self._object ) or POINTER(c_int)())

    def state_is_running(  self, state, progress, ):

        
        return libgtk3.gtk_theming_engine_state_is_running( self._object,state,progress )

    def get_margin(  self, state, margin, ):
        if margin: margin = margin._object
        else: margin = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_get_margin( self._object,state,margin )

    def has_region(  self, style_region, flags, ):
        if flags: flags = flags._object
        else: flags = POINTER(c_int)()

        
        return libgtk3.gtk_theming_engine_has_region( self._object,style_region,flags )

    def get_state(  self, ):

        
        return libgtk3.gtk_theming_engine_get_state( self._object )

    def get_junction_sides(  self, ):

        
        return libgtk3.gtk_theming_engine_get_junction_sides( self._object )

    def has_class(  self, style_class, ):

        
        return libgtk3.gtk_theming_engine_has_class( self._object,style_class )

    def get(  self, state,*args  ):


        def callit( state, *args ):
                for arg in args:
                     libgtk3.gtk_theming_engine_get.argtypes.append(args[1])
                return libgtk3.gtk_theming_engine_get( state, *args)
    
        return callit( self._object, state,*args )

    def get_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_int)()

        
        libgtk3.gtk_theming_engine_get_color( self._object,state,color )

    def get_direction(  self, ):

        
        return libgtk3.gtk_theming_engine_get_direction( self._object )

    @staticmethod
    def load( name,):
        from gtk3 import GtkThemingEngine
        return GtkThemingEngine( obj=    libgtk3.gtk_theming_engine_load(name, )
 or POINTER(c_int)())
