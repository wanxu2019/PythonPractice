# -*- coding: utf-8 -*-
#  @Time        :    2018/9/16 19:22
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory


# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    arr1 = map(int, raw_input().split())
    arr2 = map(int, raw_input().split())
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    n = 0
    while i < len(arr1) and j < len(arr2):
        if arr2[j] >= arr1[i]:
            i += 1
            j += 1
            n += 1
        else:
            j += 1
    print n
