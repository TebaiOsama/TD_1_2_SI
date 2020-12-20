import numpy as np
import random
import csv

liste_morale_armees = np.array([random.uniform(20, 100), random.uniform(20, 100), random.uniform(20, 100), random.uniform(20, 100), random.uniform(20, 100)])

liste_test = np.genfromtxt('characters.csv', delimiter=',')[1:,4]

somme_moral = liste_morale_armees.dot(liste_test);

print (somme_moral)