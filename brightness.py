import getsetPWM

set_PWM = getsetPWM.setPWN()
get_PWM = getsetPWM.getPWN()

MAX_BRIGHTNESS=255
MIN_BRIGHTNESS=0

class brightness(object):

    def up(self):
        blue = get_PWM.getBluePWN()
        red = get_PWM.getRedPWN()
        green = get_PWM.getGreenPWN()

        new_blue = blue + 1
        new_red = red + 1
        new_green = green + 1

        if new_blue > MAX_BRIGHTNESS:
            new_blue = MAX_BRIGHTNESS

        if new_red > MAX_BRIGHTNESS:
            new_red = MAX_BRIGHTNESS

        if new_green > MAX_BRIGHTNESS:
            new_green = MAX_BRIGHTNESS

        set_PWM.setAllPWN(new_blue, new_red, new_green)

    def down(self):
        blue = get_PWM.getBluePWN()
        red = get_PWM.getRedPWN()
        green = get_PWM.getGreenPWN()

        new_blue = blue - 1
        new_red = red - 1
        new_green = green - 1

        if new_blue < MIN_BRIGHTNESS:
            new_blue = MIN_BRIGHTNESS

        if new_red < MIN_BRIGHTNESS:
            new_red = MIN_BRIGHTNESS

        if new_green < MIN_BRIGHTNESS:
            new_green = MIN_BRIGHTNESS

        set_PWM.setAllPWN(new_blue, new_red, new_green)

    def user(self, brightness):
        blue = get_PWM.getBluePWN()
        red = get_PWM.getRedPWN()
        green = get_PWM.getGreenPWN()

	relativeBrightness = brightness / float(MAX_BRIGHTNESS)
	print(relativeBrightness)

        new_blue = round(blue * relativeBrightness)
        new_red = round(red * relativeBrightness)
        new_green = round(green * relativeBrightness)

	if brightness > new_blue:
	   relativeBrightnessBlue = (blue + brightness) / float(MAX_BRIGHTNESS)		
	   new_blue = round(blue * relativeBrightnessBlue)

	if brightness > new_red:
	   relativeBrightnessRed = (red + brightness) / float(MAX_BRIGHTNESS)		
	   new_red = round(red * relativeBrightnessRed)

	if brightness > new_green:
	   relativeBrightnessGreen = (green + brightness) / float(MAX_BRIGHTNESS)		
	   new_green = round(green * relativeBrightnessGreen)

        if new_blue < MIN_BRIGHTNESS:
            new_blue = MIN_BRIGHTNESS

        if new_red < MIN_BRIGHTNESS:
            new_red = MIN_BRIGHTNESS

        if new_green < MIN_BRIGHTNESS:
            new_green = MIN_BRIGHTNESS

        if new_blue > MAX_BRIGHTNESS:
            new_blue = MAX_BRIGHTNESS

        if new_red > MAX_BRIGHTNESS:
            new_red = MAX_BRIGHTNESS

        if new_green > MAX_BRIGHTNESS:
            new_green = MAX_BRIGHTNESS

	print(new_blue)
	print(new_red)
	print(new_green)

        set_PWM.setAllPWN(new_blue, new_red, new_green)







