def rev_the_array(arr, n):
    low = 0
    high = n-1
    while(low < high):
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return arr


print(rev_the_array([6, 5, 4, 3, 2, 1], 6))
