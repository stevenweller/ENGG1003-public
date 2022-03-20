def y(v0, t):
    g = 9.81
    return v0*t - 0.5*g*t**2


v0 = 5
time = 0.6
print(y(v0, time))