# Copyright, John Rusnak, 2012
    # This code binding is available under the license agreement of the LGPL with
    # an additional constraint described below,
    # and with the understanding that the webkit API is copyright protected
    # by Apple Computer, Inc. (see below).
    # There is an  additional constraint that any derivatives of this work aimed
    # at providing bindings to GObject, GTK, GDK, or WebKit be strictly
    # python-only bindings with no native code.
    # * THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY
    # * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    # * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
    # * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    # * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    # * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    # * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    #
    # ******************************************************
    # For the API:
    # /*
    # * Copyright (C) 2006 Apple Computer, Inc.  All rights reserved.
    # *
    # * Redistribution and use in source and binary forms, with or without
    # * modification, are permitted provided that the following conditions
    # * are met:
    # * 1. Redistributions of source code must retain the above copyright
    # *    notice, this list of conditions and the following disclaimer.
    # * 2. Redistributions in binary form must reproduce the above copyright
    # *    notice, this list of conditions and the following disclaimer in the
    # *    documentation and/or other materials provided with the distribution.
    # *
    # * THIS SOFTWARE IS PROVIDED BY APPLE COMPUTER, INC. ``AS IS'' AND ANY
    # * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    # * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
    # * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    # * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    # * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    # * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    # */
from ctypes import *
from .gtk3_types import *
from .javascriptcore_types import *
import logging
            
