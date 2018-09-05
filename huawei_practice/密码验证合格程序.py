# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 11:15
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    密码验证合格程序.py
#  @Place       :    dormitory


def is_ok(s):
    if len(s)<=8:
        return False
    hasUpperCh=0
    hasLowerCh=0
    hasNum=0
    hasOther=0
    for ch in s:
        if 'A'<=ch<='Z':
            hasUpperCh=1
        elif 'a'<=ch<='z':
            hasLowerCh=1
        elif '0'<=ch<='9':
            hasNum=1
        else:
            hasOther=1
    if hasUpperCh+hasLowerCh+hasNum+hasOther>=3:
        for i in range(len(s)-3):
            for j in range(i+3,len(s)):
                if s[i:i+3]==s[j:j+3]:
                    return False
        return True
    return False

while True:
    try:
        s = raw_input()
        if is_ok(s):
            print "OK"
        else:
            print "NG"
    except Exception,e:
        break
