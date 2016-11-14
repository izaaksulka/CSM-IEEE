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
using namespace std;
class Maze{
public:
    Maze();
    //Returns a list of Points that refer to locations in the maze that the robot should progress through to get somewhere
    vector<Point> GetPath(Point start, Point end);

private:
	int height;
	int width;
	Tile** map;

};