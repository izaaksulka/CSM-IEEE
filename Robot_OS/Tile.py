import time


foam, wire, void, target = range(4);
AC_WIRE_TIME_THRESHOLD = 0.2;
class Tile:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.state = foam;
        self.lastAcData = False;
        self.lastAcTime = 0;
        self.totalAcOnTime = 0;

    def SetState(self, newState):
        self.state = newState;
        #something about updating lights maybe?  maybe returns true if update needed
    def UpdateACSensorData(self, newAcData):
        currentTime = time.time();
        if(newAcData != self.lastAcData):
            if(newAcData == False):
                self.totalAcOnTime += currentTime - self.lastAcTime;
            self.lastAcTime = currentTime;
            self.lastAcData = newAcData;
            self.CheckTotalAcTime();
    def CheckTotalAcTime(self):
        if(self.totalAcTime > AC_WIRE_TIME_THRESHOLD):
            self.SetState(wire);

    def GetState(self):
        return self.state;
