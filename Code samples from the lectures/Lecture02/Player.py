class player:
    def __init__(self, name, posX, posY):
        self.name = name
        self.positionX = posX
        self.positionY = posY


playerOne   = player("P1", 0.0, 10)
playerTwo   = player("P2", 5.0, 0.0)
playerThree = player("P3", 10.0, 0.0)

print playerOne
