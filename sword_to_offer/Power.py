# -*- coding: utf-8 -*-
#  @Time        :    2018/6/21 21:28
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    Power.py
#  @Place       :    dormitory
'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
思路：注意细节就行
'''


class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        negative = False
        if exponent < 0:
            exponent = -exponent
            negative = True
        result = base
        while exponent > 1:
            result *= base
            exponent -= 1
        if negative:
            return 1. / result
        return result


def main():
    for i in range(-2, 2):
        print(Solution().Power(2, i))
    pass


if __name__ == '__main__':
    main()
