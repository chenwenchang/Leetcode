# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:03:11 2018

@author: Wenchang Chen
"""

word1 = 'prosperity'
word2 = 'properties'
l1, l2 = len(word1), len(word2)
M = []
M += [list(range(0, -l1-1, -1))] 
for i in range(1,l2+1):
    M += [[-i]]
for i in range(1, l2+1):
    for j in range(1, l1+1):
        M[i] += [max(M[i-1][j-1] + (word2[i-1] == word1[j-1]) - 1, M[i][j-1] - 1, M[i-1][j]-1)]

res = 0
col = l1
row = l2
while col != 0 and row != 0:
# =============================================================================
#     print(row,col)
#     print(res)
# =============================================================================
    if max(M[row-1][col-1], M[row][col-1],M[row-1][col]) == M[row-1][col-1]:
        if M[row-1][col-1] != M[row][col]:
            res += 1
        col = col -1
        row = row - 1
    elif max(M[row-1][col-1], M[row][col-1],M[row-1][col]) == M[row][col-1]:
        col = col - 1
        res += 1
    else:
        row = row - 1
        res += 1
res += col + row
print(res)
        
        
        