import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt


# fit a parabola to data
def parabola(x, a, b, c):
    return a*x**2 + b*x + c


np.random.seed(1)
# data is actually a cubic + noise
x = np.linspace(-4, 4, 100)
y = -4*x**3 + 3*x**2 + 25*x + 6 + np.random.normal(0., 10, len(x))
plt.plot(x, y, 'r.')

popt, _ = sco.curve_fit(parabola, x, y)
a = popt[0]
b = popt[1]
c = popt[2]

plt.plot(x, parabola(x, a, b, c), 'b')
plt.title('Best fit parabola: {:.2f}x**2 + {:.2f}x + {:.2f}'.format(a, b, c))
plt.xlabel('x')
plt.ylabel('y')
plt.show()