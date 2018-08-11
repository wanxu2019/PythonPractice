# -*- coding: utf-8 -*-
#  @Time        :    2018/8/11 10:34
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    isNumeric.py
#  @Place       :    dormitory
'''
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
思路：
常规题目，用正则匹配几条规则即可：
（1）整个字符串中只能出现[0-9]+-.e，有其他字符则不是；
（2）根据e将字符串分为两半，左边的必须为一个合理的数字，右边的必须为一个整数；
（3）整数：首位只能是+-[0-9]，后面只能是[0-9]
（4）数字：首位只能是+-[0-9].，若首位为+-，则后面为不带符号的数字
（5）不带符号的数字：以小数点为分隔，两边都必须为纯数字，且数字数量>=1
'''


class Solution:
    # 纯数字
    def isPureNumber(self, s):
        import re
        pattern = re.compile(r"^[0-9]*$")
        if pattern.match(s):
            return True
        return False

    # 不带符号的数字
    def isNumberWithoutSign(self, s):
        pointIndex = s.find(".")
        # 没有小数点
        if pointIndex == -1:
            return len(s) >= 1 and self.isPureNumber(s)
        else:
            return len(s) >= 2 and self.isPureNumber(s[:pointIndex]) and self.isPureNumber(s[pointIndex + 1:])

    # 数字
    def isNumber(self, s):
        if len(s) == 0:
            return False
        import re
        pattern = re.compile(r"^[+-.0-9]$")
        if not pattern.match(s[0]):
            return False
        else:
            if s[0] in ['+', '-']:
                return self.isNumberWithoutSign(s[1:])
            else:
                return self.isNumberWithoutSign(s)

    # 整数
    def isInteger(self, s):
        import re
        pattern = re.compile(r"^[+\-0-9][0-9]*$")
        if pattern.match(s):
            return True
        return False

    # s字符串
    def isNumeric(self, s):
        # write code here
        s=s.lower()
        eIndex = s.find("e")
        if eIndex == -1:
            return self.isNumber(s)
        else:
            return self.isNumber(s[:eIndex]) and self.isInteger(s[eIndex + 1:])


def main():
    # 正用例
    print(Solution().isNumeric("+100"))
    print(Solution().isNumeric("5e2"))
    print(Solution().isNumeric("-123"))
    print(Solution().isNumeric("3.1416"))
    print(Solution().isNumeric("-1E-16"))
    # 负用例
    print(Solution().isNumeric("12e"))
    print(Solution().isNumeric("1a3.14"))
    print(Solution().isNumeric("1.2.3"))
    print(Solution().isNumeric("+-5"))
    print(Solution().isNumeric("12e+4.3"))
    pass


if __name__ == '__main__':
    main()
