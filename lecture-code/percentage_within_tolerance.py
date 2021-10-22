import numpy as np

# generate random array of N floats in range [17,19)
N = 10000
x = np.random.uniform(17, 19, N)
tolLow = 17.25
tolHigh = 18.75
print(x)

goodCnt = 0
for i in range(0, N):
    if tolLow <= x[i] <= tolHigh:
        goodCnt += 1

print('Percentage of parts in tolerance range [{},{}]: {}%'.format(tolLow, tolHigh, 100*goodCnt/N))