/*******************
Declaration of BSensor class
This looks for a magnetic field and reports some info about it.  Not really sure how that's going to work so here's a blank
*******************/
#pragma once
using namespace std;

//A container in case the data needed is a little more complicated than 1 number
//If it is just 1 number this isn't needed
class BSensorData {
	//Whatever this data type needs to store information about magnetic fields gathered by our sensor
public:
	BSensorData();
};

//The class that detects magnetic fields and tells the core or navigator about them.
class BSensor {
public:
	BSensor();

	BSensorData GetReading();



private:



};


