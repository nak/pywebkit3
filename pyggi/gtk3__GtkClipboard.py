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
_WebKitWebPolicyDecision = POINTER(c_void_p)
_PangoEngineShape = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
_GAsyncResult = POINTER(c_void_p)
_cairo_matrix_t = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_font_options_t = POINTER(c_void_p)
_JSValue = POINTER(c_void_p)
_JSContext = POINTER(c_void_p)
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
_GInterface = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_JSContextGroup = POINTER(c_void_p)
_GFileEnumerator = POINTER(c_void_p)
_GtkDialog = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_GtkCssProvider = POINTER(c_void_p)
_GtkSymbolicColor = POINTER(c_void_p)
_void = POINTER(c_void_p)
_GtkStyleProperties = POINTER(c_void_p)
_GInputStream = POINTER(c_void_p)
_GtkIconInfo = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_WebKitWebResource = POINTER(c_void_p)
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
_GIOStream = POINTER(c_void_p)
_GIOStream = POINTER(c_void_p)
_JSString = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_GOutputStream = POINTER(c_void_p)
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
_GCancellable = POINTER(c_void_p)
_GtkWidgetClass = POINTER(c_void_p)
_GtkContainerClass = POINTER(c_void_p)
_GdkEventKey = POINTER(c_void_p)
_GtkAdjustment = POINTER(c_void_p)
_GdkDragContext = POINTER(c_void_p)
_GtkAssistant = POINTER(c_void_p)
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
_GtkScrolledWindow = POINTER(c_void_p)
_WebKitNetworkRequest = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_JSContextGroup = POINTER(c_void_p)
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
_GPollFD = POINTER(c_void_p)
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
_JSGlobalContext = POINTER(c_void_p)
_GFileIOStream = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_GtkStylePropertyParser = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_SoupMessage = POINTER(c_void_p)
_WebKitWebDataSource = POINTER(c_void_p)
_GdkAtom = POINTER(c_void_p)
_GtkBox = POINTER(c_void_p)
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
_GInputStream = POINTER(c_void_p)
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
_GtkPackType = POINTER(c_void_p)
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
GDriveStartFlags = c_int
GDriveStartStopType = c_int
GtkAssistantPageType = c_int

try:
    libgtk3.gtk_clipboard_set_with_owner.restype = gboolean
    libgtk3.gtk_clipboard_set_with_owner.argtypes = [_GtkClipboard,_GtkTargetEntry,guint,GtkClipboardGetFunc,GtkClipboardClearFunc,_GObject]
except:
   pass
try:
    libgtk3.gtk_clipboard_store.restype = None
    libgtk3.gtk_clipboard_store.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_get_owner.restype = _GObject
    libgtk3.gtk_clipboard_get_owner.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_is_target_available.restype = gboolean
    libgtk3.gtk_clipboard_wait_is_target_available.argtypes = [_GtkClipboard,POINTER(c_void_p)]
except:
   pass
try:
    libgtk3.gtk_clipboard_request_contents.restype = None
    libgtk3.gtk_clipboard_request_contents.argtypes = [_GtkClipboard,POINTER(c_void_p),GtkClipboardReceivedFunc,gpointer]
except:
   pass
try:
    libgtk3.gtk_clipboard_clear.restype = None
    libgtk3.gtk_clipboard_clear.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_set_text.restype = None
    libgtk3.gtk_clipboard_set_text.argtypes = [_GtkClipboard,Asciifier,gint]
except:
   pass
try:
    libgtk3.gtk_clipboard_request_text.restype = None
    libgtk3.gtk_clipboard_request_text.argtypes = [_GtkClipboard,GtkClipboardTextReceivedFunc,gpointer]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_for_targets.restype = gboolean
    libgtk3.gtk_clipboard_wait_for_targets.argtypes = [_GtkClipboard,_GdkAtom,POINTER(gint)]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_for_contents.restype = _GtkSelectionData
    libgtk3.gtk_clipboard_wait_for_contents.argtypes = [_GtkClipboard,POINTER(c_void_p)]
except:
   pass
try:
    libgtk3.gtk_clipboard_set_can_store.restype = None
    libgtk3.gtk_clipboard_set_can_store.argtypes = [_GtkClipboard,_GtkTargetEntry,gint]
