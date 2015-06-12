from arduinoClass import *

my_arduino = Arduino("/dev/tty.usbserial-A5027JHH")

my_arduino.configurePWMBoards(0)

while True:
    my_arduino.servoWrite(15, 0)
    my_arduino.delay(1)
    my_arduino.servoWrite(15, 90)
    my_arduino.delay(1)
