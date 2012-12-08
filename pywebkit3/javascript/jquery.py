from ..javascript import ScriptEnv
from ..webkit3_enums import *
import logging


_load_status_listeners = []

import Queue
_ = None
_initialized = False
def initialize( env):
    global _initialized
    if _initialized:
        return
    assert(isinstance( env, ScriptEnv))
    def view_ready():
        global _
        logging.error("LOAD COMPLETE")
        _ = env.get_jsobject(  "$", can_call = True)
    env._webview.on_view_ready( view_ready)
    _initialized = True
    return _

