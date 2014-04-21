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
from .gtk3_types import *
from .gtk3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_void_p)
_GdkGeometry = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
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
_PangoItem = POINTER(c_void_p)
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
_GInputStream = POINTER(c_void_p)
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
_GtkRequisition = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GtkIconTheme = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_GtkAccelLabel = POINTER(c_void_p)
_JSGlobalContext = POINTER(c_void_p)
_GApplication = POINTER(c_void_p)
_GFileMonitor = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_GString = POINTER(c_void_p)
_GFileAttributeMatcher = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_WebKitHitTestResult = POINTER(c_void_p)
_WebKitWebSettings = POINTER(c_void_p)
_GBoxed = POINTER(c_void_p)
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
_GtkMisc = POINTER(c_void_p)
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
_GdkDragContext = POINTER(c_void_p)
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
_PangoLayoutIter = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoLayoutRun = POINTER(c_void_p)
_GFileInputStream = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_JSPropertyNameArray = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GtkAboutDialog = POINTER(c_void_p)
_WebKitViewportAttributes = POINTER(c_void_p)
_WebKitWebHistoryItem = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
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
_PangoFontsetSimple = POINTER(c_void_p)
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
_GString = POINTER(c_void_p)
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
_GtkInvisible = POINTER(c_void_p)
_GSourceFuncs = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_GFileIOStream = POINTER(c_void_p)
_WebKitSecurityOrigin = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
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
_PangoFontFace = POINTER(c_void_p)
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
cairo_extend_t = c_int
cairo_filter_t = c_int
CairoPatternype_t = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkLicense = c_int

try:
    libgtk3.gtk_about_dialog_set_authors.restype = None
    libgtk3.gtk_about_dialog_set_authors.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_website_label.restype = c_char_p
    libgtk3.gtk_about_dialog_get_website_label.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_license_type.restype = None
    libgtk3.gtk_about_dialog_set_license_type.argtypes = [_GtkAboutDialog,GtkLicense]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_artists.restype = c_char_p
    libgtk3.gtk_about_dialog_get_artists.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_logo_icon_name.restype = None
    libgtk3.gtk_about_dialog_set_logo_icon_name.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_documenters.restype = None
    libgtk3.gtk_about_dialog_set_documenters.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_license.restype = c_char_p
    libgtk3.gtk_about_dialog_get_license.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_logo.restype = None
    libgtk3.gtk_about_dialog_set_logo.argtypes = [_GtkAboutDialog,_GdkPixbuf]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_website_label.restype = None
    libgtk3.gtk_about_dialog_set_website_label.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_license.restype = None
    libgtk3.gtk_about_dialog_set_license.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_artists.restype = None
    libgtk3.gtk_about_dialog_set_artists.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_program_name.restype = None
    libgtk3.gtk_about_dialog_set_program_name.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_translator_credits.restype = None
    libgtk3.gtk_about_dialog_set_translator_credits.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_website.restype = None
    libgtk3.gtk_about_dialog_set_website.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_copyright.restype = None
    libgtk3.gtk_about_dialog_set_copyright.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_authors.restype = c_char_p
    libgtk3.gtk_about_dialog_get_authors.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_logo_icon_name.restype = c_char_p
    libgtk3.gtk_about_dialog_get_logo_icon_name.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_wrap_license.restype = None
    libgtk3.gtk_about_dialog_set_wrap_license.argtypes = [_GtkAboutDialog,gboolean]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_documenters.restype = c_char_p
    libgtk3.gtk_about_dialog_get_documenters.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_wrap_license.restype = gboolean
    libgtk3.gtk_about_dialog_get_wrap_license.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_version.restype = None
    libgtk3.gtk_about_dialog_set_version.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_translator_credits.restype = c_char_p
    libgtk3.gtk_about_dialog_get_translator_credits.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_program_name.restype = c_char_p
    libgtk3.gtk_about_dialog_get_program_name.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_comments.restype = None
    libgtk3.gtk_about_dialog_set_comments.argtypes = [_GtkAboutDialog,Asciifier]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_logo.restype = _GdkPixbuf
    libgtk3.gtk_about_dialog_get_logo.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_show_about_dialog.restype = None
    libgtk3.gtk_show_about_dialog.argtypes = [_GtkAboutDialog,_GtkWindow,Asciifier,]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_license_type.restype = GtkLicense
    libgtk3.gtk_about_dialog_get_license_type.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_copyright.restype = c_char_p
    libgtk3.gtk_about_dialog_get_copyright.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_version.restype = c_char_p
    libgtk3.gtk_about_dialog_get_version.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_website.restype = c_char_p
    libgtk3.gtk_about_dialog_get_website.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_comments.restype = c_char_p
    libgtk3.gtk_about_dialog_get_comments.argtypes = [_GtkAboutDialog]
