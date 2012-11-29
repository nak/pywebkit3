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

class GSList( object):
    """Class GSList Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def g_slist_insert_before(  self, sibling, data, ):
        if sibling: sibling = sibling._object
        else: sibling = POINTER(c_int)()

        libgobject.g_slist_insert_before.restype = _GSList
        libgobject.g_slist_insert_before.argtypes = [_GSList,_GSList,gpointer]
        from gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_insert_before( self._object,sibling,data ) or POINTER(c_int)())

    def g_slist_free(  self, ):

        libgobject.g_slist_free.argtypes = [_GSList]
        
        libgobject.g_slist_free( self._object )

    def g_slist_insert_sorted_with_data(  self, data, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgobject.g_slist_insert_sorted_with_data.restype = _GSList
        libgobject.g_slist_insert_sorted_with_data.argtypes = [_GSList,gpointer,GCompareDataFunc,gpointer]
        from gobject import GSList
        return GSList(None,None,None, obj=libgobject.g_slist_insert_sorted_with_data( self._object,data,func,user_data ) or POINTER(c_int)())

    def g_slist_copy(  self, ):

        libgobject.g_slist_copy.restype = _GSList
        libgobject.g_slist_copy.argtypes = [_GSList]
        from gobject import GSList
        return GSList( obj=libgobject.g_slist_copy( self._object ) or POINTER(c_int)())

    def g_slist_concat(  self, list2, ):
        if list2: list2 = list2._object
        else: list2 = POINTER(c_int)()

        libgobject.g_slist_concat.restype = _GSList
        libgobject.g_slist_concat.argtypes = [_GSList,_GSList]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_concat( self._object,list2 ) or POINTER(c_int)())

    def g_slist_nth(  self, n, ):

        libgobject.g_slist_nth.restype = _GSList
        libgobject.g_slist_nth.argtypes = [_GSList,guint]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_nth( self._object,n ) or POINTER(c_int)())

    def g_slist_free_full(  self, free_func, ):

        libgobject.g_slist_free_full.argtypes = [_GSList,GDestroyNotify]
        
        libgobject.g_slist_free_full( self._object,free_func )

    def g_slist_position(  self, llink, ):
        if llink: llink = llink._object
        else: llink = POINTER(c_int)()

        libgobject.g_slist_position.restype = gint
        libgobject.g_slist_position.argtypes = [_GSList,_GSList]
        
        return libgobject.g_slist_position( self._object,llink )

    def g_slist_remove(  self, data, ):

        libgobject.g_slist_remove.restype = _GSList
        libgobject.g_slist_remove.argtypes = [_GSList,gpointer]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_remove( self._object,data ) or POINTER(c_int)())

    def g_slist_insert(  self, data, position, ):

        libgobject.g_slist_insert.restype = _GSList
        libgobject.g_slist_insert.argtypes = [_GSList,gpointer,gint]
        from gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_insert( self._object,data,position ) or POINTER(c_int)())

    def g_slist_last(  self, ):

        libgobject.g_slist_last.restype = _GSList
        libgobject.g_slist_last.argtypes = [_GSList]
        from gobject import GSList
        return GSList( obj=libgobject.g_slist_last( self._object ) or POINTER(c_int)())

    def g_slist_reverse(  self, ):

        libgobject.g_slist_reverse.restype = _GSList
        libgobject.g_slist_reverse.argtypes = [_GSList]
        from gobject import GSList
        return GSList( obj=libgobject.g_slist_reverse( self._object ) or POINTER(c_int)())

    def g_slist_find_custom(  self, data, func, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgobject.g_slist_find_custom.restype = _GSList
        libgobject.g_slist_find_custom.argtypes = [_GSList,gpointer,GCompareFunc]
        from gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_find_custom( self._object,data,func ) or POINTER(c_int)())

    def g_slist_sort(  self, compare_func, ):
        if compare_func: compare_func = compare_func._object
        else: compare_func = POINTER(c_int)()

        libgobject.g_slist_sort.restype = _GSList
        libgobject.g_slist_sort.argtypes = [_GSList,GCompareFunc]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_sort( self._object,compare_func ) or POINTER(c_int)())

    def g_slist_delete_link(  self, link_, ):
        if link_: link_ = link_._object
        else: link_ = POINTER(c_int)()

        libgobject.g_slist_delete_link.restype = _GSList
        libgobject.g_slist_delete_link.argtypes = [_GSList,_GSList]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_delete_link( self._object,link_ ) or POINTER(c_int)())

    def g_slist_length(  self, ):

        libgobject.g_slist_length.restype = guint
        libgobject.g_slist_length.argtypes = [_GSList]
        
        return libgobject.g_slist_length( self._object )

    def g_slist_free_1(  self, ):

        libgobject.g_slist_free_1.argtypes = [_GSList]
        
        libgobject.g_slist_free_1( self._object )

    def g_slist_insert_sorted(  self, data, func, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgobject.g_slist_insert_sorted.restype = _GSList
        libgobject.g_slist_insert_sorted.argtypes = [_GSList,gpointer,GCompareFunc]
        from gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_insert_sorted( self._object,data,func ) or POINTER(c_int)())

    def g_slist_remove_all(  self, data, ):

        libgobject.g_slist_remove_all.restype = _GSList
        libgobject.g_slist_remove_all.argtypes = [_GSList,gpointer]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_remove_all( self._object,data ) or POINTER(c_int)())

    def g_slist_sort_with_data(  self, compare_func, user_data, ):
        if compare_func: compare_func = compare_func._object
        else: compare_func = POINTER(c_int)()

        libgobject.g_slist_sort_with_data.restype = _GSList
        libgobject.g_slist_sort_with_data.argtypes = [_GSList,GCompareDataFunc,gpointer]
        from gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_sort_with_data( self._object,compare_func,user_data ) or POINTER(c_int)())

    def g_slist_find(  self, data, ):

        libgobject.g_slist_find.restype = _GSList
        libgobject.g_slist_find.argtypes = [_GSList,gpointer]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_find( self._object,data ) or POINTER(c_int)())

    def g_slist_append(  self, data, ):

        libgobject.g_slist_append.restype = _GSList
        libgobject.g_slist_append.argtypes = [_GSList,gpointer]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_append( self._object,data ) or POINTER(c_int)())

    def g_slist_remove_link(  self, link_, ):
        if link_: link_ = link_._object
        else: link_ = POINTER(c_int)()

        libgobject.g_slist_remove_link.restype = _GSList
        libgobject.g_slist_remove_link.argtypes = [_GSList,_GSList]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_remove_link( self._object,link_ ) or POINTER(c_int)())

    def g_slist_copy_deep(  self, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgobject.g_slist_copy_deep.restype = _GSList
        libgobject.g_slist_copy_deep.argtypes = [_GSList,GCopyFunc,gpointer]
        from gobject import GSList
        return GSList(None,None, obj=libgobject.g_slist_copy_deep( self._object,func,user_data ) or POINTER(c_int)())

    def g_slist_prepend(  self, data, ):

        libgobject.g_slist_prepend.restype = _GSList
        libgobject.g_slist_prepend.argtypes = [_GSList,gpointer]
        from gobject import GSList
        return GSList(None, obj=libgobject.g_slist_prepend( self._object,data ) or POINTER(c_int)())

    def g_slist_index(  self, data, ):

        libgobject.g_slist_index.restype = gint
        libgobject.g_slist_index.argtypes = [_GSList,gpointer]
        
        return libgobject.g_slist_index( self._object,data )

    def g_slist_nth_data(  self, n, ):

        libgobject.g_slist_nth_data.restype = gpointer
        libgobject.g_slist_nth_data.argtypes = [_GSList,guint]
        
        return libgobject.g_slist_nth_data( self._object,n )

    def g_slist_foreach(  self, func, user_data, ):
        if func: func = func._object
        else: func = POINTER(c_int)()

        libgobject.g_slist_foreach.argtypes = [_GSList,GFunc,gpointer]
        
        libgobject.g_slist_foreach( self._object,func,user_data )

    @staticmethod
    def g_slist_alloc():
        libgobject.g_slist_alloc.restype = _GSList
        from gobject import GSList
        return GSList( obj=    libgobject.g_slist_alloc()
 or POINTER(c_int)())
