def remove_repeating(arr):
    ar = []
    for i in range(len(arr)-1):
        if(arr[i] != arr[i+1]):
            ar.append(arr[i])
    if(arr[-1] != arr[-2]):
        ar.append(arr[-1])
    return ar


def union_and_inter(ara, arb):
    na = len(ara)
    nb = len(arb)
    i = j = 0
    uni = []
    inte = []
    while(i < (na) or j < (nb)):
        if(i < na and j < nb and ara[i] == arb[j]):
            uni.append(ara[i])
            inte.append(ara[i])
            i += 1
            j += 1
        elif(i < (na) and ara[i] < arb[j]):
            uni.append(ara[i])
            if(i < (na)):
                i += 1
        else:
            uni.append(arb[j])
            if(j < (nb)):
                j += 1
    uni = remove_repeating(uni)
    inte = remove_repeating(inte)
    return uni, inte


print(union_and_inter([1, 2, 3, 4, 4, 4, 5, 6, 7, 8],
                      [4, 4, 5, 5, 6, 66, 666, 6666, 66666]))


def inbuilt(ara, arb):
    ara = set(ara)
    arb = set(arb)
    uni = list(ara.union(arb))
    inter = list(ara.intersection(arb))
    return uni, inter


print(inbuilt([1, 2, 3, 4, 4, 4, 5, 6, 7, 8],
              [4, 4, 5, 5, 6, 66, 666, 6666, 66666]))
