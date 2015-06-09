'''
TO-DO:
Separate utilities/main into .py files / add import
Motor/Servo attach (lists)
Motor/Servo move
'''

import serial, time

class Arduino(object):
    config_mode = False
    ext_pins = -1
    ext_servo = -1:0
    ext_motor = -1:0
    ext_pwm = -1:0
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
            self.ext_servo.append(pin_num:90)
            msg = "M " + str(pin_num) + " ;"
            self.ard_ser.write(msg)
            self.recvMsg()
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
            self.ext_pwm.append(pin_num:50)
            msg = "M " + str(pin_num) + " ;"
            self.ard_ser.write(msg)
            self.recvMsg()
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
            self.ext_motor.append(pin_num:0)
            msg = "M " + str(pin_num) + " ;"
            self.ard_ser.write(msg)
            self.recvMsg()
        elif self.ext_pins.count(pin_num) > 0 and pin_num < 16 and pin_num > -1:
            print "ERR: This pin already attached!"
        else:
            print "ERR: Invalid pin number!"

    def setMotor(self, pin_num, value):
        value += 500
        if pin_num in self.ext_motor and value <= 1000 and value >= 0:
            msg = "K " + str(pin_num) + " " + str(value) + ";"
            self.ard_ser.write(msg)
            self.recvMsg()
            self.ext_motor[pin_num] = value
        else:
            print "ERR: Invalid pin number or PWM value"

    def getMotorVal(self, pin_num):
        if pin_num in self.ext_motor:
            return self.ext_motor[pin_num]
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
