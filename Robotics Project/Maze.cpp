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
	position = Vector2(0.5, 0.5);
	//Set up the Tile array
	map = new Tile*[width];
	int k = 0;
	for (int i = 0; i < width; i++) {
		map[i] = new Tile[height];
		for (int ii = 0; ii < height; ii++) {
			map[i][ii] = Tile(i, ii);
			map[i][ii].SetType(k);  //This line is just for testing if the array is being stored correctly
			k++;
		}
	}
	cout << "Finished Maze() constructor   <-- why does this happen twice??" << endl;
}

Maze::~Maze() {
	for (int i = 0; i < width; i++) {
		delete[] map[i];
	}
	delete[] map;
}

void Maze::Print(ostream& out) {
	for (int ii = 0; ii < height; ii++) {
		for (int i = 0; i < width; i++) {
			map[i][ii].Print(out);
		}
		out << endl;
	}
}


Point Maze::CurrentTilePoint() {
	//Havn't tested this yet
	return Point(position.x / tileWidth, position.y / tileHeight);
}

Tile* Maze::CurrentTile() {
	Point cp = CurrentTilePoint();
	return map[cp.GetY(), cp.GetX()];
}