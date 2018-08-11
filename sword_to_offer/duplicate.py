# -*- coding: utf-8 -*-
#  @Time        :    2018/8/6 0:44
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    duplicate.py
#  @Place       :    dormitory
'''
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
思路1：
最简单的想法是利用哈希，直接建立一个set帮助判断即可；
这里可以注意一下，能用set的地方就不要用list，二者性能差距非常大；
思路2：
应该要用位运算，属于新的一类题目吧，先学习一波。
利用数字的范围0-n，用数组本身来记录次数，属于通过模运算将一个数拆分为多个数，表示多种信息的情况，适用于数据有上限的情况。
'''


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        l = len(numbers)
        for num in numbers:
            index = num
            if index >= l:
                index -= l
            if numbers[index] >= l:
                duplication[0] = index
                return True
            else:
                numbers[index] += l
        return False

    def duplicate1(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        s = set()
        for num in numbers:
            if num in s:
                duplication[0] = num
                return True
            else:
                s.add(num)
        return False


def main():
    pass


if __name__ == '__main__':
    main()
