//Implementation for tile
#include "Tile.h"

Tile::Tile() {
	type = 0;
}

Tile::Tile(int nx, int ny) {
	type = 0;
	position = Point(nx, ny);
}
