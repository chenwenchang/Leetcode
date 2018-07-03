# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 23:18:53 2018

@author: Wenchang Chen

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

https://leetcode.com/problems/triangle/description/
"""

def minimumTotal(triangle):
    res = [float('inf')] * len(triangle)
    for nums in triangle:
        if len(nums) == 1:
            res[0] = nums[0]

        else:
            for idx, num in enumerate(nums):
                print(res)
                if idx == len(nums) - 1:
                    res[idx] = num + tmp
                elif idx == 0:
                    tmp = res[0] * 1
                    res[0] = num + res[0]
                else:
                    tmp0 = res[idx] * 1
                    res[idx] = min(num + res[idx], tmp + num)
                    tmp = tmp0                   
    print(res)
    return min(res)

triangle = [[-1],[-2,-3]]
print(minimumTotal(triangle))