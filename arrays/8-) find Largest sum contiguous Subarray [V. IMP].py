# we use kedane algorithm for this

def kedane(arr):
    mx = s = arr[0]
    for i in range(1, len(arr)):
        mx = max(mx+arr[i], arr[i])
        s = max(s, mx)
    return s


print(kedane([1, 2, 3, -1, -8, 9, 10, 111]))
