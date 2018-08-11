# -*- coding: utf-8 -*-
#  @Time        :    2018/8/5 23:57
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    match.py
#  @Place       :    dormitory
'''
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
思路：一开始想着匹配问题可能得用栈来做，先找非通配符的字符，遇到通配符先压栈，等到非通配符匹配完了再看通配符；
后来想到可能递归更简单，证实了一下，确实如此，先看前两个字符，根据其匹配情况与后续匹配情况综合确定整体匹配情况，将问题简化，进而递归求解。
'''


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(pattern) == 0:
            return len(s) == 0
        if len(pattern) == 1:
            return len(s) == 1 and (s[0] == pattern[0] or pattern[0] == ".")
        if pattern[1] == '*':
            newPattern = pattern[2:]
            if pattern[0] == ".":
                # 只要s任意一个到末尾的子串匹配就匹配
                for i in range(len(s), -1, -1):
                    newS = s[i:]
                    if self.match(newS, newPattern):
                        return True
            else:
                # 要求s前面有0-x个pattern[0]
                # 先找出连续的pattern[0]的最右位置
                index = 0
                while 0 <= index < len(s) and s[index] == pattern[0]:
                    index += 1
                for i in range(index, -1, -1):
                    newS = s[i:]
                    if self.match(newS, newPattern):
                        return True
        else:
            if pattern[0] == ".":
                return self.match(s[1:], pattern[1:])
            else:
                return s[0] == pattern[0] and self.match(s[1:], pattern[1:])
        return False


def main():
    print(Solution().match("aaa", "a.a"))
    print(Solution().match("aaa", "ab*ac*a"))
    print(Solution().match("aaa", "aa.a"))
    print(Solution().match("aaa", "ab*a"))
    pass


if __name__ == '__main__':
    main()
