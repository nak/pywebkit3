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
_PangoFont = POINTER(c_void_p)
_WebKitNetworkResponse = POINTER(c_void_p)
_GtkLabel = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_GAsyncResult = POINTER(c_void_p)
_cairo_matrix_t = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_JSValue = POINTER(c_void_p)
_GtkIconFactory = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GdkTimeCoord = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GtkContainer = POINTER(c_void_p)
_PangoItem = POINTER(c_void_p)
_GClosure = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GMainContext = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_JSContextGroup = POINTER(c_void_p)
_GFileEnumerator = POINTER(c_void_p)
_GtkDialog = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GtkSymbolicColor = POINTER(c_void_p)
_void = POINTER(c_void_p)
_GtkStyleProperties = POINTER(c_void_p)
_GInputStream = POINTER(c_void_p)
_GtkIconInfo = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GBytes = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GMainContext = POINTER(c_void_p)
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
_GFileAttributeMatcher = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GtkIconTheme = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_GtkAccelLabel = POINTER(c_void_p)
_GtkAdjustment = POINTER(c_void_p)
_JSGlobalContext = POINTER(c_void_p)
_GApplication = POINTER(c_void_p)
_GFileMonitor = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_GString = POINTER(c_void_p)
_GFileAttributeMatcher = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_WebKitHitTestResult = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
_GBoxed = POINTER(c_void_p)
_GtkPathPriorityType = POINTER(c_void_p)
_JSClass = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_JSValue = POINTER(c_void_p)
_GdkPoint = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GSource = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_JSString = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GSource = POINTER(c_void_p)
_GtkMisc = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_GFileInfo = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_GEmblemedIcon = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_WebKitWebInspector = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_GOptionGroup = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_GFileAttributeInfoList = POINTER(c_void_p)
_GtkWidgetClass = POINTER(c_void_p)
_GtkContainerClass = POINTER(c_void_p)
_GdkEventKey = POINTER(c_void_p)
_GtkAdjustment = POINTER(c_void_p)
_GdkDragContext = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GFileIOStream = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_PangoFontMetrics = POINTER(c_void_p)
_GCond = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_cairo_surface_t = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_WebKitWebFrame = POINTER(c_void_p)
_JSString = POINTER(c_void_p)
_GActionGroup = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_WebKitNetworkRequest = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_GFile = POINTER(c_void_p)
_PangoLayoutIter = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoLayoutRun = POINTER(c_void_p)
_GFileInputStream = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_JSPropertyNameArray = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GtkAboutDialog = POINTER(c_void_p)
_WebKitViewportAttributes = POINTER(c_void_p)
_JSClass = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_cairo_t = POINTER(c_void_p)
_GWeakRef = POINTER(c_void_p)
_GdkPixbufAnimationIter = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_GdkEventButton = POINTER(c_void_p)
_GCancellable = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_GMount = POINTER(c_void_p)
_PangoRectangle = POINTER(c_void_p)
_GtkAccelGroup = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GFile = POINTER(c_void_p)
_JSContext = POINTER(c_void_p)
_GDrive = POINTER(c_void_p)
_PangoFontsetSimple = POINTER(c_void_p)
_GtkAllocation = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_PangoLayoutLine = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_GMutex = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GtkStatusbar = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitDOMDocument = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkPrintOperation = POINTER(c_void_p)
_GtkThemingEngine = POINTER(c_void_p)
_GString = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GFileInfo = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_GTimeVal = POINTER(c_void_p)
_GtkInvisible = POINTER(c_void_p)
_GSourceFuncs = POINTER(c_void_p)
_JSPropertyNameAccumulator = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_GFileIOStream = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_GtkStylePropertyParser = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_SoupMessage = POINTER(c_void_p)
_WebKitWebDataSource = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GdkPixbufAnimation = POINTER(c_void_p)
_GEmblem = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_gunichar = POINTER(c_void_p)
_GVolume = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GPollFD = POINTER(c_void_p)
_GFileOutputStream = POINTER(c_void_p)
_JSObject = POINTER(c_void_p)
_WebKitDOMNode = POINTER(c_void_p)
_GtkStyleProperties = POINTER(c_void_p)
_WebKitWebNavigationAction = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GParameter = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_GtkGradient = POINTER(c_void_p)
_cairo_pattern_t = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GMountOperation = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_JSPropertyNameArray = POINTER(c_void_p)
_GSourceCallbackFuncs = POINTER(c_void_p)
_PangoFontFace = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GByteArray = POINTER(c_void_p)
_GdkPixbufSimpleAnim = POINTER(c_void_p)
_JSObject = POINTER(c_void_p)
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
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkLicense = c_int
GtkIconSize = c_int

