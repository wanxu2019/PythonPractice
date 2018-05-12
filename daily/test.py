# -*- coding: utf-8 -*-
#  @Time        :    2018/3/27 22:18
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test.py
#  @Place       :    dormitory


def solution1():
    n = 4
    step_a = 3
    step_b = 5
    sum_a = n * step_a
    sum_b = 0
    for i in range(n):
        sum_a -= step_a
        sum_b += step_b
        if sum_a <= sum_b:
            print(min(sum_b, sum_a + step_a))
            break


def solution2():
    n = 4
    a = 3
    b = 5
    t1 = max(int(float(b) / (a + b) * n) * a, int(float(a) / (a + b) * n + 1) * b)
    t2 = max(int(float(b) / (a + b) * n + 1) * a, int(float(a) / (a + b) * n) * b)
    print(min(t1, t2))


def main():
    solution2()
    pass


if __name__ == '__main__':
    main()
