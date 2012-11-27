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
__GtkRcStyle = c_void_p
__GdkGeometry = c_void_p
_GdkPixbuf = c_void_p
__GtkRequisition = c_void_p
_GtkRcStyle = c_void_p
__GtkRegionFlags = c_void_p
_GdkEvent = c_void_p
_GtkWindow = c_void_p
__cairo_font_options_t = c_void_p
__GdkAtom = c_void_p
__GdkTimeCoord = c_void_p
__GtkWidgetPath = c_void_p
__GClosure = c_void_p
_GdkDisplay = c_void_p
__GtkStyleProvider = c_void_p
_GScanner = c_void_p
_PangoFont = c_void_p
_GtkStyleContext = c_void_p
__GtkTextBuffer = c_void_p
_guchar = c_void_p
_GdkAppLaunchContext = c_void_p
__GObject = c_void_p
__PangoLayout = c_void_p
__GParamSpec = c_void_p
__PangoAttrIterator = c_void_p
_GtkIconSet = c_void_p
_GtkSelectionData = c_void_p
_GtkWindowGroup = c_void_p
_GtkAdjustment = c_void_p
_PangoLogAttr = c_void_p
__PangoContext = c_void_p
__GtkPathPriorityType = c_void_p
__GtkSettings = c_void_p
__PangoFontMap = c_void_p
__PangoAttrList = c_void_p
_PangoMatrix = c_void_p
_GtkApplication = c_void_p
__PangoAnalysis = c_void_p
_PangoFontDescription = c_void_p
__GdkCursor = c_void_p
_guint8 = c_void_p
__GScanner = c_void_p
__GtkWidgetClass = c_void_p
__GdkEventKey = c_void_p
__GtkAdjustment = c_void_p
__GdkDisplay = c_void_p
_GtkWidgetPath = c_void_p
_GdkScreen = c_void_p
_PangoFontMetrics = c_void_p
_GdkVisual = c_void_p
_PangoFontMap = c_void_p
_GSList = c_void_p
_GtkWidget = c_void_p
__GdkWindow = c_void_p
__PangoFontFamily = c_void_p
__cairo_region_t = c_void_p
_PangoFontset = c_void_p
_GdkWindow = c_void_p
__PangoFontDescription = c_void_p
__GtkBorder = c_void_p
__GError = c_void_p
__PangoCoverage = c_void_p
__cairo_t = c_void_p
__GWeakRef = c_void_p
__GdkVisual = c_void_p
_GdkDevice = c_void_p
_GList = c_void_p
__GtkAccelGroup = c_void_p
_GObject = c_void_p
__GtkIconSource = c_void_p
__GtkAllocation = c_void_p
__GtkWidget = c_void_p
_PangoLayoutLine = c_void_p
_gchar = c_void_p
__PangoTabArray = c_void_p
__GValue = c_void_p
_GdkDeviceManager = c_void_p
_GdkCursor = c_void_p
__PangoMatrix = c_void_p
_PangoContext = c_void_p
__GList = c_void_p
_PangoCoverage = c_void_p
_GParamSpec = c_void_p
__PangoRectangle = c_void_p
__GdkRGBA = c_void_p
_char = c_void_p
__PangoGlyphString = c_void_p
__GObjectClass = c_void_p
__GSList = c_void_p
__GdkWindowAttr = c_void_p
__GdkColor = c_void_p
__GdkRectangle = c_void_p
__PangoLanguage = c_void_p
_PangoAttrList = c_void_p
__gunichar = c_void_p
__GdkWMDecoration = c_void_p
__PangoLogAttr = c_void_p
_PangoLayout = c_void_p
_GtkStyle = c_void_p
__GParameter = c_void_p
__GtkStyle = c_void_p
__GIcon = c_void_p
__GtkWindow = c_void_p
__cairo_pattern_t = c_void_p
__GdkPixbuf = c_void_p
_GtkSettings = c_void_p
__GtkTargetEntry = c_void_p
__GtkApplication = c_void_p
_GtkClipboard = c_void_p
__GdkScreen = c_void_p
_PangoLanguage = c_void_p
__GdkDevice = c_void_p
_PangoTabArray = c_void_p
"""Enumerations"""
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
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int

