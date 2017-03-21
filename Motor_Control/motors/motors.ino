int rearE = 9, frontRightE = 10, frontLeftE = 11;
int rearM = 8, frontRightM = 12, frontLeftM = 13;
 
void setup() 
{ 
  pinMode(rearE, OUTPUT);
  pinMode(rearM, OUTPUT);

  pinMode(frontRightE, OUTPUT);
  pinMode(frontRightM, OUTPUT);

  pinMode(frontLeftE, OUTPUT);
  pinMode(frontLeftM, OUTPUT);

  
  Serial.begin(9600);
  while (! Serial);
  Serial.println("Speed 0 to 255");
} 
 
 
void loop() { 

  
  if (Serial.available()) {
    
    int speedRear = Serial.parseInt();

    Serial.println(speedRear);

    if (speedRear < 0){
      speedRear *= -1;
      digitalWrite(rearM, HIGH);
      digitalWrite(frontRightM, HIGH);
      digitalWrite(frontLeftM, HIGH);
     
      } else{
        digitalWrite(rearM, LOW);
      digitalWrite(frontRightM, LOW);
      digitalWrite(frontLeftM, LOW);
        }

 Serial.println(speedRear);
 Serial.println();

    
    analogWrite(rearE, speedRear);
    analogWrite(frontRightE, speedRear);
    analogWrite(frontLeftE, speedRear);
      
  }

  
} 
