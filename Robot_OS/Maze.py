import Tile
import Vector
import serial
import time

class Maze:
    def __init__(self, x, y, comPort):
   
        self.ser = serial.Serial( comPort, 9600 )
        
        initBit = self.ser.inWaiting()
        #t0 = time.clock()
        
        # Just wait for the serial to connect,
        # That is, wait until we see something in the input buffer
        while self.ser.inWaiting() == initBit:
            print( "", end = '' ) # Literally here to do nothing

        #self.loadTime = time.clock() - t0

        #print("creating maze with x = " + str(x) + " and y = " + str(y))
        self.width = x
        self.height = y
        self.tiles = [None] * x
        i = 0
        while (i < x):
            j = 0
            self.tiles[i] = [None] * y
            while(j < y):
                self.tiles[i][j] = Tile.Tile(i, j)
                j += 1
            i += 1
        #self.lastPosition = Vector.Vector(0, 6)

    def SendAcSensorData(self, position, data):
        x = int(position[0])
        y = int(position[1])
        
        if(self.tiles[x][y].UpdateACSensorData(data)):#returns true of state changes
            self.Output()
        
    def Output(self, x, y):
        
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            output = "%d %d %d\n" % ( x, y, self.tile[x][y].GetColor() )
            self.ser.write( output.encode( encoding = "ascii" ) )
        else:
            print( "%d %d %d is out of range!" % ( x, y, self.tile[x][y].GetColor() ) )        
        '''
        if(position != self.lastPosition):
            self.tiles[lastx][lasty].UpdateACSensorData(False)
            self.lastPosition = position
        
        
        lastx = int(self.lastPosition[0])
        lasty = int(self.lastPosition[1])
        '''
