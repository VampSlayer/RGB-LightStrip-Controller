import pigpio

pi = pigpio.pi()

BLUE_PIN  = 24
RED_PIN = 17
GREEN_PIN  = 23
LED_MAXIMUM = 255
LED_MINIMUM = 0

pi.set_mode(BLUE_PIN, pigpio.OUTPUT)
pi.set_mode(RED_PIN, pigpio.OUTPUT)
pi.set_mode(GREEN_PIN, pigpio.OUTPUT)

class setPWN(object):

    def setAllPWN(self, blue, red, green):
        if (blue >= LED_MINIMUM  and blue <= LED_MAXIMUM):
	    pi.set_PWM_dutycycle(BLUE_PIN, blue)
	else:
	    print 'ERROR: You entered for blue : [{0}]'.format(blue)
            print 'ERROR: Please enter integer number >=0 and <=255'

	if(red >= LED_MINIMUM  and red <= LED_MAXIMUM):
	    pi.set_PWM_dutycycle(RED_PIN, red)
 	else:
	    print 'ERROR: You entered for red : [{0}]'.format(red)
            print 'ERROR: Please enter integer number >=0 and <=255'

	if(green >= LED_MINIMUM  and green <= LED_MAXIMUM):
	    pi.set_PWM_dutycycle(GREEN_PIN, green)
        else:
	    print 'ERROR: You entered for green : [{0}]'.format(green)
            print 'ERROR: Please enter integer number >=0 and <=255'

class getPWN(object):

    def getBluePWN(self):
        return pi.get_PWM_dutycycle(BLUE_PIN)

    def getRedPWN(self):
        return pi.get_PWM_dutycycle(RED_PIN)

    def getGreenPWN(self):
        return pi.get_PWM_dutycycle(GREEN_PIN)

    def printRGB(self):
	print 'INFO: Brightness changed to RED : [{0}] GREEN : [{1}] BLUE : [{2}]'.format(self.getRedPWN(), self.getGreenPWN(), self.getBluePWN())
