# Arduino-Python interface firmware
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
+ Move
  + Moves the servo to the specified position, between 0 and 180 degrees.
  + `S {servo id} {position} ;`
  + Returns:
    + `S {servo id} {position} ;`
+ Attach (config mode)
  + When in configuration mode, this function attaches a servo to the specified pin.  Pin restrictions are handled by the Python interface.
  + `S {servo id} {pin number} ;`
  + Returns:
    + `S {servo id} {pin number} ;`

### Motor
+ Move
  + Moves the DC Motor at the given speed.  Positive speeds are forward, negative speeds are reverse.
  + `M {motor id} {speed} ;`
  + Returns:
    + `M {motor id} {speed} ;`

+ Attach (config mode)
  + When in configuration mode, this function attaches a motor to the specified pin.  Pin restrictions are handled by the Python interface.
  + `M {motor id} {pin number} ;`
  + Returns:
    + `M {motor id} {pin number} ;`

### Tone generation
  + Generates a beep for a piezo buzzer on the specified pin for the given duration.
  + `t {pin number} {duration} ;`
  + Returns:
    + `t {pin number} {duration} ;`

### Accelerometer
  + Gets a reading from the accelerometer.
  + `g ;`
  + Returns:
    + `g {x-acc} {y-acc} {z-acc} ;`

### Compass
  + Gets a reading from the Compass.
  + `c ;`
  + Returns:
    + `c {x-mag} {y-mag} {z-mag} ;`

### Gyroscope
  + Gets a reading from the gyro.
  + `y ;`
  + Returns:
    + `y {x-gyro} {y-gyro} {z-gyro} ;`

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
+ Attach Motor
  + `M {motor id} {pin number} ;`
  + Returns:
    + `M {motor id} {pin number} ;`
+ Attach Servo
  + `S {servo id} {pin number} ;`
  + Returns:
    + `S {servo id} {pin number} ;`
+ Setup IMU
  + 'I ;'
  + Returns:
    + 'I {accel success} {mag success} {gyro success} ;'
