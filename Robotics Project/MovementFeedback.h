/******************************
This class reads the encoder or whatever that tells us how far the robot has moved



******************************/
#include <iostream>
#include "Vector2.h"
#include "MotorControl.h"
using namespace std;

class MovementData {
public:
	Vector2 movement;
	//Clockwise is positive - radians
	double rotation;
};

#pragma once
class MovementFeedback{
public:
	MovementFeedback();
	MovementFeedback(MotorControl *mc); //Currently this requires a motor control because i'm going to use it to simulate feedback.  In the future may not need this
	MovementData Report();



private:
	MotorControl *mc;


};