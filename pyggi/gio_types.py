from ctypes import cdll, CDLL, c_int, CFUNCTYPE, c_void_p, Structure, c_uint, c_longlong, POINTER, c_char_p

import platform
from pyggi import load

libgio = load("libgio-2.0","0")
        

GFileProgressCallback = CFUNCTYPE( c_void_p, c_uint, c_uint, c_void_p)
GFileReadMoreCallback = CFUNCTYPE( c_void_p,c_char_p, c_uint, c_void_p)
GCancellableSourceFunc= CFUNCTYPE( c_uint, c_void_p, c_void_p)

goffset = c_uint
