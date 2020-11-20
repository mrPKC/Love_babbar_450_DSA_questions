def min_jump(a, n):
    if(n == 1):
        return 0
    if(a[0] == 0):
        return -1
    max_reach = a[0]
    ju = 1
    step = a[0]

    for i in range(1, n):
        if(i == n-1):
            return ju
        max_reach = max(max_reach, a[i]+i)
        step -= 1
        if(step == 0):
            if(i >= max_reach):
                return -1
            ju += 1
            step = max_reach - i
    return -1


a = [2, 9, 1, 1, 1, 1, 1, 1]
n = len(a)
print(min_jump(a, n))
