from ctypes import cdll, CDLL, c_int

cdll.LoadLibrary("libgdk-3.so.0")
libgdk = CDLL("libgdk-3.so.0")

GdkGravity = c_int
GdkWindowTypeHint = c_int
GdkModifierType = c_int
GtkResizeMode = c_int
