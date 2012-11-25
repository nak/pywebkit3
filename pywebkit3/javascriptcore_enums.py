from ctypes import c_int

kJSPropertyAttributeNone         = c_int(0)
kJSPropertyAttributeReadOnly     = c_int(1 << 1)
kJSPropertyAttributeDontEnum     = c_int(1 << 2)
kJSPropertyAttributeDontDelete   = c_int(1 << 3)


kJSClassAttributeNone = c_int(0)
kJSClassAttributeNoAutomaticPrototype = c_int(1 << 1)

kJSTypeUndefined = c_int(0)
kJSTypeNull = c_int(1)
kJSTypeBoolean = c_int(2)
kJSTypeNumber = c_int(3)
kJSTypeString = c_int(4)
kJSTypeObject = c_int(5)

