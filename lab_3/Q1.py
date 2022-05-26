import numpy as np
import rootfinding as rf
import matplotlib.pyplot as plt


def f(x):
    return np.exp(x) - x - 2


xLO = 0
xHI = 3

x1, _ = rf.bisection(f, xLO, xHI)
print("Bisection solution in interval [{:.2f}, {:.2f}] is {:.4f}".format(xLO, xHI, x1))

print("Check solution: f({:.4f}) = {:.4f}".format(x1, f(x1)))

xLO = -3
xHI = 0
x2, _ = rf.bisection(f, xLO, xHI)
print("Bisection solution in interval [{:.2f}, {:.2f}] is {:.4f}".format(xLO, xHI, x2))
print("Check solution: f({:.4f}) = {:.4f}".format(x2, f(x2)))

x = np.linspace(-3, 3, num=1001)
plt.plot(x, f(x))
plt.grid("on")
plt.show()
