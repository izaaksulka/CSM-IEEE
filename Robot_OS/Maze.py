from Tile import Tile, WIRE
import Vector
import serial
import time

class Maze:
    def __init__(self, x, y, comPort):
   
        self.ser = serial.Serial( comPort, 9600 )
        
        # Wait for the serial to connect
        initBit = self.ser.inWaiting()
        #t0 = time.clock()
        while self.ser.inWaiting() == initBit:
            print( "", end = '' )
        #self.loadTime = time.clock() - t0

        # Generate the map to be written to
        self.width = x
        self.height = y  
        self.tiles = [] 
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append( Tile(i, j) ) 
            self.tiles.append( row ) 
        
        #self.lastPosition = Vector.Vector(0, 6)

        #Set the starting tile to START state
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
        
        #make sure it is within the bounds to write
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
        	#create the output string
            output = "-1 %d %d %d\n" % ( y, x, self.tiles[x][y].GetColor() )
            #write to the serial 
            self.ser.write( output.encode( encoding = "ascii" ) )
        else:
            print( "%d %d %d is out of range!" % ( y, x, self.tiles[x][y].GetColor() ) )        
        

    def PrintMap(self):
        output = ""
        for i in range( self.width ):
            for j in range( self.height ):
                output += "-1 %d %d %d\n" % (j, i, self.tiles[i][j].GetColor())
                #self.Output( i, j )

        #output += "\n"
        self.ser.write( output.encode( encoding = "ascii" ) )


    def SetEnds(self):
        ends = self.Connect()

        if len(ends) <= 2:#meaning there's no corners here
            for end in ends:
                end.SetState(WIRE) #2 is WIRE, trying importing from Tile at top
            PrintMap()

        else:#meaning that there are more than two ends, so there is a corner
            print("need to handle corners")
            #wait to set LED until gotten to the corner

    def Connect(self):

        ends = []

        #for every tile 1 space from the edge
        for i in range(1, 6):
            
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

        return ends

    def GetAdjTiles(self, pos):
        adjs = []
        if pos[0] == 0:#left
            adjs.append(pos[0] - 1, pos[1])
        if pos[0] < width - 2:#right
            adjs.append(pos[0] + 1, pos[1])
        if pos[1] > 0:#up
            adjs.append(pos[0],     pos[0] - 1)
        if pos[1] < height - 2:#down
            adjs.append(pos[0],     pos[0] + 1)
        return adjs
    def GetAdjWireCount(self, pos):

        adjs = GetAdjTiles(pos)
        i = 0
        for t in adjs:
            if t.IsWire():
                i += 1
        return t

    def Cleanup(self):
        self.ser.close()
