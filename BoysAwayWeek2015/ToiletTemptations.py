

from arduinoClass import *

#variables

ard = Arduino()
bluePin = 9
enablePin = 10
redPin = 11
btnPin = 2
potentPin = 0
buzzerPin = 12
pingPin = 5
servoPin = 8
sitting = False
counter = 0
sittingCounter = 0
count = 0
nearCount = 0
seatCount = 0

#setup

ard.open("/dev/ttyUSB0")
ard.enterConfigMode()
ard.pinMode( enablePin, OUTPUT )
ard.pinMode( buzzerPin, OUTPUT )
ard.pinMode( btnPin, INPUT )
ard.pinMode( potentPin, INPUT )
ard.pinMode( pingPin, INPUT )
ard.attachStepper(9,8)

ard.exitConfigMode()
#ard.digitalWrite(10, HIGH)
ard.configurePWMBoards(1)

# actions

#Ride of the Valkyries

def playOpeningAnthem():
	ard.tone(12, NOTE_D5, 375)
	ard.tone(12, NOTE_D5, 125)
	ard.tone(12, NOTE_F5, 500)
	ard.tone(12, NOTE_D5, 500)
	ard.tone(12, NOTE_F5, 375)
	ard.tone(12, NOTE_F5, 125)
	ard.tone(12, NOTE_A5, 500)
	ard.tone(12, NOTE_F5, 500)
	ard.tone(12, NOTE_A5, 375)
	ard.tone(12, NOTE_A5, 125)
	ard.tone(12, NOTE_C6, 500)
	ard.tone(12, NOTE_C5, 500)
	ard.tone(12, NOTE_F5, 375)
	ard.tone(12, NOTE_F5, 125)
	ard.tone(12, NOTE_A5, 1000)


#Superstition
	
def playSuperstition():
	ard.tone(12, NOTE_DS4, 250)
	ard.tone(12, NOTE_DS5, 250)
	ard.tone(12, NOTE_CS5, 250)
	ard.tone(12, NOTE_DS5, 250)
	ard.tone(12, NOTE_FS5, 375)
	ard.tone(12, NOTE_DS5, 125)
	ard.tone(12, NOTE_CS5, 250)
	ard.tone(12, NOTE_DS5, 250)
	ard.tone(12, NOTE_DS4, 250)
	ard.tone(12, NOTE_DS5, 250)
	ard.tone(12, NOTE_CS5, 250)
	ard.tone(12, NOTE_DS5, 250)
	ard.tone(12, NOTE_FS5, 375)
	ard.tone(12, NOTE_DS5, 375)
	ard.tone(12, NOTE_AS4, 125)
	ard.tone(12, NOTE_CS5, 125)
	ard.tone(12, NOTE_DS5, 125)



#ard.digitalWrite(enablePin, LOW)

#flush will rotate the servo 180 degrees back and forth to simulate a flush mechanism
def flush():
	ard.servoWrite(servoPin, 180)	
	ard.delay(1)
	ard.servoWrite(servoPin, 0)
	ard.delay(1)
	ard.servoWrite(servoPin,180)

#An infinite for loop analyzes button position and alternates between songs each time the button is released. Also waits for pings to register as somebody sitting for 300 iterations before a flush is allowed. Will wait 100 iterations after stand up to flush.

while True:

	# READ PING
	pingVal = ard.getPing(pingPin)
	if(pingVal <= 10):
		seatCount += 1
	if(pingVal <= 10 and nearCount < 1 and (seatCount % 100 == 0)):
		ard.digitalWrite(10, LOW)
		time.sleep(0.1)
		ard.runStepper(-120)
		ard.digitalWrite(10, HIGH)
		nearCount += 1
	if(pingVal <= 5):
		sitting = True
		sittingCounter += 1
	if(pingVal > 5 and sitting == True and sittingCounter > 300):
		counter += 1
		if(counter % 100 == 0):
			flush()
			sittingCounter = 0	
			sitting = False
	if(pingVal > 10):
		seatCount += 1
	if(pingVal > 10 and nearCount >= 1 and (seatCount % 100 == 0)):
		ard.digitalWrite(10, LOW)
		time.sleep(0.1)
		ard.runStepper(120)
		ard.digitalWrite(10, HIGH)
		nearCount -= 1	

	
	#Play music when button is released
	buttonPressed = ard.digitalRead(btnPin)
	
	if(buttonPressed == LOW and (count % 2 == 0)):
		playOpeningAnthem()
		#print "Play opening anthem"
		#ard.delay(3)
		#print "[song ends]"
		buttonPressed = ard.digitalRead(btnPin)
		if(buttonPressed == HIGH):
			count += 1
	elif(buttonPressed == LOW and (count % 2 != 0)):
		playSuperstition()
		#print "Play superstition"
		#ard.delay(3)
		#print "[song ends]"
		buttonPressed = ard.digitalRead(btnPin)
		if(buttonPressed == HIGH):
			count += 1
			
			
			
		
			
		ard.delay(0.05)	
			




		
	
	
	

			
			
			



