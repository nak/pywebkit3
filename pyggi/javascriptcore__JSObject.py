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
from gtk3_types import *
from javascriptcore_types import *
    
    
"""Derived Pointer Types"""
__GtkRcStyle = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
_WebKitWebPolicyDecision = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
_GtkBin = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
_PangoEngineShape = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
_GMainLoop = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
_GdkColor = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
_GtkContainer = POINTER(c_int)
_PangoItem = POINTER(c_int)
__GClosure = POINTER(c_int)
_GtkAboutDialog = POINTER(c_int)
__GMainContext = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
_GtkScrolledWindow = POINTER(c_int)
_GtkDialog = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
_GMainContext = POINTER(c_int)
_GBoxed = POINTER(c_int)
__GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
__GObject = POINTER(c_int)
__PangoLayout = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
_GtkOffscreenWindow = POINTER(c_int)
__GParamSpec = POINTER(c_int)
__PangoAttrIterator = POINTER(c_int)
_GtkRequisition = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAdjustment = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
_GString = POINTER(c_int)
__PangoContext = POINTER(c_int)
__JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__PangoFont = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__JSClass = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
__GtkSettings = POINTER(c_int)
_GSource = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
__GSource = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
__GMutex = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
_GdkGeometry = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_GtkBorder = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
_GdkWindowAttr = POINTER(c_int)
_GOptionGroup = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GtkContainerClass = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GtkAdjustment = POINTER(c_int)
_GdkDragContext = POINTER(c_int)
_GtkAssistant = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
__GCond = POINTER(c_int)
_GtkIconSource = POINTER(c_int)
__cairo_surface_t = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
__GActionGroup = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__PangoFontFamily = POINTER(c_int)
__JSContextGroup = POINTER(c_int)
__GPollFD = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GtkBorder = POINTER(c_int)
__GError = POINTER(c_int)
__PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
_PangoFontFamily = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
__GCancellable = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
_GPollFD = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__GFile = POINTER(c_int)
__JSContext = POINTER(c_int)
_PangoFontsetSimple = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
__GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
__PangoTabArray = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
__GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
__PangoMatrix = POINTER(c_int)
__GtkPrintOperation = POINTER(c_int)
__GString = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GtkTargetList = POINTER(c_int)
__GList = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
_GList = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__GTimeVal = POINTER(c_int)
_GtkInvisible = POINTER(c_int)
__GSourceFuncs = POINTER(c_int)
__JSPropertyNameAccumulator = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GSList = POINTER(c_int)
_PangoAnalysis = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkAtom = POINTER(c_int)
__GdkColor = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
__gunichar = POINTER(c_int)
__GdkWMDecoration = POINTER(c_int)
__PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
__JSObject = POINTER(c_int)
__GdkDragContext = POINTER(c_int)
_WebKitWebNavigationAction = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
__GIcon = POINTER(c_int)
__GtkWindow = POINTER(c_int)
_PangoLayoutRun = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_WebKitGeolocationPolicyDecision = POINTER(c_int)
_GtkSettings = POINTER(c_int)
__GSourceCallbackFuncs = POINTER(c_int)
__PangoFontFace = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_GByteArray = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
__GdkDevice = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
_JSPropertyNameAccumulator = POINTER(c_int)

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

from javascriptcore__JSValue import JSValue

libjavascriptcore.JSObjectCallAsFunction.argtypes = [_JSContext,_JSObject,_JSObject,c_int,_JSValue,_JSValue]
libjavascriptcore.JSObjectCallAsFunction.restype = _JSValue

libjavascriptcore.JSObjectSetPrivate.restype = bool
libjavascriptcore.JSObjectSetPrivate.argtypes = [_JSObject,c_char_p]
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
libjavascriptcore.JSObjectGetPropertyAtIndex.restype = POINTER(c_int)
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
libjavascriptcore.JSObjectMake.argtypes = [_JSContext,_JSClass,c_char_p]

