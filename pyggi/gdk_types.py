from ctypes import cdll, CDLL, c_int
import platform

if platform.platform().startswith("Windows"):
    try:
        cdll.LoadLibrary("libgdk-win32-2.0-0.dll")
        libgdk = CDLL("libgdk-win32-2.0-0.dll")
        HAVE_CSS3D= True
    except:
        import logging
        logging.error("Unable to load webkitgtk. Aborting")
        import sys
        sys.exit(1)
else:
    try:
        cdll.LoadLibrary("libgdk-3.so.0")
        libgdk = CDLL("libgdk-3.so.0")
    except:
        import logging
        logging.error("Unable to load libgdk. Aborting")
        import sys
        sys.exit(1)
        
GdkGravity = c_int
GdkWindowTypeHint = c_int
GdkModifierType = c_int
GtkResizeMode = c_int
