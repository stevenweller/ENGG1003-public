# compute height of a ball in vertical motion
# SRW, 3-Feb-2022

v0 = 5             # Initial velocity
g = 9.81           # Acceleration of gravity
t = 0.6            # Time

y = v0*t - 0.5*g*t**2        # Vertical position

print(y)