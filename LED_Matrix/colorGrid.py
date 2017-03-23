
import serial
import time
from enum import Enum

class colorGrid:

    WIDTH = 8
    HEIGHT = 8
    
    # All the possible states of a tile
    OFF = 0
    GREEN = 1
    RED = 2
    BLUE = 3

    # Setup serial connection in specified COM port
    def __init__( self, comPort ):
        self.ser = serial.Serial( comPort, 9600 )
        
        initBit = self.ser.inWaiting()
        t0 = time.clock()

        # Just wait for the serial to connect,
        # That is, wait until we see something in the input buffer
        while self.ser.inWaiting() == initBit:
            print( "", end = '' ) # Literally here to do nothing

        self.loadTime = time.clock() - t0

    # Print info, if you like
    def printInfo( self ):
        print( "Using port: " + self.ser.name )
        print( "Loading took %.2f seconds" % ( self.loadTime ) )

    # Color a tile at the x,y coordinate
    def setTile( self, x, y, color ):

        if x >= 0 and x < self.WIDTH and y >= 0 and y < self.HEIGHT:
            output = "%d %d %d\n" % ( x, y, color )
            self.ser.write( output.encode( encoding = "ascii" ) )
        else:
            print( "%d %d %d is out of range!" % ( x, y, color ) )        
    
    # Close serial connection, do whatever else we need to
    def cleanup( self ):
        self.ser.close()    
