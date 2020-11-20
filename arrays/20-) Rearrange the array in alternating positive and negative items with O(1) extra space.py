# Rearrange the array in alternating positive and negative items with O(1) extra space

def odd_eve_alg_alg(arr):
    # pivo = arr[-1]
    j = -1
    for i in range(len(arr)):
        if(arr[i] < 0):
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    return arr, j+1


def odd_eve_alter(arr):
    arr, ind = odd_eve_alg_alg(arr)
    print(arr, ind)
    i = 1
    l = len(arr)
    while(ind < l and (ind) != i):
        j = ind
        while(j != i):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        ind += 1
        i += 2
    return arr


# print(odd_eve_alter([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))
print(odd_eve_alter([-5, -2, 5, 2, -4, -7, -1, 8, 0, -8]))
