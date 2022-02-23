# compute height of a ball in vertical motion
# LL text, Section 1.2.1
# SRW, 3=Feb=2022

v0 = 5          # initial velocity (m/s)
g = 9.81       # a c c e l e r a t i o n due to g r a v i t y (m/ s ˆ2)
t = 0.6 # t ime ( s )

y = v0 * t - 0.5* g* t **2 # v e r t i c a l p o s i t i o n (m)

print(y)