import pandas
import seaborn
import matplotlib.pyplot as plt
#load dataset:

data = pandas.read_csv(filepath_or_buffer = 'DATA/iris.csv', sep = ',')

#visualize:
x = data['sepal_length']
y = data['sepal_width']

seaborn.regplot(x, y)
plt.show()
