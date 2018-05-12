# -*- coding: utf-8 -*-
#  @Time        :    2018/4/17 20:10
#  @Author      :    Json Wan
#  @Description :    德才论
#  @File        :    pat_y_dcl.py
#  @Place       :    dormitory

import sys

line = sys.stdin.readline().strip()
values = map(int, line.split())
N, L, H = values[0], values[1], values[2]
array1 = []
array2 = []
array3 = []
array4 = []


def my_cmp(x, y):
    ret = cmp(y[1] + y[2], x[1] + x[2])
    if ret == 0:
        ret = cmp(y[1], x[1])
        if ret == 0:
            return cmp(x[0], y[0])
        else:
            return ret
    else:
        return ret


for i in range(N):
    line = sys.stdin.readline().strip()
    values = map(int, line.split())
    id, d, c = values[0], values[1], values[2]
    if d >= L and c >= L:
        if d >= H and c >= H:
            array1.append((id, d, c))
        elif d >= H:
            array2.append((id, d, c))
        elif d >= c:
            array3.append((id, d, c))
        else:
            array4.append((id, d, c))
array1.sort(my_cmp)
array2.sort(my_cmp)
array3.sort(my_cmp)
array4.sort(my_cmp)
print(len(array1) + len(array2) + len(array3) + len(array4))
array1 += array2 + array3 + array4
for x in array1:
    print x[0], x[1], x[2]
