import time
import RPi.GPIO as GPIO

class ACDetectorReader:

    def __init__(self, pinID):
        self.createdAt = time.time();
        self.currentTime = time.time();
        self.pinID = pinID;
        self.delayForFalseReading = 0.05;
        self.lastOnTime = time.time() - self.delayForFalseReading;
        
        self.updateCounter = 0;
        GPIO.setmode( GPIO.BOARD );
        print("Pin id = " + str(pinID));
        GPIO.setup( self.pinID, GPIO.IN );
 #       self.wireDetected = False;
    def TakeReading(self):
        print( "Reading: ", not GPIO.input( self.pinID ) )        
        return not GPIO.input( self.pinID );

    def GetSensorValue(self): #use this one to get a value out of this class
        #print("ACSensorReader: " + str(self.currentTime - self.lastOnTime < self.delayForFalseReading));
        if(self.currentTime - self.lastOnTime < self.delayForFalseReading):
            return True;
        else:
            return False;
    
    def Update(self):  #needs to be fed an update every now and then
        self.UpdateTime();
        readingValue = self.TakeReading();
        if(readingValue == True):
            self.lastOnTime = self.currentTime;
        #print(self.currentTime - self.createdAt)
        #print("Update");
        self.updateCounter += 1;

    #def GetElapsedTime():
    #    return time.time();

    def UpdateTime(self):
        self.currentTime = time.time();

    def GetAge(self):
        return self.currentTime - self.createdAt;


#Some example usage

#reader = ACDetectorReader(1);

#while(1):
#    reader.Update();
#    if(reader.GetAge() > 5):
#        break;

#print("done");
