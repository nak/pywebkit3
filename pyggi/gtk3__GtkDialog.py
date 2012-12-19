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
_GtkDialog = POINTER(c_int)
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
GtkDialogFlags = c_int
GtkResponseType = c_int

try:
    libgtk3.gtk_dialog_add_action_widget.restype = None
    libgtk3.gtk_dialog_add_action_widget.argtypes = [_GtkDialog,_GtkWidget,gint]
except:
   pass
try:
    libgtk3.gtk_dialog_set_alternative_button_order.restype = None
    libgtk3.gtk_dialog_set_alternative_button_order.argtypes = [_GtkDialog,gint,]
except:
   pass
try:
    libgtk3.gtk_dialog_set_response_sensitive.restype = None
    libgtk3.gtk_dialog_set_response_sensitive.argtypes = [_GtkDialog,gint,gboolean]
except:
   pass
try:
    libgtk3.gtk_dialog_add_button.restype = _GtkWidget
    libgtk3.gtk_dialog_add_button.argtypes = [_GtkDialog,c_char_p,gint]
except:
   pass
try:
    libgtk3.gtk_dialog_set_default_response.restype = None
    libgtk3.gtk_dialog_set_default_response.argtypes = [_GtkDialog,gint]
except:
   pass
try:
    libgtk3.gtk_dialog_run.restype = gint
    libgtk3.gtk_dialog_run.argtypes = [_GtkDialog]
except:
   pass
try:
    libgtk3.gtk_dialog_get_content_area.restype = _GtkWidget
    libgtk3.gtk_dialog_get_content_area.argtypes = [_GtkDialog]
except:
   pass
try:
    libgtk3.gtk_dialog_response.restype = None
    libgtk3.gtk_dialog_response.argtypes = [_GtkDialog,gint]
except:
   pass
try:
    libgtk3.gtk_dialog_get_response_for_widget.restype = gint
    libgtk3.gtk_dialog_get_response_for_widget.argtypes = [_GtkDialog,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_dialog_set_alternative_button_order_from_array.restype = None
    libgtk3.gtk_dialog_set_alternative_button_order_from_array.argtypes = [_GtkDialog,gint,POINTER(gint)]
except:
   pass
try:
    libgtk3.gtk_dialog_get_action_area.restype = _GtkWidget
    libgtk3.gtk_dialog_get_action_area.argtypes = [_GtkDialog]
except:
   pass
try:
    libgtk3.gtk_dialog_get_widget_for_response.restype = _GtkWidget
    libgtk3.gtk_dialog_get_widget_for_response.argtypes = [_GtkDialog,gint]
except:
   pass
try:
    libgtk3.gtk_dialog_add_buttons.restype = None
    libgtk3.gtk_dialog_add_buttons.argtypes = [_GtkDialog,c_char_p,]
except:
   pass
try:
    libgtk3.gtk_alternative_dialog_button_order.restype = gboolean
    libgtk3.gtk_alternative_dialog_button_order.argtypes = [_GdkScreen]
except:
   pass
try:
    libgtk3.gtk_dialog_new_with_buttons.restype = _GtkWidget
    libgtk3.gtk_dialog_new_with_buttons.argtypes = [c_char_p,_GtkWindow,GtkDialogFlags,c_char_p,]
except:
   pass
import gtk3__GtkBin
class GtkDialog( gtk3__GtkBin.GtkBin):
    """Class GtkDialog Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_dialog_new.restype = POINTER(c_int)
            
            libgtk3.gtk_dialog_new.argtypes = []
            self._object = libgtk3.gtk_dialog_new()

    """Methods"""
    def add_action_widget(  self, child, response_id, ):
        if child: child = child._object
        else: child = POINTER(c_int)()

        
        libgtk3.gtk_dialog_add_action_widget( self._object,child,response_id )

    def set_alternative_button_order(  self, first_response_id,*args  ):


        def callit( first_response_id, *args ):
                for arg in args:
                     libgtk3.gtk_dialog_set_alternative_button_order.argtypes.append(args[1])
                return libgtk3.gtk_dialog_set_alternative_button_order( first_response_id, *args)
    
        return callit( self._object, first_response_id,*args )

    def set_response_sensitive(  self, response_id, setting, ):

        
        libgtk3.gtk_dialog_set_response_sensitive( self._object,response_id,setting )

    def add_button(  self, button_text, response_id, ):

        from gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_dialog_add_button( self._object,button_text,response_id ) or POINTER(c_int)())

    def set_default_response(  self, response_id, ):

        
        libgtk3.gtk_dialog_set_default_response( self._object,response_id )

    def run(  self, ):

        
        return libgtk3.gtk_dialog_run( self._object )

    def get_content_area(  self, ):

        from gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_dialog_get_content_area( self._object ) or POINTER(c_int)())

    def response(  self, response_id, ):

        
        libgtk3.gtk_dialog_response( self._object,response_id )

    def get_response_for_widget(  self, widget, ):
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        
        return libgtk3.gtk_dialog_get_response_for_widget( self._object,widget )

    def set_alternative_button_order_from_array(  self, n_params, new_order, ):

        
        libgtk3.gtk_dialog_set_alternative_button_order_from_array( self._object,n_params,new_order )

    def get_action_area(  self, ):

        from gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_dialog_get_action_area( self._object ) or POINTER(c_int)())

    def get_widget_for_response(  self, response_id, ):

        from gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_dialog_get_widget_for_response( self._object,response_id ) or POINTER(c_int)())

    def add_buttons(  self, first_button_text,*args  ):


        def callit( first_button_text, *args ):
                for arg in args:
                     libgtk3.gtk_dialog_add_buttons.argtypes.append(args[1])
                return libgtk3.gtk_dialog_add_buttons( first_button_text, *args)
    
        return callit( self._object, first_button_text,*args )

    @staticmethod
    def gtk_alternative_dialog_button_order( screen,):
        if screen: screen = screen._object
        else: screen = POINTER(c_int)()
        
        return     libgtk3.gtk_alternative_dialog_button_order(screen, )

    @staticmethod
    def new_with_buttons( title, parent, flags, first_button_text,*args ):
        if parent: parent = parent._object
        else: parent = POINTER(c_int)()
        from gtk3 import GtkWidget
        return GtkWidget( obj=    libgtk3.gtk_dialog_new_with_buttons(title, parent, flags, first_button_text, *args)
 or POINTER(c_int)())
