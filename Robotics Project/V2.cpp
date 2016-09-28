#include "V2.h"

//using namespace std;


V2::V2() {
	x = 0;
	y = 0;
}
V2::V2(int newX, int newY) {
	x = newX;
	y = newY;
}

int V2::GetX() {
	return x;
}
int V2::GetY() {
	return y;
}
void V2::SetX(int newX) {
	x = newX;
}
void V2::SetY(int newY) {
	y = newY;
}

V2 V2::operator+(V2 other) {
	return V2(x + other.GetX(), y + other.GetY());
}
V2 V2::operator-(V2 other) {
	return V2(x - other.GetX(), y - other.GetY());
}

string V2::ToString() {
	return "(" + to_string(x) + ", " + to_string(y) + ")";
}