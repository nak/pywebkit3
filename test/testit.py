#!/usr/bin/python
from ctypes import *
from pywebkit3 import gtk3,webkit3,javascript
import logging
import os.path


def set_bg(color ):
    import logging
    logging.error("COLOR: %s"% color)
    jquery._('.cubie').each(change)
      
    return False

#create the webkit webview
web = webkit3.WebKitWebView()
web.load_uri("file://%s/test.html"%os.path.abspath(os.path.dirname(__file__)))

#create the containing window
window = gtk3.GtkWindow(gtk3.GTK_WINDOW_TOPLEVEL)
#close this app on close of the window:
window.connect("delete-event", gtk3.main_quit)

web.on_view_ready( set_bg, "red")
#add our web view to the main window
window.add(web)
window.set_default_size( 250, 100)
window.set_title("PyWebkit with CSS 3D ala Python")

#create a class available to javascript, by inheriting from JavascriptClass
import cube

#get the context for the javascript environment:
frame = web.get_main_frame()
context =frame.get_global_context()
from cube import YPR_Updater
YPR_Updater.web = web

#now create our class base on that context:
import cube
javascript.export_module(web.get_env(), cube)

            
#and show it!
window.show_all()
from pywebkit3.javascript import jquery
from pywebkit3 import gobject
from pywebkit3.webkit3_enums import *


def change( index, obj):
    _ = jquery._
    logging.error("CHANGE!!!!!!!!")
    if index%3 == 0:
        color = "#CC%d%d%d%d"%(index,index, index, index)
    elif index%3 == 1:
        color = "#%d%dAA%d%d"%(index,index, index, index)
    else:
        color = "#%d%d%d%d88"%(index,index, index, index)

    logging.error("########### COLOR %s %s %s"%(color, index, obj))
    _(obj).css('background-color',color)
    
    return True


#gobject.idle_add( jquery.initialize,web)
gtk3.main()
