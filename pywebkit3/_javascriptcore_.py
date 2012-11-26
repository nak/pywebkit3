# Copyright, John Rusnak, 2012
# This code is available under the license agreement of the LGPL,
# with the additional constraint that any derivatives of this work aimed
# at providing bindings to GObject, GTK, GDK, or WebKit be strictly
# python-only bindings with no native code.
from ctypes import *
from gtk3_types import *
from javascriptcore_types import *


"""Derived Pointer Types"""
_JSObject = c_void_p
_JSGlobalContext = c_void_p
_JSContext = c_void_p
_JSClass = c_void_p
_JSContextGroup = c_void_p
"""Enumerations"""


def JSGlobalContextCreateInGroup( group, globalObjectClass,):
    if group : group = group._object
    else : group = c_void_p()
    if globalObjectClass : globalObjectClass = globalObjectClass._object
    else : globalObjectClass = c_void_p()
    libjavascriptcore.JSGlobalContextCreateInGroup.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextCreateInGroup.argtypes = [_JSContextGroup,_JSClass]
    return libjavascriptcore.JSGlobalContextCreateInGroup( group, globalObjectClass,)


def JSContextGroupRetain( group,):
    if group : group = group._object
    else : group = c_void_p()
    libjavascriptcore.JSContextGroupRetain.restype = _JSContextGroup
    libjavascriptcore.JSContextGroupRetain.argtypes = [_JSContextGroup]
    return libjavascriptcore.JSContextGroupRetain( group,)


def JSContextGetGlobalObject( ctx,):
    if ctx : ctx = ctx._object
    else : ctx = c_void_p()
    libjavascriptcore.JSContextGetGlobalObject.restype = _JSObject
    libjavascriptcore.JSContextGetGlobalObject.argtypes = [_JSContext]
    return libjavascriptcore.JSContextGetGlobalObject( ctx,)


def JSGlobalContextCreate( globalObjectClass,):
    if globalObjectClass : globalObjectClass = globalObjectClass._object
    else : globalObjectClass = c_void_p()
    libjavascriptcore.JSGlobalContextCreate.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextCreate.argtypes = [_JSClass]
    return libjavascriptcore.JSGlobalContextCreate( globalObjectClass,)


def JSContextGetGroup( ctx,):
    if ctx : ctx = ctx._object
    else : ctx = c_void_p()
    libjavascriptcore.JSContextGetGroup.restype = _JSContextGroup
    libjavascriptcore.JSContextGetGroup.argtypes = [_JSContext]
    return libjavascriptcore.JSContextGetGroup( ctx,)


def JSGlobalContextRetain( ctx,):
    if ctx : ctx = ctx._object
    else : ctx = c_void_p()
    libjavascriptcore.JSGlobalContextRetain.restype = _JSGlobalContext
    libjavascriptcore.JSGlobalContextRetain.argtypes = [_JSGlobalContext]
    return libjavascriptcore.JSGlobalContextRetain( ctx,)

