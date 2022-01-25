# function definition
def ball_height(v0, t):                     # function header
    """ calculate height of ball at time t
    given an initial velocity of v0 """     # docstring
    g = 9.81                                # function body
    y = v0*t - 0.5*g*t**2                   # function body
    return y                                # return statement


# main program
v0 = 5
time1 = 0.6
height1 = ball_height(v0, time1)            # function call
print(height1)

time2 = 0.9
height2 = ball_height(v0, time2)            # function call
print(height2)
