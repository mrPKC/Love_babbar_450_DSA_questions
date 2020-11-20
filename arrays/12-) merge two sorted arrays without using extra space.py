# merging two sorted arrays without using extra space
def merge(ar1, ar2):
    n = len(ar1)
    m = len(ar2)
    i = 0
    j = 0
    for i in range(n):
        if(ar1[i] > ar2[j]):
            ar1[-1], ar2[j] = ar2[j], ar1[-1]
            j += 1
            for k in range(n-1, i, -1):
                ar1[k], ar1[k-1] = ar1[k-1], ar1[k]
    ar2.sort()
    return ar1, ar2


a = [1, 2, 3, 6, 8, 9, 999]
b = [4, 5, 6, 11, 22, 33, 44]
print(merge(a, b))
