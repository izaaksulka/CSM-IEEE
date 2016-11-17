/**************

Implementation for the Core class

**************/
#include "Core.h"


Core::Core(){
    printDelay = 1 * CLOCKS_PER_SEC;  //Set the delay to 1 second
    printAt = clock() + printDelay;
   // nav = Maze();
	//motorControl = MotorControl();
	moveFeedback = MovementFeedback(&motorControl);
}


void Core::Update() {
	//cout << "Core::Update doesn't do anything except this print" << endl;
    nav.Update(moveFeedback.Report(), &motorControl);



    //Every period of printDelay print the maze
    if (clock() > printAt) {
        nav.Print(cout);
        printAt += printDelay;
    }
}