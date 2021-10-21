import time

def f(L):
    return 0.0268*L**3 + 1.884*L**2 + 44.15*L - 500

def my_bisection(f, x_LO, x_HI, tol):
    x_MID = (x_LO + x_HI) / 2
    itCnt = 0
    while abs(f(x_MID)) > tol:
        if f(x_MID) * f(x_LO) > 0:
            x_LO = x_MID
        else:
            x_HI = x_MID
        x_MID = (x_LO + x_HI) / 2
        itCnt += 1
    return x_MID, itCnt

def my_secant(f, x0, x1, tol):
    itCnt = 0
    while abs(f(x1)) > tol:
        x = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        x0 = x1
        x1 = x
        itCnt += 1
    return x1, itCnt

tStart = time.perf_counter()
xB, numItB = my_bisection(f, 6, 10, 1e-6)
tStop = time.perf_counter()
tBisect = tStop - tStart

tStart = time.perf_counter()
xS, numItS = my_secant(f, 6, 10, 1e-6)
tStop = time.perf_counter()
tSecant = tStop - tStart

print('Solution (bisection): {}'.format(xB))
print('Number of iterations (bisection): {}'.format(numItB))
print('Check: f({:.8f}) = {:.8f}'.format(xB,f(xB)))
print('Run-time (bisection): {:.4g} seconds'.format(tBisect))
print(' ' )
print('Solution (secant): {}'.format(xS))
print('Number of iterations (secant): {}'.format(numItS))
print('Check: f({:.8f}) = {:.8f}'.format(xS,f(xS)))
print('Run-time (secant): {:.4g} seconds'.format(tSecant))
print(' ')
print('Secant method is {:.2g} times as fast as bisection method'.format(tBisect/tSecant))