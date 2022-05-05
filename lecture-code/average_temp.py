import numpy as np
import matplotlib.pyplot as plt
import integration as integ


def T(t):
    return 20 - 5*np.cos(np.pi*t/12)


a = 6
b = 12
Tavg = integ.trapezoidal(T, a, b)/(b-a)
print('Average temp over [{:},{:}] hours is {:.2f} degC'.format(a, b, Tavg))

t = np.linspace(0, 24, num=1001)
t612 = np.linspace(6, 12, num=1001)
plt.plot(t, T(t))
plt.fill_between(t612, T(t612), color='r', alpha=0.5) #alpha=transparency
plt.xlabel('t (hrs)')
plt.ylabel('T(t) (degC)')
plt.show()