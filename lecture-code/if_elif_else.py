T = float(input('What is the water temperature? '))
if T > 24:
    print('Great, jump in!')
elif 20 <= T <= 24:
    print('Not bad. Put your toe in first!')
else:
    print('Do not swim. Too cold!')
# first line after if-elif-else construction