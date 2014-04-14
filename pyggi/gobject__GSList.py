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
_GtkIconSet = POINTER(c_int)
_GtkIconTheme = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAccelLabel = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GFileAttributeMatcher = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
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

try:
    libgobject.g_slist_insert_before.restype = _GSList
    libgobject.g_slist_insert_before.argtypes = [_GSList,_GSList,gpointer]
except:
   pass
try:
    libgobject.g_slist_free.restype = None
    libgobject.g_slist_free.argtypes = [_GSList]
except:
   pass
try:
    libgobject.g_slist_insert_sorted_with_data.restype = _GSList
    libgobject.g_slist_insert_sorted_with_data.argtypes = [_GSList,gpointer,GCompareDataFunc,gpointer]
except:
   pass
try:
    libgobject.g_slist_copy.restype = _GSList
    libgobject.g_slist_copy.argtypes = [_GSList]
except:
   pass
try:
    libgobject.g_slist_concat.restype = _GSList
    libgobject.g_slist_concat.argtypes = [_GSList,_GSList]
except:
   pass
try:
    libgobject.g_slist_nth.restype = _GSList
    libgobject.g_slist_nth.argtypes = [_GSList,guint]
except:
   pass
try:
    libgobject.g_slist_free_full.restype = None
    libgobject.g_slist_free_full.argtypes = [_GSList,GDestroyNotify]
except:
   pass
try:
    libgobject.g_slist_position.restype = gint
    libgobject.g_slist_position.argtypes = [_GSList,_GSList]
except:
   pass
try:
    libgobject.g_slist_remove.restype = _GSList
    libgobject.g_slist_remove.argtypes = [_GSList,gconstpointer]
except:
   pass
try:
    libgobject.g_slist_insert.restype = _GSList
    libgobject.g_slist_insert.argtypes = [_GSList,gpointer,gint]
except:
   pass
try:
    libgobject.g_slist_last.restype = _GSList
    libgobject.g_slist_last.argtypes = [_GSList]
except:
   pass
try:
    libgobject.g_slist_reverse.restype = _GSList
    libgobject.g_slist_reverse.argtypes = [_GSList]
except:
   pass
try:
    libgobject.g_slist_find_custom.restype = _GSList
    libgobject.g_slist_find_custom.argtypes = [_GSList,gconstpointer,GCompareFunc]
except:
   pass
try:
    libgobject.g_slist_sort.restype = _GSList
    libgobject.g_slist_sort.argtypes = [_GSList,GCompareFunc]
except:
   pass
try:
    libgobject.g_slist_delete_link.restype = _GSList
    libgobject.g_slist_delete_link.argtypes = [_GSList,_GSList]
except:
   pass
try:
    libgobject.g_slist_length.restype = guint
    libgobject.g_slist_length.argtypes = [_GSList]
except:
   pass
try:
    libgobject.g_slist_free_1.restype = None
    libgobject.g_slist_free_1.argtypes = [_GSList]
except:
   pass
try:
    libgobject.g_slist_insert_sorted.restype = _GSList
    libgobject.g_slist_insert_sorted.argtypes = [_GSList,gpointer,GCompareFunc]
except:
   pass
try:
    libgobject.g_slist_remove_all.restype = _GSList
    libgobject.g_slist_remove_all.argtypes = [_GSList,gconstpointer]
except:
   pass
try:
    libgobject.g_slist_sort_with_data.restype = _GSList
    libgobject.g_slist_sort_with_data.argtypes = [_GSList,GCompareDataFunc,gpointer]
except:
   pass
try:
    libgobject.g_slist_find.restype = _GSList
    libgobject.g_slist_find.argtypes = [_GSList,gconstpointer]
except:
   pass
try:
    libgobject.g_slist_append.restype = _GSList
    libgobject.g_slist_append.argtypes = [_GSList,gpointer]
except:
   pass
try:
    libgobject.g_slist_remove_link.restype = _GSList
    libgobject.g_slist_remove_link.argtypes = [_GSList,_GSList]
except:
   pass
try:
    libgobject.g_slist_copy_deep.restype = _GSList
    libgobject.g_slist_copy_deep.argtypes = [_GSList,GCopyFunc,gpointer]
except:
   pass
try:
    libgobject.g_slist_prepend.restype = _GSList
    libgobject.g_slist_prepend.argtypes = [_GSList,gpointer]
except:
   pass
try:
    libgobject.g_slist_index.restype = gint
    libgobject.g_slist_index.argtypes = [_GSList,gconstpointer]
except:
   pass
