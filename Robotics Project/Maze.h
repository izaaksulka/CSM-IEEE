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
using namespace std;
class Maze{
public:
    Maze();
	~Maze();
    //Returns a list of Points that refer to locations in the maze that the robot should progress through to get somewhere
    vector<Point> GetPath(Point start, Point end);
	//Lets us see what the program thinks the maze looks like
	void Print(ostream& out);
	//Solve() is the core telling this nav module to try to solve the maze - Do whatever it wants and explore
	void Solve();
private:
	int height;
	int width;
	//These are in feet right now.
	double tileHeight;
	//These are in feet right now.
	double tileWidth;
	//Where the robot is (currently in feet)
	Vector2 position;

	Tile** map;
	//The stuff that has to happen when information is learned about a tile. (set tile type, any special action that has to be taken when a tile of that type is found, etc)
	void SetTile();
	//Converts the current position to a point that can be used to reference a tile
	Point CurrentTilePoint();
	//Returns a pointer to the current tile.
	Tile* CurrentTile();
};