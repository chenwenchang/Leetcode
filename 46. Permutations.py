# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 01:48:32 2018

@author: Wenchang Chen
"""

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def getP(nums, n, oneres, res):
        if n == 0:
            res += [oneres]
            return 
        else: 
            for idx,num in enumerate(nums):
                getP(nums[0:idx] + nums[idx+1:], n-1, oneres + [num], res)
    res = []
    n = len(nums)
    getP(nums, n, [], res)
    return res