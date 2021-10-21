# standard_normal_a_b
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

def trapezoidal(f, a, b, n):
    h = (b-a)/n
    f_sum = 0
    for i in range(1, n, 1):
        x = a + i*h
        f_sum = f_sum + f(x)
    return h*(0.5*f(a) + f_sum + 0.5*f(b))

a = 1
b = 2
prob_ab = trapezoidal(f, a, b, 100)
print('Probability X in range [{},{}] is: {:.4f}'.format(a, b, prob_ab))

x = np.linspace(-6, 6, 1000)
xab = np.linspace(a, b, 100)

plt.plot(x, f(x), 'b')             # standard normal pdf
plt.plot(xab,f(xab),'r')
plt.fill_between(xab,f(xab),color='r',alpha=0.5) #alpha=transparency
plt.axis([-4, 4, 0, 0.42])
plt.show()