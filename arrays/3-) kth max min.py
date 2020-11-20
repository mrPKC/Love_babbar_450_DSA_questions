# def lombito_for_small(arr, l, h):
#     p = arr[h]
#     j = l-1
#     for i in range(l, h):
#         if(arr[i] < p):
#             j += 1
#             arr[j], arr[i] = arr[i], arr[j]
#     arr[j+1], arr[h] = arr[h], arr[j+1]
#     return j+1


# def kth_min(arr, n, k):
#     l = 0
#     h = n-1
#     while(l <= h):
#         p = lombito_for_small(arr, l, h)
#         if(p == k-1):
#             return arr[p]
#         elif(p > (k-1)):
#             h = p-1
#         else:
#             l = p+1


# print(kth_min([5, 4, 3, 2, 1, 7, 8], 7, 6))


######################################################################


def lombito_for_big(arr, l, h):
    p = arr[h]
    j = l-1
    for i in range(l, h):
        if(arr[i] > p):
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j+1], arr[h] = arr[h], arr[j+1]
    return j+1


def kth_max(arr, n, k):
    l = 0
    h = n-1
    while(l <= h):
        p = lombito_for_big(arr, l, h)
        if(p == k-1):
            return arr[p]
        elif(p > (k-1)):
            h = p-1
        else:
            l = p+1


print(kth_max([5, 4, 3, 2, 1, 7, 8], 7, 3))
