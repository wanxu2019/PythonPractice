# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 7:18
# @Author  : Json Wan
# @Description : 
# @File    : Add.py
'''
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
思路：
两个数异或：相当于每一位相加，而不考虑进位；
两个数相与，并左移一位：相当于求得进位；
将上述两步的结果相加
'''


class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            sum = num1 ^ num2
            carray = (num1 & num2) << 1
            num1 = sum
            num2 = carray
        return num1


def main():
    print(Solution().Add(0, 0))
    print(Solution().Add(1, 1))
    print(Solution().Add(1, 2))
    print(Solution().Add(3, 5))
    print(Solution().Add(30000000, 50000000))
    pass


if __name__ == '__main__':
    main()
