from ctypes import *

try:
    cdll.LoadLibrary("libwebkitgtk-3.0.so")
    libwebkit3 = CDLL("libwebkitgtk-3.0.so")
    HAVE_CSS3D= True
except:
    import traceback
    import logging
    logging.error(traceback.format_exc())
    import sys
    sys.exit(1)
