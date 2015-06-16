from arduinoClass import *

my_arduino = Arduino("/dev/tty.usbserial-A5027JS4")

#my_arduino.configurePWMBoards()

while True:
    print my_arduino.getPing(3)
    my_arduino.delay(1)
