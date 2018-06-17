# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:36:25 2018

@author: Wenchang Chen

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

https://leetcode.com/problems/two-sum/description/
"""

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        sec = target - nums[i]
        if sec in d.keys():
            return(d[sec], i)
        else:
            d[nums[i]] = i;