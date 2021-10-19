def f(L):
    return 0.0268*L**3 + 1.884*L**2 + 44.15*L - 500

def my_secant(f, x0, x1, tol):
    itCnt = 0
    while abs(f(x1)) > tol:
        x = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        x0 = x1
        x1 = x
        itCnt += 1
    return x1, itCnt

x, numIt = my_secant(f, 4, 12, 1e-8)

print('Solution: {}'.format(x))
print('Number of iterations: {}'.format(numIt))
print('Check: f({:.8f}) = {:.8f}'.format(x,f(x)))