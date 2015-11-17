class player:
    def __init__(self, name, posX, posY):
        self.name = name
        self.positionX = posX
        self.positionY = posY

    # Met de __str__-methode kan je aangeven hoe je deze class wil printen
    def __str__(self):
        return "Player {} is at position ({}, {})".format(self.name, self.positionX, self.positionY)


class stukje:
    def __init__(self, grootte, icoon, locatie):
        self.grootte = grootte
        self.icoon   = icoon
        self.locatie = locatie

    def __str__(self):
        return "{} - {} - {}".format(self.grootte, self.icoon, self.locatie)

# Maak een concrete instance van de stukje-class
stukje1 = stukje(3, "zwaard", 10)

# Maak een paar concrete instances van de player-class
playerOne   = player("P1", 0.0, 10)
playerTwo   = player("P2", 5.0, 0.0)
playerThree = player("P3", 10.0, 0.0)

# Hiermee wordt de __str__-methode aangeroepen
print playerOne

# Zo kun je variabelen van een class aanroepen en printen
print playerOne.name
print playerOne.positionX
