/*******************

Declaration of MotorControl class

This object gets instructions from Maze (the navigation module) and turns them into movement

*******************/

#pragma once

class MotorControl{
public:
	//Moves the robot, use negative numbers for backwards
	void Move(double distance);
	//Rotates the robot.  Use positive for clockwise and negative for counter-clockwise
	void Rotate(double angle);

	



private:





};