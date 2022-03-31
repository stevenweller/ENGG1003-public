import numpy as np

m = np.array([[1,2,3],[4,5,6],[7,8,9]])

total = 0   # total of elements in m
count = 0   # number of elements in m
for r in range(0, len(m)):
    for c in range(0, len(m[0])):
        total += m[r, c]
        count += 1

avg = total/count
print(avg)