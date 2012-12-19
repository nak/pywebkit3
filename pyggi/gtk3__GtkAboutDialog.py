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
from gtk3_types import *
from gtk3_enums import *

    
"""Derived Pointer Types"""
_GtkRcStyle = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
_PangoFont = POINTER(c_int)
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
_PangoItem = POINTER(c_int)
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
_GInputStream = POINTER(c_int)
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
_GtkRequisition = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkIconTheme = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAccelLabel = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_GFileMonitor = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GString = POINTER(c_int)
_GFileAttributeMatcher = POINTER(c_int)
_PangoContext = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
_GBoxed = POINTER(c_int)
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
_GtkMisc = POINTER(c_int)
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
_GdkDragContext = POINTER(c_int)
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
_PangoLayoutIter = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
_GFileInputStream = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
_GError = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GtkAboutDialog = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
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
_PangoFontsetSimple = POINTER(c_int)
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
_GString = POINTER(c_int)
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
_GtkInvisible = POINTER(c_int)
_GSourceFuncs = POINTER(c_int)
_PangoGlyphString = POINTER(c_int)
_GFileIOStream = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
_GObjectClass = POINTER(c_int)
_GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
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
_PangoFontFace = POINTER(c_int)
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
cairo_extend_t = c_int
cairo_filter_t = c_int
CairoPatternype_t = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkLicense = c_int

try:
    libgtk3.gtk_about_dialog_set_authors.restype = None
    libgtk3.gtk_about_dialog_set_authors.argtypes = [_GtkAboutDialog,c_char_p]
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
    libgtk3.gtk_about_dialog_set_logo_icon_name.argtypes = [_GtkAboutDialog,c_char_p]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_documenters.restype = None
    libgtk3.gtk_about_dialog_set_documenters.argtypes = [_GtkAboutDialog,c_char_p]
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
    libgtk3.gtk_about_dialog_set_website_label.argtypes = [_GtkAboutDialog,c_char_p]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_license.restype = None
    libgtk3.gtk_about_dialog_set_license.argtypes = [_GtkAboutDialog,c_char_p]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_artists.restype = None
    libgtk3.gtk_about_dialog_set_artists.argtypes = [_GtkAboutDialog,c_char_p]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_program_name.restype = None
    libgtk3.gtk_about_dialog_set_program_name.argtypes = [_GtkAboutDialog,c_char_p]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_translator_credits.restype = None
    libgtk3.gtk_about_dialog_set_translator_credits.argtypes = [_GtkAboutDialog,c_char_p]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_website.restype = None
    libgtk3.gtk_about_dialog_set_website.argtypes = [_GtkAboutDialog,c_char_p]
except:
   pass
try:
    libgtk3.gtk_about_dialog_set_copyright.restype = None
    libgtk3.gtk_about_dialog_set_copyright.argtypes = [_GtkAboutDialog,c_char_p]
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
    libgtk3.gtk_about_dialog_set_version.argtypes = [_GtkAboutDialog,c_char_p]
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
    libgtk3.gtk_about_dialog_set_comments.argtypes = [_GtkAboutDialog,c_char_p]
except:
   pass
try:
    libgtk3.gtk_about_dialog_get_logo.restype = _GdkPixbuf
    libgtk3.gtk_about_dialog_get_logo.argtypes = [_GtkAboutDialog]
except:
   pass
try:
    libgtk3.gtk_show_about_dialog.restype = None
    libgtk3.gtk_show_about_dialog.argtypes = [_GtkAboutDialog,_GtkWindow,c_char_p,]
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
import gtk3__GtkDialog
class GtkAboutDialog( gtk3__GtkDialog.GtkDialog):
    """Class GtkAboutDialog Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_about_dialog_new.restype = POINTER(c_int)
            
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
        else: logo = POINTER(c_int)()

        
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

        from gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_about_dialog_get_logo( self._object ) or POINTER(c_int)())

    def gtk_show_about_dialog(  self, parent, first_property_name,*args  ):
        if parent: parent = parent._object
        else: parent = POINTER(c_int)()


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

