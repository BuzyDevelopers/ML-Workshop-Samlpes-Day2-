import numpy
from matplotlib import pyplot


def scatterData(N, area) :
    x = numpy.random.rand(N)
    y = numpy.random.rand(N)

    colors = numpy.random.rand(N)
    area = (area*numpy.random.rand(N))**2
    return (x, y, colors, area)


x, y, colors, area = scatterData(60, 30)

pyplot.scatter(x = x, y = y, s = area, c = colors)

pyplot.show()
