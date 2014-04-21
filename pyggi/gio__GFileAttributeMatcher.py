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
from .gio_types import *
from .gio_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_void_p)
_GdkGeometry = POINTER(c_void_p)
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
_GtkClipboard = POINTER(c_void_p)
_PangoLayoutRun = POINTER(c_void_p)
_GFileInputStream = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
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

try:
    libgio.g_file_attribute_matcher_enumerate_next.restype = c_char_p
    libgio.g_file_attribute_matcher_enumerate_next.argtypes = [_GFileAttributeMatcher]
except:
   pass
try:
    libgio.g_file_info_set_display_name.restype = None
    libgio.g_file_info_set_display_name.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_attribute_stringv.restype = None
    libgio.g_file_info_set_attribute_stringv.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_attribute_byte_string.restype = None
    libgio.g_file_info_set_attribute_byte_string.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_attribute_stringv.restype = None
    libgio.g_file_info_get_attribute_stringv.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_attribute_object.restype = None
    libgio.g_file_info_set_attribute_object.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,_GObject]
except:
   pass
try:
    libgio.g_file_info_get_edit_name.restype = None
    libgio.g_file_info_get_edit_name.argtypes = [_GFileAttributeMatcher,_GFileInfo]
except:
   pass
try:
    libgio.g_file_attribute_matcher_enumerate_namespace.restype = gboolean
    libgio.g_file_attribute_matcher_enumerate_namespace.argtypes = [_GFileAttributeMatcher,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_symlink_target.restype = None
    libgio.g_file_info_set_symlink_target.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_attribute_string.restype = None
    libgio.g_file_info_set_attribute_string.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_display_name.restype = None
    libgio.g_file_info_get_display_name.argtypes = [_GFileAttributeMatcher,_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_unset_attribute_mask.restype = None
    libgio.g_file_info_unset_attribute_mask.argtypes = [_GFileAttributeMatcher,_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_set_size.restype = None
    libgio.g_file_info_set_size.argtypes = [_GFileAttributeMatcher,_GFileInfo,goffset]
except:
   pass
try:
    libgio.g_file_info_set_is_hidden.restype = None
    libgio.g_file_info_set_is_hidden.argtypes = [_GFileAttributeMatcher,_GFileInfo,gboolean]
except:
   pass
try:
    libgio.g_file_info_get_name.restype = None
    libgio.g_file_info_get_name.argtypes = [_GFileAttributeMatcher,_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_attribute_byte_string.restype = None
    libgio.g_file_info_get_attribute_byte_string.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_attribute_int64.restype = None
    libgio.g_file_info_set_attribute_int64.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,gint64]
except:
   pass
try:
    libgio.g_file_attribute_matcher_ref.restype = _GFileAttributeMatcher
    libgio.g_file_attribute_matcher_ref.argtypes = [_GFileAttributeMatcher]
except:
   pass
try:
    libgio.g_file_info_set_attribute.restype = None
    libgio.g_file_info_set_attribute.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,GFileAttributeType,gpointer]
except:
   pass
try:
    libgio.g_file_info_set_is_symlink.restype = None
    libgio.g_file_info_set_is_symlink.argtypes = [_GFileAttributeMatcher,_GFileInfo,gboolean]
except:
   pass
try:
    libgio.g_file_info_set_attribute_uint64.restype = None
    libgio.g_file_info_set_attribute_uint64.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,guint64]
except:
   pass
try:
    libgio.g_file_info_set_content_type.restype = None
    libgio.g_file_info_set_content_type.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_attribute_as_string.restype = None
    libgio.g_file_info_get_attribute_as_string.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_attribute_matcher_unref.restype = None
    libgio.g_file_attribute_matcher_unref.argtypes = [_GFileAttributeMatcher]
except:
   pass
try:
    libgio.g_file_info_set_attribute_mask.restype = None
    libgio.g_file_info_set_attribute_mask.argtypes = [_GFileAttributeMatcher,_GFileInfo,_GFileAttributeMatcher]
except:
   pass
try:
    libgio.g_file_info_list_attributes.restype = None
    libgio.g_file_info_list_attributes.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_sort_order.restype = None
    libgio.g_file_info_set_sort_order.argtypes = [_GFileAttributeMatcher,_GFileInfo,gint32]
except:
   pass
try:
    libgio.g_file_info_set_edit_name.restype = None
    libgio.g_file_info_set_edit_name.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_attribute_matcher_matches_only.restype = gboolean
    libgio.g_file_attribute_matcher_matches_only.argtypes = [_GFileAttributeMatcher,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_file_type.restype = None
    libgio.g_file_info_set_file_type.argtypes = [_GFileAttributeMatcher,_GFileInfo,GFileType]
except:
   pass
try:
    libgio.g_file_info_set_attribute_boolean.restype = None
    libgio.g_file_info_set_attribute_boolean.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,gboolean]
except:
   pass
try:
    libgio.g_file_info_set_name.restype = None
    libgio.g_file_info_set_name.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_icon.restype = None
    libgio.g_file_info_set_icon.argtypes = [_GFileAttributeMatcher,_GFileInfo,_GIcon]
except:
   pass
try:
    libgio.g_file_info_get_etag.restype = None
    libgio.g_file_info_get_etag.argtypes = [_GFileAttributeMatcher,_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_content_type.restype = None
    libgio.g_file_info_get_content_type.argtypes = [_GFileAttributeMatcher,_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_symlink_target.restype = None
    libgio.g_file_info_get_symlink_target.argtypes = [_GFileAttributeMatcher,_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_modification_time.restype = None
    libgio.g_file_info_get_modification_time.argtypes = [_GFileAttributeMatcher,_GFileInfo,_GTimeVal]
except:
   pass
try:
    libgio.g_file_info_copy_into.restype = None
    libgio.g_file_info_copy_into.argtypes = [_GFileAttributeMatcher,_GFileInfo,_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_set_attribute_int32.restype = None
    libgio.g_file_info_set_attribute_int32.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,gint32]
except:
   pass
try:
    libgio.g_file_attribute_matcher_matches.restype = gboolean
    libgio.g_file_attribute_matcher_matches.argtypes = [_GFileAttributeMatcher,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_modification_time.restype = None
    libgio.g_file_info_set_modification_time.argtypes = [_GFileAttributeMatcher,_GFileInfo,_GTimeVal]
except:
   pass
try:
    libgio.g_file_info_remove_attribute.restype = None
    libgio.g_file_info_remove_attribute.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_set_attribute_uint32.restype = None
    libgio.g_file_info_set_attribute_uint32.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier,guint32]
except:
   pass
try:
    libgio.g_file_info_clear_status.restype = None
    libgio.g_file_info_clear_status.argtypes = [_GFileAttributeMatcher,_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_attribute_string.restype = None
    libgio.g_file_info_get_attribute_string.argtypes = [_GFileAttributeMatcher,_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_attribute_status.restype = GFileAttributeStatus
    libgio.g_file_info_get_attribute_status.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_attribute_int64.restype = gint64
    libgio.g_file_info_get_attribute_int64.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_attribute_boolean.restype = gboolean
    libgio.g_file_info_get_attribute_boolean.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_attribute_data.restype = gboolean
    libgio.g_file_info_get_attribute_data.argtypes = [_GFileInfo,Asciifier,POINTER(GFileAttributeType),POINTER(gpointer),POINTER(GFileAttributeStatus)]
except:
   pass
try:
    libgio.g_file_info_get_size.restype = goffset
    libgio.g_file_info_get_size.argtypes = [_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_is_hidden.restype = gboolean
    libgio.g_file_info_get_is_hidden.argtypes = [_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_is_backup.restype = gboolean
    libgio.g_file_info_get_is_backup.argtypes = [_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_has_attribute.restype = gboolean
    libgio.g_file_info_has_attribute.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_file_type.restype = GFileType
    libgio.g_file_info_get_file_type.argtypes = [_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_attribute_uint32.restype = guint32
    libgio.g_file_info_get_attribute_uint32.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_has_namespace.restype = gboolean
    libgio.g_file_info_has_namespace.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_icon.restype = _GIcon
    libgio.g_file_info_get_icon.argtypes = [_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_attribute_int32.restype = gint32
    libgio.g_file_info_get_attribute_int32.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_attribute_uint64.restype = guint64
    libgio.g_file_info_get_attribute_uint64.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_attribute_type.restype = GFileAttributeType
    libgio.g_file_info_get_attribute_type.argtypes = [_GFileInfo,Asciifier]
except:
   pass
try:
    libgio.g_file_info_get_is_symlink.restype = gboolean
    libgio.g_file_info_get_is_symlink.argtypes = [_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_set_attribute_status.restype = gboolean
    libgio.g_file_info_set_attribute_status.argtypes = [_GFileInfo,Asciifier,GFileAttributeStatus]
except:
   pass
try:
    libgio.g_file_info_get_sort_order.restype = gint32
    libgio.g_file_info_get_sort_order.argtypes = [_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_dup.restype = _GFileInfo
    libgio.g_file_info_dup.argtypes = [_GFileInfo]
except:
   pass
try:
    libgio.g_file_info_get_attribute_object.restype = _GObject
    libgio.g_file_info_get_attribute_object.argtypes = [_GFileInfo,Asciifier]
except:
   pass
from . import gobject__GBoxed
class GFileAttributeMatcher( gobject__GBoxed.GBoxed):
    """Class GFileAttributeMatcher Constructors"""
    def __init__( self, attributes,  obj = None):
        if obj: self._object = obj
        else:
            libgio.g_file_attribute_matcher_new.restype = POINTER(c_void_p)
            
            libgio.g_file_attribute_matcher_new.argtypes = [Asciifier]
            self._object = libgio.g_file_attribute_matcher_new(attributes, )

    """Methods"""
    def enumerate_next(  self, ):

        
        return libgio.g_file_attribute_matcher_enumerate_next( self._object )

    def g_file_info_set_display_name(  self, info, display_name, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_display_name( self._object,info,display_name )

    def g_file_info_set_attribute_stringv(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_stringv( self._object,info,attribute,attr_value )

    def g_file_info_set_attribute_byte_string(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_byte_string( self._object,info,attribute,attr_value )

    def g_file_info_get_attribute_stringv(  self, info, attribute, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_attribute_stringv( self._object,info,attribute )

    def g_file_info_set_attribute_object(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        if attr_value: attr_value = attr_value._object
        else: attr_value = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_object( self._object,info,attribute,attr_value )

    def g_file_info_get_edit_name(  self, info, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_edit_name( self._object,info )

    def enumerate_namespace(  self, ns, ):

        
        return libgio.g_file_attribute_matcher_enumerate_namespace( self._object,ns )

    def g_file_info_set_symlink_target(  self, info, symlink_target, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_symlink_target( self._object,info,symlink_target )

    def g_file_info_set_attribute_string(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_string( self._object,info,attribute,attr_value )

    def g_file_info_get_display_name(  self, info, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_display_name( self._object,info )

    def g_file_info_unset_attribute_mask(  self, info, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_unset_attribute_mask( self._object,info )

    def g_file_info_set_size(  self, info, size, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_size( self._object,info,size )

    def g_file_info_set_is_hidden(  self, info, is_hidden, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_is_hidden( self._object,info,is_hidden )

    def g_file_info_get_name(  self, info, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_name( self._object,info )

    def g_file_info_get_attribute_byte_string(  self, info, attribute, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_attribute_byte_string( self._object,info,attribute )

    def g_file_info_set_attribute_int64(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_int64( self._object,info,attribute,attr_value )

    def ref(  self, ):

        from .gio import GFileAttributeMatcher
        return GFileAttributeMatcher( obj=libgio.g_file_attribute_matcher_ref( self._object ) or POINTER(c_void_p)())

    def g_file_info_set_attribute(  self, info, attribute, type, value_p, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute( self._object,info,attribute,type,value_p )

    def g_file_info_set_is_symlink(  self, info, is_symlink, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_is_symlink( self._object,info,is_symlink )

    def g_file_info_set_attribute_uint64(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_uint64( self._object,info,attribute,attr_value )

    def g_file_info_set_content_type(  self, info, content_type, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_content_type( self._object,info,content_type )

    def g_file_info_get_attribute_as_string(  self, info, attribute, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_attribute_as_string( self._object,info,attribute )

    def unref(  self, ):

        
        libgio.g_file_attribute_matcher_unref( self._object )

    def g_file_info_set_attribute_mask(  self, info, mask, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        if mask: mask = mask._object
        else: mask = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_mask( self._object,info,mask )

    def g_file_info_list_attributes(  self, info, name_space, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_list_attributes( self._object,info,name_space )

    def g_file_info_set_sort_order(  self, info, sort_order, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_sort_order( self._object,info,sort_order )

    def g_file_info_set_edit_name(  self, info, edit_name, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_edit_name( self._object,info,edit_name )

    def matches_only(  self, attribute, ):

        
        return libgio.g_file_attribute_matcher_matches_only( self._object,attribute )

    def g_file_info_set_file_type(  self, info, type, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_file_type( self._object,info,type )

    def g_file_info_set_attribute_boolean(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_boolean( self._object,info,attribute,attr_value )

    def g_file_info_set_name(  self, info, name, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_name( self._object,info,name )

    def g_file_info_set_icon(  self, info, icon, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        if icon: icon = icon._object
        else: icon = POINTER(c_void_p)()

        
        libgio.g_file_info_set_icon( self._object,info,icon )

    def g_file_info_get_etag(  self, info, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_etag( self._object,info )

    def g_file_info_get_content_type(  self, info, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_content_type( self._object,info )

    def g_file_info_get_symlink_target(  self, info, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_symlink_target( self._object,info )

    def g_file_info_get_modification_time(  self, info, result, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        if result: result = result._object
        else: result = POINTER(c_void_p)()

        
        libgio.g_file_info_get_modification_time( self._object,info,result )

    def g_file_info_copy_into(  self, src_info, dest_info, ):
        if src_info: src_info = src_info._object
        else: src_info = POINTER(c_void_p)()
        if dest_info: dest_info = dest_info._object
        else: dest_info = POINTER(c_void_p)()

        
        libgio.g_file_info_copy_into( self._object,src_info,dest_info )

    def g_file_info_set_attribute_int32(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_int32( self._object,info,attribute,attr_value )

    def matches(  self, attribute, ):

        
        return libgio.g_file_attribute_matcher_matches( self._object,attribute )

    def g_file_info_set_modification_time(  self, info, mtime, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        if mtime: mtime = mtime._object
        else: mtime = POINTER(c_void_p)()

        
        libgio.g_file_info_set_modification_time( self._object,info,mtime )

    def g_file_info_remove_attribute(  self, info, attribute, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_remove_attribute( self._object,info,attribute )

    def g_file_info_set_attribute_uint32(  self, info, attribute, attr_value, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_set_attribute_uint32( self._object,info,attribute,attr_value )

    def g_file_info_clear_status(  self, info, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_clear_status( self._object,info )

    def g_file_info_get_attribute_string(  self, info, attribute, ):
        if info: info = info._object
        else: info = POINTER(c_void_p)()

        
        libgio.g_file_info_get_attribute_string( self._object,info,attribute )

    @staticmethod
    def g_file_info_get_attribute_status( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_attribute_status(info, attribute, )

    @staticmethod
    def g_file_info_get_attribute_int64( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_attribute_int64(info, attribute, )

    @staticmethod
    def g_file_info_get_attribute_boolean( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_attribute_boolean(info, attribute, )

    @staticmethod
    def g_file_info_get_attribute_data( info, attribute, type, value_pp, status,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_attribute_data(info, attribute, type, value_pp, status, )

    @staticmethod
    def g_file_info_get_size( info,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_size(info, )

    @staticmethod
    def g_file_info_get_is_hidden( info,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_is_hidden(info, )

    @staticmethod
    def g_file_info_get_is_backup( info,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_is_backup(info, )

    @staticmethod
    def g_file_info_has_attribute( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_has_attribute(info, attribute, )

    @staticmethod
    def g_file_info_get_file_type( info,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_file_type(info, )

    @staticmethod
    def g_file_info_get_attribute_uint32( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_attribute_uint32(info, attribute, )

    @staticmethod
    def g_file_info_has_namespace( info, name_space,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_has_namespace(info, name_space, )

    @staticmethod
    def g_file_info_get_icon( info,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        from .gobject import GIcon
        return GIcon( obj=    libgio.g_file_info_get_icon(info, )
 or POINTER(c_void_p)())
    @staticmethod
    def g_file_info_get_attribute_int32( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_attribute_int32(info, attribute, )

    @staticmethod
    def g_file_info_get_attribute_uint64( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_attribute_uint64(info, attribute, )

    @staticmethod
    def g_file_info_get_attribute_type( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_attribute_type(info, attribute, )

    @staticmethod
    def g_file_info_get_is_symlink( info,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_is_symlink(info, )

    @staticmethod
    def g_file_info_set_attribute_status( info, attribute, status,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_set_attribute_status(info, attribute, status, )

    @staticmethod
    def g_file_info_get_sort_order( info,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        
        return     libgio.g_file_info_get_sort_order(info, )

    @staticmethod
    def g_file_info_dup( other,):
        if other: other = other._object
        else: other = POINTER(c_void_p)()
        from .gio import GFileInfo
        return GFileInfo(None,None, obj=    libgio.g_file_info_dup(other, )
 or POINTER(c_void_p)())
    @staticmethod
    def g_file_info_get_attribute_object( info, attribute,):
        if info: info = info._object
        else: info = POINTER(c_void_p)()
        from .gobject import GObject
        return GObject(None,None,None,None, obj=    libgio.g_file_info_get_attribute_object(info, attribute, )
 or POINTER(c_void_p)())
