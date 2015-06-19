/***************************************************
  This is an example sketch for our optical Fingerprint sensor

  Designed specifically to work with the Adafruit BMP085 Breakout
  ----> http://www.adafruit.com/products/751

  These displays use TTL Serial to communicate, 2 pins are required to
  interface
  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>

uint8_t getFingerprintEnroll(int id);


// pin #2 is IN from sensor (GREEN wire)
// pin #3 is OUT from arduino  (WHITE wire)
SoftwareSerial mySerial(10, 11);

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

void setup()
{
  Serial.begin(9600);

  //Serial.println("fingertest");

  // set the data rate for the sensor serial port
  finger.begin(57600);

  if (finger.verifyPassword()) {
    //Serial.println("Found fingerprint sensor!");
  } else {
    //Serial.println("Did not find fingerprint sensor :(");
    while (1);
  }
}

void loop()                     // run over and over again
{
  while(!Serial.available());
  String input = Serial.readStringUntil(';');
  if(input.charAt(0) == 'f')
  {  
  
    //Serial.println("Scan Finger");
    checkFingerprint();
   
    //Serial.println("Finger Scanned");
  }
  

}



int checkFingerprint()
{
  while(1)
  {
    int result = getFingerprintIDez();
    delay(50);
    //Serial.println(result);
    if (result !=  -1)
      break;
  }
  return FINGERPRINT_OK;
}



// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)  return -1;

  // found a match!
  Serial.print("f "); Serial.print(finger.fingerID);  Serial.print(" "); Serial.print(finger.confidence); Serial.println(" ;");
  //response = "f " + String(finger.fingerID) + " " + String(finger.confidence) + " ;";
  return p;
}
