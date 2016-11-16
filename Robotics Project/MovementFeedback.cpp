


#include "MovementFeedback.h"

MovementFeedback::MovementFeedback() {
	mc = NULL;
}

MovementFeedback::MovementFeedback(MotorControl *nmc) {
	mc = nmc;
}

MovementData MovementFeedback::Report() {

	return MovementData();
}