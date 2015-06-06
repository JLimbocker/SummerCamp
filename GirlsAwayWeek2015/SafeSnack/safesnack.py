# This is a program to run the SafeSnack apparatus


# import statements
from arduino import *





# variables

lockBtnPinTop = 7
lockBtnPinBottom = 6


consoleBtnPin = 8



lockPinTop = 15
lockPinBottom = 8


topDoorOpen = False
bottomDoorOpen = False

my_ard = Arduino()
finger_ard = Arduino()


topInventory = {}
bottomInventory = {}

knownID = {0:3,1:1,2:2,3:3,4:1,5:3}
passwords = {"12":1,"24":2,"76":3,"34":1,"52":2}


aport = "/dev/ttyUSB1"
fport = "/dev/ttyUSB0"


# functions

	
def lockTopDoor(): # this will lock the top door of the pantry
	my_ard.servoWrite(lockPinTop,180)
	
def lockBottomDoor(): # this will lock the bottom door of the pantry
	my_ard.servoWrite(lockPinBottom,0)
	
def unlockTopDoor(): # this will unlock the top door on the SafeSnack depending  on which fingerprint is entered 
	my_ard.servoWrite(lockPinTop,90)
	
def unlockBottomDoor(): # this will unlock the bottom door on the SafeSnack depending  on which fingerprint is entered 
	my_ard.servoWrite(lockPinBottom,90)
	

def displayTopInventory(): # this will display the inventory of the top box on the screen
	for key in topInventory:
		my_ard.writeToScreen(0,str(topInventory[key]) + " " + key + "s") 
		my_ard.delay ( 1 )
		my_ard.writeToScreen(2,"")
	
def displayBottomInventory(): # this will display the inventory of the bottom box on the screen
	for key in bottomInventory:
		my_ard.writeToScreen(0,str(bottomInventory[key]) + " " + key + "s") 
		my_ard.delay ( 1 )
		my_ard.writeToScreen(2,"")
	
def addTopInventory( food ): # this will add a new food item to the top box inventory once it is enetered on the keypad
	if food in topInventory:
		topInventory[food] = topInventory[food] + 1 
	else: 
		topInventory[food] = 1 
	
def subtractTopInventory( food ): # this will add a new food item to the top box inventory once it is enetered on the keypad
	if food in topInventory:
		topInventory[food] = topInventory[food] - 1 
		if topInventory[food] == 0:
			del topInventory[food]
	else: 
		print "not in inventory" 
		
def addBottomInventory( food ): # this will add a new food item to the bottom box inventory once it is enetered on the keypad
	if food in bottomInventory:
		bottomInventory[food] = bottomInventory[food] + 1 
	else: 
		bottomInventory[food] = 1 
		
def subtractBottomInventory( food ): # this will add a new food item to the top box inventory once it is enetered on the keypad
	if food in bottomInventory:
		bottomInventory[food] = bottomInventory[food] - 1 
		if bottomInventory[food] == 0:
			del bottomInventory[food]
	else: 
		print "not in inventory" 
		
def pressedButton(pin):
	if my_ard.digitalRead(pin) == 1: 
		return False
	else: 
		return True










# setup (arduino)
my_ard.open(aport)

my_ard.configurePWMBoards(1)

my_ard.enterConfigMode()

#buttons
my_ard.pinMode(lockBtnPinTop,INPUT)
my_ard.pinMode(lockBtnPinBottom,INPUT)
my_ard.pinMode(consoleBtnPin,INPUT)

my_ard.exitConfigMode()




# loop


addTopInventory("apple") 
	

addTopInventory("banana")
	

addTopInventory("nutri-grain bar")
addTopInventory("nutri-grain bar")
	

addTopInventory("fruit snacks")
addTopInventory("fruit snacks")
	

addTopInventory("peanut butter crackers")
addTopInventory("peanut butter crackers")
addTopInventory("peanut butter crackers")
	







addBottomInventory("pretzel")


addBottomInventory("candy")
addBottomInventory("candy")
addBottomInventory("candy")
addBottomInventory("candy")


addBottomInventory("granola bar")


addBottomInventory("chips")
addBottomInventory("chips")




#displayTopInventory ()


