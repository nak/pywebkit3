from ctypes import *
from gtk3_types import *
from gtk3_types import *


"""Derived Pointer Types"""
_GOptionGroup = c_void_p
_GdkDragContext = c_void_p
_GdkPixbuf = c_void_p
_GIcon = c_void_p
_GdkDevice = c_void_p
_GtkTargetList = c_void_p
_GtkWidget = c_void_p
_GdkEvent = c_void_p
_GtkTargetEntry = c_void_p
_PangoLanguage = c_void_p
_cairo_surface_t = c_void_p
_GdkWindow = c_void_p
"""Enumerations"""
GtkDestDefaults = c_int
GtkTargetFlags = c_int


def gtk_key_snooper_install( func_data,):
    libgtk3.gtk_key_snooper_install.restype = guint
    libgtk3.gtk_key_snooper_install.argtypes = [gpointer]
    return libgtk3.gtk_key_snooper_install( func_data,)


def gtk_drag_set_icon_surface( context,):
    libgtk3.gtk_drag_set_icon_surface.argtypes = [_GdkDragContext]
    libgtk3.gtk_drag_set_icon_surface( context,)


def gtk_drag_set_icon_gicon( context,):
    libgtk3.gtk_drag_set_icon_gicon.argtypes = [_GdkDragContext]
    libgtk3.gtk_drag_set_icon_gicon( context,)


def gtk_grab_remove( widget,):
    libgtk3.gtk_grab_remove.argtypes = [_GtkWidget]
    libgtk3.gtk_grab_remove( widget,)


def gtk_drag_set_icon_default( context,):
    libgtk3.gtk_drag_set_icon_default.argtypes = [_GdkDragContext]
    libgtk3.gtk_drag_set_icon_default( context,)


def gtk_drag_source_set_icon_pixbuf( widget,):
    libgtk3.gtk_drag_source_set_icon_pixbuf.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_set_icon_pixbuf( widget,)


def gtk_drag_dest_set_track_motion( widget,):
    libgtk3.gtk_drag_dest_set_track_motion.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_dest_set_track_motion( widget,)


def gtk_drag_dest_unset( widget,):
    libgtk3.gtk_drag_dest_unset.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_dest_unset( widget,)


def gtk_drag_dest_get_target_list( widget,):
    libgtk3.gtk_drag_dest_get_target_list.restype = ['_GtkTargetList']
    libgtk3.gtk_drag_dest_get_target_list.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_dest_get_target_list( widget,)


def gtk_drag_dest_set( widget,):
    libgtk3.gtk_drag_dest_set.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_dest_set( widget,)


def gtk_drag_source_add_image_targets( widget,):
    libgtk3.gtk_drag_source_add_image_targets.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_add_image_targets( widget,)


def gtk_drag_check_threshold( widget,):
    libgtk3.gtk_drag_check_threshold.restype = gboolean
    libgtk3.gtk_drag_check_threshold.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_check_threshold( widget,)


def gtk_drag_source_unset( widget,):
    libgtk3.gtk_drag_source_unset.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_unset( widget,)


def gtk_device_grab_add( widget,):
    libgtk3.gtk_device_grab_add.argtypes = [_GtkWidget]
    libgtk3.gtk_device_grab_add( widget,)


def gtk_drag_source_set_target_list( widget,):
    libgtk3.gtk_drag_source_set_target_list.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_set_target_list( widget,)


def gtk_get_event_widget( event,):
    libgtk3.gtk_get_event_widget.restype = ['_GtkWidget']
    libgtk3.gtk_get_event_widget.argtypes = [_GdkEvent]
    return libgtk3.gtk_get_event_widget( event,)


def gtk_drag_source_set( widget,):
    libgtk3.gtk_drag_source_set.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_set( widget,)


def gtk_drag_dest_add_text_targets( widget,):
    libgtk3.gtk_drag_dest_add_text_targets.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_dest_add_text_targets( widget,)


def gtk_drag_dest_get_track_motion( widget,):
    libgtk3.gtk_drag_dest_get_track_motion.restype = gboolean
    libgtk3.gtk_drag_dest_get_track_motion.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_dest_get_track_motion( widget,)


def gtk_drag_set_icon_pixbuf( context,):
    libgtk3.gtk_drag_set_icon_pixbuf.argtypes = [_GdkDragContext]
    libgtk3.gtk_drag_set_icon_pixbuf( context,)


def gtk_get_current_event_state( state,):
    libgtk3.gtk_get_current_event_state.restype = gboolean
    libgtk3.gtk_get_current_event_state.argtypes = [POINTER(GdkModifierType)]
    return libgtk3.gtk_get_current_event_state( state,)


def gtk_drag_dest_add_uri_targets( widget,):
    libgtk3.gtk_drag_dest_add_uri_targets.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_dest_add_uri_targets( widget,)


