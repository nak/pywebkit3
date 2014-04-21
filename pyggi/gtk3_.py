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
from .gtk3_types import *
    
    
"""Derived Pointer Types"""
__GtkRcStyle = OPAQUE_PTR
__GdkGeometry = OPAQUE_PTR
_WebKitWebPolicyDecision = OPAQUE_PTR
_WebKitNetworkResponse = OPAQUE_PTR
_GdkPixbuf = OPAQUE_PTR
_GtkBin = OPAQUE_PTR
__GtkRequisition = OPAQUE_PTR
_GtkRcStyle = OPAQUE_PTR
_PangoEngineShape = OPAQUE_PTR
__GtkRegionFlags = OPAQUE_PTR
__WebKitDOMNode = OPAQUE_PTR
_GtkWindow = OPAQUE_PTR
__cairo_font_options_t = OPAQUE_PTR
__JSValue = OPAQUE_PTR
_JSContext = OPAQUE_PTR
_GtkIconFactory = OPAQUE_PTR
__GdkAtom = OPAQUE_PTR
_GMainLoop = OPAQUE_PTR
__GdkTimeCoord = OPAQUE_PTR
_GdkColor = OPAQUE_PTR
__GtkWidgetPath = OPAQUE_PTR
_GtkContainer = OPAQUE_PTR
_PangoItem = OPAQUE_PTR
__GClosure = OPAQUE_PTR
_GtkAboutDialog = OPAQUE_PTR
__GMainContext = OPAQUE_PTR
_GdkDisplay = OPAQUE_PTR
__GtkStyleProvider = OPAQUE_PTR
_GtkScrolledWindow = OPAQUE_PTR
_GtkDialog = OPAQUE_PTR
__WebKitWebWindowFeatures = OPAQUE_PTR
_JSObject = OPAQUE_PTR
_GBytes = OPAQUE_PTR
_GScanner = OPAQUE_PTR
_PangoFont = OPAQUE_PTR
_GtkStyleContext = OPAQUE_PTR
_GMainContext = OPAQUE_PTR
_GBoxed = OPAQUE_PTR
__GtkTextBuffer = OPAQUE_PTR
_GtkTargetList = OPAQUE_PTR
__WebKitWebSettings = OPAQUE_PTR
_GdkAppLaunchContext = OPAQUE_PTR
__GObject = OPAQUE_PTR
__PangoLayout = OPAQUE_PTR
_WebKitWebBackForwardList = OPAQUE_PTR
_GtkOffscreenWindow = OPAQUE_PTR
__GParamSpec = OPAQUE_PTR
__PangoAttrIterator = OPAQUE_PTR
_GtkRequisition = OPAQUE_PTR
_GtkIconSet = OPAQUE_PTR
_GtkSelectionData = OPAQUE_PTR
_GtkWindowGroup = OPAQUE_PTR
_GtkAdjustment = OPAQUE_PTR
_JSGlobalContext = OPAQUE_PTR
_GApplication = OPAQUE_PTR
_PangoLogAttr = OPAQUE_PTR
_GString = OPAQUE_PTR
__PangoContext = OPAQUE_PTR
__JSPropertyNameArray = OPAQUE_PTR
_WebKitWebSettings = OPAQUE_PTR
__PangoFont = OPAQUE_PTR
__GtkPathPriorityType = OPAQUE_PTR
__JSClass = OPAQUE_PTR
__WebKitWebHistoryItem = OPAQUE_PTR
_JSValue = OPAQUE_PTR
__GtkSettings = OPAQUE_PTR
_GSource = OPAQUE_PTR
__PangoFontMap = OPAQUE_PTR
__JSString = OPAQUE_PTR
__PangoAttrList = OPAQUE_PTR
_PangoMatrix = OPAQUE_PTR
__GSource = OPAQUE_PTR
_GtkApplication = OPAQUE_PTR
__PangoAnalysis = OPAQUE_PTR
__GMutex = OPAQUE_PTR
_PangoFontDescription = OPAQUE_PTR
_GdkGeometry = OPAQUE_PTR
__GdkCursor = OPAQUE_PTR
_GtkBorder = OPAQUE_PTR
_WebKitWebInspector = OPAQUE_PTR
_GdkWindowAttr = OPAQUE_PTR
_GOptionGroup = OPAQUE_PTR
__GScanner = OPAQUE_PTR
__GtkWidgetClass = OPAQUE_PTR
__GtkContainerClass = OPAQUE_PTR
__GdkEventKey = OPAQUE_PTR
__GtkAdjustment = OPAQUE_PTR
_GdkDragContext = OPAQUE_PTR
_GtkAssistant = OPAQUE_PTR
__GdkDisplay = OPAQUE_PTR
_GtkWidgetPath = OPAQUE_PTR
_GdkScreen = OPAQUE_PTR
_PangoFontMetrics = OPAQUE_PTR
__GCond = OPAQUE_PTR
_GtkIconSource = OPAQUE_PTR
__cairo_surface_t = OPAQUE_PTR
_GdkVisual = OPAQUE_PTR
_PangoFontMap = OPAQUE_PTR
_GSList = OPAQUE_PTR
_WebKitWebFrame = OPAQUE_PTR
_JSString = OPAQUE_PTR
__GActionGroup = OPAQUE_PTR
_GtkWidget = OPAQUE_PTR
__WebKitNetworkRequest = OPAQUE_PTR
__GdkWindow = OPAQUE_PTR
__PangoFontFamily = OPAQUE_PTR
__JSContextGroup = OPAQUE_PTR
__GPollFD = OPAQUE_PTR
__cairo_region_t = OPAQUE_PTR
_PangoFontset = OPAQUE_PTR
_GdkWindow = OPAQUE_PTR
__PangoFontDescription = OPAQUE_PTR
__GtkBorder = OPAQUE_PTR
__GError = OPAQUE_PTR
__PangoCoverage = OPAQUE_PTR
_WebKitViewportAttributes = OPAQUE_PTR
_JSClass = OPAQUE_PTR
_WebKitWebHistoryItem = OPAQUE_PTR
_PangoFontFamily = OPAQUE_PTR
__cairo_t = OPAQUE_PTR
__GWeakRef = OPAQUE_PTR
__GdkVisual = OPAQUE_PTR
__GdkEventButton = OPAQUE_PTR
__GCancellable = OPAQUE_PTR
_GdkDevice = OPAQUE_PTR
__PangoRectangle = OPAQUE_PTR
__GtkAccelGroup = OPAQUE_PTR
_GObject = OPAQUE_PTR
_GPollFD = OPAQUE_PTR
__GtkIconSource = OPAQUE_PTR
__GFile = OPAQUE_PTR
__JSContext = OPAQUE_PTR
_PangoFontsetSimple = OPAQUE_PTR
__GtkAllocation = OPAQUE_PTR
__GtkWidget = OPAQUE_PTR
_PangoLayoutLine = OPAQUE_PTR
__GtkIconSet = OPAQUE_PTR
_WebKitWebView = OPAQUE_PTR
__PangoTabArray = OPAQUE_PTR
_WebKitHitTestResult = OPAQUE_PTR
__GValue = OPAQUE_PTR
_GdkDeviceManager = OPAQUE_PTR
_GdkCursor = OPAQUE_PTR
_WebKitDOMDocument = OPAQUE_PTR
__PangoMatrix = OPAQUE_PTR
__GtkPrintOperation = OPAQUE_PTR
__GString = OPAQUE_PTR
_PangoContext = OPAQUE_PTR
__GtkTargetList = OPAQUE_PTR
__GList = OPAQUE_PTR
__WebKitWebView = OPAQUE_PTR
_WebKitWebWindowFeatures = OPAQUE_PTR
_PangoCoverage = OPAQUE_PTR
_GParamSpec = OPAQUE_PTR
_GList = OPAQUE_PTR
__GdkRGBA = OPAQUE_PTR
__GTimeVal = OPAQUE_PTR
_GtkInvisible = OPAQUE_PTR
__GSourceFuncs = OPAQUE_PTR
__JSPropertyNameAccumulator = OPAQUE_PTR
__PangoGlyphString = OPAQUE_PTR
__JSGlobalContext = OPAQUE_PTR
_WebKitSecurityOrigin = OPAQUE_PTR
__GObjectClass = OPAQUE_PTR
__GSList = OPAQUE_PTR
_PangoAnalysis = OPAQUE_PTR
__GdkWindowAttr = OPAQUE_PTR
_SoupMessage = OPAQUE_PTR
_WebKitWebDataSource = OPAQUE_PTR
_GdkAtom = OPAQUE_PTR
__GdkColor = OPAQUE_PTR
_JSContextGroup = OPAQUE_PTR
__GdkRectangle = OPAQUE_PTR
__PangoLanguage = OPAQUE_PTR
_PangoAttrList = OPAQUE_PTR
__gunichar = OPAQUE_PTR
__GdkWMDecoration = OPAQUE_PTR
__PangoLogAttr = OPAQUE_PTR
_PangoLayout = OPAQUE_PTR
_JSPropertyNameArray = OPAQUE_PTR
__JSObject = OPAQUE_PTR
__GdkDragContext = OPAQUE_PTR
_WebKitWebNavigationAction = OPAQUE_PTR
_GtkStyle = OPAQUE_PTR
__GParameter = OPAQUE_PTR
__GtkStyle = OPAQUE_PTR
__GIcon = OPAQUE_PTR
__GtkWindow = OPAQUE_PTR
_PangoLayoutRun = OPAQUE_PTR
__cairo_pattern_t = OPAQUE_PTR
__GdkPixbuf = OPAQUE_PTR
_WebKitGeolocationPolicyDecision = OPAQUE_PTR
_GtkSettings = OPAQUE_PTR
__GSourceCallbackFuncs = OPAQUE_PTR
__PangoFontFace = OPAQUE_PTR
__GtkTargetEntry = OPAQUE_PTR
__GtkApplication = OPAQUE_PTR
_GtkClipboard = OPAQUE_PTR
_GByteArray = OPAQUE_PTR
__GdkScreen = OPAQUE_PTR
_PangoLanguage = OPAQUE_PTR
__GdkDevice = OPAQUE_PTR
_PangoTabArray = OPAQUE_PTR
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
GtkAssistantPageType = c_int
GApplicationFlags = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
GtkDestDefaults = c_int
GtkTargetFlags = c_int

