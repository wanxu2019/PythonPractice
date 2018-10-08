# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 19:00
# @Author  : Json Wan
# @Description : 
# @File    : exam1.py


def main():
    # a, b, k = map(int, raw_input().split())
    a, b, k = raw_input().split()

    def is_lucky(a, b, n):
        str_a = str(a)
        str_b = str(b)
        s = str(n)
        n_sum = 0
        for ch in s:
            if ch != str_a and ch != str_b:
                return False
            n_sum += int(ch)
        for ch in str(n_sum):
            if ch != str_a and ch != str_b:
                return False
        return True

    def gen_set(a, b, k):
        if k == 1:
            s = set()
            s.add(a)
            s.add(b)
            return s
        else:
            sub_set = gen_set(a, b, k - 1)
            s = set()
            for x in sub_set:
                new_x = a + x
                s.add(new_x)
                new_x = x + a
                s.add(new_x)
                new_x = b + x
                s.add(new_x)
                new_x = x + b
                s.add(new_x)
            return s
    count=0

    for x in gen_set(a,b,int(k)):
        if is_lucky(a,b,x):
            count+=1
    print count % 1000000007


if __name__ == '__main__':
    main()
