from ..javascript import ScriptEnv

_ = None


import Queue
q = Queue.Queue()

def initialize( webview):
    global _
    try:
        _ = ScriptEnv.get_jsobject( webview, "$", can_call = True)
        import logging
        q.put("Found jQuery %s"%_)
        return False
    except:
        import logging
        import traceback
        logging.error(traceback.format_exc())
        logging.error("Unable to initialize jQuery")
        return True

def ready():
    q.get()
