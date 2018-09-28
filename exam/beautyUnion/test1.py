# -*- coding: utf-8 -*-
#  @Time        :    2018/9/27 19:31
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory


def main():
    x, y = map(int, raw_input().split())
    n = x + y
    x = min(x, y)
    result = 1
    m = 1
    while x > 0:
        result *= n
        m *= x
        x -= 1
        n -= 1
    print(result / m)


if __name__ == '__main__':
    main()
