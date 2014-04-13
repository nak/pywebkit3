#!/usr/bin/env python
import os.path
import sys
sys.path = [ os.path.abspath( os.path.join( os.path.dirname(__file__),"..", ".."))] + \
           sys.path

from pyggi.gtk3 import GtkWindow, GtkScrolledWindow
from pyggi import gtk3
from pyggi.webkit3 import WebKitWebView

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


#setup the environment and get the javascript object
color_block = None
from pyggi.javascript import ScriptEnv
env = ScriptEnv( webview)
#must get the object only when javascript has been processed,
#so setup callback 

def import_element():
    global color_block
    color_block = env.get_jsobject( "color_block", can_call=False)
    assert(color_block)
    import logging
    logging.error("GOT COLOR BLOCK %s"%color_block)

webview.on_view_ready( import_element )
#set up a loop to continually increment the color
color = int("00FF00",16)
def update_color( increment ):
    global color
    global color_block
    hex_color = "#%0.6X"%color
    color_block.set_color( hex_color )
    color += increment + (increment/2)*256 + (increment/4)*256*256
    if color > int('FFFFFF',16):
        color = 0
    return False

import threading
class Thread(threading.Thread):

    def run(self):
        while self._active:
            #Must run actualy javascript manipulation in gtk main thread:
            gobject.idle_add( update_color, 20 )
            #we put this code in a real Python thread, to be able to
            #sleep here.  Doing this in the gtk main thread will hamper
            #the display of the GUI, locking any display updates out
            #during the sleep call
            import time
            time.sleep(0.2)
        
thread = Thread()
thread._active = True

from pyggi import gobject
#start the color update thread ONLY when view is ready:
webview.on_view_ready( thread.start )

def do_quit():
    thread._active = False
    gtk3.main_quit()
    
#on delete of window, exit:
window.connect( "delete-event", do_quit )

def main():
    gtk3.main()

if __name__ == "__main__":
    main()
