
# from arduinoClass import *


# setup
led_pin = 9
Arduino.pinMode( led_pin, Arduino.OUTPUT )


# loop

while True:
	Arduino.digitalWrite( led_pin, True )
	Arduino.delay( 1000 )
	Arduino.digitalWrite( led_pin, False )
	Arduino.delay( 1000 )