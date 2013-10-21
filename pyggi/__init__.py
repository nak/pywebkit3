import sys
import platform
from ctypes import CDLL, cdll

PLATFORM = platform.platform()

def load( libname, postversion ):
    
    if PLATFORM.startswith("Windows"):
        try:
            cdll.LoadLibrary("%s-%s.dll"%( libname, postversion))
            return CDLL("%s-%s.dll"%( libname, postversion))
        except:
            import logging
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
