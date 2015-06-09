import serial, time

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

    def digitalWrite(self, pin_num, value):
        msg = "d " + str(pin_num) + " " + str(value) + ";"
        self.ard_ser.write(msg)
        self.recvMsg()

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

arduino = Arduino("/dev/tty.usbserial-A5027JS4")
arduino.enterConfigMode()
arduino.pinMode(9, 1)
arduino.exitConfigMode()
while True:
    arduino.tone(9, 440)
    arduino.delay(1)

