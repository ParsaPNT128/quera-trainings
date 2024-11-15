def func(bwidth, blength, bheight, iwidth, ilength, iheight):
    for i in range(6):
        if bwidth >= iwidth and blength >= ilength:
            return 'zende mimuni'

        if i == 0:
            iwidth, ilength, iheight = [iwidth, iheight, ilength]
        elif i == 1:
            iwidth, ilength, iheight = [iheight, iwidth, ilength]
        elif i == 2:
            iwidth, ilength, iheight = [iheight, ilength, iwidth]
        elif i == 3:
            iwidth, ilength, iheight = [iwidth, iheight, ilength]
        elif i == 4:
            iwidth, ilength, iheight = [ilength, iwidth, iheight]
        
    return 'dari mimiri'

a, b, c, d, e, f = list(map(int, input().split()))
print(func(a, b, c, d, e, f))