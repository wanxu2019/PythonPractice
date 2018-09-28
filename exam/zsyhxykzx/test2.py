# -*- coding: utf-8 -*-
#  @Time        :    2018/9/16 19:27
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory


def main():
    n = int(raw_input())
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    print b


if __name__ == '__main__':
    main()
