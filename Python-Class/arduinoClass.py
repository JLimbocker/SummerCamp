'''
TO-DO:
Separate utilities/main into .py files / add import
gyro, accel, magnetometer
'''

import pygame, sys, serial, time
from pygame.locals import *

class Arduino(object):
    config_mode = False
    ext_pins = [-1]
    ext_servo = {-1:0}
    ext_motor = {-1:0}
    ext_pwm = {-1:0}
    ard_ser = serial.Serial(None, 115200)

    def __init__(self, port_name):
        self.ard_ser.port = port_name
        self.ard_ser.timeout = None
        self.ard_ser.open()
        time.sleep(3)

    def readUntil(self, file_obj, delim_char):
        string_read = ""
        while file_obj.inWaiting() == 0:
            pass
        while True:
            curr_char = file_obj.read()
            if curr_char == delim_char:
                break
            else:
                string_read += curr_char
                pass
        return string_read

    def sendMsg(self, msg):
        self.ard_ser.write(msg)

    def recvMsg(self):
        return self.readUntil(self.ard_ser, '\n')

    def enterConfigMode(self):
        if self.config_mode == False:
            self.sendMsg("C 1 ;")
            print self.recvMsg()
                # print "NO_RESP_ERR"
                # time.sleep(1)
            self.config_mode = True;
            print "Now in config mode"
        else:
            print "Already in config mode"

    def exitConfigMode(self):
        if self.config_mode == True:
            self.sendMsg("C 0 ;")
            print self.recvMsg()
            self.config_mode = False
            print "Exited config mode"
        else:
            print "Not in config mode"

    def analogWrite(self, pin_num, value):
        msg = "a " + str(pin_num) + " " + str(value) + ";"
        self.sendMsg(msg)
        print self.recvMsg()

    def analogRead(self, pin_num):
        msg = "A " + str(pin_num) + " ;"
        self.sendMsg(msg)
        front = self.readUntil(self.ard_ser, ' ')
        middle = self.readUntil(self.ard_ser, ' ')
        rest = self.recvMsg()
        print front + " " + middle + " " + rest
        return middle

    def digitalWrite(self, pin_num, value):
        msg = "d " + str(pin_num) + " " + str(value) + ";"
        self.ard_ser.write(msg)
        self.recvMsg()

    def digitalRead(self, pin_num):
        msg = "D " + str(pin_num) + " ;"
        self.sendMsg(msg)
        front = self.readUntil(self.ard_ser, ' ')
        middle = self.readUntil(self.ard_ser, ' ')
        rest = self.recvMsg()
        print front + " " + middle + " " + rest
        return middle

    def pinMode(self, pin_num, value):
        msg = "P " + str(pin_num) + " " + str(value) + ";"
        self.sendMsg(msg)
        self.recvMsg()

    def delay(self, seconds):
        time.sleep(seconds)

    def tone(self, pin_num, value):
        msg = "t " + str(pin_num) + " " + str(value) + ";"
        self.ard_ser.write(msg)
        self.recvMsg()

    def attachServo(self, pin_num):
        if self.ext_pins.count(pin_num) == 0 and pin_num < 16 and pin_num > -1:
            self.ext_pins.append(pin_num)
            self.ext_servo[pin_num] = 90
        elif self.ext_pins.count(pin_num) > 0 and pin_num < 16 and pin_num > -1:
            print "ERR: This pin already attached!"
        else:
            print "ERR: Invalid pin number!"

    def moveServo(self, pin_num, value):
        if pin_num in self.ext_servo and value <= 180 and value >= 0:
            msg = "S " + str(pin_num) + " " + str(value) + ";"
            self.ard_ser.write(msg)
            self.recvMsg()
            self.ext_servo[pin_num] = value
        else:
            print "ERR: Invalid pin number or servo value"

    def attachExtPWM(self, pin_num):
        if self.ext_pins.count(pin_num) == 0 and pin_num < 16 and pin_num > -1:
            self.ext_pins.append(pin_num)
            self.ext_pwm[pin_num] = 50
        elif self.ext_pins.count(pin_num) > 0 and pin_num < 16 and pin_num > -1:
            print "ERR: This pin already attached!"
        else:
            print "ERR: Invalid pin number!"

    def setPWM(self, pin_num, value):
        if pin_num in self.ext_pwm and value <= 100 and value >= 0:
            msg = "P " + str(pin_num) + " " + str(value) + ";"
            self.ard_ser.write(msg)
            self.recvMsg()
            self.ext_pwm[pin_num] = value
        else:
            print "ERR: Invalid pin number or PWM value"

    def attachMotor(self, pin_num):
        if self.ext_pins.count(pin_num) == 0 and pin_num < 16 and pin_num > -1:
            self.ext_pins.append(pin_num)
            self.ext_motor[pin_num]=0
        elif self.ext_pins.count(pin_num) > 0 and pin_num < 16 and pin_num > -1:
            print "ERR: This pin already attached!"
        else:
            print "ERR: Invalid pin number!"

    def setMotor(self, pin_num, value):
        value += 500
        if pin_num in self.ext_motor and value <= 1000 and value >= 0:
            msg = "M " + str(pin_num) + " " + str(value) + ";"
            self.ard_ser.write(msg)
            self.recvMsg()
            self.ext_motor[pin_num] = value
        else:
            print "ERR: Invalid pin number or PWM value"

    def getMotorVal(self, pin_num):
        if pin_num in self.ext_motor:
            return self.ext_motor[pin_num]-500
        else:
            print "ERR: Invalid pin"

    def getPWMVal(self, pin_num):
        if pin_num in self.ext_pwm:
            return self.ext_pwm[pin_num]
        else:
            print "ERR: Invalid pin"

    def getServoVal(self, pin_num):
        if pin_num in self.ext_servo:
            return self.ext_servo[pin_num]
        else:
            print "ERR: Invalid pin"



