
/*
TO-DO:
servo/PWM driver
fingerprint sensor

*/
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_LSM303_U.h>
#include <Adafruit_L3GD20_U.h>
#include <Adafruit_PWMServoDriver.h>
#include <LiquidCrystal.h>
#include <SoftwareSerial.h>
#include <stdlib.h>
#include <AccelStepper.h>




//IMU Declarations
Adafruit_LSM303_Accel_Unified accel = Adafruit_LSM303_Accel_Unified(54321);
Adafruit_LSM303_Mag_Unified mag = Adafruit_LSM303_Mag_Unified(12345);
Adafruit_L3GD20_Unified gyro = Adafruit_L3GD20_Unified(20);
Adafruit_PWMServoDriver motor;
Adafruit_PWMServoDriver servo;
AccelStepper stepper;


// Other Decs
String command;
String response;
int index, pin, value, id;
bool screenWritten = false;
int rows[] = {5,4,3,2};
int columns[] = {9,8,7,6};
char charData[4][4] = {{'1', '4', '7', 'r'}, {'2', '5', '8', '0'}, {'3', '6', '9', 'd'}, {'c', 'p', 'b', 'e'}};

LiquidCrystal lcd(12,11,5,4,3,2);

void setup()
{
  Serial.begin(115200);
  Serial.println("*** ;");

}

void loop()
{

  if(Serial.available())
  {
    command = Serial.readStringUntil(';');
    switch(command[0])
    {

      case 'a':
        writeAnalogPin();
        break;
      case 'd':
        writeDigitalPin();
        break;
      case 'A':
        readAnalogPin();
        break;
      case 'D':
        readDigitalPin();
        break;
      case 'M':
        runDCMotor();
        break;
      case 'S':
        moveServo();
        break;
      case 't':
        generateTone();
        break;
      case 'T':
        getPing();
        break;
      case 'g':
        readAccel();
        break;
      case 'k':
        keypad();
        break;
      case 'y':
        readGyro();
        break;
      case 'c':
        readMag();
        break;
      case 'U':
        runStepper();
        break;
      case 'L':
        writeToScreen();
        break;
      case 'C':
        configure();
        break;
    }

  }
  if(response.length() > 1)
  {
    Serial.println(response);
    //Serial.flush();
    response = "";
  }
}

void configure()
{

  if(command[2] != '1')
    return;
  Serial.println("C 1 ;");
  //Serial.flush();
  while(true)
  {
    if(Serial.available())
    {
      command = Serial.readStringUntil(';');
      switch(command[0])
      {


        case 'P':
          setPinMode();
          break;
        case 'M':
          attachDCMotor();
          break;
        case 'S':
          attachServo();
          break;
        case 't':
          generateTone();
          break;
        case 'g':

          break;
        case 'U':
          attachStepper();
          break;
        case 'I':
          setupIMU();
          break;
        case 'C':
          if(command[2] == '0')
          {
            command = "";
            //Serial.flush();
            Serial.println("C 0 ;");
            return;
          }
          break;
      }

    }
    if(response.length() > 1)
    {
      Serial.println(response);
      //Serial.flush();
      response = "";
    }
  }
}

<<<<<<< Updated upstream
String readKeypad(){
  for(int i = 0; i <= 3; i++){
    pinMode(columns[i], OUTPUT);
  }
  String message;
  char pButtonVal = 0;
  char lastCharWritten = 0;
  char buttonVal = 0;
  buttonVal = getCharacter();
  while(true){
    while(buttonVal == 0){
      buttonVal = getCharacter();
      pButtonVal = 0;
    }
    while(buttonVal == 'e'){
      buttonVal = getCharacter();
      if(buttonVal != 'e')
        return message;
    }
    if(buttonVal != pButtonVal){
      message += buttonVal;
      //Serial.println(message);
    }
    buttonVal = getCharacter();
    //Serial.println(buttonVal);
    pButtonVal = buttonVal;
  }
}

