# -*- coding: utf-8 -*-
#  @Time        :    2018/9/13 20:48
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory

def main():
    def is_prime(n):
        if n <= 1:
            return False
        else:
            import math
            for i in range(2, int(math.sqrt(n) + 1)):
                if n % i == 0:
                    return False
        return True

    n = int(raw_input())
    if is_prime(n):
        print "1"
    else:
        print "0"


if __name__ == '__main__':
    main()
