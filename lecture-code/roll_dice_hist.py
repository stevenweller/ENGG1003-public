import numpy as np
import matplotlib.pyplot as plt

N = 100
# 1,2,3,4,5,6
x = np.random.randint(1, 7, size=N)

plt.hist(x, bins=20)
plt.xlabel('Outcome of dice roll')
plt.ylabel('Number of outcomes')
plt.show()