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
from gobject_types import *
from gobject_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_PangoFont = POINTER(c_int)
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
_PangoItem = POINTER(c_int)
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
_GInputStream = POINTER(c_int)
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
_GtkRequisition = POINTER(c_int)
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
_GBoxed = POINTER(c_int)
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
_GtkMisc = POINTER(c_int)
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
_GdkDragContext = POINTER(c_int)
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
_PangoLayoutIter = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
_GFileInputStream = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
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
_PangoFontsetSimple = POINTER(c_int)
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
_GtkInvisible = POINTER(c_int)
_GSourceFuncs = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
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
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int

try:
    libgobject.g_object_disconnect.restype = None
    libgobject.g_object_disconnect.argtypes = [_GObject,c_char_p]
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
    libgobject.g_object_steal_data.argtypes = [_GObject,c_char_p]
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
    libgobject.g_object_set_data.argtypes = [_GObject,c_char_p,gpointer]
except:
   pass
try:
    libgobject.g_object_ref_sink.restype = gpointer
    libgobject.g_object_ref_sink.argtypes = [_GObject]
except:
   pass
try:
    libgobject.g_object_connect.restype = gpointer
    libgobject.g_object_connect.argtypes = [_GObject,c_char_p,]
except:
   pass
try:
    libgobject.g_object_notify.restype = None
    libgobject.g_object_notify.argtypes = [_GObject,c_char_p]
except:
   pass
try:
    libgobject.g_object_class_install_properties.restype = None
    libgobject.g_object_class_install_properties.argtypes = [_GObject,_GObjectClass,guint,_GParamSpec]
except:
   pass
try:
    libgobject.g_object_replace_data.restype = gboolean
    libgobject.g_object_replace_data.argtypes = [_GObject,c_char_p,gpointer,gpointer,GDestroyNotify,POINTER(GDestroyNotify)]
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
    libgobject.g_object_set_property.argtypes = [_GObject,c_char_p,_GValue]
except:
   pass
try:
    libgobject.g_object_set.restype = None
    libgobject.g_object_set.argtypes = [_GObject,c_char_p,]
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
    libgobject.g_object_get.argtypes = [_GObject,c_char_p,]
except:
   pass
try:
    libgobject.g_weak_ref_set.restype = None
    libgobject.g_weak_ref_set.argtypes = [_GObject,_GWeakRef,gpointer]
except:
   pass
try:
    libgobject.g_object_dup_data.restype = gpointer
    libgobject.g_object_dup_data.argtypes = [_GObject,c_char_p,GDuplicateFunc,gpointer]
except:
   pass
try:
    libgobject.g_object_replace_qdata.restype = gboolean
    libgobject.g_object_replace_qdata.argtypes = [_GObject,GQuark,gpointer,gpointer,GDestroyNotify,POINTER(GDestroyNotify)]
except:
   pass
try:
    libgobject.g_object_get_data.restype = gpointer
    libgobject.g_object_get_data.argtypes = [_GObject,c_char_p]
except:
   pass
try:
    libgobject.g_object_get_property.restype = None
    libgobject.g_object_get_property.argtypes = [_GObject,c_char_p,_GValue]
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
    libgobject.g_object_set_data_full.argtypes = [_GObject,c_char_p,gpointer,GDestroyNotify]
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
    libgobject.g_object_class_override_property.argtypes = [_GObject,_GObjectClass,guint,c_char_p]
except:
   pass
