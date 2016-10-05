#include "Point.h"

//using namespace std;


Point::Point() {
	x = 0;
	y = 0;
}
Point::Point(int newX, int newY) {
	x = newX;
	y = newY;
}

int Point::GetX() {
	return x;
}
int Point::GetY() {
	return y;
}
void Point::SetX(int newX) {
	x = newX;
}
void Point::SetY(int newY) {
	y = newY;
}

Point Point::operator+(Point other) {
	return Point(x + other.GetX(), y + other.GetY());
}
Point Point::operator-(Point other) {
	return Point(x - other.GetX(), y - other.GetY());
}

string Point::ToString() {
	return "(" + to_string(x) + ", " + to_string(y) + ")";
}