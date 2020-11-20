def maximum(arr, n):
    m = arr[0]
    for i in range(1, n):
        # m = max(arr[i], m)
        if(arr[i] > m):
            m = arr[i]
    return m


def minimum(arr, n):
    m = arr[0]
    for i in range(1, n):
        # m = max(arr[i], m)
        if(arr[i] < m):
            m = arr[i]
    return m


print(minimum([5, 4, 3, 2, 1, 99999], 6))
