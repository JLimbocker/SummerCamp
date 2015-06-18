# Python-Arduino class Firmware
---
This firmware serves as the interface between a Raspberry Pi running python and an Arduino microcontroller.  This firmware is designed to be run using its Arduino counterpart [link to Arduino counterpart].

## Compatible Commands
General form of communication is call and response.  Pi sends command, terminated by a semicolon. Arduino responds with the result of the command, terminated by a semicolon.

### Reads
+ analogRead(self, pin_num)
  + Reads the analog value from the specified pins
  + Returns:
    + int variable of the pin read

+ digitalRead(self, pin_num)
  + Reads the digital values from the specified pins
  + Returns:
    + int variable of the pin read

### Writes
+ analogWrite(self, pin_num, value)
  + Writes the specified analog value(s) to the given pin(s).  Analog Writes are limited to PWM capable pins.
  + Returns:
    + nothing
+ Digital Write
  + Writes the specified digital value(s) to the given pin(s).
  + Returns:
    + nothing

### PWM Device
+ Set Pulse Width
  +
  +
+ Set PWM freq
  +
  +
+ Attach (config mode)
  +  
  +


### Servo
+ servoWrite(self, pin_num, value)
  + Moves the servo to the specified position (value), between 0 and 180 degrees.
  + Returns:
    + nothing
+ **** servoWriteMicroseconds(self, pin_num, value)
  + Moves the servo to the specified position (value), between 0 and 180 degrees.
  + Returns:
    + nothing
+ attachServo(self,pin_num)   (config mode)
  + When in configuration mode, this function attaches an Adafruit PWM controller at the specified address.  Pin restrictions are handled by the Python interface.
  + Returns:
    + nothing


### Tone generation
  + tone(self, pin_num, frequency, duration)
    + Generates a beep for a piezo buzzer on the specified pin for the given duration in milliseconds.

    + Returns:
      + nothing
