#!/usr/bin/python
from ctypes import *
import gtk3
import webkit3
import javascriptcore
from javascriptcore import *

    
web = webkit3.WebKitWebView()
web.load_uri("http://www.google.com")

window = gtk3.GtkWindow(gtk3.GTK_WINDOW_TOPLEVEL)
window.connect("delete-event", gtk3.main_quit)
window.add(web)
window.set_default_size( 1000, 800)
window.show_all()

context = web.get_javascript_global_context()

from javascript import JavascriptClass
class Test( JavascriptClass ):

    def __init__(self, arg1, arg2, arg3):
        JavascriptClass.__init__(self)
        print "%s %s %s"%(arg1, arg2, arg3)


Test.create( context, "testinstance", 1, "HI", 2.34)
print "XXXXXXXXXXXXX"


gtk3.main()
