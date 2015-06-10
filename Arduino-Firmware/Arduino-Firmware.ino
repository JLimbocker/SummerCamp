/*
TO-DO:
servo/PWM driver
fingerprint sensor
IMU

*/
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_LSM303_U.h>
#include <Adafruit_L3GD20_U.h>

//IMU Declarations
Adafruit_LSM303_Accel_Unified accel = Adafruit_LSM303_Accel_Unified(54321);
Adafruit_LSM303_Mag_Unified mag = Adafruit_LSM303_Mag_Unified(12345);
Adafruit_L3GD20_Unified gyro = Adafruit_L3GD20_Unified(20);

// Other Decs
String command;
String response;
int index, pin, value;

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
        //generateTone();
        break;
      case 'g':
        readAccel();
        break;
      case 'C':
        configure();
        break;
    }

  }
  if(response.length() > 1)
  {
    Serial.println(response);
    Serial.flush();
    response = "";
  }
}

void configure()
{

  if(command[2] != '1')
    return;
  Serial.println("C 1 ;");
  Serial.flush();
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
          //generateTone();
          break;
        case 'g':

          break;
        case 'I':
          setupIMU();
          break;
        case 'C':
          if(command[2] == '0')
          {
            command = "";
            Serial.flush();
            Serial.println("C 0 ;");
            return;
          }
          break;
      }

    }
    if(response.length() > 1)
    {
      Serial.println(response);
      Serial.flush();
      response = "";
    }
  }
}

void readAnalogPin()
{
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
  response += ";";
}

void moveServo()
{
  response += ";";
}

void readAccel()
{
  sensors_event_t event;
  accel.getEvent(&event);
  response = "g " + String(event.acceleration.x) + " " + String(event.acceleration.y) + " " + String(event.acceleration.z) + " ;";
  command = "";
}



void attachDCMotor()
{
  response += "M ;";
}

void attachServo()
{
  response += "S ;";
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
