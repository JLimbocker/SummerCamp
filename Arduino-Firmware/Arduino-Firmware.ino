String command;
String response;
int index, pin, value;

void setup()
{
  Serial.begin(9600);
  
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
        //readAccelerometer();
        break;
      case 'C':
        configure();
        break;
    }

  }
  if(response.length() > 1)
  {
    Serial.println(response);
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


        case 'A':
          setPinMode();
          break;
        case 'D':
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
          //readAccelerometer();
          break;
        case 'C':
          Serial.print("C ");
          if(command[2] == '0')
          {
            command = "";
            Serial.flush();
            Serial.println("0 ;");
            return;
          }
          break;
      }

    }
    if(response.length() > 1)
    {
      Serial.println(response);
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
  while(command.length() > 1)
  {


    index = command.indexOf(' ');
    pin = command.substring(0, index).toInt();
    command = command.substring(index+1);

    index = command.indexOf(' ');
    value = command.substring(0, index).toInt();
    command = command.substring(index+1);
    //command.trim();
    if(value == 1)
    {
      pinMode(pin, OUTPUT);
    }
    else
    {
      pinMode(pin, INPUT);
    }
    response += String(pin) + String(" ") + String(value) + String(" ");
  }
  response += ";";

}
