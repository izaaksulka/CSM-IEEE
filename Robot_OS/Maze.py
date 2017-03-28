from Tile import Tile
import Vector
import serial
import time
from Tile import WIRE

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
        #self.GetEnds()        
    def SendAcSensorData(self, position, data):
        x = int(position[0])
        y = int(position[1])
        
        if(self.tiles[x][y].UpdateACSensorData(data)):#returns true of state changes
            #self.Output(x, y)
            self.PrintMap()
        
    def Output(self, x, y):
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            output = "-1 %d %d %d\n" % ( y, x, self.tiles[x][y].GetColor() )
            #print( "To Map: ", output ) 
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
        output = ""
        for i in range( self.width ):
            for j in range( self.height ):
                output += "-1 %d %d %d\n" % (i, j, self.tiles[i][j].GetColor())
                #self.Output( i, j )

        #output += "\n"
        self.ser.write( output.encode( encoding = "ascii" ) )
    def GetEnds(self):
        ends = self.Connect()
        if len(ends) < 2:
            print( "Oh god something's wrong.  there's less than 2 end points")
            #do something to handle that there are not enough end points
        elif len(ends) == 2:#meaning there's no corners here
            for end in ends:
                end.SetState(WIRE) #2 is WIRE, trying importing from Tile at top
        else:#meaning that there are more than two ends, so there is a corner
            print("need to handle corners")
            
        return ends
    def Connect(self):
        ends = []
        #for every tile 1 space from the edge
        for i in range(1, 6):
            #top row
            if (self.tiles[i][1].IsWire()):#Across the top
                if GetAdjWireCount(i, 1) == 1:
                    ends.append(i, 0)
            if (self.tiles[i][5].IsWire()):#Across the bottom
                if GetAdjWireCount(i, 5) == 1:
                    ends.append(i, 6)
            if (self.tiles[1][i].IsWire()):#Down the left side
                if GetAdjWireCount(1, i) == 1:
                    ends.append(0, i)
            if (self.tiles[5][i].IsWire()):#Down the right side
                if GetAdjWireCount(5, i) == 1:
                    ends.append(6, i)
        if(len(ends) == 2):
            return ends
        #if the length of ends was not equal to 2 then have to figure out what to do next
        print("found some corners")
        return ends
       # print( "Connect ends found: ", len(ends) )
       # print( "Hello world!" )    
        
    def GetAdjTiles(self, pos):
        adjs = []
        if pos[0] > 0:#left
            adjs.append(pos[0] - 1, pos[1])
        if pos[0] < width - 1:#right
            adjs.append(pos[0] + 1, pos[1])
        if pos[1] > 0:#up
            adjs.append(pos[0],     pos[0] - 1)
        if pos[1] < height - 1:#down
            adjs.append(pos[0],     pos[0] + 1)
        return adjs
    def GetAdjWireCount(self, pos):
        adjs = GetAdjTiles(pos)
        i = 0
        for t in adjs:
            if t.IsWire():
                i += 1
        return t





