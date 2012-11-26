from ctypes import c_int, c_uint, c_ubyte,c_char_p,  CFUNCTYPE, c_void_p, cdll, CDLL, Structure, c_ushort, POINTER
from webkit3_types import libwebkit3

libjavascriptcore = libwebkit3

JSPropertyAttributes = c_uint;
JSClassAttributes = c_uint;
JSChar = c_ushort;
JSType = c_int;
size_t = c_uint

JSObjectInitializeCallback = CFUNCTYPE( None, c_void_p, c_void_p)
JSObjectFinalizeCallback = CFUNCTYPE( None, c_void_p)
JSObjectHasPropertyCallback = CFUNCTYPE( c_ubyte, c_void_p, c_void_p, c_void_p)
JSObjectGetPropertyCallback = CFUNCTYPE( c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)
JSObjectSetPropertyCallback = CFUNCTYPE( c_ubyte, c_void_p, c_void_p, c_void_p, c_void_p)
JSObjectDeletePropertyCallback = CFUNCTYPE( c_ubyte, c_void_p, c_void_p, c_void_p, c_void_p)
JSObjectGetPropertyNamesCallback = CFUNCTYPE( c_ubyte, c_void_p, c_void_p, c_void_p)
JSObjectCallAsFunctionCallback = CFUNCTYPE( c_void_p, c_void_p, c_void_p, c_void_p, c_uint , c_void_p, c_void_p)
JSObjectCallAsConstructorCallback = CFUNCTYPE( c_void_p, c_void_p, c_void_p, c_uint , c_void_p, c_void_p)
JSObjectHasInstanceCallback = CFUNCTYPE( c_ubyte, c_void_p, c_void_p, c_void_p, c_void_p)
JSObjectConvertToTypeCallback =  CFUNCTYPE( c_void_p, c_void_p, c_uint , c_void_p, c_void_p)

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
               ('parentClass', c_void_p),
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


kJSClassDefinitionEmpty = libwebkit3.kJSClassDefinitionEmpty

NULL = c_void_p()
