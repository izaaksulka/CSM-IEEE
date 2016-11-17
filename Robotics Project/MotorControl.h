/*******************

Declaration of MotorControl class

This object gets instructions from Maze (the navigation module) and turns them into movement

*******************/

#pragma once
#include <iostream>
using namespace std;
class MotorControl{
public:
	//Moves the robot, use negative numbers for backwards
	void Move(double speed);
	//Rotates the robot.  Use positive for clockwise and negative for counter-clockwise
	void Rotate(double speed);
	//Cancels any instructions that are currently being executed
	void CancelAll();

    double forwardMotorSpeed;
    double rotatingSpeed;
private:
	//How exactly movement is calculated may change
	double wheelCircumference;




};