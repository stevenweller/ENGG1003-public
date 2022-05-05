def trapezoidal(f, a, b, n=100):
    h = (b-a)/n
    f_sum = 0
    for i in range(1, n, 1):
        x = a + i*h
        f_sum = f_sum + f(x)
    return h*(0.5*f(a) + f_sum + 0.5*f(b))


def simpson(f, a, b, n=100):
    h = (b-a)/n
    x0 = a
    summ = 0
    # i-th sub-interval (i=0,1,...,n-1) is [x_i,x_{i+1}]
    for i in range(0,n,1):
        xi = x0 + i*h
        summ += (f(xi) + 4*f((xi+xi+h)/2) + f(xi+h))*h/6
    return summ