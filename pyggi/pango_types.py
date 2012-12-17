from ctypes import cdll, CDLL, c_int, CFUNCTYPE, c_void_p, Structure, c_uint, c_longlong, POINTER, c_char_p

import platform

if platform.platform().startswith("Windows"):
    try:
        cdll.LoadLibrary("libpango-1.0-0.dll")
        libpango = CDLL("libpango-1.0-0.dll")
        HAVE_CSS3D= True
    except:
        import logging
        logging.error("Unable to load webkitgtk. Aborting")
        import sys
        sys.exit(1)
else:
    try:
        cdll.LoadLibrary("libpango-1.0.so.0")
        libpango = CDLL("libpango-1.0.so.0")
    except:
        import logging
        logging.error("Unable to load webkitgtk. Aborting")
        import sys
        sys.exit(1)
        