def gtk_drag_source_get_target_list( widget,):
    libgtk3.gtk_drag_source_get_target_list.restype = ['_GtkTargetList']
    libgtk3.gtk_drag_source_get_target_list.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_source_get_target_list( widget,)


def gtk_main_iteration_do( blocking,):
    libgtk3.gtk_main_iteration_do.restype = gboolean
    libgtk3.gtk_main_iteration_do.argtypes = [gboolean]
    return libgtk3.gtk_main_iteration_do( blocking,)


def gtk_drag_source_set_icon_gicon( widget,):
    libgtk3.gtk_drag_source_set_icon_gicon.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_set_icon_gicon( widget,)


def gtk_drag_dest_set_proxy( widget,):
    libgtk3.gtk_drag_dest_set_proxy.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_dest_set_proxy( widget,)


def gtk_drag_set_icon_stock( context,):
    libgtk3.gtk_drag_set_icon_stock.argtypes = [_GdkDragContext]
    libgtk3.gtk_drag_set_icon_stock( context,)


def gtk_device_grab_remove( widget,):
    libgtk3.gtk_device_grab_remove.argtypes = [_GtkWidget]
    libgtk3.gtk_device_grab_remove( widget,)


def gtk_drag_dest_add_image_targets( widget,):
    libgtk3.gtk_drag_dest_add_image_targets.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_dest_add_image_targets( widget,)


def gtk_drag_set_icon_widget( context,):
    libgtk3.gtk_drag_set_icon_widget.argtypes = [_GdkDragContext]
    libgtk3.gtk_drag_set_icon_widget( context,)


def gtk_grab_add( widget,):
    libgtk3.gtk_grab_add.argtypes = [_GtkWidget]
    libgtk3.gtk_grab_add( widget,)


def gtk_drag_get_data( widget,):
    libgtk3.gtk_drag_get_data.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_get_data( widget,)


def gtk_drag_source_add_uri_targets( widget,):
    libgtk3.gtk_drag_source_add_uri_targets.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_add_uri_targets( widget,)


def gtk_propagate_event( widget,):
    libgtk3.gtk_propagate_event.argtypes = [_GtkWidget]
    libgtk3.gtk_propagate_event( widget,)


def gtk_drag_unhighlight( widget,):
    libgtk3.gtk_drag_unhighlight.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_unhighlight( widget,)


def gtk_get_option_group( open_default_display,):
    libgtk3.gtk_get_option_group.restype = ['_GOptionGroup']
    libgtk3.gtk_get_option_group.argtypes = [gboolean]
    return libgtk3.gtk_get_option_group( open_default_display,)


def gtk_drag_dest_find_target( widget,):
    libgtk3.gtk_drag_dest_find_target.restype = GdkAtom
    libgtk3.gtk_drag_dest_find_target.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_dest_find_target( widget,)


def gtk_drag_set_icon_name( context,):
    libgtk3.gtk_drag_set_icon_name.argtypes = [_GdkDragContext]
    libgtk3.gtk_drag_set_icon_name( context,)


def gtk_drag_source_set_icon_stock( widget,):
    libgtk3.gtk_drag_source_set_icon_stock.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_set_icon_stock( widget,)


def gtk_drag_begin( widget,):
    libgtk3.gtk_drag_begin.restype = ['_GdkDragContext']
    libgtk3.gtk_drag_begin.argtypes = [_GtkWidget]
    return libgtk3.gtk_drag_begin( widget,)


def gtk_drag_dest_set_target_list( widget,):
    libgtk3.gtk_drag_dest_set_target_list.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_dest_set_target_list( widget,)


def gtk_drag_source_add_text_targets( widget,):
    libgtk3.gtk_drag_source_add_text_targets.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_add_text_targets( widget,)


def gtk_drag_finish( context,):
    libgtk3.gtk_drag_finish.argtypes = [_GdkDragContext]
    libgtk3.gtk_drag_finish( context,)


def gtk_drag_get_source_widget( context,):
    libgtk3.gtk_drag_get_source_widget.restype = ['_GtkWidget']
    libgtk3.gtk_drag_get_source_widget.argtypes = [_GdkDragContext]
    return libgtk3.gtk_drag_get_source_widget( context,)


def gtk_drag_highlight( widget,):
    libgtk3.gtk_drag_highlight.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_highlight( widget,)


def gtk_main_do_event( event,):
    libgtk3.gtk_main_do_event.argtypes = [_GdkEvent]
    libgtk3.gtk_main_do_event( event,)


def gtk_key_snooper_remove( snooper_handler_id,):
    libgtk3.gtk_key_snooper_remove.argtypes = [guint]
    libgtk3.gtk_key_snooper_remove( snooper_handler_id,)


def gtk_drag_source_set_icon_name( widget,):
    libgtk3.gtk_drag_source_set_icon_name.argtypes = [_GtkWidget]
    libgtk3.gtk_drag_source_set_icon_name( widget,)

