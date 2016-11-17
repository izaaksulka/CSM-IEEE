


#include "MovementFeedback.h"

MovementFeedback::MovementFeedback() {
	mc = NULL;
    lastReport = clock();
}

MovementFeedback::MovementFeedback(MotorControl *nmc) {
	mc = nmc;
    lastReport = clock();
}

MovementData MovementFeedback::Report() {
    if (mc == NULL) {
        cout << "MovementFeedback currently requires a pointer to a MotorController because it's not getting its data from real sensors yet.  mc == NULL.  Returning blank MovementData." << endl;
        return MovementData();
    }
    //Here is where the part that senses if the robot is moving goes.  Right now it's just copying data from the motor controllers for testing purposes
    ////////
    


    ////////
    clock_t elapsedTime
	return MovementData(mc->forwardMotorSpeed, mc->rotatingSpeed);
}


MovementData::MovementData() {
    rotation = 0.0;
    movement = 0.0;
}

MovementData::MovementData(double newMovement, double newRotation) {
    movement = newMovement;
    rotation = newRotation;
}
