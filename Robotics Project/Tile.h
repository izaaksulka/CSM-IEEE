#pragma once
#include "Point.h"

class Tile {
public:
	Tile();
	Tile(int, int);

private:

    //Need to make an enumerator so that using this isn't confusing
    int type;
    Point position;
};