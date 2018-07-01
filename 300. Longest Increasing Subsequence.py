# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 13:25:50 2018

@author: Wenchang Chen
"""

def lengthOfLIS(nums):
    def getlength(nums, calbool):
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        lislength = []
        for idx, num in enumerate(nums):
            if calbool[idx] == 0: 
                continue
            print('nums', nums)
            print('idx', idx)
            print('num', num)
            print('cal' , calbool)
            print('----------------------')

            if idx == len(nums) - 1:
                continue
            nums2 = nums[idx+1:]
            lislength2 = [1] * len(nums2)
            flag = 0
            small = float('Inf')
            for idx2, num2 in enumerate(nums2):
                if num2 > num:
                    calbool[idx2+idx+1] = 0
                    if num2 < small:
                        small = num2
                        flag = 1
                        lislength2[idx2] += getlength(nums2[idx2:], [1] + [0] * (len(nums2[idx2:]) - 1))
                elif flag == 0 and sum(calbool) > 1:
                    calbool[idx2+idx+1] = 1
                    break
            lislength += [max(lislength2)]
            print(lislength)
            
        return max(lislength)
    
    return getlength(nums, [1]*len(nums))