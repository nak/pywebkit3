#!/usr/bin/env python
from pyggi.gtk3 import GtkWindow, GtkScrolledWindow
from pyggi import gtk3
from pyggi.webkit3 import WebKitWebView

window = GtkWindow( gtk3.GTK_WINDOW_TOPLEVEL )
window.set_default_size( 1200, 800 )
window.set_title("Example1: Load a Web Page")
scrolled = GtkScrolledWindow( None, None )
window.add( scrolled )
webview = WebKitWebView()
scrolled.add( webview )

webview.open( "http://www.python.org" )

window.show_all()
window.connect( "delete-event", gtk3.main_quit )

def main():
    gtk3.main()

if __name__ == "__main__":
    main()