char getCharacter(){
  int iVal = 0;
  int jVal = 0;
  int returnChar = 0;
  for(int i = 0; i <= 3; i++){
    digitalWrite(columns[i], HIGH);
    //Serial.print("Column: ");
    //Serial.print(i);
    for(int j = 0; j <= 3; j++){
      //Serial.print(" Row: ");
      //Serial.print(j);
      int pinValue = analogRead(rows[j]);
      //Serial.print("  pinValue: ");
      //Serial.println(pinValue);
      if(pinValue >= 500){
        iVal = i+1;
        jVal = j+1;
        break;
      }
      //delay(10);
    }
    digitalWrite(columns[i], LOW);
  }
  if(iVal == 0 && jVal == 0)
    returnChar = 0;
  else
    returnChar = charData[iVal-1][jVal-1];
  //Serial.println(returnChar);
  return returnChar;
}
void attachStepper()
{
  index = command.indexOf(' ');
  command = command.substring(index+1);
  command.trim();
  index = command.indexOf(' ');
  int pinStep = command.substring(0, index).toInt();
  command = command.substring(index+1);
  command.trim();
  index = command.indexOf(' ');
  int pinDir = command.substring(0, index).toInt();

  stepper = AccelStepper(1, pinStep, pinDir);

  stepper.setMaxSpeed(2400);
  stepper.setAcceleration(600);
  response = "U " + String(pinStep) + " " + String(pinDir) + " ;";
}

void runStepper()
{
  index = command.indexOf(' ');
  command = command.substring(index+1);
  command.trim();
  index = command.indexOf(' ');
  int steps = command.substring(0, index).toInt();

  stepper.move(steps);
  while(stepper.distanceToGo())
    stepper.run();
  response = "U " + String(steps) + " ;";
>>>>>>> Stashed changes
}

void getPing(){
  response = "T ";
  while(command.length() > 1)
  {
    index = command.indexOf(' ');
    command = command.substring(index+1);
    command.trim();
    index = command.indexOf(' ');
    pin = command.substring(0, index).toInt();

    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
    delayMicroseconds(2);
    digitalWrite(pin, HIGH);
    delayMicroseconds(5);
    digitalWrite(pin, LOW);
    pinMode(pin, INPUT);
    long duration = pulseIn(pin, HIGH);

    duration = duration / 74 / 2;
  response += String(duration) + " ";

  }
  response += ";";
}

void readAnalogPin()
{
  response = "A ";
  while(command.length() > 1)
  {
    index = command.indexOf(' ');
    command = command.substring(index+1);
    command.trim();
    index = command.indexOf(' ');
    pin = command.substring(0, index).toInt();
    response += String(analogRead(pin)) + " ";

  }
  response += ";";
}

void keypad()
{
  response = "k ";
  response += readKeypad();
  response += " ;";
}

void writeToScreen()
{
  if(!screenWritten){
    lcd.begin(16, 2);
    screenWritten = true;
  }
  response = "L ";
  index = command.indexOf(' ');
  command = command.substring(index+1);
  command.trim();
  index = command.indexOf(' ');
  int line = command.substring(0, index).toInt();

  if(line == 2)
  {
    lcd.begin(16,2);
    response += "cleared ;";
    return;
  }
  lcd.setCursor(0,line);

  index = command.indexOf(' ');
  command = command.substring(index+1, command.length());
  command.trim();

  lcd.print(command);

  int stringLen = command.length();
  if(stringLen > 16)
    delay(1000);
  while(stringLen > 16){
    lcd.scrollDisplayLeft();
    delay(200);
    stringLen--;
  }

  response += command + " ;";
}

void readDigitalPin()
{
  response = "D ";
  while(command.length() > 1)
  {
    index = command.indexOf(' ');
    command = command.substring(index+1);
    command.trim();
    index = command.indexOf(' ');
    pin = command.substring(0, index).toInt();
    response += digitalRead(pin) + String(" ");
  }
  response += ";";
}

void writeAnalogPin()
{
  response = "a ";
  index = command.indexOf(' ');
  command = command.substring(index+1);
  while(command.length() > 1)
  {
    //command.trim();
    index = command.indexOf(' ');
    pin = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //command.trim();
    index = command.indexOf(' ');
    value = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //command.trim();
    analogWrite(pin, value);
    response += String(pin) + String(" ") + String(value) + String(" ");
  }
  response += ";";
}

void writeDigitalPin()
{
  response = "d ";
  //Serial.print("d ");
  index = command.indexOf(' ');
  command = command.substring(index+1);
  while(command.length() > 1)
  {

    //command.trim();
    index = command.indexOf(' ');
    pin = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //command.trim();
    index = command.indexOf(' ');
    value = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //command.trim();
    digitalWrite(pin, value);
    response += String(pin) + String(" ") + String(value) + String(" ");
  }
  response += ";";
}

void runDCMotor()
{
  int motorNum;
  int pulseWidth;
  response = "M " ;

  index = command.indexOf(' ');
  command = command.substring(index+1);

  index = command.indexOf(' ');
  motorNum = command.substring(0, index).toInt();
  command = command.substring(index+1);

  index = command.indexOf(' ');
  pulseWidth = command.substring(0, index).toInt();
  command = command.substring(index+1);

  motor.setPWM(motorNum, 0, pulseWidth);

  response += String(motorNum) + " " + String(pulseWidth) + " ;";
}

