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
    libgobject.g_main_context_find_source_by_funcs_user_data.restype = _GSource
    libgobject.g_main_context_find_source_by_funcs_user_data.argtypes = [_GMainContext,_GSourceFuncs,gpointer]
except:
   pass
try:
    libgobject.g_main_context_pending.restype = gboolean
    libgobject.g_main_context_pending.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_remove_poll.restype = None
    libgobject.g_main_context_remove_poll.argtypes = [_GMainContext,_GPollFD]
except:
   pass
try:
    libgobject.g_main_context_add_poll.restype = None
    libgobject.g_main_context_add_poll.argtypes = [_GMainContext,_GPollFD,gint]
except:
   pass
try:
    libgobject.g_main_context_query.restype = gint
    libgobject.g_main_context_query.argtypes = [_GMainContext,gint,POINTER(gint),_GPollFD,gint]
except:
   pass
try:
    libgobject.g_main_context_dispatch.restype = None
    libgobject.g_main_context_dispatch.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_push_thread_default.restype = None
    libgobject.g_main_context_push_thread_default.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_invoke.restype = None
    libgobject.g_main_context_invoke.argtypes = [_GMainContext,GSourceFunc,gpointer]
except:
   pass
try:
    libgobject.g_main_context_find_source_by_id.restype = _GSource
    libgobject.g_main_context_find_source_by_id.argtypes = [_GMainContext,guint]
except:
   pass
try:
    libgobject.g_main_context_check.restype = gint
    libgobject.g_main_context_check.argtypes = [_GMainContext,gint,_GPollFD,gint]
except:
   pass
try:
    libgobject.g_main_context_prepare.restype = gboolean
    libgobject.g_main_context_prepare.argtypes = [_GMainContext,POINTER(gint)]
except:
   pass
try:
    libgobject.g_main_context_get_poll_func.restype = GPollFunc
    libgobject.g_main_context_get_poll_func.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_pop_thread_default.restype = None
    libgobject.g_main_context_pop_thread_default.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_set_poll_func.restype = None
    libgobject.g_main_context_set_poll_func.argtypes = [_GMainContext,GPollFunc]
except:
   pass
try:
    libgobject.g_main_context_wakeup.restype = None
    libgobject.g_main_context_wakeup.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_ref.restype = _GMainContext
    libgobject.g_main_context_ref.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_wait.restype = gboolean
    libgobject.g_main_context_wait.argtypes = [_GMainContext,_GCond,_GMutex]
except:
   pass
try:
    libgobject.g_main_context_acquire.restype = gboolean
    libgobject.g_main_context_acquire.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_release.restype = None
    libgobject.g_main_context_release.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_unref.restype = None
    libgobject.g_main_context_unref.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_is_owner.restype = gboolean
    libgobject.g_main_context_is_owner.argtypes = [_GMainContext]
except:
   pass
try:
    libgobject.g_main_context_iteration.restype = gboolean
    libgobject.g_main_context_iteration.argtypes = [_GMainContext,gboolean]
except:
   pass
try:
    libgobject.g_main_context_invoke_full.restype = None
    libgobject.g_main_context_invoke_full.argtypes = [_GMainContext,gint,GSourceFunc,gpointer,GDestroyNotify]
except:
   pass
try:
    libgobject.g_main_context_find_source_by_user_data.restype = _GSource
    libgobject.g_main_context_find_source_by_user_data.argtypes = [_GMainContext,gpointer]
except:
   pass
try:
    libgobject.g_main_depth.restype = gint
    libgobject.g_main_depth.argtypes = []
except:
   pass
try:
    libgobject.g_idle_add.restype = guint
    libgobject.g_idle_add.argtypes = [GSourceFunc,gpointer]
except:
   pass
try:
    libgobject.g_timeout_add_seconds.restype = guint
    libgobject.g_timeout_add_seconds.argtypes = [guint,GSourceFunc,gpointer]
except:
   pass
try:
    libgobject.g_main_current_source.restype = _GSource
    libgobject.g_main_current_source.argtypes = []
except:
   pass
try:
    libgobject.g_idle_source_new.restype = _GSource
    libgobject.g_idle_source_new.argtypes = []
except:
   pass
try:
    libgobject.g_timeout_add_full.restype = guint
    libgobject.g_timeout_add_full.argtypes = [gint,guint,GSourceFunc,gpointer,GDestroyNotify]
except:
   pass
