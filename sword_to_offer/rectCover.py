# -*- coding: utf-8 -*-
#  @Time        :    2018/6/21 20:50
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    rectCover.py
#  @Place       :    dormitory
'''
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
思路：转化为子问题递归求解
'''


class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 1:
            return number
        n1 = 1
        n2 = 2
        while number > 2:
            n1, n2 = n2, n1 + n2
            number -= 1
        return n2


def main():
    for i in range(10):
        print(Solution().rectCover(i))
    pass


if __name__ == '__main__':
    main()
