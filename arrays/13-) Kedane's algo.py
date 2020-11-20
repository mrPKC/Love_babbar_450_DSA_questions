def kedane(arr):
    m = s = arr[0]
    for i in range(1, len(arr)):
        m = max(m+arr[i], arr[i])
        s = max(s, m)
    return s