except:
   pass
try:
    libgtk3.gtk_clipboard_request_targets.restype = None
    libgtk3.gtk_clipboard_request_targets.argtypes = [_GtkClipboard,GtkClipboardTargetsReceivedFunc,gpointer]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_is_rich_text_available.restype = gboolean
    libgtk3.gtk_clipboard_wait_is_rich_text_available.argtypes = [_GtkClipboard,_GtkTextBuffer]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_for_image.restype = _GdkPixbuf
    libgtk3.gtk_clipboard_wait_for_image.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_for_rich_text.restype = POINTER(guint8)
    libgtk3.gtk_clipboard_wait_for_rich_text.argtypes = [_GtkClipboard,_GtkTextBuffer,_GdkAtom,POINTER(gsize)]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_for_text.restype = c_char_p
    libgtk3.gtk_clipboard_wait_for_text.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_get_display.restype = _GdkDisplay
    libgtk3.gtk_clipboard_get_display.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_for_uris.restype = c_char_p
    libgtk3.gtk_clipboard_wait_for_uris.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_set_with_data.restype = gboolean
    libgtk3.gtk_clipboard_set_with_data.argtypes = [_GtkClipboard,_GtkTargetEntry,guint,GtkClipboardGetFunc,GtkClipboardClearFunc,gpointer]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_is_text_available.restype = gboolean
    libgtk3.gtk_clipboard_wait_is_text_available.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_request_uris.restype = None
    libgtk3.gtk_clipboard_request_uris.argtypes = [_GtkClipboard,GtkClipboardURIReceivedFunc,gpointer]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_is_uris_available.restype = gboolean
    libgtk3.gtk_clipboard_wait_is_uris_available.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_wait_is_image_available.restype = gboolean
    libgtk3.gtk_clipboard_wait_is_image_available.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_request_rich_text.restype = None
    libgtk3.gtk_clipboard_request_rich_text.argtypes = [_GtkClipboard,_GtkTextBuffer,GtkClipboardRichTextReceivedFunc,gpointer]
except:
   pass
try:
    libgtk3.gtk_clipboard_set_image.restype = None
    libgtk3.gtk_clipboard_set_image.argtypes = [_GtkClipboard,_GdkPixbuf]
except:
   pass
try:
    libgtk3.gtk_clipboard_request_image.restype = None
    libgtk3.gtk_clipboard_request_image.argtypes = [_GtkClipboard,GtkClipboardImageReceivedFunc,gpointer]
except:
   pass
try:
    libgtk3.gtk_clipboard_get.restype = _GtkClipboard
    libgtk3.gtk_clipboard_get.argtypes = [POINTER(c_void_p)]
except:
   pass
try:
    libgtk3.gtk_clipboard_get_for_display.restype = _GtkClipboard
    libgtk3.gtk_clipboard_get_for_display.argtypes = [_GdkDisplay,POINTER(c_void_p)]
except:
   pass