try:
    libgobject.g_object_class_find_property.restype = _GParamSpec
    libgobject.g_object_class_find_property.argtypes = [_GObjectClass,c_char_p]
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
    libgobject.g_object_interface_find_property.argtypes = [gpointer,c_char_p]
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
            libgobject.g_object_new.restype = POINTER(c_int)
            
            libgobject.g_object_new.argtypes = [GType,c_char_p,]
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
        else: oclass = POINTER(c_int)()
        if pspecs: pspecs = pspecs._object
        else: pspecs = POINTER(c_int)()

        
        libgobject.g_object_class_install_properties( self._object,oclass,n_pspecs,pspecs )

    def replace_data(  self, key, oldval, newval, destroy, old_destroy, ):

        
        return libgobject.g_object_replace_data( self._object,key,oldval,newval,destroy,old_destroy )

    def interface_install_property(  self, g_iface, pspec, ):
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        
        libgobject.g_object_interface_install_property( self._object,g_iface,pspec )

    def get_qdata(  self, quark, ):

        
        return libgobject.g_object_get_qdata( self._object,quark )

    def set_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        
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
        else: oclass = POINTER(c_int)()
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        
        libgobject.g_object_class_install_property( self._object,oclass,property_id,pspec )

    def freeze_notify(  self, ):

        
        libgobject.g_object_freeze_notify( self._object )

    def notify_by_pspec(  self, pspec, ):
        if pspec: pspec = pspec._object
        else: pspec = POINTER(c_int)()

        
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
        else: weak_ref = POINTER(c_int)()

        
        libgobject.g_weak_ref_set( self._object,weak_ref,object )

    def dup_data(  self, key, dup_func, user_data, ):

        
        return libgobject.g_object_dup_data( self._object,key,dup_func,user_data )

    def replace_qdata(  self, quark, oldval, newval, destroy, old_destroy, ):

        
        return libgobject.g_object_replace_qdata( self._object,quark,oldval,newval,destroy,old_destroy )

    def get_data(  self, key, ):

        
        return libgobject.g_object_get_data( self._object,key )

    def get_property(  self, property_name, value, ):
        if value: value = value._object
        else: value = POINTER(c_int)()

        
        libgobject.g_object_get_property( self._object,property_name,value )

    def watch_closure(  self, closure, ):
        if closure: closure = closure._object
        else: closure = POINTER(c_int)()

        
        libgobject.g_object_watch_closure( self._object,closure )

    def g_weak_ref_clear(  self, weak_ref, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_int)()

        
        libgobject.g_weak_ref_clear( self._object,weak_ref )

    def set_data_full(  self, key, data, destroy, ):

        
        libgobject.g_object_set_data_full( self._object,key,data,destroy )

    def g_weak_ref_init(  self, weak_ref, object, ):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_int)()

        
        libgobject.g_weak_ref_init( self._object,weak_ref,object )

    def force_floating(  self, ):

        
        libgobject.g_object_force_floating( self._object )

    def class_override_property(  self, oclass, property_id, name, ):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_int)()

        
        libgobject.g_object_class_override_property( self._object,oclass,property_id,name )

    @staticmethod
    def class_find_property( oclass, property_name,):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_int)()
        from gobject import GParamSpec
        return GParamSpec( obj=    libgobject.g_object_class_find_property(oclass, property_name, )
 or POINTER(c_int)())
    @staticmethod
    def interface_list_properties( g_iface, n_properties_p,):
        from gobject import GParamSpec
        return GParamSpec( obj=    libgobject.g_object_interface_list_properties(g_iface, n_properties_p, )
 or POINTER(c_int)())
    @staticmethod
    def newv( object_type, n_parameters, parameters,):
        if parameters: parameters = parameters._object
        else: parameters = POINTER(c_int)()
        
        return     libgobject.g_object_newv(object_type, n_parameters, parameters, )

    @staticmethod
    def class_list_properties( oclass, n_properties,):
        if oclass: oclass = oclass._object
        else: oclass = POINTER(c_int)()
        from gobject import GParamSpec
        return GParamSpec( obj=    libgobject.g_object_class_list_properties(oclass, n_properties, )
 or POINTER(c_int)())
    @staticmethod
    def interface_find_property( g_iface, property_name,):
        from gobject import GParamSpec
        return GParamSpec( obj=    libgobject.g_object_interface_find_property(g_iface, property_name, )
 or POINTER(c_int)())
    @staticmethod
    def g_weak_ref_get( weak_ref,):
        if weak_ref: weak_ref = weak_ref._object
        else: weak_ref = POINTER(c_int)()
        
        return     libgobject.g_weak_ref_get(weak_ref, )


    _cfuncs=[]

    def connect(self,  name, func, *args, **kargs):
        cfunc = None
        def C_Callable():
            try:
                newkargs = kargs
                if newkargs.has_key('cfunc'):
                    del newkargs['cfunc']
                retval = func(*args, **newkargs)
                if not retval:
                    GObject._cfuncs.remove(cfunc)
                    return False
                return retval
            except:
                import traceback
                import logging
                logging.error("Error executing callback:")
                logging.error(traceback.format_exc())
                try:
                    GObject._cfuncs.remove(cfunc)
                except:
                    pass
                return False
        if 'cfunc' in kargs.iterkeys():
            (cfunc, cfunctype) = kargs['cfunc']
        else:
            cfunc = CFUNCTYPE(None)(C_Callable) 
            cfunctype= CFUNCTYPE(None)
        #prevent from gonig out of scope:
        GObject._cfuncs.append(cfunc)
        libgobject.g_signal_connect_data.restype = c_ulonglong
        libgobject.g_signal_connect_data.argtypes = [c_void_p, c_char_p, CFUNCTYPE(None), c_void_p, c_void_p, c_int]
        return libgobject.g_signal_connect_data(self._object, name, cfunc, 0,0,0)


    def __del__(self):
        if self._object:
           libgobject.g_object_unref.argtypes=[c_void_p]
           libgobject.g_object_unref( self._object )

        self._object = None
