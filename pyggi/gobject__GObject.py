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
from .gobject_types import *
from .gobject_enums import *

    
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
_GtkIconFactory = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GdkTimeCoord = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
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
_WebKitWebHistoryItem = POINTER(c_void_p)
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
_GdkEventKey = POINTER(c_void_p)
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
_WebKitViewportAttributes = POINTER(c_void_p)
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
_GSourceCallbackFuncs = POINTER(c_void_p)
_PangoFontFace = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GByteArray = POINTER(c_void_p)
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

try:
    libgobject.g_object_disconnect.restype = None
    libgobject.g_object_disconnect.argtypes = [_GObject,Asciifier]
except:
   pass
try:
    libgobject.g_object_set_qdata_full.restype = None
    libgobject.g_object_set_qdata_full.argtypes = [_GObject,GQuark,gpointer,GDestroyNotify]
except:
   pass
try:
    libgobject.g_object_weak_unref.restype = None
    libgobject.g_object_weak_unref.argtypes = [_GObject,GWeakNotify,gpointer]
except:
   pass
try:
    libgobject.g_object_steal_data.restype = gpointer
    libgobject.g_object_steal_data.argtypes = [_GObject,Asciifier]
except:
   pass
try:
    libgobject.g_object_run_dispose.restype = None
    libgobject.g_object_run_dispose.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_set_qdata.restype = None
    libgobject.g_object_set_qdata.argtypes = [_GObject,GQuark,gpointer]
except:
   pass
try:
    libgobject.g_clear_object.restype = None
    libgobject.g_clear_object.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_set_data.restype = None
    libgobject.g_object_set_data.argtypes = [_GObject,Asciifier,gpointer]
except:
   pass
try:
    libgobject.g_object_ref_sink.restype = gpointer
    libgobject.g_object_ref_sink.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_connect.restype = gpointer
    libgobject.g_object_connect.argtypes = [_GObject,Asciifier,]
except:
   pass
try:
    libgobject.g_object_notify.restype = None
    libgobject.g_object_notify.argtypes = [_GObject,Asciifier]
except:
   pass
try:
    libgobject.g_object_class_install_properties.restype = None
    libgobject.g_object_class_install_properties.argtypes = [_GObject,_GObjectClass,guint,_GParamSpec]
except:
   pass
try:
    libgobject.g_object_replace_data.restype = gboolean
    libgobject.g_object_replace_data.argtypes = [_GObject,Asciifier,gpointer,gpointer,GDestroyNotify,POINTER(GDestroyNotify)]
except:
   pass
try:
    libgobject.g_object_interface_install_property.restype = None
    libgobject.g_object_interface_install_property.argtypes = [_GObject,gpointer,_GParamSpec]
except:
   pass
try:
    libgobject.g_object_get_qdata.restype = gpointer
    libgobject.g_object_get_qdata.argtypes = [_GObject,GQuark]
except:
   pass
try:
    libgobject.g_object_set_property.restype = None
    libgobject.g_object_set_property.argtypes = [_GObject,Asciifier,_GValue]
except:
   pass
try:
    libgobject.g_object_set.restype = None
    libgobject.g_object_set.argtypes = [_GObject,Asciifier,]
except:
   pass
try:
    libgobject.g_object_ref.restype = gpointer
    libgobject.g_object_ref.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_steal_qdata.restype = gpointer
    libgobject.g_object_steal_qdata.argtypes = [_GObject,GQuark]
except:
   pass
try:
    libgobject.g_object_add_toggle_ref.restype = None
    libgobject.g_object_add_toggle_ref.argtypes = [_GObject,GToggleNotify,gpointer]
except:
   pass
try:
    libgobject.g_object_weak_ref.restype = None
    libgobject.g_object_weak_ref.argtypes = [_GObject,GWeakNotify,gpointer]
except:
   pass
try:
    libgobject.g_object_add_weak_pointer.restype = None
    libgobject.g_object_add_weak_pointer.argtypes = [_GObject,POINTER(gpointer)]
except:
   pass
try:
    libgobject.g_object_remove_weak_pointer.restype = None
    libgobject.g_object_remove_weak_pointer.argtypes = [_GObject,POINTER(gpointer)]
except:
   pass
try:
    libgobject.g_object_class_install_property.restype = None
    libgobject.g_object_class_install_property.argtypes = [_GObject,_GObjectClass,guint,_GParamSpec]
except:
   pass
