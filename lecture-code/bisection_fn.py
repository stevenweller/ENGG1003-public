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

x, numIt = my_bisection(f, 4, 12, 1e-6)

print('Solution: {}'.format(x))
print('Number of iterations: {}'.format(numIt))
print('Check: f({:.8f}) = {:.8f}'.format(x,f(x)))