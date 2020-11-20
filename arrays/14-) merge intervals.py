def merge(a):
    a.sort()
    op = []
    m = a[0][0]
    n = a[0][1]
    for i in range(1, len(a)):
        if((m <= a[i][0] and n >= a[i][0]) or (a[i][0] <= n and n <= a[i][1])):
            n = max(a[i][1], n)
        else:
            op.append([m, n])
            m = a[i][0]
            n = a[i][1]
    op.append([m, n])
    return op
