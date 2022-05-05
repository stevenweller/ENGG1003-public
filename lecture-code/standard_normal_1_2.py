import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1/(np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)


a = 1
b = 2
x = np.linspace(-6, 6, 1000)
xab = np.linspace(a, b, 100)

plt.plot(x, f(x), 'b')             # standard normal pdf
plt.plot(xab,f(xab), 'r')
plt.fill_between(xab, f(xab), color='r', alpha=0.5) #alpha=transparency
plt.axis([-4, 4, 0, 0.42])
plt.show()