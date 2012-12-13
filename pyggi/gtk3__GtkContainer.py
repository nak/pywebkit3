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
__GtkRcStyle = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
_GtkContainer = POINTER(c_int)
_PangoItem = POINTER(c_int)
__GClosure = POINTER(c_int)
_GtkAboutDialog = POINTER(c_int)
__GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GBoxed = POINTER(c_int)
__GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
__GObject = POINTER(c_int)
__PangoLayout = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
__GParamSpec = POINTER(c_int)
__PangoAttrIterator = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAdjustment = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GString = POINTER(c_int)
__PangoContext = POINTER(c_int)
__JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__PangoFont = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__JSClass = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
__GtkSettings = POINTER(c_int)
_GSource = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
__GSource = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
__GMutex = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GtkContainerClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GtkAdjustment = POINTER(c_int)
_GdkDragContext = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
__GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__PangoFontFamily = POINTER(c_int)
__JSContextGroup = POINTER(c_int)
__GPollFD = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GtkBorder = POINTER(c_int)
__GError = POINTER(c_int)
__PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__JSContext = POINTER(c_int)
_PangoFontsetSimple = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
__GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
__PangoTabArray = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
__GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
__PangoMatrix = POINTER(c_int)
__GtkPrintOperation = POINTER(c_int)
__GString = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GList = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__GTimeVal = POINTER(c_int)
_GtkInvisible = POINTER(c_int)
__GSourceFuncs = POINTER(c_int)
__JSPropertyNameAccumulator = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
__GdkColor = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
__gunichar = POINTER(c_int)
__GdkWMDecoration = POINTER(c_int)
__PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
__JSObject = POINTER(c_int)
_WebKitWebNavigationAction = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GIcon = POINTER(c_int)
__GtkWindow = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
__GSourceCallbackFuncs = POINTER(c_int)
__PangoFontFace = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GByteArray = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
__GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
"""Enumerations"""
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkIconSize = c_int
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
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GdkCursorType = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
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
GtkDialogFlags = c_int
GtkResponseType = c_int
WebKitWebNavigationReason = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkLicense = c_int
GtkIconSize = c_int