OPAQUE_PTR = POINTER(c_void_p)
NULL = OPAQUE_PTR()
"""Derived Pointer Types"""
__GtkRcStyle = OPAQUE_PTR
__GdkGeometry = OPAQUE_PTR
_WebKitWebPolicyDecision = OPAQUE_PTR
_WebKitNetworkResponse = OPAQUE_PTR
_GdkPixbuf = OPAQUE_PTR
_GtkBin = OPAQUE_PTR
__GtkRequisition = OPAQUE_PTR
_GtkRcStyle = OPAQUE_PTR
_PangoEngineShape = OPAQUE_PTR
__GtkRegionFlags = OPAQUE_PTR
__WebKitDOMNode = OPAQUE_PTR
_GtkWindow = OPAQUE_PTR
__cairo_font_options_t = OPAQUE_PTR
__JSValue = OPAQUE_PTR
_JSContext = OPAQUE_PTR
_GtkIconFactory = OPAQUE_PTR
__GdkAtom = OPAQUE_PTR
_GMainLoop = OPAQUE_PTR
__GdkTimeCoord = OPAQUE_PTR
_GdkColor = OPAQUE_PTR
__GtkWidgetPath = OPAQUE_PTR
_GtkContainer = OPAQUE_PTR
_PangoItem = OPAQUE_PTR
__GClosure = OPAQUE_PTR
_GtkAboutDialog = OPAQUE_PTR
__GMainContext = OPAQUE_PTR
_GdkDisplay = OPAQUE_PTR
__GtkStyleProvider = OPAQUE_PTR
_GtkScrolledWindow = OPAQUE_PTR
_GtkDialog = OPAQUE_PTR
__WebKitWebWindowFeatures = OPAQUE_PTR
_JSObject = OPAQUE_PTR
_GBytes = OPAQUE_PTR
_GScanner = OPAQUE_PTR
_PangoFont = OPAQUE_PTR
_GtkStyleContext = OPAQUE_PTR
_GMainContext = OPAQUE_PTR
_GBoxed = OPAQUE_PTR
__GtkTextBuffer = OPAQUE_PTR
_GtkTargetList = OPAQUE_PTR
__WebKitWebSettings = OPAQUE_PTR
_GdkAppLaunchContext = OPAQUE_PTR
__GObject = OPAQUE_PTR
__PangoLayout = OPAQUE_PTR
_WebKitWebBackForwardList = OPAQUE_PTR
_GtkOffscreenWindow = OPAQUE_PTR
__GParamSpec = OPAQUE_PTR
__PangoAttrIterator = OPAQUE_PTR
_GtkRequisition = OPAQUE_PTR
_GtkIconSet = OPAQUE_PTR
_GtkSelectionData = OPAQUE_PTR
_GtkWindowGroup = OPAQUE_PTR
_GtkAdjustment = OPAQUE_PTR
_JSGlobalContext = OPAQUE_PTR
_GApplication = OPAQUE_PTR
_PangoLogAttr = OPAQUE_PTR
_GString = OPAQUE_PTR
__PangoContext = OPAQUE_PTR
__JSPropertyNameArray = OPAQUE_PTR
_WebKitWebSettings = OPAQUE_PTR
__PangoFont = OPAQUE_PTR
__GtkPathPriorityType = OPAQUE_PTR
__JSClass = OPAQUE_PTR
__WebKitWebHistoryItem = OPAQUE_PTR
_JSValue = OPAQUE_PTR
__GtkSettings = OPAQUE_PTR
_GSource = OPAQUE_PTR
__PangoFontMap = OPAQUE_PTR
__JSString = OPAQUE_PTR
__PangoAttrList = OPAQUE_PTR
_PangoMatrix = OPAQUE_PTR
__GSource = OPAQUE_PTR
_GtkApplication = OPAQUE_PTR
__PangoAnalysis = OPAQUE_PTR
__GMutex = OPAQUE_PTR
_PangoFontDescription = OPAQUE_PTR
_GdkGeometry = OPAQUE_PTR
__GdkCursor = OPAQUE_PTR
_GtkBorder = OPAQUE_PTR
_WebKitWebInspector = OPAQUE_PTR
_GdkWindowAttr = OPAQUE_PTR
_GOptionGroup = OPAQUE_PTR
__GScanner = OPAQUE_PTR
__GtkWidgetClass = OPAQUE_PTR
__GtkContainerClass = OPAQUE_PTR
__GdkEventKey = OPAQUE_PTR
__GtkAdjustment = OPAQUE_PTR
_GdkDragContext = OPAQUE_PTR
_GtkAssistant = OPAQUE_PTR
__GdkDisplay = OPAQUE_PTR
_GtkWidgetPath = OPAQUE_PTR
_GdkScreen = OPAQUE_PTR
_PangoFontMetrics = OPAQUE_PTR
__GCond = OPAQUE_PTR
_GtkIconSource = OPAQUE_PTR
__cairo_surface_t = OPAQUE_PTR
_GdkVisual = OPAQUE_PTR
_PangoFontMap = OPAQUE_PTR
_GSList = OPAQUE_PTR
_WebKitWebFrame = OPAQUE_PTR
_JSString = OPAQUE_PTR
__GActionGroup = OPAQUE_PTR
_GtkWidget = OPAQUE_PTR
__WebKitNetworkRequest = OPAQUE_PTR
__GdkWindow = OPAQUE_PTR
__PangoFontFamily = OPAQUE_PTR
__JSContextGroup = OPAQUE_PTR
__GPollFD = OPAQUE_PTR
__cairo_region_t = OPAQUE_PTR
_PangoFontset = OPAQUE_PTR
_GdkWindow = OPAQUE_PTR
__PangoFontDescription = OPAQUE_PTR
__GtkBorder = OPAQUE_PTR
__GError = OPAQUE_PTR
__PangoCoverage = OPAQUE_PTR
_WebKitViewportAttributes = OPAQUE_PTR
_JSClass = OPAQUE_PTR
_WebKitWebHistoryItem = OPAQUE_PTR
_PangoFontFamily = OPAQUE_PTR
__cairo_t = OPAQUE_PTR
__GWeakRef = OPAQUE_PTR
__GdkVisual = OPAQUE_PTR
__GdkEventButton = OPAQUE_PTR
__GCancellable = OPAQUE_PTR
_GdkDevice = OPAQUE_PTR
__PangoRectangle = OPAQUE_PTR
__GtkAccelGroup = OPAQUE_PTR
_GObject = OPAQUE_PTR
_GPollFD = OPAQUE_PTR
__GtkIconSource = OPAQUE_PTR
__GFile = OPAQUE_PTR
__JSContext = OPAQUE_PTR
_PangoFontsetSimple = OPAQUE_PTR
__GtkAllocation = OPAQUE_PTR
__GtkWidget = OPAQUE_PTR
_PangoLayoutLine = OPAQUE_PTR
__GtkIconSet = OPAQUE_PTR
_WebKitWebView = OPAQUE_PTR
__PangoTabArray = OPAQUE_PTR
_WebKitHitTestResult = OPAQUE_PTR
__GValue = OPAQUE_PTR
_GdkDeviceManager = OPAQUE_PTR
_GdkCursor = OPAQUE_PTR
_WebKitDOMDocument = OPAQUE_PTR
__PangoMatrix = OPAQUE_PTR
__GtkPrintOperation = OPAQUE_PTR
__GString = OPAQUE_PTR
_PangoContext = OPAQUE_PTR
__GtkTargetList = OPAQUE_PTR
__GList = OPAQUE_PTR
__WebKitWebView = OPAQUE_PTR
_WebKitWebWindowFeatures = OPAQUE_PTR
_PangoCoverage = OPAQUE_PTR
_GParamSpec = OPAQUE_PTR
_GList = OPAQUE_PTR
__GdkRGBA = OPAQUE_PTR
__GTimeVal = OPAQUE_PTR
_GtkInvisible = OPAQUE_PTR
__GSourceFuncs = OPAQUE_PTR
__JSPropertyNameAccumulator = OPAQUE_PTR
__PangoGlyphString = OPAQUE_PTR
__JSGlobalContext = OPAQUE_PTR
_WebKitSecurityOrigin = OPAQUE_PTR
__GObjectClass = OPAQUE_PTR
__GSList = OPAQUE_PTR
_PangoAnalysis = OPAQUE_PTR
__GdkWindowAttr = OPAQUE_PTR
_SoupMessage = OPAQUE_PTR
_WebKitWebDataSource = OPAQUE_PTR
_GdkAtom = OPAQUE_PTR
__GdkColor = OPAQUE_PTR
_JSContextGroup = OPAQUE_PTR
__GdkRectangle = OPAQUE_PTR
__PangoLanguage = OPAQUE_PTR
_PangoAttrList = OPAQUE_PTR
__gunichar = OPAQUE_PTR
__GdkWMDecoration = OPAQUE_PTR
__PangoLogAttr = OPAQUE_PTR
_PangoLayout = OPAQUE_PTR
_JSPropertyNameArray = OPAQUE_PTR
__JSObject = OPAQUE_PTR
__GdkDragContext = OPAQUE_PTR
_WebKitWebNavigationAction = OPAQUE_PTR
_GtkStyle = OPAQUE_PTR
__GParameter = OPAQUE_PTR
__GtkStyle = OPAQUE_PTR
__GIcon = OPAQUE_PTR
__GtkWindow = OPAQUE_PTR
_PangoLayoutRun = OPAQUE_PTR
__cairo_pattern_t = OPAQUE_PTR
__GdkPixbuf = OPAQUE_PTR
_WebKitGeolocationPolicyDecision = OPAQUE_PTR
_GtkSettings = OPAQUE_PTR
__GSourceCallbackFuncs = OPAQUE_PTR
__PangoFontFace = OPAQUE_PTR
__GtkTargetEntry = OPAQUE_PTR
__GtkApplication = OPAQUE_PTR
_GtkClipboard = OPAQUE_PTR
_GByteArray = OPAQUE_PTR
__GdkScreen = OPAQUE_PTR
_PangoLanguage = OPAQUE_PTR
__GdkDevice = OPAQUE_PTR
_PangoTabArray = OPAQUE_PTR
_JSPropertyNameAccumulator = OPAQUE_PTR

