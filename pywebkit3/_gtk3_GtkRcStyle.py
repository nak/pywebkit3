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
_GdkDisplay = c_void_p
__GtkStyleProvider = c_void_p
_GScanner = c_void_p
_PangoFont = c_void_p
_GtkStyleContext = c_void_p
_guchar = c_void_p
_GdkAppLaunchContext = c_void_p
__PangoLayout = c_void_p
__GParamSpec = c_void_p
__PangoAttrIterator = c_void_p
__GtkWindow = c_void_p
_GtkWindowGroup = c_void_p
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
__GScanner = c_void_p
__GtkWidgetClass = c_void_p
__GdkEventKey = c_void_p
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
__GdkVisual = c_void_p
_GdkDevice = c_void_p
_GList = c_void_p
__GtkAccelGroup = c_void_p
_GtkIconSet = c_void_p
__GtkAllocation = c_void_p
__GtkWidget = c_void_p
_gchar = c_void_p
__GValue = c_void_p
_GdkDeviceManager = c_void_p
_GdkCursor = c_void_p
__PangoMatrix = c_void_p
_PangoContext = c_void_p
__GList = c_void_p
_PangoCoverage = c_void_p
_GParamSpec = c_void_p
__PangoRectangle = c_void_p
__GtkIconSource = c_void_p
_char = c_void_p
__PangoGlyphString = c_void_p
__GSList = c_void_p
__GdkRGBA = c_void_p
__GdkWindowAttr = c_void_p
__GdkColor = c_void_p
__GdkRectangle = c_void_p
__PangoLanguage = c_void_p
__GdkWMDecoration = c_void_p
__PangoLogAttr = c_void_p
_PangoLayout = c_void_p
_GtkStyle = c_void_p
__GtkStyle = c_void_p
__GIcon = c_void_p
__cairo_pattern_t = c_void_p
__GdkPixbuf = c_void_p
_GtkSettings = c_void_p
__GtkApplication = c_void_p
_GtkClipboard = c_void_p
__GdkScreen = c_void_p
_PangoLanguage = c_void_p
__GdkDevice = c_void_p
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

