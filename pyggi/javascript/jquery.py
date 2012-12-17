from ..javascript import ScriptEnv
from ..javascriptcore import JSString, JSObject
from ..javascriptcore_enums import *
from ..webkit3_enums import *
import logging 
from ctypes import POINTER, c_int


def _(*args):
    try:
        retval =  ___(*args)
    except:
        retval = None
    return retval


jQuery = None

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
        try:
            ___= env.get_jsobject(  "$", can_call = True)
        except:
            ___=None
        if ___:
            _ = ___
            global jQurey
            jQuery = env.get_jsobject( "jQuery", can_call = False)
            logging.error("############## GOT JQUREY")
        else:
            logging.error("jQuery not detected.")
        return False
    env._webview.on_view_ready( view_ready)
    _initialized = True
    
    return _

