# -*- coding: utf-8 -*-
#  @Time        :    2018/9/19 21:00
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory
'''
小P在工作之余研究起了等差数列。这天，小P在会议室的白板上写下了一个等差数列之后，接到电话就离开了会议室打电话。不明真相的小Q紧接着进入了会议室，然而，小Q有一个非常糟糕的强迫症——他非常讨厌偶数。于是，他将白板上所有的偶数擦去，将每个偶数替换为除以二的结果。如果一遍操作之后，白板上仍有偶数，他就重复一遍操作，直到白板上的偶数都消失为止。小P打完电话，回到了会议室，发现了小Q的杰作。可是，之前的等差数列对于小P来说无比重要，现在他想知到在小Q操作之前他写下的等差数列是什么？如果有多种可能的答案，请输出首项最小的等差数列。

输入
第一行一个整数N（4<=N<=50)，表示小Q操作完之后白板上整数的数量。

之后N行每行一个奇数A[i]，依次表示小Q操作完之后白板上的数列。保证1<=A[i]<=1000
输出
N行每行一个整数，表示小P原本写下的等差数列。

样例输入
6
1
1
3
1
5
3
样例输出
1
2
3
4
5
6

Hint
等差数列也可能从大到小排列
'''


def main():
    n = int(raw_input())
    arr = []
    for i in range(n):
        arr.append(int(raw_input()))
    # 先找公差
    # 分离奇数列与偶数列
    start = -1
    result = []

    def isEqualDArr(arr):
        for i in range(1, len(arr) - 1):
            if 2 * arr[i] != arr[i - 1] + arr[i + 1]:
                return False
        return True

    def isSquare(n):
        if n==1:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n = n / 2
        return True

    # 偶数列
    even_arr = []
    # 奇数列
    odd_arr = []
    for i in range(len(arr)):
        if i % 2 == 0:
            even_arr.append(arr[i])
        else:
            odd_arr.append(arr[i])
    if isEqualDArr(even_arr):
        d = (even_arr[1] - even_arr[0]) / 2
        flag = False
        while not flag:
            flag=True
            for i in range(len(odd_arr)):
                temp=even_arr[i]+d
                if temp%odd_arr[i]!=0 or not isSquare(temp/odd_arr[i]):
                    flag = False
                    break
            if not flag:
                d = d * 2
                even_arr = map(lambda x: 2 * x, even_arr)
        for i in range(len(odd_arr)):
            result.append(even_arr[i])
            result.append(even_arr[i]+d)
        if len(even_arr) > len(odd_arr):
            result.append(even_arr[-1])
    elif isEqualDArr(odd_arr):
        d = (odd_arr[1] - odd_arr[0]) / 2
        flag = False
        while not flag:
            flag=True
            for i in range(len(even_arr)):
                if i < len(odd_arr):
                    temp = odd_arr[i] - d
                else:
                    temp = odd_arr[-1] + 2 * d
                if temp%even_arr[i]!=0 or not isSquare(temp/even_arr[i]):
                    flag = False
                    break
            if not flag:
                d = d * 2
                odd_arr = map(lambda x: 2 * x, odd_arr)
        for i in range(len(odd_arr)):
            result.append(odd_arr[i]-d)
            result.append(odd_arr[i])
        if len(even_arr) > len(odd_arr):
            result.append(odd_arr[-1]+d)
    for x in result:
        print x


if __name__ == '__main__':
    main()
