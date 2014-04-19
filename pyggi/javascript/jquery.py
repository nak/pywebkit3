#from ..javascript import ScriptEnv
from ..javascriptcore import JSString, JSObject, JSContext
from ..javascriptcore_enums import *
from ..webkit3_enums import *
import logging 
from ctypes import POINTER, c_int



def on_jquery_ready( context, callback , *args):
    if not hasattr(context, "_callbacks"):
        context._callbacks = []
    context._callbacks.append(( callback, args ))

def initialize(  context , on_view_ready):
    assert(context is not None)
    assert( isinstance( context, JSContext))
    if hasattr(context, "_dollarsign") and context._dollarsign:
        return context.__jq
    assert(isinstance( context, JSContext))
    def view_ready():
        try:
            context._dollarsign= context.get_jsobject(  "$", can_call = True)
            if not hasattr( context, "_callbacks"):
                context._callbacks=[]
            for cb, args in context._callbacks:
                cb( *args)
        except:
            import traceback
            traceback.print_exc()
            context._dollarsign = None
            raise Exception("No jquery")
        if context._dollarsign:
            
            context._jQuery = context.get_jsobject( "jQuery", can_call = False)
        else:
            logging.error("jQuery not detected.")
        return False
    on_view_ready( view_ready)
    class _(object):
        attempt = context.get_jsobject(  "$", can_call = True)
        if attempt and attempt._object().contents.value is not None:
            jq = attempt
        else:
            jq = None
        
        def __exit__(self,type, value, traceback):
            pass
        
        def __enter__(self):
            return self
        
        def __call__(self,*args):
            if _.jq is None:
                attempt = context.get_jsobject(  "$", can_call = True)
                if attempt and attempt._object().contents.value is not None:
                    _.jq = attempt                    
            return _.jq(*args)

    return  _()

