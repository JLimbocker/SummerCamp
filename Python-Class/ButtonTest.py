# This program is to test the button functionality of Arduino in Python

from arduinoClass import *



my_arduino = Arduino("/dev/ttyUSB2")
btnPin = 2

redPin = 11
bluePin = 9
greenPin = 10

# setup

my_arduino.enterConfigMode()

my_arduino.pinMode(btnPin,1)
my_arduino.pinMode(redPin,0)

my_arduino.exitConfigMode()

# loop

while True:
	btnVal = my_arduino.digitalRead(btnPin)
	
	
	if int(btnVal) == 1:
		my_arduino.digitalWrite(redPin, 0)
	else:
		my_arduino.digitalWrite(redPin, 1)
	
	my_arduino.delay(0.01)
	