try:
    libgobject.g_object_freeze_notify.restype = None
    libgobject.g_object_freeze_notify.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_notify_by_pspec.restype = None
    libgobject.g_object_notify_by_pspec.argtypes = [_GObject,_GParamSpec]
except:
   pass
try:
    libgobject.g_object_remove_toggle_ref.restype = None
    libgobject.g_object_remove_toggle_ref.argtypes = [_GObject,GToggleNotify,gpointer]
except:
   pass
try:
    libgobject.g_object_thaw_notify.restype = None
    libgobject.g_object_thaw_notify.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_is_floating.restype = gboolean
    libgobject.g_object_is_floating.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_dup_qdata.restype = gpointer
    libgobject.g_object_dup_qdata.argtypes = [_GObject,GQuark,GDuplicateFunc,gpointer]
except:
   pass
try:
    libgobject.g_object_unref.restype = None
    libgobject.g_object_unref.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_get.restype = None
    libgobject.g_object_get.argtypes = [_GObject,Asciifier,]
except:
   pass
try:
    libgobject.g_weak_ref_set.restype = None
    libgobject.g_weak_ref_set.argtypes = [_GObject,_GWeakRef,gpointer]
except:
   pass
try:
    libgobject.g_object_dup_data.restype = gpointer
    libgobject.g_object_dup_data.argtypes = [_GObject,Asciifier,GDuplicateFunc,gpointer]
except:
   pass
try:
    libgobject.g_object_replace_qdata.restype = gboolean
    libgobject.g_object_replace_qdata.argtypes = [_GObject,GQuark,gpointer,gpointer,GDestroyNotify,POINTER(GDestroyNotify)]
except:
   pass
try:
    libgobject.g_object_get_data.restype = gpointer
    libgobject.g_object_get_data.argtypes = [_GObject,Asciifier]
except:
   pass
try:
    libgobject.g_object_get_property.restype = None
    libgobject.g_object_get_property.argtypes = [_GObject,Asciifier,_GValue]
except:
   pass
try:
    libgobject.g_object_watch_closure.restype = None
    libgobject.g_object_watch_closure.argtypes = [_GObject,_GClosure]
except:
   pass
try:
    libgobject.g_weak_ref_clear.restype = None
    libgobject.g_weak_ref_clear.argtypes = [_GObject,_GWeakRef]
except:
   pass
try:
    libgobject.g_object_set_data_full.restype = None
    libgobject.g_object_set_data_full.argtypes = [_GObject,Asciifier,gpointer,GDestroyNotify]
except:
   pass
try:
    libgobject.g_weak_ref_init.restype = None
    libgobject.g_weak_ref_init.argtypes = [_GObject,_GWeakRef,gpointer]
except:
   pass
try:
    libgobject.g_object_force_floating.restype = None
    libgobject.g_object_force_floating.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_class_override_property.restype = None
    libgobject.g_object_class_override_property.argtypes = [_GObject,_GObjectClass,guint,Asciifier]
except:
   pass
try:
    libgobject.g_object_class_find_property.restype = _GParamSpec
    libgobject.g_object_class_find_property.argtypes = [_GObjectClass,Asciifier]
except:
   pass
try:
    libgobject.g_object_interface_list_properties.restype = _GParamSpec
    libgobject.g_object_interface_list_properties.argtypes = [gpointer,POINTER(guint)]
except:
   pass
try:
    libgobject.g_object_newv.restype = gpointer
    libgobject.g_object_newv.argtypes = [GType,guint,_GParameter]
except:
   pass
try:
    libgobject.g_object_class_list_properties.restype = _GParamSpec
    libgobject.g_object_class_list_properties.argtypes = [_GObjectClass,POINTER(guint)]
except:
   pass
try:
    libgobject.g_object_interface_find_property.restype = _GParamSpec
    libgobject.g_object_interface_find_property.argtypes = [gpointer,Asciifier]
except:
   pass
try:
    libgobject.g_weak_ref_get.restype = gpointer
    libgobject.g_weak_ref_get.argtypes = [_GWeakRef]
except:
   pass
