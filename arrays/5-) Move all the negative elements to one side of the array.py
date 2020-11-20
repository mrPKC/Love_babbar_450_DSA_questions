def eve_odd_seprator(arr, n):
    low = 0
    high = n-1
    j = -1
    for i in range(n):
        if(arr[i] < 0):
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    return arr


print(eve_odd_seprator([-1, 2, 3, 4, 5, 6, -2, -1, -6], 9))
