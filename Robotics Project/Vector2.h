/************
To hold 2D vectors like positions on the board.  This is different from point - point is integers, it is for 2 dimensional indices. This is
made with doubles.  It is for things that require precision like positions.

*************/
#pragma once
#include <cmath>

using namespace std;

class Vector2 {
public:
	double x;
	double y;
	Vector2();
	Vector2(double nx, double ny);
	double Magnitude();
	Vector2 operator+(Vector2 other);
	Vector2 operator-(Vector2 other);
	Vector2 operator*(double other);
	void operator+=(Vector2 other);
	void operator-=(Vector2 other);
	void operator*=(double other);
private:

};