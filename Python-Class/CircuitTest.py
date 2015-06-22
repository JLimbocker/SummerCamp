# Test the circuits including
  # RGB LED
  # Buzzer
  # Button
  # Potentiometer

from arduinoClass import *

my_arduino = Arduino()
ard = Arduino()


redPin = 13

my_arduino.open("/dev/cu.usbserial-A5027IY6");

# setup
my_arduino.enterConfigMode()
my_arduino.pinMode(redPin,OUTPUT)
my_arduino.exitConfigMode()
my_arduino.close()

# ard.open("/dev/cu.usbserial-A5027JH5")
# ard.enterConfigMode()
# ard.pinMode(redPin,OUTPUT)
# ard.exitConfigMode()
# ard.close()





while True:
	my_arduino.open("/dev/cu.usbserial-A5027IY6")
	my_arduino.digitalWrite(redPin, HIGH)
	my_arduino.delay(0.25)
	my_arduino.digitalWrite(redPin, LOW)
	my_arduino.delay(0.25)
	my_arduino.close()

	# ard.open("/dev/cu.usbserial-A5027JH5")
	# ard.digitalWrite(redPin, HIGH);
	# ard.delay(0.25);
	# ard.digitalWrite(redPin, LOW);
	# ard.delay(0.25);
	# ard.close();
