# -*- coding: utf-8 -*-
#  @Time        :    2018/7/22 0:51
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    FirstNotRepeatingChar.py
#  @Place       :    dormitory
"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
思路：最容易想到的解法是遍历，双指针游走
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        length = len(s)
        if length == 1:
            return 0
        for i in range(length - 1):
            flag = True
            j = i + 1
            while flag and j < length:
                if s[j] == s[i]:
                    flag = False
                j += 1
            j = i - 1
            while flag and j >= 0:
                if s[j] == s[i]:
                    flag = False
                j -= 1
            if flag:
                return i
        return -1


def main():
    print(Solution().FirstNotRepeatingChar("gcabcdefg"))
    print(Solution().FirstNotRepeatingChar("gcabcdefag"))
    print(Solution().FirstNotRepeatingChar("google"))
    pass


if __name__ == '__main__':
    main()