import gtk3__GtkWidget
class GtkContainer( gtk3__GtkWidget.GtkWidget):
    """Class GtkContainer Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def unset_focus_chain(  self, ):

        libgtk3.gtk_container_unset_focus_chain.argtypes = [_GtkContainer]
        
        libgtk3.gtk_container_unset_focus_chain( self._object )

    def add_with_properties(  self, widget, first_prop_name,*args  ):
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()


        def callit( widget, first_prop_name, *args ):
                libgtk3.gtk_container_add_with_properties.restype = None
                libgtk3.gtk_container_add_with_properties.argtypes = [ POINTER(c_int), _GtkWidget, c_char_p]
                for arg in args:
                     libgtk3.gtk_container_add_with_properties.argtypes.append(args[1])
                return libgtk3.gtk_container_add_with_properties( widget, first_prop_name, *args)
    
        return callit( self._object, widget, first_prop_name,*args )

    def child_notify(  self, child, child_property, ):
        if child: child = child._object
        else: child = POINTER(c_int)()

        libgtk3.gtk_container_child_notify.argtypes = [_GtkContainer,_GtkWidget,c_char_p]
        
        libgtk3.gtk_container_child_notify( self._object,child,child_property )

    def propagate_draw(  self, child, cr, ):
        if child: child = child._object
        else: child = POINTER(c_int)()
        if cr: cr = cr._object
        else: cr = POINTER(c_int)()

        libgtk3.gtk_container_propagate_draw.argtypes = [_GtkContainer,_GtkWidget,_cairo_t]
        
        libgtk3.gtk_container_propagate_draw( self._object,child,cr )

    def set_focus_hadjustment(  self, adjustment, ):
        if adjustment: adjustment = adjustment._object
        else: adjustment = POINTER(c_int)()

        libgtk3.gtk_container_set_focus_hadjustment.argtypes = [_GtkContainer,_GtkAdjustment]
        
        libgtk3.gtk_container_set_focus_hadjustment( self._object,adjustment )

    def forall(  self, callback, callback_data, ):
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        libgtk3.gtk_container_forall.argtypes = [_GtkContainer,GtkCallback,gpointer]
        
        libgtk3.gtk_container_forall( self._object,callback,callback_data )

    def resize_children(  self, ):

        libgtk3.gtk_container_resize_children.argtypes = [_GtkContainer]
        
        libgtk3.gtk_container_resize_children( self._object )

    def child_set_property(  self, child, property_name, value, ):
        if child: child = child._object
        else: child = POINTER(c_int)()
        if value: value = value._object
        else: value = POINTER(c_int)()

        libgtk3.gtk_container_child_set_property.argtypes = [_GtkContainer,_GtkWidget,c_char_p,_GValue]
        
        libgtk3.gtk_container_child_set_property( self._object,child,property_name,value )

    def set_resize_mode(  self, resize_mode, ):

        libgtk3.gtk_container_set_resize_mode.argtypes = [_GtkContainer,GtkResizeMode]
        
        libgtk3.gtk_container_set_resize_mode( self._object,resize_mode )

    def get_border_width(  self, ):

        libgtk3.gtk_container_get_border_width.restype = guint
        libgtk3.gtk_container_get_border_width.argtypes = [_GtkContainer]
        
        return libgtk3.gtk_container_get_border_width( self._object )

    def set_border_width(  self, border_width, ):

        libgtk3.gtk_container_set_border_width.argtypes = [_GtkContainer,guint]
        
        libgtk3.gtk_container_set_border_width( self._object,border_width )

    def check_resize(  self, ):

        libgtk3.gtk_container_check_resize.argtypes = [_GtkContainer]
        
        libgtk3.gtk_container_check_resize( self._object )

    def child_get_property(  self, child, property_name, value, ):
        if child: child = child._object
        else: child = POINTER(c_int)()
        if value: value = value._object
        else: value = POINTER(c_int)()

        libgtk3.gtk_container_child_get_property.argtypes = [_GtkContainer,_GtkWidget,c_char_p,_GValue]
        
        libgtk3.gtk_container_child_get_property( self._object,child,property_name,value )

    def set_focus_chain(  self, focusable_widgets, ):
        if focusable_widgets: focusable_widgets = focusable_widgets._object
        else: focusable_widgets = POINTER(c_int)()

        libgtk3.gtk_container_set_focus_chain.argtypes = [_GtkContainer,_GList]
        
        libgtk3.gtk_container_set_focus_chain( self._object,focusable_widgets )

    def class_handle_border_width(  self, klass, ):
        if klass: klass = klass._object
        else: klass = POINTER(c_int)()

        libgtk3.gtk_container_class_handle_border_width.argtypes = [_GtkContainer,_GtkContainerClass]
        
        libgtk3.gtk_container_class_handle_border_width( self._object,klass )

    def get_focus_chain(  self, focusable_widgets, ):
        if focusable_widgets: focusable_widgets = focusable_widgets._object
        else: focusable_widgets = POINTER(c_int)()

        libgtk3.gtk_container_get_focus_chain.restype = gboolean
        libgtk3.gtk_container_get_focus_chain.argtypes = [_GtkContainer,_GList]
        
        return libgtk3.gtk_container_get_focus_chain( self._object,focusable_widgets )

    def set_focus_child(  self, child, ):
        if child: child = child._object
        else: child = POINTER(c_int)()

        libgtk3.gtk_container_set_focus_child.argtypes = [_GtkContainer,_GtkWidget]
        
        libgtk3.gtk_container_set_focus_child( self._object,child )

    def set_reallocate_redraws(  self, needs_redraws, ):

        libgtk3.gtk_container_set_reallocate_redraws.argtypes = [_GtkContainer,gboolean]
        
        libgtk3.gtk_container_set_reallocate_redraws( self._object,needs_redraws )

    def child_get(  self, child, first_prop_name,*args  ):
        if child: child = child._object
        else: child = POINTER(c_int)()


        def callit( child, first_prop_name, *args ):
                libgtk3.gtk_container_child_get.restype = None
                libgtk3.gtk_container_child_get.argtypes = [ POINTER(c_int), _GtkWidget, c_char_p]
                for arg in args:
                     libgtk3.gtk_container_child_get.argtypes.append(args[1])
                return libgtk3.gtk_container_child_get( child, first_prop_name, *args)
    
        return callit( self._object, child, first_prop_name,*args )

    def get_path_for_child(  self, child, ):
        if child: child = child._object
        else: child = POINTER(c_int)()

        libgtk3.gtk_container_get_path_for_child.restype = _GtkWidgetPath
        libgtk3.gtk_container_get_path_for_child.argtypes = [_GtkContainer,_GtkWidget]
        from gtk3 import GtkWidgetPath
        return GtkWidgetPath(None, obj=libgtk3.gtk_container_get_path_for_child( self._object,child ) or POINTER(c_int)())

    def foreach(  self, callback, callback_data, ):
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        libgtk3.gtk_container_foreach.argtypes = [_GtkContainer,GtkCallback,gpointer]
        
        libgtk3.gtk_container_foreach( self._object,callback,callback_data )

    def class_install_child_property(  self, cclass, property_id, pspec, ):
        if cclass: cclass = cclass._object
        else: cclass = POINTER(c_int)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        libgtk3.gtk_container_class_install_child_property.argtypes = [_GtkContainer,_GtkContainerClass,guint,_GParamSpec]
        
        libgtk3.gtk_container_class_install_child_property( self._object,cclass,property_id,pspec )

    def add(  self, widget, ):
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        libgtk3.gtk_container_add.argtypes = [_GtkContainer,_GtkWidget]
        
        libgtk3.gtk_container_add( self._object,widget )

    def get_resize_mode(  self, ):

        libgtk3.gtk_container_get_resize_mode.restype = GtkResizeMode
        libgtk3.gtk_container_get_resize_mode.argtypes = [_GtkContainer]
        
        return libgtk3.gtk_container_get_resize_mode( self._object )

    def get_focus_vadjustment(  self, ):

        libgtk3.gtk_container_get_focus_vadjustment.restype = _GtkAdjustment
        libgtk3.gtk_container_get_focus_vadjustment.argtypes = [_GtkContainer]
        from gtk3 import GtkAdjustment
        return GtkAdjustment(None,None, obj=libgtk3.gtk_container_get_focus_vadjustment( self._object ) or POINTER(c_int)())

    def set_focus_vadjustment(  self, adjustment, ):
        if adjustment: adjustment = adjustment._object
        else: adjustment = POINTER(c_int)()

        libgtk3.gtk_container_set_focus_vadjustment.argtypes = [_GtkContainer,_GtkAdjustment]
        
        libgtk3.gtk_container_set_focus_vadjustment( self._object,adjustment )

    def child_type(  self, ):

        libgtk3.gtk_container_child_type.restype = GType
        libgtk3.gtk_container_child_type.argtypes = [_GtkContainer]
        
        return libgtk3.gtk_container_child_type( self._object )

    def remove(  self, widget, ):
        if widget: widget = widget._object
        else: widget = POINTER(c_int)()

        libgtk3.gtk_container_remove.argtypes = [_GtkContainer,_GtkWidget]
        
        libgtk3.gtk_container_remove( self._object,widget )

    def child_set(  self, child, first_prop_name,*args  ):
        if child: child = child._object
        else: child = POINTER(c_int)()


        def callit( child, first_prop_name, *args ):
                libgtk3.gtk_container_child_set.restype = None
                libgtk3.gtk_container_child_set.argtypes = [ POINTER(c_int), _GtkWidget, c_char_p]
                for arg in args:
                     libgtk3.gtk_container_child_set.argtypes.append(args[1])
                return libgtk3.gtk_container_child_set( child, first_prop_name, *args)
    
        return callit( self._object, child, first_prop_name,*args )

    def get_focus_hadjustment(  self, ):

        libgtk3.gtk_container_get_focus_hadjustment.restype = _GtkAdjustment
        libgtk3.gtk_container_get_focus_hadjustment.argtypes = [_GtkContainer]
        from gtk3 import GtkAdjustment
        return GtkAdjustment(None, obj=libgtk3.gtk_container_get_focus_hadjustment( self._object ) or POINTER(c_int)())

    def get_children(  self, ):

        libgtk3.gtk_container_get_children.restype = _GList
        libgtk3.gtk_container_get_children.argtypes = [_GtkContainer]
        from gobject import GList
        return GList( obj=libgtk3.gtk_container_get_children( self._object ) or POINTER(c_int)())

    def get_focus_child(  self, ):

        libgtk3.gtk_container_get_focus_child.restype = _GtkWidget
        libgtk3.gtk_container_get_focus_child.argtypes = [_GtkContainer]
        from gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_container_get_focus_child( self._object ) or POINTER(c_int)())

    @staticmethod
    def class_list_child_properties( cclass, n_properties,):
        if cclass: cclass = cclass._object
        else: cclass = POINTER(c_int)()
        libgtk3.gtk_container_class_list_child_properties.restype = _GParamSpec
        libgtk3.gtk_container_class_list_child_properties.argtypes = [_GObjectClass,POINTER(guint)]
        from gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.gtk_container_class_list_child_properties(cclass, n_properties, )
 or POINTER(c_int)())
    @staticmethod
    def class_find_child_property( cclass, property_name,):
        if cclass: cclass = cclass._object
        else: cclass = POINTER(c_int)()
        libgtk3.gtk_container_class_find_child_property.restype = _GParamSpec
        libgtk3.gtk_container_class_find_child_property.argtypes = [_GObjectClass,c_char_p]
        from gobject import GParamSpec
        return GParamSpec( obj=    libgtk3.gtk_container_class_find_child_property(cclass, property_name, )
 or POINTER(c_int)())
