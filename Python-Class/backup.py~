#get weather from internet
import pywapi
import pprint
import datetime
from arduinoClass import *


arduino = Arduino("/dev/ttyUSB0")
arduino.configurePWMBoards(0)

def moveToHot():
	arduino.setTalon(0,100)
	while(arduino.digitalRead(6) != LOW):
		pass
	arduino.setTalon(0,0)
	
def moveToCold():
	arduino.setTalon(0,100)
	while(arduino.digitalRead(7) != LOW):
		pass
	arduino.setTalon(0,0)

def moveToRainy():
	arduino.setTalon(0,100)
	while(arduino.digitalRead(8) != LOW):
		pass
	arduino.setTalon(0,0)

switchPin = 10
buzzerPin = 13


arduino.enterConfigMode()

arduino.pinMode(buzzerPin,OUTPUT)
arduino.pinMode(6, INPUT_PULLUP)
arduino.pinMode(7, INPUT_PULLUP)
arduino.pinMode(8, INPUT_PULLUP)
arduino.exitConfigMode()

#prints current time
currentHour = datetime.datetime.now().hour
currentMinute = datetime.datetime.now().minute
currentTime = str(currentHour) + ":" + str(currentMinute)
print currentTime


 #switch 
while True:
	#set alarm
	arduino.writeToScreen(0, "Set Alarm?")
	askTime = raw_input("Set Alarm?")
	if askTime == "+":
		arduino.writeToScreen(0, "Hour?")
		askHour = raw_input("Hour?")
		arduino.writeToScreen(0, "Minute?")
		askMinute = raw_input("Minute?")
		arduino.delay(1)
		setTime = str(askHour) + ":" + str(askMinute)
		arduino.writeToScreen(0, "Alarm is set to" +" "+ setTime)
		arduino.delay(2)
	else: 
		arduino.writeToScreen(0, "Rotate clothes?")
		askRotation = raw_input("Rotate clothes?")
		if askRotation == "yes":
			arduino.writeToScreen(0, "Which Section?")
			askSection = raw_input("Which Section?")
				if askSection == "hot" or if askSection == "h":
					moveToHot() 
				elif askSection == "cold" or if askSection == "c":
					moveToCold()
				else:
					moveToRainy()						
	
	currentHour = datetime.datetime.now().hour
	currentMinute = datetime.datetime.now().minute
	currentTime = str(currentHour) + ":" + str(currentMinute)
	while currentTime != setTime:
		currentHour = datetime.datetime.now().hour
		currentMinute = datetime.datetime.now().minute
		currentTime = str(currentHour) + ":" + str(currentMinute)
		arduino.delay(.5)
		arduino.writeToScreen(0, "It is now" + " " + currentTime)	



	pp = pprint.PrettyPrinter(indent=4)
	weather_com_result = pywapi.get_weather_from_weather_com('40201')
	chance_precip = weather_com_result['forecasts'][0]['day']['chance_precip']
	text = weather_com_result['current_conditions']['text']
	temp= weather_com_result['current_conditions']['temperature']
	chance_precip = int(chance_precip)
	temp = int(temp)
	arduino.writeToScreen(0, "It is" + " " + text)
	arduino.delay(2) 
	arduino.writeToScreen(0, str(chance_precip) + " " + " percent chance of rain")
	arduino.delay(2)
	arduino.writeToScreen(0, str(temp) + "C")
	arduino.delay(2)
	if chance_precip >= 35: #Rain
		arduino.writeToScreen(0, "Rainy")
		moveToRainy()
		thirdnotes = [NOTE_E4, NOTE_E5, NOTE_CS5, NOTE_B4, NOTE_A4, NOTE_FS4, 
					NOTE_E4, NOTE_A4, NOTE_A4, NOTE_B4, NOTE_CS5, NOTE_E5,
					NOTE_E4, NOTE_FS4, NOTE_A4, NOTE_B4, NOTE_CS5, NOTE_E5, NOTE_CS5,
					NOTE_E5, NOTE_E5, NOTE_CS5, NOTE_B4, NOTE_FS4]
		thirdnoteTypes = [4, 8/5, 8, 8, 8, 3/2, 
						4, 8/5, 8, 8, 8, 3/2,
						8, 8, 8/5, 8, 4, 2, 4,
						4, 8/5, 8, 4, 2]
		for thirdnote, t in zip(thirdnotes, thirdnoteTypes):
			arduino.tone(buzzerPin, thirdnote, 1000/t)
			

	elif temp >= 22: #Hot Weather
		arduino.writeToScreen(0, "Hot")
		moveToHot()
		notes = [0, NOTE_CS4, NOTE_B3, NOTE_CS4, NOTE_A3, NOTE_CS4, NOTE_A3, NOTE_B3, NOTE_CS4, 
				0, NOTE_CS4, NOTE_B3, NOTE_CS4, NOTE_A3, NOTE_A3, NOTE_B3, NOTE_A3,
				0, NOTE_CS4, NOTE_B3, NOTE_A3, 
				NOTE_E3, NOTE_FS3, NOTE_A3, NOTE_B3, NOTE_E3, NOTE_A3, NOTE_B3, NOTE_D3, NOTE_A3,
				NOTE_B3, NOTE_E3, NOTE_A3, NOTE_B3, NOTE_A3, NOTE_GS3, NOTE_FS3, NOTE_E3]
		noteTypes = [4, 8, 4, 4, 8/3, 8, 8, 8, 8/3,
					4, 8, 4, 4, 2, 8, 4, 4, 
					16, 4, 4, 4,
					8, 8, 8, 8, 8, 8, 8, 8, 8,
					8, 8, 8, 8, 8, 8, 8, 8]	
		for note, t in zip(notes, noteTypes):
			arduino.tone(buzzerPin, note*2, 1500/t)
			

	else:  #Cold Weather
		arduino.writeToScreen(0, "Cold")
		moveToCold()
		secnotes = [NOTE_D4, NOTE_D4, NOTE_D5, NOTE_D5, NOTE_C5, NOTE_B4, NOTE_A4, NOTE_G4, NOTE_D4,
					NOTE_D4, NOTE_D4, NOTE_A4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_FS4, NOTE_D4,
					NOTE_E4, NOTE_E5, NOTE_E5, NOTE_D5, NOTE_C5, NOTE_B4, NOTE_A4, 
					NOTE_FS5, NOTE_E5, NOTE_D5, NOTE_D5, NOTE_C5, NOTE_B4, NOTE_B4, NOTE_A4, NOTE_G4]
		secnoteTypes = [8, 8, 8, 8, 4, 4, 4, 4, 2,
						8, 8, 8/3, 8, 8/3, 8, 4, 2,
						4, 8, 8, 4, 4, 4, 3/2,
						8, 8, 4, 8, 8, 4, 8, 8, 3/2]	
		for secnote, t in zip(secnotes, secnoteTypes):
			arduino.tone(buzzerPin, secnote, 1500/t)
			


