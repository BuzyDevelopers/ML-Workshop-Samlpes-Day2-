from matplotlib import pyplot
import math

def sine(xvals) : 
    y = []
    for i in xvals : 
        y.append(math.sin(i * math.pi / 180))
    pyplot.plot(xvals, y)
    pyplot.show()

def plotLine(x, m, c) :
   y = [(i*m) + c for i in x]
   pyplot.xlabel("X axis")
   pyplot.ylabel("Y axis, y = mx+c")
   pyplot.xlim([0, 30])
   pyplot.ylim([0, 60])
   pyplot.plot(x, y)
   pyplot.show()

#plotLine([0, 1, 2, 3, 4, 5, 6], 2, 1)

sine([i for i in range(0, 360, 15)])