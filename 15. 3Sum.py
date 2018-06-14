# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:50:26 2018

@author: Wenchang Chen


Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

https://leetcode.com/problems/3sum/description/
"""

# =============================================================================
# def bisection(lst, a):
#     if lst == '' or lst[-1] < a:
#         return -1
#     start = 0
#     end = len(lst) - 1
#     mid = (start + end) // 2
#     if lst[end] == a:
#         return end
#     while mid != start and mid != end:
#         if lst[mid] == a:
#             return mid
#         elif lst[mid] < a:
#             start = mid
#         else:
#             end = mid
#         mid = (start + end) // 2
#     if lst[mid] == a:
#         return mid
#     else:
#         return start
# =============================================================================
            
def twosum(nums, a):
    zerotri = []
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == a:
            zerotri += [[-a, nums[i], nums[j]]]
            i += 1
            j -= 1
        elif nums[i] + nums[j] > a:
                j -= 1
        elif nums[i] + nums[j] < a:
            i += 1
        if nums[i] == nums[j]:
            if nums[i] + nums[j] == a:
                zerotri += [[-a, nums[i], nums[j]]]
            break
    return zerotri
        

def threeSum(nums):
    nums.sort()
    zerotri = []
    length = len(nums)
    for i in range(length-2):
        if nums[i] > 0:
            break
        zerotri += twosum(nums[i+1:], -nums[i])
        
    reList = list(set([tuple(t) for t in zerotri]))
    reList = [list(v) for v in reList]
    return reList  
# =============================================================================
#     nums.sort()
#     zerotri = []
#     length = len(nums)
#     for i in range(length-2):
#         if nums[i] > 0:
#             break
#         a = nums[i] + nums[-1]
#         b = bisection(nums[i+1:-1], -a)
#         if b == -1:
#             continue
#         for j in range(b+i+1, length-1):
#             twosum = nums[i]+nums[j]
#             if twosum > 0:
#                 break
#             c = bisection(nums[j+1:], -twosum)
#             if c == -1:
#                 continue
#             if nums[c+j+1] + twosum == 0:
#                 zerotri += [[nums[i], nums[j], nums[c+j+1]]]
#                 
#     reList = list(set([tuple(t) for t in zerotri]))
#     reList = [list(v) for v in reList]
# 
#     return reList
# 
# =============================================================================
# =============================================================================
#     nums.sort()
#     zerotri = []
#     length = len(nums)
#     for i in range(length-2):
#         if nums[i] > 0:
#             return zerotri
#         if i+1 < length - 1:
#             for j in range(i+1, length - 1):
#                 if nums[i]+nums[j] > 0:
#                     break                      
#                 start = j + 1
#                 end = length - 1
#                 if nums[i]+nums[j]+nums[start] > 0:
#                     break
#                 if nums[i]+nums[j]+nums[end] < 0:
#                     continue
#                 if nums[i]+nums[j]+nums[start] == 0 and [nums[i], nums[j], nums[start]] not in zerotri:
#                     zerotri += [[nums[i], nums[j], nums[start]]]
#                     break
#                 elif nums[i]+nums[j]+nums[end] == 0 and [nums[i], nums[j], nums[end]] not in zerotri:
#                     zerotri += [[nums[i], nums[j], nums[end]]]
#                     break
#                 mid = (start + end) // 2
#                 tmp = end
#                 while nums[tmp] != nums[mid]:
#                     tmp = mid
#                     if nums[i]+nums[j]+nums[mid] < 0:
#                         start = mid
#                     elif nums[i]+nums[j]+nums[mid] > 0:
#                         end = mid
#                     elif [nums[i], nums[j], nums[mid]] not in zerotri:
#                         zerotri += [[nums[i], nums[j], nums[mid]]]
#                         break
#                     mid = (start + end) // 2
#     return zerotri
# =============================================================================
