
from Vector import Vector
import time
from math import cos, sin, pi
import RPi.GPIO as GPIO


# Number of reading per second
POLL_RATE = 1.0
DELTA_TIME = 1 / POLL_RATE

# Convert mouse distance to feet    
DISTANCE_SCALE = 0.36590066804 * 1.4 / 680 #ft/rot / ticks/rot
#ROTATION_SCALE = -0.900 #degrees per tick.  changed to negative because feedback was backwards
ROTATION_SCALE = -0.13

class MovementFeedback:

    def __init__(self, portA, portB):

        GPIO.setmode(GPIO.BOARD)        

        self.portA = portA
        self.portB = portB

        # Setup the GPIO on RPi
        #GPIO.setmode( GPIO.BOARD )
        GPIO.setup( self.portA, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
        GPIO.setup( self.portB, GPIO.IN, pull_up_down = GPIO.PUD_DOWN )
        
        #print( "Encoder port A: ", self.portA )
        #print( "Encoder port B: ", self.portB )

        self.counter = 0
        self.ALastState = GPIO.input( self.portA )

        self.lastPoll = time.time()
    
        self.timesPolled = 0
    def Update( self, rotation, isRotating ):
    
        self.timesPolled += 1
 
        aState = GPIO.input( self.portA )
        bState = GPIO.input( self.portB )
        
        if aState != self.ALastState:
            if bState != aState:
                self.counter -= 1
            else:
                self.counter += 1
        #print( "Counter: ", self.counter ) 
        self.ALastState = aState 
                    
        #if we have passed the update threshold
        #if time.time() - self.lastPoll > DELTA_TIME:
            #print( "Distance: ", self.counter, "Delta time: ", time.time() - self.lastPoll )
            #print( "Times counted: ", self.timesPolled )
        self.timesPolled = 0
        self.lastPoll = time.time()

        distChange = Vector( 0, 0 )
        rotChange  = 0

            
            #rotating math
        if isRotating:
            rotChange = self.counter * ROTATION_SCALE
            #translating math
        else:
            delX = self.counter *  cos(ToRad(rotation)) * DISTANCE_SCALE
            delY = self.counter * -sin(ToRad(rotation)) * DISTANCE_SCALE
            distChange = Vector( delX, delY )
    
        self.counter = 0

        return ( distChange, rotChange )
        
        #return nothing if enough time hasn't passed
        return ( Vector( 0, 0 ), 0 )

def ToRad(angle):
    return angle * pi / 180

