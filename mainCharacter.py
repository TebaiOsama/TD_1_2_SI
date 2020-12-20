import csv
import random
from Character import *
from Army import *

if __name__ == '__main__':

    with open('characters.csv', newline='') as f:
        reader = csv.reader(f)
        liste = list(reader)

    del liste[0];

    liste_personnages = [];
    liste_armees = []

    for i in range(len(liste)):
        liste_personnages.append(Character(liste[i][0], liste[i][1], liste[i][2], liste[i][3], liste[i][4]))

    for i in range(len(liste)):
        liste_armees.append(Army(liste_personnages[i], random.randint(20, 100)))

    print(*liste_armees)

    somme_morale = 0;
    for i in range(len(liste_armees)):
        somme_morale += float(liste_armees[i].getTotalMorale())

    print ("Somme du morale totale : " + str(somme_morale))