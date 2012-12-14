from ..javascript import ScriptEnv
from ..javascriptcore import JSString, JSObject
from ..javascriptcore_enums import *
from ..webkit3_enums import *
import logging 
from ctypes import POINTER, c_int

_load_status_listeners = []

import Queue
def _(*args):
    retval =  ___(*args)
  
   
    return retval
___=None
_initialized = False

def initialize( env):
    global _initialized
    if _initialized:
        return
    assert(isinstance( env, ScriptEnv))
    def view_ready():
        global ___
        global _
        ___= env.get_jsobject(  "$", can_call = True)
        assert(___)
        _ = ___
        
        return False
    env._webview.on_view_ready( view_ready)
    _initialized = True
    
    return _

