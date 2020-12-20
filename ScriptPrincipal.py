from Perceptron import *

if __name__ == '__main__':
    inputs_possibles = [[0, 0], [0, 1], [1, 0], [1, 1]]

    sorties_attendues = [0, 0, 0, 1]

    perceptron = Perceptron(4, 50, 0.1)
    perceptron.train(inputs_possibles, sorties_attendues)
    print(perceptron.predict(0,0));
    print(perceptron.predict(0,1));
    print(perceptron.predict(1,0));
    print(perceptron.predict(1,1));