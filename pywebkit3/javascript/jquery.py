from ..javascript import ScriptEnv
from ..webkit3_enums import *
import logging


_load_status_listeners = []

import Queue
_ = None

def initialize( env):
    global _
    q = Queue.Queue()
    assert(isinstance( env, ScriptEnv))
    def load_complete():
        logging.error("LOAD COMPLETE")
        q.put("loaded")
    env._webview.connect("resource-load-finished", load_complete)
    #q.get()
    _ = env.get_jsobject(  "$", can_call = True)
    loggign.error("INITED")
    return _

