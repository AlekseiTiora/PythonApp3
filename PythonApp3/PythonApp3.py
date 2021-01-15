import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x1 = np.arange(-9,-1)
y1 = (-1/16)*(x1+5)**2+2
x2 = np.arange(1,10,1)
y2 = (-1/16)*(x2-5)**2+2
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


#babo4ka------------------------------------

x_1 = np.arange(-9,-1)
y_1= (-1/8)*(x_1+9)**2+8
x_2 = np.arange(1,9)
y_2=(-1/8)*(x_2-9)**2+8
x_3= np.arange(-9,-8)
y_3= 7*(x_3+8)**2+1
x_4 = np.arange(8,9)
y_4= 7*(x_4-8)**2+1
x_5 = np.arange(-8,-1)
y_5= 1/49*(x_5+1)**2
x_6= np.arange(1,8)
y_6= 1/49*(x_6-1)**2
x_7 = np.arange(-8,-1)
y_7 = (-4/49)*(x_7+1)**2
x_8 = np.arange(1,8)
y_8= (-4/49)*(x_8-1)**2
x_9 = np.arange(-8,-2)
y_9= 1/3*(x_9+5)**2-7
x_10 = np.arange(2,8)
y_10= 1/3*(x_10-5)**2-7
x_11 = np.arange(-2,-1)
y_11 = -2*(x_11+1)**2-2
x_12 = np.arange(1,2)
y_12=-2*(x_12-1)**2-2
x_13 = np.arange(-1,1)
y_13= -4*x_13**2+2
x_14 = np.arange(-1,1)
y_14= -4*x_14**2-6
x_15 = np.arange (-2,0)
y_15= -1.5*x_15+2
x_16 = np.arange(0,2)
y_16= 1.5*x_16+2

plt.subplots()
plt.title("бабочка")
plt.grid(True)

plt.plot(x_1,y_1,x_2,y_2,x_3,y_3,x_4,y_4,x_5,y_5,x_6,y_6,x_7,y_7,x_8,y_8,x_9,y_10,x_11,y_11,x_12,y_12,x_13,y_13,x_14,y_14,x_15,y_15,x_16,y_16, linewidth=2, color="red")

plt.show()
