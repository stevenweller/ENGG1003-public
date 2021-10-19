import numpy as np
import matplotlib.pyplot as plt

def v(t):
    return 3*t**2*np.exp(t**3)

t = np.linspace(0,1,num=1000)
tt = np.array([0, 0.2, 0.6, 0.8, 1])

panel1 = np.linspace(0,0.2,num=2)
panel2 = np.linspace(0.2,0.6,num=2)
panel3 = np.linspace(0.6,0.8,num=2)
panel4 = np.linspace(0.8,1.0,num=2)

plt.plot(t,v(t),color='k',linewidth=3)
plt.plot(tt,v(tt),color='k')

plt.fill_between(panel1,v(panel1),color='k')
plt.fill_between(panel2,v(panel2),color='g')
plt.fill_between(panel3,v(panel3),color='r')
plt.fill_between(panel4,v(panel4),color='b')

plt.axis([0, 1, 0, 9])
plt.grid()
plt.show()