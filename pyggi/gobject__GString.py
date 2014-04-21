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

try:
    libgobject.g_string_append_c.restype = _GString
    libgobject.g_string_append_c.argtypes = [_GString,gchar]
except:
   pass
try:
    libgobject.g_string_prepend_c.restype = _GString
    libgobject.g_string_prepend_c.argtypes = [_GString,gchar]
except:
   pass
try:
    libgobject.g_string_equal.restype = gboolean
    libgobject.g_string_equal.argtypes = [_GString,_GString]
except:
   pass
try:
    libgobject.g_string_insert.restype = _GString
    libgobject.g_string_insert.argtypes = [_GString,gssize,Asciifier]
except:
   pass
try:
    libgobject.g_string_set_size.restype = _GString
    libgobject.g_string_set_size.argtypes = [_GString,gsize]
except:
   pass
try:
    libgobject.g_string_append_printf.restype = None
    libgobject.g_string_append_printf.argtypes = [_GString,Asciifier,]
except:
   pass
try:
    libgobject.g_string_free_to_bytes.restype = _GBytes
    libgobject.g_string_free_to_bytes.argtypes = [_GString]
except:
   pass
try:
    libgobject.g_string_append_uri_escaped.restype = _GString
    libgobject.g_string_append_uri_escaped.argtypes = [_GString,Asciifier,Asciifier,gboolean]
except:
   pass
try:
    libgobject.g_string_free.restype = c_char_p
    libgobject.g_string_free.argtypes = [_GString,gboolean]
except:
   pass
try:
    libgobject.g_string_up.restype = _GString
    libgobject.g_string_up.argtypes = [_GString]
except:
   pass
try:
    libgobject.g_string_prepend_len.restype = _GString
    libgobject.g_string_prepend_len.argtypes = [_GString,Asciifier,gssize]
except:
   pass
try:
    libgobject.g_string_overwrite_len.restype = _GString
    libgobject.g_string_overwrite_len.argtypes = [_GString,gsize,Asciifier,gssize]
except:
   pass
try:
    libgobject.g_string_assign.restype = _GString
    libgobject.g_string_assign.argtypes = [_GString,Asciifier]
except:
   pass
try:
    libgobject.g_string_erase.restype = _GString
    libgobject.g_string_erase.argtypes = [_GString,gssize,gssize]
except:
   pass
try:
    libgobject.g_string_down.restype = _GString
    libgobject.g_string_down.argtypes = [_GString]
except:
   pass
try:
    libgobject.g_string_append_len.restype = _GString
    libgobject.g_string_append_len.argtypes = [_GString,Asciifier,gssize]
except:
   pass
try:
    libgobject.g_string_printf.restype = None
    libgobject.g_string_printf.argtypes = [_GString,Asciifier,]
except:
   pass
try:
    libgobject.g_string_truncate.restype = _GString
    libgobject.g_string_truncate.argtypes = [_GString,gsize]
except:
   pass
try:
    libgobject.g_string_append.restype = _GString
    libgobject.g_string_append.argtypes = [_GString,Asciifier]
except:
   pass
try:
    libgobject.g_string_prepend.restype = _GString
    libgobject.g_string_prepend.argtypes = [_GString,Asciifier]
except:
   pass
try:
    libgobject.g_string_append_unichar.restype = _GString
    libgobject.g_string_append_unichar.argtypes = [_GString,gunichar]
except:
   pass
try:
    libgobject.g_string_prepend_unichar.restype = _GString
    libgobject.g_string_prepend_unichar.argtypes = [_GString,gunichar]
except:
   pass
try:
    libgobject.g_string_insert_len.restype = _GString
    libgobject.g_string_insert_len.argtypes = [_GString,gssize,Asciifier,gssize]
except:
   pass
try:
    libgobject.g_string_overwrite.restype = _GString
    libgobject.g_string_overwrite.argtypes = [_GString,gsize,Asciifier]
except:
   pass
try:
    libgobject.g_string_insert_c.restype = _GString
    libgobject.g_string_insert_c.argtypes = [_GString,gssize,gchar]
except:
   pass
try:
    libgobject.g_string_hash.restype = guint
    libgobject.g_string_hash.argtypes = [_GString]
except:
   pass
try:
    libgobject.g_string_insert_unichar.restype = _GString
    libgobject.g_string_insert_unichar.argtypes = [_GString,gssize,gunichar]
except:
   pass
try:
    libgobject.g_string_new_len.restype = _GString
    libgobject.g_string_new_len.argtypes = [Asciifier,gssize]
except:
   pass
