import numpy

weights = numpy.load('Saved.npy')


def sigmoid(z) :
    return 1 / (1 + numpy.exp(-z))

print(weights)

input_ = [[0, 0, 1], [0, 0, 1], [0, 0, 0], [1, 1, 0], [0, 1, 1], [1, 0, 0], [0, 0, 1]]

l1 = numpy.dot(input_, weights)

print(sigmoid(l1))