#!/usr/bin/python

import gtk3
import webkit3


web = webkit3.WebKitWebView()
web.load_uri("http://www.google.com")

window = gtk3.GtkWindow(gtk3.GTK_WINDOW_TOPLEVEL)
window.connect("delete-event", gtk3.main_quit)
window.add(web)
window.set_default_size( 1000, 800)
window.show_all()



gtk3.main()
