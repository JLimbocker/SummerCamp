# This program is to test the button functionality of Arduino in Python

from arduinoClass import *



my_arduino = Arduino("/dev/cu.usbserial-A5027IVX")
btnPin = 9

redPin = 11
bluePin = 9
greenPin = 10

# setup

my_arduino.enterConfigMode()

my_arduino.pinMode(btnPin,INPUT_PULLUP)

my_arduino.exitConfigMode()

prevBtn = False
counter = 0;

# loop

while True:
	btnVal = my_arduino.digitalRead(btnPin)

	if btnVal != prevBtn and btnVal == 0:
		counter = counter + 1
		


	my_arduino.delay(0.01)
