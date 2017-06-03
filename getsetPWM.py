import pigpio

pi = pigpio.pi()

BLUE_PIN  = 24
RED_PIN = 17
GREEN_PIN  = 22

pi.set_mode(BLUE_PIN, pigpio.OUTPUT)
pi.set_mode(RED_PIN, pigpio.OUTPUT)
pi.set_mode(GREEN_PIN, pigpio.OUTPUT)

class setPWN(object):

    def setAllPWN(self, blue, red, green):
        if (blue >=0 
	and red >=0 
	and green >=0
        and blue <=255 
	and red <=255 
	and green <=255):
            pi.set_PWM_dutycycle(BLUE_PIN, blue)
            pi.set_PWM_dutycycle(RED_PIN, red)
            pi.set_PWM_dutycycle(GREEN_PIN, green)
        else:
            print("ERROR: Please enter integer number >=0 && <=255")

class getPWN(object):

    def getBluePWN(self):
        return pi.get_PWM_dutycycle(BLUE_PIN)

    def getRedPWN(self):
        return pi.get_PWM_dutycycle(RED_PIN)

    def getGreenPWN(self):
        return pi.get_PWM_dutycycle(GREEN_PIN)
