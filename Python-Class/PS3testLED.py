# This program will allow someone to raise and lower the brightness of an
# RGB LED using a PS3 controller

from arduinoClass import *

# setup
print "setting up..."
redPin = 11
bluePin = 9
greenPin = 10

my_util = PyUtil()
my_arduino = Arduino("/dev/ttyUSB1")

my_arduino.digitalWrite(greenPin,0)
my_arduino.digitalWrite(redPin,0)

# loop

#my_util.testPS()
#screen = pygame.display.set_mode(0)
#pygame.display.set_caption('Hello World') 

interval = 0.01


while True: 
	
	
    leftY = my_util.getAxisValue(1)
    rightY = my_util.getAxisValue(3)
    leftX = my_util.getAxisValue(0)
    rightX = my_util.getAxisValue(2)
    
    redVal = my_util.map( int(leftY*1000), -1000, 999, 255, 0 )
    blueVal = my_util.map( int(rightY*1000), -1000, 999, 255, 0 )
    greenVal = my_util.map( int( (leftX + rightX)*500 ), -1000, 999, 255, 0 )
    
    my_arduino.analogWrite(redPin, redVal)
    my_arduino.analogWrite(bluePin, blueVal)
    my_arduino.analogWrite(greenPin, greenVal)
    
    print str(leftY) + " " + str(rightY)
    print str(redVal) + " " + str(blueVal)
    print
    
    


      # other event tests, but polling seems to work better in main loop 
      # if event.type == pygame.JOYBUTTONDOWN: 
        # print("joy button down") 
      # if event.type == pygame.JOYBUTTONUP: 
        # print("joy button up") 
      # if event.type == pygame.JOYBALLMOTION: 
        # print("joy ball motion") 
      # axis motion is movement of controller 
      # dominates events when used 
      # if event.type == pygame.JOYAXISMOTION: 
        # print("joy axis motion") 

    # pygame.display.update() 
    my_arduino.delay(interval)

pygame.quit() 
sys.exit()
"""
while True:

	leftY = my_util.getAxisValue(1)
	rightY = my_util.getAxisValue(3)
	
	redVal = my_util.map( int(leftY*1000), -1000, 999, 0, 255 )
	blueVal = my_util.map( int(leftY*1000), -1000, 999, 0, 255 )
	
	my_arduino.analogWrite(redPin, redVal)
	my_arduino.analogWrite(bluePin, blueVal)
	
	print str(leftY) + " " + str(rightY)
	print str(redVal) + " " + str(blueVal)
	print
	
	my_arduino.delay(0.010)


"""

"""
	for i in range(0,256):
		my_arduino.analogWrite(bluePin, i)
		my_arduino.delay(0.005)
	
	print "bright!"
	my_arduino.delay(1)
	
	for i in range(255,-1,-1):
		my_arduino.analogWrite(bluePin, i)
		my_arduino.delay(0.005)
	
	print "dark!"
	my_arduino.delay(1)
"""
