from arduino import *


# variables

my_arduino = Arduino("/dev/ttyUSB0")

bluePin = 9
greenPin = 10
redPin = 11
buzzerPin = 12 

btnPin = 2
potentPin = 0


# setup 

my_arduino.enterConfigMode()


my_arduino.pinMode(bluePin, OUTPUT) 
my_arduino.pinMode(greenPin, OUTPUT) 
my_arduino.pinMode(redPin, OUTPUT)
my_arduino.pinMode(buzzerPin, OUTPUT)

my_arduino.pinMode(btnPin, INPUT) 
my_arduino.pinMode(potentPin, INPUT)


my_arduino.exitConfigMode()




# actions

	
my_arduino.tone(buzzerPin,NOTE_A4, 1000)
