from arduino import *


# variables

my_arduino = Arduino("/dev/ttyUSBO")

bluePin = 9


# setup 

my_arduino.enterConfigMode()


my_arduino.pinMode(bluePin, OUTPUT) 


my_arduino.exitConfigMode()




# actions

my_arduino.digitalWrite(bluePin,HIGH) 
