/************
Implementation for Vector2
*************/
#include "Vector2.h"

Vector2::Vector2() {
	x = 0.0;
	y = 0.0;
}
Vector2::Vector2(double nx, double ny) {
	x = nx;
	y = ny;
}
double Vector2::Magnitude() {
	return sqrt(x*x + y*y);
}
Vector2 Vector2::operator+(Vector2 other) {
	return Vector2(other.x + x, other.y + y);
}
Vector2 Vector2::operator-(Vector2 other) {
	return Vector2(x - other.x, y - other.y);
}
Vector2 Vector2::operator*(double other) {
	return Vector2(x * other, y * other);
}
void Vector2::operator+=(Vector2 other) {
	x += other.x;    y += other.y;
}
void Vector2::operator-=(Vector2 other) {
	x -= other.x;    y -= other.y;
}
void Vector2::operator*=(double other) {
	x *= other;      y *= other;
}
double Vector2::Dot(const Vector2 &other) {
    return x * other.x + y * other.y;
}