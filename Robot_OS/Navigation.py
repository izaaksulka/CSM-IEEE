from Transform import Transform
from Vector import Vector
import Maze

from Drive import Drive
from MovementFeedback import MovementFeedback

BEGIN_SEARCH, SEARCH_PERIMETER, FOLLOW_CABLE, OPEN_CACHE, RETURN_HOME = range(5)
RIGHT, UP, LEFT, DOWN, ROTATE = range(5)

BOARD_WIDTH = 7#feet
BOARD_HEIGHT = 7#feet

class Navigation:
    def __init__(self, startPosition, startRotation, driveBoard):
       
        self.position = startPosition
        self.rotation = startRotation

        self.velocity = Vector( 0, 0 )
        self.rotVelocity = 0
    
        # The current algorithm the robot is running
        self.state = BEGIN_SEARCH
  
        # Initialize drive 
        self.drive = Drive( driveBoard )

        self.feedback = MovementFeedback()

        #initialization of the maze array
        self.maze = Maze.Maze(BOARD_WIDTH, BOARD_HEIGHT)
       
        ''' 
        self.currentMovement = Transform(Vector(0.0, 0.0), 0.0)
        self.initialSearchDirection = 0
        self.transform = Transform(startPosition, startRotation)

        self.driver = newDriver
        '''

        # For determining the printout rate 
        #self.updateCounter = 0
        '''
        # For the zig-zag algorithm
        self.zigZagDirection = 1
        self.zigZagVerticalMoveTarget = startPosition[1]
        self.zigZagInVerticalMovement = False
        '''
    def SetDriver(self, newDriver):
        self.driver = newDriver
        
    def Update(self, acSensorData, deltaTransform):
    
        self.foundCable = acSensorData
        
        # Map cable onto the LED Matrix
        self.maze.SendAcSensorData(self.position, acSensorData)

        #self.transform.position = self.transform.position + deltaTransform.position
        
        # Call the appropriate update function based on what algo
        # we're running right now
        if self.state == BEGIN_SEARCH:
            self.UpdateStartup()
        elif self.state == SEARCH_PERIMETER:
            self.PerimeterSearch()
        elif self.state == FOLLOW_CABLE:
            self.UpdateTrack()
        
        '''
        # Print out where we're at right now
        self.updateCounter += 1
        if(self.updateCounter % 1000 == 0):
            print("Transform => " + self.transform.ThoString())
        '''

    # Start the robot off by making it move forward
    def UpdateStartup(self):
        #print("Begin Search...")
        #self.currentMovement = Transform(Vector(100.0, 0.0), 0.0)
        self.velocity = Vector( 0, 100 )
        self.rotVelocity = 0.0

        self.SendNewMovement()
        self.state = SEARCH_PERIMETER

        self.curDirection = RIGHT
        self.lastDirection = RIGHT
        self.feedback.SetDirection( self.velocity, self.rotation )

    
    # Make the robot run along the perimeter until we find the cable 
    def PerimeterSearch(self):
        #print("Searching perimeter for current...")
        if self.foundCable == True:
            self.state = FOLLOW_CABLE
            #should probably set a value in the maze array somewhere around here
            #self.currentMovement = Transform(Vector(0.0, 0.0), -50.0)
            #self.SendNewMovement()
        else:
            # TODO: Write the algorithm where we move forward and turn left
            #       four times
            if curDirection == ROTATE:

            elif curDirection == RIGHT:
                delta = self.feedback.Update()
                self.position += delta[0]
                self.rotation += delta[1]

                if self.position > 6.5:
                    curDirection = 

        '''
        else:#this part makes a hard coded square loop
            newDir = Vector(0.0, 0.0)
            needNewMovementSent = False
            if(self.initialSearchDirection % 2 == 0):
                if(self.transform.position[0] < 0.5 or self.transform.position[0] > 6.5):
                    newDir = Vector(0.0, 100.0) * (self.initialSearchDirection - 1)
                    needNewMovementSent = True
                    if(self.transform.position[0] < 0.5):
                        self.transform.position = Vector(0.5, self.transform.position[1])
                    else:
                        self.transform.position = Vector(6.5, self.transform.position[1])
            else:   
                if(self.transform.position[1] < 0.5 or self.transform.position[1] > 6.5):
                    newDir = Vector(100.0, 0.0) * (self.initialSearchDirection - 2)
                    needNewMovementSent = True
                    if(self.transform.position[1] < 0.5):
                        self.transform.position = Vector(self.transform.position[0], 0.5)
                    else:
                        self.transform.position = Vector(self.transform.position[0], 6.5)
                        
            if(needNewMovementSent):
                self.currentMovement.position = newDir
                self.SendNewMovement()
                self.initialSearchDirection += 1
                if(self.initialSearchDirection > 3):#loop back to zero if gone around every side.
                    self.initialSearchDirection = 0
        '''

    # Follow the cable
    def UpdateTrack():
        x =3
        return
    
    def SendNewMovement(self):
        print("SendNewMovementTransform")
        self.driver.SetMotors(self.currentMovement)
    def StopAllMotors(self):
        self.currentMovement.position = Vector( 0, 0 )
        self.currentMovement.rotation = 0
        self.SendNewMovement()
    '''
    def PerimeterSearch(self):
        newDir = Vector(0.0, 0.0)
        terminated = False
        if(self.zigZagInVerticalMovement):
            if(self.zigZagVerticalMoveTarget < 0):
                terminated = True
                newDir = self.TerminateZigZagSearch()
            else:     
                if(self.transform.position[1] < self.zigZagVerticalMoveTarget):
                    self.zigZagInVerticalMovement = False
                    if(self.zigZagDirection == 0):
                        newDir = Vector(-100, 0)
                    else:
                        newDir = Vector(100, 0)
        else:#when the movement is not vertical
            if(self.zigZagDirection == 0):#0 is left, 1 is right
                if(self.transform.position[0] < 0.5):
                    newDir = self.FinishedZigZagSidewaysMovement()
            else:#when moving right
                if(self.transform.position[0] > BOARD_WIDTH - 0.5):
                    newDir = self.FinishedZigZagSidewaysMovement()
        if(newDir != Vector(0.0, 0.0) or terminated == True):  
            self.currentMovement.position = newDir
            self.SendNewMovement()
        
        #self.state = FOLLOW_CABLE
    
    def FinishedZigZagSidewaysMovement(self):
        self.zigZagDirection = 0 if (self.zigZagDirection == 1) else 1
        self.zigZagInVerticalMovement= True
        self.zigZagVerticalMoveTarget -= 1
        return Vector(0, -100)
    def TerminateZigZagSearch(self):
        self.state = FOLLOW_CABLE
        return Vector(0, 0)
    
    '''
