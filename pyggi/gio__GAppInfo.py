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
from .gio_types import *
from .gio_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_void_p)
_GdkGeometry = POINTER(c_void_p)
_WebKitNetworkResponse = POINTER(c_void_p)
_GtkLabel = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
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
_GdkDisplay = POINTER(c_void_p)
_GtkStyleProvider = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_void = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
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
_GtkIconSet = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_JSGlobalContext = POINTER(c_void_p)
_GFileMonitor = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_WebKitHitTestResult = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
_GtkPathPriorityType = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_GAppInfo = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitWebInspector = POINTER(c_void_p)
_GOptionGroup = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_GtkWidgetClass = POINTER(c_void_p)
_GdkEventKey = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_PangoFontMetrics = POINTER(c_void_p)
_cairo_surface_t = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_WebKitWebFrame = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_WebKitNetworkRequest = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
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
_GdkVisual = POINTER(c_void_p)
_GdkEventButton = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
_GdkDevice = POINTER(c_void_p)
_PangoRectangle = POINTER(c_void_p)
_GtkAccelGroup = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_GtkIconSource = POINTER(c_void_p)
_GFile = POINTER(c_void_p)
_GtkAllocation = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_PangoLayoutLine = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_PangoTabArray = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_WebKitDOMDocument = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkPrintOperation = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebView = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_SoupMessage = POINTER(c_void_p)
_WebKitWebDataSource = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_gunichar = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_WebKitDOMNode = POINTER(c_void_p)
_GtkStyleProperties = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GParameter = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_GtkGradient = POINTER(c_void_p)
_cairo_pattern_t = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_CairoPattern = POINTER(c_void_p)
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

try:
    libgio.g_app_info_launch_uris.restype = gboolean
    libgio.g_app_info_launch_uris.argtypes = [_GAppInfo,_GList,_GAppLaunchContext,_GError]
except:
   pass
try:
    libgio.g_app_info_set_as_last_used_for_type.restype = gboolean
    libgio.g_app_info_set_as_last_used_for_type.argtypes = [_GAppInfo,Asciifier,_GError]
except:
   pass
try:
    libgio.g_app_info_reset_type_associations.restype = None
    libgio.g_app_info_reset_type_associations.argtypes = [_GAppInfo,Asciifier]
except:
   pass
