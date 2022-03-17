import numpy as np

N = 1000
# np.random.choice(a, size, p)
# N samples from "a", p = prob each entry in "a"
x = np.random.choice([0, 1], N, p=[0.6, 0.4])

headCnt = 0
for i in range(0, len(x)):
    if x[i] == 0:
        headCnt += 1

print(headCnt)