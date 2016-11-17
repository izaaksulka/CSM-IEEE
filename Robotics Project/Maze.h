/**********************************

Author: Izaak Sulka

Declaration of Maze which stores data about the maze and has functions that work with it like "GetPath(from, to)"
I think this class will also do the navigation, like telling the motor controller module where to go.

**********************************/
#pragma once
#include <iostream>
#include <string>
#include <vector>
#include "Point.h"
#include "Tile.h"
#include "Vector2.h"
#include "MovementFeedback.h"
#include <cmath>
using namespace std;
enum ActionTypes {none, move, rotate};
class Maze{
public:
    Maze();
	~Maze();
    //Returns a list of Points that refer to locations in the maze that the robot should progress through to get somewhere
    vector<Point> GetPath(Point start, Point end);
	//Lets us see what the program thinks the maze looks like
	void Print(ostream& out);
    //Core calls this and the maze decides how to navigate
	void Update(const MovementData &movementData, MotorControl* motorControl);
private:
	int height;
	int width;
	//These are in feet right now.
	double tileHeight;
	//These are in feet right now.
	double tileWidth;
	//Where the robot is (currently in feet)
	Vector2 position;
    //The current rotation of the robot.  Right (positive x) is 0, with counterclockwise rotation as positive
    double rotation;
    //Where the robot wants to be
    Vector2 targetPosition;
    //Which way the robot wants to face
    double targetRotation;
    //Keep track of what the robot is doing
    int actionType;
    //An array of arrays of Tile objects
	Tile** map;
	//The stuff that has to happen when information is learned about a tile. (set tile type, any special action that has to be taken when a tile of that type is found, etc)
	void SetTile(); //Not sure about this one
	//Converts the current position to a point that can be used to reference a tile
	Point CurrentTilePoint();
	//Returns a pointer to the current tile.
	Tile* CurrentTile();
    //A function to get the direction the robot is moving in from the direction it is facing
    Vector2 FacingVector();
    //Decide where the best place to go is, and tell the motorController where to go
    void Solve(MotorControl* motorControl);
    //Do the things (rotate then move forward as needed) to get to a new position
    void MoveTo(MotorControl* motorControl);
    //Starts rotating to a new rotation
    void RotateTo(MotorControl* motorControl);
    //Starts moving to a new point
    void StartForwardMotors(MotorControl* motorControl, Vector2 newTargetLocation);
    //Cancel all motor instructions
    void CancelAll(MotorControl* motorControl);
};