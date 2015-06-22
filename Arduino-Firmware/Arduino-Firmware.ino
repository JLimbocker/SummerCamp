
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
#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>
#include <stdlib.h>



//Fingerprint Decs
SoftwareSerial fingerprintSerial(10, 11);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&fingerprintSerial);


//IMU Declarations
Adafruit_LSM303_Accel_Unified accel = Adafruit_LSM303_Accel_Unified(54321);
Adafruit_LSM303_Mag_Unified mag = Adafruit_LSM303_Mag_Unified(12345);
Adafruit_L3GD20_Unified gyro = Adafruit_L3GD20_Unified(20);
Adafruit_PWMServoDriver motor;
Adafruit_PWMServoDriver servo;



// Other Decs
String command;
String response;
int index, pin, value, id;
bool screenWritten = false;

LiquidCrystal lcd(12,11,5,4,3,2);

void setup()
{
  Serial.begin(115200);

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
      case 'y':
        readGyro();
        break;
      case 'c':
        readMag();
        break;
      case 'L':
        writeToScreen();
        break;
      case 'f':
        readFingerprint();
        break;
      case 'F':
        addFingerprint();
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
        case 'I':
          setupIMU();
          break;
        case 'f':
          setupFingerprint();
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

void readFingerprint()
{
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)
  {
    response = "f -1 0 ;";
    return;
  }

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)
  {
    response = "f -1 0 ;";
    return;
  }

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)
  {
    response = "f -1 0 ;";
    return;
  }

  response = "f " + String(finger.fingerID) + " " + String(finger.confidence) + " ;";
}

int addFingerprint()
{
  index = command.indexOf(' ');
  command = command.substring(index+1);

  index = command.indexOf(' ');
  id = command.substring(0, index).toInt();
  command = command.substring(index+1);
  int p = -1;
  Serial.println("Waiting for valid finger to enroll");
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image taken");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.println(".");
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      break;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("Imaging error");
      break;
    default:
      Serial.println("Unknown error");
      break;
    }
  }

  // OK success!

  p = finger.image2Tz(1);
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Could not find fingerprint features");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }

  Serial.println("Remove finger");
  delay(2000);
  p = 0;
  while (p != FINGERPRINT_NOFINGER) {
    p = finger.getImage();
  }

  p = -1;
  Serial.println("Place same finger again");
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image taken");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.print(".");
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      break;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("Imaging error");
      break;
    default:
      Serial.println("Unknown error");
      break;
    }
  }

  // OK success!

  p = finger.image2Tz(2);
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Could not find fingerprint features");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }


  // OK converted!
  p = finger.createModel();
  if (p == FINGERPRINT_OK) {
    Serial.println("Prints matched!");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_ENROLLMISMATCH) {
    Serial.println("Fingerprints did not match");
    return p;
  } else {
    Serial.println("Unknown error");
    return p;
  }

  Serial.print("ID "); Serial.println(id);
  //p = finger.storeModel(id);
  if (p == FINGERPRINT_OK) {
    Serial.println("Stored!");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_BADLOCATION) {
    Serial.println("Could not store in that location");
    return p;
  } else if (p == FINGERPRINT_FLASHERR) {
    Serial.println("Error writing to flash");
    return p;
  } else {
    Serial.println("Unknown error");
    return p;
  }
  //response = "F " + String(id) + " ;";
  /*Serial.flush();
  index = command.indexOf(' ');
  command = command.substring(index+1);

  index = command.indexOf(' ');
  id = command.substring(0, index).toInt();
  command = command.substring(index+1);

  int p = -1;
  //Hold until finger detected
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
  }
  Serial.println("Initial Read Success");
  // OK success!

  p = finger.image2Tz(1);
  switch (p) {
    case FINGERPRINT_OK:
      break;
    case FINGERPRINT_IMAGEMESS:
      response = "F -1 ;";
      return;
    case FINGERPRINT_PACKETRECIEVEERR:
      response = "F -1 ;";
      return;
    case FINGERPRINT_FEATUREFAIL:
      response = "F -1 ;";
      return;
    case FINGERPRINT_INVALIDIMAGE:
      response = "F -1 ;";
      return;
    default:
      response = "F -1 ;";
      return;
  }
  Serial.println("Initial Read Parsed");

  delay(2000);
  p = 0;
  Serial.println("Re-scan...");
  //Sense finger
  while (p != FINGERPRINT_NOFINGER) {
    p = finger.getImage();
  }
  //Clear and rescan
  p = -1;
  //Repeat Scan
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
  }
  Serial.println("Re-scan complete");
  // OK success!

  p = finger.image2Tz(2);
  switch (p) {
    case FINGERPRINT_OK:
      break;
    case FINGERPRINT_IMAGEMESS:
      response = "F -1 ;";
      return;
    case FINGERPRINT_PACKETRECIEVEERR:
      response = "F -1 ;";
      return;
    case FINGERPRINT_FEATUREFAIL:
      response = "F -1 ;";
      return;
    case FINGERPRINT_INVALIDIMAGE:
      response = "F -1 ;";
      return;
    default:
      response = "F -1 ;";
      return;
  }

  Serial.println("Re-scan converted");
  // OK converted!
  p = finger.createModel();
  Serial.println("Model Created");
  if (p == FINGERPRINT_OK) {
    //do nothing
  } else {
    Serial.println("Problem");
    response = "F -1 ;";
    return;
  }
  delay(500);
  Serial.println("Storing");
  //p = finger.storeModel(id);
  Serial.println("Stored");
  if (p == FINGERPRINT_OK) {
    response = String("F ") + String(id) + String(" ;");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Problem");
    response = "F -1 ;";
    return;
  } else if (p == FINGERPRINT_BADLOCATION) {
    Serial.println("Problem");
    response = "F -1 ;";
    return;
  } else if (p == FINGERPRINT_FLASHERR) {
    Serial.println("Problem");
    response = "F -1 ;";
    return;
  } else {
    Serial.println("Problem");
    response = "F -1 ;";
    return;
  }*/
  //Serial.println(response);
  Serial.println("Done");
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
void setupFingerprint()
{
  finger.begin(57600);
  if(finger.verifyPassword())
    response = "f 1 ;";
  else
    response = "f 0 ;";
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