class GObject( object):
    """Class GObject Constructors"""
    def __init__( self, object_type, first_property_name,  obj=None, *args):
        if obj: self._object = obj
        else:
            libgobject.g_object_new.restype = POINTER(c_void_p)
            
            libgobject.g_object_new.argtypes = [GType,Asciifier,]
            self._object = libgobject.g_object_new(object_type, first_property_name, *args )

    """Methods"""
    def disconnect(  self, signal_spec, ):

        
        libgobject.g_object_disconnect( self._object,signal_spec )

    def set_qdata_full(  self, quark, data, destroy, ):

        
        libgobject.g_object_set_qdata_full( self._object,quark,data,destroy )

    def weak_unref(  self, notify, data, ):

        
        libgobject.g_object_weak_unref( self._object,notify,data )

    def steal_data(  self, key, ):

        
        return libgobject.g_object_steal_data( self._object,key )

    def run_dispose(  self, ):

        
        libgobject.g_object_run_dispose( self._object )

    def set_qdata(  self, quark, data, ):

        
        libgobject.g_object_set_qdata( self._object,quark,data )

    def g_clear_object(  self, ):

        
        libgobject.g_clear_object( self._object )

    def set_data(  self, key, data, ):

        
        libgobject.g_object_set_data( self._object,key,data )

    def ref_sink(  self, ):

        
        return libgobject.g_object_ref_sink( self._object )

    def connect(  self, signal_spec,*args  ):


        def callit( signal_spec, *args ):
                for arg in args:
                     libgobject.g_object_connect.argtypes.append(args[1])
                return libgobject.g_object_connect( signal_spec, *args)
    
        return callit( self._object, signal_spec,*args )

    def notify(  self, property_name, ):

        
        libgobject.g_object_notify( self._object,property_name )

    def class_install_properties(  self, oclass, n_pspecs, pspecs, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()
        if pspecs: pspecs = pspecs._object
        else: pspecs = POINTER(c_void_p)()

        
        libgobject.g_object_class_install_properties( self._object,oclass,n_pspecs,pspecs )

    def replace_data(  self, key, oldval, newval, destroy, old_destroy, ):

        
        return libgobject.g_object_replace_data( self._object,key,oldval,newval,destroy,old_destroy )

    def interface_install_property(  self, g_iface, pspec, ):
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_void_p)()

        
        libgobject.g_object_interface_install_property( self._object,g_iface,pspec )

    def get_qdata(  self, quark, ):

        
        return libgobject.g_object_get_qdata( self._object,quark )

    def set_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgobject.g_object_set_property( self._object,property_name,value )

    def set(  self, first_property_name,*args  ):


        def callit( first_property_name, *args ):
                for arg in args:
                     libgobject.g_object_set.argtypes.append(args[1])
                return libgobject.g_object_set( first_property_name, *args)
    
        return callit( self._object, first_property_name,*args )

    def ref(  self, ):

        
        return libgobject.g_object_ref( self._object )

    def steal_qdata(  self, quark, ):

        
        return libgobject.g_object_steal_qdata( self._object,quark )

    def add_toggle_ref(  self, notify, data, ):

        
        libgobject.g_object_add_toggle_ref( self._object,notify,data )

    def weak_ref(  self, notify, data, ):

        
        libgobject.g_object_weak_ref( self._object,notify,data )

    def add_weak_pointer(  self, weak_pointer_location, ):

        
        libgobject.g_object_add_weak_pointer( self._object,weak_pointer_location )

    def remove_weak_pointer(  self, weak_pointer_location, ):

        
        libgobject.g_object_remove_weak_pointer( self._object,weak_pointer_location )

    def class_install_property(  self, oclass, property_id, pspec, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_void_p)()

        
        libgobject.g_object_class_install_property( self._object,oclass,property_id,pspec )

    def freeze_notify(  self, ):

        
        libgobject.g_object_freeze_notify( self._object )

    def notify_by_pspec(  self, pspec, ):
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_void_p)()

        
        libgobject.g_object_notify_by_pspec( self._object,pspec )

    def remove_toggle_ref(  self, notify, data, ):

        
        libgobject.g_object_remove_toggle_ref( self._object,notify,data )

    def thaw_notify(  self, ):

        
        libgobject.g_object_thaw_notify( self._object )

    def is_floating(  self, ):

        
        return libgobject.g_object_is_floating( self._object )

    def dup_qdata(  self, quark, dup_func, user_data, ):

        
        return libgobject.g_object_dup_qdata( self._object,quark,dup_func,user_data )

    def unref(  self, ):

        
        libgobject.g_object_unref( self._object )

    def get(  self, first_property_name,*args  ):


        def callit( first_property_name, *args ):
                for arg in args:
                     libgobject.g_object_get.argtypes.append(args[1])
                return libgobject.g_object_get( first_property_name, *args)
    
        return callit( self._object, first_property_name,*args )

    def g_weak_ref_set(  self, weak_ref, object, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_void_p)()

        
        libgobject.g_weak_ref_set( self._object,weak_ref,object )

    def dup_data(  self, key, dup_func, user_data, ):

        
        return libgobject.g_object_dup_data( self._object,key,dup_func,user_data )

    def replace_qdata(  self, quark, oldval, newval, destroy, old_destroy, ):

        
        return libgobject.g_object_replace_qdata( self._object,quark,oldval,newval,destroy,old_destroy )

    def get_data(  self, key, ):

        
        return libgobject.g_object_get_data( self._object,key )

    def get_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_void_p)()

        
        libgobject.g_object_get_property( self._object,property_name,value )

    def watch_closure(  self, closure, ):
        if closure: closure = closure._object
        else: closure = POINTER(c_void_p)()

        
        libgobject.g_object_watch_closure( self._object,closure )

    def g_weak_ref_clear(  self, weak_ref, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_void_p)()

        
        libgobject.g_weak_ref_clear( self._object,weak_ref )

    def set_data_full(  self, key, data, destroy, ):

        
        libgobject.g_object_set_data_full( self._object,key,data,destroy )

    def g_weak_ref_init(  self, weak_ref, object, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_void_p)()

        
        libgobject.g_weak_ref_init( self._object,weak_ref,object )

    def force_floating(  self, ):

        
        libgobject.g_object_force_floating( self._object )

    def class_override_property(  self, oclass, property_id, name, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()

        
        libgobject.g_object_class_override_property( self._object,oclass,property_id,name )

    @staticmethod
    def class_find_property( oclass, property_name,):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgobject.g_object_class_find_property(oclass, property_name, )
 or POINTER(c_void_p)())
    @staticmethod
    def interface_list_properties( g_iface, n_properties_p,):
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgobject.g_object_interface_list_properties(g_iface, n_properties_p, )
 or POINTER(c_void_p)())
    @staticmethod
    def newv( object_type, n_parameters, parameters,):
        if parameters: parameters = parameters._object
        else: parameters = POINTER(c_void_p)()
        
        return     libgobject.g_object_newv(object_type, n_parameters, parameters, )

    @staticmethod
    def class_list_properties( oclass, n_properties,):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_void_p)()
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgobject.g_object_class_list_properties(oclass, n_properties, )
 or POINTER(c_void_p)())
    @staticmethod
    def interface_find_property( g_iface, property_name,):
        from .gobject import GParamSpec
        return GParamSpec( obj=    libgobject.g_object_interface_find_property(g_iface, property_name, )
 or POINTER(c_void_p)())
    @staticmethod
    def g_weak_ref_get( weak_ref,):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_void_p)()
        
        return     libgobject.g_weak_ref_get(weak_ref, )


    _cfuncs=[]

    def connect(self,  name, func, *args, **kargs):
        cfunc = None
        def C_Callable():
            try:
                newkargs = kargs
                if 'cfunc' in newkargs:
                    del newkargs['cfunc']
                retval = func(*args, **newkargs)
                if not retval:
                    try:
                        GObject._cfuncs.remove(cfunc)
                    except:
                        pass
                    return False
                return retval
            except:
                import traceback
                import logging
                logging.error("Error executing callback: %s"%(name))
                logging.error(traceback.format_exc())
                try:
                    GObject._cfuncs.remove(cfunc)
                except:
                    pass
                return False
        if 'cfunc' in iter(kargs.keys()):
            (cfunc, cfunctype) = kargs['cfunc']
        else:
            cfunc = CFUNCTYPE(None)(C_Callable) 
            cfunctype= CFUNCTYPE(None)
        #prevent from gonig out of scope:
        GObject._cfuncs.append(cfunc)
        libgobject.g_signal_connect_data.restype = POINTER(c_void_p)
        libgobject.g_signal_connect_data.argtypes = [c_void_p, Asciifier, CFUNCTYPE(None), c_void_p, c_void_p, c_int]
        return libgobject.g_signal_connect_data(self._object, name, cfunc, 0,0,0)


    def __del__(self):
        if self._object:
           libgobject.g_object_unref.argtypes=[c_void_p]
           libgobject.g_object_unref( self._object )

        self._object = None
