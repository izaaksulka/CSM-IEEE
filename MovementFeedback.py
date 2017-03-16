import Transform;
import Vector;
class MovementFeedback:
    def __init__(self, newDriver):#passed driver to fake feedback for testing
        self.driver = newDriver;
        print("MovementFeedback setup done");
    #returns movement value
    def Update(self):
        #print("MovementFeedback update");
        
        return Transform.Transform(self.GetDeltaPos(), self.GetDeltaRot());

    def GetDeltaPos(self):
        movement = self.driver.bodyVel * 0.0000005;#here, the feedback unit just
        #copies the setting from
        #the driver - this gets replaced when we actually get data from the
        #sensors.
        return movement;

    def GetDeltaRot(self):
        return 0.0;#for now I have the rotation constant
