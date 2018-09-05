# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 12:16
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    蛇形矩阵.py
#  @Place       :    dormitory


while True:
    try:
        N = int(raw_input())
        start=1
        for i in range(N):
            start+=i
            step=i+1
            temp=start-step
            for j in range(N-i):
                temp+=step
                print  temp,
                step+=1
            print


    except Exception,e:
        break

