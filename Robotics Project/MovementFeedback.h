/******************************
This class reads the encoder or whatever that tells us how far the robot has moved.
******************************/
#pragma once
#include <iostream>
#include "Vector2.h"
#include "MotorControl.h"
#include <ctime>
using namespace std;

class MovementData {
public:
    MovementData();
    MovementData(double newMovement, double newRotation);
	double movement;
	//counterclockwise is positive - radians
	double rotation;
};

class MovementFeedback{
public:
	MovementFeedback();
	MovementFeedback(MotorControl *mc); //Currently this requires a motor control because I'm going to use it to simulate feedback.  In the future may not need this
    MovementData Report();


private:
	MotorControl *mc;
    clock_t lastReport;

};