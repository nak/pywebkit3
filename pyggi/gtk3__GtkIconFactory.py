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
_GdkPixbuf = POINTER(c_void_p)
_GtkRequisition = POINTER(c_void_p)
_GtkRcStyle = POINTER(c_void_p)
_GtkRegionFlags = POINTER(c_void_p)
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
_GScanner = POINTER(c_void_p)
_PangoFont = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GtkTextBuffer = POINTER(c_void_p)
_GtkNumerableIcon = POINTER(c_void_p)
_GdkAppLaunchContext = POINTER(c_void_p)
_GObject = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GtkWidget = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_PangoAttrIterator = POINTER(c_void_p)
_GtkIconSet = POINTER(c_void_p)
_GtkSelectionData = POINTER(c_void_p)
_GtkWindowGroup = POINTER(c_void_p)
_GFileMonitor = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GtkPathPriorityType = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
_PangoAnalysis = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_GScanner = POINTER(c_void_p)
_GtkWidgetClass = POINTER(c_void_p)
_GdkEventKey = POINTER(c_void_p)
_GdkDisplay = POINTER(c_void_p)
_GtkSettings = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_PangoFontMetrics = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
_PangoFontMap = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_cairo_region_t = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontFamily = POINTER(c_void_p)
_GtkClipboard = POINTER(c_void_p)
_PangoFontset = POINTER(c_void_p)
_GdkWindow = POINTER(c_void_p)
_PangoFontDescription = POINTER(c_void_p)
_GtkBorder = POINTER(c_void_p)
_GError = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_cairo_t = POINTER(c_void_p)
_GWeakRef = POINTER(c_void_p)
_GdkVisual = POINTER(c_void_p)
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
_PangoTabArray = POINTER(c_void_p)
_GtkStyleContext = POINTER(c_void_p)
_GValue = POINTER(c_void_p)
_GdkDeviceManager = POINTER(c_void_p)
_GdkCursor = POINTER(c_void_p)
_PangoMatrix = POINTER(c_void_p)
_PangoContext = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_WebKitWebWindowFeatures = POINTER(c_void_p)
_PangoCoverage = POINTER(c_void_p)
_GParamSpec = POINTER(c_void_p)
_GList = POINTER(c_void_p)
_GdkRGBA = POINTER(c_void_p)
_PangoGlyphString = POINTER(c_void_p)
_GObjectClass = POINTER(c_void_p)
_GSList = POINTER(c_void_p)
_GdkWindowAttr = POINTER(c_void_p)
_GdkColor = POINTER(c_void_p)
_GdkRectangle = POINTER(c_void_p)
_PangoLanguage = POINTER(c_void_p)
_PangoAttrList = POINTER(c_void_p)
_gunichar = POINTER(c_void_p)
_GdkWMDecoration = POINTER(c_void_p)
_PangoLogAttr = POINTER(c_void_p)
_PangoLayout = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GParameter = POINTER(c_void_p)
_GtkStyle = POINTER(c_void_p)
_GIcon = POINTER(c_void_p)
_GtkWindow = POINTER(c_void_p)
_cairo_pattern_t = POINTER(c_void_p)
_GdkPixbuf = POINTER(c_void_p)
_GdkScreen = POINTER(c_void_p)
_GtkWidgetPath = POINTER(c_void_p)
_GtkTargetEntry = POINTER(c_void_p)
_GtkApplication = POINTER(c_void_p)
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

try:
    libgtk3.gtk_icon_factory_remove_default.restype = None
    libgtk3.gtk_icon_factory_remove_default.argtypes = [_GtkIconFactory]
except:
   pass
try:
    libgtk3.gtk_icon_factory_add.restype = None
    libgtk3.gtk_icon_factory_add.argtypes = [_GtkIconFactory,Asciifier,_GtkIconSet]
except:
   pass
try:
    libgtk3.gtk_icon_factory_add_default.restype = None
    libgtk3.gtk_icon_factory_add_default.argtypes = [_GtkIconFactory]
except:
   pass
try:
    libgtk3.gtk_icon_factory_lookup.restype = _GtkIconSet
    libgtk3.gtk_icon_factory_lookup.argtypes = [_GtkIconFactory,Asciifier]
except:
   pass
try:
    libgtk3.gtk_icon_factory_lookup_default.restype = _GtkIconSet
    libgtk3.gtk_icon_factory_lookup_default.argtypes = [Asciifier]
except:
   pass
from . import gobject__GObject
class GtkIconFactory( gobject__GObject.GObject):
    """Class GtkIconFactory Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_icon_factory_new.restype = POINTER(c_void_p)
            
            libgtk3.gtk_icon_factory_new.argtypes = []
            self._object = libgtk3.gtk_icon_factory_new()

    """Methods"""
    def remove_default(  self, ):

        
        libgtk3.gtk_icon_factory_remove_default( self._object )

    def add(  self, stock_id, icon_set, ):
        if icon_set: icon_set = icon_set._object
        else: icon_set = POINTER(c_void_p)()

        
        libgtk3.gtk_icon_factory_add( self._object,stock_id,icon_set )

    def add_default(  self, ):

        
        libgtk3.gtk_icon_factory_add_default( self._object )

    def lookup(  self, stock_id, ):

        from .gtk3 import GtkIconSet
        return GtkIconSet(None, obj=libgtk3.gtk_icon_factory_lookup( self._object,stock_id ) or POINTER(c_void_p)())

    @staticmethod
    def lookup_default( stock_id,):
        from .gtk3 import GtkIconSet
        return GtkIconSet( obj=    libgtk3.gtk_icon_factory_lookup_default(stock_id, )
 or POINTER(c_void_p)())
