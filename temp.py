#plots with matplotlib
import numpy as np
import matplotlib.pyplot as pl 
data=np.loadtxt("deneme.txt",comments="#")
#print("This is data\n", data)
#print("This is first column\n", data[:,1])

x = data[:,0]
y1 = data[:,1]
y2 = data[:,2]

#making plots
p1, = pl.plot(x,y1,"r")
p2, = pl.plot(x,y2,"b",linewidth=5)

pl.xlim(min(x),max(x))
# pl.ylim(0.02,0.06)

pl.legend((p1,p2),("y1","y2"), loc=(0.3,0.8))