from .javascriptcore_enums import *
"""Enumerations"""
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkIconSize = c_int
GdkWindowType = c_int
GdkWindowWindowClass = c_int
GdkWindowHints = c_int
GdkGravity = c_int
GdkWindowEdgeh = c_int
GdkWindowTypeHint = c_int
GdkWindowAttributesType = c_int
GdkFilterReturn = c_int
GdkModifierType = c_int
GdkWMDecoration = c_int
GdkWMFunction = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GdkCursorType = c_int
GdkVisualType = c_int
GdkByteOrder = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
WebKitLoadStatus = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitEditingBehavior = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GtkDialogFlags = c_int
GtkResponseType = c_int
WebKitWebNavigationReason = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkLicense = c_int
GtkIconSize = c_int
GtkAssistantPageType = c_int
GApplicationFlags = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
GtkDestDefaults = c_int
GtkTargetFlags = c_int

from .javascriptcore__JSValue import JSValue

libjavascriptcore.JSObjectCallAsFunction.argtypes = [_JSContext,_JSObject,_JSObject,c_int,_JSValue,_JSValue]
libjavascriptcore.JSObjectCallAsFunction.restype = _JSValue

libjavascriptcore.JSObjectSetPrivate.restype = bool
libjavascriptcore.JSObjectSetPrivate.argtypes = [_JSObject,Asciifier]
libjavascriptcore.JSObjectGetProperty.restype = _JSValue
libjavascriptcore.JSObjectGetProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue]
libjavascriptcore.JSPropertyNameAccumulatorAddName.argtypes = [_JSObject,_JSPropertyNameAccumulator,_JSString]        
libjavascriptcore.JSObjectSetPrototype.argtypes = [_JSContext,_JSObject,_JSValue]
libjavascriptcore.JSObjectHasProperty.restype = bool
libjavascriptcore.JSObjectHasProperty.argtypes = [_JSContext,_JSObject,_JSString]
libjavascriptcore.JSObjectGetPrototype.restype = _JSValue
libjavascriptcore.JSObjectGetPrototype.argtypes = [_JSContext,_JSObject]
libjavascriptcore.JSObjectCallAsConstructor.restype = _JSObject
libjavascriptcore.JSObjectCallAsConstructor.argtypes = [_JSContext,_JSObject,size_t,_JSValue,_JSValue]
libjavascriptcore.JSPropertyNameArrayRelease.argtypes = [_JSObject,_JSPropertyNameArray]
libjavascriptcore.JSObjectCopyPropertyNames.restype = _JSPropertyNameArray
libjavascriptcore.JSObjectCopyPropertyNames.argtypes = [_JSContext,_JSObject]
libjavascriptcore.JSObjectMakeFunction.restype = _JSObject
libjavascriptcore.JSObjectMakeFunction.argtypes = [_JSContext,_JSString,unsigned,_JSString,_JSString,_JSString,c_int,_JSValue]
libjavascriptcore.JSObjectSetPropertyAtIndex.argtypes = [_JSContext,_JSObject,unsigned,_JSValue,_JSValue]
libjavascriptcore.JSPropertyNameArrayRetain.restype = _JSPropertyNameArray
libjavascriptcore.JSPropertyNameArrayRetain.argtypes = [_JSPropertyNameArray]
libjavascriptcore.JSClassRelease.argtypes = [_JSObject,_JSClass]
libjavascriptcore.JSObjectGetPropertyAtIndex.restype = OPAQUE_PTR
libjavascriptcore.JSObjectGetPropertyAtIndex.argtypes = [_JSContext,_JSObject,unsigned,_JSValue]
libjavascriptcore.JSObjectMakeFunctionWithCallback.restype = _JSObject
libjavascriptcore.JSObjectMakeFunctionWithCallback.argtypes = [_JSContext,_JSString,JSObjectCallAsFunctionCallback]
libjavascriptcore.JSObjectMakeRegExp.restype = _JSObject
libjavascriptcore.JSObjectMakeRegExp.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
libjavascriptcore.JSObjectGetPrivate.restype = c_char_p
libjavascriptcore.JSObjectGetPrivate.argtypes = [_JSObject]
libjavascriptcore.JSPropertyNameArrayGetCount.restype = size_t
libjavascriptcore.JSPropertyNameArrayGetCount.argtypes = [_JSPropertyNameArray]
libjavascriptcore.JSClassCreate.restype = _JSClass
libjavascriptcore.JSClassCreate.argtypes = [POINTER(JSClassDefinition)]
libjavascriptcore.JSObjectMake.restype = _JSObject
libjavascriptcore.JSObjectMake.argtypes = [_JSContext,_JSClass,Asciifier]
libjavascriptcore.JSObjectSetProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue,JSPropertyAttributes,_JSValue]

