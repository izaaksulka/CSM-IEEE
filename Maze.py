import Tile;

class Maze:
    def __init__(self, x, y):
        self.tiles = [None] * x;
        i = 0;
        while (i < x):
            j = 0;
            self.tiles[i] = [None] * y;
            while(j < y):
                self.tiles[i][j] = Tile.Tile(i, j);
                j += 1;
            i += 1;
