/************
This one is the main control for the robot.  It has all the modules and main calls update on
it to make it recheck it's state and decide if something new needs to happen


*************/

#pragma once
#include "MotorControl.h"
#include "Maze.h"
#include "MovementFeedback.h"
#include <ctime>
using namespace std;


class Core {
public:
	//Setup is required for this class
	Core();
	void Update();


private:
    clock_t printDelay;
    clock_t printAt;
	Maze nav;
	MotorControl motorControl;
	MovementFeedback moveFeedback;
};