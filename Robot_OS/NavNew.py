
# Code in the repo
from MovementFeedback import MovementFeedback
from Vector import Vector
from Drive import Drive
import ACDetectorReader
import Maze

# External libraries
from math import pi, cos, sin 
import time

# SERIAL PORTS
DRIVE_PORT = "/dev/ttyACM0"
MAP_PORT = "/dev/ttyUSB0"

# RPi DIGITAL PORTS
# Encoder ports
ENCODER_A = 15 
ENCODER_B = 16
AC_DETECTOR_PORT = 36

PAUSE_DURATION = 2.0 

SCAN_BOARD, OPEN_CACHE, RETURN_HOME = range(4)
RIGHT, LEFT, UP, ROTATE_CW, ROTATE_CCW = range(5)

# Dimensions in feet
BOARD_WIDTH = 7.0
BOARD_HEIGHT = 7.0

# Pre-defined move speeds
STOP = Vector( 0, 0 )
STOP_ROTATION = 0
MOVE_FORWARD = Vector( 0, 200 )
ROTATE_SPEED = 100

class Navigation:
    def __init__(self, startPosition, startRotation):
       
        ############################################
        # INITIALIZE ALL HARDWARE COMPONENTS FIRST #
        ############################################

        # Initialize drive 
        self.drive = Drive( DRIVE_PORT )

        # Initialize the encoders with movement feedback
        self.feedback = MovementFeedback( ENCODER_A, ENCODER_B )

        #initialization of the maze array
        self.maze = Maze.Maze( BOARD_WIDTH, BOARD_HEIGHT, MAP_PORT )

        #Initialize ACDetectorReader
        self.reader = ACDetectorReader.ACDetectorReader( AC_DETECTOR_PORT )

        ##########################
        # INIZIALIZE ROBOT STATE #
        ##########################

        self.position = startPosition
        self.rotation = startRotation
        self.rotating = False

        self.velocity = MOVE_FORWARD
        self.rotVelocity = STOP_ROTATION

        self.targetPos = startPosition
        self.targetAngle = startRotation
    
        # The current algorithm the robot is running
        self.state = SCAN_BOARD

        self.moveQueue = []
        self.PopulateQueue()
  
        ''' I think all this is deprecated
        self.curDirection = RIGHT
        self.curRow = 6 
        self.drive.SetMotors( self.velocity, self.rotVelocity )
        '''   
    def Update(self):
            
            # Update the hardware state
            self.reader.Update()

            ''' This needs to be moved elsewhere
            isRotating = False
            if self.curDirection == ROTATE_CCW or self.curDirection == ROTATE_CW:           
                isRotating = True
            '''
            dr, dAngle = self.feedback.Update(self.rotation, isRotating)
            newPosX = self.position[0] + delta[0][0]
            newPosY = self.position[1] + delta[0][1]
            self.position = Vector( newPosX, newPosY )
            self.rotation += delta[1]
        
            #print( "Cur Pos: ", self.position, ", Cur Rotation: ", self.rotation, ", State: ", self.curDirection )
            
            # Call the appropriate update function based on what algo
            # we're running right now
            if self.state == SCAN_BOARD:
                self.ScanBoard()
            elif self.state == OPEN_CACHE:
                self.maze.PrintMap()
            
            # Tell the chassis what to do now that we've figure that out
            # where we're going

    def ScanBoard(self):
        fin = open( "./moveCommands.txt", 'r' )
        instructions = fin.read()
        fin.close()

        


    # Tells the robot to go forward a set distance
    def SetForward(self, distance):
        self.rotVelocity = STOP_ROTATION
        self.velocity = MOVE_FORWARD

        rotRad = ToRad( self.rotation )
        self.targetPos = ( self.position[0] * distance * cos( rotRad ),
                           self.position[1] * distance * sin( rotRad ) )

        # TODO: Set the motors somewhere

    # Tells the robot to move a certain number of degrees
    def SetRotate(self, deltaAngle):
        self.velocity = STOP
        self.rotVelocity = ROTATE_SPEED * ( -1 if deltaAngle < 0 else 1 )

        # TODO: Set the motors somewhere

    def StopAllMotors(self):
        self.velocity = STOP
        self.rotVelocity = STOP_ROTATION

        # TODO: Set the motors somewhere

    # Closes all serial communications and stops the robot
    def Cleanup(self):
        self.StopAllMotors()
        self.drive.Cleanup()
        self.maze.Cleanup()


    def ToRad(angle):
        return angle * pi / 180.0
