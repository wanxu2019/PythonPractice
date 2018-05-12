# -*- coding: utf-8 -*-
#  @Time        :    2018/4/20 20:15
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    gcd.py
#  @Place       :    dormitory
# 编程题 | 30.0分1/2
# 经典的gcd
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 给你A数组，询问ΣΣA[gcd(i,j)],1<=i<=n,1<=j<=m
#
# 输入
# 每行有四个整数，N,n,m,p,其中N表示A数组长度,n,m,p为参数;对于A数组如下得出：
#
# A[1]=p,A[x]=(A[x-1]+153)%p
#
# 数据范围
#
# 小数据 n,m<=N<=1000,p<=1000
#
# 大数据 n,m<=N<=100000,p<=100000
import sys


def gcd(i, j):
    while j:
        i, j = j, i % j
    return i


line = sys.stdin.readline().strip()
# 把每一行的数字分隔后转化成int列表
N, n, m, p = map(int, line.split())
A = []
A.append(p)


def getA(n):
    if len(A) < n:
        for i in range(len(A) - 1, n):
            A.append((A[i] + 153) % p)
    return A


result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        index = gcd(i, j) - 1
        result += getA(index + 1)[index]
print(result)
