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
_WebKitNetworkResponse = POINTER(c_void_p)
_GtkLabel = POINTER(c_void_p)
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
_GtkDialog = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_void = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GtkTextBuffer = POINTER(c_void_p)
_GtkTargetList = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
_GtkNumerableIcon = POINTER(c_void_p)
_GdkAppLaunchContext = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GtkSymbolicColor = POINTER(c_void_p)
_WebKitWebBackForwardList = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_GtkOffscreenWindow = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GAppLaunchContext = POINTER(c_void_p)
_PangoAttrIterator = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_JSGlobalContext = POINTER(c_void_p)
_GApplication = POINTER(c_void_p)
_GFileMonitor = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_WebKitHitTestResult = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
_GtkPathPriorityType = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitWebInspector = POINTER(c_void_p)
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
_WebKitWebFrame = POINTER(c_void_p)
_GActionGroup = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_WebKitNetworkRequest = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_WebKitViewportAttributes = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_cairo_t = POINTER(c_void_p)
_GWeakRef = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GdkEventButton = POINTER(c_void_p)
_GCancellable = POINTER(c_void_p)
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
_WebKitWebView = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitDOMDocument = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkPrintOperation = POINTER(c_void_p)
_GtkThemingEngine = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_SoupMessage = POINTER(c_void_p)
_WebKitWebDataSource = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_gunichar = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_WebKitDOMNode = POINTER(c_void_p)
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

try:
    libgtk3.gtk_style_context_remove_provider.restype = None
    libgtk3.gtk_style_context_remove_provider.argtypes = [_GtkStyleContext,_GtkStyleProvider]
except:
   pass
try:
    libgtk3.gtk_style_context_get_junction_sides.restype = GtkJunctionSides
    libgtk3.gtk_style_context_get_junction_sides.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_has_class.restype = gboolean
    libgtk3.gtk_style_context_has_class.argtypes = [_GtkStyleContext,Asciifier]
except:
   pass
try:
    libgtk3.gtk_style_context_add_class.restype = None
    libgtk3.gtk_style_context_add_class.argtypes = [_GtkStyleContext,Asciifier]
except:
   pass
try:
    libgtk3.gtk_style_context_add_region.restype = None
    libgtk3.gtk_style_context_add_region.argtypes = [_GtkStyleContext,Asciifier,GtkRegionFlags]
except:
   pass
try:
    libgtk3.gtk_style_context_push_animatable_region.restype = None
    libgtk3.gtk_style_context_push_animatable_region.argtypes = [_GtkStyleContext,gpointer]
except:
   pass
try:
    libgtk3.gtk_style_context_set_junction_sides.restype = None
    libgtk3.gtk_style_context_set_junction_sides.argtypes = [_GtkStyleContext,GtkJunctionSides]
except:
   pass
try:
    libgtk3.gtk_style_context_scroll_animations.restype = None
    libgtk3.gtk_style_context_scroll_animations.argtypes = [_GtkStyleContext,_GdkWindow,gint,gint]
except:
   pass
try:
    libgtk3.gtk_style_context_get_state.restype = GtkStateFlags
    libgtk3.gtk_style_context_get_state.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_set_screen.restype = None
    libgtk3.gtk_style_context_set_screen.argtypes = [_GtkStyleContext,_GdkScreen]
except:
   pass
try:
    libgtk3.gtk_style_context_get_style_property.restype = None
    libgtk3.gtk_style_context_get_style_property.argtypes = [_GtkStyleContext,Asciifier,_GValue]
except:
   pass
try:
    libgtk3.gtk_style_context_list_regions.restype = _GList
    libgtk3.gtk_style_context_list_regions.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_set_background.restype = None
    libgtk3.gtk_style_context_set_background.argtypes = [_GtkStyleContext,_GdkWindow]
except:
   pass
try:
    libgtk3.gtk_style_context_get_screen.restype = _GdkScreen
    libgtk3.gtk_style_context_get_screen.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_save.restype = None
    libgtk3.gtk_style_context_save.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_get_border_color.restype = None
    libgtk3.gtk_style_context_get_border_color.argtypes = [_GtkStyleContext,GtkStateFlags,_GdkRGBA]
except:
   pass
