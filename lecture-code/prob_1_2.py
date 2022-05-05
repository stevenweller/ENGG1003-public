import numpy as np
import integration as integ

def f(x):
    return 1/(np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

a = 1
b = 2
prob_12 = integ.trapezoidal(f, a, b)
print('Probability X in range [{},{}] is: {:.4f}'.format(a, b, prob_12))