import numpy as np

# compute pi using classic 1706 formula by John Machin:
#
# pi/4 = 4*arctan(1/5) - arctan(1/239)
#
# https://en.wikipedia.org/wiki/Machin-like_formula
# https://www.craig-wood.com/nick/articles/pi-machin/


def arctan(x):
    """ arctan(1/x) using power series
    arctan(1/x) = 1/x - 1/(3*x**3) + 1/(5*x**5) - 1/(7*x**7) + ..."""

    N = 22
    result = 0
    sign = 1
    # truncate power series at ... + 1/(21*x**21)
    for i in range(1, N+1, 2):
        result += sign/(i*x**i)
        sign *= -1
    return result


mypi = 4*(4*arctan(5) - arctan(239))


print(mypi)
print(mypi - np.pi)
