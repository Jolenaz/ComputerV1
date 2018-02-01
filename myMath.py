def equal(e1, e2):
    if (e1 > e2) and (e1 - e2 < 0.001):
        return True
    elif (e1 < e2) and (e2 - e1 < 0.001):
        return True
    else:
        return False

def rac(val):
    if (val < 0):
        return (None)
    if (val == 0):
        return (0)
    i = 0.0
    while(True):
        if (equal(i*i, val)):
            return i
        if (i*i > val):
            return i
        i = i + 0.01


