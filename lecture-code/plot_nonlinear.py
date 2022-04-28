import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(x) - 3*x


xLO = 0
xHI = 2

xrange = np.linspace(xLO, xHI, num=1001)

plt.plot(xrange, f(xrange))

# two solutions, obtained using bisection & secant
plt.plot(0.61906, f(0.61906), 'ks')
plt.plot(1.51213, f(1.51213), 'ks')
plt.title("f(x) = exp(x) - 3*x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid("on")
plt.show()