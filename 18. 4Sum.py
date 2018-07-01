# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 21:23:31 2018

@author: Wenchang 

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

https://leetcode.com/problems/4sum/description/
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def twosum(nums, target):
            res = []
            i = 0
            j = len(nums) - 1
            while i < j:
                if target < 0 and (2 * nums[i] > target or nums[j] < target) or target >= 0 and (nums[i] > target or 2*nums[j] < target):
                    break
                if nums[i] == nums[j]:
                    if nums[i] + nums[j] == target:
                        res += [[nums[i], nums[j]]] 
                    break
                if nums[i] + nums[j] == target:
                    if [nums[i], nums[j]] not in res:
                        res += [[nums[i], nums[j]]]
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] > target:
                        j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
            return res
    
        def threeSum(nums, target):
            res = []
            length = len(nums)
            for i in range(length-2):
                if (nums[i] < 0 and 3*nums[i] > target) or (nums[i] >= 0 and nums[i] > target):
                    break
                res += [[nums[i]]+x for x in twosum(nums[i+1:], target - nums[i]) if [nums[i]]+x not in res]
            return res
        
        res = []
        length = len(nums)
        nums.sort()
        for i in range(length-3):
            res += [[nums[i]]+x for x in threeSum(nums[i+1:], target - nums[i]) if [nums[i]]+x not in res]
        return res