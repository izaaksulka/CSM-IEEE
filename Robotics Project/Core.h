/************
This one 


*************/

#pragma once
#include "MotorControl.h"
#include "Maze.h"

using namespace std;


class Core {
public:
	Core();
	void Update();


private:
	Maze nav;
	MotorControl motorControl;

};