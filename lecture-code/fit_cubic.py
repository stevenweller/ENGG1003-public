import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt


# fit a cubic poly to data
# guess data is a cubic
def cubic(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d


np.random.seed(1)
# data is actually a cubic + noise
x = np.linspace(-4, 4, 100)
y = -4*x**3 + 3*x**2 + 25*x + 6 + np.random.normal(0., 10, len(x))
plt.plot(x, y, 'r.')

popt, _ = sco.curve_fit(cubic, x, y)
a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]

plt.plot(x, cubic(x, a, b, c, d), 'b')
plt.title('Best fit cubic {:.2f}x**3 + {:.2f}x**2 + {:.2f}x + {:.2f}'.format(a,b,c,d))
plt.xlabel('x')
plt.ylabel('y')
plt.show()