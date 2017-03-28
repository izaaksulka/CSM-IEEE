from math import sqrt
from Vector import Vector
import time
import serial

# Minimum write value that results in movement
OFFSET = 40.0 


class Drive:
    def __init__(self, comPort):
        # Movement mode is either translate or rotate
        #self.movementMode = NO_MOVEMENT
        # The radius of the drive wheels
        self.wheelR = 1.125
        
        # Wheel baseline (distance from the center of the chassis to the wheel)
        self.b = 1 

        # The unit direction vectors of the wheels
        self.rearDir = Vector( 1, 0 ) 
        self.frontRDir = Vector( -0.5, sqrt(3)/2 ) 
        self.frontLDir = Vector( -0.5, -sqrt(3)/2 )

        #setting up the serial port
        self.ser = serial.Serial( comPort, 9600 )
        initBit = self.ser.inWaiting()
        t0 = time.clock()

        # Just wait for the serial to connect,
        # That is, wait until we see something in the input buffer
        while self.ser.inWaiting() == initBit:
            print( "", end = '' ) # Literally here to do nothing
          
        # How we want the body to move
        self.bodyRot = 0 
        self.bodyVel = Vector( 0, 1 ) 

    def SetMotors(self, velocity, rotVelocity):
        print( "Ding!", " Velocity = ", velocity, " rotVelocity = ", rotVelocity )

        self.bodyVel = Vector( velocity[0], -velocity[1] )
        self.bodyRot = rotVelocity

        # Do da math 
        rearOut   =  ( self.bodyVel.inner( self.rearDir   ) + self.b * self.bodyRot ) / self.wheelR
        frontROut =  ( self.bodyVel.inner( self.frontRDir ) + self.b * self.bodyRot ) / self.wheelR
        frontLOut =  ( self.bodyVel.inner( self.frontLDir ) + self.b * self.bodyRot ) / self.wheelR

        output = "1 %d %d %d\n" % (int(round(rearOut)),
                                   int(round(frontLOut)), 
                                   int(round(frontROut)))
    
        print( "Serial outut: ", output )
        self.ser.write( output.encode( encoding = "ascii" ) )
     
    def Cleanup(self):
        self.SetMotors( Vector(0,0), 0 )
        self.ser.close()
