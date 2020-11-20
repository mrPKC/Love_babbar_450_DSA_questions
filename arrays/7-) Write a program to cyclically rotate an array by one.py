############### BASIC #############

# def reverse_by_1(arr):
#     h = len(arr)-1
#     l = h-1
#     while(l >= 0):
#         arr[l], arr[h] = arr[h], arr[l]
#         l -= 1
#         h -= 1
#     return arr


# a = list(map(int, input().split()))
# b = reverse_by_1(a)
# print(*b)


############### ultra max pro :) ################
n = int(input('size of array: '))
d = int(input("number of rotation = "))
a = [*([0]*d), *list(map(int, input().split()))]
j = -1
for i in range(d-1, -1, -1):
    a[j], a[i] = a[i], a[j]
    j -= 1
a = a[:n]
print(*a)
