# imports first
import numpy as np

# function definitions are next
def f(x):
    return np.sin(x)

def g(x):
    return x**2

# main starts here
t = 1.2345
print(f(t))
print(g(t))