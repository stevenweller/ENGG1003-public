import numpy as np

# intended purpose: fill array f[t] = t**2
# t = 0,1,2,...,9

f = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
N = len(f)
for t in range(0, 10, N):
    f[t] = t**2
    print(f[t])