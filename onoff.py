import getsetPWM

set_PWM = getsetPWM.setPWN()
get_PWM = getsetPWM.getPWN()

class onoff(object):

    def on(self):
        set_PWM.setAllPWN(255, 255, 255)
	get_PWM.printRGB()

    def off(self):
        set_PWM.setAllPWN(0, 0, 0)
	get_PWM.printRGB()
