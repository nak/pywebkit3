from ctypes import *

cdll.LoadLibrary("libwebkitgtk-3.0.so.0")
libwebkit = CDLL("libwebkitgtk-3.0.so.0")

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
GdkGravity = c_int
GdkWindowTypeHint = c_int
GdkModifierType = c_int

from gi.repository import Gtk
