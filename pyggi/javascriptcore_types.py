from ctypes import c_int, c_uint, c_ubyte,c_char_p,  CFUNCTYPE, c_void_p, cdll, CDLL, Structure, c_ushort, POINTER, c_longlong
from pyggi.webkit3_types import libwebkit3

libjavascriptcore = libwebkit3

JSPropertyAttributes = c_uint;
JSClassAttributes = c_uint;
JSChar = c_ushort;
JSType = c_int;
size_t = c_uint

JSObjectInitializeCallback = CFUNCTYPE( None, POINTER(c_int), POINTER(c_int))
JSObjectFinalizeCallback = CFUNCTYPE( None, POINTER(c_int))
JSObjectHasPropertyCallback = CFUNCTYPE( c_ubyte, POINTER(c_int), POINTER(c_int), POINTER(c_int))
JSObjectGetPropertyCallback = CFUNCTYPE( c_longlong, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int))
JSObjectSetPropertyCallback = CFUNCTYPE( c_ubyte, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int))
JSObjectDeletePropertyCallback = CFUNCTYPE( c_ubyte, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int))
JSObjectGetPropertyNamesCallback = CFUNCTYPE( c_ubyte, POINTER(c_int), POINTER(c_int), POINTER(c_int))
JSObjectCallAsFunctionCallback = CFUNCTYPE( c_longlong, POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int , POINTER(POINTER(c_int)), POINTER(c_int))
JSObjectCallAsConstructorCallback = CFUNCTYPE( c_longlong, POINTER(c_int), POINTER(c_int), c_uint , POINTER(c_int), POINTER(c_int))
JSObjectHasInstanceCallback = CFUNCTYPE( c_ubyte, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int))
JSObjectConvertToTypeCallback =  CFUNCTYPE( c_longlong, POINTER(c_int), c_uint , POINTER(c_int), POINTER(c_int))

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
               ('parentClass', POINTER(c_int)),
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

NULL = POINTER(c_int)()
