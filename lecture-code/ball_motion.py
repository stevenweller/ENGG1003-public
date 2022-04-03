def ball_height(v0, t):
    g = 9.81
    return v0*t - 0.5*g*t**2


def time_of_flight(v0):
    g = 9.81
    return 2*v0/g