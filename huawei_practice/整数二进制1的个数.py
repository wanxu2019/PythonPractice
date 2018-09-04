# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:38
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    整数二进制1的个数.py
#  @Place       :    dormitory

while True:
    try:
        n = int(raw_input())
        count=0
        while n>0:
            if n%2!=0:
                count+=1
            n=n/2
        print count
    except Exception,e:
        break