//Implementation for tile
#include "Tile.h"

Tile::Tile() {
	type = 0;
	position = Point(0, 0);
}

Tile::Tile(int nx, int ny) {
	type = 0;
	position = Point(nx, ny);
}

void Tile::Print(ostream& out) {
	out << "[ " << type << " ]";
}

void Tile::SetType(int newType) {
	type = newType;
}
