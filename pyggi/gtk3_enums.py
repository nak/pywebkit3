from ctypes import c_int

GTK_ICON_SIZE_INVALID = c_int(0)
GTK_ICON_SIZE_MENU = c_int(1)
GTK_ICON_SIZE_SMALL_TOOLBAR = c_int(2)
GTK_ICON_SIZE_LARGE_TOOLBAR = c_int(3)
GTK_ICON_SIZE_BUTTON = c_int(4)
GTK_ICON_SIZE_DND = c_int(5)
GTK_ICON_SIZE_DIALOG = c_int(6)

#GtkStateType
GtkStateType = c_int
GTK_STATE_NORMAL = c_int(0)
GTK_STATE_ACTIVE = c_int(1)
GTK_STATE_PRELIGHT = c_int(2)
GTK_STATE_SELECTED = c_int(3)
GTK_STATE_INSENSITIVE = c_int(4)
GTK_STATE_INCONSISTENT = c_int(5)
GTK_STATE_FOCUSED = c_int(6)

#GtkExpanderStyle
GTK_EXPANDER_COLLAPSED = c_int(0)
GTK_EXPANDER_SEMI_COLLAPSED = c_int(1)
GTK_EXPANDER_SEMI_EXPANDED = c_int(2)
GTK_EXPANDER_EXPANDED = c_int(3)

#GtkWindowType
GTK_WINDOW_TOPLEVEL = c_int(0)
GTK_WINDOW_POPUP = c_int(1)

#GtkWindowPosition
GtkWindowPosition = c_int

#GtkPositionType
GtkPositionType = c_int

#GtkShadowType
GtkShadowType = c_int

#GtkCornerType
GtkCornerType = c_int

#GtkPolicyType
GtkPolicyType = c_int

#GtkPrintOperationResult
GtkPrintOperationResult = c_int
#GtkPrintOperationAction
GtkPrintOperationAction = c_int

#GtkMovementStep
GtkMovementStep = c_int

#GtkJunctionSides
GtkJunctionSides = c_int

#GtkRequestedSize
GtkRequestedSize = c_int

#GtkArrowType
GtkArrowType = c_int

#GtkExpanderStyle
GtkExpanderStyle = c_int

#GtkDirectionType
GtkDirectionType = c_int
GTK_DIR_TAB_FORWARD = c_int(0)
GTK_DIR_TAB_BACKWARD = c_int(1)
GTK_DIR_UP = c_int(2)
GTK_DIR_DOWN = c_int(3)
GTK_DIR_LEFT = c_int(4)
GTK_DIR_RIGHT = c_int(5)

#GtkOrientation
GTK_ORIENTATION_HORIZONTAL = c_int(0)
GTK_ORIENTATION_VERTICAL = c_int(1)

#GtkResizeMode
GTK_RESIZE_PARENT = c_int(0)
GTK_RESIZE_QUEUE = c_int(1)
GTK_RESIZE_IMMEDIATE = c_int(2)

#GtkJunctionSides
GTK_JUNCTION_NONE   = c_int(0)
GTK_JUNCTION_CORNER_TOPLEFT = c_int(1 << 0)
GTK_JUNCTION_CORNER_TOPRIGHT = c_int(1 << 1)
GTK_JUNCTION_CORNER_BOTTOMLEFT = c_int(1 << 2)
GTK_JUNCTION_CORNER_BOTTOMRIGHT = c_int(1 << 3)
GTK_JUNCTION_TOP    = c_int(GTK_JUNCTION_CORNER_TOPLEFT.value | GTK_JUNCTION_CORNER_TOPRIGHT.value)
GTK_JUNCTION_BOTTOM = c_int(GTK_JUNCTION_CORNER_BOTTOMLEFT.value | GTK_JUNCTION_CORNER_BOTTOMRIGHT.value)
GTK_JUNCTION_LEFT   = c_int(GTK_JUNCTION_CORNER_TOPLEFT.value | GTK_JUNCTION_CORNER_BOTTOMLEFT.value)
GTK_JUNCTION_RIGHT  = c_int(GTK_JUNCTION_CORNER_TOPRIGHT.value | GTK_JUNCTION_CORNER_BOTTOMRIGHT.value)

