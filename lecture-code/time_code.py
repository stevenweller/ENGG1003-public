import time
import numpy as np

t0 = time.perf_counter()

N = 100000000
t = np.linspace(0, 1, num=N)
x = np.sin(t**2)
print("Loop time (s): {}".format(time.perf_counter() - t0))