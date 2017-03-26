import Transform
from Vector import Vector
#import pygame
import time
import Drive
from math import cos, sin

# Number of reading per second
POLL_RATE = 10
DELTA_TIME = 1 / float(POLL_RATE)
'''
THETA = 60.0

# Convert mouse distance to feet    
DISTANCE_SCALE = 0.001

#distance from the center of the robot to the mouse
MOUSE_LOCATION_RADIUS = 0.5;
'''

class MovementFeedback:

    def __init__(self):#passed driver to fake feedback for testing

        '''
        # Initialize pygame, we use this to keep track of the mouse
        pygame.init()
        screen_w = pygame.display.Info().current_w
        screen_h = pygame.display.Info().current_h
        screen = pygame.display.set_mode( ( 300, 300 ), pygame.NOFRAME )
        self.width, self.height = screen.get_size()
        pygame.mouse.set_pos( self.width/2, self.height/2 ) 
        self.driver = newDriver
        '''       
        
        #self.startPoll = time.time()
        self.lastPoll = time.time()
        self.curPoll = self.lastPoll

        print("Movement Feedback setup done")

    def StartMeasurement(self):
        #self.startPoll = time.time()
        self.lastPoll = time.time()
        self.curPoll = self.lastPoll

    # Soley for dead reckoning,
    # Tells the movement feedback how the motors are running
    # So that we can "measure" the distance it's traveled
    def SetDirection( velocity, rotVelocity ):
        self.velocity = velocity
        self.rotVelocity = rotVelocity

    #returns movement value
    def Update(self):
            
        # For the moment it's dead reckoning,
        # but in a normal situation we would
        # Update and return the sensor value
        self.curPoll = time.time()

        # Only update POLL_RATE times per second
        if self.curPoll - self.lastPoll > DELTA_TIME:

            deltaTime = self.curPoll - self.lastPoll
            
            distanceTraveled = Vector( self.velocity[0] * deltaTime, 
                                       self.velocity[1] * deltaTime )

            distanceRotated = self.rotVelocity * deltaTime

            self.lastPoll = self.curPoll

            return ( distanceTraveled, distanceRotated )

        # This is weird, but if we're not getting the reading yet, 
        # then we're just reporting no change
        return ( Vector(0, 0), 0 )

        '''
        deltaPos = Vector( 0, 0 )
        deltaRot = 0.0;
        # Get the mouse change from pygame
        # Have to do it via event dequeuing
        if time.time() - self.lastPolled > DELTA_TIME:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    
                    mPos = pygame.mouse.get_pos()
                    
                    # Get the change in position from the mouse   
                    deltaM = ( mPos[0] - self.width / 2, mPos[1] - self.height / 2 )
                    
                    # Reset the timer for the next poll
                    self.lastPolled = time.time()
                    # Move the mouse back to the middle of the window
                    # so we can't hit the edge of the screen
                    pygame.mouse.set_pos( [ self.width/2, self.height/2 ] )
                    if(drive.GetMovementMode() == TRANSLATE):
                        #print( "Mouse Change: ", deltaPos )
                        deltaPos = self.ToBoardSpace( deltaM )
                        #print( "Robot Change: ", deltaPos )
                    if(drive.GetMovementMode() == ROTATE):
                        deltaRot = self.RotationFromMouse(deltaM);
        
        return Transform.Transform( deltaPos, deltaRot)
        '''
'''
    def GetDeltaPos(self):
        movement = self.driver.bodyVel * 0.000001#here, the feedback unit just
        #copies the setting from
        #the driver - this gets replaced when we actually get data from the
        #sensors.
        return movement

    def GetDeltaRot(self):
        #for now I have the rotation constant
        return 0.0

    def ToBoardSpace(self, deltaPos):
        deltaPos = Vector( deltaPos[0], -deltaPos[1] )
        return Vector( deltaPos.inner( Vector(  cos(THETA), -sin(THETA) ) ) * DISTANCE_SCALE, 
                       deltaPos.inner( Vector( -sin(THETA), -cos(THETA) ) ) * DISTANCE_SCALE )

    def RotationFromMouse(self, deltaM):
        rot = deltaM[0] / MOUSE_LOCATION_RADIUS;
        return rot;
'''