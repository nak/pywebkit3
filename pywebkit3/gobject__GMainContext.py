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

import gobject__GObject
class GMainContext( gobject__GObject.GObject):
    """Class GMainContext Constructors"""
    def __init__( self, pid,  obj = None):
        if obj: self._object = obj
        else:
            libgobject.g_child_watch_source_new.restype = POINTER(c_int)
            
            if pid : pid = pid._object
            else :  pid = POINTER(c_int)()

            libgobject.g_child_watch_source_new.argtypes = [GPid]
            self._object = libgobject.g_child_watch_source_new(pid, )

    """Methods"""
    def find_source_by_funcs_user_data(  self, funcs, user_data, ):
        if funcs: funcs = funcs._object
        else: funcs = POINTER(c_int)()

        libgobject.g_main_context_find_source_by_funcs_user_data.restype = _GSource
        libgobject.g_main_context_find_source_by_funcs_user_data.argtypes = [_GMainContext,_GSourceFuncs,gpointer]
        from gobject import GSource
        return GSource(None,None, obj=libgobject.g_main_context_find_source_by_funcs_user_data( self._object,funcs,user_data ) or POINTER(c_int)())

    def pending(  self, ):

        libgobject.g_main_context_pending.restype = gboolean
        libgobject.g_main_context_pending.argtypes = [_GMainContext]
        
        return libgobject.g_main_context_pending( self._object )

    def remove_poll(  self, fd, ):
        if fd: fd = fd._object
        else: fd = POINTER(c_int)()

        libgobject.g_main_context_remove_poll.argtypes = [_GMainContext,_GPollFD]
        
        libgobject.g_main_context_remove_poll( self._object,fd )

    def add_poll(  self, fd, priority, ):
        if fd: fd = fd._object
        else: fd = POINTER(c_int)()

        libgobject.g_main_context_add_poll.argtypes = [_GMainContext,_GPollFD,gint]
        
        libgobject.g_main_context_add_poll( self._object,fd,priority )

    def query(  self, max_priority, timeout_, fds, n_fds, ):
        if fds: fds = fds._object
        else: fds = POINTER(c_int)()

        libgobject.g_main_context_query.restype = gint
        libgobject.g_main_context_query.argtypes = [_GMainContext,gint,POINTER(gint),_GPollFD,gint]
        
        return libgobject.g_main_context_query( self._object,max_priority,timeout_,fds,n_fds )

    def dispatch(  self, ):

        libgobject.g_main_context_dispatch.argtypes = [_GMainContext]
        
        libgobject.g_main_context_dispatch( self._object )

    def push_thread_default(  self, ):

        libgobject.g_main_context_push_thread_default.argtypes = [_GMainContext]
        
        libgobject.g_main_context_push_thread_default( self._object )

    def invoke(  self, function, data, ):

        libgobject.g_main_context_invoke.argtypes = [_GMainContext,GSourceFunc,gpointer]
        
        libgobject.g_main_context_invoke( self._object,function,data )

    def find_source_by_id(  self, source_id, ):

        libgobject.g_main_context_find_source_by_id.restype = _GSource
        libgobject.g_main_context_find_source_by_id.argtypes = [_GMainContext,guint]
        from gobject import GSource
        return GSource(None, obj=libgobject.g_main_context_find_source_by_id( self._object,source_id ) or POINTER(c_int)())

    def check(  self, max_priority, fds, n_fds, ):
        if fds: fds = fds._object
        else: fds = POINTER(c_int)()

        libgobject.g_main_context_check.restype = gint
        libgobject.g_main_context_check.argtypes = [_GMainContext,gint,_GPollFD,gint]
        
        return libgobject.g_main_context_check( self._object,max_priority,fds,n_fds )

    def prepare(  self, priority, ):

        libgobject.g_main_context_prepare.restype = gboolean
        libgobject.g_main_context_prepare.argtypes = [_GMainContext,POINTER(gint)]
        
        return libgobject.g_main_context_prepare( self._object,priority )

    def get_poll_func(  self, ):

        libgobject.g_main_context_get_poll_func.restype = GPollFunc
        libgobject.g_main_context_get_poll_func.argtypes = [_GMainContext]
        
        return libgobject.g_main_context_get_poll_func( self._object )

    def pop_thread_default(  self, ):

        libgobject.g_main_context_pop_thread_default.argtypes = [_GMainContext]
        
        libgobject.g_main_context_pop_thread_default( self._object )

    def set_poll_func(  self, func, ):

        libgobject.g_main_context_set_poll_func.argtypes = [_GMainContext,GPollFunc]
        
        libgobject.g_main_context_set_poll_func( self._object,func )

    def wakeup(  self, ):

        libgobject.g_main_context_wakeup.argtypes = [_GMainContext]
        
        libgobject.g_main_context_wakeup( self._object )

    def ref(  self, ):

        libgobject.g_main_context_ref.restype = _GMainContext
        libgobject.g_main_context_ref.argtypes = [_GMainContext]
        from gobject import GMainContext
        return GMainContext( obj=libgobject.g_main_context_ref( self._object ) or POINTER(c_int)())

    def wait(  self, cond, mutex, ):
        if cond: cond = cond._object
        else: cond = POINTER(c_int)()
        if mutex: mutex = mutex._object
        else: mutex = POINTER(c_int)()

        libgobject.g_main_context_wait.restype = gboolean
        libgobject.g_main_context_wait.argtypes = [_GMainContext,_GCond,_GMutex]
        
        return libgobject.g_main_context_wait( self._object,cond,mutex )

    def acquire(  self, ):

        libgobject.g_main_context_acquire.restype = gboolean
        libgobject.g_main_context_acquire.argtypes = [_GMainContext]
        
        return libgobject.g_main_context_acquire( self._object )

    def release(  self, ):

        libgobject.g_main_context_release.argtypes = [_GMainContext]
        
        libgobject.g_main_context_release( self._object )

    def unref(  self, ):

        libgobject.g_main_context_unref.argtypes = [_GMainContext]
        
        libgobject.g_main_context_unref( self._object )

    def is_owner(  self, ):

        libgobject.g_main_context_is_owner.restype = gboolean
        libgobject.g_main_context_is_owner.argtypes = [_GMainContext]
        
        return libgobject.g_main_context_is_owner( self._object )

    def iteration(  self, may_block, ):

        libgobject.g_main_context_iteration.restype = gboolean
        libgobject.g_main_context_iteration.argtypes = [_GMainContext,gboolean]
        
        return libgobject.g_main_context_iteration( self._object,may_block )

    def invoke_full(  self, priority, function, data, notify, ):

        libgobject.g_main_context_invoke_full.argtypes = [_GMainContext,gint,GSourceFunc,gpointer,GDestroyNotify]
        
        libgobject.g_main_context_invoke_full( self._object,priority,function,data,notify )

    def find_source_by_user_data(  self, user_data, ):

        libgobject.g_main_context_find_source_by_user_data.restype = _GSource
        libgobject.g_main_context_find_source_by_user_data.argtypes = [_GMainContext,gpointer]
        from gobject import GSource
        return GSource(None, obj=libgobject.g_main_context_find_source_by_user_data( self._object,user_data ) or POINTER(c_int)())

    @staticmethod
    def g_main_depth():
        libgobject.g_main_depth.restype = gint
        
        return     libgobject.g_main_depth()

    @staticmethod
    def g_idle_add( function, data,):
        libgobject.g_idle_add.restype = guint
        libgobject.g_idle_add.argtypes = [GSourceFunc,gpointer]
        
        return     libgobject.g_idle_add(function, data, )

    @staticmethod
    def g_timeout_add_seconds( interval, function, data,):
        libgobject.g_timeout_add_seconds.restype = guint
        libgobject.g_timeout_add_seconds.argtypes = [guint,GSourceFunc,gpointer]
        
        return     libgobject.g_timeout_add_seconds(interval, function, data, )

    @staticmethod
    def g_main_current_source():
        libgobject.g_main_current_source.restype = _GSource
        from gobject import GSource
        return GSource(None, obj=    libgobject.g_main_current_source()
 or POINTER(c_int)())
    @staticmethod
    def g_idle_source_new():
        libgobject.g_idle_source_new.restype = _GSource
        from gobject import GSource
        return GSource(None, obj=    libgobject.g_idle_source_new()
 or POINTER(c_int)())
    @staticmethod
    def g_timeout_add_full( priority, interval, function, data, notify,):
        libgobject.g_timeout_add_full.restype = guint
        libgobject.g_timeout_add_full.argtypes = [gint,guint,GSourceFunc,gpointer,GDestroyNotify]
        
        return     libgobject.g_timeout_add_full(priority, interval, function, data, notify, )

    @staticmethod
    def default():
        libgobject.g_main_context_default.restype = _GMainContext
        from gobject import GMainContext
        return GMainContext(None, obj=    libgobject.g_main_context_default()
 or POINTER(c_int)())
    @staticmethod
    def g_timeout_add( interval, function, data,):
        libgobject.g_timeout_add.restype = guint
        libgobject.g_timeout_add.argtypes = [guint,GSourceFunc,gpointer]
        
        return     libgobject.g_timeout_add(interval, function, data, )

    @staticmethod
    def g_idle_remove_by_data( data,):
        libgobject.g_idle_remove_by_data.restype = gboolean
        libgobject.g_idle_remove_by_data.argtypes = [gpointer]
        
        return     libgobject.g_idle_remove_by_data(data, )

    @staticmethod
    def g_child_watch_add_full( priority, pid, function, data, notify,):
        if pid: pid = pid._object
        else: pid = POINTER(c_int)()
        if function: function = function._object
        else: function = POINTER(c_int)()
        libgobject.g_child_watch_add_full.restype = guint
        libgobject.g_child_watch_add_full.argtypes = [gint,GPid,GChildWatchFunc,gpointer,GDestroyNotify]
        
        return     libgobject.g_child_watch_add_full(priority, pid, function, data, notify, )

    @staticmethod
    def g_timeout_source_new_seconds( interval,):
        libgobject.g_timeout_source_new_seconds.restype = _GSource
        libgobject.g_timeout_source_new_seconds.argtypes = [guint]
        from gobject import GSource
        return GSource(None, obj=    libgobject.g_timeout_source_new_seconds(interval, )
 or POINTER(c_int)())
    @staticmethod
    def g_timeout_add_seconds_full( priority, interval, function, data, notify,):
        libgobject.g_timeout_add_seconds_full.restype = guint
        libgobject.g_timeout_add_seconds_full.argtypes = [gint,guint,GSourceFunc,gpointer,GDestroyNotify]
        
        return     libgobject.g_timeout_add_seconds_full(priority, interval, function, data, notify, )

    @staticmethod
    def g_idle_add_full( priority, function, data, notify,):
        libgobject.g_idle_add_full.restype = guint
        libgobject.g_idle_add_full.argtypes = [gint,GSourceFunc,gpointer,GDestroyNotify]
        
        return     libgobject.g_idle_add_full(priority, function, data, notify, )

    @staticmethod
    def g_child_watch_add( pid, function, data,):
        if pid: pid = pid._object
        else: pid = POINTER(c_int)()
        if function: function = function._object
        else: function = POINTER(c_int)()
        libgobject.g_child_watch_add.restype = guint
        libgobject.g_child_watch_add.argtypes = [GPid,GChildWatchFunc,gpointer]
        
        return     libgobject.g_child_watch_add(pid, function, data, )

    @staticmethod
    def get_thread_default():
        libgobject.g_main_context_get_thread_default.restype = _GMainContext
        from gobject import GMainContext
        return GMainContext(None, obj=    libgobject.g_main_context_get_thread_default()
 or POINTER(c_int)())
    @staticmethod
    def ref_thread_default():
        libgobject.g_main_context_ref_thread_default.restype = _GMainContext
        from gobject import GMainContext
        return GMainContext(None, obj=    libgobject.g_main_context_ref_thread_default()
 or POINTER(c_int)())
