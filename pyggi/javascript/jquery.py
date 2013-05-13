from ..javascript import ScriptEnv
from ..javascriptcore import JSString, JSObject
from ..javascriptcore_enums import *
from ..webkit3_enums import *
import logging 
from ctypes import POINTER, c_int


#def _(*args):
#    try:
#        retval =  ___(*args)
#        retval = None
#   return retval



class JQuery_Env(object):
    def __init__( self, webview):
        self._jQuery = None
        self._parent = webview
        def view_ready():
            
            try:
                ___ = webview.get_env().get_jsobject(  "$", can_call = True)
            except:
                ___=None
            if ___:
                self._jQuery = ___               
            else:
                logging.error("jQuery not detected.")
            return True
        webview.on_view_ready( view_ready)
        
    def jquery(self):
        if not self._jQuery:
            try:
                self._jQuery = self._parent.get_env().get_jsobject("$", can_call=True)
            except:
                pass
        return self._jQuery
    

    def __enter__(self):
        if not self._jQuery:
            try:
                self._jQuery = self._parent.get_env().get_jsobject("$", can_call=True)
            except:
                pass
        return self._jQuery
    
    def __exit__(self, type, value, tb):
        pass
    

