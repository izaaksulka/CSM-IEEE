from math import sqrt
from Vector import Vector
import RPi.GPIO as GPIO
import holoMotor as HM
import time
        
class Drive:
    def __init__(self):#have to pass in the nav because this uses its transform
        print("fix me - Drive init");
        # The radius of the drive wheels
        self.wheelR = 1 

        # The unit direction vectors of the wheels
        self.rearDir = Vector( 1, 0 ) 
        self.frontRDir = Vector( -0.5, sqrt(3)/2 ) 
        self.frontLDir = Vector( -0.5, -sqrt(3)/2 )

        # Wheel baseline (distance from the center of the chassis to the wheel)
        self.b = 1
        
        # How we want the body to move
        self.bodyRot = 0 
        self.bodyVel = Vector( 0, 1 ) 

        self.ROT_SPEED = 10 
        self.LIN_SPEED = 255
        print("Creating motors on hard coded values");
        self.motors = [ HM.holoMotor(12, 11), HM.holoMotor(32, 31), HM.holoMotor(33, 36) ]
        #self.nav = newNavModule;
        #self.nav.SetDriver(self);
        
    def SetMotors(self, newMotionTransform):
        #here needs to get the transform from the nav.
        
        self.bodyVel = newMotionTransform.position;
        self.bodyRot = newMotionTransform.rotation;
        self.UpdateSpeeds();

    def UpdateSpeeds(self):
        # Do da math
	rearOut = ( self.bodyVel.inner( self.rearDir ) + self.b * self.bodyRot ) / self.wheelR
	frontROut = ( self.bodyVel.inner( self.frontRDir ) + self.b * self.bodyRot ) / self.wheelR
	frontLOut = ( self.bodyVel.inner( self.frontLDir ) + self.b * self.bodyRot ) / self.wheelR

        self.motors[0].setSpeed( rearOut )
        self.motors[1].setSpeed( frontROut )
	self.motors[2].setSpeed( frontLOut )



"""

GPIO.setmode( GPIO.BOARD )

motors = [ HM.holoMotor(12, 11), HM.holoMotor(32, 31), HM.holoMotor(33, 36) ]

try:
	while 1:
		fSpeed = eval( input( "Forward velocity: " ) )
		sSpeed = eval( input( "Sideways velocity: " ) )
		bodyRot = eval( input( "Rotational velocity: " ) )
		
		bodyVel = Vector( sSpeed, fSpeed )
		
		# Do da math
		rearOut = ( bodyVel.inner( rearDir ) + b * bodyRot ) / wheelR 	
		frontROut = ( bodyVel.inner( frontRDir ) + b * bodyRot ) / wheelR 
		frontLOut = ( bodyVel.inner( frontLDir ) + b * bodyRot ) / wheelR 
	
		# Motors are numberd from the back going ccw
		motors[0].setSpeed( rearOut )
		motors[1].setSpeed( frontROut )
		motors[2].setSpeed( frontLOut )
	
except KeyboardInterrupt:
	pass 

GPIO.cleanup()
	"""	
