# compute height of a ball in vertical motion
# LL text, Section 1.2.1
# SRW, 3=Feb=2022

v0 = 5          # initial velocity (m/s)
g = 9.81        # acceleration due to gravity (m/s^2)
t = 0.6         # time (s)

y = v0*t - 0.5*g*t**2   # vertical position (m)

print(y)
