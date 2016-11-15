#pragma once
#include "Point.h"
#include <string>
using namespace std;
class Tile {
public:
	Tile();
	Tile(int, int);
	void Print(ostream& out);
	void SetType(int newType);
private:

    //Need to make an enumerator so that using this isn't confusing
    int type;
    Point position;
};