# generate quiz
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,4*np.pi,200)

y = 0.2*np.sin(t+2*np.pi/3)

plt.plot(t,y)
plt.title("Oscillation One Vs. Time")
plt.savefig("plot.png")

with open("sequence.txt", "w") as f:
    x = np.zeros(10)
    x[0] = 0.1
    x[1] = 2
    f.write(f'\\\\{x[0]:.5f}\\\\\n')
    f.write(f'{x[1]:.5f}\\\\\n')
    sum1 = x[0] + x[1]
    sum2 = 0
    for n in range(2,10):
        x[n] = 2*x[n-1] + 0.5*x[n-2]
        sum1 = sum1 + x[n]
        if x[n] > 4 and x[n] < 100:
            sum2 = sum2 + x[n]
        f.write(f'{x[n]:.5f}\\\\\n')

with open("sum1.txt", "w") as f:
    f.write(f'{sum1:.5f}')

with open("sum2.txt", "w") as f:
    f.write(f'{sum2:5f}')
