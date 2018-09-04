# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:36
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    字串的连接最长路径查找.py
#  @Place       :    dormitory

while True:
    try:
        n = int(raw_input())
        arr=[]
        for i in range(n):
            arr.append(raw_input())
        arr.sort()
        for x in arr:
            print x
    except Exception,e:
        break