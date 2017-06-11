import getsetPWM
import brightnessCheck

set_PWM = getsetPWM.setPWN()
get_PWM = getsetPWM.getPWN()
brightnessCheck = brightnessCheck.brightnessCheck()

MAX_BRIGHTNESS=255
MIN_BRIGHTNESS=0
STEP=1

class brightness(object):

    def up(self):
        blue = get_PWM.getBluePWN()
        red = get_PWM.getRedPWN()
        green = get_PWM.getGreenPWN()

        new_blue = blue + (blue * (float(STEP) / float(blue))) if blue !=0 else 0
        new_red = red + (red * (float(STEP) / float(red))) if red !=0 else 0
        new_green = green + (green * (float(STEP) / float(green))) if green !=0 else 0

        new_blue = brightnessCheck.checkMaximum(new_blue)
	new_red = brightnessCheck.checkMaximum(new_red)
	new_green = brightnessCheck.checkMaximum(new_green)

        set_PWM.setAllPWN(new_blue, new_red, new_green)
	get_PWM.printRGB()

    def down(self):
        blue = get_PWM.getBluePWN()
        red = get_PWM.getRedPWN()
        green = get_PWM.getGreenPWN()

        new_blue = blue - STEP
        new_red = red - STEP
        new_green = green - STEP

        new_blue = brightnessCheck.checkMinimum(new_blue)
	new_red = brightnessCheck.checkMinimum(new_red)
	new_green = brightnessCheck.checkMinimum(new_green)

        set_PWM.setAllPWN(new_blue, new_red, new_green)
	get_PWM.printRGB()

    def user(self, brightness):
        blue = get_PWM.getBluePWN()
        red = get_PWM.getRedPWN()
        green = get_PWM.getGreenPWN()

        new_blue = blue * (float(brightness) / float(blue)) if blue !=0 else 0
        new_red = red * (float(brightness) / float(red)) if red !=0 else 0
        new_green = green * (float(brightness) / float(green)) if green !=0 else 0

        new_blue = brightnessCheck.checkMinimum(new_blue)
	new_red = brightnessCheck.checkMinimum(new_red)
	new_green = brightnessCheck.checkMinimum(new_green)

        new_blue = brightnessCheck.checkMaximum(new_blue)
	new_red = brightnessCheck.checkMaximum(new_red)
	new_green = brightnessCheck.checkMaximum(new_green)

        set_PWM.setAllPWN(new_blue, new_red, new_green)
	get_PWM.printRGB()
