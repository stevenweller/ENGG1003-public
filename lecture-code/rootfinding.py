def bisection(f, xLO, xHI, tol=1e-10, iterMax=64):
    if xLO >= xHI:
        print("ERROR: xLO must be strictly less than xHI")
        print("f(xLO): ", f(xLO))
        print("f(xHI): ", f(xHI))
        return

    if f(xLO)*f(xHI) > 0:
        print("ERROR: f(xLO) and f(xHI) must have different sign")
        print("f(xLO): ", f(xLO))
        print("f(xHI): ", f(xHI))
        return

    xMID = (xLO + xHI) / 2
    iters = 0
    while abs(f(xMID)) > tol and iters < iterMax:
        if f(xMID)*f(xLO) > 0:
            xLO = xMID
        else:
            xHI = xMID
        xMID = (xLO + xHI) / 2
        iters += 1
    return xMID, iters


def secant(f, x0=0, x1=1, tol=1e-10, iterMax=64):
    iters = 0
    while abs(f(x1)) > tol and iters < iterMax:
        x = x1 - f(x1)*((x1 - x0)/(f(x1) - f(x0)))
        x0 = x1
        x1 = x
        iters += 1
    return x, iters


def newton(f, df, x0=1, tol=1e-10, iterMax=32):
    iters = 0
    xNew = x0 - f(x0)/df(x0)
    x0 = xNew
    while abs(f(xNew)) > tol and iters < iterMax:
        xNew = x0 - f(x0)/df(x0)
        x0 = xNew
        iters += 1
    return x0, iters