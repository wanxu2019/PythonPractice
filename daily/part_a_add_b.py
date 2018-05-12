# -*- coding: utf-8 -*-
#  @Time        :    2018/4/17 21:00
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    part_a_add_b.py
#  @Place       :    dormitory

import sys

values = sys.stdin.readline().strip().split()
A, DA, B, DB = values[0], values[1], values[2], values[3]
num_a = ""
num_b = ""
for i in range(len(A)):
    if DA == A[i]:
        num_a += DA
for i in range(len(B)):
    if DB == B[i]:
        num_b += DB
if num_a == "":
    num_a = "0"
if num_b == "":
    num_b = "0"
print int(num_a) + int(num_b)
