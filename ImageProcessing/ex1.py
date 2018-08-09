from PIL import Image
import numpy


#load image :

img = Image.open('barack-obama.jpeg')

array = numpy.array(img)

reduce_factor = 0.45

array = array*reduce_factor

img = Image.fromarray(array.astype('uint8'))

img.save('new.png')

#cropping the image:
img = Image.open('barack-obama.jpeg')

array = numpy.array(img)

array = array[30 : 800, 90:800, 0:3]

img = Image.fromarray(array.astype('uint8'))
img.save('new1.png')


#nullify all blue pixels :
img = Image.open('barack-obama.jpeg') 
array = numpy.array(img)
print(array.shape)
for i in range(array.shape[0]):
    for j in range(array.shape[1]) :
        #print('Pixel : ', i, j)
        array[i][j][0] = 0
        array[i][j][1] = 0

img = Image.fromarray(array.astype('uint8'))

img.save('ex3.png')