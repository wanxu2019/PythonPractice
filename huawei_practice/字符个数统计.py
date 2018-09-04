# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:27
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    字符个数统计.py
#  @Place       :    dormitory

while True:
    try:
        s = raw_input()
        count=0
        _set=set()
        for ch in s:
            # print("%s:%d"%(ch,ord(ch)))
            if 0<=ord(ch)<=127 and ch not in _set:
                count+=1
                _set.add(ch)
        print(count)
    except Exception,e:
        break