#GtkStateFlags
GtkStateFlags = c_int
GTK_STATE_FLAG_NORMAL       = c_int(0)
GTK_STATE_FLAG_ACTIVE       = c_int(1 << 0)
GTK_STATE_FLAG_PRELIGHT     = c_int(1 << 1)
GTK_STATE_FLAG_SELECTED     = c_int(1 << 2)
GTK_STATE_FLAG_INSENSITIVE  = c_int(1 << 3)
GTK_STATE_FLAG_INCONSISTENT = c_int(1 << 4)
GTK_STATE_FLAG_FOCUSED      = c_int(1 << 5)

#GtkRegionFlags
GtkRegionFlags = c_int
GTK_REGION_EVEN    = c_int(1 << 0)
GTK_REGION_ODD     = c_int(1 << 1)
GTK_REGION_FIRST   = c_int(1 << 2)
GTK_REGION_LAST    = c_int(1 << 3)
GTK_REGION_SORTED  = c_int(1 << 5)

#GtkIconTheme
GtkIconTheme = c_int

#GtkIconThemeError
GtkIconThemeError = c_int

#GtkImageType
GtkImageType = c_int

#GtkAccelFags
GtkAccelFlags = c_int

#GtkJustification
GtkJustificcation = c_int
GTK_JUSTIFY_LEFT = c_int(0)
GTK_JUSTIFY_RIGHT = c_int(1)
GTK_JUSTIFY_CENTER = c_int(2)
GTK_JUSTIFY_FILL = c_int(3)

#GdkDeviceType
GdkDeviceType = c_int

#GdkInputSource
GdkInputSource = c_int

#GdkGravity
GDK_GRAVITY_NORTH_WEST = c_int(1)
GDK_GRAVITY_NORTH = c_int(2)
GDK_GRAVITY_NORTH_EAST = c_int(3)
GDK_GRAVITY_WEST = c_int(4)
GDK_GRAVITY_CENTER = 5
GDK_GRAVITY_EAST = 6
GDK_GRAVITY_SOUTH_WEST = 7
GDK_GRAVITY_SOUTH = 8
GDK_GRAVITY_SOUTH_EAST = 9
GDK_GRAVITY_STATIC = c_int(10)

#GdkModifierType
GDK_SHIFT_MASK    = c_int(1 << 0)
GDK_CONTROL_MASK  = c_int(1 << 2)
GDK_MOD1_MASK     = c_int(1 << 3)
GDK_MOD2_MASK     = c_int(1 << 4)
GDK_MOD3_MASK     = c_int(1 << 5)
GDK_MOD4_MASK     = c_int(1 << 6)
GDK_MOD5_MASK     = c_int(1 << 7)
GDK_BUTTON1_MASK  = c_int(1 << 8)
GDK_BUTTON2_MASK  = c_int(1 << 9)
GDK_BUTTON3_MASK  = c_int(1 << 10)
GDK_BUTTON4_MASK  = c_int(1 << 11)
GDK_BUTTON5_MASK  = c_int(1 << 12)

GDK_MODIFIER_RESERVED_13_MASK  = c_int( 1<< 13)
GDK_MODIFIER_RESERVED_14_MASK  = c_int( 1<< 14)
GDK_MODIFIER_RESERVED_15_MASK  = c_int( 1<< 15)
GDK_MODIFIER_RESERVED_16_MASK  = c_int( 1<< 16)
GDK_MODIFIER_RESERVED_17_MASK  = c_int( 1<< 17)
GDK_MODIFIER_RESERVED_18_MASK  = c_int( 1<< 18)
GDK_MODIFIER_RESERVED_19_MASK  = c_int( 1<< 19)
GDK_MODIFIER_RESERVED_20_MASK  = c_int( 1<< 20)
GDK_MODIFIER_RESERVED_21_MASK  = c_int( 1<< 21)
GDK_MODIFIER_RESERVED_22_MASK  = c_int( 1<< 22)
GDK_MODIFIER_RESERVED_23_MASK  = c_int( 1<< 23)
GDK_MODIFIER_RESERVED_24_MASK  = c_int( 1<< 24)
GDK_MODIFIER_RESERVED_25_MASK  = c_int( 1<< 25)

# The next few modifiers are used by XKB, so we skip to the end.
#   Bits 15 - 25 are currently unused. Bit 29 is used internally.
  
