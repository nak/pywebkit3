from ctypes import *

cdll.LoadLibrary("libwebkit2gtk-3.0.so")
libwebkit3 = CDLL("libwebkit2gtk-3.0.so")
