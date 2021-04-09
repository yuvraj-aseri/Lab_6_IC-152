import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
csvdata_1=pd.read_csv('data_for_question2\Class1.txt',sep=' ')
csvdata_2=pd.read_csv('data_for_question2\Class2.txt',sep=' ')
foo=csvdata_1.to_numpy()
data=foo.tolist()
foo1=csvdata_2.to_numpy()
data_1=foo1.tolist()
x=[data[i][0] for i in range(len(data))]
y=[data[i][1] for i in range(len(data))]
y2=[data[i][1]+0.4 for i in range(len(data))]
x1=[data_1[i][0] for i in range(len(data_1))]
y1=[data_1[i][1] for i in range(len(data_1))]
plt.subplot(121)
plt.scatter(x,y,s=25,marker='^')
plt.scatter(x1,y1,s=25 ,marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Before changes:Function f(n)")
plt.plot([-1.5,3],[0,0])
plt.subplot(122)
plt.scatter(x,y2,s=25,marker='^')
plt.scatter(x1,y1,s=25 ,marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("After changes:Function f(n)")
plt.plot([-1.5,3],[0,0],color='k')
plt.show()

def mean(x):
    count=0
    for i in x:
        count+=i
    return (count/len(x))
print(mean(x))
 
   
    