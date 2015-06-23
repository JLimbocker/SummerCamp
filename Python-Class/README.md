# ArduPithon
---
This firmware serves as the interface between a Raspberry Pi running python and an Arduino microcontroller.  This firmware is designed to be run using its [Arduino counterpart](https://github.com/JLimbocker/SummerCamp/tree/master/Arduino-Firmware).

Written by Parker Holloway, Travis Siems, and Jeff Limbocker.
Summer 2015
## Contents
+ [Functions](#functions)
  + [open](#f_open)
  + [close](#f_close)
  + [readUntil](#f_readUntil)
  + [readUntil_file](#f_readUntil_file)
  + [sendMsg](#f_sendMsg)
  + [recvMsg](#f_recvMsg)
  + [enterConfigMode](#f_enterConfigMode)
  + [exitConfigMode](#f_exitConfigMode)
  + [analogWrite](#f_analogWrite)
  + [analogRead](#f_analogRead)
  + [digitalWrite](#f_digitalWrite)
  + [digitalRead](#f_digitalRead)
  + [pinMode](#f_pinMode)
  + [delay](#f_delay)
  + [tone](#f_tone)
  + [readFingerprint](#f_readFingerprint)
  + [writeToScreen](#f_writeToScreen)
  + [servoWrite](#f_servoWrite)
  + [servoWriteMicroseconds](#f_servoWriteMicroseconds)
  + [setPWM](#f_setPWM)
  + [setVEX](#f_setVEX)
  + [setTalon](#f_setTalon)
  + [getGyro](#f_getGyro)
  + [getAccel](#f_getAccel)
  + [setupIMU](#f_setupIMU)
  + [configurePWMBoards](#f_configurePWMBoards)
  + [getPing](#f_getPing)
  + [attachStepper](#f_attachStepper)
+ [Constants](#constants)
+ [Communication](#communication)

## Functions <a id="functions"></a>
#### __init__(self) <a id="f_init"></a>
  + Constructor for the Arduino Object.

#### open(self, port_name) <a id="f_open"></a>
  + Opens a serial connection on the given port
  + Parameters:
    + port_name - the port on which to open the serial port
  + Returns:
    + nothing

#### close(self)  <a id="f_close"></a>
  + Closes the serial connection
  + Parameters:
    + none
  + Returns:
    + nothing

#### readUntil(self, file_obj, delim_char)  <a id="f_readUntil"></a>
  + Reads from file_obj until delim_char
  + Parameters:
    + file_obj - the stream from which to read data
    + delim_char - the delimiting character
  + Returns:
    + string_read - the string read from the file

#### readUntil_file(self, file_obj, delim_char) <a id="f_readUntil_file"></a>
  + Appears to be a debug version of readUntil.
  + Parameters:
    + file_obj - the stream from which to read data
    + delim_char - the delimiting character
  + Returns:
    + string_read - the string read from the file

#### sendMsg(self, msg) <a id="f_sendMsg"></a>
  + Sends msg over the serial connection
  + Parameters:
    + msg - the message to send
  + Returns:
    + nothing

#### recvMsg(self) <a id="f_recvMsg"></a>
  + Receives a message over the serial connection.  Reads until the newline character
  + Parameters:
    + none  
  + Returns:
    + the received message

#### enterConfigMode(self) <a id="f_enterConfigMode"></a>
  + Puts the Arduino into config mode
  + Parameters:
    + none
  + Returns:
    + nothing

#### exitConfigMode(self) <a id="f_exitConfigMode"></a>
  + Takes the Arduino out of config mode
  + Parameters:
    + none
  + Returns:
    + none

#### analogWrite(self, pin_num, value) <a id="f_analogWrite"></a>
  + Writes a PWM signal to the given pin
  + Parameters:
    + pin_num - the pin number to write to
    + value - the 8-bit PWM value
  + Returns:
    + nothing

#### analogRead(self, pin_num) <a id="f_analogRead"></a>
  + Reads the ADC value on the given analog pin
  + Parameters:
    + pin_num - the pin to read
  + Returns:
    + the analog input value from the specified pin

#### digitalWrite(self, pin_num, value) <a id="f_digitalWrite"></a>
  + Writes a digital value to the specified pin
  + Parameters:
    + pin_num - the pin to write to
    + value - the value to write
  + Returns:
    + nothing

#### digitalRead() <a id="f_digitalRead"></a>
  + Reads a digital value from the specified pin
  + Parameters:
    + pin_num - the pin to read from
  + Returns:
    + the digital input value from the specified pin

#### pinMode(pin_num, value) <a id="f_pinMode"></a>
  + Sets the pin mode of the specified pin.  Must be used from config mode.
  + Parameters:
    + pin_num - the specified pin
    + value - the mode to set the pin to
  + Returns:
    + nothing

#### delay(self, seconds) <a id="f_delay"></a>
  + Delays for a specified time
  + Parameters:
    + seconds - the delay time
  + Returns:
    + nothing

#### tone(self, pin_num, value, duration) <a id="f_tone"></a>
  + Plays a tone on the given pin
  + Parameters:
    + pin_num - the pin to play the tone on
    + value - the frequency of the tone
    + duration - the duration of the tone
  + Returns:
    + nothing

#### readFingerprint(self) <a id="f_readFingerprint"></a>
  + SPECIAL FIRMWARE REQUIRED
  + This function requests a fingerprint scan from the Arduino
  + Parameters:
    + none  
  + Returns:
    + fingerID - the ID of the fingerprint, or -1 if no fingerprint found

#### writeToScreen(self, row_num, message) <a id="f_writeToScreen"></a>
  + Writes a message to the LCD screen
  + Parameters:
    + row_num - the row on which to write the message
    + message - the message to be writeToScreen
  + Returns:
    + nothing

#### servoWrite(self, pin_num, value) <a id="f_servoWrite"></a>
  + Writes a position to the servo specified by pin_num
  + Parameters:
    + pin_num - the index of the servo on the Servo Controller board  
    + value - the position to write in degrees
  + Returns:
    + nothing

#### servoWriteMicroseconds(self, pin_num, value) <a id="f_servoWriteMicroseconds"></a>
  + Writes a pulse width to the servo specified by pin_num
  + Parameters:
    + pin_num - the index of the servo
    + value - the pulse width in microseconds
  + Returns:
    + nothing

#### setPWM(self, pin_num, value) <a id="f_setPWM"></a>
  + Sets the PWM value for the specified channel on a PWM board
  + Parameters:
    + pin_num - the index of the pin on the PWM board
    + value - the 12-bit PWM value to write to the pin
  + Returns:
    + nothing

#### setVEX(self, pin_num, value) <a id="f_setVEX"></a>
  + Sets the PWM value for a VEX 29 motor driver
  + Parameters:
    + pin_num - the index of the motor driver on the PWM board
    + value - the pwm value
  + Returns:
    + nothing

#### setTalon(self, pin_num, value) <a id="f_setTalon"></a>
  + Sets the PWM value for a Talon motor driver
  + Parameters:
    + pin_num - the index of the motor driver on the PWM board
    + value - the pwm value
  + Returns:
    + nothing

#### getGyro(self, axis) <a id="f_getGyro"></a>
  + Reads the specified axis of the gyroscope
  + Parameters:
    + axis - the axis of the gyroscope to read
  + Returns:
    + x_val or y_val or z_val - the measured value

#### getAccel(self, axis) <a id="f_getAccel"></a>
  + Reads the specified axis of the accelerometer
  + Parameters:
    + axis - the axis of the accelerometer to read
  + Returns:
    + x_val or y_val or z_val - the measured value

#### setupIMU(self) <a id="f_setupIMU"></a>
  + Enables the IMU.  Requires config mode
  + Parameters:
    + none
  + Returns:
    + nothing

#### configurePWMBoards(self, mode) <a id="f_configurePWMBoards"></a>
  + Sets up Adafruit PWM boards for use with either motor controllers or servos
  + Parameters:
    + mode - the mode to set the PWM board to
  + Returns:
    + nothing

#### getPing(self, pin_num) <a id="f_getPing"></a>
  + Reads a ping sensor on the specified pin
  + Parameters:
    + pin_num - the pin on which the sensor is located
  + Returns:
    + distance - the output of the sensor

### attachStepper(self, pinStep, pinDir) <a id="f_attachStepper"></a>
  + Attaches a stepper motor driver on pinStep and pinDir
  + REQUIRES CONFIG MODE
  + Parameters:
    + pinStep - the pin connected to the step pin of the driver
    + pinDir - the pin connected to the direction pin of the driver
  + Returns:
    + nothing

### runStepper(self, steps) <a id="f_runStepper"></a>
  + Runs the stepper motor 'steps' steps.
  + This function is blocking.
  + Acceleration and Speed are set up for NEMA17 2.3A stepper motor, 1/2 stepping
  + 1/2 step = 0.9 degrees
  + Parameters:
    + steps - the number of steps to run
  + Returns:
    + nothing
    
## Constants <a id="constants"></a>
+ Pin Modes
  + OUTPUT
  + INPUT
  + INPUT_PULLUP
+ Digital States
  + HIGH
  + LOW
  + OFF
  + ON
+ Musical Notes
  + Format: NOTE_{note name}{sharp}{octave}
  + Example: NOTE_A4 (A4) NOTE_AS4 (A4 Sharp)

## Communication <a id="communication"></a>
General form of communication is call and response.  Pi sends command, terminated by a semicolon. Arduino responds with the result of the command, terminated by a semicolon.
As of this writing, there is no handshake between the Arduino and the Python script upon the opening of the serial port.
