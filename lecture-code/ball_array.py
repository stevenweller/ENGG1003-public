import numpy as np

def y(v0, t):
    g = 9.81
    #t[0] = 100
    return v0*t - 0.5*g*t**2

v0 = 5
t = np.linspace(0, 1, num=1001)
h = y(v0, t)

# changes to t in function affect t in main!
print(t)