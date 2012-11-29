#!/usr/bin/python
from ctypes import *
from pywebkit3 import gtk3,webkit3,javascriptcore
from pywebkit3.javascriptcore import *
import os.path
    
web = webkit3.WebKitWebView()
web.open("file://%s/test.html"%os.path.abspath(os.path.dirname(__file__)))

window = gtk3.GtkWindow(gtk3.GTK_WINDOW_TOPLEVEL)
window.connect("delete-event", gtk3.main_quit)
window.add(web)
window.set_default_size( 250, 100)
window.show_all()
web.show_all()
frame = web.get_main_frame()
context =frame.get_global_context()

from pywebkit3.javascript import JavascriptClass
class YPR_Updater( JavascriptClass ):

    def __init__(self, init_angles):
        JavascriptClass.__init__(self)
        self.ypr = init_angles
        self.sign = 1
        print "YPRUpdater initialize"
    
    def __del__(self):
        print "DEL"

    def update(self, offset_yaw, offset_pitch, offset_roll):
        self.ypr[0] += offset_yaw
        self.ypr[1] += offset_pitch
        self.ypr[2] += offset_roll
        if(self.ypr[2]> 90 ):
            self.sign=-self.sign;
            
            self.ypr[2] -= 180;
            self.ypr[0] -= 180;
            self.ypr[1] = 180-self.ypr[1];
             

        if(self.ypr[0]>=360):
            self.ypr[0] -=360;
        else:
            self.ypr[0] += 360;
	
        if(self.ypr[1]>=180) :
            self.ypr[1] -= 360;
        else:
            self.ypr[1] += 360;
	

    def yaw(self):
        return self.ypr[0]

    def pitch(self):
        return self.ypr[1]

    def roll(self):
        return self.ypr[2]
    
YPR_Updater.create( context, "py_ypr_updater", [45, -45, 45])


gtk3.main()
