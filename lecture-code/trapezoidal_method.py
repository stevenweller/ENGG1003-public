import numpy as np

def v(t):
   return 3*t**2*np.exp(t**3)

def trapezoidal(f, a, b, n):
    h = (b-a)/n
    f_sum = 0
    for i in range(1, n, 1):
        x = a + i*h
        f_sum = f_sum + f(x)
    return h*(0.5*f(a) + f_sum + 0.5*f(b))

n = 100
trap = trapezoidal(v, 0, 1, n)
exact = np.exp(1) - 1

print('Trapezoidal, {} sub-intervals: {:.8f}'.format(n,trap))
print('Exact answer: {:.8f}'.format(exact))