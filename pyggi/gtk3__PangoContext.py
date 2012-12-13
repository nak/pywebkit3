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
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
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
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
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

import gobject__GObject
class PangoContext( gobject__GObject.GObject):
    """Class PangoContext Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.pango_context_new.restype = POINTER(c_int)
            
            libgtk3.pango_context_new.argtypes = []
            self._object = libgtk3.pango_context_new()

    """Methods"""
    def pango_find_paragraph_boundary(  self, text, length, paragraph_delimiter_index, next_paragraph_start, ):

        libgtk3.pango_find_paragraph_boundary.argtypes = [_PangoContext,c_char_p,gint,POINTER(gint),POINTER(gint)]
        
        libgtk3.pango_find_paragraph_boundary( self._object,text,length,paragraph_delimiter_index,next_paragraph_start )

    def set_language(  self, language, ):
        if language: language = language._object
        else: language = POINTER(c_int)()

        libgtk3.pango_context_set_language.argtypes = [_PangoContext,_PangoLanguage]
        
        libgtk3.pango_context_set_language( self._object,language )

    def pango_itemize(  self, text, start_index, length, attrs, cached_iter, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()
        if cached_iter: cached_iter = cached_iter._object
        else: cached_iter = POINTER(c_int)()

        libgtk3.pango_itemize.restype = _GList
        libgtk3.pango_itemize.argtypes = [_PangoContext,c_char_p,int,int,_PangoAttrList,_PangoAttrIterator]
        from gobject import GList
        return GList( obj=libgtk3.pango_itemize( self._object,text,start_index,length,attrs,cached_iter ) or POINTER(c_int)())

    def pango_shape_full(  self, item_text, item_length, paragraph_text, paragraph_length, analysis, glyphs, ):
        if analysis: analysis = analysis._object
        else: analysis = POINTER(c_int)()
        if glyphs: glyphs = glyphs._object
        else: glyphs = POINTER(c_int)()

        libgtk3.pango_shape_full.argtypes = [_PangoContext,c_char_p,gint,c_char_p,gint,_PangoAnalysis,_PangoGlyphString]
        
        libgtk3.pango_shape_full( self._object,item_text,item_length,paragraph_text,paragraph_length,analysis,glyphs )

    def set_base_dir(  self, direction, ):

        libgtk3.pango_context_set_base_dir.argtypes = [_PangoContext,PangoDirection]
        
        libgtk3.pango_context_set_base_dir( self._object,direction )

    def pango_get_log_attrs(  self, text, length, level, language, log_attrs, attrs_len, ):
        if language: language = language._object
        else: language = POINTER(c_int)()
        if log_attrs: log_attrs = log_attrs._object
        else: log_attrs = POINTER(c_int)()

        libgtk3.pango_get_log_attrs.argtypes = [_PangoContext,c_char_p,int,int,_PangoLanguage,_PangoLogAttr,int]
        
        libgtk3.pango_get_log_attrs( self._object,text,length,level,language,log_attrs,attrs_len )

    def set_matrix(  self, matrix, ):
        if matrix: matrix = matrix._object
        else: matrix = POINTER(c_int)()

        libgtk3.pango_context_set_matrix.argtypes = [_PangoContext,_PangoMatrix]
        
        libgtk3.pango_context_set_matrix( self._object,matrix )

    def get_matrix(  self, ):

        libgtk3.pango_context_get_matrix.restype = _PangoMatrix
        libgtk3.pango_context_get_matrix.argtypes = [_PangoContext]
        from gtk3 import PangoMatrix
        return PangoMatrix( obj=libgtk3.pango_context_get_matrix( self._object )  or POINTER(c_int)())

    def set_font_description(  self, desc, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()

        libgtk3.pango_context_set_font_description.argtypes = [_PangoContext,_PangoFontDescription]
        
        libgtk3.pango_context_set_font_description( self._object,desc )

    def get_base_gravity(  self, ):

        libgtk3.pango_context_get_base_gravity.restype = PangoGravity
        libgtk3.pango_context_get_base_gravity.argtypes = [_PangoContext]
        
        return libgtk3.pango_context_get_base_gravity( self._object )

    def load_fontset(  self, desc, language, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()
        if language: language = language._object
        else: language = POINTER(c_int)()

        libgtk3.pango_context_load_fontset.restype = _PangoFontset
        libgtk3.pango_context_load_fontset.argtypes = [_PangoContext,_PangoFontDescription,_PangoLanguage]
        from gtk3 import PangoFontset
        return PangoFontset( obj=libgtk3.pango_context_load_fontset( self._object,desc,language )  or POINTER(c_int)())

    def pango_default_break(  self, text, length, analysis, attrs, attrs_len, ):
        if analysis: analysis = analysis._object
        else: analysis = POINTER(c_int)()
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        libgtk3.pango_default_break.argtypes = [_PangoContext,c_char_p,int,_PangoAnalysis,_PangoLogAttr,int]
        
        libgtk3.pango_default_break( self._object,text,length,analysis,attrs,attrs_len )

    def set_base_gravity(  self, gravity, ):

        libgtk3.pango_context_set_base_gravity.argtypes = [_PangoContext,PangoGravity]
        
        libgtk3.pango_context_set_base_gravity( self._object,gravity )

    def pango_itemize_with_base_dir(  self, base_dir, text, start_index, length, attrs, cached_iter, ):
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()
        if cached_iter: cached_iter = cached_iter._object
        else: cached_iter = POINTER(c_int)()

        libgtk3.pango_itemize_with_base_dir.restype = _GList
        libgtk3.pango_itemize_with_base_dir.argtypes = [_PangoContext,PangoDirection,c_char_p,int,int,_PangoAttrList,_PangoAttrIterator]
        from gobject import GList
        return GList( obj=libgtk3.pango_itemize_with_base_dir( self._object,base_dir,text,start_index,length,attrs,cached_iter ) or POINTER(c_int)())

    def list_families(  self, families, n_families, ):
        if families: families = families._object
        else: families = POINTER(c_int)()

        libgtk3.pango_context_list_families.argtypes = [_PangoContext,POINTER(_PangoFontFamily),POINTER(int)]
        
        libgtk3.pango_context_list_families( self._object,families,n_families )

    def set_font_map(  self, font_map, ):
        if font_map: font_map = font_map._object
        else: font_map = POINTER(c_int)()

        libgtk3.pango_context_set_font_map.argtypes = [_PangoContext,_PangoFontMap]
        
        libgtk3.pango_context_set_font_map( self._object,font_map )

    def get_language(  self, ):

        libgtk3.pango_context_get_language.restype = _PangoLanguage
        libgtk3.pango_context_get_language.argtypes = [_PangoContext]
        from gtk3 import PangoLanguage
        return PangoLanguage( obj=libgtk3.pango_context_get_language( self._object )  or POINTER(c_int)())

    def get_font_map(  self, ):

        libgtk3.pango_context_get_font_map.restype = _PangoFontMap
        libgtk3.pango_context_get_font_map.argtypes = [_PangoContext]
        from gtk3 import PangoFontMap
        return PangoFontMap( obj=libgtk3.pango_context_get_font_map( self._object )  or POINTER(c_int)())

    def pango_shape(  self, text, length, analysis, glyphs, ):
        if analysis: analysis = analysis._object
        else: analysis = POINTER(c_int)()
        if glyphs: glyphs = glyphs._object
        else: glyphs = POINTER(c_int)()

        libgtk3.pango_shape.argtypes = [_PangoContext,c_char_p,gint,_PangoAnalysis,_PangoGlyphString]
        
        libgtk3.pango_shape( self._object,text,length,analysis,glyphs )

    def get_base_dir(  self, ):

        libgtk3.pango_context_get_base_dir.restype = PangoDirection
        libgtk3.pango_context_get_base_dir.argtypes = [_PangoContext]
        
        return libgtk3.pango_context_get_base_dir( self._object )

    def set_gravity_hint(  self, hint, ):

        libgtk3.pango_context_set_gravity_hint.argtypes = [_PangoContext,PangoGravityHint]
        
        libgtk3.pango_context_set_gravity_hint( self._object,hint )

    def get_gravity(  self, ):

        libgtk3.pango_context_get_gravity.restype = PangoGravity
        libgtk3.pango_context_get_gravity.argtypes = [_PangoContext]
        
        return libgtk3.pango_context_get_gravity( self._object )

    def get_font_description(  self, ):

        libgtk3.pango_context_get_font_description.restype = _PangoFontDescription
        libgtk3.pango_context_get_font_description.argtypes = [_PangoContext]
        from gtk3 import PangoFontDescription
        return PangoFontDescription(None, obj=libgtk3.pango_context_get_font_description( self._object )  or POINTER(c_int)())

    def get_metrics(  self, desc, language, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()
        if language: language = language._object
        else: language = POINTER(c_int)()

        libgtk3.pango_context_get_metrics.restype = _PangoFontMetrics
        libgtk3.pango_context_get_metrics.argtypes = [_PangoContext,_PangoFontDescription,_PangoLanguage]
        from gtk3 import PangoFontMetrics
        return PangoFontMetrics( obj=libgtk3.pango_context_get_metrics( self._object,desc,language )  or POINTER(c_int)())

    def get_gravity_hint(  self, ):

        libgtk3.pango_context_get_gravity_hint.restype = PangoGravityHint
        libgtk3.pango_context_get_gravity_hint.argtypes = [_PangoContext]
        
        return libgtk3.pango_context_get_gravity_hint( self._object )

    def pango_break(  self, text, length, analysis, attrs, attrs_len, ):
        if analysis: analysis = analysis._object
        else: analysis = POINTER(c_int)()
        if attrs: attrs = attrs._object
        else: attrs = POINTER(c_int)()

        libgtk3.pango_break.argtypes = [_PangoContext,c_char_p,int,_PangoAnalysis,_PangoLogAttr,int]
        
        libgtk3.pango_break( self._object,text,length,analysis,attrs,attrs_len )

    def load_font(  self, desc, ):
        if desc: desc = desc._object
        else: desc = POINTER(c_int)()

        libgtk3.pango_context_load_font.restype = _PangoFont
        libgtk3.pango_context_load_font.argtypes = [_PangoContext,_PangoFontDescription]
        from gtk3 import PangoFont
        return PangoFont( obj=libgtk3.pango_context_load_font( self._object,desc )  or POINTER(c_int)())

    @staticmethod
    def pango_reorder_items( logical_items,):
        if logical_items: logical_items = logical_items._object
        else: logical_items = POINTER(c_int)()
        libgtk3.pango_reorder_items.restype = _GList
        libgtk3.pango_reorder_items.argtypes = [_GList]
        from gobject import GList
        return GList( obj=    libgtk3.pango_reorder_items(logical_items, )
 or POINTER(c_int)())
