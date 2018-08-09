import numpy
import matplotlib.pyplot as plt

def sigmoid(x, deriv = False):
    
    if deriv:
        return x* (1 - x)
    return 1/(1 + numpy.exp(-x))
    

ip = numpy.array([[0, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])

op = numpy.array([[0, 0, 0, 0, 1, 1, 1, 1]]).T

weights = numpy.random.rand(3, 1) 
error_rate = []; epochs = []
for i in range(0, 10000):
    epochs.append(i)
    X = ip
    l1 = numpy.dot(X, weights)
    y = sigmoid(l1)
    error = op - y 
    error_rate.append(-numpy.mean(error))
    delta_y = error * sigmoid(y, True)
    weights = weights + numpy.dot(X.T, delta_y)

print(y)
numpy.save('Saved.npy', weights)


plt.plot(epochs, error_rate)
plt.show()

