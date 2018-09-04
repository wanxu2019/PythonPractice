# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:35
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    句子逆序.py
#  @Place       :    dormitory

while True:
    try:
        s = raw_input()
        l=s.split(" ")
        l.reverse()
        print("".join(l))
    except Exception,e:
        break