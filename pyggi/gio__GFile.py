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
from gio_types import *
from gio_enums import *

    
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
_JSValue = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkContainer = POINTER(c_int)
_PangoItem = POINTER(c_int)
_GClosure = POINTER(c_int)
_GIcon = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
_GInterface = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
_GFileEnumerator = POINTER(c_int)
_GtkDialog = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_GtkCssProvider = POINTER(c_int)
_GtkSymbolicColor = POINTER(c_int)
_void = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_GInputStream = POINTER(c_int)
_GtkIconInfo = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_WebKitWebResource = POINTER(c_int)
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
_GtkAdjustment = POINTER(c_int)
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
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
_GdkPoint = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GSource = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GIOStream = POINTER(c_int)
_GIOStream = POINTER(c_int)
_JSString = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_GOutputStream = POINTER(c_int)
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
_GCancellable = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GtkContainerClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GtkAdjustment = POINTER(c_int)
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
_GtkAboutDialog = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
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
_JSContext = POINTER(c_int)
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
_JSPropertyNameAccumulator = POINTER(c_int)
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
_JSObject = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
_GInputStream = POINTER(c_int)
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
_JSPropertyNameArray = POINTER(c_int)
_GSourceCallbackFuncs = POINTER(c_int)
_PangoFontFace = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_CairoPattern = POINTER(c_int)
_GByteArray = POINTER(c_int)
_GdkPixbufSimpleAnim = POINTER(c_int)
_JSObject = POINTER(c_int)
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
GtkLicense = c_int
GtkIconSize = c_int
GDriveStartFlags = c_int
GDriveStartStopType = c_int

