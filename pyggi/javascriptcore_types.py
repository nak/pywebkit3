from ctypes import c_int, c_uint, c_ubyte,c_char_p,  CFUNCTYPE, c_void_p, cdll, CDLL, Structure, c_ushort, POINTER, c_longlong
from pyggi.webkit3_types import load

from pyggi.gtk3_types import OPAQUE_PTR

libjavascriptcore = load("libjavascriptcoregtk-3.0","0")

JSPropertyAttributes = c_uint;
JSClassAttributes = c_uint;
JSChar = c_ushort;
JSType = c_int;
size_t = c_uint

JSObjectInitializeCallback = CFUNCTYPE( None, OPAQUE_PTR, OPAQUE_PTR)
JSObjectFinalizeCallback = CFUNCTYPE( None, OPAQUE_PTR)
JSObjectHasPropertyCallback = CFUNCTYPE( c_ubyte, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR)
JSObjectGetPropertyCallback = CFUNCTYPE( c_longlong, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR)
JSObjectSetPropertyCallback = CFUNCTYPE( c_ubyte, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR)
JSObjectDeletePropertyCallback = CFUNCTYPE( c_ubyte, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR)
JSObjectGetPropertyNamesCallback = CFUNCTYPE( c_ubyte, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR)
JSObjectCallAsFunctionCallback = CFUNCTYPE( c_void_p, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR, c_int , POINTER(OPAQUE_PTR), OPAQUE_PTR)
JSObjectCallAsConstructorCallback = CFUNCTYPE( c_longlong, OPAQUE_PTR, OPAQUE_PTR, c_uint , OPAQUE_PTR, OPAQUE_PTR)
JSObjectHasInstanceCallback = CFUNCTYPE( c_ubyte, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR, OPAQUE_PTR)
JSObjectConvertToTypeCallback =  CFUNCTYPE( c_longlong, OPAQUE_PTR, c_uint , OPAQUE_PTR, OPAQUE_PTR)

class JSStaticValue(Structure):
    _fields_  = [('name', c_char_p),
                 ('getProperty', JSObjectGetPropertyCallback),
                 ('setProperty', JSObjectSetPropertyCallback),
                 ('attributes', JSPropertyAttributes)]

class JSStaticFunction(Structure):
    _fields_ = [ ('name', c_char_p),
                 ('callAsFunction',JSObjectCallAsFunctionCallback),
                 ('attributes', JSPropertyAttributes)]
    


class JSClassDefinition(Structure):
    _fields_ = [('version',c_int),
               ('attributes', JSClassAttributes),
               
               ('className', c_char_p),
               ('parentClass', OPAQUE_PTR),
               ('staticValues', POINTER(JSStaticValue)),
               ('staticFunctions', POINTER( JSStaticFunction)),
               ('initialize', JSObjectInitializeCallback ),
               ('finalize',JSObjectFinalizeCallback ),
               ('hasProperty',JSObjectHasPropertyCallback),
               ('getProperty',JSObjectGetPropertyCallback ),
               ('setProperty',JSObjectSetPropertyCallback ),
               ('deleteProperty',JSObjectDeletePropertyCallback ),
               ('getPropertyName',JSObjectGetPropertyNamesCallback), 
               ('callAsFunction',JSObjectCallAsFunctionCallback),
               ('callAsConstructor',JSObjectCallAsConstructorCallback),
               ('hasInstance',JSObjectHasInstanceCallback ),
               ('convertToType',JSObjectConvertToTypeCallback)]


kJSClassDefinitionEmpty = libjavascriptcore.kJSClassDefinitionEmpty

NULL = OPAQUE_PTR()


class Asciifier(object):
    @classmethod
    def from_param(cls, value):
        if isinstance(value, bytes):
            return value
        else:
            return value.encode('ascii')
