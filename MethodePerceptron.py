import numpy as np
import matplotlib.pyplot as plt

input_possibles = np.asarray([[0, 0], [0, 1], [1, 0], [1, 1]])
output_possibles = np.asarray([0, 0, 0, 1])



somme = 0
y = 0
error_surface = np.zeros((21, 21))
for w1 in range(-10, 11, 1):
    for w2 in range(-10, 11, 1):
        somme = 0
        for i in range(len(output_possibles)):
            sortie = w1 * input_possibles[i][0] + w2 * input_possibles[i][1]

            if sortie <= 0:
                y = 0
            else:
                y = 1

            somme += 0.5*(y-output_possibles[i])**2
        error_surface[w1+10][w2+10] = somme

print(*error_surface)
plt.imshow(error_surface)
plt.show()

