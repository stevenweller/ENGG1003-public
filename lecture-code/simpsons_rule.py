import numpy as np

def v(t):
    return 3*t**2*np.exp(t**3)

def simpson(f, a, b, n):
    h = (b-a)/n
    x0 = a
    summ = 0
    # i-th sub-interval (i=0,1,...,n-1) is [x_i,x_{i+1}]
    for i in range(0,n,1):
        xi = x0 + i*h
        summ += (f(xi) + 4*f((xi+xi+h)/2) + f(xi+h))*h/6
    return summ

n = 100
simp = simpson(v, 0, 1, n)
exact = np.exp(1) - 1

print('Simpson, {} sub-intervals: {:.8f}'.format(n,simp))
print('Exact answer: {:.8f}'.format(exact))