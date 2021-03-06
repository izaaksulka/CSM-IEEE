
from math import sqrt
from Vector import Vector
import serial
import time

comPort = "/dev/ttyACM0"

# The radius of the drive wheels
wheelR = 1 

# Wheel baseline (distance from the center of the chassis to the wheel)
b = 1 

# The unit direction vectors of the wheels
rearDir = Vector( 1, 0 ) 
frontRDir = Vector( -0.5, sqrt(3)/2 ) 
frontLDir = Vector( -0.5, -sqrt(3)/2 )


# How we want the body to move
bodyRot = 0 
bodyVel = Vector( 0, 1 ) 

ROT_SPEED = 10 
LIN_SPEED = 255 

# Wait for the serial to connect
ser = serial.Serial( comPort, 9600 )
initBit = ser.inWaiting()
t0 = time.clock()

while ser.inWaiting() == initBit:
    print( "", end = '' )

try:
    while 1:
        setMotor = eval( input( "Select which motor to set (0-5): " ) )

        # Set all the motors
        if setMotor == 3:
            fSpeed = eval( input( "Forward velocity: " ) )
            sSpeed = eval( input( "Sideways velocity: " ) )
            bodyRot = eval( input( "Rotational velocity: " ) )

            bodyVel = Vector( sSpeed, fSpeed )
        
            # Do da math
            rearOut = ( bodyVel.inner( rearDir ) - b * bodyRot ) / wheelR   
            frontROut = ( bodyVel.inner( frontRDir ) - b * bodyRot ) / wheelR 
            frontLOut = ( bodyVel.inner( frontLDir ) - b * bodyRot ) / wheelR 

            output = "1 %d %d %d\n" % ( rearOut, frontROut, frontLOut )
            print( output )
        elif setMotor == 4:
            rSpeed = eval( input( "rear Speed: " ) )
            fRSpeed = eval(input("front Right Speed: "))
            fLSpeed = eval(input("front Left Speed: "))

            output = "1 %d %d %d\n" % (rSpeed, fRSpeed, fLSpeed)
        # Sets the stepper motor to move numSteps steps
        elif setMotor == 5:
            numSteps = eval( input( "Number of steps to move: " ) )
            output = "0 %d\n" % (numSteps)
            print ( "OUTPUT TO STEPPER: " , output )
        else:
            speed = eval( input( "Motor Speed: " ) )

            output = "1 "
            for i in range(3):
                if i == setMotor:
                    output += "%d " % speed
                else:
                    output += "0 "
        output = list( output ) 
        output[-1] = "\n"
        output = "".join(output)

        print( output )
        ser.write( output.encode( encoding = "ascii" ) )        
    
except KeyboardInterrupt:
    pass 

output = "0 0 0 0\n"
ser.write( output.encode( encoding = "ascii" ) )
ser.close()
