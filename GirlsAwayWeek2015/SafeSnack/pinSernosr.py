from arduino import *
import time

my_arduino = Arduino("dev/ttyUSB0")

bluePin = 9

my_arduino.enterConfigMode()

my_arduino.pinMode(bluePin, OUTPUT)

my_arduino.pinMode(6, OUTPUT)
my_arduino.pinMode(5, INPUT)
my_arduino.exitConfigMode()

while True:
	currentTime = time.time()
	my_arduino.digitalWrite(6, HIGH)
	my_arduino.digitalWrite(6, LOW)
	
	while(my_arduino.digitalRead(5) == LOW and time.time()-currentTime < .01):
		pass
	newTime = time.time()
	
	value = newTime-currentTime
	
	value = (value - .01) * 10000
	print value
	
	mappedvalue = map(value, -10, 50, 0, 255)
	
	print mappedvalue
	
	my_arduino.analogWrite( bluePin, mappedValue )
	
	my_arduino.delay(0.100)
