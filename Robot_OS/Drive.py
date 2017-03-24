from math import sqrt
from Vector import Vector
import time
import serial

OFFSET = 40.0                       #minimum write value that results in movement
DRIVE_SCALE = (255 - OFFSET)/100.0  #scaled up to account for the offset

class Drive:
    def __init__(self, comPort):
        # The radius of the drive wheels
        self.wheelR = 1.125
        
        # Wheel baseline (distance from the center of the chassis to the wheel)
        self.b = 5.5 

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

    def SetMotors(self, newMotionTransform):
        #here needs to get the transform from the nav.
        
        self.bodyVel = newMotionTransform.position * DRIVE_SCALE;
        self.bodyRot = newMotionTransform.rotation * DRIVE_SCALE;

        # Do da math 
        rearOut   =  ( self.bodyVel.inner( self.rearDir   ) + self.b * self.bodyRot ) / self.wheelR
        frontROut =  ( self.bodyVel.inner( self.frontRDir ) + self.b * self.bodyRot ) / self.wheelR
        frontLOut =  ( self.bodyVel.inner( self.frontLDir ) + self.b * self.bodyRot ) / self.wheelR

        rearOut += OFFSET * (-1 if rearOut < 0 else 1)
        frontROut += OFFSET * (-1 if frontROut < 0 else 1)
        frontLOut += OFFSET * (-1 if frontLOut < 0 else 1)

        if self.bodyVel != Vector(0.0,0.0) or self.bodyRot != 0.0:
            output = "1 %d %d %d\n" % (int(round(rearOut)), int(round(frontLOut)), int(round(frontROut)));
        else:
            output = "1 %d %d %d\n" % (0,0,0);

        #print("output = " + output);
        print( "Vel: ", self.bodyVel, ", Rot: ", self.bodyRot )

        self.ser.write( output.encode( encoding = "ascii" ) );
        print("post write");
        
        #self.motors[0].setSpeed( rearOut )
        #self.motors[1].setSpeed( frontROut )
        #self.motors[2].setSpeed( frontLOut )
