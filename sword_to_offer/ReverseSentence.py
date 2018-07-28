# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 6:23
# @Author  : Json Wan
# @Description : 
# @File    : ReverseSentence.py
"""
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
思路：在python里面还是太简单了
"""


class Solution:
    def ReverseSentence(self, s):
        # write code here
        arr = s.split(" ")

        def reverse(arr):
            result = []
            for i in range(len(arr)):
                result.append(arr[len(arr) - 1 - i])
            return result

        return " ".join(reverse(arr))


def main():
    print(Solution().ReverseSentence("student. a am I"))
    pass


if __name__ == '__main__':
    main()
