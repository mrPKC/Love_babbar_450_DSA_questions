def count_and_merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m
    left = [0]*n1
    right = [0]*n2
    for i in range(n1):
        left[i] = arr[i+l]
    for j in range(n2):
        right[j] = arr[m+1+j]
    res = 0
    i = j = 0
    k = l
    while(i < n1 and j < n2):
        if(left[i] <= right[j]):

            arr[k] = left[i]
            k += 1
            i += 1
        else:

            arr[k] = right[j]
            k += 1
            j += 1
            res += (n1-i)
    while(i < n1):

        arr[k] = left[i]
        k += 1
        i += 1
    while(j < n2):

        arr[k] = right[j]
        k += 1
        j += 1
    return res


def count_inv(arr, l, r):
    res = 0
    if(l < r):
        m = (r+l)//2
        res += count_inv(arr, l, m)
        res += count_inv(arr, m+1, r)
        res += count_and_merge(arr, l, m, r)
    return res


n = int(input())
arr = list(map(int, input().split()))
print(count_inv(arr, 0, n-1))
