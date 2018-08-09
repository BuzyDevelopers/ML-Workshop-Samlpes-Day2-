import seaborn
import matplotlib.pyplot as plt

data = seaborn.load_dataset('iris')

seaborn.pairplot(data, hue = 'species', size = 2.5)
plt.show()