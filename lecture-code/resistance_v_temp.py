import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco


def line(x, m, b):
    return m * x + b


# temperature (degC)
x = np.array([20.5, 32.7, 51.0, 73.2, 95.7])
# resistance (ohms)
y = np.array([765, 826, 873, 942, 1032])
plt.plot(x, y, 'r.', markersize=15)

popt, _ = sco.curve_fit(line, x, y)
m = popt[0]
b = popt[1]
print("m = {:.2f}, b = {:.0f}".format(m, b))

xfine = np.linspace(0., 100., 100)
plt.plot(xfine, line(xfine, m, b), 'b')
plt.title('y = {:.2f} x + {:.0f} '.format(m, b))
plt.xlabel('x')
plt.ylabel('y')
plt.show()