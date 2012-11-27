from ctypes import *

try:
    cdll.LoadLibrary("libwebkitgtk-3.0.so.0.17.4")
    libwebkit3 = CDLL("libwebkitgtk-3.0.so.0.17.4")
    HAVE_CSS3D= True
except:
    import traceback
    import logging
    logging.error(traceback.format_exc())
    cdll.LoadLibrary("libwebkitgtk-3.0.so.0")
    libwebkit3 = CDLL("libwebkitgtk-3.0.so.0")
    HAVE_CSS3D = False
