/**************

Implementation for the Core class

**************/
#include "Core.h"


Core::Core(){
	nav = Maze();
	motorControl = MotorControl();
}


void Core::Update() {
	cout << "Core::Update doesn't do anything" << endl;
}