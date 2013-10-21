from ctypes import cdll, CDLL, c_int

import platform

from pyggi import load

if platform.platform().startswith("Windows"):
    libgdk = load("libgdk-win32-3.0","0")
else:
    libgdk = load("libgdk-3","0")
        
GdkGravity = c_int
GdkWindowTypeHint = c_int
GdkModifierType = c_int
GtkResizeMode = c_int
