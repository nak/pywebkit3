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
__GtkWidget = c_void_p
_GtkWidget = c_void_p
__GtkWindow = c_void_p
"""Enumerations"""
GtkMessageType = c_int
GtkButtonsType = c_int

import _gtk3_GtkDialog
class GtkMessageDialog( _gtk3_GtkDialog.GtkDialog):
    """Class GtkMessageDialog Constructors"""
    def __init__( self, parent, flags, type, buttons, message_format,  obj=None, *args):
        if obj: self._object = obj
        else:
            libgtk3.gtk_message_dialog_new.restype = c_void_p
        if parent : parent = parent._object
        else : parent = c_void_p()
        if flags : flags = flags._object
        else : flags = c_void_p()

        libgtk3.gtk_message_dialog_new.argtypes = [_GtkWindow,GtkDialogFlags,GtkMessageType,GtkButtonsType,c_char_p,]
        self._object = libgtk3.gtk_message_dialog_new(parent, flags, type, buttons, message_format, *args )

    """Methods"""
    def get_image(self, ):

        libgtk3.gtk_message_dialog_get_image.restype = _GtkWidget
        libgtk3.gtk_message_dialog_get_image.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_message_dialog_get_image(self._object, ) or c_void_p())

    def format_secondary_text(self,  message_format,*args ):


        def callit( message_format, *args ):
                libgtk3.gtk_message_dialog_format_secondary_text.restype = None
                libgtk3.gtk_message_dialog_format_secondary_text.argtypes = [c_void_p, c_void_p, c_char_p]
                for arg in args:
                     libgtk3.gtk_message_dialog_format_secondary_text.argtypes.append(args[1])
                return libgtk3.gtk_message_dialog_format_secondary_text(self._object, message_format, *args)
    
        return callit( message_format,*args )

    def set_markup(self,  str,):

        libgtk3.gtk_message_dialog_set_markup.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_message_dialog_set_markup(self._object,  str,)

    def format_secondary_markup(self,  message_format,*args ):


        def callit( message_format, *args ):
                libgtk3.gtk_message_dialog_format_secondary_markup.restype = None
                libgtk3.gtk_message_dialog_format_secondary_markup.argtypes = [c_void_p, c_void_p, c_char_p]
                for arg in args:
                     libgtk3.gtk_message_dialog_format_secondary_markup.argtypes.append(args[1])
                return libgtk3.gtk_message_dialog_format_secondary_markup(self._object, message_format, *args)
    
        return callit( message_format,*args )

    def get_message_area(self, ):

        libgtk3.gtk_message_dialog_get_message_area.restype = _GtkWidget
        libgtk3.gtk_message_dialog_get_message_area.argtypes = [c_void_p]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_message_dialog_get_message_area(self._object, ) or c_void_p())

    def set_image(self,  image,):
        if image : image = image._object
        else : image = c_void_p()

        libgtk3.gtk_message_dialog_set_image.argtypes = [c_void_p, _GtkWidget]
        
        libgtk3.gtk_message_dialog_set_image(self._object,  image,)

    @staticmethod
    def new_with_markup( parent, flags, type, buttons, message_format,*args ):
        if parent : parent = parent._object
        else : parent = c_void_p()
        if flags : flags = flags._object
        else : flags = c_void_p()
        libgtk3.gtk_message_dialog_new_with_markup.restype = _GtkWidget
        libgtk3.gtk_message_dialog_new_with_markup.argtypes = [_GtkWindow,GtkDialogFlags,GtkMessageType,GtkButtonsType,c_char_p,]
        return libgtk3.gtk_message_dialog_new_with_markup(parent, flags, type, buttons, message_format, *args)

