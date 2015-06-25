from arduinoClass import *

my_arduino = Arduino()
my_arduino.open("/dev/cu.wchusbserial1420")

while True:
    entry = my_arduino.readFromKeypad()
    if entry == "c":
        my_arduino.writeToScreen(2, entry)
    else:
        my_arduino.writeToScreen(0, entry)
    print entry
