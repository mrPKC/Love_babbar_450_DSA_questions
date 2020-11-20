def best_profit(a):
    if(len(a) <= 1):
        return 0
    m = min(a[0], a[1])
    dif = a[1]-a[0]
    for i in range(2, len(a)):
        if((a[i]-m) > dif):
            dif = a[i]-m
        if(a[i] < m):
            m = a[i]
    if(dif <= 0):
        return 0
    else:
        return dif
