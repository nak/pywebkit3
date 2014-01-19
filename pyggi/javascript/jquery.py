from ..javascript import ScriptEnv
from ..javascriptcore import JSString, JSObject
from ..javascriptcore_enums import *
from ..webkit3_enums import *
import logging 
from ctypes import POINTER, c_int



def on_jquery_ready( env, callback , *args):
    if not hasattr(env, "_callbacks"):
        env._callbacks = []
    env._callbacks.append(( callback, args ))

def initialize( env):
    if hasattr(env, "_dollarsign") and env._dollarsign:
        return env.__jq
    assert(isinstance( env, ScriptEnv))
    def view_ready():
        try:
            env._dollarsign= env.get_jsobject(  "$", can_call = True)
            if not hasattr( env, "_callbacks"):
                env._callbacks=[]
            for cb, args in env._callbacks:
                cb( *args)
        except:
            import traceback
            traceback.print_exc()
            env._dollarsign = None
            raise Exception("No jquery")
        if env._dollarsign:
            
            env._jQuery = env.get_jsobject( "jQuery", can_call = False)
        else:
            logging.error("jQuery not detected.")
        return False
    env._webview.on_view_ready( view_ready)
    class _(object):
        
        def __exit__(self,type, value, traceback):
            pass
        
        def __enter__(self):
            return self
        
        def __call__(self,*args):
            #try:
                return env._dollarsign(*args)
            #except:
            #    return None
    env.__jq = _()
    return env.__jq

