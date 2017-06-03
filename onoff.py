import getsetPWM

set_PWM = getsetPWM.setPWN()

class onoff(object):

    def on(self):
        set_PWM.setAllPWN(255, 255, 255)

    def off(self):
        set_PWM.setAllPWN(0, 0, 0)
