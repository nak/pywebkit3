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
_GFileEnumerator = POINTER(c_int)
_GtkDialog = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_void = POINTER(c_int)
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
_cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
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
_PangoTabArray = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
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
    libgobject.g_source_remove_poll.restype = None
    libgobject.g_source_remove_poll.argtypes = [_GSource,_GPollFD]
except:
   pass
try:
    libgobject.g_source_set_callback_indirect.restype = None
    libgobject.g_source_set_callback_indirect.argtypes = [_GSource,gpointer,_GSourceCallbackFuncs]
except:
   pass
try:
    libgobject.g_source_destroy.restype = None
    libgobject.g_source_destroy.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_get_id.restype = guint
    libgobject.g_source_get_id.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_get_context.restype = _GMainContext
    libgobject.g_source_get_context.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_set_can_recurse.restype = None
    libgobject.g_source_set_can_recurse.argtypes = [_GSource,gboolean]
except:
   pass
try:
    libgobject.g_source_get_name.restype = c_char_p
    libgobject.g_source_get_name.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_get_priority.restype = gint
    libgobject.g_source_get_priority.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_ref.restype = _GSource
    libgobject.g_source_ref.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_remove_child_source.restype = None
    libgobject.g_source_remove_child_source.argtypes = [_GSource,_GSource]
except:
   pass
try:
    libgobject.g_source_add_child_source.restype = None
    libgobject.g_source_add_child_source.argtypes = [_GSource,_GSource]
except:
   pass
try:
    libgobject.g_source_set_name.restype = None
    libgobject.g_source_set_name.argtypes = [_GSource,Asciifier]
except:
   pass
try:
    libgobject.g_source_get_can_recurse.restype = gboolean
    libgobject.g_source_get_can_recurse.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_get_current_time.restype = None
    libgobject.g_source_get_current_time.argtypes = [_GSource,_GTimeVal]
except:
   pass
try:
    libgobject.g_source_is_destroyed.restype = gboolean
    libgobject.g_source_is_destroyed.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_unref.restype = None
    libgobject.g_source_unref.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_add_poll.restype = None
    libgobject.g_source_add_poll.argtypes = [_GSource,_GPollFD]
except:
   pass
try:
    libgobject.g_source_set_priority.restype = None
    libgobject.g_source_set_priority.argtypes = [_GSource,gint]
except:
   pass
try:
    libgobject.g_source_set_funcs.restype = None
    libgobject.g_source_set_funcs.argtypes = [_GSource,_GSourceFuncs]
except:
   pass
try:
    libgobject.g_source_get_time.restype = gint64
    libgobject.g_source_get_time.argtypes = [_GSource]
except:
   pass
try:
    libgobject.g_source_set_name_by_id.restype = None
    libgobject.g_source_set_name_by_id.argtypes = [_GSource,guint,Asciifier]
except:
   pass
try:
    libgobject.g_source_set_callback.restype = None
    libgobject.g_source_set_callback.argtypes = [_GSource,GSourceFunc,gpointer,GDestroyNotify]
except:
   pass
try:
    libgobject.g_source_attach.restype = guint
    libgobject.g_source_attach.argtypes = [_GSource,_GMainContext]
except:
   pass
try:
    libgobject.g_source_remove_by_user_data.restype = gboolean
    libgobject.g_source_remove_by_user_data.argtypes = [gpointer]
except:
   pass
try:
    libgobject.g_source_remove.restype = gboolean
    libgobject.g_source_remove.argtypes = [guint]
except:
   pass
try:
    libgobject.g_source_remove_by_funcs_user_data.restype = gboolean
    libgobject.g_source_remove_by_funcs_user_data.argtypes = [_GSourceFuncs,gpointer]
except:
   pass
