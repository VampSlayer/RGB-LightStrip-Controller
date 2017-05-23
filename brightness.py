import getsetPWM

set_PWM = getsetPWM.setPWN()
get_PWM = getsetPWM.getPWM()

class brightness(object):

    def up(self):
        blue = get_PWM.getBluePWN
        red = get_PWM.getRedPWN
        green = get_PWM.getGreenPWN

        new_blue = blue + 1
        new_red = red + 1
        new_green = green + 1

        if new_blue > 255:
            new_blue = 255

        if new_red > 255:
            new_red = 255

        if new_green > 255:
            new_green = 255

        set_PWM.setAllPWN(new_blue, new_red, new_green)

    def down(self):
        blue = get_PWM.getBluePWN
        red = get_PWM.getRedPWN
        green = get_PWM.getGreenPWN

        new_blue = blue - 1
        new_red = red - 1
        new_green = green - 1

        if new_blue < 0:
            new_blue = 0

        if new_red < 0:
            new_red = 0

        if new_green < 0:
            new_green = 0

        set_PWM.setAllPWN(new_blue, new_red, new_green)
