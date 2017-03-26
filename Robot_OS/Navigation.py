import Transform
import Vector
import Maze

startup, initialSearch, goToTarget, figureOutTheShit = range(4);
BOARD_WIDTH = 7;#feet
BOARD_HEIGHT = 7;#feet

class Navigation:
    def __init__(self, startPosition, startRotation, newDriver):
        self.currentMovement = Transform.Transform(Vector.Vector(0.0, 0.0), 0.0);
        self.initialSearchDirection = 0;
        self.updateCounter = 0;
        self.transform = Transform.Transform(startPosition, startRotation);
        #self.transform = Transform.Transform();
        self.state = startup;
        self.driver = newDriver;
        self.zigZagDirection = 1;
        self.zigZagVerticalMoveTarget = startPosition[1];
        self.zigZagInVerticalMovement = False;
        #initialization of the maze array
        self.maze = Maze.Maze(BOARD_WIDTH, BOARD_HEIGHT);
        
    def SetDriver(self, newDriver):
        self.driver = newDriver;
        
    def Update(self, acSensorData, deltaTransform):
        self.updateCounter += 1;
        self.mracSensorData = acSensorData;
        
        self.maze.SendAcSensorData(self.transform.position, acSensorData)
        self.mrDeltaTransform = deltaTransform;
        self.transform.position = self.transform.position + deltaTransform.position;
        #may need to multiply rotation by this movement
        #if(self.updateCounter % 1000 == 0):
            #print("Transform => " + self.transform.ToString());
        if (self.state == startup):
            self.UpdateStartup();
        if(self.state == initialSearch):
            self.UpdateInitialSearch();
        
        #print("Navigation.Update()");
        #changeMotors = False;


        #if(changeMotors):
        
        #print("need to change motors");

    def UpdateStartup(self):
        #print("Working on startup");
        self.currentMovement = Transform.Transform(Vector.Vector(100.0, 0.0), 0.0);
        self.SendNewMovement();
        self.state = initialSearch;
    """    
    def UpdateInitialSearch(self):
        #print("Working on initialSearch");
        if(self.mracSensorData == True):
            self.state = track;
            #should probably set a value in the maze array somewhere around here
            self.currentMovement = Transform.Transform(Vector.Vector(0.0, 0.0), -50.0);
            self.SendNewMovement();
        else:#this part makes a hard coded square loop
            newDir = Vector.Vector(0.0, 0.0);
            needNewMovementSent = False;
            if(self.initialSearchDirection % 2 == 0):
                if(self.transform.position[0] < 0.5 or self.transform.position[0] > 6.5):
                    newDir = Vector.Vector(0.0, 100.0) * (self.initialSearchDirection - 1);
                    needNewMovementSent = True;
                    if(self.transform.position[0] < 0.5):
                        self.transform.position = Vector.Vector(0.5, self.transform.position[1]);
                    else:
                        self.transform.position = Vector.Vector(6.5, self.transform.position[1]);
            else:   
                if(self.transform.position[1] < 0.5 or self.transform.position[1] > 6.5):
                    newDir = Vector.Vector(100.0, 0.0) * (self.initialSearchDirection - 2);
                    needNewMovementSent = True;
                    if(self.transform.position[1] < 0.5):
                        self.transform.position = Vector.Vector(self.transform.position[0], 0.5);
                    else:
                        self.transform.position = Vector.Vector(self.transform.position[0], 6.5);
                        
            if(needNewMovementSent):
                self.currentMovement.position = newDir;
                self.SendNewMovement();
                self.initialSearchDirection += 1;
                if(self.initialSearchDirection > 3):#loop back to zero if gone around every side.
                    self.initialSearchDirection = 0;
     """
    def UpdateInitialSearch(self):
        newDir = Vector.Vector(0.0, 0.0);
        terminated = False;
        if(self.zigZagInVerticalMovement):
            if(self.zigZagVerticalMoveTarget < 0):
                terminated = True;
                newDir = self.TerminateZigZagSearch();
            else:     
                if(self.transform.position[1] < self.zigZagVerticalMoveTarget):
                    self.zigZagInVerticalMovement = False;
                    if(self.zigZagDirection == 0):
                        newDir = Vector.Vector(-100, 0);
                    else:
                        newDir = Vector.Vector(100, 0);
        else:#when the movement is not vertical
            if(self.zigZagDirection == 0):#0 is left, 1 is right
                if(self.transform.position[0] < 0.5):
                    newDir = self.FinishedZigZagSidewaysMovement();
            else:#when moving right
                if(self.transform.position[0] > BOARD_WIDTH - 0.5):
                    newDir = self.FinishedZigZagSidewaysMovement();
        if(newDir != Vector.Vector(0.0, 0.0) or terminated == True):  
            self.currentMovement.position = newDir;
            self.SendNewMovement();
        
        #self.state = goToTarget;
    def FinishedZigZagSidewaysMovement(self):
        self.zigZagDirection = 0 if (self.zigZagDirection == 1) else 1;
        self.zigZagInVerticalMovement= True;
        self.zigZagVerticalMoveTarget -= 1;
        return Vector.Vector(0, -100);
    def TerminateZigZagSearch(self):
        self.state = goToTarget;
        return Vector.Vector(0, 0);
    def SendNewMovement(self):
        print("SendNewMovementTransform");
        self.driver.SetMotors(self.currentMovement);
    def StopAllMotors(self):
        self.currentMovement.position = Vector.Vector( 0, 0 );
        self.currentMovement.rotation = 0
        self.SendNewMovement();
