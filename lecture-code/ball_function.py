def y(v0, t):
    g = 9.81
    return v0*t - 0.5*g*t**2


print(y(5, 0.6))