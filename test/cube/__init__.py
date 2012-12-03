from pywebkit3.javascript import *



class YPR_Updater( JavascriptClass ):
    """This class is reponsible for updating the yaw pitch an roll
    (orientation) of a cube, with the javascript calling the
    update metho and get methods"""

    web = None
    
    def __init__(self, context, name, *init_angles):
        JavascriptClass.__init__(self, context, name )
        print "ARGS: %s"%[a for a in init_angles]
        self.ypr =  [a for a in init_angles]
        self.sign = 1
        print "YPRUpdater initialize"

    def __del__(self):
        pass

    index = 0
    def update(self, offset_yaw, offset_pitch, offset_roll):
        from pywebkit3.javascript import ScriptEnv
        if YPR_Updater.index == 100:
            try:
                tmp = ScriptEnv.get_jsobject(YPR_Updater.web,
                                             "tmp", can_call=False)
                tmp.func()
            except:
                import logging
                import traceback
                logging.error("EXCEPTION IN GETTIN JS OBJ")
                logging.error( traceback.print_exc() )
            finally:
                import logging
                logging.error("...CALLED")
        YPR_Updater.index += 1
        self.ypr[0] += offset_yaw
        self.ypr[1] += offset_pitch
        self.ypr[2] += offset_roll
        if(self.ypr[2]> 90 ):
            self.sign=-self.sign;
            
            self.ypr[2] -= 180;
            self.ypr[0] -= 180;
            self.ypr[1] = 180-self.ypr[1];
             

        if(self.ypr[0]>=360):
            self.ypr[0] -=360;
        else:
            self.ypr[0] += 360;
    
        if(self.ypr[1]>=180) :
            self.ypr[1] -= 360;
        else:
            self.ypr[1] += 360;
    

    def yaw(self):
        return self.ypr[0]

    def pitch(self):
        return self.ypr[1]

    def roll(self):
        return self.ypr[2]
