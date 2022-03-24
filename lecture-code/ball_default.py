def y(v0, t, g=9.81):   # default g in header
    return v0*t - 0.5*g*t**2


print(y(5, 0.6))
print(y(5, 0.6, g=9.80665)) # more accurate g