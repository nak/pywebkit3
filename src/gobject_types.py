from ctypes import cdll, CDLL, c_int

cdll.LoadLibrary("libgobject-2.0.so")
libgobject = CDLL("libgobject-2.0.so")

GType = c_int
