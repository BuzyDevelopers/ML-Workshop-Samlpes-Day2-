import numpy

#random array of desired shape: 

a = numpy.random.rand(100, 100, 3)

print(a)

print(a.shape)


#some random functions:
#generate random integers
b = numpy.random.randint(10 , 20, (10, 3, 3))

print(b)


#distributions: 

#standard normal distribution
c = numpy.random.randn(300)

print(c)

d = numpy.random.poisson(lam = 0.2, size = (3))

print(d)

#and many others