def gtkkeysnooperinstall( snooper, func_data,):
    if snooper: snooper = snooper._object
    else: snooper = OPAQUE_PTR()
    libgtk3.gtk_key_snooper_install.restype = guint
    libgtk3.gtk_key_snooper_install.argtypes = [GtkKeySnoopFunc,gpointer]
    
    return     libgtk3.gtk_key_snooper_install(snooper, func_data, )

def gtkgetoptiongroup( open_default_display,):
    libgtk3.gtk_get_option_group.restype = _GOptionGroup
    libgtk3.gtk_get_option_group.argtypes = [gboolean]
    from pyggi.gobject import GOptionGroup
    return GOptionGroup( obj=    libgtk3.gtk_get_option_group(open_default_display, )
 or OPAQUE_PTR())
def gtkdragdestfindtarget( widget, context, target_list,):
    if widget: widget = widget._object
    else: widget = OPAQUE_PTR()
    if context: context = context._object
    else: context = OPAQUE_PTR()
    if target_list: target_list = target_list._object
    else: target_list = OPAQUE_PTR()
    libgtk3.gtk_drag_dest_find_target.restype = GdkAtom
    libgtk3.gtk_drag_dest_find_target.argtypes = [_GtkWidget,_GdkDragContext,_GtkTargetList]
    
    return     libgtk3.gtk_drag_dest_find_target(widget, context, target_list, )

