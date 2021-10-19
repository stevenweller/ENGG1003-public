# linefitdemo
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def line(x, m, b):
    return m * x + b

np.random.seed(1)   # replicate results by fixing seed
x = np.linspace(0, 100, 100)
y = 3. * x + 2. + np.random.normal(0., 10., 100)
plt.plot(x, y, '.')

popt, pcov = curve_fit(line, x, y)
m = popt[0]
b = popt[1]
print('Straight-line gradient m = {:.2f}'.format(m))
print('Straight-line intercept b = {:.2f}'.format(b))

xfine = np.linspace(0., 100., 100)
plt.plot(xfine, line(xfine, m, b), 'r')
plt.show()