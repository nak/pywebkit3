from ctypes import *
import platform
from pyggi import load

libwebkit3 = None
if platform.platform().startswith("Windows"):
    libwebkit3 = load("libwebkitgtk-3.0","0")
    HAVE_CSS3D= False
else:
    libwebkit3 = load("libwebkitgtk-3.0","0")
    HAVE_CSS3D= True

class Asciifier(object):
    @classmethod
    def from_param(cls, value):
        if isinstance(value, bytes):
            return value
        else:
            return value.encode('ascii')
