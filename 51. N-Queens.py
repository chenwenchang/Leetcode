# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:37:12 2018

@author: Wenchang Chen

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
def getPos(allnum, x, z1, z2, n, allpuzzle):
    if n == -1:
        s = '.' * len(x)
        puzzle = []
        puzzle += [s[0:xi] + 'Q' + s[xi+1:] for xi in x]
        allpuzzle += [puzzle]
    w1 = [n - z for z in z1]
    w2 = [z - n for z in z2]
    remain = list(set(allnum).difference(set(x + w1 + w2)))
    for c in remain:
        getPos(allnum, x + [c], z1 + [n-c], z2 + [n+c], n-1, allpuzzle)
        
def solveNQueens(n):
    choice = []
    for i in range(n):
        choice += [i]
    allpuzzle = []
    getPos(choice, [],[],[],n-1, allpuzzle)
    return allpuzzle































