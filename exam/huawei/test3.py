# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 18:55
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test3.py
#  @Place       :    dormitory

import re

pattern = re.compile("([a-z]+[0-9]+)")
while True:
    try:
        s = raw_input()
        arr = pattern.findall(s)
        print arr


        def get_string_num(s):
            i = -1
            while '0' <= s[i] <= '9':
                i -= 1
            return s[:i + 1], int(s[i + 1:])


        def custom_cmp(x, y):
            x, x_num = get_string_num(x)
            y, y_num = get_string_num(y)
            if x_num == y_num:
                return cmp(x, y)
            else:
                return cmp(x_num, y_num)


        arr.sort(custom_cmp)
        # print arr
        result = ""
        for x in arr:
            x, x_num = get_string_num(x)
            result += x * x_num
        print result

    except Exception, e:
        break
