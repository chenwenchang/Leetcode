# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 21:50:24 2018

@author: Wenchang Chen

There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

Example 1:
Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:
Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them. 
Note:

All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.

https://leetcode.com/problems/erect-the-fence/description/
"""

#def outerTrees(points):
points = [[1,2],[2,2],[4,2]]
pT = [p for p in zip(*points)]
xmin, xmax, ymin, ymax = min(pT[0]), max(pT[0]), min(pT[1]), max(pT[1])
left, right, up, down = [], [], [], []
for point in points:
    if point[0] == xmin:    left += [point]
    if point[0] == xmax:    right += [point]
    if point[1] == ymin:    down += [point]
    if point[1] == ymax:    up += [point]   
fence = []
fence += [x for x in left if x not in fence]
fence += [x for x in right if x not in fence]
fence += [x for x in up if x not in fence]
fence += [x for x in down if x not in fence]
print(fence)
leftmin, leftmax, rightmin, rightmax = min(left), max(left), min(right), max(right)
upmin, upmax, downmin, downmax = min(up), max(up), min(down), max(down)

def outerpoints(point1, point2, flag, points):
    if len(points) == 0:
        return []
    online, upline, upmost = [], [], []
    k = (point2[1] - point1[1]) / (point2[0] - point1[0])
    zset = []
    for point in points:
        z = ((point[1] - point1[1]) - k * (point[0] - point1[0])) * flag
        zset += [z]
        if z == 0 and point != point1 and point != point2:
            online += [point]
        elif z > 0:
            upline += [point]
    zmax = max(zset)
    if zmax <= 0: return online
    for i in range(len(zset)):
        if zset[i] == zmax: upmost += [points[i]]
    return upmost + outerpoints(point1, min(upmost), flag, upline) + outerpoints(max(upmost), point2, flag, upline)

if upmin != leftmax:
    flag= 1
    fence += [x for x in outerpoints(leftmax, upmin, flag, points) if x not in fence]    

if upmax != rightmax:
    flag= 1
    fence += [x for x in outerpoints(upmax, rightmax, flag, points) if x not in fence]
    
if downmin != leftmin:
    flag = -1
    fence += [x for x in outerpoints(leftmin, downmin, flag, points) if x not in fence]
        
if downmax != rightmin:
    flag = -1
    fence += [x for x in outerpoints(downmax, rightmin, flag, points) if x not in fence]
print(fence)