class PyUtil(object):

	

    def __init__(self):
        pygame.joystick.init()  # initialize pygame to read controllers
        self.joystick_count = pygame.joystick.get_count()  # get 1 joystick, number 0
        self.joystick = pygame.joystick.Joystick(0)  # assign the first controller
        self.joystick.init()  # initialize the first controller for reading

        self.numaxes = self.joystick.get_numaxes() # return the number of axes on the controller
        self.numbuttons = self.joystick.get_numbuttons() # return number of buttons on the controller

    def getAxisValue(self, axis):
        # axis values:
        # 0 = Left joystick left to right values -1.0 to 0.99
        # 1 = Left joystick up to down values -1.0 to 0.99
        # 2 = Right joystick left to right values -1.0 to 0.99
        # 3 = Right joystick up to down values -1.0 to 0.99
        return self.joystick.get_axis(axis)

    def getButtonValue(self, button):
        # button values:
        # 0 = Select
        # 1 =
        # 2 = 
        # 3 = Start
        # 4 = Digital Up
        # 5 = Digital Right
        # 6 = Digital Down
        # 7 = Digitial Left
        # 8 = L2 (digital mode)
        # 9 = R2 (digital mode)
        # 10 = R1
        # 11 = L1
        # 12 = Triangle
        # 13 = Circle
        # 14 = X
        # 15 = Square
        # 16 = PS
        # 17 = 
        # 18 =
        return self.joystick.get_button(button)


    def constrain(self, value, low_bound, high_bound):
        # make sure bounds are in the correct order
        if low_bound > high_bound:
            temp = low_bound
            low_bound = high_bound
            high_bound = temp

        if value < low_bound:
            return low_bound
        elif value > high_bound:
            return high_bound
        else:
            return value

    def map(self, value, from_low, from_high, to_low, to_high):
        return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low

    def testPS(self):
        screen = pygame.display.set_mode((400,300))
        pygame.display.set_caption('Hello World') 

        interval = 0.01

        print("joystick_count")
        print(self.joystick_count)
        print("______________")

        print("numaxes") 
        print(self.numaxes) 
        print("______________")

        print("numbuttons")
        print(self.numbuttons)
        print("______________")
        
        loopQuit = False 
        while loopQuit == False: 
		
            # test joystick axes 
            
            print

            outstr = "" 

            for i in range(0,4):
            	axis = self.joystick.get_axis(i)
            	outstr = outstr + str(i) + ":" + str(axis) + "|"

            print(outstr) 

            # test controller buttons 
            
            outstr = "" 

            for i in range(0,self.numbuttons): 

                button = self.joystick.get_button(i) 

                outstr = outstr + str(i) + ":" + str(button) + "|" 
            
            print(outstr) 

            for event in pygame.event.get(): 

                if event.type == QUIT: 
					loopQuit = True

                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE: 
                        loopQuit = True 

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
            time.sleep(interval) 

        pygame.quit() 
        sys.exit() 



my_util = PyUtil()

my_util.testPS()

# arduino = Arduino("/dev/tty.usbserial-A5027J57")
# arduino.enterConfigMode()
# arduino.pinMode(9, 2)
# arduino.pinMode(3, 0)
# arduino.exitConfigMode()
# while True:
#     if arduino.digitalRead(9) == "0":
#         arduino.digitalWrite(3, 1)
#     else:
#         arduino.digitalWrite(3, 0)
