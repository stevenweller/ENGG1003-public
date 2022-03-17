import numpy as np

np.random.seed(10)

# 10 random integers from {0,1}
# 0==heads, 1==tails
x = np.random.randint(0, 2, size=10)
print(x)