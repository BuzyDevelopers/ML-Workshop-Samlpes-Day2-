import numpy

#creating array 1 

array1 = numpy.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

#creating array 2

array2  = numpy.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])



result = numpy.matmul(array1, array2)

print(result)


#understanding shapes : 

array3 = numpy.array([
    [[1, 2, 3], [1, 2, 3]], 
    [[1, 2, 3], [1, 2, 3]], 
    [[1, 2, 3], [1, 2, 3]]
    ])

print(array3.shape)

#now transpose 

array4 = numpy.transpose(array3)

print(array4.shape)


array5 = numpy.array(
    [
        [[1, 2], [1, 2], [1, 2]],
        [[1, 2], [1, 2], [1, 2]],
        [[1, 2], [1, 2], [1, 2]]
    ]
)

print(array5.shape)

array6 = numpy.transpose(array5)

print(array6.shape)


#creating arrays (2)

identity = numpy.eye(10, 10)

print(identity)

zeros = numpy.zeros((20))

print(zeros)