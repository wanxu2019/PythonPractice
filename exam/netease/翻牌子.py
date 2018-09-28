# -*- coding: utf-8 -*-
#  @Time        :    2018/9/8 20:12
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    翻牌子.py
#  @Place       :    dormitory
'''
给定一个N*M的矩阵，在矩阵中每一块有一块牌子，假定刚开始的时候所有牌面向上。
现在对于每个块进行如下操作：
>翻转某个块中的牌子，并且与之相邻的其余八张牌也会翻转；
XXX
XXX
XXX
如上矩阵所示，翻转中间那块时，这九块都翻转一次。请输出在对矩阵中每一块进行如上操作后，牌面向下的个数。
输入描述：
第一行为测试用例数t，（1<=t<=100000）
接下来t行，每行2个整数N,M(1<=N,M<=1,000,000,000)
输出牌面向下的块的个数。
示例：
输入：
5
1 1
1 2
3 1
4 1
2 2
输出：
1
0
1
2
0
思路：
关注点应该转移，不应该从翻的那张牌入手去考察周围的，而应该整体思考，看每张牌被翻了几次，也就是周围有几个牌。
'''


def main():
    N = int(raw_input())
    test_data = []
    for i in range(N):
        test_data.append(map(int, raw_input().strip().split()))

    def solve(n, m):
        if n == 1:
            if m == 1:
                return 1
            return max(0, m - 2)
        else:
            if m == 1:
                return max(0, n - 2)
            else:
                # 4个角都是被翻了4次
                # 4条边都是被翻了6次
                # 中间的都是被翻了9次
                return (n - 2) * (m - 2)

    for data in test_data:
        print(solve(data[0], data[1]))


if __name__ == '__main__':
    main()
