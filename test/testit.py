#!/usr/bin/python
from ctypes import *
from pywebkit3 import gtk3,webkit3,javascript

import os.path

#create the webkit webview
web = webkit3.WebKitWebView()
web.open("file://%s/test.html"%os.path.abspath(os.path.dirname(__file__)))

#create the containing window
window = gtk3.GtkWindow(gtk3.GTK_WINDOW_TOPLEVEL)
#close this app on close of the window:
window.connect("delete-event", gtk3.main_quit)

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
#Namespace.add_global_class(context, YPR_Updater, 45 , -45, 45)
import cube
javascript.export_module(context, cube)

#create( context, "py_ypr_updater", 45, -45, 45)

            
#an show it!
window.show_all()

gtk3.main()
