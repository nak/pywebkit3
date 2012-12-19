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
_WebKitWebWindowFeatures = POINTER(c_int)
_void = POINTER(c_int)
_GAppInfo = POINTER(c_int)
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
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GtkPathPriorityType = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_GAppInfo = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkCursor = POINTER(c_int)
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
_cairo_region_t = POINTER(c_int)
_WebKitNetworkRequest = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
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
_CairoPattern = POINTER(c_int)
_GdkDevice = POINTER(c_int)
_PangoRectangle = POINTER(c_int)
_GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
_GFile = POINTER(c_int)
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
_GdkRectangle = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
_gunichar = POINTER(c_int)
_GdkWMDecoration = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_WebKitDOMNode = POINTER(c_int)
_GtkStyleProperties = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GParameter = POINTER(c_int)
_GtkStyle = POINTER(c_int)
_GIcon = POINTER(c_int)
_GtkWindow = POINTER(c_int)
_GtkGradient = POINTER(c_int)
_cairo_pattern_t = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GtkTargetEntry = POINTER(c_int)
_GtkApplication = POINTER(c_int)
_CairoPattern = POINTER(c_int)
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

try:
    libgio.g_app_info_launch_uris.restype = gboolean
    libgio.g_app_info_launch_uris.argtypes = [_GAppInfo,_GList,_GAppLaunchContext,_GError]
except:
   pass
try:
    libgio.g_app_info_set_as_last_used_for_type.restype = gboolean
    libgio.g_app_info_set_as_last_used_for_type.argtypes = [_GAppInfo,c_char_p,_GError]
except:
   pass
try:
    libgio.g_app_info_reset_type_associations.restype = None
    libgio.g_app_info_reset_type_associations.argtypes = [_GAppInfo,c_char_p]
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
    libgio.g_app_info_add_supports_type.argtypes = [_GAppInfo,c_char_p,_GError]
except:
   pass
try:
    libgio.g_app_info_set_as_default_for_extension.restype = gboolean
    libgio.g_app_info_set_as_default_for_extension.argtypes = [_GAppInfo,c_char_p,_GError]
except:
   pass
try:
    libgio.g_app_info_remove_supports_type.restype = gboolean
    libgio.g_app_info_remove_supports_type.argtypes = [_GAppInfo,c_char_p,_GError]
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
    libgio.g_app_info_set_as_default_for_type.argtypes = [_GAppInfo,c_char_p,_GError]
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
    libgio.g_app_info_get_all_for_type.argtypes = [c_char_p]
except:
   pass
try:
    libgio.g_app_info_get_all.restype = _GList
    libgio.g_app_info_get_all.argtypes = []
except:
   pass
try:
    libgio.g_app_info_create_from_commandline.restype = _GAppInfo
    libgio.g_app_info_create_from_commandline.argtypes = [c_char_p,c_char_p,GAppInfoCreateFlags,_GError]
except:
   pass
try:
    libgio.g_app_info_get_recommended_for_type.restype = _GList
    libgio.g_app_info_get_recommended_for_type.argtypes = [c_char_p]
except:
   pass
try:
    libgio.g_app_info_get_fallback_for_type.restype = _GList
    libgio.g_app_info_get_fallback_for_type.argtypes = [c_char_p]
except:
   pass
try:
    libgio.g_app_info_launch_default_for_uri.restype = gboolean
    libgio.g_app_info_launch_default_for_uri.argtypes = [c_char_p,_GAppLaunchContext,_GError]
except:
   pass
try:
    libgio.g_app_info_get_default_for_uri_scheme.restype = _GAppInfo
    libgio.g_app_info_get_default_for_uri_scheme.argtypes = [c_char_p]
except:
   pass
try:
    libgio.g_app_info_get_default_for_type.restype = _GAppInfo
    libgio.g_app_info_get_default_for_type.argtypes = [c_char_p,gboolean]
except:
   pass
