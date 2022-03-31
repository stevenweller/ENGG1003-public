import numpy as np
import matplotlib.pyplot as plt

# # version: 1,2,3,4,5
# version = 1
#
# if version == 1:
t = np.linspace(0, 4 * np.pi, num=1001)

y = 0.2 * np.sin(t + 2 * np.pi / 3)

plt.plot(t, y, 'r.')
plt.xlabel('time (days)')
plt.axis([-1, 15, -0.2, 0.2])
plt.savefig("plot.png")

# with open("float.txt", "w") as f:
#     f.write(f'{np.pi ** 2:.6f}')
print("Float is: {:.6f}".format(np.pi**2))

# with open("int.txt", "w") as f:
#     f.write(f'Int is: {3**7:7d}')
print("Int is: {:7d}".format(3**7))

# elif version == 2:
# elif version == 3:
# elif version == 4:
# else:
