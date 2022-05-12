import numpy as np
import matplotlib.pyplot as plt


def line(x, m, b):
    return m * x + b


# temperature (degC)
x = np.array([20.5, 32.7, 51.0, 73.2, 95.7])
# resistance (ohms)
y = np.array([765, 826, 873, 942, 1032])
plt.plot(x, y, 'r.', markersize=15)

N = len(x)
xbar = np.mean(x)
ybar = np.mean(y)
mnum = 0    # numerator of m
mden = 0    # denominator of m
for k in range(0, N):
    mnum += (x[k]-xbar)*(y[k]-ybar)
    mden += (x[k]-xbar)**2
m = mnum/mden
b = ybar - m*xbar
print("m = {:.2f}, b = {:.0f}".format(m, b))

xfine = np.linspace(0., 100., 100)
plt.plot(xfine, line(xfine, m, b), 'b')
plt.title('y = {:.2f} x + {:.0f} '.format(m, b))
plt.xlabel('x')
plt.ylabel('y')
plt.show()