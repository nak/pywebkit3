from ..javascript import ScriptEnv
from ..webkit3_enums import *
import logging

_ = None
_load_status_listeners = []

def initialize( webview):
    def set_load_status():
        status = webview.get('load-status')

        if status == WEBKIT_LOAD_FINISHED.value:
            global _
            try:
                _ = ScriptEnv.get_jsobject( webview, "$", can_call = True)
            except:
                import logging
                import traceback
                logging.error(traceback.format_exc())
                logging.error("Unable to initialize jQuery")
            for callback, args in _load_status_listeners:
                callback(*args)
        return False
    
    webview.connect("notify::load-status", set_load_status)

def ready( callback,*args ):
    import time
    time.sleep(1.0)#webkit lies to us -- is it not fully loaded
    _load_status_listeners.append( (callback, args ))
    return False
