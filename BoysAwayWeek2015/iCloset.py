from arduinoClass import *

ard = Arduino()
port ="/dev/ttyUSB0"
ard2 = Arduino()
port2 = "/dev/ttyUSB1"
bumpPin1 = 2
bumpPin2 = 3
bumpPin3 = 4
greenPin = 6
redPin = 7
bluePin = 8
yellowPin = 9
redo = 1


# setup

def setupArd2():

	ard2.open(port2)

	ard2.enterConfigMode()
	ard2.pinMode(bumpPin1, INPUT)
	ard2.pinMode(bumpPin2, INPUT)
	ard2.pinMode(bumpPin3, INPUT)
	ard2.pinMode(greenPin, OUTPUT)
	ard2.pinMode(redPin,OUTPUT)
	ard2.pinMode(bluePin, OUTPUT)
	ard2.pinMode(yellowPin,OUTPUT)
	
	print "PWM Configured"
	ard2.exitConfigMode()
	ard2.configurePWMBoards(1)
	
def runTillBump(bumpPin):
	value = 0
	while value == 0:
		read = ard2.digitalRead(bumpPin) 
		print "read is: " + str(read)
		if read == HIGH:
			print str(bumpPin) + " " + str(read)  
			ard2.setTalon(1,200)
		else:
			print "Read Low"
			ard2.setTalon(1,0)
        	value = value + 1

def runTillBump2(bumpPin):
	value = 0
	while value == 0:
		read = ard2.digitalRead(bumpPin)
		print "read is: " + str(read)
		if read == HIGH:
			print str(bumpPin) + " " + str(read)
			ard2.setTalon(1,200)
		else:
			print "Read Low"
			ard2.setTalon(1,100)
			value = value + 1

def resetLights():
	ard2.digitalWrite(greenPin, LOW)
	ard2.digitalWrite(bluePin, LOW)
	ard2.digitalWrite(redPin, LOW)
	ard2.digitalWrite(yellowPin, LOW)

def motorAndLight (articleColor, articleType, bumpPin, lightPin):
	ard.writeToScreen(2, "...")
	ard.writeToScreen(0, articleColor + " " + articleType)
	ard.close()
	
	setupArd2()
	resetLights()
	ard2.delay(1)
	runTillBump2(bumpPin)
	
	
	
	print str(lightPin) + " On!"
	ard2.digitalWrite(lightPin, HIGH)
	
	ard2.close()
	time.sleep(1)
	ard.open(port)
	ard.writeToScreen(2,"...")
	ard.writeToScreen(0,"DONE")
	ard.writeToScreen(1, "1 = run again.")
	if int(ard.readFromKeypad()) == 1:
		print "Redo is 1"
		redo = 1
	else:
		print "Redo is 0"
		redo = 0
	ard.close()
	time.sleep(1)
	
	ard2.open(port2)
	print str(lightPin) + " Off!"
	ard2.digitalWrite(lightPin, LOW)
	ard2.close()
	
	ard.open(port)
			
ard.open(port)
while redo == 1:
	
	ard.writeToScreen(2,"...")
	ard.writeToScreen(0, "Press any ")
	ard.writeToScreen(1, "number to start")
	begin = int(ard.readFromKeypad())
	#begin = int(raw_input("Any num to start."))

	if begin in range(0,100000):
		ard.writeToScreen(2, "...")
		ard.writeToScreen(0, "1=Shirt  2=Pants") 
		ard.writeToScreen(1, "3=Ties")
		choice = int(ard.readFromKeypad())

		if choice == 1:
			ard.writeToScreen(2, "...")
			ard.writeToScreen(0, "Shirts")
			ard.delay(.5)
			ard.writeToScreen(2,"...")
			ard.writeToScreen(0, "1=Green 2=Yellow")
			ard.writeToScreen(1, "3=Red 4=Blue")
			shirt = int(ard.readFromKeypad())
			#shirt = int(raw_input("Enter 1 to pick dress clothes or 2 to pick football uniform."))


			if shirt == 1:
				motorAndLight("Green", "Shirt", bumpPin1, greenPin)
			

			elif shirt == 2:
				motorAndLight("Yellow", "Shirt", bumpPin1, yellowPin)


			elif shirt == 3:
				motorAndLight("Red", "Shirt", bumpPin1, redPin)


			elif shirt == 4:
				motorAndLight ("Blue", "Shirt", bumpPin1, bluePin)


			else: 
				ard.writeToScreen(2, "...")
				ard.writeToScreen(0, "Invalid input. Please try again.")
				ard.delay(1)


		elif choice == 2:
			ard.writeToScreen(2, "...")
			ard.writeToScreen(0, "Pants")
			ard.delay(.5)
			ard.writeToScreen(0, "1=Green 2=Yellow")
			ard.writeToScreen(1, "3=Red 4=Blue")
			pants = int(ard.readFromKeypad())
			#outfit = int(raw_input("Enter 1 to pick dress clothes or 2 to pick football uniform."))
			if pants == 1:
				motorAndLight("Green", "Pants", bumpPin2, greenPin)
			elif pants == 2:
				motorAndLight("Yellow", "Pants", bumpPin2, yellowPin)
			elif pants == 3:
				motorAndLight("Red", "Pants", bumpPin2,redPin)
			elif pants == 4:
				motorAndLight("Blue", "Pants", bumpPin2, bluePin)
			else: 
				ard.writeToScreen(2, "...")
				ard.writeToScreen(0, "Invalid")
				ard.delay(1)

		elif choice == 3:
			ard.writeToScreen(2, "...")
			ard.writeToScreen(0, "Ties")
			ard.delay(.5)
			ard.writeToScreen(0, "1=Green 2=Yellow")
			ard.writeToScreen(1, "3=Red 4=Blue")
			formal = int(ard.readFromKeypad())
			if formal == 1:
				motorAndLight("Green", "Tie", bumpPin3, greenPin)
			elif formal == 2:
				motorAndLight("Yellow","Tie",bumpPin3,yellowPin)
			elif formal == 3:
				motorAndLight("Red","Tie",bumpPin3,redPin)
			elif formal == 4:
				motorAndLight("Blue","Tie",bumpPin3,bluePin)
			else:
				ard.writeToScreen(0, "Invalid")
				ard.delay(1)

		else:
			ard.writeToScreen(2, "...")
			ard.writeToScreen(0, "Invalid")
			ard.delay(1)
