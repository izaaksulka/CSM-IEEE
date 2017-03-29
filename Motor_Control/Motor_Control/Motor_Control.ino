//Declare pin functions on Arduino

#define REAR_E 11
#define FRONT_RIGHT_E 9
#define FRONT_LEFT_E 10

#define REAR_M 13
#define FRONT_RIGHT_M 8
#define FRONT_LEFT_M 12

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

  digitalWrite( EN, HIGH );

  Serial.begin(9600);
  Serial.print(1);
}

bool isRearDirCCW = true;
bool isFrontLDirCCW = true;
bool isFrontRDirCCW = true;

void loop() {

  if (Serial.available() > 0) {

    motorType = Serial.parseInt();

    if (motorType == HOLONOMIC) {

      /*
      int lastV = rearV;
      int lastfLV = frontLV;
      int lastfRV = frontRV;
      */
      
      int rearV   = Serial.parseInt();
      int frontLV = Serial.parseInt();
      int frontRV = Serial.parseInt();

      if( rearV == 0 && frontLV == 0 && frontRV == 0 ) {
        digitalWrite( REAR_M, !isRearDirCCW );
        digitalWrite(FRONT_LEFT_M, !isFrontLDirCCW);
        digitalWrite(FRONT_RIGHT_M, !isFrontRDirCCW);
        delay( 100 );
      }
      
      isRearDirCCW = rearV < 0;
      isFrontLDirCCW = frontLV < 0;
      isFrontRDirCCW = frontRV < 0;
      
      digitalWrite(REAR_M, isRearDirCCW);
      digitalWrite(FRONT_LEFT_M, isFrontLDirCCW);
      digitalWrite(FRONT_RIGHT_M, isFrontRDirCCW);

      analogWrite(REAR_E,       abs(rearV));
      analogWrite(FRONT_RIGHT_E, abs(frontLV));
      analogWrite(FRONT_LEFT_E, abs(frontRV));
    }
    else if (motorType == STEPPER) {

      int steps = Serial.parseInt();

      digitalWrite(dir, steps < 0);       //Pull direction pin low to move "forward"

      for (int x = 0; x < abs(steps); x++) { //Loop the forward stepping enough times for motion to be visible
        digitalWrite(stp, HIGH);        //Trigger one step forward
        delay(1);
        digitalWrite(stp, LOW);         //Pull step pin low so it can be triggered again
        delay(1);
      }
      resetBEDPins();
    }

    char findNewline;
    do {
      findNewline = Serial.read();
    } while ( findNewline != '\n' ); 
  }

}

//Reset Big Easy Driver pins to default states
void resetBEDPins() {
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(MS3, LOW);
  digitalWrite(EN, HIGH);
}
