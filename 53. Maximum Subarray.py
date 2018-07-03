# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 19:48:00 2018

@author: Wenchang Chen

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

https://leetcode.com/problems/maximum-subarray/description/
"""

def maxseq(nums):
    res_set = []
    res = -float('inf')
    for num in nums:
        if res + num > num:
            res += num
        else:
            res = num
    return res


nums = [8,-19,5,-4,20]
print(maxseq(nums))

        
        
        
        
        
        