# -*- coding: utf-8 -*-
#  @Time        :    2018/6/21 21:01
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    NumberOf1.py
#  @Place       :    dormitory
'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
思路：正数往右移同1比较，负数转化为正数计算，先找出右边0的个数处理，左边是与正数互补的
'''


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n >= 0:
            while n > 0:
                count += n & 1
                n >>= 1
        else:
            n = -n
            r = 0
            while n & 1 == 0:
                r += 1
                count += n & 1
                n >>= 1
            while n > 0:
                count += n & 1
                n >>= 1
            count = 32 - r - count + 1
        return count


def main():
    for i in range(-5, 5):
        print(Solution().NumberOf1(i))
    pass


if __name__ == '__main__':
    main()
