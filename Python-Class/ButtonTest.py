# This program is to test the button functionality of Arduino in Python

from arduinoClass import *



my_arduino = Arduino("/dev/cu.usbserial-A5027JS4")
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
	print btnVal

	if btnVal != prevBtn and btnVal == 0:
		counter = counter + 1

	prevBtn = btnVal
	my_arduino.writeToScreen(0, "Count is: ")
	my_arduino.writeToScreen(1, str(counter))

	my_arduino.delay(0.01)
