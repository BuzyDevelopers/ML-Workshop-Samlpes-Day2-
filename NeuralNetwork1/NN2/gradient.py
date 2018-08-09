import numpy
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [2, 5, 6, 9, 10, 12, 13, 16]

lr = 0.001

w = numpy.random.rand()
b = numpy.random.rand()

print(w, b)

for i in range(0, 100000):

    #predict and compute loss:
    cost = 0; deriv_w_sum = 0; deriv_b_sum = 0
    for j in range(len(X)):

        z = w*X[j] + b
        error  = (z - Y[j])**2
        cost += error
        
        derivative_w = 2*(z - Y[j])*X[j]
        derivative_b = 2*(z - Y[j])

        deriv_w_sum += derivative_w
        deriv_b_sum += derivative_b

    w = w - lr * deriv_w_sum
    b = b - lr * deriv_b_sum


#prediction:
print(w, b)

#lets plot it:

#test for some output :

op = w * 6 + b

print(op)

y = [i * w + b for i in X]

plt.scatter(X, Y, c = 'b')
plt.plot(X, y, c = 'r')
plt.show()