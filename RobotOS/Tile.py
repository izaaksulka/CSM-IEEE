
foam, wire, void, target = range(4);
class Tile:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.state = foam;
        self.PrintTile();

    def SetState(self, newState):
        state = newState;

        
    def PrintTile(self):
        print("Tile: x = " + str(self.x) + " y = " + str(self.y) + " --- " + self.StateToString(self.state));

    def StateToString(self, state):
        if(state == foam):
            return "Foam";
        if(state == wire):
            return "Wire";
        if(state == void):
            return "Void";
        if(state == target):
            return "Target";
        