def gtkmainiterationdo( blocking,):
    libgtk3.gtk_main_iteration_do.restype = gboolean
    libgtk3.gtk_main_iteration_do.argtypes = [gboolean]
    
    return     libgtk3.gtk_main_iteration_do(blocking, )

def gtkdragdestgettrackmotion( widget,):
    if widget: widget = widget._object
    else: widget = OPAQUE_PTR()
    libgtk3.gtk_drag_dest_get_track_motion.restype = gboolean
    libgtk3.gtk_drag_dest_get_track_motion.argtypes = [_GtkWidget]
    
    return     libgtk3.gtk_drag_dest_get_track_motion(widget, )

def gtkgeteventwidget( event,):
    libgtk3.gtk_get_event_widget.restype = _GtkWidget
    libgtk3.gtk_get_event_widget.argtypes = [POINTER(GdkEvent)]
    from pyggi.gtk3 import GtkWidget
    return GtkWidget(None, obj=    libgtk3.gtk_get_event_widget(event, )
 or OPAQUE_PTR())
def gtkgetcurrenteventstate( state,):
    libgtk3.gtk_get_current_event_state.restype = gboolean
    libgtk3.gtk_get_current_event_state.argtypes = [POINTER(GdkModifierType)]
    
    return     libgtk3.gtk_get_current_event_state(state, )

