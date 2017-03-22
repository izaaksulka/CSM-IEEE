const int REAR_E = 9, FRONT_RIGHT_E = 10, FRONT_LEFT_E = 11;
const int REAR_M = 8, FRONT_RIGHT_M = 12, FRONT_LEFT_M = 13;
 
void setup() 
{ 
  pinMode(REAR_E, OUTPUT);
  pinMode(REAR_M, OUTPUT);

  pinMode(FRONT_RIGHT_E, OUTPUT);
  pinMode(FRONT_RIGHT_M, OUTPUT);

  pinMode(FRONT_LEFT_E, OUTPUT);
  pinMode(FRONT_LEFT_M, OUTPUT);

  
  Serial.begin(9600);
  while (! Serial);
  Serial.println("Speed 0 to 255");
} 
 

void loop() {

  
  if (Serial.available() > 0) {

    // Tells the program which set of motors to set
    int motorSet = Serial.parseInt();
    
    int forwardV = Serial.parseInt();
    int sidewaysV = Serial.parseInt();
    int rotationalV = Serial.parseInt();
    
    int speedRear = Serial.parseInt();

    // TODO: Implement vector math
    // TODO: Implement holonomic math
    Serial.println(speedRear);
    
    if (speedRear < 0){
      speedRear *= -1;
      digitalWrite(REAR_M, HIGH);
      digitalWrite(FRONT_RIGHT_M, HIGH);
      digitalWrite(FRONT_LEFT_M, HIGH);
      
    } else{
      digitalWrite(REAR_M, LOW);
      digitalWrite(FRONT_RIGHT_M, LOW);
      digitalWrite(FRONT_LEFT_M, LOW);
    }
    
    Serial.println(speedRear);
    Serial.println();
    
    
    analogWrite(REAR_E, speedRear);
    analogWrite(FRONT_RIGHT_E, speedRear);
    analogWrite(FRONT_LEFT_E, speedRear);
      
  }

}
