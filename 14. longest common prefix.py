# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:26:45 2018

@author: Wenchang Chen

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
def p(strs):
    strsLen = []
    for s in strs:
        strsLen += [len(s)]
    if strsLen == []:
        return ''
    common = ''
    for i in range(min(strsLen)):
        tmp = ''
        for s in strs:
            if tmp == '':
                tmp = s[i]
            else:
                if s[i] != tmp:
                    return common
        common += tmp
    return common

    