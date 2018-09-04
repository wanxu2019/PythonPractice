# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:21
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    提取不重复的整数.py
#  @Place       :    dormitory

while True:
    try:
        s = raw_input()
        result=list()
        for i in range(len(s)-1,-1,-1):
            if s[i] not in result:
                result.append(s[i])
        print("".join(result))
    except Exception,e:
        break