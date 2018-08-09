from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.callbacks import TensorBoard
import numpy

(train_X, train_Y) , (test_X,test_Y)  = mnist.load_data()
train_X = numpy.array(train_X, dtype = 'float32')
train_X /= 255
train_X = train_X.reshape(train_X.shape[0],train_X.shape[1]*train_X.shape[2])
train_Y = to_categorical(train_Y, num_classes = 10)

def neuralNetwork():
    model = Sequential()
    model.add(Dense(128, activation = 'relu', input_shape = (784,)))
    model.add(Dense(10, activation = 'softmax'))

    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

    return model

#tfc_c = TensorBoard(log_dir = '.')

NN = neuralNetwork()
NN.fit(train_X, train_Y, epochs = 20)

NN.save('model.h5')