import numpy as np

# Q4(a)
np.random.seed(1)
N = 10
x = np.random.normal(0, 1, size=N)
print(x)

# Q4(b)
total = 0
for i in range(0, len(x)):
    total += x[i]

print(total/len(x))
