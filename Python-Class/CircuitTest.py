# Test the circuits including
  # RGB LED
  # Buzzer
  # Button
  # Potentiometer

from arduinoClass import *

my_arduino = Arduino("/dev/tty.usbserial-A5027J5I")

potentiometerPin = 0
buttonPin = 2

redPin = 11
greenPin = 10
bluePin = 9

buzzerPin = 12

# setup
my_arduino.enterConfigMode()

my_arduino.pinMode(buttonPin,INPUT)
my_arduino.pinMode(potentiometerPin,INPUT)

my_arduino.pinMode(redPin,OUTPUT)
my_arduino.pinMode(greenPin,OUTPUT)
my_arduino.pinMode(bluePin,OUTPUT)
my_arduino.pinMode(buzzerPin,OUTPUT)

my_arduino.exitConfigMode()


color = 0
value = 0

notes = [ NOTE_A3, NOTE_B3, NOTE_CS4, NOTE_D4, NOTE_E4, NOTE_FS4, NOTE_GS4, NOTE_A4 ]

while True:
	print "Button: ", str(my_arduino.digitalRead(buttonPin)), " | Potentiometer: ", str(my_arduino.analogRead(potentiometerPin)),
	print " | Value: ", str(value)

	if color == 0:
		my_arduino.analogWrite(redPin,value)

		value = value + 10
		if value >= 255:
			color = 1
			value = 0
			my_arduino.analogWrite(redPin,value)
	elif color == 1:
		my_arduino.analogWrite(greenPin,value)

		value = value + 10
		if value >= 255:
			color = 2
			value = 0
			my_arduino.analogWrite(greenPin,value)
	elif color == 2:
		my_arduino.analogWrite(bluePin,value)

		value = value + 10
		if value >= 255:
			color = 3
			value = 0
			my_arduino.analogWrite(bluePin,value)
	else:
		my_arduino.tone( buzzerPin, notes[value]*2, 1000/4)

		value = value+1
		if value >= 8:
			color = 0
			value = 0

	

	my_arduino.delay(0.001)




