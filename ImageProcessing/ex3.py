import numpy
from PIL import Image


#generating random images

image_array = numpy.random.randint(10, 255, size = (100, 100, 3))
print(image_array.shape)
img = Image.fromarray(image_array.astype('uint8'))
img = img.resize((1000, 1000))
img.save('gen.png')