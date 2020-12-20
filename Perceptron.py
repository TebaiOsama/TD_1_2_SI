class Perceptron:
    def __init__(self, n_inputs, n_epochs, learning_rate):
        self.biais = 1
        self.poids_biais = 0;
        self.n_inputs = n_inputs;
        self.poids = [0] * n_inputs;
        self.n_epochs = n_epochs;
        self.learning_rate = learning_rate;

    def predict(self, input1, input2):
        z = input1 * self.poids[0] + input2 * self.poids[1];
        if z <= 0:
            return 0;
        else:
            return 1;

    def train(self, input_possibles, output_attendu):
        for n in self.n_epochs:
            for i in input_possibles:
                prediction = self.predict(input_possibles[i][0], input_possibles[i][1]);
                if prediction > self.biais:
                    for j in self.poids:
                        self.poids[j] = self.poids[j] + self.learning_rate*(output_attendu[i]-prediction)*input_possibles[i][j];
                else:
                    return 0;