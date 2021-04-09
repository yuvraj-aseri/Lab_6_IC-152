import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
def mean(x,bins):
    midpoint=[]
    for i in range(len(x)):
        midpoint.append((bins[i]+bins[i+1])/2)
    sums=0
    for i in range(len(x)):
        sums+=(midpoint[i]*x[i])
    return sums/sum(x)
def median(x,bins):
    cf=0
    cf_list=[]
    for i in range(len(x)):
        cf+=x[i]
        cf_list.append(cf)
    N=cf/2
    a=[]
    for i in range(len(x)):
        if cf_list[i]>=N:
            a.append(cf_list[i])
    a.sort()
    b=int(a[0])
    c=int(cf_list.index(b))
    d=bins[c] 
    h=int(int(bins[1])-int(bins[0]))
    f=x[c]
    cfd=cf_list[c-1]
    
    return d+(h*(N-cfd)/f)
def mode(x,bins):
    a=max(x)
    Xk=bins[x.index(a)]
    h=int(int(bins[1])-int(bins[0]))
    b=x[(x.index(a))-1]
    c=x[(x.index(a))+1]
    return Xk+(h*(a-b)/((2*a)-b-c))
bins=list([i for i in range(0,13,2)])
x=list([8,10,18,10,12,6])
z=[]
k=[]
for i,j in zip(bins,x):
    k = [i]*j
    z += k
    k = []
fig, axs = plt.subplots(1, 1,figsize =(10, 7), tight_layout = True)
N, bins, patches = axs.hist(z, bins )
fracs = ((N**(1 / 5)) / N.max())
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
plt.grid(b = True, color ='grey',linestyle ='-.', linewidth = 0.5,alpha = 0.6) 
plt.xlabel("X-axis")
plt.ylabel("y-axis")  
plt.vlines(mean(x,bins), 0, 20, label="mean", colors='red', linestyle='dashed')
plt.vlines(median(x,bins), 0, 20, label='median', colors='blue', linestyle='dashed')
plt.vlines(mode(x,bins), 0, 20, label="mode", colors='black', linestyles='dashed')
plt.legend()
plt.show()