void moveServo()
{
  int servoNum;
  int pulseWidth;
  response = "S " ;

  index = command.indexOf(' ');
  command = command.substring(index+1);

  index = command.indexOf(' ');
  servoNum = command.substring(0, index).toInt();
  command = command.substring(index+1);

  index = command.indexOf(' ');
  pulseWidth = command.substring(0, index).toInt();
  command = command.substring(index+1);

  servo.setPWM(servoNum, 0, pulseWidth);

  response += String(servoNum) + " " + String(pulseWidth) + " ;";
}

void readAccel()
{
  sensors_event_t event;
  accel.getEvent(&event);
  response = "g " + String(event.acceleration.x) + " " + String(event.acceleration.y) + " " + String(event.acceleration.z) + " ;";
  command = "";
}

void readGyro()
{
  sensors_event_t event;
  gyro.getEvent(&event);
  response = "y " + String(event.gyro.x) + " " + String(event.gyro.y) + " " + String(event.gyro.z) + " ;";
  command = "";
}

void readMag()
{
  sensors_event_t event;
  mag.getEvent(&event);
  response = "c " + String(event.magnetic.x) + " " + String(event.magnetic.y) + " " + String(event.magnetic.z) + " ;";
  command = "";
}

void attachDCMotor()
{
  int address;
  int type;
  char** endptr;
  response = "M " ;
  index = command.indexOf(' ');
  command = command.substring(index+1);
  index = command.indexOf(' ');
  address = strtoul(command.substring(0, index).c_str(), endptr, 16);
  command = command.substring(index+1);
  index = command.indexOf(' ');
  type = command.substring(0, index).toInt();
  command = command.substring(index+1);
  motor = Adafruit_PWMServoDriver(address);
  motor.begin();
  if(type == 1)
    motor.setPWMFreq(50);
  else
    motor.setPWMFreq(333);
  response += String(address, HEX) + " " + String(type) + " ;";
}

void attachServo()
{
  int address;
  int type;
  char** endptr;
  index = command.indexOf(' ');
  command = command.substring(index+1);
  index = command.indexOf(' ');
  address = strtoul(command.substring(0, index).c_str(), endptr, 16);

  command = command.substring(index+1);
  servo = Adafruit_PWMServoDriver(address);
  servo.begin();
  servo.setPWMFreq(50);

  response = "S " + String(address, HEX) + " ;";
}

void setPinMode()
{
  response = "P " ;
  index = command.indexOf(' ');
  command = command.substring(index+1);
  //Serial.print("P ");
  while(command.length() > 1)
  {


    index = command.indexOf(' ');
    pin = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //Serial.print(pin);

    index = command.indexOf(' ');
    value = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //Serial.print(value);

    //command.trim();
    if(value == 1)
    {
      pinMode(pin, INPUT);
    }
    else if(value == 2)
    {
      pinMode(pin, INPUT_PULLUP);
    }
    else
    {
      pinMode(pin, OUTPUT);
    }

    response += String(pin) + String(" ") + String(value) + String(" ");

    break;
  }
  response += ";";

}

void generateTone()
{
  response = "t ";

  index = command.indexOf(' ');
  command = command.substring(index+1);

  while(command.length() > 1)
  {

    //command.trim();
    index = command.indexOf(' ');
    pin = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //command.trim();
    index = command.indexOf(' ');
    value = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //command.trim();
    index = command.indexOf(' ');
    int duration = command.substring(0, index).toInt();
    command = command.substring(index+1);

    tone(pin, value, duration);

    delay(duration*1.3);
    noTone(pin);

    response += String(pin) + String(" ") + String(value) + String(" ") + String(duration) + String(" ");
  }
  response += ";";

}

void setupIMU()
{
  int accInit = 1;
  int gyrInit = 1;
  int magInit = 1;
  if(!accel.begin())
  {
    /* There was a problem detecting the ADXL345 ... check your connections */
    accInit = 0;
  }
  if(!mag.begin())
  {
    /* There was a problem detecting the LSM303 ... check your connections */
    magInit = 0;
  }
  gyro.enableAutoRange(true);
  /* Initialise the sensor */
  if(!gyro.begin())
  {
    /* There was a problem detecting the L3GD20 ... check your connections */
    gyrInit = 0;
  }
  response = "I " + String(accInit) + " " + String(magInit) + " " + String(gyrInit) + " ;";

}
