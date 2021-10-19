# standardnormaldemo
import numpy as np

N = 1000000
x = np.random.normal(0.0, 1.0, size=N)
a = 1
b = 2
num_ab = 0
for k in range(0, len(x)):
    if a <= x[k] <= b:
        num_ab += 1

print('{} standard normal random numbers'.format(N))
print('Fraction of random numbers in range [{},{}] = {:.4f}'.format(a, b, num_ab/N))