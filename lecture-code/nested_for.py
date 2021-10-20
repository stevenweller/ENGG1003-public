for i in [1, 2, 3]:
    # first indentation level (outer loop)
    print('i = {:d}'.format(i))
    for j in [4.0, 5.0, 6.0]:
        # second indentation level (inner loop)
        print('      j = {:.1f}'.format(j))