from arduinoClass import *

my_arduino = Arduino("/dev/tty.usbserial-A5027IVX")

my_arduino.configurePWMBoards(0)

my_arduino.enterConfigMode()
my_arduino.pinMode(9, 2)
my_arduino.exitConfigMode()

while True:
    btnVal = my_arduino.digitalRead(9)
    print btnVal
    if btnVal == 0:
		my_arduino.setTalon(0, -500)
    else:
        my_arduino.setTalon(0, 0)

	my_arduino.delay(0.01)
