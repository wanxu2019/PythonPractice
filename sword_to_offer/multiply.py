# -*- coding: utf-8 -*-
#  @Time        :    2018/8/7 6:56
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    multiply.py
#  @Place       :    dormitory
'''
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
思路：
最简单的思路，直接乘出来就可以了。
高级的思路：
乘法，乘法的本质是什么？如何从位运算体现？
位运算的思路是错的，想太复杂了；
该题精髓在于复用之前计算出的结果，去除重复计算：
B[i]=MUL(A,0,i-1)*MUL(A,i+1,n-1)
B[i-1]=MUL(A,0,i-2)*MUL(A,i,n-1)
left(B[i])=left(B[i-1])*A[i-1]
right(B[i-1])=right(B[i])*A[i]

'''


class Solution:
    def multiply1(self, A):
        # write code here
        if len(A) == 1:
            return [0]
        elif not A:
            return []
        B = []
        for i in range(len(A)):
            B.append(reduce(lambda x, y: x * y, A[:i] + A[i + 1:], 1))
        return B

    def multiply(self, A):
        # write code here
        if len(A) == 1:
            return [0]
        elif not A:
            return []
        B = [1]
        for i in range(1, len(A)):
            B.append(B[-1] * A[i - 1])
        print(B)
        temp = 1
        for i in range(len(A), 1, -1):
            temp *= A[i - 1]
            B[i - 2] *= temp
        return B


def main():
    print(Solution().multiply([1]))
    print(Solution().multiply1([1, 2, 3, 4, 5, 6]))
    print(Solution().multiply([1, 2, 3, 4, 5, 6]))
    pass


if __name__ == '__main__':
    main()
