# Arduino-Python interface firmware
---
This firmware serves as the interface between an Arduino microcontroller and a Raspberry Pi running python.  This firmware is designed to be run using its Python counterpart [link to Python counterpart].

## Compatible Commands

### Reads
+ #### Analog Read
`A {pin number}`
+ #### Digital Read
`D {pin number}`
### Writes
+ #### Analog Write
`a {pin number} {value}`
+ #### Digital Write
`d {pin number} {value}`
### Servo
+ #### Move
`S {servo id} {position}`
+ #### Attach (config mode)
`S {servo id} {pin number}`
### Motor
+ #### Move
`M {motor id} {speed}`
+ #### Attach (config mode)
`M {motor id} {pin number}`
### Tone generation
't {pin number} {duration}'
### Configuration mode
+ #### Enter
`C 1`
+ #### Exit
`C 2`
+ #### Set pin mode
`P {pin number} {mode}`
+ #### Attach Motor
`M {motor id} {pin number}`
+ #### Attach Servo
`S {servo id} {pin number}`
