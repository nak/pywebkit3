from pyggi.javascript import *



class YPR_Updater( JavascriptClass ):
    """
    This class is reponsible for updating the yaw pitch an roll
    (orientation) of a cube, with the javascript calling the
    update method and get methods.  By inheriting from JavascriptClass,
    when this module is exported to javascript, it will automatically
    become available to execute under javascript code!
    """

    
    def __init__(self, env, name, *init_angles):
        assert(isinstance(env, ScriptEnv))
        JavascriptClass.__init__(self, env, name )
        self.ypr =  [angl for angl in init_angles]
        self.sign = 1
        

    def __del__(self):
        pass

    index = 0
    def update(self, offset_yaw, offset_pitch, offset_roll):
        import logging
        if YPR_Updater.index == 100:
            try:
                # On the 100th update, import a javascript object
                # and call it.  This object has a func method that
                # simply generates an alert
                alerter = self._env.get_jsobject("alerter", can_call=False)
                import logging
                returnval = alerter.func()
                logging.info("Got response from caling javascript objet of  %s"%returnval)
            except:
                import logging
                import traceback
                logging.error("EXCEPTION IN GETTIN JS OBJ")
                logging.error( traceback.print_exc() )
        YPR_Updater.index += 1
        # Now update the angles for yaw pitch roll for next iteration
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
