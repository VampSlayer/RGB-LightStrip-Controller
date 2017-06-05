MAXIMUM=255
MINIMUM=0

class brightnessCheck(object):

    def checkMaximum(self, value):
	if(value > MAXIMUM):
	    return MAXIMUM
	else:
            return value	

    def checkMinimum(self, value):
	if(value < MINIMUM):
	    return MINIMUM
	else:
            return value
