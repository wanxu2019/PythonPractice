# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 18:55
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory


while True:
    try:
        s1 = raw_input()
        s2 = raw_input()
        if len(s1) < 5 or len(s2) < 5 or len(s1) < len(s2):
            print "false"
        else:
            flag = True
            for ch in s1:
                if not "A" <= ch <= "Z":
                    flag = False
                    break
            if flag:
                for ch in s2:
                    if not "A" <= ch <= "Z":
                        flag = False
                        break
            if flag:
                for ch in s2:
                    if ch not in s1:
                        flag = False
                        break
            if flag:
                print "true"
            else:
                print "false"
                # elif set(s2).issubset(set(s1)):
                #     print "true"
                # else:
                #     print "false"
    except Exception, e:
        break