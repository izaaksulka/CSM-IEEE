
class Maze:
    def __init__(self, x, y):
        self.tiles = [x];
        i = 0;
        while (i < x):
            self.tiles[i] = [];
            i += 1;
