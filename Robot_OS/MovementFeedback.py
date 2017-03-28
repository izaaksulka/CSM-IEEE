
from Vector import Vector
import time
from math import cos, sin, pi
import RPi.GPIO as GPIO


# Number of reading per second
POLL_RATE = 1000.0
DELTA_TIME = 1 / POLL_RATE

# Convert mouse distance to feet    
DISTANCE_SCALE = 0.036590066804 / 680 #ft/rot / ticks/rot
ROTATION_SCALE = 0.900 #degrees per tick


class MovementFeedback:

    def __init__(self, portA, portB):

        # Setup the GPIO on RPi
        GPIO.setmode( GPIO.BOARD )
        GPIO.setup( ENC_A, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
        GPIO.setup( ENC_B, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )

        self.counter = 0
        self.ALastState = GPIO.input( ENC_A )

        self.lastPoll = time.time()

    def Update( self, rotation, isRotating ):
     
        aState = GPIO.input( ENC_A )
        bState = GPIO.input( ENC_B )
        
        if aState != self.ALastState:
            if bState != aState:
                self.counter += 1
            else:
                self.counter -= 1
       
        self.ALastState = aState 
            
        #if we have passed the update threshold
        if time.time() - self.lastPoll > DELTA_TIME:
            self.lastPoll = time.time()

            distChange = Vector( 0, 0 )
            rotChange  = 0


            #rotating math
            if isRotating:
                rotChange = self.counter * ROTATION_SCALE
            #translating math
            else:
                delX = self.counter *  cos(toRad(rotation)) * DISTANCE_SCALE
                delY = self.counter * -sin(toRad(rotation)) * DISTANCE_SCALE
                distChange = Vector( delX, delY )
    
            self.counter = 0

            return ( distChange, rotChange )
        
        #return nothing if enough time hasn't passed
        return ( Vector( 0, 0 ), 0 )