class JSObject( JSValue ):
    """Class JSObject Constructors"""
    def __init__(self, obj , context):
        #assert( isinstance( obj, OPAQUE_PTR))
        JSValue.__init__(self, obj, context)
        
    """Methods"""
    def GetProperty(  self, propertyName, exception, ):
        if propertyName: propertyName = propertyName._object()
        else: propertyName = JSValue.MakeNull(self._context)
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()

        from .javascriptcore import JSValue, JSContext
        if isinstance( self, JSContext):
            raise AttributeError("No such attribute")
        else:
            context = self._context
        if self._object() and propertyName and context._object():
            retval =  JSValue( obj=libjavascriptcore.JSObjectGetProperty\
                            ( context._object(),
                              self._object(),propertyName,exception ),
                            context = context)
            return retval
        else:
            return None

    def JSPropertyNameAccumulatorAddName(  self, accumulator, propertyName, ):
        if accumulator: accumulator = accumulator._object()
        else: accumulator = OPAQUE_PTR()
        if propertyName: propertyName = propertyName._object()
        else: propertyName = OPAQUE_PTR()
        if self._object():

            libjavascriptcore.JSPropertyNameAccumulatorAddName( self._object(),accumulator,propertyName )

    def SetPrototype(  self, ctx, value, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if value: value = value._object()
        else: value = OPAQUE_PTR()

        
        if self._object():
            libjavascriptcore.JSObjectSetPrototype( ctx,self._object(),value )

    def HasProperty(  self, ctx, propertyName, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if propertyName: propertyName = propertyName._object()
        else: propertyName = OPAQUE_PTR()

        if self._object():
            return libjavascriptcore.JSObjectHasProperty( ctx,self._object(),propertyName )

    def GetPrototype(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()

        from .javascriptcore import JSValue
        if self._object():
            return JSValue( obj=libjavascriptcore.JSObjectGetPrototype( ctx,self._object() )  or OPAQUE_PTR())

    def CallAsConstructor(  self, ctx, argumentCount, arguments, exception, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()

        from .javascriptcore import JSObject
        if argumentCount.value:
            args = (_JSValue*(argumentCount.value))()
            for index in range(argumentCount.value):
                args[index] = arguments[index]._object()
                
        else:
            args = NULL
        if self._object():
            return JSObject(obj=libjavascriptcore.JSObjectCallAsConstructor\
                            ( ctx,self._object(),argumentCount.value,
                              cast(args, OPAQUE_PTR),exception ),
                            context = self._context)
        
    def JSPropertyNameArrayRelease(  self, array, ):
        if array: array = array._object()
        else: array = OPAQUE_PTR()        
        if self._object():
            libjavascriptcore.JSPropertyNameArrayRelease( self._object(),array )

    def DeleteProperty(  self, ctx, propertyName, exception, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if propertyName: propertyName = propertyName._object()
        else: propertyName = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()

        libjavascriptcore.JSObjectDeleteProperty.restype = bool
        libjavascriptcore.JSObjectDeleteProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue]
        
        if self._object():
            return libjavascriptcore.JSObjectDeleteProperty( ctx,self._object(),propertyName,exception )

    def IsConstructor(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()

        libjavascriptcore.JSObjectIsConstructor.restype = bool
        libjavascriptcore.JSObjectIsConstructor.argtypes = [_JSContext,_JSObject]
        
        if self._object():
            return libjavascriptcore.JSObjectIsConstructor( ctx, self._object() )

    def SetPropertyAtIndex(  self, ctx, propertyIndex, value, exception, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if propertyIndex: propertyIndex = propertyIndex._object()
        else: propertyIndex = OPAQUE_PTR()
        if value: value = value._object()
        else: value = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()

        
        if self._object():
            libjavascriptcore.JSObjectSetPropertyAtIndex( ctx,self._object(),propertyIndex,value,exception )

    def SetPrivate(  self, data, ):
        
        return libjavascriptcore.JSObjectSetPrivate( self._object(), str(data).encode('ascii') )

    def JSClassRelease(  self, jsClass, ):
        if jsClass: jsClass = jsClass._object()
        else: jsClass = OPAQUE_PTR()

        
        if self._object():
            libjavascriptcore.JSClassRelease( self._object(),jsClass )

    def CallAsFunction(  self, ctx, thisObject, argumentCount, arguments, exception, ):
        if exception and exception != True: exception = exception._object()
        else: exception = None
        if argumentCount.value:
            args = (_JSValue*(argumentCount.value))()
            for index in range(argumentCount.value):
                args[index] = arguments[index]._object()
                
        else:
            args = NULL
        if thisObject:
            thisObject = thisObject._object()
        else:
            thisObject = NULL
        
        if self._object():
            if not thisObject:
                thisObject = self._object()
            retval = libjavascriptcore.JSObjectCallAsFunction( ctx._object(),
                                                           self._object(),
                                                           thisObject,
                                                           argumentCount,
                                                           cast(args, OPAQUE_PTR),
                                                           exception )
            return JSValue( obj= retval, context = ctx)

    def CopyPropertyNames(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()

        from .javascriptcore import JSPropertyNameArray
        return JSPropertyNameArray( obj=libjavascriptcore.JSObjectCopyPropertyNames( ctx,self._object() )  or OPAQUE_PTR())

    def GetPropertyAtIndex(  self, propertyIndex, exc, ):
        
        from .javascriptcore import JSValue
        if self._object():
            return JSValue( obj=libjavascriptcore.JSObjectGetPropertyAtIndex
                            ( self._context._object(),
                              self._object(),propertyIndex,exc)  or
                            OPAQUE_PTR())

    def GetPrivate(  self, ):
        
        if self._object():
            return libjavascriptcore.JSObjectGetPrivate( self._object() )

    def SetProperty(  self, ctx, propertyName, value, attributes, exception, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if propertyName: propertyName = propertyName._object()
        else: propertyName = OPAQUE_PTR()
        if value: value = value._object()
        else: value = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()

        if self._object():
            libjavascriptcore.JSObjectSetProperty( ctx,self._object(),propertyName,value,attributes,exception )

    def IsFunction(  self, ctx, ):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()

        if self._object():
            libjavascriptcore.JSObjectIsFunction.restype = bool
            libjavascriptcore.JSObjectIsFunction.argtypes = [_JSContext,_JSObject]
        
            return libjavascriptcore.JSObjectIsFunction( ctx,self._object() )

    @staticmethod
    def JSClassRetain( jsClass,):
        if jsClass: jsClass = jsClass._object()
        else: jsClass = OPAQUE_PTR()
        libjavascriptcore.JSClassRetain.restype = _JSClass
        libjavascriptcore.JSClassRetain.argtypes = [_JSClass]
        from .javascriptcore import JSClass
        return JSClass( obj=    libjavascriptcore.JSClassRetain(jsClass, )
  or OPAQUE_PTR())

    @staticmethod
    def MakeError( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if arguments: arguments = arguments._object()
        else: arguments = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()
        libjavascriptcore.JSObjectMakeError.restype = _JSObject
        libjavascriptcore.JSObjectMakeError.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from .javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeError(ctx, argumentCount, arguments, exception, )
  or OPAQUE_PTR())
    
    @staticmethod
    def MakeFunctionWithCallback( ctx, name, callAsFunction,):
        if name: name = name._object()
        else: name = OPAQUE_PTR()
        from .javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeFunctionWithCallback(ctx._object(), name, callAsFunction, ),
                         context = ctx)
                         
    @staticmethod
    def MakeArray( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if arguments: arguments = arguments._object()
        else: arguments = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()
        libjavascriptcore.JSObjectMakeArray.restype = _JSObject
        libjavascriptcore.JSObjectMakeArray.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from .javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeArray(ctx, argumentCount, arguments, exception, )
  or OPAQUE_PTR())
    @staticmethod
    def MakeConstructor( ctx, jsClass, callAsConstructor,):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if jsClass: jsClass = jsClass._object()
        else: jsClass = OPAQUE_PTR()
        libjavascriptcore.JSObjectMakeConstructor.restype = _JSObject
        libjavascriptcore.JSObjectMakeConstructor.argtypes = [_JSContext,_JSClass,JSObjectCallAsConstructorCallback]
        from .javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeConstructor(ctx, jsClass, callAsConstructor, )
  or OPAQUE_PTR())
    
    @staticmethod
    def MakeDate( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if arguments: arguments = arguments._object()
        else: arguments = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()
        libjavascriptcore.JSObjectMakeDate.restype = _JSObject
        libjavascriptcore.JSObjectMakeDate.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from .javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeDate(ctx, argumentCount, arguments, exception, )
  or OPAQUE_PTR())
    
    @staticmethod
    def JSPropertyNameArrayRetain( array,):
        if array: array = array._object()
        else: array = OPAQUE_PTR()
        from .javascriptcore import JSPropertyNameArray
        return JSPropertyNameArray( obj=    libjavascriptcore.JSPropertyNameArrayRetain(array, )
  or OPAQUE_PTR())
    
    @staticmethod
    def JSPropertyNameArrayGetNameAtIndex( array, index,):
        if array: array = array._object()
        else: array = OPAQUE_PTR()
        libjavascriptcore.JSPropertyNameArrayGetNameAtIndex.restype = _JSString
        libjavascriptcore.JSPropertyNameArrayGetNameAtIndex.argtypes = [_JSPropertyNameArray,size_t]
        from .javascriptcore import JSString
        return JSString( obj=    libjavascriptcore.JSPropertyNameArrayGetNameAtIndex(array, index, )
  or OPAQUE_PTR())
    
    @staticmethod
    def MakeFunction( ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception,):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if name: name = name._object()
        else: name = OPAQUE_PTR()
        if parameterCount: parameterCount = parameterCount._object()
        else: parameterCount = OPAQUE_PTR()
        if parameterNames: parameterNames = parameterNames._object()
        else: parameterNames = OPAQUE_PTR()
        if body: body = body._object()
        else: body = OPAQUE_PTR()
        if sourceURL: sourceURL = sourceURL._object()
        else: sourceURL = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()
        from .javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeFunction(ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception, )
  or OPAQUE_PTR())
    
    @staticmethod
    def Make( ctx, jsClass, data,):
        if jsClass: jsClass = jsClass._object()
        else: jsClass = OPAQUE_PTR()
        from .javascriptcore import JSObject, JSValue
        obj =   libjavascriptcore.JSObjectMake(ctx._object(), jsClass, str(data).encode('ascii'))
        return JSObject( obj=  obj,
                         context = ctx)
    @staticmethod
    def JSPropertyNameArrayGetCount( array,):
        if array: array = array._object()
        else: array = OPAQUE_PTR()
        
        return     libjavascriptcore.JSPropertyNameArrayGetCount(array, )

    @staticmethod
    def MakeRegExp( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object()
        else: ctx = OPAQUE_PTR()
        if arguments: arguments = arguments._object()
        else: arguments = OPAQUE_PTR()
        if exception: exception = exception._object()
        else: exception = OPAQUE_PTR()
        from .javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeRegExp(ctx, argumentCount, arguments, exception, )
  or OPAQUE_PTR())
    
    @staticmethod
    def JSClassCreate( definition,):
        from .javascriptcore import JSClass
        obj= libjavascriptcore.JSClassCreate(definition )
        return JSClass( obj = obj  or OPAQUE_PTR())

    def __getattr__(self, attr):
        from .javascriptcore import JSContext
        assert(self._context or isinstance(self, JSContext))
        if isinstance(self, JSContext):
            context = self
        else:
            assert(self._context)
            context = self._context
        if attr == "__len__":
            from .javascript import JSString
            name = JSString.CreateWithUTF8CString("length")
            length = self.GetProperty( name, NULL )
            name.Release()
            if length.GetType( context ) == kJSTypeUndefined.value:
                raise AttributeError( "No such attribute: length")
            val = int(length.ToNumber( context, NULL ))
            def _len():
                return val
            return _len
        from .javascriptcore import JSString
        text = JSString.CreateWithUTF8CString( attr)
        prop = self.GetProperty( text , NULL)
        text.Release()
        if prop is None:
            return None
        jstype = prop.GetType(context)
        if jstype == kJSTypeNull.value:
            return None#object.__getattribute__(self, attr)
        elif jstype == kJSTypeObject.value or jstype == kJSTypeUndefined.value:
            propobj = prop.ToObject(context, NULL)
            if propobj.IsFunction(context):
                from .javascript import JSFunction
                jsfunc = JSFunction(context, obj = propobj, thisobj = self, name = attr)
                setattr(self, attr, 
                        jsfunc)
                return jsfunc
            else:
                setattr(self, attr, propobj)
                return propobj
        elif jstype== kJSTypeNumber.value:
                val = prop.ToNumber( context, NULL)
                setattr(self, attr, val)    
                
                return val
        elif jstype==kJSTypeBoolean.value:
                val = prop.ToBoolean( context, NULL)
                setattr(self, attr, val)
                return val
        elif jstype == kJSTypeString.value:
                val = prop.ToPyString( context, NULL)
                setattr (self, attr, val)
                return val
        raise Exception("unknown javascript type")
        
    def __iter__(self, index):
        if isinstance(self, JSContext):
            context = self
        else:
            assert(self._context)
            context = self._context
        prop = self.GetPropertyAtIndex( index , NULL)
        jstype = prop.GetType(context)
        if jstype == kJSTypeUndefined.value:
            return object.__getattribute__(self, attr)
        else:
            
            if jstype == kJSTypeObject.value:
                propobj = prop.ToObject(context, NULL)
                if propobj.IsFunction(context):
                    from .javascript import JSFunction
                    jsfunc = JSFunction(context, obj = propobj, thisobj = self, name = attr)
                    setattr(self, attr, 
                            jsfunc)
                    #if cast (propobj._object(),c_void_p).value != cast (prop._object(),c_void_p).value:
                    #    prop.Unprotect( context )
                    return jsfunc
                else:
                    setattr(self, attr, prop)
                    return prop
            elif jstype== kJSTypeNumber.value:
                val = prop.ToNumber( context, NULL)
                setattr(self, attr, val)    
                
                return val
            elif jstype==kJSTypeBoolean.value:
                val = prop.ToBoolean( context, NULL)
                setattr(self, attr, val)
                return val
            elif jstype == kJSTypeString.value:
                val = prop.ToPyString( context, NULL)
                setattr (self, attr, val)
                return val
            elif jstype == kJSTypeNull.value:
                return None
        raise Exception("unknown javascript type")


