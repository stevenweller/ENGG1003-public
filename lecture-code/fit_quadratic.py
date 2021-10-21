# fit_quadratic
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# guess data is a parabola
def parabola(x, a, b, c):
    return a*x**2 + b*x + c

np.random.seed(1)   # replicate results by fixing seed
# data is actually a cubic + noise
x = np.linspace(-4, 4, 100)
y = -4*x**3 + 3*x**2 + 25*x + 6 + np.random.normal(0., 10, len(x))
plt.plot(x, y, '.')

popt, pcov = curve_fit(parabola, x, y)
a = popt[0]; b = popt[1]; c = popt[2]

plt.plot(x, parabola(x, a, b, c), 'r')
plt.title('Best fit parabola: {:.2f}x**2 + {:.2f}x + {:.2f}'.format(a,b,c))
plt.xlabel('x'); plt.ylabel('y')
plt.show()