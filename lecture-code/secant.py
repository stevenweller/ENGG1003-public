import numpy as np

def f(x):
    return np.exp(x) - 3*x

eps = 1e-6
x0 = 0
x1 = 1
iters = 0       # iteration counter
while abs(f(x1)) > eps:
    # line (=secant) through (x0,f(x)) and (x1,f(x1)) intersects
    # horizontal axis at (x,0)
    x = x1 - f(x1)*((x1 - x0)/(f(x1) - f(x0)))
    x0 = x1
    x1 = x
    iters += 1

print('Solution: {:.5f}'.format(x))
print('Number of iterations: {}'.format(iters))
print('Check: f({:.5f}) = {:.5f}'.format(x, f(x)))