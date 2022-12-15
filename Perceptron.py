import numpy as np

class Perceptron:
  def __init__(self, n_inputs, learning_rate=0.1):
    self.weights = np.zeros(n_inputs + 1)
    self.learning_rate = learning_rate

  def predict(self, inputs):
    weighted_sum = np.dot(inputs, self.weights[1:]) + self.weights[0]
    return 1 if weighted_sum >= 0 else 0

  def train(self, inputs, expected_output):
    prediction = self.predict(inputs)
    error = expected_output - prediction
    self.weights[1:] += self.learning_rate * error * inputs
    self.weights[0] += self.learning_rate * error

# Cria uma instância do Perceptron com duas entradas e taxa de aprendizado 0.1
perceptron = Perceptron(2, learning_rate=0.1)

# Treina o modelo com as entradas [1, 1] e saída esperada 1
perceptron.train([1, 1], 1)

# Faz uma previsão com as entradas [0, 1]
prediction = perceptron.predict([0, 1])
print(prediction)

# Treina o modelo com as entradas [0, 0] e saída esperada 0
perceptron.train([0, 0], 0)

# Faz uma previsão com as entradas [1, 0]
prediction = perceptron.predict([1, 0])
print(prediction)
