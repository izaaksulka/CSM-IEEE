import Vector


class Transform:
    def __init__(self):
        self.position = Vector(0.0, 0.0);
        self.rotation = 0.0;

    def __init__(self, newP, newR):
        self.position = newP;
        self.rotation = newR;

    def ToString(self):
        return "pos = " + str(self.position) + "  rot = " + str(self.rotation);
