#pragma once
#include <string>
using namespace std;
class Point {
public:
	Point();
	Point(int newX, int newY);

	int GetX();
	int GetY();
	void SetX(int newX);
	void SetY(int newY);

	Point operator+(Point other);
	Point operator-(Point other);

	string ToString();
private:
	int x;
	int y;

};