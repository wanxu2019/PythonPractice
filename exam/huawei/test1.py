# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 18:55
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory


while True:
    try:
        def convert_to_10(s):
            num = 0
            for ch in s:
                num = num * 26 + ord(ch) - ord('a')
            return num


        def convert_to_26(n):
            s = ""
            while n > 0:
                s = chr(ord('a') + n % 26) + s
                n = n / 26
            if len(s)==0:
                return "a"
            return s
        n1_26 = raw_input()
        n2_26=raw_input()
        # n1_10=convert_to_10(n1_26)
        # n2_10=convert_to_10(n2_26)
        # print(n1_10)
        # print(n2_10)
        # print(convert_to_26(0))
        # print(convert_to_26(25))
        print(convert_to_26(convert_to_10(n1_26)+convert_to_10(n2_26)))
    except Exception, e:
        break
