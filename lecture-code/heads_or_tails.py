import numpy as np

# generate random array of 0s and 1s
# 0==heads & 1==tails
# N integers from [0,2) ie: 0 or 1
N = 100000
x = np.random.randint(0, 2, N)
print(x)

headCnt = 0;
for i in range(0, N):
    if x[i] == 0:
        headCnt += 1

print('Expected number of heads: {}'.format(N/2))
print('Observed number of heads: {}'.format(headCnt))