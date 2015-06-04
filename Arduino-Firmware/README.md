# Arduino-Python interface firmware
---
This firmware serves as the interface between an Arduino microcontroller and a Raspberry Pi running python.  This firmware is designed to be run using its Python counterpart [link to Python counterpart].

## Compatible Commands

### Reads
+ Analog Read
  + Reads the analog value from the specified pins
  + `A {pin number}`
  + `A {pin number} {pin number} ...`
+ Digital Read
  + Reads the digital values from the specified pins
  + `D {pin number}`
  + `D {pin number} {pin number} ...`

### Writes
+ Analog Write
  + Writes the specified analog value(s) to the given pin(s).  Analog Writes are limited to PWM capable pins.
  + `a {pin number} {value}`
  + `a {pin number} {value} {pin number} {value} ...`
+ Digital Write
  + Writes the specified digital value(s) to the given pin(s).
  + `d {pin number} {value}`
  + `d {pin number} {value} {pin number} {value} ...`

### Servo
+ Move
  + Moves the servo to the specified position, between 0 and 180 degrees.
  + `S {servo id} {position}`
+ Attach (config mode)
  + When in configuration mode, this function attaches a servo to the specified pin.  Pin restrictions are handled by the Python interface.
  + `S {servo id} {pin number}`

### Motor
+ Move
  + Moves the DC Motor at the given speed.  Positive speeds are forward, negative speeds are reverse.
  + `M {motor id} {speed}`
+ Attach (config mode)
  + When in configuration mode, this function attaches a motor to the specified pin.  Pin restrictions are handled by the Python interface.
  + `M {motor id} {pin number}`

### Tone generation
  + Generates a beep for a piezo buzzer on the specified pin for the given duration.
  + `t {pin number} {duration}`

### Accelerometer
  + Gets a reading from the accelerometer.
  + `g`

### Configuration mode
+ Enter
  + `C 1`
+ Exit
  + `C 2`
+ Set pin mode
  + Sets the output mode of the specified pin
  + `P {pin number} {mode}`
+ Attach Motor
  + `M {motor id} {pin number}`
+ Attach Servo
  + `S {servo id} {pin number}`
