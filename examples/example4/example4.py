#!/usr/bin/env python
import os.path
import sys
sys.path = [ os.path.dirname(__file__), os.path.abspath( os.path.join( os.path.dirname(__file__),"..", ".."))] + \
           sys.path

import aquarium
from pyggi.gtk3 import GtkWindow, GtkScrolledWindow
from pyggi import gtk3
from pyggi.webkit3 import WebKitWebView, WebKitWebSettings

window = GtkWindow( gtk3.GTK_WINDOW_TOPLEVEL )
window.set_default_size( 1200, 800 )
window.set_title("Example1: Load a Web Page")
scrolled = GtkScrolledWindow( None, None )
window.add( scrolled )
webview = WebKitWebView()
settings = webview.get_settings()
statc = settings.set( "enable-webgl", True, None )
webview.set_settings( settings )
aquarium.initialize_aquarium( webview.get_env(), webview.on_view_ready)
import logging
logging.error("ENABLE: ")
scrolled.add( webview )

#webview.open( "http://learningwebgl.com/lessons/lesson04/index.html" )
webview.open( "http://webglsamples.googlecode.com/hg/aquarium/aquarium.html")
window.show_all()
window.connect( "delete-event", gtk3.main_quit )


def main():
    
    gtk3.main()

if __name__ == "__main__":
    main()
