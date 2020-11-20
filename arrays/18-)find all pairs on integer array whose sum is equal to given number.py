def getPairsCount(self, arr, n, k):
    # code here
    ha = [0]*(k+1)
    for i in arr:
        if(i <= k):
            ha[i] += 1
    i = 0
    j = k
    op = 0
    while(i < j):
        op += (ha[i]*ha[j])
        i += 1
        j -= 1
    if(k % 2 == 0 and ha[k//2] > 1):
        op += ((ha[k//2])*(ha[k//2]-1))//2
    return op
