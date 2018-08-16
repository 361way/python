#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2018 www.361way.com site All rights reserved.
#   
#   Filename      ：01sum.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2018-08-16 14:33
#   Description   ：
# ===============================================================================
'''
nums = [2, 7, 11, 15]
target = 9
l = []
for x in nums:
  for y in nums:
      if (x + y) == target:
        #print x,y
        l.append(x)
        l.append(y)
print list(set(l))
'''

'''
nums = [3,2,4]
target = 6
n = range(len(nums))
l = []
for x in n:
  for y in n:
    # [3,3] 6
    #if nums[x] != nums[y]:
    if x != y:
      if nums[x] + nums[y] == target:
        print x,y
        l.append(x)
        l.append(y)
print list(set(l))
'''  

'''
# 超出内存限制
from itertools import combinations
nums = [2, 7, 11, 15]
l = [c for c in  combinations(nums, 2)]

n = [ x  for x in l if sum(x)==9]
m = [ x for x in range(len(nums)) if nums[x]==n[0][0] or nums[x]==n[0][1] ]
print m
'''
d = {}
nums = [3, 2, 4, 15]
#nums = [3, 3, 4, 15]
target = 6
for i in range(len(nums)):
  #y = target - nums[x]
  x = nums[i]
  if target-x in d:
     print d
     print [d[target-x],i]
  d[x] = i
