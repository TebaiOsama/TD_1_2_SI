class Army:
    def __init__(self, chef, morale_basique):
        self.chef = chef
        self.morale_basique = morale_basique

    def getChef(self):
        return self.chef

    def setChef(self, chef):
        self.chef = chef

    def getMoraleBasique(self):
        return self.morale_basique

    def setMoraleBasique(self, morale_basique):
        self.morale_basique = morale_basique

    def getTotalMorale(self):
        return float(self.morale_basique*float(self.chef.getBoostMorale()))

    def __repr__(self):
        return "\nChef : " + str(self.chef.getNom()) + " " + str(self.chef.getPrenom())\
               + ", Morale de base : " + str(self.morale_basique)






