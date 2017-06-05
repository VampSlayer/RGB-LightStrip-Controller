import getsetPWM

set_PWM = getsetPWM.setPWN()
get_PWM = getsetPWM.getPWN()

class colors(object):

    def white(self):
        set_PWM.setAllPWN(255, 255, 255)
	get_PWM.printRGB()

    def blue(self):
        set_PWM.setAllPWN(255, 0, 0)
	get_PWM.printRGB()

    def red(self):
        set_PWM.setAllPWN(0, 255, 0)
	get_PWM.printRGB()

    def green(self):
        set_PWM.setAllPWN(0, 0, 255)
	get_PWM.printRGB()

    def user(self, blue, red, green):
        set_PWM.setAllPWN(blue, red, green)
	get_PWM.printRGB()
