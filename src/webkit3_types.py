from ctypes import *

cdll.LoadLibrary("libwebkitgtk-3.0.so.0")
libwebkit3 = CDLL("libwebkitgtk-3.0.so.0")
