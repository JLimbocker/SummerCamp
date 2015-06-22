'''
TO-DO:
Separate utilities/main into .py files / add import
'''

import sys, serial, time, math #, pygame
#from pygame.locals import *

class PyUtil(object):

    def __init__(self):
		pass

    def initializeBluetooth(self):
        pygame.init()
        pygame.joystick.init() # initialize pygame to read controllers
        self.joystick_count = pygame.joystick.get_count() # get 1 joystick, number 0
        self.joystick = pygame.joystick.Joystick(0) # assign the first controller
        self.joystick.init() # initialize first controller for reading

        self.numaxes = self.joystick.get_numaxes()
        self.numbuttons = self.joystick.get_numbuttons()
    def getAxisValue(self, axis):
        # axis values:
        # 0 = Left joystick left to right values -1.0 to 0.99
        # 1 = Left joystick up to down values -1.0 to 0.99
        # 2 = Right joystick left to right values -1.0 to 0.99
        # 3 = Right joystick up to down values -1.0 to 0.99
        pygame.event.pump()
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
        pygame.event.pump()
        return self.joystick.get_button(button)



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
            	axis = self.getAxisValue(i)
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


class Arduino(object):
    config_mode = False
    LF_pins = [-1]

    # These are the lists for 60 HZ boards
    amt_LF_boards = 0
    LF_pins = [-1]
    ext_servo = {-1:0}

    # These are the lists for 333 HZ boards
    amt_HF_boards = 0
    HF_pins = [-1]
    ext_pwm = {-1:0}
    ext_motor = {-1:0}

    ard_ser = serial.Serial(None, 115200)
    util = PyUtil()



    # Constructor
    # Creates an Arduino object
    def __init__(self):
        self.ard_ser.port = None
        self.ard_ser.timeout = None

    # open(self, port_name)
    # Opens a serial connection on the given port
    #
    # Parameters:
    # port_name - the port on which to open the serial port
    #
    # TODO: Add error handling for port not found errors
    def open(self, port_name):
        self.ard_ser.port = port_name;
        self.ard_ser.open();
        #time.sleep(0.1);
        msg = self.recvMsg();
        print "Connected!"
    # close(self)
    # Closes the serial port
    #
    # Parameters:
    # none
    def close(self):
        self.ard_ser.close()

    # readUntil(self, file_obj, delim_char)
    # Reads from file_obj until delim_char
    #
    # Parameters:
    # file_obj - the stream from which to read data
    # delim_char - the delimiting character
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

    # readUntil_file(self, file_obj, delim_char)
    # Not actually sure what this is for.
    #
    # Parameters:
    # file_obj - the stream from which to read data
    # delim_char - the delimiting character
    def readUntil_file(self, file_obj, delim_char):
        string_read = ""
        while True:
            curr_char = file_obj.read()
            print curr_char
            if curr_char == delim_char:
                print "hello"
                break
            else:
                string_read += curr_char
                pass
        return string_read

    # sendMsg(self, msg)
    # Sends some monosodium glutemate over the serial connection
    #
    # Parameters:
    # msg - the message to be sent
    def sendMsg(self, msg):
        self.ard_ser.write(msg)

    # recvMsg(self, msg)
    # Receives a message over the serial connection.  Reads until new line character.
    #
    # Parameters:
    # none
    def recvMsg(self):
        return self.readUntil(self.ard_ser, '\n')

    # enterConfigMode(self)
    # Puts the Arduino into config mode
    #
    # Parameters:
    # none
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

    # exitConfigMode(self)
    # Takes the Arduino out of config mode
    #
    # Parameters:
    # none
    def exitConfigMode(self):
        if self.config_mode == True:
            self.sendMsg("C 0 ;")
            print self.recvMsg()
            self.config_mode = False
            print "Exited config mode"
        else:
            print "Not in config mode"
    # analogWrite(self, pin_num, value)
    # Writes a PWM signal to the given pin
    #
    # Parameters:
    # pin_num - the pin number to write to
    # value - the 8 bit PWM value
    def analogWrite(self, pin_num, value):
        msg = "a " + str(pin_num) + " " + str(value) + " ;"
        self.sendMsg(msg)
        self.recvMsg()

    # analogRead(self, pin_num)
    # Reads the ADC value on the given analog pin
    #
    # Parameters:
    # pin_num - the pin to read
    def analogRead(self, pin_num):
        msg = "A " + str(pin_num) + " ;"
        self.sendMsg(msg)
        front = self.readUntil(self.ard_ser, ' ')
        middle = self.readUntil(self.ard_ser, ' ')
        rest = self.recvMsg()
        # print front + " " + middle + " " + rest
        return int(middle)

    # digitalWrite(self, pin_num, value)
    # Writes a digital value to the specified pin
    #
    # Parameters:
    # pin_num - the pin to write
    # value - the value to write
    def digitalWrite(self, pin_num, value):
        msg = "d " + str(pin_num) + " " + str(value) + " ;"
        self.ard_ser.write(msg)
        self.recvMsg()

    # digitalRead(self, pin_num)
    # Reads the digital value of the sprcified pin
    #
    # Parameters:
    # pin_num - the pin to read
    def digitalRead(self, pin_num):
        msg = "D " + str(pin_num) + " ;"
        self.sendMsg(msg)
        front = self.readUntil(self.ard_ser, ' ')
        middle = self.readUntil(self.ard_ser, ' ')
        rest = self.recvMsg()
        # print front + " " + middle + " " + rest
        return int(middle)

    # pinMode(self, pin_num, value)
    # Set the pin mode.  Must be used from config mode
    #
    # Parameters:
    # pin_num - the pin to change
    # value - the mode to set the pin to
    def pinMode(self, pin_num, value):
        msg = "P " + str(pin_num) + " " + str(value) + " ;"
        self.sendMsg(msg)
        print self.recvMsg()

    # delay(self, seconds)
    # Waits for 'seconds' seconds.
    #
    # Parameters:
    # seconds - the time to wait
    def delay(self, seconds):
        time.sleep(seconds)

    # tone(self, pin_num, value, duration)
    # plays a tone on the given pin
    #
    # Parameters:
    # pin_num - the pin to play the tone on
    # value - the frequency of the tone
    # duration - the duration of the tone
    def tone(self, pin_num, value, duration):
        msg = "t " + str(pin_num) + " " + str(value) + " " + str(duration) + " ;"
        self.ard_ser.write(msg)
        print self.recvMsg()

    # readFingerprint(self)
    # SPECIAL FIRMWARE REQUIRED
    # This function requests a fingerprint scan from the Arduino
    #
    # Parameters:
    # none
    #
    # Returns:
    # fingerID - the id of the fingerprint, or -1 if bad read
    def readFingerprint(self):
        msg = "f ;"
        self.sendMsg(msg)
        front = self.readUntil(self.ard_ser, ' ')
        fingerID = self.readUntil(self.ard_ser, ' ')
        confidence = self.recvMsg()
        if(confidence < 100):
            return fingerID
        return -1

    # writeToScreen(self, row_num, message)
    # Writes 'message' to the LCD screen
    #
    # Parameters:
    # row_num - the row of the LCD to write to
    # message - the message to write
    def writeToScreen(self, row_num, message):
        msg = "L " + str(row_num) + " " + message + " ;"
        self.ard_ser.write(msg)
        print self.recvMsg()

    # servoWrite(self, pin_num, value)
    # Writes a position to a servo specified by pin_num
    #
    # Parameters:
    # pin_num - the index of the servo
    # value - the position to write
    def servoWrite(self, pin_num, value):
        if value <= 180 and value >= 0:
            value = map(value, 0, 180, 200, 425)
            msg = "S " + str(pin_num) + " " + str(value) + " ;"
            self.sendMsg(msg)
            print self.recvMsg()
        else:
            print "ERR: Invalid pin number or servo value"

    # servoWriteMicroseconds(self, pin_num, value)
    # Writes a pulse width to a servo
    #
    # Parameters:
    # pin_num - the index of the servo
    # value - the pulse width
    def servoWriteMicroseconds(self, pin_num, value):
        if value <= 3000 and value >= 200:
            value = map(value, 200, 3000, 42, 625)
            msg = "S " + str(pin_num) + " " + str(value) + " ;"
            self.ard_ser.write(msg)
            print self.recvMsg()
        else:
            print "ERR: Invalid pin number or servo value"

    # setPWM(self, pin_num, value)
    # Sets the PWM value for a channel on the PWM board
    #
    # Parameters:
    # pin_num - the index of the pin on the PWM board
    # value - the pwm value
    def setPWM(self, pin_num, value):
        if value <= 2000 and value >= 0:
            msg = "M " + str(pin_num) + " " + str(value) + " ;"
            self.ard_ser.write(msg)
            self.recvMsg()
        else:
            print "ERR: Invalid pin number or PWM value"

    # setVEX(self, pin_num, value)
    # Sets the PWM value for a VEX 29 Motor driver
    #
    # Parameters:
    # pin_num - the index of the motor on the PWM board
    # value - the pwm value
    def setVEX(self, pin_num, value):
        value += 500
        if value <= 1000 and value >= 0:
            value = map(value, 0, 1000, 195, 425)
            msg = "S " + str(pin_num) + " " + str(value) + " ;"
            self.ard_ser.write(msg)
            self.recvMsg()
        else:
            print "ERR: Invalid pin number or PWM value"

    # setTalon(self, pin_num, value)
    # Sets the PWM value for a Talon Motor driver
    #
    # Parameters:
    # pin_num - the index of the motor on the PWM board
    # value - the pwm value
    def setTalon(self, pin_num, value):
        value += 500
        if value <= 1000 and value >= 0:
            value = map(value, 0, 1000, 600, 3500)
            msg = "M " + str(pin_num) + " " + str(value) + " ;"
            self.ard_ser.write(msg)
            self.recvMsg()
        else:
            print "ERR: Invalid pin number or PWM value"

    # getGyro(self, axis)
    # Reads the gyroscope
    #
    # Parameters:
    # axis - the axis to read
    def getGyro(self, axis):
        msg = "y ;"
        self.ard_ser.write(msg)
        prefix = self.readUntil(self.ard_ser, ' ')
        x_val = self.readUntil(self.ard_ser, ' ')
        y_val = self.readUntil(self.ard_ser, ' ')
        z_val = self.readUntil(self.ard_ser, ' ')
        suffix = self.recvMsg()
        print prefix + " " + x_val + " " + y_val + " " + z_val + " " + suffix
        if axis == 0:
            return x_val
        elif axis == 1:
            return y_val
        elif axis == 2:
            return z_val
        else:
            print "ERR: Invalid axis number"

    # getAccel(self, axis)
    # Reads the accelerometer
    #
    # Parameters:
    # axis - the axis to read
    def getAccel(self, axis):
        msg = "g ;"
        self.ard_ser.write(msg)
        prefix = self.readUntil(self.ard_ser, ' ')
        x_val = self.readUntil(self.ard_ser, ' ')
        y_val = self.readUntil(self.ard_ser, ' ')
        z_val = self.readUntil(self.ard_ser, ' ')
        suffix = self.recvMsg()
        print prefix + " " + x_val + " " + y_val + " " + z_val + " " + suffix
        if axis == 0:
            return x_val
        elif axis == 1:
            return y_val
        elif axis == 2:
            return z_val
        else:
            print "ERR: Invalid axis number"

    # setupIMU(self)
    # Enables the I2C IMU
    #
    # Parameters:
    # none
    def setupIMU(self):
        msg = "I ;"
        self.sendMsg(msg)
        self.recvMsg()

    # configurePWMBoards(self, mode)
    # Sets up the Adafruit PWM boards for use with either of the motor controllers or servos.
    #
    # Parameters:
    # mode - the mode to set the PWM board to
    def configurePWMBoards(self, mode):
        #text-based setup system
        if mode == 0:

            #Gather data on input amounts
            file = open('boardSetup.dat', 'w')
            print "Welcome to the PWM board configuration menu."
            amt_LF_outs = raw_input("How many low frequency devices (servos, VEX 29 controllers) are you using?")
            amt_HF_outs = raw_input("How many high frequency devices (Talon motor controllers) are you using?")
            self.amt_LF_boards = math.ceil(float(amt_LF_outs)/16.0);
            print str(self.amt_LF_boards) + " low frequency boards necessary."
            file.write(str(int(self.amt_LF_boards)) + '\n')
            self.amt_HF_boards = math.ceil(float(amt_HF_outs)/16.0);
            print str(self.amt_HF_boards) + " high frequency boards necessary."
            file.write(str(int(self.amt_HF_boards)) + '\n')

            if int(self.amt_HF_boards) > 1 or int(self.amt_LF_boards) > 1:
                print "ERR: This amount of boards not supported at this time (max 1 each type). Config not saved."
                os.remove('boardSetup.dat')
                return

            #Get addresses for those boards
            for i in range(0,int(self.amt_LF_boards)):
                address = raw_input("What is the I2C address of low freq board #" + str(i+1) + "? ")
                file.write(str(address) + '\n')

            #Get addresses for those boards
            for i in range(0,int(self.amt_HF_boards)):
                address = raw_input("What is the I2C address of high freq board #" + str(i+1) + "? ")
                file.write(str(address) + '\n')

            file.close()

        #Use configuration data to set up and attach boards
        if mode == 0:
            print "Warning: Running without config menu. Make sure config is up to date"

        time.sleep(1)

        self.enterConfigMode()

        infile = open('boardSetup.dat', 'r')

        self.amt_LF_boards = int(infile.readline())
        print str(self.amt_LF_boards) + " lf boards read"
        self.amt_HF_boards = int(infile.readline())
        print str(self.amt_HF_boards) + " hf boards read"

        for i in range(0, self.amt_LF_boards):
            address = int(infile.readline())
            msg = "S " + str(address) + " ;"
            self.sendMsg(msg)
            print self.recvMsg()

        for i in range(0, self.amt_HF_boards):
            address = int(infile.readline())
            msg = "M " + str(address) + " 2 ;"
            self.sendMsg(msg)
            print self.recvMsg()

        self.exitConfigMode()

        ##DEPRECATED##

        def attachServo(self, pin_num):
            if self.amt_LF_boards == 0:
                print "ERR: No boards of this type exist"
            if self.ext_pins.count(pin_num) == 0 and pin_num < 16 and pin_num > -1:
                self.ext_pins.append(pin_num)
                self.ext_servo[pin_num] = 90
            elif self.ext_pins.count(pin_num) > 0 and pin_num < 16 and pin_num > -1:
                print "ERR: This pin already attached!"
            else:
                print "ERR: Invalid pin number!"

        def attachMotor(self, pin_num):
            if self.ext_pins.count(pin_num) == 0 and pin_num < 16 and pin_num > -1:
                self.ext_pins.append(pin_num)
                self.ext_motor[pin_num]=0
            elif self.ext_pins.count(pin_num) > 0 and pin_num < 16 and pin_num > -1:
                print "ERR: This pin already attached!"
            else:
                print "ERR: Invalid pin number!"

        def attachExtPWM(self, pin_num):
            if self.ext_pins.count(pin_num) == 0 and pin_num < 16 and pin_num > -1:
                self.ext_pins.append(pin_num)
                self.ext_pwm[pin_num] = 50
            elif self.ext_pins.count(pin_num) > 0 and pin_num < 16 and pin_num > -1:
                print "ERR: This pin already attached!"
            else:
                print "ERR: Invalid pin number!"
    # getPing(self, pin_num)
    # This function reads a ping sensor on the specified pin
    #
    # Parameters:
    # pin_num - the pin on which the sensor is located
    def getPing(self, pin_num):
        msg = "T " + str(pin_num) + " ;"
        self.sendMsg(msg)
        prefix = self.readUntil(self.ard_ser, ' ')
        distance = self.readUntil(self.ard_ser, ' ')
        suffix = self.recvMsg()
        print prefix + " " + distance + " " + suffix
        return int(distance)


