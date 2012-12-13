from ctypes import c_int, c_uint

kJSPropertyAttributeNone         = c_uint(0)
kJSPropertyAttributeReadOnly     = c_uint(1 << 1)
kJSPropertyAttributeDontEnum     = c_uint(1 << 2)
kJSPropertyAttributeDontDelete   = c_uint(1 << 3)


kJSClassAttributeNone = c_uint(0)
kJSClassAttributeNoAutomaticPrototype = c_uint(1 << 1)

kJSTypeUndefined = c_uint(0)
kJSTypeNull = c_uint(1)
kJSTypeBoolean = c_uint(2)
kJSTypeNumber = c_uint(3)
kJSTypeString = c_uint(4)
kJSTypeObject = c_uint(5)

