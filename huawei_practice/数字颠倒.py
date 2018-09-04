# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:33
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    数字颠倒.py
#  @Place       :    dormitory

while True:
    try:
        s = raw_input()
        l=list(s)
        l.reverse()
        print("".join(l))
    except Exception,e:
        break