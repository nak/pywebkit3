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
__GdkPixbuf = c_void_p
_gchar = c_void_p
_GdkPixbuf = c_void_p
_GtkWidget = c_void_p
__GtkWindow = c_void_p
"""Enumerations"""
GtkLicense = c_int

import _gtk3_GtkDialog
class GtkAboutDialog( _gtk3_GtkDialog.GtkDialog):
    """Class GtkAboutDialog Constructors"""
    def __init__( self,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_about_dialog_new.restype = c_void_p

        libgtk3.gtk_about_dialog_new.argtypes = []
        self._object = libgtk3.gtk_about_dialog_new()

    """Methods"""
    def set_authors(self,  authors,):

        libgtk3.gtk_about_dialog_set_authors.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_authors(self._object,  authors,)

    def get_website_label(self, ):

        libgtk3.gtk_about_dialog_get_website_label.restype = _gchar
        libgtk3.gtk_about_dialog_get_website_label.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_website_label(self._object, )

    def set_license_type(self,  license_type,):

        libgtk3.gtk_about_dialog_set_license_type.argtypes = [c_void_p, GtkLicense]
        
        libgtk3.gtk_about_dialog_set_license_type(self._object,  license_type,)

    def get_artists(self, ):

        libgtk3.gtk_about_dialog_get_artists.restype = _gchar
        libgtk3.gtk_about_dialog_get_artists.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_artists(self._object, )

    def set_logo_icon_name(self,  icon_name,):

        libgtk3.gtk_about_dialog_set_logo_icon_name.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_logo_icon_name(self._object,  icon_name,)

    def set_documenters(self,  documenters,):

        libgtk3.gtk_about_dialog_set_documenters.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_documenters(self._object,  documenters,)

    def get_license(self, ):

        libgtk3.gtk_about_dialog_get_license.restype = _gchar
        libgtk3.gtk_about_dialog_get_license.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_license(self._object, )

    def set_logo(self,  logo,):
        if logo : logo = logo._object
        else : logo = c_void_p()

        libgtk3.gtk_about_dialog_set_logo.argtypes = [c_void_p, _GdkPixbuf]
        
        libgtk3.gtk_about_dialog_set_logo(self._object,  logo,)

    def set_website_label(self,  website_label,):

        libgtk3.gtk_about_dialog_set_website_label.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_website_label(self._object,  website_label,)

    def set_license(self,  license,):

        libgtk3.gtk_about_dialog_set_license.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_license(self._object,  license,)

    def set_artists(self,  artists,):

        libgtk3.gtk_about_dialog_set_artists.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_artists(self._object,  artists,)

    def set_program_name(self,  name,):

        libgtk3.gtk_about_dialog_set_program_name.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_program_name(self._object,  name,)

    def set_translator_credits(self,  translator_credits,):

        libgtk3.gtk_about_dialog_set_translator_credits.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_translator_credits(self._object,  translator_credits,)

    def set_website(self,  website,):

        libgtk3.gtk_about_dialog_set_website.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_website(self._object,  website,)

    def set_copyright(self,  copyright,):

        libgtk3.gtk_about_dialog_set_copyright.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_copyright(self._object,  copyright,)

    def get_authors(self, ):

        libgtk3.gtk_about_dialog_get_authors.restype = _gchar
        libgtk3.gtk_about_dialog_get_authors.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_authors(self._object, )

    def get_logo_icon_name(self, ):

        libgtk3.gtk_about_dialog_get_logo_icon_name.restype = _gchar
        libgtk3.gtk_about_dialog_get_logo_icon_name.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_logo_icon_name(self._object, )

    def set_wrap_license(self,  wrap_license,):

        libgtk3.gtk_about_dialog_set_wrap_license.argtypes = [c_void_p, gboolean]
        
        libgtk3.gtk_about_dialog_set_wrap_license(self._object,  wrap_license,)

    def get_documenters(self, ):

        libgtk3.gtk_about_dialog_get_documenters.restype = _gchar
        libgtk3.gtk_about_dialog_get_documenters.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_documenters(self._object, )

    def get_wrap_license(self, ):

        libgtk3.gtk_about_dialog_get_wrap_license.restype = gboolean
        libgtk3.gtk_about_dialog_get_wrap_license.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_wrap_license(self._object, )

    def set_version(self,  version,):

        libgtk3.gtk_about_dialog_set_version.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_version(self._object,  version,)

    def get_translator_credits(self, ):

        libgtk3.gtk_about_dialog_get_translator_credits.restype = _gchar
        libgtk3.gtk_about_dialog_get_translator_credits.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_translator_credits(self._object, )

    def get_program_name(self, ):

        libgtk3.gtk_about_dialog_get_program_name.restype = _gchar
        libgtk3.gtk_about_dialog_get_program_name.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_program_name(self._object, )

    def set_comments(self,  comments,):

        libgtk3.gtk_about_dialog_set_comments.argtypes = [c_void_p, c_char_p]
        
        libgtk3.gtk_about_dialog_set_comments(self._object,  comments,)

    def get_logo(self, ):

        libgtk3.gtk_about_dialog_get_logo.restype = _GdkPixbuf
        libgtk3.gtk_about_dialog_get_logo.argtypes = [c_void_p]
        from pywebkit3.gobject import GdkPixbuf
        return GdkPixbuf( obj=libgtk3.gtk_about_dialog_get_logo(self._object, ) or c_void_p())

    def gtk_show_about_dialog(self,  parent, first_property_name,*args ):
        if parent : parent = parent._object
        else : parent = c_void_p()


        def callit( parent, first_property_name, *args ):
                libgtk3.gtk_show_about_dialog.restype = None
                libgtk3.gtk_show_about_dialog.argtypes = [c_void_p, c_void_p, _GtkWindow, c_char_p]
                for arg in args:
                     libgtk3.gtk_show_about_dialog.argtypes.append(args[1])
                return libgtk3.gtk_show_about_dialog(self._object, parent, first_property_name, *args)
    
        return callit( parent, first_property_name,*args )

    def get_license_type(self, ):

        libgtk3.gtk_about_dialog_get_license_type.restype = GtkLicense
        libgtk3.gtk_about_dialog_get_license_type.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_license_type(self._object, )

    def get_copyright(self, ):

        libgtk3.gtk_about_dialog_get_copyright.restype = _gchar
        libgtk3.gtk_about_dialog_get_copyright.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_copyright(self._object, )

    def get_version(self, ):

        libgtk3.gtk_about_dialog_get_version.restype = _gchar
        libgtk3.gtk_about_dialog_get_version.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_version(self._object, )

    def get_website(self, ):

        libgtk3.gtk_about_dialog_get_website.restype = _gchar
        libgtk3.gtk_about_dialog_get_website.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_website(self._object, )

    def get_comments(self, ):

        libgtk3.gtk_about_dialog_get_comments.restype = _gchar
        libgtk3.gtk_about_dialog_get_comments.argtypes = [c_void_p]
        
        return libgtk3.gtk_about_dialog_get_comments(self._object, )

