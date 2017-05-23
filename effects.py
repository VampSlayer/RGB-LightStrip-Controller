import getsetPWM

set_PWM = getsetPWM.setPWN()
get_PWM = getsetPWM.getPWM()

class effects(object):

    def flashcolors(self):
        #flash between colors
        var = 1
        while var == 1      # This constructs an infinite loop
            set_PWM.setAllPWN(255, 0, 0) #blue

            set_PWM.setAllPWN(255, 255, 0) #purple

            set_PWM.setAllPWN(0, 255, 0) #red

            set_PWM.setAllPWN(0, 255, 255) #red+green

            set_PWM.setAllPWN(0, 0, 255) #green

            set_PWM.setAllPWN(255, 255, 255) #white

            set_PWM.setAllPWN(255, 0, 255) #blue+green

    def strobe(self):
        # goes from previous setting to min then to previous setting
        blue = get_PWM.getBluePWN
        red = get_PWM.getRedPWN
        green = get_PWM.getGreenPWN

        # read color. then switch that color to 0 then back to max
        var = 1
        while var == 1:
            set_PWM.setAllPWN(0, 0, 0)

            set_PWM.setAllPWN(blue, red, green)

    def fade(self):
        # goes incrementally from  white max to min then to max etc.
        step = 1
        maximum = 255
        blue = maximum
        red = maximum
        green = maximum
        set_PWM.setAllPWN(blue, red, green)

        var = 1
        while var == 1:
            while blue != 0 && blue <= maximum:
                blue = blue - step
                red = red - step
                green = green - step
                set_PWM.setAllPWN(blue, red, green)

            while blue >= 0 && blue != maximum:
                blue = blue + step
                red = red + step
                green = green + step
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
        while var == 1:
            # red decreases as green increase
            while red ! = 0 && green <= maximum:
                red = red - step
                green = green + step
                set_PWM.setAllPWN(blue, red, green)

            #green decrease as blue increases
            while green ! = 0 && blue <= maximum:
                green = green - step
                blue = blue + step
                set_PWM.setAllPWN(blue, red, green)

            # bring red and green back to max
            while green <= maximum && red <= maximum:
                red = red + step
                green = green + step
                set_PWM.setAllPWN(blue, red, green)

            #decrease blue
            while blue ! = 0:
                blue = blue - step
                set_PWM.setAllPWN(blue, red, green)

            #increase blue as decrease red
            while red ! = 0  && blue <= maximum:
                red = red - step
                blue = blue + step
                set_PWM.setAllPWN(blue, red, green)

            #inccrease red as decrease green
            while green ! = 0  && red <= maximum:
                red = red + step
                green = green - step
                set_PWM.setAllPWN(blue, red, green)

            #come back to white, so increase green
            while green <= maximum:
                green = green + step
                set_PWM.setAllPWN(blue, red, green)

            # decrease blue and green, back to start for red
            while green ! = 0 && blue ! = 0  && red <= maximum:
                red = red + step
                green = green - step
                blue = blue - step
                set_PWM.setAllPWN(blue, red, green)
