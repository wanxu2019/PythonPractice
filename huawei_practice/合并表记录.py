# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:11
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    合并表记录.py
#  @Place       :    dormitory

while True:
    try:
        n = int(raw_input())
        arr = []
        for i in range(n):
            arr.append(map(int, raw_input().split(" ")))
        arr.sort(lambda x, y: cmp(x[0], y[0]))
        last_key = arr[0][0]
        key = 0
        value = 0
        for k, v in arr:
            if k == last_key:
                key = k
                value += v
            else:
                print key,value
                last_key = k
                value=0
                key = k
                value += v
        print key, value
    except:
        break