try:
    libgio.g_file_enumerate_children_finish.restype = _GFileEnumerator
    libgio.g_file_enumerate_children_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_enumerate_children.restype = _GFileEnumerator
    libgio.g_file_enumerate_children.argtypes = [_GFile,c_char_p,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_query_info.restype = _GFileInfo
    libgio.g_file_query_info.argtypes = [_GFile,c_char_p,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_make_symbolic_link.restype = gboolean
    libgio.g_file_make_symbolic_link.argtypes = [_GFile,c_char_p,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_copy.restype = gboolean
    libgio.g_file_copy.argtypes = [_GFile,_GFile,GFileCopyFlags,_GCancellable,GFileProgressCallback,gpointer,_GError]
except:
   pass
try:
    libgio.g_file_set_attribute_int64.restype = gboolean
    libgio.g_file_set_attribute_int64.argtypes = [_GFile,c_char_p,gint64,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_find_enclosing_mount_async.restype = None
    libgio.g_file_find_enclosing_mount_async.argtypes = [_GFile,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_poll_mountable_finish.restype = gboolean
    libgio.g_file_poll_mountable_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_get_child_for_display_name.restype = _GFile
    libgio.g_file_get_child_for_display_name.argtypes = [_GFile,c_char_p,_GError]
except:
   pass
try:
    libgio.g_file_open_readwrite_async.restype = None
    libgio.g_file_open_readwrite_async.argtypes = [_GFile,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_get_uri_scheme.restype = c_char_p
    libgio.g_file_get_uri_scheme.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_enumerate_children_async.restype = None
    libgio.g_file_enumerate_children_async.argtypes = [_GFile,c_char_p,GFileQueryInfoFlags,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_make_directory.restype = gboolean
    libgio.g_file_make_directory.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_get_parse_name.restype = c_char_p
    libgio.g_file_get_parse_name.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_poll_mountable.restype = None
    libgio.g_file_poll_mountable.argtypes = [_GFile,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_get_basename.restype = c_char_p
    libgio.g_file_get_basename.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_get_child.restype = _GFile
    libgio.g_file_get_child.argtypes = [_GFile,c_char_p]
except:
   pass
try:
    libgio.g_file_eject_mountable.restype = None
    libgio.g_file_eject_mountable.argtypes = [_GFile,GMountUnmountFlags,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_mount_mountable.restype = None
    libgio.g_file_mount_mountable.argtypes = [_GFile,GMountMountFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_open_readwrite_finish.restype = _GFileIOStream
    libgio.g_file_open_readwrite_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_find_enclosing_mount.restype = _GMount
    libgio.g_file_find_enclosing_mount.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_replace_readwrite.restype = _GFileIOStream
    libgio.g_file_replace_readwrite.argtypes = [_GFile,c_char_p,gboolean,GFileCreateFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_set_attribute_uint32.restype = gboolean
    libgio.g_file_set_attribute_uint32.argtypes = [_GFile,c_char_p,guint32,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_query_filesystem_info_finish.restype = _GFileInfo
    libgio.g_file_query_filesystem_info_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_has_prefix.restype = gboolean
    libgio.g_file_has_prefix.argtypes = [_GFile,_GFile]
except:
   pass
try:
    libgio.g_file_replace_async.restype = None
    libgio.g_file_replace_async.argtypes = [_GFile,c_char_p,gboolean,GFileCreateFlags,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_equal.restype = gboolean
    libgio.g_file_equal.argtypes = [_GFile,_GFile]
except:
   pass
try:
    libgio.g_file_set_display_name_finish.restype = _GFile
    libgio.g_file_set_display_name_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_set_attributes_async.restype = None
    libgio.g_file_set_attributes_async.argtypes = [_GFile,_GFileInfo,GFileQueryInfoFlags,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_copy_attributes.restype = gboolean
    libgio.g_file_copy_attributes.argtypes = [_GFile,_GFile,GFileCopyFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_query_exists.restype = gboolean
    libgio.g_file_query_exists.argtypes = [_GFile,_GCancellable]
except:
   pass
try:
    libgio.g_file_create_readwrite_finish.restype = _GFileIOStream
    libgio.g_file_create_readwrite_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_query_filesystem_info.restype = _GFileInfo
    libgio.g_file_query_filesystem_info.argtypes = [_GFile,c_char_p,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_query_info_finish.restype = _GFileInfo
    libgio.g_file_query_info_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_set_attribute_string.restype = gboolean
    libgio.g_file_set_attribute_string.argtypes = [_GFile,c_char_p,c_char_p,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_find_enclosing_mount_finish.restype = _GMount
    libgio.g_file_find_enclosing_mount_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_create.restype = _GFileOutputStream
    libgio.g_file_create.argtypes = [_GFile,GFileCreateFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_query_info_async.restype = None
    libgio.g_file_query_info_async.argtypes = [_GFile,c_char_p,GFileQueryInfoFlags,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_load_contents_async.restype = None
    libgio.g_file_load_contents_async.argtypes = [_GFile,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_create_readwrite.restype = _GFileIOStream
    libgio.g_file_create_readwrite.argtypes = [_GFile,GFileCreateFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_copy_async.restype = None
    libgio.g_file_copy_async.argtypes = [_GFile,_GFile,GFileCopyFlags,int,_GCancellable,GFileProgressCallback,gpointer,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_query_writable_namespaces.restype = _GFileAttributeInfoList
    libgio.g_file_query_writable_namespaces.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_append_to_finish.restype = _GFileOutputStream
    libgio.g_file_append_to_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_mount_enclosing_volume.restype = None
    libgio.g_file_mount_enclosing_volume.argtypes = [_GFile,GMountMountFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_move.restype = gboolean
    libgio.g_file_move.argtypes = [_GFile,_GFile,GFileCopyFlags,_GCancellable,GFileProgressCallback,gpointer,_GError]
except:
   pass
try:
    libgio.g_file_eject_mountable_with_operation.restype = None
    libgio.g_file_eject_mountable_with_operation.argtypes = [_GFile,GMountUnmountFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_replace.restype = _GFileOutputStream
    libgio.g_file_replace.argtypes = [_GFile,c_char_p,gboolean,GFileCreateFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_read.restype = _GFileInputStream
    libgio.g_file_read.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_replace_contents.restype = gboolean
    libgio.g_file_replace_contents.argtypes = [_GFile,c_char_p,gsize,c_char_p,gboolean,GFileCreateFlags,c_char_p,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_resolve_relative_path.restype = _GFile
    libgio.g_file_resolve_relative_path.argtypes = [_GFile,c_char_p]
except:
   pass
try:
    libgio.g_file_get_path.restype = c_char_p
    libgio.g_file_get_path.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_trash.restype = gboolean
    libgio.g_file_trash.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_unmount_mountable_with_operation_finish.restype = gboolean
    libgio.g_file_unmount_mountable_with_operation_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_replace_readwrite_finish.restype = _GFileIOStream
    libgio.g_file_replace_readwrite_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_append_to.restype = _GFileOutputStream
    libgio.g_file_append_to.argtypes = [_GFile,GFileCreateFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_make_directory_with_parents.restype = gboolean
    libgio.g_file_make_directory_with_parents.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_get_parent.restype = _GFile
    libgio.g_file_get_parent.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_create_finish.restype = _GFileOutputStream
    libgio.g_file_create_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_mount_enclosing_volume_finish.restype = gboolean
    libgio.g_file_mount_enclosing_volume_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_query_file_type.restype = GFileType
    libgio.g_file_query_file_type.argtypes = [_GFile,GFileQueryInfoFlags,_GCancellable]
except:
   pass
try:
    libgio.g_file_eject_mountable_with_operation_finish.restype = gboolean
    libgio.g_file_eject_mountable_with_operation_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_set_attributes_from_info.restype = gboolean
    libgio.g_file_set_attributes_from_info.argtypes = [_GFile,_GFileInfo,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_read_finish.restype = _GFileInputStream
    libgio.g_file_read_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_create_async.restype = None
    libgio.g_file_create_async.argtypes = [_GFile,GFileCreateFlags,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_get_relative_path.restype = c_char_p
    libgio.g_file_get_relative_path.argtypes = [_GFile,_GFile]
except:
   pass
try:
    libgio.g_file_stop_mountable_finish.restype = gboolean
    libgio.g_file_stop_mountable_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_monitor_file.restype = _GFileMonitor
    libgio.g_file_monitor_file.argtypes = [_GFile,GFileMonitorFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_load_contents.restype = gboolean
    libgio.g_file_load_contents.argtypes = [_GFile,_GCancellable,c_char_p,POINTER(gsize),c_char_p,_GError]
except:
   pass
try:
    libgio.g_file_delete.restype = gboolean
    libgio.g_file_delete.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_start_mountable_finish.restype = gboolean
    libgio.g_file_start_mountable_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_replace_readwrite_async.restype = None
    libgio.g_file_replace_readwrite_async.argtypes = [_GFile,c_char_p,gboolean,GFileCreateFlags,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_load_contents_finish.restype = gboolean
    libgio.g_file_load_contents_finish.argtypes = [_GFile,_GAsyncResult,c_char_p,POINTER(gsize),c_char_p,_GError]
except:
   pass
try:
    libgio.g_file_eject_mountable_finish.restype = gboolean
    libgio.g_file_eject_mountable_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_replace_contents_finish.restype = gboolean
    libgio.g_file_replace_contents_finish.argtypes = [_GFile,_GAsyncResult,c_char_p,_GError]
except:
   pass
try:
    libgio.g_file_create_readwrite_async.restype = None
    libgio.g_file_create_readwrite_async.argtypes = [_GFile,GFileCreateFlags,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_open_readwrite.restype = _GFileIOStream
    libgio.g_file_open_readwrite.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_monitor_directory.restype = _GFileMonitor
    libgio.g_file_monitor_directory.argtypes = [_GFile,GFileMonitorFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_dup.restype = _GFile
    libgio.g_file_dup.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_set_attribute_int32.restype = gboolean
    libgio.g_file_set_attribute_int32.argtypes = [_GFile,c_char_p,gint32,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_monitor.restype = _GFileMonitor
    libgio.g_file_monitor.argtypes = [_GFile,GFileMonitorFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_replace_contents_async.restype = None
    libgio.g_file_replace_contents_async.argtypes = [_GFile,c_char_p,gsize,c_char_p,gboolean,GFileCreateFlags,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_is_native.restype = gboolean
    libgio.g_file_is_native.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_set_attribute_uint64.restype = gboolean
    libgio.g_file_set_attribute_uint64.argtypes = [_GFile,c_char_p,guint64,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_unmount_mountable_with_operation.restype = None
    libgio.g_file_unmount_mountable_with_operation.argtypes = [_GFile,GMountUnmountFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_append_to_async.restype = None
    libgio.g_file_append_to_async.argtypes = [_GFile,GFileCreateFlags,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_load_partial_contents_finish.restype = gboolean
    libgio.g_file_load_partial_contents_finish.argtypes = [_GFile,_GAsyncResult,c_char_p,POINTER(gsize),c_char_p,_GError]
except:
   pass
try:
    libgio.g_file_set_display_name.restype = _GFile
    libgio.g_file_set_display_name.argtypes = [_GFile,c_char_p,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_copy_finish.restype = gboolean
    libgio.g_file_copy_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_replace_finish.restype = _GFileOutputStream
    libgio.g_file_replace_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_has_parent.restype = gboolean
    libgio.g_file_has_parent.argtypes = [_GFile,_GFile]
except:
   pass
try:
    libgio.g_file_query_settable_attributes.restype = _GFileAttributeInfoList
    libgio.g_file_query_settable_attributes.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_read_async.restype = None
    libgio.g_file_read_async.argtypes = [_GFile,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_set_display_name_async.restype = None
    libgio.g_file_set_display_name_async.argtypes = [_GFile,c_char_p,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_load_partial_contents_async.restype = None
    libgio.g_file_load_partial_contents_async.argtypes = [_GFile,_GCancellable,GFileReadMoreCallback,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_unmount_mountable_finish.restype = gboolean
    libgio.g_file_unmount_mountable_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_query_default_handler.restype = _GAppInfo
    libgio.g_file_query_default_handler.argtypes = [_GFile,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_mount_mountable_finish.restype = _GFile
    libgio.g_file_mount_mountable_finish.argtypes = [_GFile,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_file_supports_thread_contexts.restype = gboolean
    libgio.g_file_supports_thread_contexts.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_set_attribute.restype = gboolean
    libgio.g_file_set_attribute.argtypes = [_GFile,c_char_p,GFileAttributeType,gpointer,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_stop_mountable.restype = None
    libgio.g_file_stop_mountable.argtypes = [_GFile,GMountUnmountFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_set_attribute_byte_string.restype = gboolean
    libgio.g_file_set_attribute_byte_string.argtypes = [_GFile,c_char_p,c_char_p,GFileQueryInfoFlags,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_file_get_uri.restype = c_char_p
    libgio.g_file_get_uri.argtypes = [_GFile]
except:
   pass
try:
    libgio.g_file_start_mountable.restype = None
    libgio.g_file_start_mountable.argtypes = [_GFile,GDriveStartFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_set_attributes_finish.restype = gboolean
    libgio.g_file_set_attributes_finish.argtypes = [_GFile,_GAsyncResult,_GFileInfo,_GError]
except:
   pass
try:
    libgio.g_file_unmount_mountable.restype = None
    libgio.g_file_unmount_mountable.argtypes = [_GFile,GMountUnmountFlags,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_has_uri_scheme.restype = gboolean
    libgio.g_file_has_uri_scheme.argtypes = [_GFile,c_char_p]
except:
   pass
try:
    libgio.g_file_query_filesystem_info_async.restype = None
    libgio.g_file_query_filesystem_info_async.argtypes = [_GFile,c_char_p,int,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_file_parse_name.restype = _GFile
    libgio.g_file_parse_name.argtypes = [c_char_p]
except:
   pass
try:
    libgio.g_file_new_for_path.restype = _GFile
    libgio.g_file_new_for_path.argtypes = [c_char_p]
except:
   pass
try:
    libgio.g_file_new_tmp.restype = _GFile
    libgio.g_file_new_tmp.argtypes = [c_char_p,_GFileIOStream,_GError]
except:
   pass
try:
    libgio.g_file_hash.restype = guint
    libgio.g_file_hash.argtypes = [gconstpointer]
except:
   pass
try:
    libgio.g_file_new_for_commandline_arg.restype = _GFile
    libgio.g_file_new_for_commandline_arg.argtypes = [c_char_p]
except:
   pass
try:
    libgio.g_file_new_for_uri.restype = _GFile
    libgio.g_file_new_for_uri.argtypes = [c_char_p]
except:
   pass
import gio__GInterface
class GFile( gio__GInterface.GInterface):
    """Class GFile Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def enumerate_children_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileEnumerator
        return GFileEnumerator( obj=libgio.g_file_enumerate_children_finish( self._object,res,error ) or POINTER(c_int)())

    def enumerate_children(  self, attributes, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileEnumerator
        return GFileEnumerator( obj=libgio.g_file_enumerate_children( self._object,attributes,flags,cancellable,error ) or POINTER(c_int)())

    def query_info(  self, attributes, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileInfo
        return GFileInfo(None,None, obj=libgio.g_file_query_info( self._object,attributes,flags,cancellable,error ) or POINTER(c_int)())

    def make_symbolic_link(  self, symlink_value, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_make_symbolic_link( self._object,symlink_value,cancellable,error )

    def copy(  self, destination, flags, cancellable, progress_callback, progress_callback_data, error, ):
        if destination: destination = destination._object
        else: destination = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if progress_callback: progress_callback = progress_callback._object
        else: progress_callback = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_copy( self._object,destination,flags,cancellable,progress_callback,progress_callback_data,error )

    def set_attribute_int64(  self, attribute, value, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attribute_int64( self._object,attribute,value,flags,cancellable,error )

    def find_enclosing_mount_async(  self, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_find_enclosing_mount_async( self._object,io_priority,cancellable,callback,user_data )

    def poll_mountable_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_poll_mountable_finish( self._object,result,error )

    def get_child_for_display_name(  self, display_name, error, ):
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFile
        return GFile(None,None, obj=libgio.g_file_get_child_for_display_name( self._object,display_name,error ) or POINTER(c_int)())

    def open_readwrite_async(  self, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_open_readwrite_async( self._object,io_priority,cancellable,callback,user_data )

    def get_uri_scheme(  self, ):

        
        return libgio.g_file_get_uri_scheme( self._object )

    def enumerate_children_async(  self, attributes, flags, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_enumerate_children_async( self._object,attributes,flags,io_priority,cancellable,callback,user_data )

    def make_directory(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_make_directory( self._object,cancellable,error )

    def get_parse_name(  self, ):

        
        return libgio.g_file_get_parse_name( self._object )

    def poll_mountable(  self, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_poll_mountable( self._object,cancellable,callback,user_data )

    def get_basename(  self, ):

        
        return libgio.g_file_get_basename( self._object )

    def get_child(  self, name, ):

        from gio import GFile
        return GFile(None, obj=libgio.g_file_get_child( self._object,name ) or POINTER(c_int)())

    def eject_mountable(  self, flags, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_eject_mountable( self._object,flags,cancellable,callback,user_data )

    def mount_mountable(  self, flags, mount_operation, cancellable, callback, user_data, ):
        if mount_operation: mount_operation = mount_operation._object
        else: mount_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_mount_mountable( self._object,flags,mount_operation,cancellable,callback,user_data )

    def open_readwrite_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileIOStream
        return GFileIOStream( obj=libgio.g_file_open_readwrite_finish( self._object,res,error ) or POINTER(c_int)())

    def find_enclosing_mount(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GMount
        return GMount( obj=libgio.g_file_find_enclosing_mount( self._object,cancellable,error ) or POINTER(c_int)())

    def replace_readwrite(  self, etag, make_backup, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileIOStream
        return GFileIOStream( obj=libgio.g_file_replace_readwrite( self._object,etag,make_backup,flags,cancellable,error ) or POINTER(c_int)())

    def set_attribute_uint32(  self, attribute, value, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attribute_uint32( self._object,attribute,value,flags,cancellable,error )

    def query_filesystem_info_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileInfo
        return GFileInfo(None, obj=libgio.g_file_query_filesystem_info_finish( self._object,res,error ) or POINTER(c_int)())

    def has_prefix(  self, prefix, ):
        if prefix: prefix = prefix._object
        else: prefix = POINTER(c_int)()

        
        return libgio.g_file_has_prefix( self._object,prefix )

    def replace_async(  self, etag, make_backup, flags, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_replace_async( self._object,etag,make_backup,flags,io_priority,cancellable,callback,user_data )

    def equal(  self, file2, ):
        if file2: file2 = file2._object
        else: file2 = POINTER(c_int)()

        
        return libgio.g_file_equal( self._object,file2 )

    def set_display_name_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFile
        return GFile(None,None, obj=libgio.g_file_set_display_name_finish( self._object,res,error ) or POINTER(c_int)())

    def set_attributes_async(  self, info, flags, io_priority, cancellable, callback, user_data, ):
        if info: info = info._object
        else: info = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_set_attributes_async( self._object,info,flags,io_priority,cancellable,callback,user_data )

    def copy_attributes(  self, destination, flags, cancellable, error, ):
        if destination: destination = destination._object
        else: destination = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_copy_attributes( self._object,destination,flags,cancellable,error )

    def query_exists(  self, cancellable, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()

        
        return libgio.g_file_query_exists( self._object,cancellable )

    def create_readwrite_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileIOStream
        return GFileIOStream( obj=libgio.g_file_create_readwrite_finish( self._object,res,error ) or POINTER(c_int)())

    def query_filesystem_info(  self, attributes, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileInfo
        return GFileInfo(None, obj=libgio.g_file_query_filesystem_info( self._object,attributes,cancellable,error ) or POINTER(c_int)())

    def query_info_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileInfo
        return GFileInfo(None, obj=libgio.g_file_query_info_finish( self._object,res,error ) or POINTER(c_int)())

    def set_attribute_string(  self, attribute, value, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attribute_string( self._object,attribute,value,flags,cancellable,error )

    def find_enclosing_mount_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GMount
        return GMount( obj=libgio.g_file_find_enclosing_mount_finish( self._object,res,error ) or POINTER(c_int)())

    def create(  self, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileOutputStream
        return GFileOutputStream( obj=libgio.g_file_create( self._object,flags,cancellable,error ) or POINTER(c_int)())

    def query_info_async(  self, attributes, flags, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_query_info_async( self._object,attributes,flags,io_priority,cancellable,callback,user_data )

    def load_contents_async(  self, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_load_contents_async( self._object,cancellable,callback,user_data )

    def create_readwrite(  self, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileIOStream
        return GFileIOStream( obj=libgio.g_file_create_readwrite( self._object,flags,cancellable,error ) or POINTER(c_int)())

    def copy_async(  self, destination, flags, io_priority, cancellable, progress_callback, progress_callback_data, callback, user_data, ):
        if destination: destination = destination._object
        else: destination = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if progress_callback: progress_callback = progress_callback._object
        else: progress_callback = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_copy_async( self._object,destination,flags,io_priority,cancellable,progress_callback,progress_callback_data,callback,user_data )

    def query_writable_namespaces(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileAttributeInfoList
        return GFileAttributeInfoList( obj=libgio.g_file_query_writable_namespaces( self._object,cancellable,error ) or POINTER(c_int)())

    def append_to_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileOutputStream
        return GFileOutputStream( obj=libgio.g_file_append_to_finish( self._object,res,error ) or POINTER(c_int)())

    def mount_enclosing_volume(  self, flags, mount_operation, cancellable, callback, user_data, ):
        if mount_operation: mount_operation = mount_operation._object
        else: mount_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_mount_enclosing_volume( self._object,flags,mount_operation,cancellable,callback,user_data )

    def move(  self, destination, flags, cancellable, progress_callback, progress_callback_data, error, ):
        if destination: destination = destination._object
        else: destination = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if progress_callback: progress_callback = progress_callback._object
        else: progress_callback = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_move( self._object,destination,flags,cancellable,progress_callback,progress_callback_data,error )

    def eject_mountable_with_operation(  self, flags, mount_operation, cancellable, callback, user_data, ):
        if mount_operation: mount_operation = mount_operation._object
        else: mount_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_eject_mountable_with_operation( self._object,flags,mount_operation,cancellable,callback,user_data )

    def replace(  self, etag, make_backup, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileOutputStream
        return GFileOutputStream( obj=libgio.g_file_replace( self._object,etag,make_backup,flags,cancellable,error ) or POINTER(c_int)())

    def read(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileInputStream
        return GFileInputStream( obj=libgio.g_file_read( self._object,cancellable,error ) or POINTER(c_int)())

    def replace_contents(  self, contents, length, etag, make_backup, flags, new_etag, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_replace_contents( self._object,contents,length,etag,make_backup,flags,new_etag,cancellable,error )

    def resolve_relative_path(  self, relative_path, ):

        from gio import GFile
        return GFile(None, obj=libgio.g_file_resolve_relative_path( self._object,relative_path ) or POINTER(c_int)())

    def get_path(  self, ):

        
        return libgio.g_file_get_path( self._object )

    def trash(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_trash( self._object,cancellable,error )

    def unmount_mountable_with_operation_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_unmount_mountable_with_operation_finish( self._object,result,error )

    def replace_readwrite_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileIOStream
        return GFileIOStream( obj=libgio.g_file_replace_readwrite_finish( self._object,res,error ) or POINTER(c_int)())

    def append_to(  self, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileOutputStream
        return GFileOutputStream( obj=libgio.g_file_append_to( self._object,flags,cancellable,error ) or POINTER(c_int)())

    def make_directory_with_parents(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_make_directory_with_parents( self._object,cancellable,error )

    def get_parent(  self, ):

        from gio import GFile
        return GFile( obj=libgio.g_file_get_parent( self._object ) or POINTER(c_int)())

    def create_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileOutputStream
        return GFileOutputStream( obj=libgio.g_file_create_finish( self._object,res,error ) or POINTER(c_int)())

    def mount_enclosing_volume_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_mount_enclosing_volume_finish( self._object,result,error )

    def query_file_type(  self, flags, cancellable, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()

        
        return libgio.g_file_query_file_type( self._object,flags,cancellable )

    def eject_mountable_with_operation_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_eject_mountable_with_operation_finish( self._object,result,error )

    def set_attributes_from_info(  self, info, flags, cancellable, error, ):
        if info: info = info._object
        else: info = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attributes_from_info( self._object,info,flags,cancellable,error )

    def read_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileInputStream
        return GFileInputStream( obj=libgio.g_file_read_finish( self._object,res,error ) or POINTER(c_int)())

    def create_async(  self, flags, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_create_async( self._object,flags,io_priority,cancellable,callback,user_data )

    def get_relative_path(  self, descendant, ):
        if descendant: descendant = descendant._object
        else: descendant = POINTER(c_int)()

        
        return libgio.g_file_get_relative_path( self._object,descendant )

    def stop_mountable_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_stop_mountable_finish( self._object,result,error )

    def monitor_file(  self, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileMonitor
        return GFileMonitor( obj=libgio.g_file_monitor_file( self._object,flags,cancellable,error ) or POINTER(c_int)())

    def load_contents(  self, cancellable, contents, length, etag_out, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_load_contents( self._object,cancellable,contents,length,etag_out,error )

    def delete(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_delete( self._object,cancellable,error )

    def start_mountable_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_start_mountable_finish( self._object,result,error )

    def replace_readwrite_async(  self, etag, make_backup, flags, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_replace_readwrite_async( self._object,etag,make_backup,flags,io_priority,cancellable,callback,user_data )

    def load_contents_finish(  self, res, contents, length, etag_out, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_load_contents_finish( self._object,res,contents,length,etag_out,error )

    def eject_mountable_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_eject_mountable_finish( self._object,result,error )

    def replace_contents_finish(  self, res, new_etag, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_replace_contents_finish( self._object,res,new_etag,error )

    def create_readwrite_async(  self, flags, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_create_readwrite_async( self._object,flags,io_priority,cancellable,callback,user_data )

    def open_readwrite(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileIOStream
        return GFileIOStream( obj=libgio.g_file_open_readwrite( self._object,cancellable,error ) or POINTER(c_int)())

    def monitor_directory(  self, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileMonitor
        return GFileMonitor( obj=libgio.g_file_monitor_directory( self._object,flags,cancellable,error ) or POINTER(c_int)())

    def dup(  self, ):

        from gio import GFile
        return GFile( obj=libgio.g_file_dup( self._object ) or POINTER(c_int)())

    def set_attribute_int32(  self, attribute, value, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attribute_int32( self._object,attribute,value,flags,cancellable,error )

    def monitor(  self, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileMonitor
        return GFileMonitor( obj=libgio.g_file_monitor( self._object,flags,cancellable,error ) or POINTER(c_int)())

    def replace_contents_async(  self, contents, length, etag, make_backup, flags, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_replace_contents_async( self._object,contents,length,etag,make_backup,flags,cancellable,callback,user_data )

    def is_native(  self, ):

        
        return libgio.g_file_is_native( self._object )

    def set_attribute_uint64(  self, attribute, value, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attribute_uint64( self._object,attribute,value,flags,cancellable,error )

    def unmount_mountable_with_operation(  self, flags, mount_operation, cancellable, callback, user_data, ):
        if mount_operation: mount_operation = mount_operation._object
        else: mount_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_unmount_mountable_with_operation( self._object,flags,mount_operation,cancellable,callback,user_data )

    def append_to_async(  self, flags, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_append_to_async( self._object,flags,io_priority,cancellable,callback,user_data )

    def load_partial_contents_finish(  self, res, contents, length, etag_out, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_load_partial_contents_finish( self._object,res,contents,length,etag_out,error )

    def set_display_name(  self, display_name, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFile
        return GFile(None,None,None, obj=libgio.g_file_set_display_name( self._object,display_name,cancellable,error ) or POINTER(c_int)())

    def copy_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_copy_finish( self._object,res,error )

    def replace_finish(  self, res, error, ):
        if res: res = res._object
        else: res = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileOutputStream
        return GFileOutputStream( obj=libgio.g_file_replace_finish( self._object,res,error ) or POINTER(c_int)())

    def has_parent(  self, parent, ):
        if parent: parent = parent._object
        else: parent = POINTER(c_int)()

        
        return libgio.g_file_has_parent( self._object,parent )

    def query_settable_attributes(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFileAttributeInfoList
        return GFileAttributeInfoList( obj=libgio.g_file_query_settable_attributes( self._object,cancellable,error ) or POINTER(c_int)())

    def read_async(  self, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_read_async( self._object,io_priority,cancellable,callback,user_data )

    def set_display_name_async(  self, display_name, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_set_display_name_async( self._object,display_name,io_priority,cancellable,callback,user_data )

    def load_partial_contents_async(  self, cancellable, read_more_callback, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if read_more_callback: read_more_callback = read_more_callback._object
        else: read_more_callback = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_load_partial_contents_async( self._object,cancellable,read_more_callback,callback,user_data )

    def unmount_mountable_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_unmount_mountable_finish( self._object,result,error )

    def query_default_handler(  self, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gobject import GAppInfo
        return GAppInfo( obj=libgio.g_file_query_default_handler( self._object,cancellable,error ) or POINTER(c_int)())

    def mount_mountable_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        from gio import GFile
        return GFile(None,None, obj=libgio.g_file_mount_mountable_finish( self._object,result,error ) or POINTER(c_int)())

    def supports_thread_contexts(  self, ):

        
        return libgio.g_file_supports_thread_contexts( self._object )

    def set_attribute(  self, attribute, type, value_p, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attribute( self._object,attribute,type,value_p,flags,cancellable,error )

    def stop_mountable(  self, flags, mount_operation, cancellable, callback, user_data, ):
        if mount_operation: mount_operation = mount_operation._object
        else: mount_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_stop_mountable( self._object,flags,mount_operation,cancellable,callback,user_data )

    def set_attribute_byte_string(  self, attribute, value, flags, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attribute_byte_string( self._object,attribute,value,flags,cancellable,error )

    def get_uri(  self, ):

        
        return libgio.g_file_get_uri( self._object )

    def start_mountable(  self, flags, start_operation, cancellable, callback, user_data, ):
        if start_operation: start_operation = start_operation._object
        else: start_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_start_mountable( self._object,flags,start_operation,cancellable,callback,user_data )

    def set_attributes_finish(  self, result, info, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if info: info = info._object
        else: info = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_file_set_attributes_finish( self._object,result,info,error )

    def unmount_mountable(  self, flags, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_unmount_mountable( self._object,flags,cancellable,callback,user_data )

    def has_uri_scheme(  self, uri_scheme, ):

        
        return libgio.g_file_has_uri_scheme( self._object,uri_scheme )

    def query_filesystem_info_async(  self, attributes, io_priority, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_file_query_filesystem_info_async( self._object,attributes,io_priority,cancellable,callback,user_data )

    @staticmethod
    def parse_name( parse_name,):
        from gio import GFile
        return GFile( obj=    libgio.g_file_parse_name(parse_name, )
 or POINTER(c_int)())
    @staticmethod
    def new_for_path( path,):
        from gio import GFile
        return GFile( obj=    libgio.g_file_new_for_path(path, )
 or POINTER(c_int)())
    @staticmethod
    def new_tmp( tmpl, iostream, error,):
        if iostream: iostream = iostream._object
        else: iostream = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()
        from gio import GFile
        return GFile( obj=    libgio.g_file_new_tmp(tmpl, iostream, error, )
 or POINTER(c_int)())
    @staticmethod
    def hash( file,):
        
        return     libgio.g_file_hash(file, )

    @staticmethod
    def new_for_commandline_arg( arg,):
        from gio import GFile
        return GFile( obj=    libgio.g_file_new_for_commandline_arg(arg, )
 or POINTER(c_int)())
    @staticmethod
    def new_for_uri( uri,):
        from gio import GFile
        return GFile( obj=    libgio.g_file_new_for_uri(uri, )
 or POINTER(c_int)())
