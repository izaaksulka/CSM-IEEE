import Tile;
import Vector;

class Maze:
    def __init__(self, x, y):
        #print("creating maze with x = " + str(x) + " and y = " + str(y));
        self.tiles = [None] * x;
        i = 0;
        while (i < x):
            j = 0;
            self.tiles[i] = [None] * y;
            while(j < y):
                self.tiles[i][j] = Tile.Tile(i, j);
                j += 1;
            i += 1;
        self.lastPosition = Vector.Vector(0, 6);

    def SendAcSensorData(self, position, data):
        x = int(position[0]);
        y = int(position[1]);
        #print("x = " + str(x));
        #print("y = " + str(y));
        lastx = int(self.lastPosition[0]);
        lasty = int(self.lastPosition[1]);
        self.tiles[x][y].UpdateACSensorData(data);
        if(position != self.lastPosition):
            self.tiles[lastx][lasty].UpdateACSensorData(False);
            self.lastPosition = position;
