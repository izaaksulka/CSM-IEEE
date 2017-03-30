
# Code in the repo
from MovementFeedback import MovementFeedback
from Vector import Vector
from Drive import Drive
import ACDetectorReader
import Maze
from sevenSegment import SevenSegment


# External libraries
from collections import deque
from math import pi, cos, sin, copysign
import time

# SERIAL PORTS
DRIVE_PORT = "/dev/ttyACM0"
MAP_PORT = "/dev/ttyUSB0"

# RPi DIGITAL PORTS
# Encoder ports
ENCODER_A = 15 
ENCODER_B = 16
AC_DETECTOR_PORT = 36

''' Probably deprecated
PAUSE_DURATION = 2.0 
'''
LINEAR_ERROR = 0.1
ROTATION_ERROR = 0.5

SCAN_BOARD, OPEN_CACHE, RETURN_HOME = range(3)
READY, PAUSED, TRANSLATING, ROTATING, FINISHED = range(5)

# Dimensions in feet
BOARD_WIDTH = 7
BOARD_HEIGHT = 7

# Pre-defined move speeds
STOP = Vector( 0, 0 )
STOP_ROTATION = 0
MOVE_FORWARD = Vector( 0, 175 )
ROTATE_SPEED = 125

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

        self.sevenSegment = SevenSegment()

        ##########################
        # INIZIALIZE ROBOT STATE #
        ##########################

        self.position = startPosition
        self.rotation = startRotation
        self.isRotating = False

        self.velocity = MOVE_FORWARD
        self.rotVelocity = STOP_ROTATION

        self.targetPos = startPosition
        self.targetAngle = startRotation
        self.startPause = time.time()
        self.targetTime = time.time()
    
        # The current algorithm the robot is running
        self.nextState = SCAN_BOARD
        self.moveState = READY

        self.moveQueue = deque( [] )
        #self.PopulateQueue()
        self.counter = 0
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
            dr, dAngle = self.feedback.Update(self.rotation, self.isRotating)
            newPosX = self.position[0] + dr[0]
            newPosY = self.position[1] + dr[1]
            self.position = Vector( newPosX, newPosY )
            self.rotation += dAngle
        

            
            # If we've just started the program
            # or finished all of the instructions from
            # the last algorithm
            if self.moveState == READY or self.moveState == FINISHED:
                # Call the appropriate update function based on what algo
                # we're running right now
                if self.nextState == SCAN_BOARD:
                    self.ScanBoard()
                    self.NextCommand()
                    self.nextState = OPEN_CACHE
                elif self.nextState == OPEN_CACHE:
                    self.maze.SetEnds()
                    self.maze.PrintMap()
                    self.sevenSegment.SetRandomNumber()
                    # Set next state here
           # self.
            self.counter += 1      
            if self.counter == 2500:
                self.counter = 0
                print("state: ", self.moveState) 
                print("Position ", self.position,  " Cur Rotation: ", self.rotation, "MoveState: " , self.moveState )
               
                print("target pos = ", self.targetPos)
                 #print("target angle = ", self.targetAngle)
             # print( "Error: ", (self.position - self.targetPos).norm(), "Threshold: ", LINEAR_ERROR )
            #if(self.moveState == ROTATING):
            #    print("rotating")
            if self.moveState == TRANSLATING and (self.position - self.targetPos).norm() < LINEAR_ERROR:
                self.NextCommand()
                
            elif self.moveState == ROTATING and abs( self.rotation - self.targetAngle ) < ROTATION_ERROR:
                
                self.NextCommand()

            elif self.moveState == PAUSED and time.time() > self.targetTime:
                self.NextCommand()
            

            if self.moveState == PAUSED and self.nextState == OPEN_CACHE and time.time() - self.startPause > 0.5:
                self.maze.SendAcSensorData( self.position, self.reader.GetSensorValue() )
            # Tell the chassis what to do now that we've figure that out
            # where we're going

    # Dequeues the next command and sets motors accordingly
    def NextCommand(self):
        if len( self.moveQueue ) != 0:
            nextCommand = self.moveQueue.popleft()
            print("Next command type: ", nextCommand[0])
            if nextCommand[0] == "FWD":
                self.SetForward( nextCommand[1] )
            elif nextCommand[0] == "ROT":
                self.SetRotate( nextCommand[1] )
            elif nextCommand[0] == "PAUSE":
                self.SetPause( nextCommand[1] )
            elif nextCommand[0] == "FWT":
                self.SetForwardTimed( nextCommand[1] )

            self.drive.SetMotors( self.velocity, self.rotVelocity )
        else:
            self.moveState = FINISHED
            self.SetPause( 1.0 ) 


    # Reads in and enqueues commands for scan board mode
    def ScanBoard(self):
        fin = open( "./moveCommands.txt", 'r' )
        contents = fin.read()
        fin.close()

        # Split the file into individual instructions
        # and add those instructions to the queue
        for instruction in contents.split("\n"):
            if len( instruction ) != 0:
                cmd, duration = instruction.split()
                duration = float( duration )
                self.moveQueue.append( (cmd, duration) )

    # Tells the robot to go forward a set distance
    def SetForward(self, distance):
        self.rotVelocity = STOP_ROTATION
        direction = copysign( 1, distance )
        self.velocity = direction * MOVE_FORWARD
        self.moveState = TRANSLATING
        self.isRotating = False

        prevRotation = round(self.rotation / 45) * 45
        rotRad = ToRad( prevRotation )

        self.targetPos = ( self.targetPos[0] + distance *  cos( rotRad ),
                           self.targetPos[1] + distance * -sin( rotRad ) )

        # TODO: Set the motors somewhere

    def SetForwardTimed(self, duration):
        self.rotVelocity = STOP_ROTATION
        self.velocity = MOVE_FORWARD
        self.isRotating = False

        self.moveState = PAUSED
        self.isRotating = False
        self.targetTime = time.time() + duration
        
        prevRotation = round(self.rotation / 45) * 45
        rotRad = ToRad( prevRotation )

        self.targetPos = ( self.targetPos[0] +  cos( rotRad ),
                           self.targetPos[1] + -sin( rotRad ) )
        
        if self.position[0] > 3.5:
            self.position = Vector( 6.5, self.position[1] )
        else:
            self.position = Vector( 0.5, self.position[1] )

    # Tells the robot to move a certain number of degrees
    def SetRotate(self, targetAngle):
        self.velocity = STOP
        self.rotVelocity = ROTATE_SPEED * ( -1 if targetAngle - self.rotation < 0 else 1 )
        self.moveState = ROTATING
        self.isRotating = True
        #self.targetAngle = self.rotation + deltaAngle
        self.targetAngle = targetAngle
        # TODO: Set the motors somewhere

    def SetPause(self, duration):
        self.velocity = STOP
        self.rotVelocity = STOP_ROTATION
        self.moveState = PAUSED
        self.isRotating = False
        self.startPause = time.time()
        self.targetTime = time.time() + duration

        # TODO: Set the motors somewhere
        # TODO: Start a timer somewhere
        # TODO: Read AC sensor somewhere

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
