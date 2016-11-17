/*******************

Implementation for MotorControl class

*******************/

#include "MotorControl.h"

void MotorControl::Move(double speed) {
	//Move the robot
	//I don't know how to do motors yet but that goes here
    forwardMotorSpeed = speed;
    //
    //Start the motor

    //
}

void MotorControl::Rotate(double speed) {
	//Rotate the robot
	//I don't know how to do motors yet but that goes here
    rotatingSpeed = speed;
}

void MotorControl::CancelAll() {
	cout << "MotorControl::CancelAll()" << endl;
    forwardMotorSpeed = 0;
    rotatingSpeed = 0;
    /*
    Here there is stuff that stops the motor
    
    
    */
}

