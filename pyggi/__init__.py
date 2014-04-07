import sys, os
import platform
from ctypes import CDLL, cdll

PLATFORM = platform.platform()


def load( libname, postversion ):
    
    if PLATFORM.startswith("Windows"):
        WINPATH=os.path.join( os.path.dirname(__file__),"lib", "Windows")
        os.environ['PATH'] = ';'.join( [WINPATH, os.environ['PATH']])
        try:
            cdll.LoadLibrary("%s.dll"%(libname))
            return CDLL("%s.dll"%( libname))
        except:
            try:
                import logging
                logging.info("Unable to load %s trying %s-0"%(libname, libname))
                cdll.LoadLibrary("%s-0.dll"%(libname))
                return CDLL("%s-0.dll"%(libname))
            except:
                import traceback
                traceback.print_exc()
                logging.error("Unable to load %s. Aborting"%libname)
                import sys
                sys.exit(1)
    elif PLATFORM.startswith("Darwin"):
        try:
            
            cdll.LoadLibrary("/opt/local/lib/%s.%s.dylib"%( libname, postversion))
            return CDLL("/opt/local/lib/%s.%s.dylib"%( libname, postversion))
        except:
            try:
                cdll.LoadLibrary("%s.%s.dylib"%( libname, postversion))
                return CDLL("%s.%s.dylib"%( libname, postversion))
            except:
                import logging
                logging.error("Unable to load '/opt/local/lib/%s.%s.dylib'. Aborting"%(libname,postversion))
                import sys
                sys.exit(1)
        
    else:
        try:
            cdll.LoadLibrary("%s.so.%s"%(libname,postversion))
            return CDLL("%s.so.%s"%(libname, postversion))
        except:
            import logging
            logging.error("Unable to load %s. Aborting"%(libname))
            import sys
            sys.exit(1)
