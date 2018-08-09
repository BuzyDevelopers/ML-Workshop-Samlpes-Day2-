import pandas
import numpy
import matplotlib.pyplot as pl
import seaborn

dataset = {
    "x" : [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "y" : [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

def visulaize(dataframe) :
    seaborn.lineplot(dataframe['x'], dataframe['y'])
    pl.show()

def createDataFrame(dataset) :

    return pandas.DataFrame(dataset)


data = createDataFrame(dataset)
visulaize(data)