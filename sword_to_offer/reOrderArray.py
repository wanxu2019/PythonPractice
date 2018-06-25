# -*- coding: utf-8 -*-
#  @Time        :    2018/6/21 21:35
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    reOrderArray.py
#  @Place       :    dormitory
'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
思路：用两个数组分离再合并即可
'''


class Solution:
    def reOrderArray(self, array):
        # write code here
        result1 = []
        result2 = []
        for x in array:
            if x % 2 != 0:
                result1.append(x)
            else:
                result2.append(x)
        array = result1 + result2
        return array


def main():
    print(Solution().reOrderArray([1, 2, 2, 3, 4, 5, 6]))
    pass


if __name__ == '__main__':
    main()
