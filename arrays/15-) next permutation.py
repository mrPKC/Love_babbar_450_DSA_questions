from typing import List


def nextPermutation(self, arr: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    ## mine logic #########
    # n = len(nums)
    # if(n > 2):
    #     ind = -1
    #     flag = 0
    #     for i in range(n-1):
    #         if(nums[i]>nums[i+1]):
    #             ind = i
    #             flag = 1
    #             break
    #     # if(flag == 1 and ind == n-2):
    #     #     nums[-3],nums[-2] = nums[-2],nums[-3]
    #     if(flag == 0):
    #         nums[-2],nums[-1] = nums[-1],nums[-2]
    #     else:
    #         flag = 0
    #         jd = -1
    #         for j in range(ind,n-1):
    #             if(nums[j]<nums[j+1]):
    #                 jd = j
    #                 flag = 1
    #                 break
    #         if(jd == -1 and ind == 0):
    #             nums.sort()
    #         elif(jd == -1 and n != 3):
    #             nums[ind-1],nums[-1] = nums[-1],nums[ind-1]
    #             nums[ind],nums[-1] = nums[-1],nums[ind]
    #         elif(jd == -1 and n == 3):
    #             nums[ind],nums[ind-1] = nums[ind-1],nums[ind]
    #             nums[ind],nums[ind+1] = nums[ind+1],nums[ind]
    #         else:
    #             nums[jd],nums[jd+1] = nums[jd+1],nums[jd]
    # elif(n==2):
    #     nums[0],nums[1] = nums[1],nums[0]

    # MK's solution##########

    i = j = len(arr)-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i == 0:
        arr.reverse()
        return
    k = i - 1
    while arr[j] <= arr[k]:
        j -= 1
    arr[k], arr[j] = arr[j], arr[k]
    l, r = k+1, len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr
