//Declare pin functions on Arduino

#define REAR_E 9
#define FRONT_RIGHT_E 10
#define FRONT_LEFT_E 11

#define REAR_M 8
#define FRONT_RIGHT_M 12
#define FRONT_LEFT_M 13

#define stp 2
#define dir 3
#define MS1 4
#define MS2 5
#define MS3 6
#define EN  7

//Declare variables for functions
int motorType;
enum motorType {STEPPER, HOLONOMIC};

void setup() 
{ 
  pinMode(REAR_E, OUTPUT);
  pinMode(REAR_M, OUTPUT);

  pinMode(FRONT_RIGHT_E, OUTPUT);
  pinMode(FRONT_RIGHT_M, OUTPUT);

  pinMode(FRONT_LEFT_E, OUTPUT);
  pinMode(FRONT_LEFT_M, OUTPUT);

  pinMode(stp, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  pinMode(MS3, OUTPUT);
  pinMode(EN, OUTPUT);
  resetBEDPins(); //Set step, direction, microstep and enable pins to default states

  Serial.begin(9600);
  Serial.print(1);
} 
 

void loop() {

  
    if (Serial.available() > 0) {

        motorType = Serial.parseInt();


        if (motorType == HOLONOMIC){

    
            int rearV   = Serial.parseInt();
            int frontLV = Serial.parseInt();
            int frontRV = Serial.parseInt();
    
            digitalWrite(REAR_M, rearV < 0);
            digitalWrite(FRONT_LEFT_M, frontLV < 0);           
            digitalWrite(FRONT_RIGHT_M, frontRV < 0);

            analogWrite(REAR_E,       abs(rearV));
            analogWrite(FRONT_RIGHT_E,abs(frontLV));
            analogWrite(FRONT_LEFT_E, abs(frontRV));
        }
        else if (motorType == STEPPER){

	    int steps = Serial.parseInt();

            digitalWrite(dir, steps < 0);       //Pull direction pin low to move "forward"
  		
	    for(int x= 0; x< abs(steps); x++){  //Loop the forward stepping enough times for motion to be visible
    		digitalWrite(stp,HIGH);         //Trigger one step forward
    		delay(1);
    		digitalWrite(stp,LOW);          //Pull step pin low so it can be triggered again
    		delay(1);
  }
        }
    }

}

//Reset Big Easy Driver pins to default states
void resetBEDPins(){
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(MS3, LOW);
  digitalWrite(EN, HIGH);
}
