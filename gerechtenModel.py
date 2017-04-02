class Gerecht(object):
    def __init__(self, naam, type, prijs):
        self.naam = naam
        self.type = type
        self.prijs = prijs

    def __str__(self):
        try:
            return self.naam + self.type + str(self.prijs)
        except:
            if AttributeError:
                return ""

    def getNaam(self):
        return self.naam

    def setNaam(self, naam):
        self.naam = naam

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getPrijs(self):
        return self.prijs

    def setPrijs(self, prijs):
        self.prijs = prijs

    def toString(self):
        return "Naam: " + self.naam + ", Type: " + self.type + ", Prijs: " + str(self.prijs)

    # Converteert Gerecht object naar een standaard object
    def serialize(self):
        return {
            'name': self.naam,
            'type': self.type,
            'price': self.prijs,
        }