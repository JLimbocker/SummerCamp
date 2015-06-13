from arduinoClass import *

my_arduino = Arduino("/dev/tty.usbserial-A5027IWF")


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

while True:

	val = my_arduino.analogRead(potentiometerPin)

	my_arduino.analogWrite( redPin, val/4 )

	my_arduino.delay(0.05)


"""
Testing Results!

	Works
		LED digital
		digital read
		tone
		analog read
		analog write
		digital write



	Does Not Work

"""