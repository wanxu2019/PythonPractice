# -*- coding: utf-8 -*-
#  @Time        :    2018/9/20 21:59
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    小米大礼包.py
#  @Place       :    dormitory
'''
题目描述
小米之家是成人糖果店。里面有很多便宜，好用，好玩的产品。中秋节快到了；小米之家想给米粉们准备一些固定金额大礼包。对于给定的一个金额，需要判断能不能用不同种产品（一种产品在礼包最多出现一次）组合出来的这个金额。聪明的你来帮帮米家的小伙伴吧。

输入
输入N（N是正整数，N<=200）
输入N个价格p（正整数，p<10000）用单空格分割
输入金额M（M是正整数，M<=100000）

输出
能组合出来输出 1
否则输出 0

样例输入
6
99 199 1999 10000 39 1499
10238

样例输出
1
'''


# A recursive solution for subset sum
def isSubsetSum(arr, n, sum):
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    # If last element is greater than
    # sum, then ignore it
    if arr[n - 1] > sum:
        return isSubsetSum(arr, n - 1, sum);
        # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])


def main():
    N = int(raw_input())
    gift_money = list(map(int, raw_input("").split()))
    # print(gift_money)
    M = int(raw_input())
    res = isSubsetSum(gift_money, N, M)
    if res:
        print(1)
    else:
        print(0)
    pass


if __name__ == '__main__':
    main()
