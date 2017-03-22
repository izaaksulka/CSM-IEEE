
from math import sqrt
from Vector import Vector
import RPi.GPIO as GPIO
import holoMotor as HM
import time
# The radius of the drive wheels
wheelR = 1 

# The unit direction vectors of the wheels
rearDir = Vector( 1, 0 ) 
frontRDir = Vector( -0.5, sqrt(3)/2 ) 
frontLDir = Vector( -0.5, -sqrt(3)/2 ) 

# Wheel baseline (distance from the center of the chassis to the wheel)
b = 1 

# How we want the body to move
bodyRot = 0 
bodyVel = Vector( 0, 1 ) 

ROT_SPEED = 10 
LIN_SPEED = 255 



GPIO.setmode( GPIO.BOARD )

motors = [ HM.holoMotor(12, 11), HM.holoMotor(32, 31), HM.holoMotor(33, 36) ]
GPIO.setup( 16, GPIO.IN )

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
		
