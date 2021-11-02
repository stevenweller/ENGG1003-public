# function definition
def ball_height(v0, t):
    """ calculate height of ball at time t
    given an initial velocity of v0 """
    g = 9.81
    y = v0*t - 0.5*g*t**2
    return y


v0 = 5
time1 = 0.6
height1 = ball_height(v0, time1)
print(height1)

time2 = 0.9
height2 = ball_height(v0, time2)
print(height2)