try:
    libgtk3.gtk_container_unset_focus_chain.restype = None
    libgtk3.gtk_container_unset_focus_chain.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_add_with_properties.restype = None
    libgtk3.gtk_container_add_with_properties.argtypes = [_GtkContainer,_GtkWidget,Asciifier,]
except:
   pass
try:
    libgtk3.gtk_container_child_notify.restype = None
    libgtk3.gtk_container_child_notify.argtypes = [_GtkContainer,_GtkWidget,Asciifier]
except:
   pass
try:
    libgtk3.gtk_container_propagate_draw.restype = None
    libgtk3.gtk_container_propagate_draw.argtypes = [_GtkContainer,_GtkWidget,_cairo_t]
except:
   pass
try:
    libgtk3.gtk_container_set_focus_hadjustment.restype = None
    libgtk3.gtk_container_set_focus_hadjustment.argtypes = [_GtkContainer,_GtkAdjustment]
except:
   pass
try:
    libgtk3.gtk_container_forall.restype = None
    libgtk3.gtk_container_forall.argtypes = [_GtkContainer,GtkCallback,gpointer]
except:
   pass
try:
    libgtk3.gtk_container_resize_children.restype = None
    libgtk3.gtk_container_resize_children.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_child_set_property.restype = None
    libgtk3.gtk_container_child_set_property.argtypes = [_GtkContainer,_GtkWidget,Asciifier,_GValue]
except:
   pass
try:
    libgtk3.gtk_container_set_resize_mode.restype = None
    libgtk3.gtk_container_set_resize_mode.argtypes = [_GtkContainer,GtkResizeMode]
except:
   pass
try:
    libgtk3.gtk_container_get_border_width.restype = guint
    libgtk3.gtk_container_get_border_width.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_set_border_width.restype = None
    libgtk3.gtk_container_set_border_width.argtypes = [_GtkContainer,guint]
except:
   pass
try:
    libgtk3.gtk_container_check_resize.restype = None
    libgtk3.gtk_container_check_resize.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_child_get_property.restype = None
    libgtk3.gtk_container_child_get_property.argtypes = [_GtkContainer,_GtkWidget,Asciifier,_GValue]
except:
   pass
try:
    libgtk3.gtk_container_set_focus_chain.restype = None
    libgtk3.gtk_container_set_focus_chain.argtypes = [_GtkContainer,_GList]
except:
   pass
try:
    libgtk3.gtk_container_class_handle_border_width.restype = None
    libgtk3.gtk_container_class_handle_border_width.argtypes = [_GtkContainer,_GtkContainerClass]
except:
   pass
try:
    libgtk3.gtk_container_get_focus_chain.restype = gboolean
    libgtk3.gtk_container_get_focus_chain.argtypes = [_GtkContainer,_GList]
except:
   pass
