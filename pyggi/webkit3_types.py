from ctypes import *
import platform

if platform.platform().startswith("Windows"):
    try:
        cdll.LoadLibrary("libgoject-2.0-0.dll")
        libwebkit3 = CDLL("libgobject-2.0-0.dll")
        HAVE_CSS3D= True
    except:
        import logging
        logging.error("Unable to load webkitgtk. Aborting")
        import sys
        sys.exit(1)
else:
    try:
        cdll.LoadLibrary("libwebkitgtk-3.0.so.0")
        libwebkit3 = CDLL("libwebkitgtk-3.0.so.0")
        HAVE_CSS3D= True
    except:
        import logging
        logging.error("Unable to load webkitgtk. Aborting")
        import sys
        sys.exit(1)
