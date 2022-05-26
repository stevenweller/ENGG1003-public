import numpy as np


def polyarea(x, y):
    n = len(x)

    sum1 = 0
    # x[0]*y[1] + x[1]*y[2] + ... + x[n-2]*y[n-1]
    for i in range(0, n-1):
        sum1 += x[i]*y[i+1]
    sum1 += x[n-1]*y[0]

    sum2 = 0
    # y[0]*x[1] + y[1]*x[2] + ... + y[n-2]*x[n-1]
    for i in range(0, n-1):
        sum2 += y[i]*x[i+1]
    sum2 += y[n-1]*x[0]

    return np.abs(sum1 - sum2)/2


# test cases

# # unit square, A==1
# x = np.array([0, 1, 1, 0])
# y = np.array([0, 0, 1, 1])

# # rectangle, A==3
# x = np.array([0, 3, 3, 0])
# y = np.array([0, 0, 1, 1])

# # triangle, A==1
# x = np.array([0, 2, 1])
# y = np.array([0, 0, 1])

# # irregular polygon in assignment sheet, A==7.075
x = np.array([1, 3, 4, 3.5, 2])
y = np.array([1, 1.2, 2.5, 5, 4])

print("{:.3f}".format(polyarea(x, y)))
