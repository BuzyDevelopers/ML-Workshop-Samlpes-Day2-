import numpy

def sigmoid(z) :
    return 1 / (1 + numpy.exp( - z))

z = numpy.random.randint(0, 2, (30, 30))

print(sigmoid(z))


#built in functions : 
z = numpy.log10([10 , 10, 10, 10])

print(z)

