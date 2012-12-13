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
from gobject_types import *
    
    
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
__GClosure = POINTER(c_int)
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
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
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
__GdkEventKey = POINTER(c_int)
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

class GString( object):
    """Class GString Constructors"""
    def __init__( self, dfl_size,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_string_sized_new.restype = POINTER(c_int)
            
            libgobject.g_string_sized_new.argtypes = [gsize]
            self._object = libgobject.g_string_sized_new(dfl_size, )

    """Methods"""
    def append_c(  self, c, ):

        libgobject.g_string_append_c.restype = _GString
        libgobject.g_string_append_c.argtypes = [_GString,gchar]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_append_c( self._object,c ) or POINTER(c_int)())

    def prepend_c(  self, c, ):

        libgobject.g_string_prepend_c.restype = _GString
        libgobject.g_string_prepend_c.argtypes = [_GString,gchar]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_prepend_c( self._object,c ) or POINTER(c_int)())

    def equal(  self, v2, ):
        if v2: v2 = v2._object
        else: v2 = POINTER(c_int)()

        libgobject.g_string_equal.restype = gboolean
        libgobject.g_string_equal.argtypes = [_GString,_GString]
        
        return libgobject.g_string_equal( self._object,v2 )

    def insert(  self, pos, val, ):
        if pos: pos = pos._object
        else: pos = POINTER(c_int)()

        libgobject.g_string_insert.restype = _GString
        libgobject.g_string_insert.argtypes = [_GString,gssize,c_char_p]
        from gobject import GString
        return GString(None,None, obj=libgobject.g_string_insert( self._object,pos,val ) or POINTER(c_int)())

    def set_size(  self, len, ):

        libgobject.g_string_set_size.restype = _GString
        libgobject.g_string_set_size.argtypes = [_GString,gsize]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_set_size( self._object,len ) or POINTER(c_int)())

    def append_printf(  self, format,*args  ):


        def callit( format, *args ):
                libgobject.g_string_append_printf.restype = None
                libgobject.g_string_append_printf.argtypes = [ POINTER(c_int), c_char_p]
                for arg in args:
                     libgobject.g_string_append_printf.argtypes.append(args[1])
                return libgobject.g_string_append_printf( format, *args)
    
        return callit( self._object, format,*args )

    def free_to_bytes(  self, ):

        libgobject.g_string_free_to_bytes.restype = _GBytes
        libgobject.g_string_free_to_bytes.argtypes = [_GString]
        from gobject import GBytes
        return GBytes(None,None, obj=libgobject.g_string_free_to_bytes( self._object ) or POINTER(c_int)())

    def append_uri_escaped(  self, unescaped, reserved_chars_allowed, allow_utf8, ):

        libgobject.g_string_append_uri_escaped.restype = _GString
        libgobject.g_string_append_uri_escaped.argtypes = [_GString,c_char_p,c_char_p,gboolean]
        from gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_append_uri_escaped( self._object,unescaped,reserved_chars_allowed,allow_utf8 ) or POINTER(c_int)())

    def free(  self, free_segment, ):

        libgobject.g_string_free.restype = c_char_p
        libgobject.g_string_free.argtypes = [_GString,gboolean]
        
        return libgobject.g_string_free( self._object,free_segment )

    def up(  self, ):

        libgobject.g_string_up.restype = _GString
        libgobject.g_string_up.argtypes = [_GString]
        from gobject import GString
        return GString( obj=libgobject.g_string_up( self._object ) or POINTER(c_int)())

    def prepend_len(  self, val, len, ):
        if len: len = len._object
        else: len = POINTER(c_int)()

        libgobject.g_string_prepend_len.restype = _GString
        libgobject.g_string_prepend_len.argtypes = [_GString,c_char_p,gssize]
        from gobject import GString
        return GString(None,None, obj=libgobject.g_string_prepend_len( self._object,val,len ) or POINTER(c_int)())

    def overwrite_len(  self, pos, val, len, ):
        if len: len = len._object
        else: len = POINTER(c_int)()

        libgobject.g_string_overwrite_len.restype = _GString
        libgobject.g_string_overwrite_len.argtypes = [_GString,gsize,c_char_p,gssize]
        from gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_overwrite_len( self._object,pos,val,len ) or POINTER(c_int)())

    def assign(  self, rval, ):

        libgobject.g_string_assign.restype = _GString
        libgobject.g_string_assign.argtypes = [_GString,c_char_p]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_assign( self._object,rval ) or POINTER(c_int)())

    def erase(  self, pos, len, ):
        if pos: pos = pos._object
        else: pos = POINTER(c_int)()
        if len: len = len._object
        else: len = POINTER(c_int)()

        libgobject.g_string_erase.restype = _GString
        libgobject.g_string_erase.argtypes = [_GString,gssize,gssize]
        from gobject import GString
        return GString(None,None, obj=libgobject.g_string_erase( self._object,pos,len ) or POINTER(c_int)())

    def down(  self, ):

        libgobject.g_string_down.restype = _GString
        libgobject.g_string_down.argtypes = [_GString]
        from gobject import GString
        return GString( obj=libgobject.g_string_down( self._object ) or POINTER(c_int)())

    def append_len(  self, val, len, ):
        if len: len = len._object
        else: len = POINTER(c_int)()

        libgobject.g_string_append_len.restype = _GString
        libgobject.g_string_append_len.argtypes = [_GString,c_char_p,gssize]
        from gobject import GString
        return GString(None,None, obj=libgobject.g_string_append_len( self._object,val,len ) or POINTER(c_int)())

    def printf(  self, format,*args  ):


        def callit( format, *args ):
                libgobject.g_string_printf.restype = None
                libgobject.g_string_printf.argtypes = [ POINTER(c_int), c_char_p]
                for arg in args:
                     libgobject.g_string_printf.argtypes.append(args[1])
                return libgobject.g_string_printf( format, *args)
    
        return callit( self._object, format,*args )

    def truncate(  self, len, ):

        libgobject.g_string_truncate.restype = _GString
        libgobject.g_string_truncate.argtypes = [_GString,gsize]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_truncate( self._object,len ) or POINTER(c_int)())

    def append(  self, val, ):

        libgobject.g_string_append.restype = _GString
        libgobject.g_string_append.argtypes = [_GString,c_char_p]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_append( self._object,val ) or POINTER(c_int)())

    def prepend(  self, val, ):

        libgobject.g_string_prepend.restype = _GString
        libgobject.g_string_prepend.argtypes = [_GString,c_char_p]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_prepend( self._object,val ) or POINTER(c_int)())

    def append_unichar(  self, wc, ):
        if wc: wc = wc._object
        else: wc = POINTER(c_int)()

        libgobject.g_string_append_unichar.restype = _GString
        libgobject.g_string_append_unichar.argtypes = [_GString,gunichar]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_append_unichar( self._object,wc ) or POINTER(c_int)())

    def prepend_unichar(  self, wc, ):
        if wc: wc = wc._object
        else: wc = POINTER(c_int)()

        libgobject.g_string_prepend_unichar.restype = _GString
        libgobject.g_string_prepend_unichar.argtypes = [_GString,gunichar]
        from gobject import GString
        return GString(None, obj=libgobject.g_string_prepend_unichar( self._object,wc ) or POINTER(c_int)())

    def insert_len(  self, pos, val, len, ):
        if pos: pos = pos._object
        else: pos = POINTER(c_int)()
        if len: len = len._object
        else: len = POINTER(c_int)()

        libgobject.g_string_insert_len.restype = _GString
        libgobject.g_string_insert_len.argtypes = [_GString,gssize,c_char_p,gssize]
        from gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_insert_len( self._object,pos,val,len ) or POINTER(c_int)())

    def overwrite(  self, pos, val, ):

        libgobject.g_string_overwrite.restype = _GString
        libgobject.g_string_overwrite.argtypes = [_GString,gsize,c_char_p]
        from gobject import GString
        return GString(None,None, obj=libgobject.g_string_overwrite( self._object,pos,val ) or POINTER(c_int)())

    def insert_c(  self, pos, c, ):
        if pos: pos = pos._object
        else: pos = POINTER(c_int)()

        libgobject.g_string_insert_c.restype = _GString
        libgobject.g_string_insert_c.argtypes = [_GString,gssize,gchar]
        from gobject import GString
        return GString(None,None, obj=libgobject.g_string_insert_c( self._object,pos,c ) or POINTER(c_int)())

    def hash(  self, ):

        libgobject.g_string_hash.restype = guint
        libgobject.g_string_hash.argtypes = [_GString]
        
        return libgobject.g_string_hash( self._object )

    def insert_unichar(  self, pos, wc, ):
        if pos: pos = pos._object
        else: pos = POINTER(c_int)()
        if wc: wc = wc._object
        else: wc = POINTER(c_int)()

        libgobject.g_string_insert_unichar.restype = _GString
        libgobject.g_string_insert_unichar.argtypes = [_GString,gssize,gunichar]
        from gobject import GString
        return GString(None,None, obj=libgobject.g_string_insert_unichar( self._object,pos,wc ) or POINTER(c_int)())

    @staticmethod
    def new_len( init, len,):
        if len: len = len._object
        else: len = POINTER(c_int)()
        libgobject.g_string_new_len.restype = _GString
        libgobject.g_string_new_len.argtypes = [c_char_p,gssize]
        from gobject import GString
        return GString(None, obj=    libgobject.g_string_new_len(init, len, )
 or POINTER(c_int)())
