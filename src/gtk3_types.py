from ctypes import *
from gdk_types import *
from gobject_types import *

cdll.LoadLibrary("libgtk-3.so")
libgtk3 = CDLL("libgtk-3.so")

GDestroyNotifyCB = CFUNCTYPE(None, c_void_p)
GDuplicateFunc = CFUNCTYPE( c_void_p, c_void_p, c_void_p)
"""default gtk types"""

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


libgtk3.gtk_init(0,0)

def main():
    libgtk3.gtk_main()
    
def main_quit():
    libgtk3.gtk_main_quit()
