import numpy as np
import matplotlib.pyplot as plt

# generate random array of (x,y) pairs covering
# square with edge length 2
N = 10000
x = np.random.uniform(-1, 1, N)      # N floats from [-1,1)
y = np.random.uniform(-1, 1, N)      # N floats from [-1,1)

insideCnt = 0
for i in range(0, N):
    if x[i]**2 + y[i]**2 <= 1:
        plt.plot(x[i], y[i], 'r.')
        insideCnt += 1
    else:
        plt.plot(x[i], y[i], 'b.')

R = insideCnt/N
print('Estimate of pi: {}'.format(4*R))

plt.axis('equal')
plt.show()