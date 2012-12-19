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
_PangoFont = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GtkLabel = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_WebKitWebPolicyDecision = POINTER(c_int)
_PangoEngineShape = POINTER(c_int)
_GtkRegionFlags = POINTER(c_int)
_GAsyncResult = POINTER(c_int)
_cairo_matrix_t = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_cairo_font_options_t = POINTER(c_int)
_JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
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
_GtkAssistant = POINTER(c_int)
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
_GtkScrolledWindow = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
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
_GPollFD = POINTER(c_int)
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
_JSGlobalContext = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_GtkStylePropertyParser = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkAtom = POINTER(c_int)
_GtkBox = POINTER(c_int)
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
_GtkPackType = POINTER(c_int)
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
    libgtk3.gtk_clipboard_wait_is_target_available.argtypes = [_GtkClipboard,POINTER(c_int)]
except:
   pass
try:
    libgtk3.gtk_clipboard_request_contents.restype = None
    libgtk3.gtk_clipboard_request_contents.argtypes = [_GtkClipboard,POINTER(c_int),GtkClipboardReceivedFunc,gpointer]
except:
   pass
try:
    libgtk3.gtk_clipboard_clear.restype = None
    libgtk3.gtk_clipboard_clear.argtypes = [_GtkClipboard]
except:
   pass
try:
    libgtk3.gtk_clipboard_set_text.restype = None
    libgtk3.gtk_clipboard_set_text.argtypes = [_GtkClipboard,c_char_p,gint]
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
    libgtk3.gtk_clipboard_wait_for_contents.argtypes = [_GtkClipboard,POINTER(c_int)]
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
    libgtk3.gtk_clipboard_get.argtypes = [POINTER(c_int)]
except:
   pass
try:
    libgtk3.gtk_clipboard_get_for_display.restype = _GtkClipboard
    libgtk3.gtk_clipboard_get_for_display.argtypes = [_GdkDisplay,POINTER(c_int)]
except:
   pass
import gobject__GObject
class GtkClipboard( gobject__GObject.GObject):
    """Class GtkClipboard Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def set_with_owner(  self, targets, n_targets, get_func, clear_func, owner, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_int)()
        if owner: owner = owner._object
        else: owner = POINTER(c_int)()

        
        return libgtk3.gtk_clipboard_set_with_owner( self._object,targets,n_targets,get_func,clear_func,owner )

    def store(  self, ):

        
        libgtk3.gtk_clipboard_store( self._object )

    def get_owner(  self, ):

        from gobject import GObject
        return GObject(None,None,None,None, obj=libgtk3.gtk_clipboard_get_owner( self._object ) or POINTER(c_int)())

    def wait_is_target_available(  self, target, ):
        if target: target = target._object
        else: target = POINTER(c_int)()

        
        return libgtk3.gtk_clipboard_wait_is_target_available( self._object,target )

    def request_contents(  self, target, callback, user_data, ):
        if target: target = target._object
        else: target = POINTER(c_int)()

        
        libgtk3.gtk_clipboard_request_contents( self._object,target,callback,user_data )

    def clear(  self, ):

        
        libgtk3.gtk_clipboard_clear( self._object )

    def set_text(  self, text, len, ):

        
        libgtk3.gtk_clipboard_set_text( self._object,text,len )

    def request_text(  self, callback, user_data, ):

        
        libgtk3.gtk_clipboard_request_text( self._object,callback,user_data )

    def wait_for_targets(  self, targets, n_targets, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_int)()

        
        return libgtk3.gtk_clipboard_wait_for_targets( self._object,targets,n_targets )

    def wait_for_contents(  self, target, ):
        if target: target = target._object
        else: target = POINTER(c_int)()

        from gtk3 import GtkSelectionData
        return GtkSelectionData( obj=libgtk3.gtk_clipboard_wait_for_contents( self._object,target ) or POINTER(c_int)())

    def set_can_store(  self, targets, n_targets, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_int)()

        
        libgtk3.gtk_clipboard_set_can_store( self._object,targets,n_targets )

    def request_targets(  self, callback, user_data, ):

        
        libgtk3.gtk_clipboard_request_targets( self._object,callback,user_data )

    def wait_is_rich_text_available(  self, buffer, ):
        if buffer: buffer = buffer._object
        else: buffer = POINTER(c_int)()

        
        return libgtk3.gtk_clipboard_wait_is_rich_text_available( self._object,buffer )

    def wait_for_image(  self, ):

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_clipboard_wait_for_image( self._object ) or POINTER(c_int)())

    def wait_for_rich_text(  self, buffer, format, length, ):
        if buffer: buffer = buffer._object
        else: buffer = POINTER(c_int)()
        if format: format = format._object
        else: format = POINTER(c_int)()

        
        return libgtk3.gtk_clipboard_wait_for_rich_text( self._object,buffer,format,length )

    def wait_for_text(  self, ):

        
        return libgtk3.gtk_clipboard_wait_for_text( self._object )

    def get_display(  self, ):

        from gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gtk_clipboard_get_display( self._object ) or POINTER(c_int)())

    def wait_for_uris(  self, ):

        
        return libgtk3.gtk_clipboard_wait_for_uris( self._object )

    def set_with_data(  self, targets, n_targets, get_func, clear_func, user_data, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_int)()

        
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
        else: buffer = POINTER(c_int)()

        
        libgtk3.gtk_clipboard_request_rich_text( self._object,buffer,callback,user_data )

    def set_image(  self, pixbuf, ):
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_int)()

        
        libgtk3.gtk_clipboard_set_image( self._object,pixbuf )

    def request_image(  self, callback, user_data, ):

        
        libgtk3.gtk_clipboard_request_image( self._object,callback,user_data )

    @staticmethod
    def get( selection,):
        if selection: selection = selection._object
        else: selection = POINTER(c_int)()
        from gtk3 import GtkClipboard
        return GtkClipboard( obj=    libgtk3.gtk_clipboard_get(selection, )
 or POINTER(c_int)())
    @staticmethod
    def get_for_display( display, selection,):
        if display: display = display._object
        else: display = POINTER(c_int)()
        if selection: selection = selection._object
        else: selection = POINTER(c_int)()
        from gtk3 import GtkClipboard
        return GtkClipboard( obj=    libgtk3.gtk_clipboard_get_for_display(display, selection, )
 or POINTER(c_int)())