try:
    libgtk3.gtk_container_set_focus_child.restype = None
    libgtk3.gtk_container_set_focus_child.argtypes = [_GtkContainer,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_container_set_reallocate_redraws.restype = None
    libgtk3.gtk_container_set_reallocate_redraws.argtypes = [_GtkContainer,gboolean]
except:
   pass
try:
    libgtk3.gtk_container_child_get.restype = None
    libgtk3.gtk_container_child_get.argtypes = [_GtkContainer,_GtkWidget,Asciifier,]
except:
   pass
try:
    libgtk3.gtk_container_get_path_for_child.restype = _GtkWidgetPath
    libgtk3.gtk_container_get_path_for_child.argtypes = [_GtkContainer,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_container_foreach.restype = None
    libgtk3.gtk_container_foreach.argtypes = [_GtkContainer,GtkCallback,gpointer]
except:
   pass
try:
    libgtk3.gtk_container_class_install_child_property.restype = None
    libgtk3.gtk_container_class_install_child_property.argtypes = [_GtkContainer,_GtkContainerClass,guint,_GParamSpec]
except:
   pass
try:
    libgtk3.gtk_container_add.restype = None
    libgtk3.gtk_container_add.argtypes = [_GtkContainer,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_container_get_resize_mode.restype = GtkResizeMode
    libgtk3.gtk_container_get_resize_mode.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_get_focus_vadjustment.restype = _GtkAdjustment
    libgtk3.gtk_container_get_focus_vadjustment.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_set_focus_vadjustment.restype = None
    libgtk3.gtk_container_set_focus_vadjustment.argtypes = [_GtkContainer,_GtkAdjustment]
except:
   pass
try:
    libgtk3.gtk_container_child_type.restype = GType
    libgtk3.gtk_container_child_type.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_remove.restype = None
    libgtk3.gtk_container_remove.argtypes = [_GtkContainer,_GtkWidget]
except:
   pass
try:
    libgtk3.gtk_container_child_set.restype = None
    libgtk3.gtk_container_child_set.argtypes = [_GtkContainer,_GtkWidget,Asciifier,]
except:
   pass
try:
    libgtk3.gtk_container_get_focus_hadjustment.restype = _GtkAdjustment
    libgtk3.gtk_container_get_focus_hadjustment.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_get_children.restype = _GList
    libgtk3.gtk_container_get_children.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_get_focus_child.restype = _GtkWidget
    libgtk3.gtk_container_get_focus_child.argtypes = [_GtkContainer]
except:
   pass
try:
    libgtk3.gtk_container_class_list_child_properties.restype = _GParamSpec
    libgtk3.gtk_container_class_list_child_properties.argtypes = [_GObjectClass,POINTER(guint)]
except:
   pass
try:
    libgtk3.gtk_container_class_find_child_property.restype = _GParamSpec
    libgtk3.gtk_container_class_find_child_property.argtypes = [_GObjectClass,Asciifier]
except:
   pass
from . import gtk3__GtkWidget
class GtkContainer( gtk3__GtkWidget.GtkWidget):
    """Class GtkContainer Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def unset_focus_chain(  self, ):

        
        libgtk3.gtk_container_unset_focus_chain( self._object )

    def add_with_properties(  self, widget, first_prop_name,*args  ):
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()


        def callit( widget, first_prop_name, *args ):
                for arg in args:
                     libgtk3.gtk_container_add_with_properties.argtypes.append(args[1])
                return libgtk3.gtk_container_add_with_properties( widget, first_prop_name, *args)
    
        return callit( self._object, widget, first_prop_name,*args )

    def child_notify(  self, child, child_property, ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()

        
        libgtk3.gtk_container_child_notify( self._object,child,child_property )

    def propagate_draw(  self, child, cr, ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()
        if cr: cr = cr._object
        else: cr = POINTER(c_void_p)()

        
        libgtk3.gtk_container_propagate_draw( self._object,child,cr )

    def set_focus_hadjustment(  self, adjustment, ):
        if adjustment: adjustment = adjustment._object
        else: adjustment = POINTER(c_void_p)()

        
        libgtk3.gtk_container_set_focus_hadjustment( self._object,adjustment )

    def forall(  self, callback, callback_data, ):
        if callback: callback = callback._object
        else: callback = POINTER(c_void_p)()

        
        libgtk3.gtk_container_forall( self._object,callback,callback_data )

    def resize_children(  self, ):

        
        libgtk3.gtk_container_resize_children( self._object )

    def child_set_property(  self, child, property_name, value, ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgtk3.gtk_container_child_set_property( self._object,child,property_name,value )

    def set_resize_mode(  self, resize_mode, ):

        
        libgtk3.gtk_container_set_resize_mode( self._object,resize_mode )

    def get_border_width(  self, ):

        
        return libgtk3.gtk_container_get_border_width( self._object )

    def set_border_width(  self, border_width, ):

        
        libgtk3.gtk_container_set_border_width( self._object,border_width )

    def check_resize(  self, ):

        
        libgtk3.gtk_container_check_resize( self._object )

    def child_get_property(  self, child, property_name, value, ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgtk3.gtk_container_child_get_property( self._object,child,property_name,value )

    def set_focus_chain(  self, focusable_widgets, ):
        if focusable_widgets: focusable_widgets = focusable_widgets._object
        else: focusable_widgets = POINTER(c_void_p)()

        
        libgtk3.gtk_container_set_focus_chain( self._object,focusable_widgets )

    def class_handle_border_width(  self, klass, ):
        if klass: klass = klass._object
        else: klass = POINTER(c_void_p)()

        
        libgtk3.gtk_container_class_handle_border_width( self._object,klass )

    def get_focus_chain(  self, focusable_widgets, ):
        if focusable_widgets: focusable_widgets = focusable_widgets._object
        else: focusable_widgets = POINTER(c_void_p)()

        
        return libgtk3.gtk_container_get_focus_chain( self._object,focusable_widgets )

    def set_focus_child(  self, child, ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()

        
        libgtk3.gtk_container_set_focus_child( self._object,child )

    def set_reallocate_redraws(  self, needs_redraws, ):

        
        libgtk3.gtk_container_set_reallocate_redraws( self._object,needs_redraws )

    def child_get(  self, child, first_prop_name,*args  ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()


        def callit( child, first_prop_name, *args ):
                for arg in args:
                     libgtk3.gtk_container_child_get.argtypes.append(args[1])
                return libgtk3.gtk_container_child_get( child, first_prop_name, *args)
    
        return callit( self._object, child, first_prop_name,*args )

    def get_path_for_child(  self, child, ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()

        from .gtk3 import GtkWidgetPath
        return GtkWidgetPath(None, obj=libgtk3.gtk_container_get_path_for_child( self._object,child ) or POINTER(c_void_p)())

    def foreach(  self, callback, callback_data, ):
        if callback: callback = callback._object
        else: callback = POINTER(c_void_p)()

        
        libgtk3.gtk_container_foreach( self._object,callback,callback_data )

    def class_install_child_property(  self, cclass, property_id, pspec, ):
        if cclass: cclass = cclass._object
        else: cclass = POINTER(c_void_p)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_void_p)()

        
        libgtk3.gtk_container_class_install_child_property( self._object,cclass,property_id,pspec )

    def add(  self, widget, ):
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_container_add( self._object,widget )

    def get_resize_mode(  self, ):

        
        return libgtk3.gtk_container_get_resize_mode( self._object )

    def get_focus_vadjustment(  self, ):

        from .gtk3 import GtkAdjustment
        return GtkAdjustment(None,None, obj=libgtk3.gtk_container_get_focus_vadjustment( self._object ) or POINTER(c_void_p)())

    def set_focus_vadjustment(  self, adjustment, ):
        if adjustment: adjustment = adjustment._object
        else: adjustment = POINTER(c_void_p)()

        
        libgtk3.gtk_container_set_focus_vadjustment( self._object,adjustment )

    def child_type(  self, ):

        
        return libgtk3.gtk_container_child_type( self._object )

    def remove(  self, widget, ):
        if widget: widget = widget._object
        else: widget = POINTER(c_void_p)()

        
        libgtk3.gtk_container_remove( self._object,widget )

    def child_set(  self, child, first_prop_name,*args  ):
        if child: child = child._object
        else: child = POINTER(c_void_p)()


        def callit( child, first_prop_name, *args ):
                for arg in args:
                     libgtk3.gtk_container_child_set.argtypes.append(args[1])
                return libgtk3.gtk_container_child_set( child, first_prop_name, *args)
    
        return callit( self._object, child, first_prop_name,*args )

    def get_focus_hadjustment(  self, ):

        from .gtk3 import GtkAdjustment
        return GtkAdjustment(None, obj=libgtk3.gtk_container_get_focus_hadjustment( self._object ) or POINTER(c_void_p)())

    def get_children(  self, ):

        from .gobject import GList
        return GList( obj=libgtk3.gtk_container_get_children( self._object ) or POINTER(c_void_p)())

    def get_focus_child(  self, ):

        from .gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_container_get_focus_child( self._object ) or POINTER(c_void_p)())

    @staticmethod
    def class_list_child_properties( cclass, n_properties,):
        if cclass: cclass = cclass._object
        else: cclass = POINTER(c_void_p)()
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.gtk_container_class_list_child_properties(cclass, n_properties, )
 or POINTER(c_void_p)())
    @staticmethod
    def class_find_child_property( cclass, property_name,):
        if cclass: cclass = cclass._object
        else: cclass = POINTER(c_void_p)()
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.gtk_container_class_find_child_property(cclass, property_name, )
 or POINTER(c_void_p)())
