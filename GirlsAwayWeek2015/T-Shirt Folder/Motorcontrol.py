from arduino import *

# variables
my_arduino = Arduino("/dev/ttyUSB0")


button = 2


# setup

my_arduino.configurePWMBoards(1)


print "hello"


my_arduino.enterConfigMode()

my_arduino.pinMode(button, INPUT_PULLUP)


my_arduino.exitConfigMode()

# actions
btnvalue = True
reverse = 1.5
while btnvalue == True:
	my_arduino.setTalon(0,-100)
	btnvalue = my_arduino.digitalRead(button)
	my_arduino.delay(.005)
	
my_arduino.setTalon(0,0)

btnvalue = True


#reverse
my_arduino.setTalon(0,100)

my_arduino.delay(reverse)
 
my_arduino.setTalon(0,0)
#


while btnvalue == True:
	my_arduino.setTalon(1,105)
	btnvalue = my_arduino.digitalRead(button)
	my_arduino.delay(.005)
	
my_arduino.setTalon(1,0)

btnvalue = True


#reverse
my_arduino.setTalon(1,-85)

my_arduino.delay(reverse)

my_arduino.setTalon(1,0)
#


while btnvalue == True:
	my_arduino.setTalon(2,105)
	btnvalue = my_arduino.digitalRead(button)
	my_arduino.delay(.005)
	
my_arduino.setTalon(2,0)


#reverse
my_arduino.setTalon(2,-75)

my_arduino.delay(reverse)

my_arduino.setTalon(2,0)
#
	

