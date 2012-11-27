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
__GtkTextBuffer = c_void_p
_guchar = c_void_p
_GdkAppLaunchContext = c_void_p
__GObject = c_void_p
__PangoLayout = c_void_p
__GParamSpec = c_void_p
__PangoAttrIterator = c_void_p
__GtkWindow = c_void_p
_GtkSelectionData = c_void_p
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
_guint8 = c_void_p
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
_GObject = c_void_p
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
__GtkTargetEntry = c_void_p
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
class GtkClipboard( _gobject_GObject.GObject):
    """Class GtkClipboard Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def set_with_owner(self,  targets, n_targets, get_func, clear_func, owner,):
        if targets : targets = targets._object
        else : targets = c_void_p()
        if owner : owner = owner._object
        else : owner = c_void_p()

        libgtk3.gtk_clipboard_set_with_owner.restype = gboolean
        libgtk3.gtk_clipboard_set_with_owner.argtypes = [c_void_p, _GtkTargetEntry,guint,GtkClipboardGetFunc,GtkClipboardClearFunc,_GObject]
        
        return libgtk3.gtk_clipboard_set_with_owner(self._object,  targets, n_targets, get_func, clear_func, owner,)

    def store(self, ):

        libgtk3.gtk_clipboard_store.argtypes = [c_void_p]
        
        libgtk3.gtk_clipboard_store(self._object, )

    def get_owner(self, ):

        libgtk3.gtk_clipboard_get_owner.restype = _GObject
        libgtk3.gtk_clipboard_get_owner.argtypes = [c_void_p]
        from pywebkit3.gobject import GObject
        return GObject(None,None,None,None, obj=libgtk3.gtk_clipboard_get_owner(self._object, ) or c_void_p())

    def wait_is_target_available(self,  target,):
        if target : target = target._object
        else : target = c_void_p()

        libgtk3.gtk_clipboard_wait_is_target_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_target_available.argtypes = [c_void_p, c_void_p]
        
        return libgtk3.gtk_clipboard_wait_is_target_available(self._object,  target,)

    def request_contents(self,  target, callback, user_data,):
        if target : target = target._object
        else : target = c_void_p()

        libgtk3.gtk_clipboard_request_contents.argtypes = [c_void_p, c_void_p,GtkClipboardReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_contents(self._object,  target, callback, user_data,)

    def clear(self, ):

        libgtk3.gtk_clipboard_clear.argtypes = [c_void_p]
        
        libgtk3.gtk_clipboard_clear(self._object, )

    def set_text(self,  text, len,):

        libgtk3.gtk_clipboard_set_text.argtypes = [c_void_p, c_char_p,gint]
        
        libgtk3.gtk_clipboard_set_text(self._object,  text, len,)

    def request_text(self,  callback, user_data,):

        libgtk3.gtk_clipboard_request_text.argtypes = [c_void_p, GtkClipboardTextReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_text(self._object,  callback, user_data,)

    def wait_for_targets(self,  targets, n_targets,):
        if targets : targets = targets._object
        else : targets = c_void_p()
        if n_targets : n_targets = n_targets._object
        else : n_targets = c_void_p()

        libgtk3.gtk_clipboard_wait_for_targets.restype = gboolean
        libgtk3.gtk_clipboard_wait_for_targets.argtypes = [c_void_p, _GdkAtom,POITNER(gint)]
        
        return libgtk3.gtk_clipboard_wait_for_targets(self._object,  targets, n_targets,)

    def wait_for_contents(self,  target,):
        if target : target = target._object
        else : target = c_void_p()

        libgtk3.gtk_clipboard_wait_for_contents.restype = _GtkSelectionData
        libgtk3.gtk_clipboard_wait_for_contents.argtypes = [c_void_p, c_void_p]
        from pywebkit3.gtk3 import GtkSelectionData
        return GtkSelectionData( obj=libgtk3.gtk_clipboard_wait_for_contents(self._object,  target,) or c_void_p())

    def set_can_store(self,  targets, n_targets,):
        if targets : targets = targets._object
        else : targets = c_void_p()

        libgtk3.gtk_clipboard_set_can_store.argtypes = [c_void_p, _GtkTargetEntry,gint]
        
        libgtk3.gtk_clipboard_set_can_store(self._object,  targets, n_targets,)

    def request_targets(self,  callback, user_data,):

        libgtk3.gtk_clipboard_request_targets.argtypes = [c_void_p, GtkClipboardTargetsReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_targets(self._object,  callback, user_data,)

    def wait_is_rich_text_available(self,  buffer,):
        if buffer : buffer = buffer._object
        else : buffer = c_void_p()

        libgtk3.gtk_clipboard_wait_is_rich_text_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_rich_text_available.argtypes = [c_void_p, _GtkTextBuffer]
        
        return libgtk3.gtk_clipboard_wait_is_rich_text_available(self._object,  buffer,)

    def wait_for_image(self, ):

        libgtk3.gtk_clipboard_wait_for_image.restype = _GdkPixbuf
        libgtk3.gtk_clipboard_wait_for_image.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_clipboard_wait_for_image(self._object, ) or c_void_p())

    def wait_for_rich_text(self,  buffer, format, length,):
        if buffer : buffer = buffer._object
        else : buffer = c_void_p()
        if format : format = format._object
        else : format = c_void_p()
        if length : length = length._object
        else : length = c_void_p()

        libgtk3.gtk_clipboard_wait_for_rich_text.restype = _guint8
        libgtk3.gtk_clipboard_wait_for_rich_text.argtypes = [c_void_p, _GtkTextBuffer,_GdkAtom,POITNER(gsize)]
        
        return libgtk3.gtk_clipboard_wait_for_rich_text(self._object,  buffer, format, length,)

    def wait_for_text(self, ):

        libgtk3.gtk_clipboard_wait_for_text.restype = _gchar
        libgtk3.gtk_clipboard_wait_for_text.argtypes = [c_void_p]
        
        return libgtk3.gtk_clipboard_wait_for_text(self._object, )

    def get_display(self, ):

        libgtk3.gtk_clipboard_get_display.restype = _GdkDisplay
        libgtk3.gtk_clipboard_get_display.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkDisplay
        return GdkDisplay( obj=libgtk3.gtk_clipboard_get_display(self._object, ) or c_void_p())

    def wait_for_uris(self, ):

        libgtk3.gtk_clipboard_wait_for_uris.restype = _gchar
        libgtk3.gtk_clipboard_wait_for_uris.argtypes = [c_void_p]
        
        return libgtk3.gtk_clipboard_wait_for_uris(self._object, )

    def set_with_data(self,  targets, n_targets, get_func, clear_func, user_data,):
        if targets : targets = targets._object
        else : targets = c_void_p()

        libgtk3.gtk_clipboard_set_with_data.restype = gboolean
        libgtk3.gtk_clipboard_set_with_data.argtypes = [c_void_p, _GtkTargetEntry,guint,GtkClipboardGetFunc,GtkClipboardClearFunc,gpointer]
        
        return libgtk3.gtk_clipboard_set_with_data(self._object,  targets, n_targets, get_func, clear_func, user_data,)

    def wait_is_text_available(self, ):

        libgtk3.gtk_clipboard_wait_is_text_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_text_available.argtypes = [c_void_p]
        
        return libgtk3.gtk_clipboard_wait_is_text_available(self._object, )

    def request_uris(self,  callback, user_data,):

        libgtk3.gtk_clipboard_request_uris.argtypes = [c_void_p, GtkClipboardURIReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_uris(self._object,  callback, user_data,)

    def wait_is_uris_available(self, ):

        libgtk3.gtk_clipboard_wait_is_uris_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_uris_available.argtypes = [c_void_p]
        
        return libgtk3.gtk_clipboard_wait_is_uris_available(self._object, )

    def wait_is_image_available(self, ):

        libgtk3.gtk_clipboard_wait_is_image_available.restype = gboolean
        libgtk3.gtk_clipboard_wait_is_image_available.argtypes = [c_void_p]
        
        return libgtk3.gtk_clipboard_wait_is_image_available(self._object, )

    def request_rich_text(self,  buffer, callback, user_data,):
        if buffer : buffer = buffer._object
        else : buffer = c_void_p()

        libgtk3.gtk_clipboard_request_rich_text.argtypes = [c_void_p, _GtkTextBuffer,GtkClipboardRichTextReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_rich_text(self._object,  buffer, callback, user_data,)

    def set_image(self,  pixbuf,):
        if pixbuf : pixbuf = pixbuf._object
        else : pixbuf = c_void_p()

        libgtk3.gtk_clipboard_set_image.argtypes = [c_void_p, _GdkPixbuf]
        
        libgtk3.gtk_clipboard_set_image(self._object,  pixbuf,)

    def request_image(self,  callback, user_data,):

        libgtk3.gtk_clipboard_request_image.argtypes = [c_void_p, GtkClipboardImageReceivedFunc,gpointer]
        
        libgtk3.gtk_clipboard_request_image(self._object,  callback, user_data,)

    @staticmethod
    def get( selection,):
        if selection : selection = selection._object
        else : selection = c_void_p()
        libgtk3.gtk_clipboard_get.restype = _GtkClipboard
        libgtk3.gtk_clipboard_get.argtypes = [c_void_p]
        return libgtk3.gtk_clipboard_get(selection, )

    @staticmethod
    def get_for_display( display, selection,):
        if display : display = display._object
        else : display = c_void_p()
        if selection : selection = selection._object
        else : selection = c_void_p()
        libgtk3.gtk_clipboard_get_for_display.restype = _GtkClipboard
        libgtk3.gtk_clipboard_get_for_display.argtypes = [_GdkDisplay,c_void_p]
        return libgtk3.gtk_clipboard_get_for_display(display, selection, )

