# -*- coding: utf-8 -*-
#  @Time        :    2018/4/20 20:38
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    countNum.py
#  @Place       :    dormitory

import sys
import math


def getLevel(num):
    level = 0
    while num != 0:
        level += 1
        num = num / 10
    return level


# print(getLevel(1))
# print(getLevel(10))
# print(getLevel(11))
# print(getLevel(110))


def getPrevious(n):
    result = 0
    while n > 0:
        result += n * int(math.pow(10, n - 1)) * 9
        n -= 1
    return result


# print(getPrevious(1))
# print(getPrevious(2))
# print(getPrevious(3))
T = int(sys.stdin.readline().strip())
nums = []
for i in range(T):
    nums.append(int(sys.stdin.readline().strip()))
for num in nums:
    level = getLevel(num)
    model = int(math.pow(10, level - 1))
    print(((num / model - 1) * model + num % model + 1) * level+getPrevious(level - 1))