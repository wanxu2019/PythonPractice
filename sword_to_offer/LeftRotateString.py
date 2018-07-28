# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 6:19
# @Author  : Json Wan
# @Description : 
# @File    : LeftRotateString.py
'''
题目描述
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
思路：在python里面就太简单了，没啥好想的
'''


class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0:
            return ""
        n = n % len(s)
        return s[n:] + s[:n]


def main():
    print(Solution().LeftRotateString("abcXYZdef", 3))
    pass


if __name__ == '__main__':
    main()
