def f(L):
    return 0.0268*L**3 + 1.884*L**2 + 44.15*L - 500

eps = 1e-8
x_LO = 6
x_HI = 10

x_MID = (x_LO + x_HI)/2
itCnt = 0
while abs(f(x_MID)) > eps:
    if f(x_MID)*f(x_LO) > 0:
        x_LO = x_MID
    else:
        x_HI = x_MID
    x_MID = (x_LO + x_HI)/2
    itCnt += 1

print('Solution: {}'.format(x_MID))
print('Number of iterations: {}'.format(itCnt))
print('Check: f({:.8f}) = {:.8f}'.format(x_MID,f(x_MID)))