try:
    libgobject.g_main_context_default.restype = _GMainContext
    libgobject.g_main_context_default.argtypes = []
except:
   pass
try:
    libgobject.g_timeout_add.restype = guint
    libgobject.g_timeout_add.argtypes = [guint,GSourceFunc,gpointer]
except:
   pass
try:
    libgobject.g_idle_remove_by_data.restype = gboolean
    libgobject.g_idle_remove_by_data.argtypes = [gpointer]
except:
   pass
try:
    libgobject.g_child_watch_add_full.restype = guint
    libgobject.g_child_watch_add_full.argtypes = [gint,GPid,GChildWatchFunc,gpointer,GDestroyNotify]
except:
   pass
try:
    libgobject.g_timeout_source_new_seconds.restype = _GSource
    libgobject.g_timeout_source_new_seconds.argtypes = [guint]
except:
   pass
try:
    libgobject.g_timeout_add_seconds_full.restype = guint
    libgobject.g_timeout_add_seconds_full.argtypes = [gint,guint,GSourceFunc,gpointer,GDestroyNotify]
except:
   pass
try:
    libgobject.g_idle_add_full.restype = guint
    libgobject.g_idle_add_full.argtypes = [gint,GSourceFunc,gpointer,GDestroyNotify]
except:
   pass
try:
    libgobject.g_child_watch_add.restype = guint
    libgobject.g_child_watch_add.argtypes = [GPid,GChildWatchFunc,gpointer]
except:
   pass
try:
    libgobject.g_main_context_get_thread_default.restype = _GMainContext
    libgobject.g_main_context_get_thread_default.argtypes = []
except:
   pass
try:
    libgobject.g_main_context_ref_thread_default.restype = _GMainContext
    libgobject.g_main_context_ref_thread_default.argtypes = []
except:
   pass
