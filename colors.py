import getsetPWM

set_PWM = getsetPWM.setPWN()

class colors(object):

    def white(self):
        set_PWM.setAllPWN(255, 255, 255)

    def blue(self):
        set_PWM.setAllPWN(255, 0, 0)

    def red(self):
        set_PWM.setAllPWN(0, 255, 0)

    def green(self):
        set_PWM.setAllPWN(0, 0, 255)

    def user(self, blue, red, green):
        pi.set_PWM_dutycycle(BLUE_PIN, blue)
        pi.set_PWM_dutycycle(RED_PIN, red)
        pi.set_PWM_dutycycle(GREEN_PIN, green)
        set_PWM.setAllPWN(blue, red, green)
