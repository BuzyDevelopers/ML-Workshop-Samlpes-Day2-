import numpy
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('barack-obama.jpeg')

array = numpy.array(img)

r = []; g = []; b = []

for i in range(10):
    for j in range(10):
        r.append(array[i][j][0])
        g.append(array[i][j][1])
        b.append(array[i][j][2])

print(array.shape[0]*array.shape[1])
print(len(r))
plt.plot(range(100), r, c = 'r')
plt.plot(range(100), g, c = 'g')
plt.plot(range(100), b, c = 'b')

plt.show()