import gio__GInterface
class GAppInfo( gio__GInterface.GInterface):
    """Class GAppInfo Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def launch_uris(  self, uris, launch_context, error, ):
        if uris: uris = uris._object
        else: uris = POINTER(c_int)()
        if launch_context: launch_context = launch_context._object
        else: launch_context = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_app_info_launch_uris( self._object,uris,launch_context,error )

    def set_as_last_used_for_type(  self, content_type, error, ):
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_app_info_set_as_last_used_for_type( self._object,content_type,error )

    def reset_type_associations(  self, content_type, ):

        
        libgio.g_app_info_reset_type_associations( self._object,content_type )

    def delete(  self, ):

        
        return libgio.g_app_info_delete( self._object )

    def get_description(  self, ):

        
        return libgio.g_app_info_get_description( self._object )

    def equal(  self, appinfo2, ):
        if appinfo2: appinfo2 = appinfo2._object
        else: appinfo2 = POINTER(c_int)()

        
        return libgio.g_app_info_equal( self._object,appinfo2 )

    def add_supports_type(  self, content_type, error, ):
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_app_info_add_supports_type( self._object,content_type,error )

    def set_as_default_for_extension(  self, extension, error, ):
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_app_info_set_as_default_for_extension( self._object,extension,error )

    def remove_supports_type(  self, content_type, error, ):
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_app_info_remove_supports_type( self._object,content_type,error )

    def dup(  self, ):

        from gobject import GAppInfo
        return GAppInfo( obj=libgio.g_app_info_dup( self._object ) or POINTER(c_int)())

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

        from gobject import GIcon
        return GIcon( obj=libgio.g_app_info_get_icon( self._object ) or POINTER(c_int)())

    def launch(  self, files, launch_context, error, ):
        if files: files = files._object
        else: files = POINTER(c_int)()
        if launch_context: launch_context = launch_context._object
        else: launch_context = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_app_info_launch( self._object,files,launch_context,error )

    def set_as_default_for_type(  self, content_type, error, ):
        if error: error = error._object
        else: error = POINTER(c_int)()

        
        return libgio.g_app_info_set_as_default_for_type( self._object,content_type,error )

    def get_executable(  self, ):

        
        return libgio.g_app_info_get_executable( self._object )

    def supports_files(  self, ):

        
        return libgio.g_app_info_supports_files( self._object )

    @staticmethod
    def get_all_for_type( content_type,):
        from gobject import GList
        return GList( obj=    libgio.g_app_info_get_all_for_type(content_type, )
 or POINTER(c_int)())
    @staticmethod
    def get_all():
        from gobject import GList
        return GList( obj=    libgio.g_app_info_get_all()
 or POINTER(c_int)())
    @staticmethod
    def create_from_commandline( commandline, application_name, flags, error,):
        if flags: flags = flags._object
        else: flags = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()
        from gobject import GAppInfo
        return GAppInfo( obj=    libgio.g_app_info_create_from_commandline(commandline, application_name, flags, error, )
 or POINTER(c_int)())
    @staticmethod
    def get_recommended_for_type( content_type,):
        from gobject import GList
        return GList( obj=    libgio.g_app_info_get_recommended_for_type(content_type, )
 or POINTER(c_int)())
    @staticmethod
    def get_fallback_for_type( content_type,):
        from gobject import GList
        return GList( obj=    libgio.g_app_info_get_fallback_for_type(content_type, )
 or POINTER(c_int)())
    @staticmethod
    def launch_default_for_uri( uri, launch_context, error,):
        if launch_context: launch_context = launch_context._object
        else: launch_context = POINTER(c_int)()
        if error: error = error._object
        else: error = POINTER(c_int)()
        
        return     libgio.g_app_info_launch_default_for_uri(uri, launch_context, error, )

    @staticmethod
    def get_default_for_uri_scheme( uri_scheme,):
        from gobject import GAppInfo
        return GAppInfo( obj=    libgio.g_app_info_get_default_for_uri_scheme(uri_scheme, )
 or POINTER(c_int)())
    @staticmethod
    def get_default_for_type( content_type, must_support_uris,):
        from gobject import GAppInfo
        return GAppInfo( obj=    libgio.g_app_info_get_default_for_type(content_type, must_support_uris, )
 or POINTER(c_int)())