try:
    libgtk3.gtk_style_context_get_margin.restype = None
    libgtk3.gtk_style_context_get_margin.argtypes = [_GtkStyleContext,GtkStateFlags,_GtkBorder]
except:
   pass
try:
    libgtk3.gtk_style_context_lookup_icon_set.restype = _GtkIconSet
    libgtk3.gtk_style_context_lookup_icon_set.argtypes = [_GtkStyleContext,Asciifier]
except:
   pass
try:
    libgtk3.gtk_style_context_get_direction.restype = GtkTextDirection
    libgtk3.gtk_style_context_get_direction.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_get_property.restype = None
    libgtk3.gtk_style_context_get_property.argtypes = [_GtkStyleContext,Asciifier,GtkStateFlags,_GValue]
except:
   pass
try:
    libgtk3.gtk_style_context_restore.restype = None
    libgtk3.gtk_style_context_restore.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_get_font.restype = _PangoFontDescription
    libgtk3.gtk_style_context_get_font.argtypes = [_GtkStyleContext,GtkStateFlags]
except:
   pass
try:
    libgtk3.gtk_style_context_get.restype = None
    libgtk3.gtk_style_context_get.argtypes = [_GtkStyleContext,GtkStateFlags,]
except:
   pass
try:
    libgtk3.gtk_style_context_list_classes.restype = _GList
    libgtk3.gtk_style_context_list_classes.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_add_provider.restype = None
    libgtk3.gtk_style_context_add_provider.argtypes = [_GtkStyleContext,_GtkStyleProvider,guint]
except:
   pass
try:
    libgtk3.gtk_style_context_state_is_running.restype = gboolean
    libgtk3.gtk_style_context_state_is_running.argtypes = [_GtkStyleContext,GtkStateType,POINTER(gdouble)]
except:
   pass
try:
    libgtk3.gtk_style_context_set_path.restype = None
    libgtk3.gtk_style_context_set_path.argtypes = [_GtkStyleContext,_GtkWidgetPath]
except:
   pass
try:
    libgtk3.gtk_style_context_lookup_color.restype = gboolean
    libgtk3.gtk_style_context_lookup_color.argtypes = [_GtkStyleContext,Asciifier,_GdkRGBA]
except:
   pass
try:
    libgtk3.gtk_style_context_get_border.restype = None
    libgtk3.gtk_style_context_get_border.argtypes = [_GtkStyleContext,GtkStateFlags,_GtkBorder]
except:
   pass
try:
    libgtk3.gtk_style_context_remove_class.restype = None
    libgtk3.gtk_style_context_remove_class.argtypes = [_GtkStyleContext,Asciifier]
except:
   pass
try:
    libgtk3.gtk_style_context_remove_region.restype = None
    libgtk3.gtk_style_context_remove_region.argtypes = [_GtkStyleContext,Asciifier]
except:
   pass
try:
    libgtk3.gtk_style_context_set_state.restype = None
    libgtk3.gtk_style_context_set_state.argtypes = [_GtkStyleContext,GtkStateFlags]
except:
   pass
try:
    libgtk3.gtk_style_context_cancel_animations.restype = None
    libgtk3.gtk_style_context_cancel_animations.argtypes = [_GtkStyleContext,gpointer]
except:
   pass
try:
    libgtk3.gtk_style_context_pop_animatable_region.restype = None
    libgtk3.gtk_style_context_pop_animatable_region.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_invalidate.restype = None
    libgtk3.gtk_style_context_invalidate.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_get_color.restype = None
    libgtk3.gtk_style_context_get_color.argtypes = [_GtkStyleContext,GtkStateFlags,_GdkRGBA]
except:
   pass
try:
    libgtk3.gtk_style_context_set_direction.restype = None
    libgtk3.gtk_style_context_set_direction.argtypes = [_GtkStyleContext,GtkTextDirection]
except:
   pass
try:
    libgtk3.gtk_style_context_reset_widgets.restype = None
    libgtk3.gtk_style_context_reset_widgets.argtypes = [_GtkStyleContext,_GdkScreen]
except:
   pass
try:
    libgtk3.gtk_style_context_get_background_color.restype = None
    libgtk3.gtk_style_context_get_background_color.argtypes = [_GtkStyleContext,GtkStateFlags,_GdkRGBA]
