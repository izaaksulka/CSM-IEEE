#pragma once
#include <string>
using namespace std;
class V2 {
public:
	V2();
	V2(int newX, int newY);

	int GetX();
	int GetY();
	void SetX(int newX);
	void SetY(int newY);

	V2 operator+(V2 other);
	V2 operator-(V2 other);

	string ToString();
private:
	int x;
	int y;

};