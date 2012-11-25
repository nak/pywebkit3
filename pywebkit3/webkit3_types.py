from ctypes import *

try:
    cdll.LoadLibrary("libwebkit2gtk-3.0.so")
    libwebkit3 = CDLL("libwebkit2gtk-3.0.so")
except:
    cdll.LoadLibrary("libwebkitgtk-3.0.so.0")
    libwebkit3 = CDLL("libwebkitgtk-3.0.so.0")
