import numpy as np
import integration as integ

def v(t):
    return 3*t**2*np.exp(t**3)

a = 0
b = 1
trap = integ.trapezoidal(v, a, b)
print("Trapezoidal method: {:.5f}".format(trap))

S = integ.simpson(v, a, b)
print("Simpsons rule: {:.5f}".format(S))