class player:
    def __init__(self, name, pos):
        self.name = name
        self.position = pos

class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

position1 = position(0.0, 10)
playerOne   = player("P1", position1)

