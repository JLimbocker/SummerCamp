from arduino import *




my_ard = Arduino()
my_ard.open("/dev/ttyUSB1")


my_ard.writeToScreen(0,"SafeSnack is")

my_ard.writeToScreen(1,"great")

my_ard.delay(2)
my_ard.writeToScreen(2,"HI")
my_ard.writeToScreen(0,":)")


