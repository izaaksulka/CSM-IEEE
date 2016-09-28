#pragma once
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

	void Print();
private:
	int x;
	int y;

};