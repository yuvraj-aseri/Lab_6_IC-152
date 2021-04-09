import matplotlib.pyplot as plt
import numpy as np
 

# Creating dataset
np.random.seed(10)
  
d1 = np.random.normal(100, 10, 100)
d2 = np.random.normal(90, 20, 100)
d3 = np.random.normal(80, 30, 100)
d4 = np.random.normal(70, 40, 100)


 
np.savetxt('q6_boxplot\d1.txt',d1,delimiter=",",fmt='%1.4e')
np.savetxt('q6_boxplot\d2.txt',d2,delimiter=",",fmt='%1.4e')
np.savetxt('q6_boxplot\d3.txt',d3,delimiter=",",fmt='%1.4e')
np.savetxt('q6_boxplot\d4.txt',d4,delimiter=",",fmt='%1.4e')
f1=open('q6_boxplot\d1.txt','r+')
f2=open('q6_boxplot\d2.txt','r+')
f3=open('q6_boxplot\d3.txt','r+')
f4=open('q6_boxplot\d4.txt','r+')
a1=[]
for line in f1.readlines():
    l=float(line)
    a1.append(l)
a2=[]
for line in f2.readlines():
    l=float(line)
    a2.append(l)
a3=[]
for line in f3.readlines():
    l=float(line)
    a3.append(l)
a4=[]
for line in f4.readlines():
    l=float(line)
    a4.append(l)
data = [a1, a2, a3, a4]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_axes([0, 0, 1, 1])
  
bp = ax.boxplot(data)

plt.show()
