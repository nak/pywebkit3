from ctypes import cdll, CDLL, c_int

cdll.LoadLibrary("libgdk-3.so")
libgdk = CDLL("libgdk-3.so")

GdkGravity = c_int
GdkWindowTypeHint = c_int
GdkModifierType = c_int
GtkResizeMode = c_int