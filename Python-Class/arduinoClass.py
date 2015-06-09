import pygame, sys, serial, time
from pygame.locals import *

class Arduino(object):
    config_mode = False
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

    def delay(self, milliseconds):
        time.sleep(milliseconds/1000.0)

    def tone(self, pin_num, value):
        msg = "t " + str(pin_num) + " " + str(value) + ";"
        self.ard_ser.write(msg)
        self.recvMsg()


class PyUtil(object):

    def __init__(self):
        pygame.joystick.init()  # initialize pygame to read controllers
        joystick_count = pygame.joystick.get_count()  # get 1 joystick, number 0
        joystick = pygame.joystick.Joystick(0)  # assign the first controller
        joystick.init()  # initialize the first controller for reading

        numaxes = joystick.get_numaxes() # return the number of axes on the controller
        numbuttons = joystick.get_numbuttons() # return number of buttons on the controller

    def getAxisValue(self, axis):
        # axis values:
        # 0 = Left joystick left to right values -1.0 to 0.99
        # 1 = Left joystick up to down values -1.0 to 0.99
        # 2 = Right joystick left to right values -1.0 to 0.99
        # 3 = Right joystick up to down values -1.0 to 0.99
        return joystick.get_axis(axis)

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
        return joystick.get_button(button)


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


arduino = Arduino("/dev/tty.usbserial-A5027J57")

arduino.enterConfigMode()
arduino.pinMode(9, 2)
arduino.pinMode(3, 0)
arduino.exitConfigMode()

while True:
    if arduino.digitalRead(9) == "0":
        arduino.digitalWrite(3, 1)
    else:
        arduino.digitalWrite(3, 0)