except:
   pass
from . import gtk3__GtkDialog
class GtkAboutDialog( gtk3__GtkDialog.GtkDialog):
    """Class GtkAboutDialog Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_about_dialog_new.restype = POINTER(c_void_p)
            
            libgtk3.gtk_about_dialog_new.argtypes = []
            self._object = libgtk3.gtk_about_dialog_new()

    """Methods"""
    def set_authors(  self, authors, ):

        
        libgtk3.gtk_about_dialog_set_authors( self._object,authors )

    def get_website_label(  self, ):

        
        return libgtk3.gtk_about_dialog_get_website_label( self._object )

    def set_license_type(  self, license_type, ):

        
        libgtk3.gtk_about_dialog_set_license_type( self._object,license_type )

    def get_artists(  self, ):

        
        return libgtk3.gtk_about_dialog_get_artists( self._object )

    def set_logo_icon_name(  self, icon_name, ):

        
        libgtk3.gtk_about_dialog_set_logo_icon_name( self._object,icon_name )

    def set_documenters(  self, documenters, ):

        
        libgtk3.gtk_about_dialog_set_documenters( self._object,documenters )

    def get_license(  self, ):

        
        return libgtk3.gtk_about_dialog_get_license( self._object )

    def set_logo(  self, logo, ):
        if logo: logo = logo._object
        else: logo = POINTER(c_void_p)()

        
        libgtk3.gtk_about_dialog_set_logo( self._object,logo )

    def set_website_label(  self, website_label, ):

        
        libgtk3.gtk_about_dialog_set_website_label( self._object,website_label )

    def set_license(  self, license, ):

        
        libgtk3.gtk_about_dialog_set_license( self._object,license )

    def set_artists(  self, artists, ):

        
        libgtk3.gtk_about_dialog_set_artists( self._object,artists )

    def set_program_name(  self, name, ):

        
        libgtk3.gtk_about_dialog_set_program_name( self._object,name )

    def set_translator_credits(  self, translator_credits, ):

        
        libgtk3.gtk_about_dialog_set_translator_credits( self._object,translator_credits )

    def set_website(  self, website, ):

        
        libgtk3.gtk_about_dialog_set_website( self._object,website )

    def set_copyright(  self, copyright, ):

        
        libgtk3.gtk_about_dialog_set_copyright( self._object,copyright )

    def get_authors(  self, ):

        
        return libgtk3.gtk_about_dialog_get_authors( self._object )

    def get_logo_icon_name(  self, ):

        
        return libgtk3.gtk_about_dialog_get_logo_icon_name( self._object )

    def set_wrap_license(  self, wrap_license, ):

        
        libgtk3.gtk_about_dialog_set_wrap_license( self._object,wrap_license )

    def get_documenters(  self, ):

        
        return libgtk3.gtk_about_dialog_get_documenters( self._object )

    def get_wrap_license(  self, ):

        
        return libgtk3.gtk_about_dialog_get_wrap_license( self._object )

    def set_version(  self, version, ):

        
        libgtk3.gtk_about_dialog_set_version( self._object,version )

    def get_translator_credits(  self, ):

        
        return libgtk3.gtk_about_dialog_get_translator_credits( self._object )

    def get_program_name(  self, ):

        
        return libgtk3.gtk_about_dialog_get_program_name( self._object )

    def set_comments(  self, comments, ):

        
        libgtk3.gtk_about_dialog_set_comments( self._object,comments )

    def get_logo(  self, ):

        from .gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_about_dialog_get_logo( self._object ) or POINTER(c_void_p)())

    def gtk_show_about_dialog(  self, parent, first_property_name,*args  ):
        if parent: parent = parent._object
        else: parent = POINTER(c_void_p)()


        def callit( parent, first_property_name, *args ):
                for arg in args:
                     libgtk3.gtk_show_about_dialog.argtypes.append(args[1])
                return libgtk3.gtk_show_about_dialog( parent, first_property_name, *args)
    
        return callit( self._object, parent, first_property_name,*args )

    def get_license_type(  self, ):

        
        return libgtk3.gtk_about_dialog_get_license_type( self._object )

    def get_copyright(  self, ):

        
        return libgtk3.gtk_about_dialog_get_copyright( self._object )

    def get_version(  self, ):

        
        return libgtk3.gtk_about_dialog_get_version( self._object )

    def get_website(  self, ):

        
        return libgtk3.gtk_about_dialog_get_website( self._object )

    def get_comments(  self, ):

        
        return libgtk3.gtk_about_dialog_get_comments( self._object )

