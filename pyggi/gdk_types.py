from ctypes import cdll, CDLL, c_int

import platform

from pyggi import load

if platform.platform().startswith("Windows"):
    libgdk = load("libgdk-3-0","0")
else:
    libgdk = load("libgdk-3","0")
        
GdkGravity = c_int
GdkWindowTypeHint = c_int
GdkModifierType = c_int
GtkResizeMode = c_int

class Asciifier(object):
    @classmethod
    def from_param(cls, value):
        if isinstance(value, bytes):
            return value
        else:
            return value.encode('ascii')