import _gobject_GObject
class GtkRcStyle( _gobject_GObject.GObject):
    """Class GtkRcStyle Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_rc_style_new.restype = c_void_p

        libgtk3.gtk_rc_style_new.argtypes = []
        self._object = libgtk3.gtk_rc_style_new()

    """Methods"""
    def gtk_rc_set_default_files(self,  filenames,):

        libgtk3.gtk_rc_set_default_files.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_rc_set_default_files(self._object,  filenames,)

    def gtk_rc_parse(self,  filename,):

        libgtk3.gtk_rc_parse.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_rc_parse(self._object,  filename,)

    def copy(self, ):

        libgtk3.gtk_rc_style_copy.restype = _GtkRcStyle
        libgtk3.gtk_rc_style_copy.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkRcStyle
        return GtkRcStyle(None, obj=libgtk3.gtk_rc_style_copy(self._object, ) or c_void_p())

    def gtk_rc_reset_styles(self,  settings,):
        if settings : settings = settings._object
        else : settings = c_void_p()

        libgtk3.gtk_rc_reset_styles.argtypes = [c_void_p, _GtkSettings]
        
        libgtk3.gtk_rc_reset_styles(self._object,  settings,)

    def gtk_rc_parse_string(self,  rc_string,):

        libgtk3.gtk_rc_parse_string.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_rc_parse_string(self._object,  rc_string,)

    def gtk_rc_add_default_file(self,  filename,):

        libgtk3.gtk_rc_add_default_file.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_rc_add_default_file(self._object,  filename,)

    @staticmethod
    def gtk_rc_parse_state( scanner, state,):
        if scanner : scanner = scanner._object
        else : scanner = c_void_p()
        if state : state = state._object
        else : state = c_void_p()
        libgtk3.gtk_rc_parse_state.restype = guint
        libgtk3.gtk_rc_parse_state.argtypes = [_GScanner,POITNER(GtkStateType)]
        return libgtk3.gtk_rc_parse_state(scanner, state, )

    @staticmethod
    def gtk_rc_get_default_files():
        libgtk3.gtk_rc_get_default_files.restype = _gchar
        return libgtk3.gtk_rc_get_default_files()

    @staticmethod
    def gtk_rc_get_im_module_file():
        libgtk3.gtk_rc_get_im_module_file.restype = _gchar
        return libgtk3.gtk_rc_get_im_module_file()

    @staticmethod
    def gtk_rc_parse_color( scanner, color,):
        if scanner : scanner = scanner._object
        else : scanner = c_void_p()
        if color : color = color._object
        else : color = c_void_p()
        libgtk3.gtk_rc_parse_color.restype = guint
        libgtk3.gtk_rc_parse_color.argtypes = [_GScanner,_GdkColor]
        return libgtk3.gtk_rc_parse_color(scanner, color, )

    @staticmethod
    def gtk_rc_get_im_module_path():
        libgtk3.gtk_rc_get_im_module_path.restype = _gchar
        return libgtk3.gtk_rc_get_im_module_path()

    @staticmethod
    def gtk_rc_parse_color_full( scanner, style, color,):
        if scanner : scanner = scanner._object
        else : scanner = c_void_p()
        if style : style = style._object
        else : style = c_void_p()
        if color : color = color._object
        else : color = c_void_p()
        libgtk3.gtk_rc_parse_color_full.restype = guint
        libgtk3.gtk_rc_parse_color_full.argtypes = [_GScanner,_GtkRcStyle,_GdkColor]
        return libgtk3.gtk_rc_parse_color_full(scanner, style, color, )

    @staticmethod
    def gtk_rc_find_module_in_path( module_file,):
        libgtk3.gtk_rc_find_module_in_path.restype = _gchar
        libgtk3.gtk_rc_find_module_in_path.argtypes = [c_char_p]
        return libgtk3.gtk_rc_find_module_in_path(module_file, )

    @staticmethod
    def gtk_rc_parse_priority( scanner, priority,):
        if scanner : scanner = scanner._object
        else : scanner = c_void_p()
        if priority : priority = priority._object
        else : priority = c_void_p()
        libgtk3.gtk_rc_parse_priority.restype = guint
        libgtk3.gtk_rc_parse_priority.argtypes = [_GScanner,_GtkPathPriorityType]
        return libgtk3.gtk_rc_parse_priority(scanner, priority, )

    @staticmethod
    def gtk_rc_reparse_all_for_settings( settings, force_load,):
        if settings : settings = settings._object
        else : settings = c_void_p()
        libgtk3.gtk_rc_reparse_all_for_settings.restype = gboolean
        libgtk3.gtk_rc_reparse_all_for_settings.argtypes = [_GtkSettings,gboolean]
        return libgtk3.gtk_rc_reparse_all_for_settings(settings, force_load, )

    @staticmethod
    def gtk_rc_get_theme_dir():
        libgtk3.gtk_rc_get_theme_dir.restype = _gchar
        return libgtk3.gtk_rc_get_theme_dir()

    @staticmethod
    def gtk_rc_get_style_by_paths( settings, widget_path, class_path, type,):
        if settings : settings = settings._object
        else : settings = c_void_p()
        libgtk3.gtk_rc_get_style_by_paths.restype = _GtkStyle
        libgtk3.gtk_rc_get_style_by_paths.argtypes = [_GtkSettings,c_char_p,c_char_p,GType]
        return libgtk3.gtk_rc_get_style_by_paths(settings, widget_path, class_path, type, )

    @staticmethod
    def gtk_rc_reparse_all():
        libgtk3.gtk_rc_reparse_all.restype = gboolean
        return libgtk3.gtk_rc_reparse_all()

    @staticmethod
    def gtk_rc_find_pixmap_in_path( settings, scanner, pixmap_file,):
        if settings : settings = settings._object
        else : settings = c_void_p()
        if scanner : scanner = scanner._object
        else : scanner = c_void_p()
        libgtk3.gtk_rc_find_pixmap_in_path.restype = _gchar
        libgtk3.gtk_rc_find_pixmap_in_path.argtypes = [_GtkSettings,_GScanner,c_char_p]
        return libgtk3.gtk_rc_find_pixmap_in_path(settings, scanner, pixmap_file, )

    @staticmethod
    def gtk_rc_get_module_dir():
        libgtk3.gtk_rc_get_module_dir.restype = _gchar
        return libgtk3.gtk_rc_get_module_dir()

    @staticmethod
    def gtk_rc_get_style( widget,):
        if widget : widget = widget._object
        else : widget = c_void_p()
        libgtk3.gtk_rc_get_style.restype = _GtkStyle
        libgtk3.gtk_rc_get_style.argtypes = [_GtkWidget]
        return libgtk3.gtk_rc_get_style(widget, )

