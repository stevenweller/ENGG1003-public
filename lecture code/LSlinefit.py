import numpy as np
import matplotlib.pyplot as plt

def line(x, m, b):
    return m * x + b

x = np.array([20.5, 32.7, 51.0, 73.2, 95.7])    # temp (degC)
y = np.array([765, 826, 873, 942, 1032])  # resistance (ohms)
plt.plot(x, y, '.', markersize=10)

N = len(x)
xbar = np.mean(x)
ybar = np.mean(y)
mnum = 0    # numerator of m
mden = 0    # denominator of m
for k in range(0,N):
    mnum += (x[k]-xbar)*(y[k]-ybar)
    mden += (x[k]-xbar)**2
m = mnum/mden
b = ybar - m*xbar

xfine = np.linspace(0., 100., 100)
plt.plot(xfine, line(xfine, m, b), 'r')
plt.title('y = {:.2f} x + {:.0f} '.format(m, b))
plt.xlabel('x')
plt.ylabel('y')
plt.show()