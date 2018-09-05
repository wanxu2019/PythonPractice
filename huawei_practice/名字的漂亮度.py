# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 12:37
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    名字的漂亮度.py
#  @Place       :    dormitory


while True:
    try:
        N = int(raw_input())
        for i in range(N):
            name=raw_input()
            d=dict()
            for ch in name:
                if ch not in d.keys():
                    d[ch]=1
                else:
                    d[ch]+=1
            l=d.items()
            l.sort(lambda x,y:cmp(y[1],x[1]))
            rate=0
            for i in range(len(l)):
                rate+=l[i][1]*(26-i)
            print rate
    except Exception,e:
        break