from . import gobject__GObject
class GtkClipboard( gobject__GObject.GObject):
    """Class GtkClipboard Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def set_with_owner(  self, targets, n_targets, get_func, clear_func, owner, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_void_p)()
        if owner: owner = owner._object
        else: owner = POINTER(c_void_p)()

        
        return libgtk3.gtk_clipboard_set_with_owner( self._object,targets,n_targets,get_func,clear_func,owner )

    def store(  self, ):

        
        libgtk3.gtk_clipboard_store( self._object )

    def get_owner(  self, ):

        from .gobject import GObject
        return GObject(None,None,None,None, obj=libgtk3.gtk_clipboard_get_owner( self._object ) or POINTER(c_void_p)())

    def wait_is_target_available(  self, target, ):
        if target: target = target._object
        else: target = POINTER(c_void_p)()

        
        return libgtk3.gtk_clipboard_wait_is_target_available( self._object,target )

    def request_contents(  self, target, callback, user_data, ):
        if target: target = target._object
        else: target = POINTER(c_void_p)()

        
        libgtk3.gtk_clipboard_request_contents( self._object,target,callback,user_data )

    def clear(  self, ):

        
        libgtk3.gtk_clipboard_clear( self._object )

    def set_text(  self, text, len, ):

        
        libgtk3.gtk_clipboard_set_text( self._object,text,len )

    def request_text(  self, callback, user_data, ):

        
        libgtk3.gtk_clipboard_request_text( self._object,callback,user_data )

    def wait_for_targets(  self, targets, n_targets, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_void_p)()

        
        return libgtk3.gtk_clipboard_wait_for_targets( self._object,targets,n_targets )

    def wait_for_contents(  self, target, ):
        if target: target = target._object
        else: target = POINTER(c_void_p)()

        from .gtk3 import GtkSelectionData
        return GtkSelectionData( obj=libgtk3.gtk_clipboard_wait_for_contents( self._object,target ) or POINTER(c_void_p)())

    def set_can_store(  self, targets, n_targets, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_void_p)()

        
        libgtk3.gtk_clipboard_set_can_store( self._object,targets,n_targets )

    def request_targets(  self, callback, user_data, ):

        
        libgtk3.gtk_clipboard_request_targets( self._object,callback,user_data )

    def wait_is_rich_text_available(  self, buffer, ):
        if buffer: buffer = buffer._object
        else: buffer = POINTER(c_void_p)()

        
        return libgtk3.gtk_clipboard_wait_is_rich_text_available( self._object,buffer )

    def wait_for_image(  self, ):

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_clipboard_wait_for_image( self._object ) or POINTER(c_void_p)())

    def wait_for_rich_text(  self, buffer, format, length, ):
        if buffer: buffer = buffer._object
        else: buffer = POINTER(c_void_p)()
        if format: format = format._object
        else: format = POINTER(c_void_p)()

        
        return libgtk3.gtk_clipboard_wait_for_rich_text( self._object,buffer,format,length )

    def wait_for_text(  self, ):

        
        return libgtk3.gtk_clipboard_wait_for_text( self._object )

    def get_display(  self, ):

        from .gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gtk_clipboard_get_display( self._object ) or POINTER(c_void_p)())

    def wait_for_uris(  self, ):

        
        return libgtk3.gtk_clipboard_wait_for_uris( self._object )

    def set_with_data(  self, targets, n_targets, get_func, clear_func, user_data, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_void_p)()

        
        return libgtk3.gtk_clipboard_set_with_data( self._object,targets,n_targets,get_func,clear_func,user_data )

    def wait_is_text_available(  self, ):

        
        return libgtk3.gtk_clipboard_wait_is_text_available( self._object )

    def request_uris(  self, callback, user_data, ):

        
        libgtk3.gtk_clipboard_request_uris( self._object,callback,user_data )

    def wait_is_uris_available(  self, ):

        
        return libgtk3.gtk_clipboard_wait_is_uris_available( self._object )

    def wait_is_image_available(  self, ):

        
        return libgtk3.gtk_clipboard_wait_is_image_available( self._object )

    def request_rich_text(  self, buffer, callback, user_data, ):
        if buffer: buffer = buffer._object
        else: buffer = POINTER(c_void_p)()

        
        libgtk3.gtk_clipboard_request_rich_text( self._object,buffer,callback,user_data )

    def set_image(  self, pixbuf, ):
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_void_p)()

        
        libgtk3.gtk_clipboard_set_image( self._object,pixbuf )

    def request_image(  self, callback, user_data, ):

        
        libgtk3.gtk_clipboard_request_image( self._object,callback,user_data )

    @staticmethod
    def get( selection,):
        if selection: selection = selection._object
        else: selection = POINTER(c_void_p)()
        from .gtk3 import GtkClipboard
        return GtkClipboard( obj=    libgtk3.gtk_clipboard_get(selection, )
 or POINTER(c_void_p)())
    @staticmethod
    def get_for_display( display, selection,):
        if display: display = display._object
        else: display = POINTER(c_void_p)()
        if selection: selection = selection._object
        else: selection = POINTER(c_void_p)()
        from .gtk3 import GtkClipboard
        return GtkClipboard( obj=    libgtk3.gtk_clipboard_get_for_display(display, selection, )
 or POINTER(c_void_p)())
