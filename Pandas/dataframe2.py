import pandas
import matplotlib.pyplot as plt 
import seaborn
import numpy

dataset = {
    "weight" : [70, 50, 80, 60, 75, 50, 55, 50, 70],
    "height" : [5.3, 5, 6, 5.7, 5.1, 4.9, 5.0, 5.4, 5.5],
    "gender" : ['female', 'male', 'male', 'female', 'male', 'female', 'female', 'female', 'male']
}

def getDatFrame(data) :
    return pandas.DataFrame(data)

def visualize(data) :

    x = data['weight']
    y = data['height']

    colors = []
    for data in dataset['gender']:
        if data == 'female' : colors.append('b')
        else : colors.append('r')

    area = 30
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.scatter(x = x, y = y, s = area, c = colors)
    plt.show()


data = getDatFrame(dataset)
visualize(data)