except:
   pass
try:
    libgtk3.gtk_style_context_get_style.restype = None
    libgtk3.gtk_style_context_get_style.argtypes = [_GtkStyleContext,]
except:
   pass
try:
    libgtk3.gtk_style_context_has_region.restype = gboolean
    libgtk3.gtk_style_context_has_region.argtypes = [_GtkStyleContext,Asciifier,_GtkRegionFlags]
except:
   pass
try:
    libgtk3.gtk_style_context_get_path.restype = _GtkWidgetPath
    libgtk3.gtk_style_context_get_path.argtypes = [_GtkStyleContext]
except:
   pass
try:
    libgtk3.gtk_style_context_notify_state_change.restype = None
    libgtk3.gtk_style_context_notify_state_change.argtypes = [_GtkStyleContext,_GdkWindow,gpointer,GtkStateType,gboolean]
except:
   pass
try:
    libgtk3.gtk_style_context_add_provider_for_screen.restype = None
    libgtk3.gtk_style_context_add_provider_for_screen.argtypes = [_GtkStyleContext,_GdkScreen,_GtkStyleProvider,guint]
except:
   pass
try:
    libgtk3.gtk_style_context_remove_provider_for_screen.restype = None
    libgtk3.gtk_style_context_remove_provider_for_screen.argtypes = [_GtkStyleContext,_GdkScreen,_GtkStyleProvider]
except:
   pass
try:
    libgtk3.gtk_style_context_get_padding.restype = None
    libgtk3.gtk_style_context_get_padding.argtypes = [_GtkStyleContext,GtkStateFlags,_GtkBorder]
except:
   pass
