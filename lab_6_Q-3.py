import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas 
b1 = np.array([43.1,45.3,47.3,30.3,54.1,
               35.6,43.5,31.2,31.4,45.6,
               37.6,40.3,42.2,35.6,36.5,
               36.5,50.2,45.5,45.2,43.1])
b2 = np.array([33.1,35.3,37.3,32.3,44.1,
               31.6,33.5,35.2,30.4,35.6,
               32.6,42.3,40.2,36.6,38.5,
               36.5,30.2,42.5,50.2,40.1])
bin=[i for i in range(30,60,5)]

plt.grid(b = True, color ='grey',linestyle ='-.', linewidth = 0.5,alpha = 0.6)  
plt.hist(b1,bin,color='r')
plt.show()
plt.grid(b = True, color ='grey',linestyle ='-.', linewidth = 0.5,alpha = 0.6)
plt.hist(b2,bin)
plt.show() 
#Bank A is more better than Bank B      
        