GDK_SUPER_MASK    = c_int( 1<< 26 )
GDK_HYPER_MASK    = c_int( 1<< 27 )
GDK_META_MASK     = c_int( 1<< 28 )

GDK_MODIFIER_RESERVED_29_MASK  = c_int( 1<< 29 )
GDK_RELEASE_MASK  = c_int( 1<< 30 )

# Combination of GDK_SHIFT_MASK..GDK_BUTTON5_MASK + GDK_SUPER_MASK
#     + GDK_HYPER_MASK + GDK_META_MASK + GDK_RELEASE_MASK */
GDK_MODIFIER_MASK = c_int(0x5c001fff)


#GdkTypeHint
GDK_WINDOW_TYPE_HINT_NORMAL = c_int(0)
GDK_WINDOW_TYPE_HINT_DIALOG = c_int(1)
GDK_WINDOW_TYPE_HINT_MENU = 2 #Torn off menu
GDK_WINDOW_TYPE_HINT_TOOLBAR= c_int(3)
GDK_WINDOW_TYPE_HINT_SPLASHSCREEN = c_int(4)
GDK_WINDOW_TYPE_HINT_UTILITY = c_int(5)
GDK_WINDOW_TYPE_HINT_DOCK = c_int(6)
GDK_WINDOW_TYPE_HINT_DESKTOP = c_int(7)
GDK_WINDOW_TYPE_HINT_DROPDOWN_MENU = c_int(8) #  A drop down menu (from a menubar) 
GDK_WINDOW_TYPE_HINT_POPUP_MENU = c_int(9) # A popup menu (from right-click) 
GDK_WINDOW_TYPE_HINT_TOOLTIP = c_int(10)
GDK_WINDOW_TYPE_HINT_NOTIFICATION = c_int(11)
GDK_WINDOW_TYPE_HINT_COMBO = c_int(12)
GDK_WINDOW_TYPE_HINT_DND = c_int(13)

#GdkEventMask
GdkEventMask = c_int
GDK_EXPOSURE_MASK             = c_int(1 << 1)
GDK_POINTER_MOTION_MASK       = c_int(1 << 2)
GDK_POINTER_MOTION_HINT_MASK  = c_int(1 << 3)
GDK_BUTTON_MOTION_MASK        = c_int(1 << 4)
GDK_BUTTON1_MOTION_MASK       = c_int(1 << 5)
GDK_BUTTON2_MOTION_MASK       = c_int(1 << 6)
GDK_BUTTON3_MOTION_MASK       = c_int(1 << 7)
GDK_BUTTON_PRESS_MASK         = c_int(1 << 8)
GDK_BUTTON_RELEASE_MASK       = c_int(1 << 9)
GDK_KEY_PRESS_MASK            = c_int(1 << 10)
GDK_KEY_RELEASE_MASK          = c_int(1 << 11)
GDK_ENTER_NOTIFY_MASK         = c_int(1 << 12)
GDK_LEAVE_NOTIFY_MASK         = c_int(1 << 13)
GDK_FOCUS_CHANGE_MASK         = c_int(1 << 14)
GDK_STRUCTURE_MASK            = c_int(1 << 15)
GDK_PROPERTY_CHANGE_MASK      = c_int(1 << 16)
GDK_VISIBILITY_NOTIFY_MASK    = c_int(1 << 17)
GDK_PROXIMITY_IN_MASK         = c_int(1 << 18)
GDK_PROXIMITY_OUT_MASK        = c_int(1 << 19)
GDK_SUBSTRUCTURE_MASK         = c_int(1 << 20)
GDK_SCROLL_MASK               = c_int(1 << 21)
GDK_TOUCH_MASK                = c_int(1 << 22)
GDK_SMOOTH_SCROLL_MASK        = c_int(1 << 23)
GDK_ALL_EVENTS_MASK           = c_int(0xFFFFFE)

#GdkWindowState
GDK_WINDOW_STATE_WITHDRAWN  = c_int(1 << 0)
GDK_WINDOW_STATE_ICONIFIED  = c_int(1 << 1)
GDK_WINDOW_STATE_MAXIMIZED  = c_int(1 << 2)
GDK_WINDOW_STATE_STICKY     = c_int(1 << 3)
GDK_WINDOW_STATE_FULLSCREEN = c_int(1 << 4)
GDK_WINDOW_STATE_ABOVE      = c_int(1 << 5)
GDK_WINDOW_STATE_BELOW      = c_int(1 << 6)
GDK_WINDOW_STATE_FOCUSED    = c_int(1 << 7)

