#!/usr/bin/python
from ctypes import *
import gtk3
import webkit3
import javascriptcore
from javascriptcore import *

def _init_cb( ctxt, object):
    print "## INITED"

def _finalize_cb( object ):
    print "##FINALIZED"

def _method_cb( ctxt, function, argumentCount, arguments, exception):
    print "##METHOD INVOKED"

static_methods = (JSStaticFunction*2)()
static_methods[0].name = c_char_p("test_method")
static_methods[0].callAsFunction = JSObjectCallAsFunctionCallback(_method_cb)
static_methods[0].attributes = kJSPropertyAttributeReadOnly
static_methods[0].name = cast(NULL, c_char_p)
static_methods[0].callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
static_methods[0].attributes = 0

jscd = JSClassDefinition()
jscd.version = 0
jscd.attributes = kJSClassAttributeNone
jscd.className = c_char_p("TestClass")
jscd.parentClass = NULL
jscd.staticValues = POINTER(JSStaticValue)()
jscd.staticFunctions = static_methods
jscd.initialize = JSObjectInitializeCallback (_init_cb)
jscd.finalize = JSObjectFinalizeCallback ( _finalize_cb)
jscd.hasProperty = cast(NULL,JSObjectHasPropertyCallback)
jscd.getProperty = cast(NULL,JSObjectGetPropertyCallback)
jscd.setPrpoerty = cast(NULL,JSObjectSetPropertyCallback)
jscd.deleteProprety = cast(NULL,JSObjectDeletePropertyCallback)
jscd.getPropertyName = cast(NULL, JSObjectGetPropertyNamesCallback)
jscd.callAsFunction = cast(NULL, JSObjectCallAsFunctionCallback)
jscd.callAsConstructor = cast(NULL,JSObjectCallAsConstructorCallback)
jscd.hasInstance = cast(NULL,JSObjectHasInstanceCallback)
jscd.convertToType = cast(NULL, JSObjectConvertToTypeCallback)

items = [jscd]

def addJSClass( gctxt ):
    import logging
    logging.error( "NAME: %s"%jscd.className )
    #cdll.LoadLibrary("libt.so")
    #libt = CDLL("libt.so")
    #libt.JSClassCreate2( byref(jscd) )
    classDef = javascriptcore.JSObject.JSClassCreate( byref(jscd) )
    logging.error("GOT DEF %s from %s"%(classDef, gctxt))
    obj = javascriptcore.JSObject.JSObjectMake( gctxt, classDef, gctxt )
    globalObj = JSContext(gctxt).JSContextGetGlobalObject( )
    text = javascriptcore.JSString.JSStringCreateWithUTF8CString("testclass")
    javascriptcore.JSObject.JSObjectSetProperty( gctxt, globalObj, text,
                                                 obj, kJSPropertyAttributeNone,
                                                 NULL)
    
web = webkit3.WebKitWebView()
web.load_uri("http://www.google.com")

window = gtk3.GtkWindow(gtk3.GTK_WINDOW_TOPLEVEL)
window.connect("delete-event", gtk3.main_quit)
window.add(web)
window.set_default_size( 1000, 800)
window.show_all()

context = web.get_javascript_global_context()
addJSClass(context)

gtk3.main()