class GString( object):
    """Class GString Constructors"""
    def __init__( self, dfl_size,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_string_sized_new.restype = POINTER(c_void_p)
            
            libgobject.g_string_sized_new.argtypes = [gsize]
            self._object = libgobject.g_string_sized_new(dfl_size, )

    """Methods"""
    def append_c(  self, c, ):

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_append_c( self._object,c ) or POINTER(c_void_p)())

    def prepend_c(  self, c, ):

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_prepend_c( self._object,c ) or POINTER(c_void_p)())

    def equal(  self, v2, ):
        if v2: v2 = v2._object
        else: v2 = POINTER(c_void_p)()

        
        return libgobject.g_string_equal( self._object,v2 )

    def insert(  self, pos, val, ):

        from .gobject import GString
        return GString(None,None, obj=libgobject.g_string_insert( self._object,pos,val ) or POINTER(c_void_p)())

    def set_size(  self, len, ):

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_set_size( self._object,len ) or POINTER(c_void_p)())

    def append_printf(  self, format,*args  ):


        def callit( format, *args ):
                for arg in args:
                     libgobject.g_string_append_printf.argtypes.append(args[1])
                return libgobject.g_string_append_printf( format, *args)
    
        return callit( self._object, format,*args )

    def free_to_bytes(  self, ):

        from .gobject import GBytes
        return GBytes(None,None, obj=libgobject.g_string_free_to_bytes( self._object ) or POINTER(c_void_p)())

    def append_uri_escaped(  self, unescaped, reserved_chars_allowed, allow_utf8, ):

        from .gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_append_uri_escaped( self._object,unescaped,reserved_chars_allowed,allow_utf8 ) or POINTER(c_void_p)())

    def free(  self, free_segment, ):

        
        return libgobject.g_string_free( self._object,free_segment )

    def up(  self, ):

        from .gobject import GString
        return GString( obj=libgobject.g_string_up( self._object ) or POINTER(c_void_p)())

    def prepend_len(  self, val, len, ):

        from .gobject import GString
        return GString(None,None, obj=libgobject.g_string_prepend_len( self._object,val,len ) or POINTER(c_void_p)())

    def overwrite_len(  self, pos, val, len, ):

        from .gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_overwrite_len( self._object,pos,val,len ) or POINTER(c_void_p)())

    def assign(  self, rval, ):

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_assign( self._object,rval ) or POINTER(c_void_p)())

    def erase(  self, pos, len, ):

        from .gobject import GString
        return GString(None,None, obj=libgobject.g_string_erase( self._object,pos,len ) or POINTER(c_void_p)())

    def down(  self, ):

        from .gobject import GString
        return GString( obj=libgobject.g_string_down( self._object ) or POINTER(c_void_p)())

    def append_len(  self, val, len, ):

        from .gobject import GString
        return GString(None,None, obj=libgobject.g_string_append_len( self._object,val,len ) or POINTER(c_void_p)())

    def printf(  self, format,*args  ):


        def callit( format, *args ):
                for arg in args:
                     libgobject.g_string_printf.argtypes.append(args[1])
                return libgobject.g_string_printf( format, *args)
    
        return callit( self._object, format,*args )

    def truncate(  self, len, ):

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_truncate( self._object,len ) or POINTER(c_void_p)())

    def append(  self, val, ):

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_append( self._object,val ) or POINTER(c_void_p)())

    def prepend(  self, val, ):

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_prepend( self._object,val ) or POINTER(c_void_p)())

    def append_unichar(  self, wc, ):
        if wc: wc = wc._object
        else: wc = POINTER(c_void_p)()

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_append_unichar( self._object,wc ) or POINTER(c_void_p)())

    def prepend_unichar(  self, wc, ):
        if wc: wc = wc._object
        else: wc = POINTER(c_void_p)()

        from .gobject import GString
        return GString(None, obj=libgobject.g_string_prepend_unichar( self._object,wc ) or POINTER(c_void_p)())

    def insert_len(  self, pos, val, len, ):

        from .gobject import GString
        return GString(None,None,None, obj=libgobject.g_string_insert_len( self._object,pos,val,len ) or POINTER(c_void_p)())

    def overwrite(  self, pos, val, ):

        from .gobject import GString
        return GString(None,None, obj=libgobject.g_string_overwrite( self._object,pos,val ) or POINTER(c_void_p)())

    def insert_c(  self, pos, c, ):

        from .gobject import GString
        return GString(None,None, obj=libgobject.g_string_insert_c( self._object,pos,c ) or POINTER(c_void_p)())

    def hash(  self, ):

        
        return libgobject.g_string_hash( self._object )

    def insert_unichar(  self, pos, wc, ):
        if wc: wc = wc._object
        else: wc = POINTER(c_void_p)()

        from .gobject import GString
        return GString(None,None, obj=libgobject.g_string_insert_unichar( self._object,pos,wc ) or POINTER(c_void_p)())

    @staticmethod
    def new_len( init, len,):
        from .gobject import GString
        return GString(None, obj=    libgobject.g_string_new_len(init, len, )
 or POINTER(c_void_p)())
