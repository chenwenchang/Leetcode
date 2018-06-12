# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 19:40:13 2018

@author: Wenchang Chen
"""
"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
"""
https://leetcode.com/problems/decode-string/description/
"""
def decodeString(s):
    s_de = ''
    if not(s[0].isdigit()):
        ite = 1
        pos = 0
    else:
        pos = getNumPos(s)
        ite = int(s[0:pos])
        
    if s[pos].isalpha():
        j = getCharPos(s[pos:]) + pos
        s_de = s_de + s[pos:j]
        pos = j
        if pos != len(s):
            s_de = s_de + decodeString(s[pos:])
    elif s[pos] == '[':
        start = pos + 1
        pos2 = getRpPos(s[start:]) + start
        while ite > 0:
            s_de = s_de + decodeString(s[pos + 1 : pos2 + 1])
            ite = ite - 1
        if pos2+1 < len(s):
            s_de = s_de + decodeString(s[pos2+1:])
                
    return s_de    
            
            
def getNumPos(s):
    for i in range(len(s)):
        if not(s[i].isdigit()):
            return i
            break
    if i == len(s) - 1:
        return i+1
        
def getCharPos(s):
    for i in range(len(s)):
        if not(s[i].isalpha()):
            return i
            break
    if i == len(s) - 1:
        return i+1
    
def getRpPos(s):
    count = 0;
    for i in range(len(s)):
        if s[i] == '[':
            count = count + 1;
        if s[i] == ']' and count == 0:
            return i
        if s[i] == ']' and count != 0:
            count = count - 1
            
            
            
