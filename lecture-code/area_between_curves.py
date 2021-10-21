import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(x)

def g(x):
    return x**3

def trapezoidal(f, a, b, n):
    h = (b-a)/n
    f_sum = 0
    for i in range(1, n, 1):
        x = a + i*h
        f_sum = f_sum + f(x)
    return h*(0.5*f(a) + f_sum + 0.5*f(b))

n = 500
x = np.linspace(0,1,1000)
underf = trapezoidal(f, 0, 1, n)
underg = trapezoidal(g, 0, 1, n)
A = underf - underg

print('Trapezoidal, {} sub-intervals'.format(n))
print('Area under f: {:.6f}'.format(underf))
print('Area under g: {:.6f}'.format(underg))
print('Area between f and g: {:.6f}'.format(A))

plt.subplot(3,1,1)
plt.plot(x, f(x), color='r')
plt.plot(x, g(x), color='b')
plt.fill_between(x, f(x), g(x), color='g', alpha=0.5)  # alpha=transparency
plt.subplot(3,1,2)
plt.plot(x,f(x),color='r')
plt.plot(x,g(x),color='b')
plt.fill_between(x,f(x),color='r',alpha=0.5) #alpha=transparency
plt.subplot(3,1,3)
plt.plot(x,f(x),color='r')
plt.plot(x,g(x),color='b')
plt.fill_between(x,g(x),color='b',alpha=0.5) #alpha=transparency

plt.show()