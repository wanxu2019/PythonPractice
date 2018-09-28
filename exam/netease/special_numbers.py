# -*- coding: utf-8 -*-
#  @Time        :    2018/3/28 0:25
#  @Author      :    Json Wan
#  @Description :    网易2018实习生笔试题目2   not ok
#                    0=<x<=n,0=<y<=n,求x mod y >=k 的(x,y)组合数量
#  @File        :    special_numbers.py
#  @Place       :    dormitory
import sys


def main():
    print("输入n与k：")
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = map(int, line.split())
    n, k = values[0], values[1]
    ans = 0
    for x in range(k, n + 1):
        for y in range(k, n + 1):
            if x % y >= k:
                print((x, y))
                ans += 1
    print("一共{0}组".format(ans))


if __name__ == '__main__':
    main()
