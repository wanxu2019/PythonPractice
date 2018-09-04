# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 22:37
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    字符串分隔.py
#  @Place       :    dormitory
from __future__ import print_function

def main():
    s1 = raw_input()
    s2 = raw_input()
    for s in [s1, s2]:
        if s:
            i = 0
            while i < len(s):
                print(s[i:i + 8],end="")
                if i + 8 > len(s):
                    print('0' * (i + 8 - len(s)))
                    break
                else:
                    print("")
                    i += 8
    pass


if __name__ == '__main__':
    main()
