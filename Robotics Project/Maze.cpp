/**********************************

Author: Izaak Sulka

Implementation for the Maze class, which stores data about the maze and has functions that work with it like "GetPath(from, to)"

**********************************/
#include "maze.h"

Maze::Maze() {
    //Do whatever needs to be done in this initialization
	height = 7;
	width = 7;
	map = new Tile*[width];
	for (int i = 0; i < width; i++) {
		map[i] = new Tile[height];
		for (int ii = 0; ii < height; ii++) {
			map[i][ii] = Tile(i, ii);
		}
	}
	cout << "Finished Maze() constructor   <-- why does this happen twice??" << endl;
}