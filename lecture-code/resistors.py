import numpy as np
import matplotlib.pyplot as plt

def f(x):
    mu = 1000
    sigma = 30
    return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2 ))

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    f_sum = 0
    for i in range(1, n, 1):
        x = a + i * h
        f_sum = f_sum + f(x)
    return h * (0.5 * f(a) + f_sum + 0.5 * f(b))

a = 950
b = 1050
prob_ab = trapezoidal(f, a, b, 100)
print('Probability resistance in range [{},{}] is: {:.2f} percent'.format(a, b, 100*prob_ab))

x = np.linspace(900, 1100, 1000)
xab = np.linspace(a, b, 100)

plt.plot(xab, f(xab), 'r')
plt.plot(x, f(x), 'b')  # standard normal pdf
plt.fill_between(xab, f(xab), color='r', alpha=0.5)  # alpha=transparency
plt.axis([900, 1100, 0, 0.015])
plt.show()