try:
    libgobject.g_slist_nth_data.restype = gpointer
    libgobject.g_slist_nth_data.argtypes = [_GSList,guint]
except:
   pass
try:
    libgobject.g_slist_foreach.restype = None
    libgobject.g_slist_foreach.argtypes = [_GSList,GFunc,gpointer]
except:
   pass
try:
    libgobject.g_slist_alloc.restype = _GSList
    libgobject.g_slist_alloc.argtypes = []
except:
   pass
class GSList( object):
    """Class GSList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def g_slist_insert_before(  self, sibling, data, ):
        if sibling: sibling = sibling._object
        else: sibling = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_insert_before( self._object,sibling,data ) or POINTER(c_int)())

    def g_slist_free(  self, ):

        
        libgobject.g_slist_free( self._object )

    def g_slist_insert_sorted_with_data(  self, data, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None,None,None, obj=libgobject.g_slist_insert_sorted_with_data( self._object,data,func,user_data ) or POINTER(c_int)())

    def g_slist_copy(  self, ):

        from .gobject import GSList
        return GSList( obj=libgobject.g_slist_copy( self._object ) or POINTER(c_int)())

    def g_slist_concat(  self, list2, ):
        if list2: list2 = list2._object
        else: list2 = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_concat( self._object,list2 ) or POINTER(c_int)())

    def g_slist_nth(  self, n, ):

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_nth( self._object,n ) or POINTER(c_int)())

    def g_slist_free_full(  self, free_func, ):

        
        libgobject.g_slist_free_full( self._object,free_func )

    def g_slist_position(  self, llink, ):
        if llink: llink = llink._object
        else: llink = POINTER(c_int)()

        
        return libgobject.g_slist_position( self._object,llink )

    def g_slist_remove(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_remove( self._object,data ) or POINTER(c_int)())

    def g_slist_insert(  self, data, position, ):

        from .gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_insert( self._object,data,position ) or POINTER(c_int)())

    def g_slist_last(  self, ):

        from .gobject import GSList
        return GSList( obj=libgobject.g_slist_last( self._object ) or POINTER(c_int)())

    def g_slist_reverse(  self, ):

        from .gobject import GSList
        return GSList( obj=libgobject.g_slist_reverse( self._object ) or POINTER(c_int)())

    def g_slist_find_custom(  self, data, func, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_find_custom( self._object,data,func ) or POINTER(c_int)())

    def g_slist_sort(  self, compare_func, ):
        if compare_func: compare_func = compare_func._object
        else: compare_func = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_sort( self._object,compare_func ) or POINTER(c_int)())

    def g_slist_delete_link(  self, link_, ):
        if link_: link_ = link_._object
        else: link_ = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_delete_link( self._object,link_ ) or POINTER(c_int)())

    def g_slist_length(  self, ):

        
        return libgobject.g_slist_length( self._object )

    def g_slist_free_1(  self, ):

        
        libgobject.g_slist_free_1( self._object )

    def g_slist_insert_sorted(  self, data, func, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_insert_sorted( self._object,data,func ) or POINTER(c_int)())

    def g_slist_remove_all(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_remove_all( self._object,data ) or POINTER(c_int)())

    def g_slist_sort_with_data(  self, compare_func, user_data, ):
        if compare_func: compare_func = compare_func._object
        else: compare_func = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_sort_with_data( self._object,compare_func,user_data ) or POINTER(c_int)())

    def g_slist_find(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_find( self._object,data ) or POINTER(c_int)())

    def g_slist_append(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_append( self._object,data ) or POINTER(c_int)())

    def g_slist_remove_link(  self, link_, ):
        if link_: link_ = link_._object
        else: link_ = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_remove_link( self._object,link_ ) or POINTER(c_int)())

    def g_slist_copy_deep(  self, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        from .gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_copy_deep( self._object,func,user_data ) or POINTER(c_int)())

    def g_slist_prepend(  self, data, ):

        from .gobject import GSList
        return GSList(None, obj=libgobject.g_slist_prepend( self._object,data ) or POINTER(c_int)())

    def g_slist_index(  self, data, ):

        
        return libgobject.g_slist_index( self._object,data )

    def g_slist_nth_data(  self, n, ):

        
        return libgobject.g_slist_nth_data( self._object,n )

    def g_slist_foreach(  self, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        
        libgobject.g_slist_foreach( self._object,func,user_data )

    @staticmethod
    def g_slist_alloc():
        from .gobject import GSList
        return GSList( obj=    libgobject.g_slist_alloc()
 or POINTER(c_int)())
