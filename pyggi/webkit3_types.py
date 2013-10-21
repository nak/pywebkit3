from ctypes import *
import platform


if platform.platform().startswith("Windows"):
    libwebkit = load("libwebkit-1.0","2")
    HAVE_CSS3D= False
else:
    libwebkit = load("libwebkit-3.0","0")
    HAVE_CSS3D= True
