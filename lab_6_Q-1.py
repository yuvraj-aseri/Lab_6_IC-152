#1
def square(number):
    return number**2
def correl(x,y):
    a=sum(x)
    b=sum(y)
    n=len(x)
    d=sum(list(map(square,x)))
    e=sum(list(map(square,y)))
    c=0
    for i in range(n):
        c+=x[i]*y[i]
    f=((n*c)-(a*b))/((((n*d)-a**2)**0.5)*(((n*e)-b**2)**0.5))
    print(f) 
x=[3,-1,6,12,8,10,9,13,15,-3,0,-5,-2,16]
y=[4,-2,5,11,6,11,7,8,9,-4,1,-6,-1,14]
x1=[3,-1,6,12,8,10,9,-5,-2,4,2,0,14,11]
y1=[0,2,-3,4,0,1,2,-1,-2,2,1,-2,9,2]
x2=[3,4,2,5,8,-8,-6,-1,0,-5,4,2,6,8]
y2=[5,-1,0,1,2,2,4,2,1,2,1,2,-4,4]
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
plt.subplot(131)
plt.scatter(x,y,s=25,color='r')
plt.xlabel('x',fontweight='bold')
plt.ylabel('y',fontweight='bold')
plt.subplot(132)
plt.scatter(x1,y1,s=25,color='b')
plt.xlabel('x',fontweight='bold')
plt.ylabel('y',fontweight='bold')
plt.subplot(133)
plt.scatter(x2,y2,s=25,color='k')
plt.xlabel('x',fontweight='bold')
plt.ylabel('y',fontweight='bold')
plt.show()