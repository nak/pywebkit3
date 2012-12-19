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
from pango_types import *
from pango_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
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

try:
    libpango.pango_layout_iter_next_char.restype = gboolean
    libpango.pango_layout_iter_next_char.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_next_run.restype = gboolean
    libpango.pango_layout_iter_next_run.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_line_yrange.restype = None
    libpango.pango_layout_iter_get_line_yrange.argtypes = [_PangoLayoutIter,POINTER(int),POINTER(int)]
except:
   pass
try:
    libpango.pango_layout_iter_get_char_extents.restype = None
    libpango.pango_layout_iter_get_char_extents.argtypes = [_PangoLayoutIter,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_iter_get_cluster_extents.restype = None
    libpango.pango_layout_iter_get_cluster_extents.argtypes = [_PangoLayoutIter,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_iter_at_last_line.restype = gboolean
    libpango.pango_layout_iter_at_last_line.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_line.restype = _PangoLayoutLine
    libpango.pango_layout_iter_get_line.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_free.restype = None
    libpango.pango_layout_iter_free.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_line_readonly.restype = _PangoLayoutLine
    libpango.pango_layout_iter_get_line_readonly.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_index.restype = int
    libpango.pango_layout_iter_get_index.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_layout.restype = _PangoLayout
    libpango.pango_layout_iter_get_layout.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_run_extents.restype = None
    libpango.pango_layout_iter_get_run_extents.argtypes = [_PangoLayoutIter,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_iter_next_line.restype = gboolean
    libpango.pango_layout_iter_next_line.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_run_readonly.restype = _PangoLayoutRun
    libpango.pango_layout_iter_get_run_readonly.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_copy.restype = _PangoLayoutIter
    libpango.pango_layout_iter_copy.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_next_cluster.restype = gboolean
    libpango.pango_layout_iter_next_cluster.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_run.restype = _PangoLayoutRun
    libpango.pango_layout_iter_get_run.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_baseline.restype = int
    libpango.pango_layout_iter_get_baseline.argtypes = [_PangoLayoutIter]
except:
   pass
try:
    libpango.pango_layout_iter_get_line_extents.restype = None
    libpango.pango_layout_iter_get_line_extents.argtypes = [_PangoLayoutIter,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_iter_get_layout_extents.restype = None
    libpango.pango_layout_iter_get_layout_extents.argtypes = [_PangoLayoutIter,_PangoRectangle,_PangoRectangle]
except:
   pass
try:
    libpango.pango_layout_get_iter.restype = _PangoLayoutIter
    libpango.pango_layout_get_iter.argtypes = [_PangoLayout]
except:
   pass
import gobject__GBoxed
class PangoLayoutIter( gobject__GBoxed.GBoxed):
    """Class PangoLayoutIter Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def next_char(  self, ):

        
        return libpango.pango_layout_iter_next_char( self._object )

    def next_run(  self, ):

        
        return libpango.pango_layout_iter_next_run( self._object )

    def get_line_yrange(  self, y0_, y1_, ):

        
        libpango.pango_layout_iter_get_line_yrange( self._object,y0_,y1_ )

    def get_char_extents(  self, logical_rect, ):
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        
        libpango.pango_layout_iter_get_char_extents( self._object,logical_rect )

    def get_cluster_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_int)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        
        libpango.pango_layout_iter_get_cluster_extents( self._object,ink_rect,logical_rect )

    def at_last_line(  self, ):

        
        return libpango.pango_layout_iter_at_last_line( self._object )

    def get_line(  self, ):

        from gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libpango.pango_layout_iter_get_line( self._object )  or POINTER(c_int)())

    def free(  self, ):

        
        libpango.pango_layout_iter_free( self._object )

    def get_line_readonly(  self, ):

        from gtk3 import PangoLayoutLine
        return PangoLayoutLine( obj=libpango.pango_layout_iter_get_line_readonly( self._object )  or POINTER(c_int)())

    def get_index(  self, ):

        
        return libpango.pango_layout_iter_get_index( self._object )

    def get_layout(  self, ):

        from gtk3 import PangoLayout
        return PangoLayout(None,None, obj=libpango.pango_layout_iter_get_layout( self._object )  or POINTER(c_int)())

    def get_run_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_int)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        
        libpango.pango_layout_iter_get_run_extents( self._object,ink_rect,logical_rect )

    def next_line(  self, ):

        
        return libpango.pango_layout_iter_next_line( self._object )

    def get_run_readonly(  self, ):

        from gtk3 import PangoLayoutRun
        return PangoLayoutRun( obj=libpango.pango_layout_iter_get_run_readonly( self._object )  or POINTER(c_int)())

    def copy(  self, ):

        from gtk3 import PangoLayoutIter
        return PangoLayoutIter( obj=libpango.pango_layout_iter_copy( self._object )  or POINTER(c_int)())

    def next_cluster(  self, ):

        
        return libpango.pango_layout_iter_next_cluster( self._object )

    def get_run(  self, ):

        from gtk3 import PangoLayoutRun
        return PangoLayoutRun( obj=libpango.pango_layout_iter_get_run( self._object )  or POINTER(c_int)())

    def get_baseline(  self, ):

        
        return libpango.pango_layout_iter_get_baseline( self._object )

    def get_line_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_int)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        
        libpango.pango_layout_iter_get_line_extents( self._object,ink_rect,logical_rect )

    def get_layout_extents(  self, ink_rect, logical_rect, ):
        if ink_rect: ink_rect = ink_rect._object
        else: ink_rect = POINTER(c_int)()
        if logical_rect: logical_rect = logical_rect._object
        else: logical_rect = POINTER(c_int)()

        
        libpango.pango_layout_iter_get_layout_extents( self._object,ink_rect,logical_rect )

    @staticmethod
    def pango_layout_get_iter( layout,):
        if layout: layout = layout._object
        else: layout = POINTER(c_int)()
        from gtk3 import PangoLayoutIter
        return PangoLayoutIter( obj=    libpango.pango_layout_get_iter(layout, )
  or POINTER(c_int)())
