import numpy as np

N = 10000
x = np.random.randint(1, 7, size=N)
y = np.random.randint(1, 7, size=N)

dblSix = 0
for i in range(0, N):
    if x[i] == 6 and y[i] == 6:
        dblSix += 1
        #print("double six!")
print(dblSix)
print(N/36)