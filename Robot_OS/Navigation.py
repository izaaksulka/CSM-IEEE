from Transform import Transform
from Vector import Vector
import Maze

from math import pi, cos, sin 

from Drive import Drive
from MovementFeedback import MovementFeedback

import time
PAUSE_DURATION = 2.0 

#BEGIN_SEARCH, SEARCH_PERIMETER, FOLLOW_CABLE, OPEN_CACHE, RETURN_HOME = range(5)
BEGIN_SEARCH, SCAN_BOARD, OPEN_CACHE, RETURN_HOME = range(4)
RIGHT, LEFT, UP, ROTATE_CW, ROTATE_CCW = range(5)

BOARD_WIDTH = 7#feet
BOARD_HEIGHT = 7#feet

STOP = Vector( 0, 0 )
STOP_ROTATION = 0

MOVE_FORWARD = Vector( 0, 200 )
ROTATE_SPEED = 100

class Navigation:
    def __init__(self, startPosition, startRotation, driveBoard, mapBoard, encoderA, encoderB):
       
        self.position = startPosition
        self.rotation = startRotation

        self.velocity = MOVE_FORWARD
        self.rotVelocity = STOP_ROTATION
    
        # The current algorithm the robot is running
        self.state = BEGIN_SEARCH
  
        # Initialize drive 
        self.drive = Drive( driveBoard )

        self.feedback = MovementFeedback( encoderA, encoderB )
        #self.feedback.SetDirection( self.velocity, self.rotVelocity )

        #initialization of the maze array
        self.maze = Maze.Maze(BOARD_WIDTH, BOARD_HEIGHT, mapBoard)
        
        self.curDirection = RIGHT
        self.curRow = 6 
        
        self.rotating = False
    
        self.drive.SetMotors( self.velocity, self.rotVelocity )
        # For determining the printout rate 
        #self.updateCounter = 0
     
    def Update(self, ACSensorData):
        
        isRotating = False
        if self.curDirection == ROTATE_CCW or self.curDirection == ROTATE_CW:           isRotating = True
 
        delta = self.feedback.Update(self.rotation, isRotating)
        newPosX = self.position[0] + delta[0][0]
        newPosY = self.position[1] + delta[0][1]
        self.position = Vector( newPosX, newPosY )
        self.rotation += delta[1]
    
        #print( "Cur Pos: ", self.position, ", Cur Rotation: ", self.rotation, ", State: ", self.curDirection )
        
        # Call the appropriate update function based on what algo
        # we're running right now
        if self.state == BEGIN_SEARCH:
            self.UpdateStartup()
        elif self.state == SCAN_BOARD:
            self.ScanBoard( ACSensorData )
        elif self.state == OPEN_CACHE:
            self.maze.PrintMap()
        
        # Tell the chassis what to do now that we've figure that out

    # Start the robot off by making it move forward
    def UpdateStartup(self):
        #print("Begin Search...")
        #self.currentMovement = Transform(Vector(100.0, 0.0), 0.0)
        
        if self.position[0] > 1.5 and self.position[1] < 5.5:
            if not self.rotating:
                self.SetRotate(-45)
                self.rotating = True
            if self.rotation <= 0:
                self.curDirection = ROTATE_CW
                self.lastLinear = UP
                self.state = SCAN_BOARD
                self.SetForward()
                self.curRow = int(self.position[1])

                self.paused = True
                self.startPause = time.time()
                self.targetPos = ( self.targetPos[0] - 1, self.targetPos[1] )
        '''
        else:
            self.velocity = MOVE_FORWARD
            self.rotVelocity = STOP_ROTATION
            #self.feedback.SetDirection( self.velocity, self.rotVelocity )
        '''
    def ScanBoard(self, ACSensorData):
        #print("Searching perimeter for current...")

        if self.paused:
            self.StopAllMotors()
            #self.feedback.SetDirection( self.velocity, self.rotVelocity )


            if time.time() - self.startPause > 0.5:
                # Map cable onto the LED Matrix
                self.maze.SendAcSensorData(self.position, ACSensorData) 
                #print( "AC Data: ", ACSensorData )
            if time.time() - self.startPause > PAUSE_DURATION:
                self.paused = False
                self.startPause = time.time()

                if self.curDirection == RIGHT:
                    self.velocity = MOVE_FORWARD
                    self.targetPos = ( self.targetPos[0] + 1, self.targetPos[1] )

                elif self.curDirection == LEFT:
                    self.velocity = MOVE_FORWARD
                    self.targetPos = ( self.targetPos[0] - 1, self.targetPos[1] )

                elif self.curDirection == ROTATE_CW:
                    self.rotVelocity = -ROTATE_SPEED

                elif self.curDirection == ROTATE_CCW:
                    self.rotVelocity = ROTATE_SPEED
                
                elif self.curDirection == UP:
                    if self.lastLinear == RIGHT:
                        self.rotVelocity = -ROTATE_SPEED
                    else: 
                        self.rotVelocity = ROTATE_SPEED

                #self.feedback.SetDirection( self.velocity, self.rotVelocity )
            return


        #if it is positioned in the top right corner and is done scanning
        if self.curDirection == ROTATE_CCW and self.curRow == 1:
            self.StopAllMotors()
            self.maze.Connect()
            self.state = OPEN_CACHE
            return

        #Moving from left or right to rotating
        if self.curDirection == RIGHT and self.position[0] > 5.5:
            self.paused = True
            self.startPause = time.time()
            self.SetRotate(90)
        elif self.curDirection == LEFT and self.position[0] < 1.5:
            self.paused = True
            self.startPause = time.time()
            self.SetRotate(-90)

        elif self.curDirection == RIGHT and self.position[0] > self.targetPos[0]:
            self.paused = True
            self.startPause = time.time()
        elif self.curDirection == LEFT and self.position[0] < self.targetPos[0]:
            self.paused = True
            self.startPause = time.time()        

        #Moving from going up to rotating
        elif self.curDirection == UP and self.position[1] < self.curRow - 0.5:
            self.curRow -= 1
            if self.lastLinear == RIGHT:
                self.SetRotate(90)
            else: 
                self.SetRotate(-90)
            self.paused = True
            self.startPause = time.time()

        #Moving from rotating to the next desired direction
        elif self.curDirection == ROTATE_CCW and self.rotation >= self.targetAngle:
            self.SetForward()
        elif self.curDirection == ROTATE_CW and self.rotation <= self.targetAngle:
            self.SetForward()

    def GoToCache(self):
        if not self.connectedMaze:
            # Solve the missing gaps in the maze, 
            # namely the cache locations
            # Print out the map one last time
            cacheLocations = self.maze.Connect()
            self.maze.PrintMap()
            self.connectedMaze = True

            self.targetCaches = []
            
            if len( cacheLocations ) == 4:
                print( "You want this cake?" )
                # TODO: Tell robot to check all caches
            elif len( cacheLocations ) == 3:
                print( "I want that cake" )
                # TODO: Tell robot to check the corner wire
            else:
                print( "The cake is a lie" ) 
                # TODO: GOTO cache
   
    def GoHome(self):
        #find the angle we need to go at to get back to B6
        vectorToB6 = (1.5 - position[0], 5.5 - position[1])
        #targetAngle = math.atan()
        return
    #returns the angle the robot needs to face in order to go in the direction a vector points
    #returns angle from 0 to 360
    def AngleOfVector(self, v):
        return 2 * math.pi * AngleOfVectorRadians(v)#find in radians and convert. done this way because python math wants radians but we want degrees
    def AngleOfVectorRadians(self, v): 
        if v[0] > 0:#if x of vector is positive, return atan of y / x
            return atan(v[1] / float(v[0]))
        elif v[0] < 0:
            return atan(v[1] / float(v[0])) + math.pi / 2.0
    # Tells the robot to go forward after we've done a rotation
    def SetForward(self):
        self.rotVelocity = STOP_ROTATION

        if self.lastLinear == UP:
            if self.curDirection == ROTATE_CCW:
                self.targetPos = (self.position[0] - 1, self.position[1])
                self.curDirection = LEFT
            else:
                self.targetPos = (self.position[0] + 1, self.position[1])
                self.curDirection = RIGHT
        else:
            self.targetPos = (self.position[0] , self.position[1] - 1)
            self.curDirection = UP

        self.velocity = MOVE_FORWARD
        self.rotVelocity = STOP_ROTATION
        #self.feedback.SetDirection( self.velocity, self.rotVelocity )
        self.drive.SetMotors( self.velocity, self.rotVelocity )

    # Tells the robot to turn 90 degrees after it's gone all the way
    # across the board        
    def SetRotate(self, deltaAngle):
        self.velocity = STOP

        self.lastLinear = self.curDirection

        self.targetAngle = self.rotation + deltaAngle
        
        if deltaAngle < 0:
            self.curDirection = ROTATE_CW
            self.rotVelocity = -ROTATE_SPEED
        else:
            self.curDirection = ROTATE_CCW
            self.rotVelocity = ROTATE_SPEED           

        self.drive.SetMotors( self.velocity, self.rotVelocity )
        #self.feedback.SetDirection( self.velocity, self.rotVelocity )

    def StopAllMotors(self):
        self.velocity = STOP
        self.rotVelocity = STOP_ROTATION
        self.drive.SetMotors( self.velocity, self.rotVelocity )
    def toRad(angle):
        return angle * pi / 180.0
    

'''
    def SetDriver(self, newDriver):
        self.driver = newDriver
'''   

'''
    def SendNewMovement(self):
        print("SendNewMovementTransform")
        self.driver.SetMotors(self.currentMovement)
'''
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

'''
        IN PERIMETER SEARCH FUNCTION
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

        
'''
    # Make the robot run along the perimeter until we find the cable 
    def PerimeterSearch(self):
        #print("Searching perimeter for current...")

        delta = self.feedback.Update()
        self.position += delta[0]
        self.rotation += delta[1]

        if self.foundCable == True:
            self.state = FOLLOW_CABLE

        else:
            if self.curDirection == ROTATE and self.rotation >= self.targetAngle:
                self.SetForward()                    
            # Once we hit the end of the board,
            # tell the robot to rotate
            elif self.curDirection == RIGHT and self.position[0] > 6.5:
                self.SetRotate()
            elif self.curDirection == UP and self.position[1] < 0.5:
                self.SetRotate()
            elif self.curDirection == LEFT and self.position[0] < 0.5:
                self.SetRotate()
            elif self.curDirection == DOWN and self.position[1] > 6.5:
                self.StopAllMotors()
    
'''
