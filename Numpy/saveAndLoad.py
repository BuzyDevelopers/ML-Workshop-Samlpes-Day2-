import numpy


def export(filename, array, type_) :
    
    if type_ == 'npy':
        numpy.save(filename+'.npy', array)
    elif type_ == 'npz':
        numpy.savez(filename+'.npz', array, [1, 2, 4], [1, 2, 4])
    elif type_ == 'txt':
        numpy.savetxt(filename+'.txt', [1, 2, 3])



data = numpy.random.randn(100 , 100, 100, 3)

export('demo', data, 'npy')
export('demo', data, 'npz')
export('demo', data, 'txt')


#loading :

data = numpy.load('demo.npy')
print(data.shape)

data = numpy.load('demo.npz')
print(data.files)
for file in data.files:
    print(data[file].shape)

data = numpy.loadtxt('demo.txt')
print(data.shape)
