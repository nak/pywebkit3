#!/usr/bin/python
import sys
import os.path
sys.path = [ os.path.abspath( os.path.join( os.path.dirname(__file__),".."))] + \
           sys.path

from pyggi import gtk3,webkit3,javascript, gobject

####################
# Ophidian is the python equivalent of javascript.  Any library in javascript
# is easily exported to python.  For jQuery, the Python equivalent of the  "$"
# operator is provided as the "_" operator in Python.
#
# NOTE: Any javascript or jQuery calls MUST be done only after a context is available,
# usually implying a webview is "ready", determined via the
# WebKitWebView class's on_view_ready callback.  Also, javascript calls will have no impact
# unless run from the gtk main thread (this IS GTK).  
######################

## Use ophidian much like jQuery t set the colors on the cube
## faces.
from pyggi.javascript import jquery
import logging

count= 0
def set_bg(color = 0 ):
    # The callback for "each":
    global jq
    _ = jq
    def change( index, obj):
        global count
        if index%3 == 0:
            index = (index + count) %10
            logging.error(index)
            color = "#CC%d%d%d%d"%(index,index, index, index)
        elif index%3 == 1:
            index = (index + count) %10            
            color = "#%d%dAA%d%d"%(index,index, index, index)
        else:
            index = (index + count) %10            
            color = "#%d%d%d%d88"%(index,index, index, index)
        count += 1
        count = count %10
        _(obj).css('background-color',color)

        return True
    #Run the callback on each cube face (cubie) a'la jQurey interface
    #through ophdian:
    _('.cubie').each(change)     
    return True

#create the webkit webview and load a local file URI
web = webkit3.WebKitWebView()
web.load_uri("file://%s/test.html"%os.path.abspath(os.path.dirname(__file__)))

#create the containing window
window = gtk3.GtkWindow(gtk3.GTK_WINDOW_TOPLEVEL)
#close this app on close of the window:
window.connect("delete-event", gtk3.main_quit)

#when web view is read, mak a callback to set_bg,
#which by the nature of it being a GTK callback,
#will be executed in the main thread
web.on_view_ready( set_bg, "red")
gobject.timeout_add( 1000, set_bg)
#add our web view to the main window, and set properties
window.add(web)
window.set_default_size( 250, 100)
window.set_title("PyWebkit with CSS 3D ala Python")


#get the context for the javascript environment:
frame = web.get_main_frame()
context =frame.get_global_context()
#create a class available to javascript, The YPR_Updater class
#is made available to javascript simply by inheriting from JavascriptClass
#Javascript code can create a python YPR_Updater object view the
#"cube.YPR_Updater.new_ method
from cube import YPR_Updater
YPR_Updater.web = web

#now create all classes under cube by exporting that module:
#We must provide an execution context (environment) which is done
#via the get_env() call.  This will also initialize jQuery python
#interface module if not already initialized
import cube
javascript.export_module(web.get_env(), cube)
jq = jquery.initialize(web.get_env())


#and show it!
window.show_all()
gtk3.main()
