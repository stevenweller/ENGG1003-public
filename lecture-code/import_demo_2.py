import ball_motion as bm

v0 = 5
time = 0.7
height = bm.ball_height(v0, time)
print('At time {} the height is {:5.3f}'.format(time, height))