try:
    libgio.g_app_info_delete.restype = gboolean
    libgio.g_app_info_delete.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_get_description.restype = c_char_p
    libgio.g_app_info_get_description.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_equal.restype = gboolean
    libgio.g_app_info_equal.argtypes = [_GAppInfo,_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_add_supports_type.restype = gboolean
    libgio.g_app_info_add_supports_type.argtypes = [_GAppInfo,Asciifier,_GError]
except:
   pass
try:
    libgio.g_app_info_set_as_default_for_extension.restype = gboolean
    libgio.g_app_info_set_as_default_for_extension.argtypes = [_GAppInfo,Asciifier,_GError]
except:
   pass
try:
    libgio.g_app_info_remove_supports_type.restype = gboolean
    libgio.g_app_info_remove_supports_type.argtypes = [_GAppInfo,Asciifier,_GError]
except:
   pass
try:
    libgio.g_app_info_dup.restype = _GAppInfo
    libgio.g_app_info_dup.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_can_delete.restype = gboolean
    libgio.g_app_info_can_delete.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_get_id.restype = c_char_p
    libgio.g_app_info_get_id.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_get_name.restype = c_char_p
    libgio.g_app_info_get_name.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_get_display_name.restype = c_char_p
    libgio.g_app_info_get_display_name.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_supports_uris.restype = gboolean
    libgio.g_app_info_supports_uris.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_should_show.restype = gboolean
    libgio.g_app_info_should_show.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_get_commandline.restype = c_char_p
    libgio.g_app_info_get_commandline.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_can_remove_supports_type.restype = gboolean
    libgio.g_app_info_can_remove_supports_type.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_get_icon.restype = _GIcon
    libgio.g_app_info_get_icon.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_launch.restype = gboolean
    libgio.g_app_info_launch.argtypes = [_GAppInfo,_GList,_GAppLaunchContext,_GError]
except:
   pass
try:
    libgio.g_app_info_set_as_default_for_type.restype = gboolean
    libgio.g_app_info_set_as_default_for_type.argtypes = [_GAppInfo,Asciifier,_GError]
except:
   pass
try:
    libgio.g_app_info_get_executable.restype = c_char_p
    libgio.g_app_info_get_executable.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_supports_files.restype = gboolean
    libgio.g_app_info_supports_files.argtypes = [_GAppInfo]
except:
   pass
try:
    libgio.g_app_info_get_all_for_type.restype = _GList
    libgio.g_app_info_get_all_for_type.argtypes = [Asciifier]
except:
   pass
try:
    libgio.g_app_info_get_all.restype = _GList
    libgio.g_app_info_get_all.argtypes = []
except:
   pass
try:
    libgio.g_app_info_create_from_commandline.restype = _GAppInfo
    libgio.g_app_info_create_from_commandline.argtypes = [Asciifier,Asciifier,GAppInfoCreateFlags,_GError]
except:
   pass
try:
    libgio.g_app_info_get_recommended_for_type.restype = _GList
    libgio.g_app_info_get_recommended_for_type.argtypes = [Asciifier]
except:
   pass
try:
    libgio.g_app_info_get_fallback_for_type.restype = _GList
    libgio.g_app_info_get_fallback_for_type.argtypes = [Asciifier]
except:
   pass
try:
    libgio.g_app_info_launch_default_for_uri.restype = gboolean
    libgio.g_app_info_launch_default_for_uri.argtypes = [Asciifier,_GAppLaunchContext,_GError]
except:
   pass
try:
    libgio.g_app_info_get_default_for_uri_scheme.restype = _GAppInfo
    libgio.g_app_info_get_default_for_uri_scheme.argtypes = [Asciifier]
except:
   pass
try:
    libgio.g_app_info_get_default_for_type.restype = _GAppInfo
    libgio.g_app_info_get_default_for_type.argtypes = [Asciifier,gboolean]
except:
   pass
from . import gio__GInterface
class GAppInfo( gio__GInterface.GInterface):
    """Class GAppInfo Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def launch_uris(  self, uris, launch_context, error, ):
        if uris: uris = uris._object
        else: uris = POINTER(c_void_p)()
        if launch_context: launch_context = launch_context._object
        else: launch_context = POINTER(c_void_p)()
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        
        return libgio.g_app_info_launch_uris( self._object,uris,launch_context,error )

    def set_as_last_used_for_type(  self, content_type, error, ):
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        
        return libgio.g_app_info_set_as_last_used_for_type( self._object,content_type,error )

    def reset_type_associations(  self, content_type, ):

        
        libgio.g_app_info_reset_type_associations( self._object,content_type )

    def delete(  self, ):

        
        return libgio.g_app_info_delete( self._object )

    def get_description(  self, ):

        
        return libgio.g_app_info_get_description( self._object )

    def equal(  self, appinfo2, ):
        if appinfo2: appinfo2 = appinfo2._object
        else: appinfo2 = POINTER(c_void_p)()

        
        return libgio.g_app_info_equal( self._object,appinfo2 )

    def add_supports_type(  self, content_type, error, ):
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        
        return libgio.g_app_info_add_supports_type( self._object,content_type,error )

    def set_as_default_for_extension(  self, extension, error, ):
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        
        return libgio.g_app_info_set_as_default_for_extension( self._object,extension,error )

    def remove_supports_type(  self, content_type, error, ):
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        
        return libgio.g_app_info_remove_supports_type( self._object,content_type,error )

    def dup(  self, ):

        from .gobject import GAppInfo
        return GAppInfo( obj=libgio.g_app_info_dup( self._object ) or POINTER(c_void_p)())

    def can_delete(  self, ):

        
        return libgio.g_app_info_can_delete( self._object )

    def get_id(  self, ):

        
        return libgio.g_app_info_get_id( self._object )

    def get_name(  self, ):

        
        return libgio.g_app_info_get_name( self._object )

    def get_display_name(  self, ):

        
        return libgio.g_app_info_get_display_name( self._object )

    def supports_uris(  self, ):

        
        return libgio.g_app_info_supports_uris( self._object )

    def should_show(  self, ):

        
        return libgio.g_app_info_should_show( self._object )

    def get_commandline(  self, ):

        
        return libgio.g_app_info_get_commandline( self._object )

    def can_remove_supports_type(  self, ):

        
        return libgio.g_app_info_can_remove_supports_type( self._object )

    def get_icon(  self, ):

        from .gobject import GIcon
        return GIcon( obj=libgio.g_app_info_get_icon( self._object ) or POINTER(c_void_p)())

    def launch(  self, files, launch_context, error, ):
        if files: files = files._object
        else: files = POINTER(c_void_p)()
        if launch_context: launch_context = launch_context._object
        else: launch_context = POINTER(c_void_p)()
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        
        return libgio.g_app_info_launch( self._object,files,launch_context,error )

    def set_as_default_for_type(  self, content_type, error, ):
        if error: error = error._object
        else: error = POINTER(c_void_p)()

        
        return libgio.g_app_info_set_as_default_for_type( self._object,content_type,error )

    def get_executable(  self, ):

        
        return libgio.g_app_info_get_executable( self._object )

    def supports_files(  self, ):

        
        return libgio.g_app_info_supports_files( self._object )

    @staticmethod
    def get_all_for_type( content_type,):
        from .gobject import GList
        return GList( obj=    libgio.g_app_info_get_all_for_type(content_type, )
 or POINTER(c_void_p)())
    @staticmethod
    def get_all():
        from .gobject import GList
        return GList( obj=    libgio.g_app_info_get_all()
 or POINTER(c_void_p)())
    @staticmethod
    def create_from_commandline( commandline, application_name, flags, error,):
        if flags: flags = flags._object
        else: flags = POINTER(c_void_p)()
        if error: error = error._object
        else: error = POINTER(c_void_p)()
        from .gobject import GAppInfo
        return GAppInfo( obj=    libgio.g_app_info_create_from_commandline(commandline, application_name, flags, error, )
 or POINTER(c_void_p)())
    @staticmethod
    def get_recommended_for_type( content_type,):
        from .gobject import GList
        return GList( obj=    libgio.g_app_info_get_recommended_for_type(content_type, )
 or POINTER(c_void_p)())
    @staticmethod
    def get_fallback_for_type( content_type,):
        from .gobject import GList
        return GList( obj=    libgio.g_app_info_get_fallback_for_type(content_type, )
 or POINTER(c_void_p)())
    @staticmethod
    def launch_default_for_uri( uri, launch_context, error,):
        if launch_context: launch_context = launch_context._object
        else: launch_context = POINTER(c_void_p)()
        if error: error = error._object
        else: error = POINTER(c_void_p)()
        
        return     libgio.g_app_info_launch_default_for_uri(uri, launch_context, error, )

    @staticmethod
    def get_default_for_uri_scheme( uri_scheme,):
        from .gobject import GAppInfo
        return GAppInfo( obj=    libgio.g_app_info_get_default_for_uri_scheme(uri_scheme, )
 or POINTER(c_void_p)())
    @staticmethod
    def get_default_for_type( content_type, must_support_uris,):
        from .gobject import GAppInfo
        return GAppInfo( obj=    libgio.g_app_info_get_default_for_type(content_type, must_support_uris, )
 or POINTER(c_void_p)())
