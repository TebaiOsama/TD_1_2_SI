import csv

class Perceptron:
    def __init__(self, n_inputs, n_epochs, learning_rate):
        self.biais = 1
        self.poids_biais = 0;
        self.n_inputs = n_inputs;
        self.w0 = 0;
        self.w1 = 0;
        self.w2 = 0;
        self.n_epochs = n_epochs;
        self.learning_rate = learning_rate;

    def predict(self, input1, input2):
        z = self.biais * self.w0 + input1 * self.w1 + input2 * self.w2;
        if z <= 0:
            return 0;
        else:
            return 1;

    def train(self, input_possibles, output_attendu):
        with open("outputCSV.csv", mode="w", newline='') as outputCSV:
            writer = csv.writer(outputCSV, delimiter=";")
            writer.writerow(("w0", "w1", "w2"))

            for n in range(self.n_epochs):

                for i in range(len(input_possibles)):

                    prediction = self.predict(input_possibles[i][0], input_possibles[i][1]);

                    self.w0 = self.w0 + self.learning_rate*(output_attendu[i]-prediction) * self.biais;
                    self.w1 = self.w1 + self.learning_rate*(output_attendu[i]-prediction) * input_possibles[i][0];
                    self.w2 = self.w2 + self.learning_rate*(output_attendu[i]-prediction) * input_possibles[i][1];

                    writer.writerow((self.w0, self.w1, self.w2))