# global functions
def constrain(value, low_bound, high_bound):
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

def map(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low


# global constants

OUTPUT = 0
INPUT = 1
INPUT_PULLUP = 2

LOW = 0
HIGH = 1

OFF = 0
ON = 1


NOTE_B0  = 31
NOTE_C1  = 33
NOTE_CS1 = 35
NOTE_D1  = 37
NOTE_DS1 = 39
NOTE_E1  = 41
NOTE_F1  = 44
NOTE_FS1 = 46
NOTE_G1  = 49
NOTE_GS1 = 52
NOTE_A1  = 55
NOTE_AS1 = 58
NOTE_B1  = 62
NOTE_C2  = 65
NOTE_CS2 = 69
NOTE_D2  = 73
NOTE_DS2 = 78
NOTE_E2  = 82
NOTE_F2  = 87
NOTE_FS2 = 93
NOTE_G2  = 98
NOTE_GS2 = 104
NOTE_A2  = 110
NOTE_AS2 = 117
NOTE_B2  = 123
NOTE_C3  = 131
NOTE_CS3 = 139
NOTE_D3  = 147
NOTE_DS3 = 156
NOTE_E3  = 165
NOTE_F3  = 175
NOTE_FS3 = 185
NOTE_G3  = 196
NOTE_GS3 = 208
NOTE_A3  = 220
NOTE_AS3 = 233
NOTE_B3  = 247
NOTE_C4  = 262
NOTE_CS4 = 277
NOTE_D4  = 294
NOTE_DS4 = 311
NOTE_E4  = 330
NOTE_F4  = 349
NOTE_FS4 = 370
NOTE_G4  = 392
NOTE_GS4 = 415
NOTE_A4  = 440
NOTE_AS4 = 466
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_CS5 = 554
NOTE_D5  = 587
NOTE_DS5 = 622
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_FS5 = 740
NOTE_G5  = 784
NOTE_GS5 = 831
NOTE_A5  = 880
NOTE_AS5 = 932
NOTE_B5  = 988
NOTE_C6  = 1047
NOTE_CS6 = 1109
NOTE_D6  = 1175
NOTE_DS6 = 1245
NOTE_E6  = 1319
NOTE_F6  = 1397
NOTE_FS6 = 1480
NOTE_G6  = 1568
NOTE_GS6 = 1661
NOTE_A6  = 1760
NOTE_AS6 = 1865
NOTE_B6  = 1976
NOTE_C7  = 2093
NOTE_CS7 = 2217
NOTE_D7  = 2349
NOTE_DS7 = 2489
NOTE_E7  = 2637
NOTE_F7  = 2794
NOTE_FS7 = 2960
NOTE_G7  = 3136
NOTE_GS7 = 3322
NOTE_A7  = 3520
NOTE_AS7 = 3729
NOTE_B7  = 3951
NOTE_C8  = 4186
NOTE_CS8 = 4435
NOTE_D8  = 4699
NOTE_DS8 = 4978
