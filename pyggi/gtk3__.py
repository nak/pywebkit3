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
_WebKitWebPolicyDecision = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkBin = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_PangoEngineShape = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
_GMainLoop = POINTER(c_int)
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
_GtkScrolledWindow = POINTER(c_int)
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
_GApplication = POINTER(c_int)
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
_GdkGeometry = POINTER(c_int)
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
_GtkAssistant = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
__GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
__cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
__GActionGroup = POINTER(c_int)
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
__GCancellable = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GPollFD = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__GFile = POINTER(c_int)
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
__GtkTargetList = POINTER(c_int)
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
_GdkAtom = POINTER(c_int)
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
__GdkDragContext = POINTER(c_int)
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
GtkAssistantPageType = c_int
GApplicationFlags = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
GtkDestDefaults = c_int
GtkTargetFlags = c_int

def gtkkeysnooperinstall( snooper, func_data,):
    if snooper: snooper = snooper._object
    else: snooper = POINTER(c_int)()
    libgtk3.gtk_key_snooper_install.restype = guint
    libgtk3.gtk_key_snooper_install.argtypes = [GtkKeySnoopFunc,gpointer]
    
    return     libgtk3.gtk_key_snooper_install(snooper, func_data, )

def gtkgetoptiongroup( open_default_display,):
    libgtk3.gtk_get_option_group.restype = _GOptionGroup
    libgtk3.gtk_get_option_group.argtypes = [gboolean]
    from gobject import GOptionGroup
    return GOptionGroup( obj=    libgtk3.gtk_get_option_group(open_default_display, )
 or POINTER(c_int)())
def gtkdragdestfindtarget( widget, context, target_list,):
    if widget: widget = widget._object
    else: widget = POINTER(c_int)()
    if context: context = context._object
    else: context = POINTER(c_int)()
    if target_list: target_list = target_list._object
    else: target_list = POINTER(c_int)()
    libgtk3.gtk_drag_dest_find_target.restype = GdkAtom
    libgtk3.gtk_drag_dest_find_target.argtypes = [_GtkWidget,_GdkDragContext,_GtkTargetList]
    
    return     libgtk3.gtk_drag_dest_find_target(widget, context, target_list, )

def gtkmainiterationdo( blocking,):
    libgtk3.gtk_main_iteration_do.restype = gboolean
    libgtk3.gtk_main_iteration_do.argtypes = [gboolean]
    
    return     libgtk3.gtk_main_iteration_do(blocking, )

def gtkdragdestgettrackmotion( widget,):
    if widget: widget = widget._object
    else: widget = POINTER(c_int)()
    libgtk3.gtk_drag_dest_get_track_motion.restype = gboolean
    libgtk3.gtk_drag_dest_get_track_motion.argtypes = [_GtkWidget]
    
    return     libgtk3.gtk_drag_dest_get_track_motion(widget, )

def gtkgeteventwidget( event,):
    libgtk3.gtk_get_event_widget.restype = _GtkWidget
    libgtk3.gtk_get_event_widget.argtypes = [POINTER(GdkEvent)]
    from gtk3 import GtkWidget
    return GtkWidget(None, obj=    libgtk3.gtk_get_event_widget(event, )
 or POINTER(c_int)())
def gtkgetcurrenteventstate( state,):
    libgtk3.gtk_get_current_event_state.restype = gboolean
    libgtk3.gtk_get_current_event_state.argtypes = [POINTER(GdkModifierType)]
    
    return     libgtk3.gtk_get_current_event_state(state, )

def gtkdraggetsourcewidget( context,):
    if context: context = context._object
    else: context = POINTER(c_int)()
    libgtk3.gtk_drag_get_source_widget.restype = _GtkWidget
    libgtk3.gtk_drag_get_source_widget.argtypes = [_GdkDragContext]
    from gtk3 import GtkWidget
    return GtkWidget( obj=    libgtk3.gtk_drag_get_source_widget(context, )
 or POINTER(c_int)())
def gtkdragsourcegettargetlist( widget,):
    if widget: widget = widget._object
    else: widget = POINTER(c_int)()
    libgtk3.gtk_drag_source_get_target_list.restype = _GtkTargetList
    libgtk3.gtk_drag_source_get_target_list.argtypes = [_GtkWidget]
    from gtk3 import GtkTargetList
    return GtkTargetList( obj=    libgtk3.gtk_drag_source_get_target_list(widget, )
 or POINTER(c_int)())
def gtkdragdestgettargetlist( widget,):
    if widget: widget = widget._object
    else: widget = POINTER(c_int)()
    libgtk3.gtk_drag_dest_get_target_list.restype = _GtkTargetList
    libgtk3.gtk_drag_dest_get_target_list.argtypes = [_GtkWidget]
    from gtk3 import GtkTargetList
    return GtkTargetList( obj=    libgtk3.gtk_drag_dest_get_target_list(widget, )
 or POINTER(c_int)())
def gtkdragcheckthreshold( widget, start_x, start_y, current_x, current_y,):
    if widget: widget = widget._object
    else: widget = POINTER(c_int)()
    libgtk3.gtk_drag_check_threshold.restype = gboolean
    libgtk3.gtk_drag_check_threshold.argtypes = [_GtkWidget,gint,gint,gint,gint]
    
    return     libgtk3.gtk_drag_check_threshold(widget, start_x, start_y, current_x, current_y, )

def gtkdragbegin( widget, targets, actions, button, event,):
    if widget: widget = widget._object
    else: widget = POINTER(c_int)()
    if targets: targets = targets._object
    else: targets = POINTER(c_int)()
    if actions: actions = actions._object
    else: actions = POINTER(c_int)()
    libgtk3.gtk_drag_begin.restype = _GdkDragContext
    libgtk3.gtk_drag_begin.argtypes = [_GtkWidget,_GtkTargetList,GdkDragAction,gint,POINTER(GdkEvent)]
    from gobject import GdkDragContext
    return GdkDragContext( obj=    libgtk3.gtk_drag_begin(widget, targets, actions, button, event, )
 or POINTER(c_int)())
