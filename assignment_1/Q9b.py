import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def RGB_scale(m, alpha):

    R = m[:, :, 0] * alpha[0]
    G = m[:, :, 1] * alpha[1]
    B = m[:, :, 2] * alpha[2]

    return R + G + B


m = mpimg.imread('stinkbugs.jpg')
alpha = [0.95, 0.5, 0.25]
I = RGB_scale(m, alpha)
plt.imshow(I)

plt.show()
