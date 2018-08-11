# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 7:34
# @Author  : Json Wan
# @Description : 
# @File    : StrToInt.py
'''
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
+2147483647
    1a33
输出
2147483647
    0
思路：
'''


class Solution:
    def isLegal(self, s):
        if not s:
            return False
        # 第一位字符的取值只能为+,-,0-9
        # 第二位及以后的字符取值只能为0-9
        import re
        pattern = re.compile(r"^[0-9+-]?[0-9]*$")
        if not pattern.match(s):
            return False
        return True

    def StrToInt(self, s):
        # write code here
        if not self.isLegal(s):
            return 0
        value = 0
        sign = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]
        for ch in s:
            value = value * 10 + ord(ch) - ord("0")
        return value * sign


def main():
    print(Solution().StrToInt("+2147483647"))
    print(Solution().StrToInt("-2147483647"))
    print(Solution().StrToInt("1a33"))
    print(Solution().StrToInt("133+"))
    pass


if __name__ == '__main__':
    main()
