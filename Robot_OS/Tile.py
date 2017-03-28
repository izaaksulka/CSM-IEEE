import time


START, FOAM, WIRE, VOID, END, OBSTACLE, UNKNOWN = range(7)
OFF, RED, BLUE, YELLOW = range(4)
#AC_WIRE_TIME_THRESHOLD = 0.2
RATIO_THRESHOLD = 0.9
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = UNKNOWN
        self.timesScanned = 0
        self.timesDetected = 0
        #self.lastAcData = False
        #self.lastAcTime = 0
        #self.totalAcOnTime = 0

    def SetState(self, newState):
        if(self.state == newState or self.state == START):
            return False
        self.state = newState
        return True

    def UpdateACSensorData(self, newACData):
        self.timesScanned += 1
        if newACData:
            self.timesDetected += 1
        
        ratio = self.timesDetected / float(self.timesScanned)
        if(ratio > RATIO_THRESHOLD):
            #print("Found a wire.  x = ", self.x, "  y = ", self.y)
            return self.SetState(WIRE)
        else:#meaning there si not a wire
            return self.SetState(FOAM)
        
        '''
        currentTime = time.time()
        if(newAcData != self.lastAcData):
            if(newAcData == False):
                self.totalAcOnTime += currentTime - self.lastAcTime
            self.lastAcTime = currentTime
            self.lastAcData = newAcData
           
             self.CheckTotalAcTime()
        '''

    '''
    def CheckTotalAcTime(self):
        if(self.totalAcTime > AC_WIRE_TIME_THRESHOLD):
            self.SetState(wire)
    '''
    
    def GetColor(self):
        if self.state == WIRE:  
            return RED
        elif self.state == VOID:
            return BLUE
        elif self.state == START:
            return YELLOW
        else:
            return OFF

    def GetState(self):
        return self.state
    def IsWire(self):
        return self.state == WIRE

