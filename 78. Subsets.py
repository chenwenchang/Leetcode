# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 00:27:02 2018

@author: Wenchang Chen
"""

def subsets(nums):
    if len(nums) == 1:
        return [[],[nums[0]]]
    else:
        tmp = nums.pop(0)
        res = subsets(nums)
        return [[tmp] + x for x in res] + res