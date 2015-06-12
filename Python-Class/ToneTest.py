

from arduinoClass import *





buzzerPin = 12
arduino = Arduino("/dev/tty.usbserial-A5027IWF")

# setup
arduino.enterConfigMode()

arduino.pinMode(buzzerPin,OUTPUT)

arduino.exitConfigMode()


# loop

""" 

HOT CROSS BUNS

notes = [NOTE_A4, NOTE_G4, NOTE_F4, 0, NOTE_A4, NOTE_G4, NOTE_F4, 0, NOTE_F4, NOTE_F4, NOTE_F4, NOTE_F4, NOTE_G4, NOTE_G4, NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_F4, 0]

noteTypes = [4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4]
"""


notes = [NOTE_F5, NOTE_F5, NOTE_C5, NOTE_D5, NOTE_D5, 
		NOTE_C5, NOTE_D5, NOTE_D5, NOTE_D5, NOTE_C5, 
		NOTE_D5, NOTE_D5, NOTE_F5, NOTE_F5, NOTE_C5, 
		NOTE_C5, NOTE_D5, NOTE_D5, NOTE_C5, NOTE_D5, 
		NOTE_D5, NOTE_C5, NOTE_A4, NOTE_A4, NOTE_A4,
		NOTE_C5, NOTE_C5, 0, NOTE_C5, NOTE_C5, 
		0, NOTE_C5, NOTE_C5, NOTE_C5, NOTE_C5,
		NOTE_C5, NOTE_C5, NOTE_D5, NOTE_D5, 0,
		NOTE_D5, NOTE_F5, NOTE_F5, NOTE_C5, NOTE_D5,
		NOTE_D5, NOTE_D5, NOTE_C5, NOTE_C5, NOTE_C5, 
		NOTE_C5, NOTE_C5, NOTE_A4, NOTE_A4, NOTE_A4,
		NOTE_A4]
		
noteTypes = [16/3, 16/3, 8, 16/3, 16/3,
			8, 16/3, 8, 16, 8,
			16/3, 16/5, 16/3, 8, 16,
			8, 16/3, 16/3, 8, 16/3, 
			16/3, 8, 8, 16, 16/5,
			16/3, 16, 4, 16/3, 16, 
			4, 16, 16, 16, 8,
			16, 8, 16, 16/3, 8,
			8, 16/3, 16/3, 8, 8,
			16, 16/3, 16, 16, 8,
			16, 8, 16, 8, 16, 
			16/3]
for note, t in zip(notes, noteTypes):
	arduino.tone(buzzerPin, note, 1500/t)

	





