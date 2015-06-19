from arduinoClass import *


my_util = PyUtil()
my_util.initializeBluetooth()

my_ard = Arduino()
my_ard.open("/dev/cu.usbserial-A5027JHH")

my_ard.enterConfigMode()
my_ard.pinMode(9, OUTPUT)
my_ard.exitConfigMode()

my_ard.digitalWrite(9, LOW)

my_ard.configurePWMBoards(0)

def fire():
    my_ard.servoWriteMicroseconds(0, 1800)
    my_ard.delay(.5)
    my_ard.servoWriteMicroseconds(0, 1250)

#range is from 1010 to 1890 in the theta
#range is from 1400 to 1600 in the vertical
#range is from 1250 to 1800 in the trigger

my_ard.servoWriteMicroseconds(0, 1250)

p_theta = 1450
p_vertical = 1500
p_trig = 0
p_arm = 0

arm_state = False

while True:
    leftY = my_util.getAxisValue(1)
    rightY = my_util.getAxisValue(3)
    leftX = my_util.getAxisValue(0)
    rightX = my_util.getAxisValue(2)

    theta = map( int(rightX*1000), -1000, 999, 1010, 1890 )
    vertical = map( int(rightY*1000), -1000, 999, 1400, 1600 )
    arm = my_util.getButtonValue(8)
    trig = my_util.getButtonValue(9)

    if theta != p_theta:
        my_ard.servoWriteMicroseconds(1, theta)

    if vertical != p_vertical:
        my_ard.servoWriteMicroseconds(2, vertical)

    if p_trig != trig and trig = 1:
        fire()

    if p_arm != arm and arm = 1:
        arm_state = !arm_state

    my_ard.digitalWrite(9, arm_state)
