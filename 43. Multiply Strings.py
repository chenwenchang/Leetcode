# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 23:19:55 2018

@author: Wenchang Chen

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

https://leetcode.com/problems/multiply-strings/description/
"""

def plus(num1, num2):
    plusNum = ''
    maxi = lambda x,y : x if x > y else y
    carry = 0
    for i in range(maxi(len(num1), len(num2))):
        if i < len(num1) and i < len(num2):
            numeric = int(num1[i]) + int(num2[i]) + carry
        elif i >= len(num1):
            numeric = int(num2[i]) + carry
        elif i >= len(num2):
            numeric = int(num1[i]) + carry
        plusNum =  plusNum + str(numeric % 10)
        carry = int(numeric / 10)
    if carry != 0:
        plusNum = plusNum + str(carry)
    return plusNum

def multiply(num1, num2):
    
# =============================================================================
#     if num1 == '0' or num2 == '0':
#         return '0'
#     result = ''
#     for i in range(len(num1)-1, -1, -1):
#         tmp = ''
#         carry = 0
#         for j in range(len(num2)-1, -1, -1):
#             numeric = int(num1[i]) * int(num2[j]) + carry
#             tmp =  tmp + str(numeric % 10)
#             carry= int(numeric / 10)  
#         if carry != 0:
#             tmp = tmp + str(carry)
#         result = plus(result, (len(num1)-1-i) * '0' + tmp)
#     return result[::-1]
# =============================================================================
    return str(int(num1) * int(num2))