from . import gobject__GObject
class GSource( gobject__GObject.GObject):
    """Class GSource Constructors"""
    def __init__( self, struct_size,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_source_new.restype = POINTER(c_int)
            
            libgobject.g_source_new.argtypes = [guint]
            self._object = libgobject.g_source_new(struct_size, )

    """Methods"""
    def remove_poll(  self, fd, ):
        if fd: fd = fd._object
        else: fd = POINTER(c_int)()

        
        libgobject.g_source_remove_poll( self._object,fd )

    def set_callback_indirect(  self, callback_data, callback_funcs, ):
        if callback_funcs: callback_funcs = callback_funcs._object
        else: callback_funcs = POINTER(c_int)()

        
        libgobject.g_source_set_callback_indirect( self._object,callback_data,callback_funcs )

    def destroy(  self, ):

        
        libgobject.g_source_destroy( self._object )

    def get_id(  self, ):

        
        return libgobject.g_source_get_id( self._object )

    def get_context(  self, ):

        from .gobject import GMainContext
        return GMainContext(None,None, obj=libgobject.g_source_get_context( self._object ) or POINTER(c_int)())

    def set_can_recurse(  self, can_recurse, ):

        
        libgobject.g_source_set_can_recurse( self._object,can_recurse )

    def get_name(  self, ):

        
        return libgobject.g_source_get_name( self._object )

    def get_priority(  self, ):

        
        return libgobject.g_source_get_priority( self._object )

    def ref(  self, ):

        from .gobject import GSource
        return GSource( obj=libgobject.g_source_ref( self._object ) or POINTER(c_int)())

    def remove_child_source(  self, child_source, ):
        if child_source: child_source = child_source._object
        else: child_source = POINTER(c_int)()

        
        libgobject.g_source_remove_child_source( self._object,child_source )

    def add_child_source(  self, child_source, ):
        if child_source: child_source = child_source._object
        else: child_source = POINTER(c_int)()

        
        libgobject.g_source_add_child_source( self._object,child_source )

    def set_name(  self, name, ):

        
        libgobject.g_source_set_name( self._object,name )

    def get_can_recurse(  self, ):

        
        return libgobject.g_source_get_can_recurse( self._object )

    def get_current_time(  self, timeval, ):
        if timeval: timeval = timeval._object
        else: timeval = POINTER(c_int)()

        
        libgobject.g_source_get_current_time( self._object,timeval )

    def is_destroyed(  self, ):

        
        return libgobject.g_source_is_destroyed( self._object )

    def unref(  self, ):

        
        libgobject.g_source_unref( self._object )

    def add_poll(  self, fd, ):
        if fd: fd = fd._object
        else: fd = POINTER(c_int)()

        
        libgobject.g_source_add_poll( self._object,fd )

    def set_priority(  self, priority, ):

        
        libgobject.g_source_set_priority( self._object,priority )

    def set_funcs(  self, funcs, ):
        if funcs: funcs = funcs._object
        else: funcs = POINTER(c_int)()

        
        libgobject.g_source_set_funcs( self._object,funcs )

    def get_time(  self, ):

        
        return libgobject.g_source_get_time( self._object )

    def set_name_by_id(  self, tag, name, ):

        
        libgobject.g_source_set_name_by_id( self._object,tag,name )

    def set_callback(  self, func, data, notify, ):

        
        libgobject.g_source_set_callback( self._object,func,data,notify )

    def attach(  self, context, ):
        if context: context = context._object
        else: context = POINTER(c_int)()

        
        return libgobject.g_source_attach( self._object,context )

    @staticmethod
    def remove_by_user_data( user_data,):
        
        return     libgobject.g_source_remove_by_user_data(user_data, )

    @staticmethod
    def remove( tag,):
        
        return     libgobject.g_source_remove(tag, )

    @staticmethod
    def remove_by_funcs_user_data( funcs, user_data,):
        if funcs: funcs = funcs._object
        else: funcs = POINTER(c_int)()
        
        return     libgobject.g_source_remove_by_funcs_user_data(funcs, user_data, )

