# ArduPithon
---
This firmware serves as the interface between a Raspberry Pi running python and an Arduino microcontroller.  This firmware is designed to be run using its [Arduino counterpart](https://github.com/JLimbocker/SummerCamp/tree/master/Arduino-Firmware).

Written by Parker Holloway, Travis Siems, and Jeff Limbocker.
Summer 2015

## Functions
+ __init__(self)
  + Constructor for the Arduino Object.
+ open(self, port_name)
  + Opens a serial connection on the given port
  + Parameters:
    + port_name - the port on which to open the serial port
  + Returns:
    + nothing
+ close(self)
  + Closes the serial connection
  + Parameters:
    + none
  + Returns:
    + nothing
+ readUntil(self, file_obj, delim_char)
  + Reads from file_obj until delim_char
  + Parameters:
    + file_obj - the stream from which to read data
    + delim_char - the delimiting character
  + Returns:
    + string_read - the string read from the file
+ readUntil_file(self, file_obj, delim_char)
  + Appears to be a debug version of readUntil.
  + Parameters:
    + file_obj - the stream from which to read data
    + delim_char - the delimiting character
  + Returns:
    + string_read - the string read from the file
+ sendMsg(self, msg)
  + Sends msg over the serial connection
  + Parameters:
    + msg - the message to send
  + Returns:
    + nothing
+ recvMsg(self)
  + Receives a message over the serial connection.  Reads until the newline character
  + Parameters:
    + none  
  + Returns:
    + the received message
+ enterConfigMode(self)
  + Puts the Arduino into config mode
  + Parameters:
    + none
  + Returns:
    + nothing
+ exitConfigMode(self)
  + Takes the Arduino out of config mode
  + Parameters:
    + none
  + Returns:
    + none
+ analogWrite(self, pin_num, value)
  + Writes a PWM signal to the given pin
  + Parameters:
    + pin_num - the pin number to write to
    + value - the 8-bit PWM value
  + Returns:
    + nothing
+ analogRead(self, pin_num)
  + Reads the ADC value on the given analog pin
  + Parameters:
    + pin_num - the pin to read
  + Returns:
    + the analog input value from the specified pin
+ digitalWrite(self, pin_num, value)
  + Writes a digital value to the specified pin
  + Parameters:
    + pin_num - the pin to write to
    + value - the value to write
  + Returns:
    + nothing
+ digitalRead()
  + Reads a digital value from the specified pin
  + Parameters:
    + pin_num - the pin to read from
  + Returns:
    + the digital input value from the specified pin
+ pinMode(pin_num, value)
  + Sets the pin mode of the specified pin.  Must be used from config mode.
  + Parameters:
    + pin_num - the specified pin
    + value - the mode to set the pin to
  + Returns:
    + nothing
+ delay(self, seconds)
  + Delays for a specified time
  + Parameters:
    + seconds - the delay time
  + Returns:
    + nothing
+ tone(self, pin_num, value, duration)
  + Plays a tone on the given pin
  + Parameters:
    + pin_num - the pin to play the tone on
    + value - the frequency of the tone
    + duration - the duration of the tone
  + Returns:
    + nothing
+ readFingerprint(self)
  + SPECIAL FIRMWARE REQUIRED
  + This function requests a fingerprint scan from the Arduino
  + Parameters:
    + none  
  + Returns:
    + fingerID - the ID of the fingerprint, or -1 if no fingerprint found
+ writeToScreen(self, row_num, message)
  + Writes a message to the LCD screen
  + Parameters:
    + row_num - the row on which to write the message
    + message - the message to be writeToScreen
  + Returns:
    + nothing
+ servoWrite(self, pin_num, value)
  + Writes a position to the servo specified by pin_num
  + Parameters:
    + pin_num - the index of the servo on the Servo Controller board  
    + value - the position to write in degrees
  + Returns:
    + nothing
+ servoWriteMicroseconds(self, pin_num, value)
  + Writes a pulse width to the servo specified by pin_num
  + Parameters:
    + pin_num - the index of the servo
    + value - the pulse width in microseconds
  + Returns:
    + nothing
+ setPWM(self, pin_num, value)
  + Sets the PWM value for the specified channel on a PWM board
  + Parameters:
    + pin_num - the index of the pin on the PWM board
    + value - the 12-bit PWM value to write to the pin
  + Returns:
    + nothing
+ setVEX(self, pin_num, value)
  + Sets the PWM value for a VEX 29 motor driver
  + Parameters:
    + pin_num - the index of the motor driver on the PWM board
    + value - the pwm value
  + Returns:
    + nothing
+ setTalon(self, pin_num, value)
  + Sets the PWM value for a Talon motor driver
  + Parameters:
    + pin_num - the index of the motor driver on the PWM board
    + value - the pwm value
  + Returns:
    + nothing
+ getGyro(self, axis)
  + Reads the specified axis of the gyroscope
  + Parameters:
    + axis - the axis of the gyroscope to read
  + Returns:
    + x_val or y_val or z_val - the measured value
+ getAccel(self, axis)
  + Reads the specified axis of the accelerometer
  + Parameters:
    + axis - the axis of the accelerometer to read
  + Returns:
    + x_val or y_val or z_val - the measured value
+ setupIMU(self)
  + Enables the IMU.  Requires config mode
  + Parameters:
    + none
  + Returns:
    + nothing
+ configurePWMBoards(self, mode)
  + Sets up Adafruit PWM boards for use with either motor controllers or servos
  + Parameters:
    + mode - the mode to set the PWM board to
  + Returns:
    + nothing
+ getPing(self, pin_num)
  + Reads a ping sensor on the specified pin
  + Parameters:
    + pin_num - the pin on which the sensor is located
  + Returns:
    + distance - the output of the sensor

## Constants
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

## Communication
General form of communication is call and response.  Pi sends command, terminated by a semicolon. Arduino responds with the result of the command, terminated by a semicolon.
As of this writing, there is no handshake between the Arduino and the Python script upon the opening of the serial port.
