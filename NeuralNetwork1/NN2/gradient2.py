import numpy
import matplotlib.pyplot as plt 

X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [2, 5, 6, 9, 10, 12, 13, 16]

w = numpy.random.rand()
b = numpy.random.rand()

for i in range(0, 10000):
    deriv_C = 0
    for j in range(len(X)):

        z = w*X[j] + b 

        error = (z - Y[j])**2

        deriv = 2 * (z - Y[j])
        deriv_C += deriv

    
