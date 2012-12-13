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
_GtkAssistant = POINTER(c_int)
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
_GPollFD = POINTER(c_int)
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

        libgtk3.gtk_clipboard_set_with_owner.restype = gboolean
        libgtk3.gtk_clipboard_set_with_owner.argtypes = [_GtkClipboard,_GtkTargetEntry,guint,GtkClipboardGetFunc,GtkClipboardClearFunc,_GObject]
        
        return libgtk3.gtk_clipboard_set_with_owner( self._object,targets,n_targets,get_func,clear_func,owner )

    def store(  self, ):

        libgtk3.gtk_clipboard_store.argtypes = [_GtkClipboard]
        
        libgtk3.gtk_clipboard_store( self._object )

    def get_owner(  self, ):

        libgtk3.gtk_clipboard_get_owner.restype = _GObject
        libgtk3.gtk_clipboard_get_owner.argtypes = [_GtkClipboard]
        from gobject import GObject
        return GObject(None,None,None,None, obj=libgtk3.gtk_clipboard_get_owner( self._object ) or POINTER(c_int)())

    def wait_is_target_available(  self, target, ):
        if target: target = target._object
        else: target = POINTER(c_int)()

        libgtk3.gtk_clipboard_wait_is_target_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_target_available.argtypes = [_GtkClipboard,POINTER(c_int)]
        
        return libgtk3.gtk_clipboard_wait_is_target_available( self._object,target )

    def request_contents(  self, target, callback, user_data, ):
        if target: target = target._object
        else: target = POINTER(c_int)()

        libgtk3.gtk_clipboard_request_contents.argtypes = [_GtkClipboard,POINTER(c_int),GtkClipboardReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_contents( self._object,target,callback,user_data )

    def clear(  self, ):

        libgtk3.gtk_clipboard_clear.argtypes = [_GtkClipboard]
        
        libgtk3.gtk_clipboard_clear( self._object )

    def set_text(  self, text, len, ):

        libgtk3.gtk_clipboard_set_text.argtypes = [_GtkClipboard,c_char_p,gint]
        
        libgtk3.gtk_clipboard_set_text( self._object,text,len )

    def request_text(  self, callback, user_data, ):

        libgtk3.gtk_clipboard_request_text.argtypes = [_GtkClipboard,GtkClipboardTextReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_text( self._object,callback,user_data )

    def wait_for_targets(  self, targets, n_targets, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_int)()

        libgtk3.gtk_clipboard_wait_for_targets.restype = gboolean
        libgtk3.gtk_clipboard_wait_for_targets.argtypes = [_GtkClipboard,_GdkAtom,POINTER(gint)]
        
        return libgtk3.gtk_clipboard_wait_for_targets( self._object,targets,n_targets )

    def wait_for_contents(  self, target, ):
        if target: target = target._object
        else: target = POINTER(c_int)()

        libgtk3.gtk_clipboard_wait_for_contents.restype = _GtkSelectionData
        libgtk3.gtk_clipboard_wait_for_contents.argtypes = [_GtkClipboard,POINTER(c_int)]
        from gtk3 import GtkSelectionData
        return GtkSelectionData( obj=libgtk3.gtk_clipboard_wait_for_contents( self._object,target ) or POINTER(c_int)())

    def set_can_store(  self, targets, n_targets, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_int)()

        libgtk3.gtk_clipboard_set_can_store.argtypes = [_GtkClipboard,_GtkTargetEntry,gint]
        
        libgtk3.gtk_clipboard_set_can_store( self._object,targets,n_targets )

    def request_targets(  self, callback, user_data, ):

        libgtk3.gtk_clipboard_request_targets.argtypes = [_GtkClipboard,GtkClipboardTargetsReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_targets( self._object,callback,user_data )

    def wait_is_rich_text_available(  self, buffer, ):
        if buffer: buffer = buffer._object
        else: buffer = POINTER(c_int)()

        libgtk3.gtk_clipboard_wait_is_rich_text_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_rich_text_available.argtypes = [_GtkClipboard,_GtkTextBuffer]
        
        return libgtk3.gtk_clipboard_wait_is_rich_text_available( self._object,buffer )

    def wait_for_image(  self, ):

        libgtk3.gtk_clipboard_wait_for_image.restype = _GdkPixbuf
        libgtk3.gtk_clipboard_wait_for_image.argtypes = [_GtkClipboard]
        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_clipboard_wait_for_image( self._object ) or POINTER(c_int)())

    def wait_for_rich_text(  self, buffer, format, length, ):
        if buffer: buffer = buffer._object
        else: buffer = POINTER(c_int)()
        if format: format = format._object
        else: format = POINTER(c_int)()

        libgtk3.gtk_clipboard_wait_for_rich_text.restype = POINTER(guint8)
        libgtk3.gtk_clipboard_wait_for_rich_text.argtypes = [_GtkClipboard,_GtkTextBuffer,_GdkAtom,POINTER(gsize)]
        
        return libgtk3.gtk_clipboard_wait_for_rich_text( self._object,buffer,format,length )

    def wait_for_text(  self, ):

        libgtk3.gtk_clipboard_wait_for_text.restype = c_char_p
        libgtk3.gtk_clipboard_wait_for_text.argtypes = [_GtkClipboard]
        
        return libgtk3.gtk_clipboard_wait_for_text( self._object )

    def get_display(  self, ):

        libgtk3.gtk_clipboard_get_display.restype = _GdkDisplay
        libgtk3.gtk_clipboard_get_display.argtypes = [_GtkClipboard]
        from gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gtk_clipboard_get_display( self._object ) or POINTER(c_int)())

    def wait_for_uris(  self, ):

        libgtk3.gtk_clipboard_wait_for_uris.restype = c_char_p
        libgtk3.gtk_clipboard_wait_for_uris.argtypes = [_GtkClipboard]
        
        return libgtk3.gtk_clipboard_wait_for_uris( self._object )

    def set_with_data(  self, targets, n_targets, get_func, clear_func, user_data, ):
        if targets: targets = targets._object
        else: targets = POINTER(c_int)()

        libgtk3.gtk_clipboard_set_with_data.restype = gboolean
        libgtk3.gtk_clipboard_set_with_data.argtypes = [_GtkClipboard,_GtkTargetEntry,guint,GtkClipboardGetFunc,GtkClipboardClearFunc,gpointer]
        
        return libgtk3.gtk_clipboard_set_with_data( self._object,targets,n_targets,get_func,clear_func,user_data )

    def wait_is_text_available(  self, ):

        libgtk3.gtk_clipboard_wait_is_text_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_text_available.argtypes = [_GtkClipboard]
        
        return libgtk3.gtk_clipboard_wait_is_text_available( self._object )

    def request_uris(  self, callback, user_data, ):

        libgtk3.gtk_clipboard_request_uris.argtypes = [_GtkClipboard,GtkClipboardURIReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_uris( self._object,callback,user_data )

    def wait_is_uris_available(  self, ):

        libgtk3.gtk_clipboard_wait_is_uris_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_uris_available.argtypes = [_GtkClipboard]
        
        return libgtk3.gtk_clipboard_wait_is_uris_available( self._object )

    def wait_is_image_available(  self, ):

        libgtk3.gtk_clipboard_wait_is_image_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_image_available.argtypes = [_GtkClipboard]
        
        return libgtk3.gtk_clipboard_wait_is_image_available( self._object )

    def request_rich_text(  self, buffer, callback, user_data, ):
        if buffer: buffer = buffer._object
        else: buffer = POINTER(c_int)()

        libgtk3.gtk_clipboard_request_rich_text.argtypes = [_GtkClipboard,_GtkTextBuffer,GtkClipboardRichTextReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_rich_text( self._object,buffer,callback,user_data )

    def set_image(  self, pixbuf, ):
        if pixbuf: pixbuf = pixbuf._object
        else: pixbuf = POINTER(c_int)()

        libgtk3.gtk_clipboard_set_image.argtypes = [_GtkClipboard,_GdkPixbuf]
        
        libgtk3.gtk_clipboard_set_image( self._object,pixbuf )

    def request_image(  self, callback, user_data, ):

        libgtk3.gtk_clipboard_request_image.argtypes = [_GtkClipboard,GtkClipboardImageReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_image( self._object,callback,user_data )

    @staticmethod
    def get( selection,):
        if selection: selection = selection._object
        else: selection = POINTER(c_int)()
        libgtk3.gtk_clipboard_get.restype = _GtkClipboard
        libgtk3.gtk_clipboard_get.argtypes = [POINTER(c_int)]
        from gtk3 import GtkClipboard
        return GtkClipboard( obj=    libgtk3.gtk_clipboard_get(selection, )
 or POINTER(c_int)())
    @staticmethod
    def get_for_display( display, selection,):
        if display: display = display._object
        else: display = POINTER(c_int)()
        if selection: selection = selection._object
        else: selection = POINTER(c_int)()
        libgtk3.gtk_clipboard_get_for_display.restype = _GtkClipboard
        libgtk3.gtk_clipboard_get_for_display.argtypes = [_GdkDisplay,POINTER(c_int)]
        from gtk3 import GtkClipboard
        return GtkClipboard( obj=    libgtk3.gtk_clipboard_get_for_display(display, selection, )
 or POINTER(c_int)())
