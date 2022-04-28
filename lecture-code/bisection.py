import numpy as np

def f(x):
    return np.exp(x) - 3

# def f(x):
#     return 3*x + np.sin(x) - np.exp(x)

eps = 1e-6
xLO = 1
xHI = 2

xMID = (xLO + xHI) / 2
iters = 0
while abs(f(xMID)) > eps:
    if f(xMID)*f(xHI) < 0:  # solution in upper half
        xLO = xMID
    else:
        xHI = xMID
    xMID = (xLO + xHI) / 2
    iters += 1

print('Solution: {:.5f}'.format(xMID))
print('Number of iterations: {}'.format(iters))
print('Check: f({:.5f}) = {:.5f}'.format(xMID, f(xMID)))