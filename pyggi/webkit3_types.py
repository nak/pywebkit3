from ctypes import *
import platform
from pyggi import load

if platform.platform().startswith("Windows"):
    libwebkit = load("libwebkitgtk-1.0","2")
    HAVE_CSS3D= False
else:
    libwebkit = load("libwebkitgtk-3.0","0")
    HAVE_CSS3D= True
