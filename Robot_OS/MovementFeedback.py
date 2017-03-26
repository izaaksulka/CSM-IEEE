import Transform
from Vector import Vector
import pygame
import time
from math import cos, sin

# Number of reading per second
POLL_RATE = 100
DELTA_TIME = 1 / float(POLL_RATE)
THETA = 60.0

# Convert mouse distance to feet    
DISTANCE_SCALE = 0.001


class MovementFeedback:

    def __init__(self, newDriver):#passed driver to fake feedback for testing

        # Initialize pygame, we use this to keep track of the mouse
        pygame.init()
        screen_w = pygame.display.Info().current_w
        screen_h = pygame.display.Info().current_h
        screen = pygame.display.set_mode( ( 300, 300 ), pygame.NOFRAME )
        self.width, self.height = screen.get_size()
        pygame.mouse.set_pos( self.width/2, self.height/2 ) 
        
        self.lastPolled = time.time()

        self.driver = newDriver
        print("MovementFeedback setup done")
    #returns movement value
    def Update(self):
       
        deltaPos = Vector( 0, 0 )
 
        # Get the mouse change from pygame
        # Have to do it via event dequeuing
        if time.time() - self.lastPolled > DELTA_TIME:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mPos = pygame.mouse.get_pos()
            
                    # Get the change in position from the mouse   
                    deltaPos = ( mPos[0] - self.width / 2, mPos[1] - self.height / 2 )
            
                    # Reset the timer for the next poll
                    self.lastPolled = time.time()
                    # Move the mouse back to the middle of the window
                    # so we can't hit the edge of the screen
                    pygame.mouse.set_pos( [ self.width/2, self.height/2 ] )
            
                    deltaPos = self.ToBoardSpace( deltaPos )

        return Transform.Transform( deltaPos, self.GetDeltaRot())

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
        deltaPos = Vector( deltaPos[0], deltaPos[1] )
        return Vector( deltaPos.inner( Vector(  cos(THETA), -sin(THETA) ) ) * DISTANCE_SCALE, 
                       deltaPos.inner( Vector(  sin(THETA),  cos(THETA) ) ) * -DISTANCE_SCALE )















