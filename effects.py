import getsetPWM
import time

set_PWM = getsetPWM.setPWN()
get_PWM = getsetPWM.getPWN()

class effects(object):

    def flashcolors(self):
        #flash between colors
        var = 1
	timeSleep = 0.4
        while var == 1:      # This constructs an infinite loop
            set_PWM.setAllPWN(255, 0, 0) #blue
	    time.sleep(timeSleep)
            set_PWM.setAllPWN(255, 255, 0) #purple
            time.sleep(timeSleep)
            set_PWM.setAllPWN(0, 255, 0) #red
	    time.sleep(timeSleep)
            set_PWM.setAllPWN(0, 255, 255) #red+green
            time.sleep(timeSleep)
            set_PWM.setAllPWN(0, 0, 255) #green
	    time.sleep(timeSleep)
            set_PWM.setAllPWN(255, 255, 255) #white
            time.sleep(timeSleep)
            set_PWM.setAllPWN(255, 0, 255) #blue+green
	    time.sleep(timeSleep)

    def strobe(self):
        # goes from previous setting to min then to previous setting
        blue = get_PWM.getBluePWN()
        red = get_PWM.getRedPWN()
        green = get_PWM.getGreenPWN()

        # read color. then switch that color to 0 then back to max
        var = 1
	timeSleep = 0.4
        while var == 1:
            set_PWM.setAllPWN(0, 0, 0)
	    time.sleep(timeSleep)
            set_PWM.setAllPWN(blue, red, green)
	    time.sleep(timeSleep)

    def fade(self):
        # goes incrementally from  white max to min then to max etc.
        step = 1
        maximum = 255
        blue = maximum
        red = maximum
        green = maximum
	timeSleep = 0.01
        set_PWM.setAllPWN(blue, red, green)

        var = 1
        while var == 1:
            while blue != 0 and blue <= maximum:
                blue = blue - step
                red = red - step
                green = green - step
		time.sleep(timeSleep)
                set_PWM.setAllPWN(blue, red, green)

            while blue >= 0 and blue != maximum:
                blue = blue + step
                red = red + step
                green = green + step
		time.sleep(timeSleep)	
                set_PWM.setAllPWN(blue, red, green)

    def smooth(self):
        # is similar to fade but of all colors, but with a offset
        step = 1
        maximum = 255
        blue = 0
        red = maximum
        green = 0
        # start at red
        set_PWM.setAllPWN(blue, red, green)

        var = 1
	timeSleep = 0.01
        while var == 1:
	    blue = self.checkMaximum(blue)
	    red = self.checkMaximum(red)
	    green = self.checkMaximum(green)
	
            blue = self.checkMinimum(blue)
	    green = self.checkMinimum(green)
            red = self.checkMinimum(red)

	    time.sleep(timeSleep)
	    print 'Loop'
		
            # red decreases as green increase
            while red != 0 and green <= maximum:
                red = red - step
                green = green + step
		red = self.checkMaximum(red)
		green = self.checkMinimum(green)
                set_PWM.setAllPWN(blue, red, green)
		time.sleep(timeSleep)

            #green decrease as blue increases
            while green != 0 and blue < maximum:
                green = green - step
                blue = blue + step
		green = self.checkMinimum(green)
		blue = self.checkMaximum(blue)
                set_PWM.setAllPWN(blue, red, green)
		time.sleep(timeSleep)

            # bring red and green back to max = white
            while green < maximum and red < maximum:
                red = red + step
                green = green + step
		red = self.checkMaximum(red)
		green = self.checkMaximum(green)
                set_PWM.setAllPWN(blue, red, green)
		time.sleep(timeSleep)

            #decrease blue
            while blue != 0:
                blue = blue - step
		blue = self.checkMinimum(blue)
                set_PWM.setAllPWN(blue, red, green)
		time.sleep(timeSleep)

            #increase blue as decrease red
            while red != 0  and blue < maximum:
                red = red - step
                blue = blue + step
		blue = self.checkMaximum(blue)
		red = self.checkMinimum(red)
                set_PWM.setAllPWN(blue, red, green)
		time.sleep(timeSleep)

            #inccrease red as decrease green
            while green != 0  and red < maximum:
                red = red + step
                green = green - step
		red = self.checkMaximum(red)
		green = self.checkMinimum(green)
                set_PWM.setAllPWN(blue, red, green)
		time.sleep(timeSleep)

            #come back to white, so increase green
            while green < maximum:
                green = green + step
		green = self.checkMaximum(blue)
                set_PWM.setAllPWN(blue, red, green)
		time.sleep(timeSleep)

            # decrease blue and green, back to start for red
            while green != 0 and blue != 0:
                green = green - step
                blue = blue - step
		green = self.checkMinimum(green)
		blue = self.checkMinimum(blue)
                set_PWM.setAllPWN(blue, red, green)
		time.sleep(timeSleep)

    def checkMaximum(self, value):
	maximum = 255
	if(value > maximum):
	   return maximum
	else:
	   return value	

    def checkMinimum(self, value):
	minimum = 0
	if(value < minimum):
	   return minimum
	else:
	   return value