from . import gobject__GObject
class GMainContext( gobject__GObject.GObject):
    """Class GMainContext Constructors"""
    def __init__( self, pid,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_child_watch_source_new.restype = POINTER(c_void_p)
            
            if pid : pid = pid._object
            else :  pid = POINTER(c_void_p)()

            libgobject.g_child_watch_source_new.argtypes = [GPid]
            self._object = libgobject.g_child_watch_source_new(pid, )

    """Methods"""
    def find_source_by_funcs_user_data(  self, funcs, user_data, ):
        if funcs: funcs = funcs._object
        else: funcs = POINTER(c_void_p)()

        from .gobject import GSource
        return GSource(None,None, obj=libgobject.g_main_context_find_source_by_funcs_user_data( self._object,funcs,user_data ) or POINTER(c_void_p)())

    def pending(  self, ):

        
        return libgobject.g_main_context_pending( self._object )

    def remove_poll(  self, fd, ):
        if fd: fd = fd._object
        else: fd = POINTER(c_void_p)()

        
        libgobject.g_main_context_remove_poll( self._object,fd )

    def add_poll(  self, fd, priority, ):
        if fd: fd = fd._object
        else: fd = POINTER(c_void_p)()

        
        libgobject.g_main_context_add_poll( self._object,fd,priority )

    def query(  self, max_priority, timeout_, fds, n_fds, ):
        if fds: fds = fds._object
        else: fds = POINTER(c_void_p)()

        
        return libgobject.g_main_context_query( self._object,max_priority,timeout_,fds,n_fds )

    def dispatch(  self, ):

        
        libgobject.g_main_context_dispatch( self._object )

    def push_thread_default(  self, ):

        
        libgobject.g_main_context_push_thread_default( self._object )

    def invoke(  self, function, data, ):

        
        libgobject.g_main_context_invoke( self._object,function,data )

    def find_source_by_id(  self, source_id, ):

        from .gobject import GSource
        return GSource(None, obj=libgobject.g_main_context_find_source_by_id( self._object,source_id ) or POINTER(c_void_p)())

    def check(  self, max_priority, fds, n_fds, ):
        if fds: fds = fds._object
        else: fds = POINTER(c_void_p)()

        
        return libgobject.g_main_context_check( self._object,max_priority,fds,n_fds )

    def prepare(  self, priority, ):

        
        return libgobject.g_main_context_prepare( self._object,priority )

    def get_poll_func(  self, ):

        
        return libgobject.g_main_context_get_poll_func( self._object )

    def pop_thread_default(  self, ):

        
        libgobject.g_main_context_pop_thread_default( self._object )

    def set_poll_func(  self, func, ):

        
        libgobject.g_main_context_set_poll_func( self._object,func )

    def wakeup(  self, ):

        
        libgobject.g_main_context_wakeup( self._object )

    def ref(  self, ):

        from .gobject import GMainContext
        return GMainContext( obj=libgobject.g_main_context_ref( self._object ) or POINTER(c_void_p)())

    def wait(  self, cond, mutex, ):
        if cond: cond = cond._object
        else: cond = POINTER(c_void_p)()
        if mutex: mutex = mutex._object
        else: mutex = POINTER(c_void_p)()

        
        return libgobject.g_main_context_wait( self._object,cond,mutex )

    def acquire(  self, ):

        
        return libgobject.g_main_context_acquire( self._object )

    def release(  self, ):

        
        libgobject.g_main_context_release( self._object )

    def unref(  self, ):

        
        libgobject.g_main_context_unref( self._object )

    def is_owner(  self, ):

        
        return libgobject.g_main_context_is_owner( self._object )

    def iteration(  self, may_block, ):

        
        return libgobject.g_main_context_iteration( self._object,may_block )

    def invoke_full(  self, priority, function, data, notify, ):

        
        libgobject.g_main_context_invoke_full( self._object,priority,function,data,notify )

    def find_source_by_user_data(  self, user_data, ):

        from .gobject import GSource
        return GSource(None, obj=libgobject.g_main_context_find_source_by_user_data( self._object,user_data ) or POINTER(c_void_p)())

    @staticmethod
    def g_main_depth():
        
        return     libgobject.g_main_depth()

    @staticmethod
    def g_idle_add( function, data,):
        
        return     libgobject.g_idle_add(function, data, )

    @staticmethod
    def g_timeout_add_seconds( interval, function, data,):
        
        return     libgobject.g_timeout_add_seconds(interval, function, data, )

    @staticmethod
    def g_main_current_source():
        from .gobject import GSource
        return GSource(None, obj=    libgobject.g_main_current_source()
 or POINTER(c_void_p)())
    @staticmethod
    def g_idle_source_new():
        from .gobject import GSource
        return GSource(None, obj=    libgobject.g_idle_source_new()
 or POINTER(c_void_p)())
    @staticmethod
    def g_timeout_add_full( priority, interval, function, data, notify,):
        
        return     libgobject.g_timeout_add_full(priority, interval, function, data, notify, )

    @staticmethod
    def default():
        from .gobject import GMainContext
        return GMainContext(None, obj=    libgobject.g_main_context_default()
 or POINTER(c_void_p)())
    @staticmethod
    def g_timeout_add( interval, function, data,):
        
        return     libgobject.g_timeout_add(interval, function, data, )

    @staticmethod
    def g_idle_remove_by_data( data,):
        
        return     libgobject.g_idle_remove_by_data(data, )

    @staticmethod
    def g_child_watch_add_full( priority, pid, function, data, notify,):
        if pid: pid = pid._object
        else: pid = POINTER(c_void_p)()
        if function: function = function._object
        else: function = POINTER(c_void_p)()
        
        return     libgobject.g_child_watch_add_full(priority, pid, function, data, notify, )

    @staticmethod
    def g_timeout_source_new_seconds( interval,):
        from .gobject import GSource
        return GSource(None, obj=    libgobject.g_timeout_source_new_seconds(interval, )
 or POINTER(c_void_p)())
    @staticmethod
    def g_timeout_add_seconds_full( priority, interval, function, data, notify,):
        
        return     libgobject.g_timeout_add_seconds_full(priority, interval, function, data, notify, )

    @staticmethod
    def g_idle_add_full( priority, function, data, notify,):
        
        return     libgobject.g_idle_add_full(priority, function, data, notify, )

    @staticmethod
    def g_child_watch_add( pid, function, data,):
        if pid: pid = pid._object
        else: pid = POINTER(c_void_p)()
        if function: function = function._object
        else: function = POINTER(c_void_p)()
        
        return     libgobject.g_child_watch_add(pid, function, data, )

    @staticmethod
    def get_thread_default():
        from .gobject import GMainContext
        return GMainContext(None, obj=    libgobject.g_main_context_get_thread_default()
 or POINTER(c_void_p)())
    @staticmethod
    def ref_thread_default():
        from .gobject import GMainContext
        return GMainContext(None, obj=    libgobject.g_main_context_ref_thread_default()
 or POINTER(c_void_p)())