while True:
	my_ard.writeToScreen(0,"Welcome to")
	my_ard.writeToScreen(1,"SafeSnack")
	
	if pressedButton(lockBtnPinTop):
		print "lock top door"
		lockTopDoor()
	if pressedButton(lockBtnPinBottom):
		print "lock bottom door"
		lockBottomDoor()
	if pressedButton(consoleBtnPin):
		my_ard.writeToScreen(2,"")
		my_ard.writeToScreen(0,"Scan finger or")
		my_ard.writeToScreen(1,"edit inventory?")
		fingerOrInventory = raw_input("Scan finger or edit inventory?")

		if fingerOrInventory == "i":
		 	
		 	my_ard.writeToScreen(2,"")
			my_ard.writeToScreen(0,"Top or Bottom?") 
			topOrBottom = raw_input("Top or Bottom?")	

			if topOrBottom == "t":
				my_ard.writeToScreen(2,"")
				my_ard.writeToScreen(0,"Add or subtract?") 
				addOrSubtract = raw_input("Add or subtract?")

				if addOrSubtract == "+" or addOrSubtract == "=" or addOrSubtract == "a":
					my_ard.writeToScreen(2,"")
					my_ard.writeToScreen(0, "what would you")
					my_ard.writeToScreen(1, "like to add?")
					adding = raw_input("What would you like to add?")
					addTopInventory(adding)
				elif addOrSubtract == "-" or addOrSubtract == "s":
					my_ard.writeToScreen(2,"")
					my_ard.writeToScreen(0, "what would you")
					my_ard.writeToScreen(1, "like to subtract?")
					subtracting = raw_input("What would you like to subtract?")
					subtractTopInventory(subtracting)
				displayTopInventory ()
			elif topOrBottom == "b":
				my_ard.writeToScreen(2,"")
				my_ard.writeToScreen(0, "Add or subtract?")
				addOrSubtract = raw_input("Add or subtract?")

				if addOrSubtract == "+" or addOrSubtract == "=" or addOrSubtract == "a":
					my_ard.writeToScreen(2,"")
					my_ard.writeToScreen (0, "What would you")
					my_ard.writeToScreen (1, "like to add?")
					adding = raw_input("What would you like to add?")
					addBottomInventory(adding)
				elif addOrSubtract == "-" or addOrSubtract == "s":
					my_ard.writeToScreen(2,"")
					my_ard.writeToScreen(0, "what would you")
					my_ard.writeToScreen(1, "like to subtract?")
					subtracting = raw_input("What would you like to subtract?")
					subtractBottomInventory(subtracting)
				displayBottomInventory ()
		elif fingerOrInventory == "open":
			unlockTopDoor ()
			unlockBottomDoor ()
		elif fingerOrInventory == "p":
			my_ard.writeToScreen(2,"")
			my_ard.writeToScreen(0,"password?")
			password = raw_input("password?")
			
			my_ard.writeToScreen(2,"")
			
			if password in passwords:
				if passwords[password] == 1:
					my_ard.writeToScreen(0,"Access granted")
					unlockTopDoor ()
				elif  passwords[password] == 2:
					my_ard.writeToScreen(0,"Access granted")
					unlockBottomDoor ()
				elif passwords[password] == 3:
					my_ard.writeToScreen(0,"Access granted")
					unlockTopDoor ()
					unlockBottomDoor ()
			else:
				my_ard.writeToScreen(0,"Access denied")
			
			
		
		elif fingerOrInventory == "f":
			my_ard.writeToScreen(2,"")
			my_ard.writeToScreen(0, "Scan Finger") 
			my_ard.close()
			finger_ard.open(fport)
			
			fingerID = finger_ard.readFingerprint()
			
			while fingerID == -1:
				fingerID = finger_ard.readFingerprint()
		
			finger_ard.close()
			my_ard.open(aport)
			my_ard.configurePWMBoards(1)
			
			my_ard.writeToScreen(2,"")
			fingerID = int(fingerID)
			if knownID[fingerID] == 1:
				my_ard.writeToScreen(0,"Access granted")
				unlockTopDoor ()
			elif knownID[fingerID] == 2:
				my_ard.writeToScreen(0,"Access granted")
				unlockBottomDoor ()
			elif knownID[fingerID] == 3:
				my_ard.writeToScreen(0,"Access granted")
				unlockTopDoor ()
				unlockBottomDoor ()
			my_ard.delay(3)
			my_ard.writeToScreen(2,"")
	my_ard.delay(.002)
		



