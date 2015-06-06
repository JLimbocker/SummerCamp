from arduino import *




my_ard = Arduino("/dev/ttyUSB1")

servo1 = 0
servo2 = 8


my_ard.configurePWMBoards(1)


my_ard.servoWrite(servo1, 0)
my_ard.delay(1)

my_ard.servoWrite(servo1, 90)
my_ard.delay(1)

my_ard.servoWrite(servo1, 0)
my_ard.delay(1)

my_ard.servoWrite(servo2, 0)
my_ard.delay(1)

my_ard.servoWrite(servo2, 90)
my_ard.delay(1)

my_ard.servoWrite(servo2, 0)
my_ard.delay(1)
