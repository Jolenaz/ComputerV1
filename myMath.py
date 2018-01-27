def rac(val):
    if (val < 0):
        return (None)
    if (val == 0):
        return (0)
    i = 0
    while(True):
        if (i*i >= val):
            return i
        i += 1