#GdkWindowEdge
GdkWindowEdge = c_int
GDK_WINDOW_EDGE_NORTH_WEST = c_int(0)
GDK_WINDOW_EDGE_NORTH = c_int(1)
GDK_WINDOW_EDGE_NORTH_EAST = c_int(2)
GDK_WINDOW_EDGE_WEST = c_int(3)
GDK_WINDOW_EDGE_EAST = c_int(4)
GDK_WINDOW_EDGE_SOUTH_WEST = c_int(5)
GDK_WINDOW_EDGE_SOUTH = c_int(6)
GDK_WINDOW_EDGE_SOUTH_EAST = c_int(7)

#GdkWindowState
GdkWindowState = c_int
GDK_WINDOW_STATE_WITHDRAWN  = c_int(1 << 0)
GDK_WINDOW_STATE_ICONIFIED  = c_int(1 << 1)
GDK_WINDOW_STATE_MAXIMIZED  = c_int(1 << 2)
GDK_WINDOW_STATE_STICKY     = c_int(1 << 3)
GDK_WINDOW_STATE_FULLSCREEN = c_int(1 << 4)
GDK_WINDOW_STATE_ABOVE      = c_int(1 << 5)
GDK_WINDOW_STATE_BELOW      = c_int(1 << 6)

#GdkGrabStatus
GdkGrabStatus = c_int
GDK_GRAB_SUCCESS         = c_int(0)
GDK_GRAB_ALREADY_GRABBED = c_int(1)
GDK_GRAB_INVALID_TIME    = c_int(2)
GDK_GRAB_NOT_VIEWABLE    = c_int(3)
GDK_GRAB_FROZEN          = c_int(4)



#PangoGravity
PANGO_GRAVITY_SOUTH = c_int(0)
PANGO_GRAVITY_EAST = c_int(1)
PANGO_GRAVITY_NORTH = c_int(2)
PANGO_GRAVITY_WEST = c_int(3)
PANGO_GRAVITY_AUTO = c_int(4)

#PangoGravityHint
PANGO_GRAVITY_HINT_NATURAL = c_int(0)
PANGO_GRAVITY_HINT_STRONG = c_int(1)
PANGO_GRAVITY_HINT_LINE = c_int(2)

#PangoCoverageLevel
PANGO_COVERAGE_NONE = c_int(0)
PANGO_COVERAGE_FALLBACK = c_int(1)
PANGO_COVERAGE_APPROXIMATE = c_int(2)
PANGO_COVERAGE_EXACT = c_int(3)

#PangoDirection
PANGO_DIRECTION_LTR = c_int(0)
PANGO_DIRECTION_RTL = c_int(1)
PANGO_DIRECTION_TTB_LTR = c_int(2)
PANGO_DIRECTION_TTB_RTL = c_int(3)
PANGO_DIRECTION_WEAK_LTR = c_int(4)
PANGO_DIRECTION_WEAK_RTL = c_int(5)
PANGO_DIRECTION_NEUTRAL = c_int(6)



#AtkRole
AtkRole = c_int(0)

#GtkFileChooserAction
GTK_FILE_CHOOSER_ACTION_OPEN = c_int(0)
GTK_FILE_CHOOSER_ACTION_SAVE = c_int(1)
GTK_FILE_CHOOSER_ACTION_SELECT_FOLDER = c_int(2)
GTK_FILE_CHOOSER_ACTION_CREATE_FOLDER = c_int(3)

#GtkResposne
GTK_RESPONSE_NONE         = c_int(-1)
GTK_RESPONSE_REJECT       = c_int(-2)
GTK_RESPONSE_ACCEPT       = c_int(-3)
GTK_RESPONSE_DELETE_EVENT = c_int(-4)
GTK_RESPONSE_OK           = c_int(-5)
GTK_RESPONSE_CANCEL       = c_int(-6)
GTK_RESPONSE_CLOSE        = c_int(-7)
GTK_RESPONSE_YES          = c_int(-8)
GTK_RESPONSE_NO           = c_int(-9)
GTK_RESPONSE_APPLY        = c_int(-10)
GTK_RESPONSE_HELP         = c_int(-11)

