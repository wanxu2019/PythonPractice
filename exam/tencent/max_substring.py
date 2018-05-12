# coding:utf-8
'''
腾讯2017暑期实习生题目：
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？输出需要删除的字符个数。
思路：
提到回文串，自然要利用回文串的特点，想到将源字符串逆转后，“回文串”（不一定连续）相当于顺序没变求原字符串和其反串的最大公共子序列（不是子串，因为可以不连续）的长度（使用动态规划很容易求得），然后用原字符串的长度减去这个最大公共子串的长度就得到了最小编辑长度。
'''
import sys
import math

MAX = 1001


def show_matrix(matrix):
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            print "{} ".format(row[j]),
        print("\n")
    print("\n")


def max_len(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    max_matrix = [[0 for j in range(l2)] for i in range(l1)]
    # print(max_matrix)
    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    max_matrix[i][j] = 1
                else:
                    max_matrix[i][j] = max_matrix[i - 1][j - 1] + 1
            else:
                if i == 0:
                    left = 0
                else:
                    left = max_matrix[i - 1][j]
                if j == 0:
                    right = 0
                else:
                    right = max_matrix[i][j - 1]
                max_matrix[i][j] = max(left, right)
                # show_matrix(max_matrix)
    return max_matrix[l1-1][l2-1]


def main():
    line = sys.stdin.readline().strip()
    reverse_line = line[::-1]
    print(len(line) - max_len(line, reverse_line))


if __name__ == "__main__":
    main()
