/**********************************

Author: Izaak Sulka

Implementation for the Maze class, which stores data about the maze and has functions that work with it like "GetPath(from, to)"

**********************************/
#include "maze.h"

Maze::Maze() {
    //Do whatever needs to be done in this initialization
	height = 7;
	width = 3;
	tileHeight = 1.0;
	tileWidth = 1.0;
	position = Vector2(0.5, height * tileHeight - tileHeight / 2.0);
    rotation = 0;
    actionType = ActionTypes::none;
	//Set up the Tile array
	map = new Tile*[width];
	int k = 0;
	for (int i = 0; i < width; i++) {
		map[i] = new Tile[height];
		for (int ii = 0; ii < height; ii++) {
			map[i][ii] = Tile(i, ii);
			//map[i][ii].SetType(k);  //This line is just for testing if the array is being stored correctly
			//k++;
		}
	}
    cout << "Printing at end of constructor:" << endl;
    Print(cout);
}

Maze::~Maze() {
	for (int i = 0; i < width; i++) {
		delete[] map[i];
	}
	delete[] map;
}

void Maze::Print(ostream& out) {
    cout << "--------------------------------------------------------" << endl;
	for (int ii = 0; ii < height; ii++) {
		for (int i = 0; i < width; i++) {
			map[i][ii].Print(out);
		}
		out << endl;
	}
    cout << "--------------------------------------------------------" << endl;
}


Point Maze::CurrentTilePoint() {
	//Havn't tested this yet
	return Point(position.x / tileWidth, position.y / tileHeight);
}

Tile* Maze::CurrentTile() {
	Point cp = CurrentTilePoint();
	return map[cp.GetY(), cp.GetX()];
}

void Maze::Update(const MovementData &movementData, MotorControl* motorControl) {
    cout << "MovementData : distance = " << movementData.movement << "    rotation = " << movementData.rotation << endl;;
    switch (actionType) {
    case ActionTypes::none:
        cout << "In \"none\" mode of update switch" << endl;
        //If the robot's not doing anything, figure out what to do and do it
        Solve(motorControl);
        break;
    case ActionTypes::move:
        cout << "In move mode of Update switch" << endl;
        position += FacingVector() * movementData.movement;
        //For now im just setting places i've been to 1 so i can see that i've been there
        CurrentTile()->SetType(1);
        //To check if the robot just moved past its destination, we can use a dot product between the direction its facing and the direction to where it wants to go.
        //Note that this is only checking if we go past the point by driving in the direction the robot is traveling
        if (FacingVector().Dot(targetPosition - position) <= 0) {
            CancelAll(motorControl);
        }
        break;
    case ActionTypes::rotate:
        rotation += movementData.rotation;
        //This is the same as the dot product above, but with one dimensional vectors
        if ((targetRotation - rotation) * movementData.rotation <= 0) {
            CancelAll(motorControl);
        }
        break;
    }

}

Vector2 Maze::FacingVector() {
    return Vector2(cos(rotation), sin(rotation));
}

void Maze::Solve(MotorControl* motorControl) {
    StartForwardMotors(motorControl, Vector2(0, 10));
}

void Maze::MoveTo(MotorControl* motorControl) {

}

void Maze::RotateTo(MotorControl* motorControl) {

}

void Maze::StartForwardMotors(MotorControl* motorControl, Vector2 newTargetLocation) {
    actionType = ActionTypes::move;
    targetPosition = newTargetLocation;
    motorControl->Move(1.0);
}

void Maze::CancelAll(MotorControl* motorControl) {
    actionType = ActionTypes::none;
    motorControl->CancelAll();
}