import _gobject_GObject
class GtkAdjustment( _gobject_GObject.GObject):
    """Class GtkAdjustment Constructors"""
    def __init__( self, page_size,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_adjustment_new.restype = c_void_p

        libgtk3.gtk_adjustment_new.argtypes = [gdouble]
        self._object = libgtk3.gtk_adjustment_new(page_size, )

    """Methods"""
    def get_page_size(self, ):

        libgtk3.gtk_adjustment_get_page_size.restype = gdouble
        libgtk3.gtk_adjustment_get_page_size.argtypes = [c_void_p]
        
        return libgtk3.gtk_adjustment_get_page_size(self._object, )

    def get_value(self, ):

        libgtk3.gtk_adjustment_get_value.restype = gdouble
        libgtk3.gtk_adjustment_get_value.argtypes = [c_void_p]
        
        return libgtk3.gtk_adjustment_get_value(self._object, )

    def get_upper(self, ):

        libgtk3.gtk_adjustment_get_upper.restype = gdouble
        libgtk3.gtk_adjustment_get_upper.argtypes = [c_void_p]
        
        return libgtk3.gtk_adjustment_get_upper(self._object, )

    def configure(self,  value, lower, upper, step_increment, page_increment, page_size,):

        libgtk3.gtk_adjustment_configure.argtypes = [c_void_p, gdouble,gdouble,gdouble,gdouble,gdouble,gdouble]
        
        libgtk3.gtk_adjustment_configure(self._object,  value, lower, upper, step_increment, page_increment, page_size,)

    def set_upper(self,  upper,):

        libgtk3.gtk_adjustment_set_upper.argtypes = [c_void_p, gdouble]
        
        libgtk3.gtk_adjustment_set_upper(self._object,  upper,)

    def get_page_increment(self, ):

        libgtk3.gtk_adjustment_get_page_increment.restype = gdouble
        libgtk3.gtk_adjustment_get_page_increment.argtypes = [c_void_p]
        
        return libgtk3.gtk_adjustment_get_page_increment(self._object, )

    def value_changed(self, ):

        libgtk3.gtk_adjustment_value_changed.argtypes = [c_void_p]
        
        libgtk3.gtk_adjustment_value_changed(self._object, )

    def set_page_size(self,  page_size,):

        libgtk3.gtk_adjustment_set_page_size.argtypes = [c_void_p, gdouble]
        
        libgtk3.gtk_adjustment_set_page_size(self._object,  page_size,)

    def set_page_increment(self,  page_increment,):

        libgtk3.gtk_adjustment_set_page_increment.argtypes = [c_void_p, gdouble]
        
        libgtk3.gtk_adjustment_set_page_increment(self._object,  page_increment,)

    def get_lower(self, ):

        libgtk3.gtk_adjustment_get_lower.restype = gdouble
        libgtk3.gtk_adjustment_get_lower.argtypes = [c_void_p]
        
        return libgtk3.gtk_adjustment_get_lower(self._object, )

    def changed(self, ):

        libgtk3.gtk_adjustment_changed.argtypes = [c_void_p]
        
        libgtk3.gtk_adjustment_changed(self._object, )

    def get_step_increment(self, ):

        libgtk3.gtk_adjustment_get_step_increment.restype = gdouble
        libgtk3.gtk_adjustment_get_step_increment.argtypes = [c_void_p]
        
        return libgtk3.gtk_adjustment_get_step_increment(self._object, )

    def set_value(self,  value,):

        libgtk3.gtk_adjustment_set_value.argtypes = [c_void_p, gdouble]
        
        libgtk3.gtk_adjustment_set_value(self._object,  value,)

    def set_step_increment(self,  step_increment,):

        libgtk3.gtk_adjustment_set_step_increment.argtypes = [c_void_p, gdouble]
        
        libgtk3.gtk_adjustment_set_step_increment(self._object,  step_increment,)

    def clamp_page(self,  lower, upper,):

        libgtk3.gtk_adjustment_clamp_page.argtypes = [c_void_p, gdouble,gdouble]
        
        libgtk3.gtk_adjustment_clamp_page(self._object,  lower, upper,)

    def set_lower(self,  lower,):

        libgtk3.gtk_adjustment_set_lower.argtypes = [c_void_p, gdouble]
        
        libgtk3.gtk_adjustment_set_lower(self._object,  lower,)

