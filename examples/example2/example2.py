#!/usr/bin/env python
import sys
import os.path
sys.path = [os.path.dirname(__file__)+"/../../"]+sys.path
print sys.path
from pyggi.gtk3 import GtkWindow, GtkScrolledWindow
from pyggi import gtk3
from pyggi.webkit3 import WebKitWebView

from pyggi import gobject

#Create the GUI component stack
window = GtkWindow( gtk3.GTK_WINDOW_TOPLEVEL )
window.set_default_size( 1200, 800 )
window.set_title("Example2: Use Python to Manipulate a Javascript Element")
scrolled = GtkScrolledWindow( None, None )
window.add( scrolled )
webview = WebKitWebView()
scrolled.add( webview )

#open the example html in the view and show all components
import os.path
webview.open( os.path.join( os.path.dirname(os.path.abspath(__file__)),"example2.html" ))
window.show_all()



#set up a loop to continually increment the color via a gobject timeout add function:
color = int("00FF00",16)
increment = 0
def update_color( ):
    global color
    global increment
    hex_color = "#%0.6X"%color
    webview._color_block.set_color( hex_color )
    color += increment + (increment/2)*256 + (increment/4)*256*256
    if color > int('FFFFFF',16):
        color = 0
    increment += 1
    return True


#to be called only once the webpage loads:
def start_update():
    webview._color_block = webview.get_jsobject( "color_block", can_call=False)
    assert(webview._color_block)
    gobject.timeout_add(100, update_color)
webview.on_view_ready( start_update )


def do_quit():
    gtk3.main_quit()
    
#on delete of window, exit:
window.connect( "delete-event", do_quit )

def main():
    gtk3.main()

if __name__ == "__main__":
    main()
