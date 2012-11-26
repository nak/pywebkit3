from ctypes import *

try:
    cdll.LoadLibrary("libwebkitgtk-3.0.so")
    libwebkit3 = CDLL("libwebkitgtk-3.0.so")
    HAVE_WEBKIT2 = True
except:
    try:
        cdll.LoadLibrary("/usr/local/lib/libglib-2.0.so")
        cdll.LoadLibrary("/usr/local/lib/libgmodule-2.0.so")
        cdll.LoadLibrary("/usr/local/lib/libdbus-glib-1.so")
        cdll.LoadLibrary("/usr/local/lib/libgobject-2.0.so")
        cdll.LoadLibrary("/usr/local/lib/libgio-2.0.so")
        cdll.LoadLibrary("/usr/local/lib/libsoup-2.4.so")
        cdll.LoadLibrary("/usr/local/lib/libgeoclue.so")
        cdll.LoadLibrary("/usr/local/lib/libjavascriptcoregtk-3.0.so")
        cdll.LoadLibrary("/usr/local/lib/libwebkit2gtk-3.0.so")
        libwebkit3 = CDLL("/usr/local/lib/libwebkit2gtk-3.0.so")
        HAVE_WEBKIT2 = True
    except:
        import traceback
        import logging
        logging.error(traceback.format_exc())
        cdll.LoadLibrary("libwebkitgtk-3.0.so.0")
        libwebkit3 = CDLL("libwebkitgtk-3.0.so.0")
        HAVE_WEBKIT2 = False
