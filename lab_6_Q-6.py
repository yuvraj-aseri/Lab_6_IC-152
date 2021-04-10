import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
style.use('ggplot')
data1 = pd.read_csv('d1.txt', sep=' ', header=None)
data2 = pd.read_csv('d2.txt', sep=' ', header=None)
data3 = pd.read_csv('d3.txt', sep=' ', header=None)
data4 = pd.read_csv('d4.txt', sep=' ', header=None)
data = [data1[0], data2[0], data3[0], data4[0]]
t=np.arange(len(data)+1)
a=[" ","data-1","data-2","data-3","data-4"]
plt.boxplot(data)
plt.xlabel("Data file")
plt.ylabel("Values")
plt.title("Boxplot for data files")
plt.xticks(t,a)
plt.show() 


