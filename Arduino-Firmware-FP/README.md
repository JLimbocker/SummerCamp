# Arduino-Python interface firmware - Fingerprint Scanner Edition
---
This firmware serves as the interface between an Arduino microcontroller and a Raspberry Pi running python.  This firmware is designed to be run using its Python counterpart [link to Python counterpart].

## Compatible Commands
General form of communication is call and response.  Pi sends command, terminated by a semicolon. Arduino responds with the result of the command, terminated by a semicolon.

### Reads
+ Analog Read
  + Reads the analog value from the specified pins
  + `A {pin number} ;`
  + `A {pin number} {pin number} ... ;`
  + Returns:
    + `A {value} ;`
    + `A {value} {value} ... ;`
+ Digital Read
  + Reads the digital values from the specified pins
  + `D {pin number} ;`
  + `D {pin number} {pin number} ... ;`
  + Returns:
    + `D {value} ;`
    + `D {value} {value} ... ;`

### Writes
+ Analog Write
  + Writes the specified analog value(s) to the given pin(s).  Analog Writes are limited to PWM capable pins.
  + `a {pin number} {value} ;`
  + `a {pin number} {value} {pin number} {value} ... ;`
  + Returns:
    + `a {pin number} {value} ;`
    + `a {pin number} {value} {pin number} {value} ... ;`
+ Digital Write
  + Writes the specified digital value(s) to the given pin(s).
  + `d {pin number} {value} ;`
  + `d {pin number} {value} {pin number} {value} ... ;`
  + Returns:
    + `d {pin number} {value} ;`
    + `d {pin number} {value} {pin number} {value} ... ;`
### Tone generation
  + Generates a beep for a piezo buzzer on the specified pin for the given duration.
  + `t {pin number} {duration} ;`
  + Returns:
    + `t {pin number} {duration} ;`
### Configuration mode
+ Enter
  + `C 1 ;`
  + Returns:
    + `C 1 ;`
+ Exit
  + `C 0 ;`
  + Returns:
    + `C 0 ;`
+ Set pin mode
  + Sets the output mode of the specified pin
  + `P {pin number} {mode} ;`
  + Returns:
    + `P {pin number} {mode} ;`
