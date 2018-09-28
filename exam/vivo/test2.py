# -*- coding: utf-8 -*-
#  @Time        :    2018/9/13 20:48
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory

def main():
    n = int(raw_input())
    result = ""
    while n > 0:
        result += str(n % 2)
        n = n / 2
    if not result:
        print "0"
    else:
        l = list(result)
        l.reverse()
        print("".join(l))


if __name__ == '__main__':
    main()
