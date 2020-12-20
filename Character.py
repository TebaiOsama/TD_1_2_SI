class Character:
    def __init__(self, nom, prenom, age, profession, boost_morale):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boost_morale = boost_morale

    def getNom(self):
        return self.nom;

    def setNom(self, nom):
        self.nom = nom;

    def getPrenom(self):
        return self.prenom;

    def setPrenom(self, prenom):
        self.prenom = prenom;

    def getAge(self):
        return self.age;

    def setAge(self, age):
        self.age = age;

    def getProfession(self):
        return self.profession;

    def setProfession(self, profession):
        self.profession = profession;

    def getBoostMorale(self):
        return self.boost_morale;

    def setBoostMorale(self, boost_morale):
        self.boost_morale = boost_morale;

    def __repr__(self): #toString
        return "\nNom et prenom : " + self.nom + " " + self.prenom + "\nAge : " + self.age + \
               "\nProfession : " + self.profession + "\nBoost de morale : " + self.boost_morale + "\n";