def gtkdraggetsourcewidget( context,):
    if context: context = context._object
    else: context = OPAQUE_PTR()
    libgtk3.gtk_drag_get_source_widget.restype = _GtkWidget
    libgtk3.gtk_drag_get_source_widget.argtypes = [_GdkDragContext]
    from pyggi.gtk3 import GtkWidget
    return GtkWidget( obj=    libgtk3.gtk_drag_get_source_widget(context, )
 or OPAQUE_PTR())
def gtkdragsourcegettargetlist( widget,):
    if widget: widget = widget._object
    else: widget = OPAQUE_PTR()
    libgtk3.gtk_drag_source_get_target_list.restype = _GtkTargetList
    libgtk3.gtk_drag_source_get_target_list.argtypes = [_GtkWidget]
    from pyggi.gtk3 import GtkTargetList
    return GtkTargetList( obj=    libgtk3.gtk_drag_source_get_target_list(widget, )
 or OPAQUE_PTR())
def gtkdragdestgettargetlist( widget,):
    if widget: widget = widget._object
    else: widget = OPAQUE_PTR()
    libgtk3.gtk_drag_dest_get_target_list.restype = _GtkTargetList
    libgtk3.gtk_drag_dest_get_target_list.argtypes = [_GtkWidget]
    from pyggi.gtk3 import GtkTargetList
    return GtkTargetList( obj=    libgtk3.gtk_drag_dest_get_target_list(widget, )
 or OPAQUE_PTR())
def gtkdragcheckthreshold( widget, start_x, start_y, current_x, current_y,):
    if widget: widget = widget._object
    else: widget = OPAQUE_PTR()
    libgtk3.gtk_drag_check_threshold.restype = gboolean
    libgtk3.gtk_drag_check_threshold.argtypes = [_GtkWidget,gint,gint,gint,gint]
    
    return     libgtk3.gtk_drag_check_threshold(widget, start_x, start_y, current_x, current_y, )

def gtkdragbegin( widget, targets, actions, button, event,):
    if widget: widget = widget._object
    else: widget = OPAQUE_PTR()
    if targets: targets = targets._object
    else: targets = OPAQUE_PTR()
    if actions: actions = actions._object
    else: actions = OPAQUE_PTR()
    libgtk3.gtk_drag_begin.restype = _GdkDragContext
    libgtk3.gtk_drag_begin.argtypes = [_GtkWidget,_GtkTargetList,GdkDragAction,gint,POINTER(GdkEvent)]
    from pyggi.gobject import GdkDragContext
    return GdkDragContext( obj=    libgtk3.gtk_drag_begin(widget, targets, actions, button, event, )
 or OPAQUE_PTR())
