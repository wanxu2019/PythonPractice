# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 7:13
# @Author  : Json Wan
# @Description : 
# @File    : Sum_Solution.py
'''
题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
思路：
'''


class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def inner_sum(n):
            self.sum += n
            n -= 1
            return n > 0 and inner_sum(n)
        inner_sum(n)
        return self.sum


def main():
    print(Solution().Sum_Solution(10))
    pass


if __name__ == '__main__':
    main()
