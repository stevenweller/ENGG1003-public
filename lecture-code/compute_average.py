# compute_average
import numpy as np
import matplotlib.pyplot as plt

def T(t):
    return 20 - 5*np.cos(np.pi*t/12)

def trapezoidal(f, a, b, n):
    h = (b-a)/n
    f_sum = 0
    for i in range(1, n, 1):
        x = a + i*h
        f_sum = f_sum + f(x)
    return h*(0.5*f(a) + f_sum + 0.5*f(b))

n = 1000
a = 6
b = 12
Tavg = trapezoidal(T, a, b, n)/(b-a)
print('Average temp over [{:},{:}] hours is {:.2f} degC'.format(a,b,Tavg))

t = np.linspace(0,24,1000)
t612 = np.linspace(6,12,1000)
plt.plot(t,T(t))
plt.fill_between(t612,T(t612),color='r',alpha=0.5) #alpha=transparency
plt.xlabel('t (hrs)')
plt.ylabel('T(t) (degC)')
plt.show()