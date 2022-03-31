import numpy as np
import matplotlib.pyplot as plt

# version: A,B,C,D,E
version = "D"

if version == "A":
    t = np.linspace(0, 4 * np.pi, num=1001)

    y = 0.2 * np.sin(t + 2 * np.pi / 3)

    plt.plot(t, y, 'r.')
    plt.xlabel('time (days)')
    plt.axis([-1, 15, -0.2, 0.2])
    plt.savefig("plot.png")

    print("Lab version:", version, '\n')
    print("Float is: {:.6f}".format(np.pi ** 2))
    print("Int is: {:7d}".format(3 ** 7))

elif version == "B":
    t = np.linspace(0, 6 * np.pi, num=101)

    y = 2 * np.cos(t + 3 * np.pi / 4)

    plt.plot(t, y, 'b-.')
    plt.xlabel('time (hours)')
    plt.axis([-1, 20, -2, 2])
    #plt.show()
    plt.savefig("plot.png")

    print("Lab version:", version, '\n')
    print("Float is: {:.6f}".format(np.pi ** 3))
    print("Int is: {:6d}".format(3 ** 5))

elif version == "C":
    t = np.linspace(0, 5 * np.pi, num=201)

    y = 3 * np.sin(t + np.pi / 2)

    plt.plot(t, y, 'k.')
    plt.xlabel('time (seconds)')
    plt.axis([-2, 18, -4, 4])
    #plt.show()
    plt.savefig("plot.png")

    print("Lab version:", version, '\n')
    print("Float is: {:.4f}".format(np.pi ** 2))
    print("Int is: {:4d}".format(4 ** 3))

elif version == "D":
    t = np.linspace(0, 3 * np.pi, num=501)

    y = 0.5 * np.cos(t + np.pi / 3)

    plt.plot(t, y, 'g-.')
    plt.xlabel('time (milliseconds)')
    plt.axis([-1, 10, -0.8, 0.8])
    #plt.show()
    plt.savefig("plot.png")

    print("Lab version:", version, '\n')
    print("Float is: {:.8f}".format(np.pi ** 4))
    print("Int is: {:8d}".format(4 ** 5))

else:
    print("haven't done that option yet")

