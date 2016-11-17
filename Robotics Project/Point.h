#pragma once
#include <string>
#include <iostream>
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
    void Print();
private:
	int x;
	int y;

};