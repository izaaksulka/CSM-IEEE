from Tile import Tile
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
        
        self.tiles = [] 
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append( Tile(i, j) ) 
            self.tiles.append( row ) 
        #self.tiles = [ [Tile() for j in range(y)] for i in range(x)]
        
        ''' 
        self.tiles = [None] * x
        i = 0
        while (i < x):
            j = 0
            self.tiles[i] = [None] * y
            while(j < y):
                
                self.tiles[i][j] = Tile(i, j)
                j += 1
            i += 1
        '''
        #self.lastPosition = Vector.Vector(0, 6)

        self.tiles[0][6].SetState(0)
        #self.Output( 0, 6 )  
        self.PrintMap()
        self.Connect()        
    def SendAcSensorData(self, position, data):
        x = int(position[0])
        y = int(position[1])
        
        if(self.tiles[x][y].UpdateACSensorData(data)):#returns true of state changes
            #self.Output(x, y)
            self.PrintMap()
        
    def Output(self, x, y):
        
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            output = "-1 %d %d %d\n" % ( y, x, self.tiles[x][y].GetColor() )
            print( "To Map: ", output ) 
            self.ser.write( output.encode( encoding = "ascii" ) )
        else:
            print( "%d %d %d is out of range!" % ( y, x, self.tiles[x][y].GetColor() ) )        
        '''
        if(position != self.lastPosition):
            self.tiles[lastx][lasty].UpdateACSensorData(False)
            self.lastPosition = position
        
        
        lastx = int(self.lastPosition[0])
        lasty = int(self.lastPosition[1])
        '''
    def PrintMap(self):
        #output = ""
        for i in range( self.width ):
            for j in range( self.height ):
                #output += "%d %d %d\n" % (i, j, self.tiles[i][j].GetColor())
                self.Output( i, j )

        #output += "\n"
        #self.ser.write( output.encode( encoding = "ascii" ) )

    def Connect(self):
        ends = []
        #for every tile 1 space from the edge
        for i in range(1, 6):
            #top row
            if (self.tiles[i][1].GetState() == Tile.WIRE):
                ends.append(i, 0)
            if (self.tiles[i][5].GetState() == Tile.WIRE):
                ends.append(i, 6)

        print( "Hello world!" )    
        







