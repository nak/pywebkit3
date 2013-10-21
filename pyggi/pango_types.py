from ctypes import cdll, CDLL, c_int, CFUNCTYPE, c_void_p, Structure, c_uint, c_longlong, POINTER, c_char_p

import platform
from pyggi import load

libpango = load( "libpango-1.0","0")
        
