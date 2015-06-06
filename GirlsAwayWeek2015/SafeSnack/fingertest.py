
from arduino import *

finger_ard = Arduino()

knownID = {1:1,2:2,3:3,4:1,5:2}


finger_ard.open("/dev/ttyUSB0")
			
fingerID = finger_ard.readFingerprint()
			
while fingerID == -1:
	fingerID = finger_ard.readFingerprint()
		
print "Id " + str(fingerID) + " recognized"	

fingerID = int(fingerID)
if knownID[fingerID] == 1:
	print "access 1 found"

elif knownID[fingerID] == 2:
	print "access 2 found"
elif knownID[fingerID] == 3:
	print "access 3 found"