from . import gobject__GObject
class GtkStyleContext( gobject__GObject.GObject):
    """Class GtkStyleContext Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_style_context_new.restype = POINTER(c_void_p)
            
            libgtk3.gtk_style_context_new.argtypes = []
            self._object = libgtk3.gtk_style_context_new()

    """Methods"""
    def remove_provider(  self, provider, ):
        if provider: provider = provider._object
        else: provider = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_remove_provider( self._object,provider )

    def get_junction_sides(  self, ):

        
        return libgtk3.gtk_style_context_get_junction_sides( self._object )

    def has_class(  self, class_name, ):

        
        return libgtk3.gtk_style_context_has_class( self._object,class_name )

    def add_class(  self, class_name, ):

        
        libgtk3.gtk_style_context_add_class( self._object,class_name )

    def add_region(  self, region_name, flags, ):
        if flags: flags = flags._object
        else: flags = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_add_region( self._object,region_name,flags )

    def push_animatable_region(  self, region_id, ):

        
        libgtk3.gtk_style_context_push_animatable_region( self._object,region_id )

    def set_junction_sides(  self, sides, ):

        
        libgtk3.gtk_style_context_set_junction_sides( self._object,sides )

    def scroll_animations(  self, window, dx, dy, ):
        if window: window = window._object
        else: window = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_scroll_animations( self._object,window,dx,dy )

    def get_state(  self, ):

        
        return libgtk3.gtk_style_context_get_state( self._object )

    def set_screen(  self, screen, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_set_screen( self._object,screen )

    def get_style_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_get_style_property( self._object,property_name,value )

    def list_regions(  self, ):

        from .gobject import GList
        return GList( obj=libgtk3.gtk_style_context_list_regions( self._object ) or POINTER(c_void_p)())

    def set_background(  self, window, ):
        if window: window = window._object
        else: window = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_set_background( self._object,window )

    def get_screen(  self, ):

        from .gobject import GdkScreen
        return GdkScreen( obj=libgtk3.gtk_style_context_get_screen( self._object ) or POINTER(c_void_p)())

    def save(  self, ):

        
        libgtk3.gtk_style_context_save( self._object )

    def get_border_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_get_border_color( self._object,state,color )

    def get_margin(  self, state, margin, ):
        if margin: margin = margin._object
        else: margin = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_get_margin( self._object,state,margin )

    def lookup_icon_set(  self, stock_id, ):

        from .gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_style_context_lookup_icon_set( self._object,stock_id ) or POINTER(c_void_p)())

    def get_direction(  self, ):

        
        return libgtk3.gtk_style_context_get_direction( self._object )

    def get_property(  self, property, state, value, ):
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_get_property( self._object,property,state,value )

    def restore(  self, ):

        
        libgtk3.gtk_style_context_restore( self._object )

    def get_font(  self, state, ):

        from .gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libgtk3.gtk_style_context_get_font( self._object,state )  or POINTER(c_void_p)())

    def get(  self, state,*args  ):


        def callit( state, *args ):
                for arg in args:
                     libgtk3.gtk_style_context_get.argtypes.append(args[1])
                return libgtk3.gtk_style_context_get( state, *args)
    
        return callit( self._object, state,*args )

    def list_classes(  self, ):

        from .gobject import GList
        return GList( obj=libgtk3.gtk_style_context_list_classes( self._object ) or POINTER(c_void_p)())

    def add_provider(  self, provider, priority, ):
        if provider: provider = provider._object
        else: provider = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_add_provider( self._object,provider,priority )

    def state_is_running(  self, state, progress, ):

        
        return libgtk3.gtk_style_context_state_is_running( self._object,state,progress )

    def set_path(  self, path, ):
        if path: path = path._object
        else: path = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_set_path( self._object,path )

    def lookup_color(  self, color_name, color, ):
        if color: color = color._object
        else: color = POINTER(c_void_p)()

        
        return libgtk3.gtk_style_context_lookup_color( self._object,color_name,color )

    def get_border(  self, state, border, ):
        if border: border = border._object
        else: border = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_get_border( self._object,state,border )

    def remove_class(  self, class_name, ):

        
        libgtk3.gtk_style_context_remove_class( self._object,class_name )

    def remove_region(  self, region_name, ):

        
        libgtk3.gtk_style_context_remove_region( self._object,region_name )

    def set_state(  self, flags, ):

        
        libgtk3.gtk_style_context_set_state( self._object,flags )

    def cancel_animations(  self, region_id, ):

        
        libgtk3.gtk_style_context_cancel_animations( self._object,region_id )

    def pop_animatable_region(  self, ):

        
        libgtk3.gtk_style_context_pop_animatable_region( self._object )

    def invalidate(  self, ):

        
        libgtk3.gtk_style_context_invalidate( self._object )

    def get_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_get_color( self._object,state,color )

    def set_direction(  self, direction, ):

        
        libgtk3.gtk_style_context_set_direction( self._object,direction )

    def reset_widgets(  self, screen, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_reset_widgets( self._object,screen )

    def get_background_color(  self, state, color, ):
        if color: color = color._object
        else: color = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_get_background_color( self._object,state,color )

    def get_style(  self,*args  ):


        def callit(  *args ):
                for arg in args:
                     libgtk3.gtk_style_context_get_style.argtypes.append(args[1])
                return libgtk3.gtk_style_context_get_style(  *args)
    
        return callit( self._object,*args )

    def has_region(  self, region_name, flags_return, ):
        if flags_return: flags_return = flags_return._object
        else: flags_return = POINTER(c_void_p)()

        
        return libgtk3.gtk_style_context_has_region( self._object,region_name,flags_return )

    def get_path(  self, ):

        from .gtk3 import GtkWidgetPath
        return GtkWidgetPath(None, obj=libgtk3.gtk_style_context_get_path( self._object ) or POINTER(c_void_p)())

    def notify_state_change(  self, window, region_id, state, state_value, ):
        if window: window = window._object
        else: window = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_notify_state_change( self._object,window,region_id,state,state_value )

    def add_provider_for_screen(  self, screen, provider, priority, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_void_p)()
        if provider: provider = provider._object
        else: provider = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_add_provider_for_screen( self._object,screen,provider,priority )

    def remove_provider_for_screen(  self, screen, provider, ):
        if screen: screen = screen._object
        else: screen = POINTER(c_void_p)()
        if provider: provider = provider._object
        else: provider = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_remove_provider_for_screen( self._object,screen,provider )

    def get_padding(  self, state, padding, ):
        if padding: padding = padding._object
        else: padding = POINTER(c_void_p)()

        
        libgtk3.gtk_style_context_get_padding( self._object,state,padding )

