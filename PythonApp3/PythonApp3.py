import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x1 = np.arange(-9,-1)
y1 = -(1/16)*(x1+5)**2+2
x2 = np.arange(1,10,1)
y2 = -(1/16)*(x2-5)**2-3
x3 = np.arange(-9,-1)
y3 = 1/4*(x3+5)**2-3
x4 = np.arange(1,9)
y4 = 1/4*(x4-5)**2-3
x5 = np.arange(-9,-6)
y5 = -(x5+7)**2+5
x6 = np.arange(6,9)
y6 = -(x6-7)**2+5
x7= np.arange(-1,1)
y7=-0.5*(x7**2)+1.5

plt.subplots()
plt.title("очки")
plt.grid(True)

plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7, linewidth=2, color="red")

plt.show()
