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
from gio_types import *
from gio_enums import *

    
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
_GdkDisplay = POINTER(c_int)
_GtkStyleProvider = POINTER(c_int)
_GtkDialog = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_void = POINTER(c_int)
_GtkIconInfo = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
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
_GtkIconSet = POINTER(c_int)
_GtkIconTheme = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAccelLabel = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_GdkPoint = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_GEmblemedIcon = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
_GScanner = POINTER(c_int)
_GtkWidgetClass = POINTER(c_int)
_GdkEventKey = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
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
_GList = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
_GdkRGBA = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkColor = POINTER(c_int)
_GEmblem = POINTER(c_int)
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GVolume = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
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

try:
    libgio.g_mount_unshadow.restype = None
    libgio.g_mount_unshadow.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_guess_content_type.restype = None
    libgio.g_mount_guess_content_type.argtypes = [_GMount,gboolean,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_mount_eject.restype = None
    libgio.g_mount_eject.argtypes = [_GMount,GMountUnmountFlags,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_mount_unmount_finish.restype = gboolean
    libgio.g_mount_unmount_finish.argtypes = [_GMount,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_mount_can_eject.restype = gboolean
    libgio.g_mount_can_eject.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_is_shadowed.restype = gboolean
    libgio.g_mount_is_shadowed.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_get_default_location.restype = _GFile
    libgio.g_mount_get_default_location.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_remount.restype = None
    libgio.g_mount_remount.argtypes = [_GMount,GMountMountFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_mount_get_icon.restype = _GIcon
    libgio.g_mount_get_icon.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_guess_content_type_finish.restype = c_char_p
    libgio.g_mount_guess_content_type_finish.argtypes = [_GMount,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_mount_remount_finish.restype = gboolean
    libgio.g_mount_remount_finish.argtypes = [_GMount,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_mount_get_drive.restype = _GDrive
    libgio.g_mount_get_drive.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_eject_finish.restype = gboolean
    libgio.g_mount_eject_finish.argtypes = [_GMount,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_mount_guess_content_type_sync.restype = c_char_p
    libgio.g_mount_guess_content_type_sync.argtypes = [_GMount,gboolean,_GCancellable,_GError]
except:
   pass
try:
    libgio.g_mount_get_root.restype = _GFile
    libgio.g_mount_get_root.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_unmount_with_operation.restype = None
    libgio.g_mount_unmount_with_operation.argtypes = [_GMount,GMountUnmountFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_mount_unmount.restype = None
    libgio.g_mount_unmount.argtypes = [_GMount,GMountUnmountFlags,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_mount_eject_with_operation.restype = None
    libgio.g_mount_eject_with_operation.argtypes = [_GMount,GMountUnmountFlags,_GMountOperation,_GCancellable,GAsyncReadyCallback,gpointer]
except:
   pass
try:
    libgio.g_mount_get_name.restype = c_char_p
    libgio.g_mount_get_name.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_can_unmount.restype = gboolean
    libgio.g_mount_can_unmount.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_get_uuid.restype = c_char_p
    libgio.g_mount_get_uuid.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_unmount_with_operation_finish.restype = gboolean
    libgio.g_mount_unmount_with_operation_finish.argtypes = [_GMount,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_mount_eject_with_operation_finish.restype = gboolean
    libgio.g_mount_eject_with_operation_finish.argtypes = [_GMount,_GAsyncResult,_GError]
except:
   pass
try:
    libgio.g_mount_shadow.restype = None
    libgio.g_mount_shadow.argtypes = [_GMount]
except:
   pass
try:
    libgio.g_mount_get_volume.restype = _GVolume
    libgio.g_mount_get_volume.argtypes = [_GMount]
except:
   pass
import gio__GInterface
class GMount( gio__GInterface.GInterface):
    """Class GMount Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def unshadow(  self, ):

        
        libgio.g_mount_unshadow( self._object )

    def guess_content_type(  self, force_rescan, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_mount_guess_content_type( self._object,force_rescan,cancellable,callback,user_data )

    def eject(  self, flags, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_mount_eject( self._object,flags,cancellable,callback,user_data )

    def unmount_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_mount_unmount_finish( self._object,result,error )

    def can_eject(  self, ):

        
        return libgio.g_mount_can_eject( self._object )

    def is_shadowed(  self, ):

        
        return libgio.g_mount_is_shadowed( self._object )

    def get_default_location(  self, ):

        from gio import GFile
        return GFile( obj=libgio.g_mount_get_default_location( self._object ) or POINTER(c_int)())

    def remount(  self, flags, mount_operation, cancellable, callback, user_data, ):
        if mount_operation: mount_operation = mount_operation._object
        else: mount_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_mount_remount( self._object,flags,mount_operation,cancellable,callback,user_data )

    def get_icon(  self, ):

        from gobject import GIcon
        return GIcon( obj=libgio.g_mount_get_icon( self._object ) or POINTER(c_int)())

    def guess_content_type_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_mount_guess_content_type_finish( self._object,result,error )

    def remount_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_mount_remount_finish( self._object,result,error )

    def get_drive(  self, ):

        from gobject import GDrive
        return GDrive( obj=libgio.g_mount_get_drive( self._object ) or POINTER(c_int)())

    def eject_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_mount_eject_finish( self._object,result,error )

    def guess_content_type_sync(  self, force_rescan, cancellable, error, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_mount_guess_content_type_sync( self._object,force_rescan,cancellable,error )

    def get_root(  self, ):

        from gio import GFile
        return GFile( obj=libgio.g_mount_get_root( self._object ) or POINTER(c_int)())

    def unmount_with_operation(  self, flags, mount_operation, cancellable, callback, user_data, ):
        if mount_operation: mount_operation = mount_operation._object
        else: mount_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_mount_unmount_with_operation( self._object,flags,mount_operation,cancellable,callback,user_data )

    def unmount(  self, flags, cancellable, callback, user_data, ):
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_mount_unmount( self._object,flags,cancellable,callback,user_data )

    def eject_with_operation(  self, flags, mount_operation, cancellable, callback, user_data, ):
        if mount_operation: mount_operation = mount_operation._object
        else: mount_operation = POINTER(c_int)()
        if cancellable: cancellable = cancellable._object
        else: cancellable = POINTER(c_int)()
        if callback: callback = callback._object
        else: callback = POINTER(c_int)()

        
        libgio.g_mount_eject_with_operation( self._object,flags,mount_operation,cancellable,callback,user_data )

    def get_name(  self, ):

        
        return libgio.g_mount_get_name( self._object )

    def can_unmount(  self, ):

        
        return libgio.g_mount_can_unmount( self._object )

    def get_uuid(  self, ):

        
        return libgio.g_mount_get_uuid( self._object )

    def unmount_with_operation_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_mount_unmount_with_operation_finish( self._object,result,error )

    def eject_with_operation_finish(  self, result, error, ):
        if result: result = result._object
        else: result = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_mount_eject_with_operation_finish( self._object,result,error )

    def shadow(  self, ):

        
        libgio.g_mount_shadow( self._object )

    def get_volume(  self, ):

        from gobject import GVolume
        return GVolume( obj=libgio.g_mount_get_volume( self._object ) or POINTER(c_int)())