class JSObject( JSValue ):
    """Class JSObject Constructors"""
    def __init__(self, obj , context):
        JSValue.__init__(self, obj, context)
        
    """Methods"""
    def GetProperty(  self, ctx, propertyName, exception, ):
        #if ctx: ctx = ctx._object
        #else: ctx = POINTER(c_int)()
        #if propertyName: propertyName = propertyName._object
        #else: propertyName = POINTER(c_int)()

        from javascriptcore import JSValue
        return JSValue( obj=libjavascriptcore.JSObjectGetProperty( ctx._object,self._object,propertyName._object,exception ),
                        context = ctx._object)

    def JSPropertyNameAccumulatorAddName(  self, accumulator, propertyName, ):
        if accumulator: accumulator = accumulator._object
        else: accumulator = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()

        libjavascriptcore.JSPropertyNameAccumulatorAddName( self._object,accumulator,propertyName )

    def SetPrototype(  self, ctx, value, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if value: value = value._object
        else: value = POINTER(c_int)()

        
        libjavascriptcore.JSObjectSetPrototype( ctx,self._object,value )

    def HasProperty(  self, ctx, propertyName, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()

        return libjavascriptcore.JSObjectHasProperty( ctx,self._object,propertyName )

    def GetPrototype(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        from javascriptcore import JSValue
        return JSValue( obj=libjavascriptcore.JSObjectGetPrototype( ctx,self._object )  or POINTER(c_int)())

    def CallAsConstructor(  self, ctx, argumentCount, arguments, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        jsargs = _JSValue*argumentCount
        for index in len(argumentCount):
            jsargs[index] = arguments[index]._object
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        from javascriptcore import JSObject
        return JSObject(None,None,None,None, obj=libjavascriptcore.JSObjectCallAsConstructor( ctx,self._object,argumentCount,arguments,exception )  or POINTER(c_int)())

    def JSPropertyNameArrayRelease(  self, array, ):
        if array: array = array._object
        else: array = POINTER(c_int)()        
        libjavascriptcore.JSPropertyNameArrayRelease( self._object,array )

    def DeleteProperty(  self, ctx, propertyName, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libjavascriptcore.JSObjectDeleteProperty.restype = bool
        libjavascriptcore.JSObjectDeleteProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue]
        
        return libjavascriptcore.JSObjectDeleteProperty( ctx,self._object,propertyName,exception )

    def IsConstructor(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libjavascriptcore.JSObjectIsConstructor.restype = bool
        libjavascriptcore.JSObjectIsConstructor.argtypes = [_JSContext,_JSObject]
        
        return libjavascriptcore.JSObjectIsConstructor( ctx,self._object )

    def SetPropertyAtIndex(  self, ctx, propertyIndex, value, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyIndex: propertyIndex = propertyIndex._object
        else: propertyIndex = POINTER(c_int)()
        if value: value = value._object
        else: value = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        
        libjavascriptcore.JSObjectSetPropertyAtIndex( ctx,self._object,propertyIndex,value,exception )

    def SetPrivate(  self, data, ):
        
        return libjavascriptcore.JSObjectSetPrivate( self._object,data )

    def JSClassRelease(  self, jsClass, ):
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()

        
        libjavascriptcore.JSClassRelease( self._object,jsClass )

    def CallAsFunction(  self, ctx, thisObject, argumentCount, arguments, exception, ):
        
        if exception: exception = exception._object
        else: exception = None
        if argumentCount.value:
            args = (_JSValue*argumentCount.value)()
            for index in xrange(argumentCount.value):
                args[index] = arguments[index]._object
            
        else:
            args = NULL
        if thisObject:
            thisObject = thisObject._object
        else:
            thisObject = NULL
        
        retval = libjavascriptcore.JSObjectCallAsFunction( ctx._object,
                                                           self._object,
                                                           thisObject,
                                                           argumentCount,
                                                           cast(args, POINTER(c_int)),exception )
      
        return JSValue( obj= retval, context = ctx._object)

    def CopyPropertyNames(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        from javascriptcore import JSPropertyNameArray
        return JSPropertyNameArray( obj=libjavascriptcore.JSObjectCopyPropertyNames( ctx,self._object )  or POINTER(c_int)())

    def GetPropertyAtIndex(  self, ctx, propertyIndex, exc, ):
        if ctx: ctx = ctx._object
        else: raise Exception("NULL CONTEXT")
        
        from javascriptcore import JSValue
        return JSValue( obj=libjavascriptcore.JSObjectGetPropertyAtIndex( ctx,self._object,propertyIndex,exc)  or POINTER(c_int)())

    def GetPrivate(  self, ):
        
        return libjavascriptcore.JSObjectGetPrivate( self._object )

    def SetProperty(  self, ctx, propertyName, value, attributes, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()
        if value: value = value._object
        else: value = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libjavascriptcore.JSObjectSetProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue,JSPropertyAttributes,_JSValue]
        
        libjavascriptcore.JSObjectSetProperty( ctx,self._object,propertyName,value,attributes,exception )

    def IsFunction(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libjavascriptcore.JSObjectIsFunction.restype = bool
        libjavascriptcore.JSObjectIsFunction.argtypes = [_JSContext,_JSObject]
        
        return libjavascriptcore.JSObjectIsFunction( ctx,self._object )

    @staticmethod
    def JSClassRetain( jsClass,):
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()
        libjavascriptcore.JSClassRetain.restype = _JSClass
        libjavascriptcore.JSClassRetain.argtypes = [_JSClass]
        from javascriptcore import JSClass
        return JSClass( obj=    libjavascriptcore.JSClassRetain(jsClass, )
  or POINTER(c_int)())
    @staticmethod
    def MakeError( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        libjavascriptcore.JSObjectMakeError.restype = _JSObject
        libjavascriptcore.JSObjectMakeError.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeError(ctx, argumentCount, arguments, exception, )
  or POINTER(c_int)())
    @staticmethod
    def MakeFunctionWithCallback( ctx, name, callAsFunction,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if name: name = name._object
        else: name = POINTER(c_int)()
        from javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeFunctionWithCallback(ctx, name, callAsFunction, ),
                         context = ctx)
                         
    @staticmethod
    def MakeArray( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        libjavascriptcore.JSObjectMakeArray.restype = _JSObject
        libjavascriptcore.JSObjectMakeArray.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeArray(ctx, argumentCount, arguments, exception, )
  or POINTER(c_int)())
    @staticmethod
    def MakeConstructor( ctx, jsClass, callAsConstructor,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()
        libjavascriptcore.JSObjectMakeConstructor.restype = _JSObject
        libjavascriptcore.JSObjectMakeConstructor.argtypes = [_JSContext,_JSClass,JSObjectCallAsConstructorCallback]
        from javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeConstructor(ctx, jsClass, callAsConstructor, )
  or POINTER(c_int)())
    @staticmethod
    def MakeDate( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        libjavascriptcore.JSObjectMakeDate.restype = _JSObject
        libjavascriptcore.JSObjectMakeDate.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeDate(ctx, argumentCount, arguments, exception, )
  or POINTER(c_int)())
    @staticmethod
    def JSPropertyNameArrayRetain( array,):
        if array: array = array._object
        else: array = POINTER(c_int)()
        from javascriptcore import JSPropertyNameArray
        return JSPropertyNameArray( obj=    libjavascriptcore.JSPropertyNameArrayRetain(array, )
  or POINTER(c_int)())
    @staticmethod
    def JSPropertyNameArrayGetNameAtIndex( array, index,):
        if array: array = array._object
        else: array = POINTER(c_int)()
        libjavascriptcore.JSPropertyNameArrayGetNameAtIndex.restype = _JSString
        libjavascriptcore.JSPropertyNameArrayGetNameAtIndex.argtypes = [_JSPropertyNameArray,size_t]
        from javascriptcore import JSString
        return JSString( obj=    libjavascriptcore.JSPropertyNameArrayGetNameAtIndex(array, index, )
  or POINTER(c_int)())
    @staticmethod
    def MakeFunction( ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if name: name = name._object
        else: name = POINTER(c_int)()
        if parameterCount: parameterCount = parameterCount._object
        else: parameterCount = POINTER(c_int)()
        if parameterNames: parameterNames = parameterNames._object
        else: parameterNames = POINTER(c_int)()
        if body: body = body._object
        else: body = POINTER(c_int)()
        if sourceURL: sourceURL = sourceURL._object
        else: sourceURL = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        from javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeFunction(ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception, )
  or POINTER(c_int)())
    @staticmethod
    def Make( ctx, jsClass, data,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()
        from javascriptcore import JSObject, JSValue
        obj =   libjavascriptcore.JSObjectMake(ctx, jsClass, data, )
        return JSObject( obj=  obj,
                         context = ctx)
    @staticmethod
    def JSPropertyNameArrayGetCount( array,):
        if array: array = array._object
        else: array = POINTER(c_int)()
        
        return     libjavascriptcore.JSPropertyNameArrayGetCount(array, )

    @staticmethod
    def MakeRegExp( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        from javascriptcore import JSObject
        return JSObject( obj=    libjavascriptcore.JSObjectMakeRegExp(ctx, argumentCount, arguments, exception, )
  or POINTER(c_int)())
    @staticmethod
    def JSClassCreate( definition,):
        from javascriptcore import JSClass
        return JSClass( obj= libjavascriptcore.JSClassCreate(definition, )  or POINTER(c_int)())

        
