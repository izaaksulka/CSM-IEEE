/**********************************

Author: Izaak Sulka

Declaration of Maze which stores data about the maze and has functions that work with it like "GetPath(from, to)"

**********************************/
#pragma once
#include <iostream>
#include <string>
#include <vector>
#include "Point.h"
using namespace std;
class Maze{
public:
    Maze();
    //Returns a list of Points that refer to locations in the maze that the robot should progress through to get somewhere
    vector<Point> GetPath(Point start, Point end);

private:

    vector<vector<Tile>> maze;

};