import numpy as np
import rootfinding as rf

def f(x):
    return np.exp(x) - 3*x

xLO = 0
xHI = 1

x, iters = rf.bisection(f, xLO, xHI)
print("Bisection solution: x = {:.6f}".format(x))

x0 = 0
x1 = 1
x, iters = rf.secant(f, x0, x1)
print("Secant solution: x = {:.6f}".format(x))