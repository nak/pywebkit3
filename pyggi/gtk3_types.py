from ctypes import *
c_void_p = c_ulonglong
from .gdk_types import *
from .gobject_types import *


OPAQUE_PTR = POINTER(c_void_p)
NULL = OPAQUE_PTR()
import platform
from pyggi import load

libgtk3 = load("libgtk-3","0")

"""default gtk types"""

unsigned = c_uint
double = c_double
guint32 = c_uint
guint64 = c_ulong
gunichar = c_int
gint64 = c_long
gssize = c_uint
guint16 = c_ushort
gfloat = c_float
guint = c_uint
guchar = c_ubyte
guint32 = c_uint
gpointer = c_void_p
GDuplicateFunc = GDuplicateFunc
gshort = c_short
glong = c_long
GQuark = c_uint
gulong = c_ulong
gint8 = c_char
gsize = c_uint
gint32 = c_int
GDestroyNotify = GDestroyNotifyCB
GPid = c_int
gint16 = c_short
gconstpointer = c_void_p
gint = c_int
guint8 = c_ubyte
gushort = c_ushort
gchar = c_char
gdouble = c_double
gboolean = c_int

GtkIconSize = c_int
GtkWindowType = c_int
GtkDirectinoType = c_int
GtkOrientation = c_int


PangoFontsetForeachFunc = CFUNCTYPE( c_int, c_void_p, c_void_p, c_void_p, c_void_p)

GdkWindowChildFunc = CFUNCTYPE( c_int, c_void_p, c_void_p)
GdkFilterFunc = CFUNCTYPE( c_int, c_void_p, c_void_p, c_void_p)

GtkAssistantPageFunc = CFUNCTYPE( c_int, c_int, c_void_p)
GtkCallback = CFUNCTYPE( None, c_void_p, c_void_p)
GtkRcPropertyParser = CFUNCTYPE( c_int, c_void_p, c_void_p, c_void_p)

GtkClipboardReceivedFunc= CFUNCTYPE( None, c_void_p, c_void_p, c_void_p)
GtkClipboardTextReceivedFunc = CFUNCTYPE(  None, c_void_p, c_void_p, c_void_p)
GtkClipboardImageReceivedFunc = CFUNCTYPE(  None, c_void_p, c_void_p, c_void_p)
GtkClipboardURIReceivedFunc =  CFUNCTYPE(  None, c_void_p, c_void_p, c_void_p)
GtkClipboardTargetsReceivedFunc = CFUNCTYPE( None, c_void_p, c_void_p, c_int, c_void_p)

GtkClipboardRichTextReceivedFunc = CFUNCTYPE( None, c_void_p, c_void_p, c_void_p, c_uint, c_void_p)
GtkClipboardGetFunc = CFUNCTYPE( None, c_void_p, c_void_p, c_uint, c_void_p)
GtkClipboardClearFunc = CFUNCTYPE( None, c_void_p, c_void_p)

libgtk3.gtk_init(0,0)

def main():
    #libgtk3.gdk_threads_init()
    #libgtk3.gdk_threads_enter()
    libgtk3.gtk_main()
    #libgtk3.gdk_threads_leave()
    
def main_quit():
    libgtk3.gtk_main_quit()
    

GdkEvent = OPAQUE_PTR

class Asciifier(object):
    @classmethod
    def from_param(cls, value):
        if isinstance(value, bytes):
            return value
        else:
            return value.encode('ascii')
