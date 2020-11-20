# in O(1) space
# in O(nlogn) time

def findDupli(arr, n):
    arr.sort()
    for i in range(1, n):
        if(arr[i-1] == arr[i]):
            return arr[i]

    return "nothing repeated"


a = [1, 2, 3, 1]
n = len(a)

print(findDupli(a, n))
