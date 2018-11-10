# -*- coding: utf-8 -*-
#  @Time        :    2018/11/10 7:51
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    Palindrome Partitioning II.py
#  @Place       :    dormitory
'''
题目描述
给定一个字符串 ss，请将它划分成若干部分，使得每一部分都是回文串。
求最少需要切几刀。

样例
输入："aab"
输出：1
解释：可以划分成：["aa","b"]，所以只用切1刀。
算法
(动态规划) O(n2)O(n2)
一共进行两次动态规划。

第一次动规：计算出每个子串是否是回文串。
状态表示：st[i][j]st[i][j] 表示 s[i…j]s[i…j] 是否是回文串;
转移方程：s[i…j]s[i…j] 是回文串当且仅当 s[i]s[i]等于s[j]s[j] 并且 s[i+1…j−1]s[i+1…j−1] 是回文串；
边界情况：如果s[i…j]s[i…j]的长度小于等于2，则st[i][j]=(s[i]==s[j])st[i][j]=(s[i]==s[j]);

在第一次动规的基础上，我们进行第二次动规。
状态表示：f[i]f[i] 表示把前 ii 个字符划分成回文串，最少划分成几部分；
状态转移：枚举最后一段回文串的起点 jj，然后利用 st[j][i]st[j][i] 可知 s[j…i]s[j…i] 是否是回文串，如果是回文串，则 f[i]f[i] 可以从 f[j−1]+1f[j−1]+1 转移；
边界情况：0个字符可以划分成0部分，所以 f[0]=0f[0]=0。

题目让我们求最少切几刀，所以答案是 f[n]−1f[n]−1。

时间复杂度分析：两次动规都是两重循环，所以时间复杂度是 O(n2)O(n2)。

作者：yxc
链接：https://www.acwing.com/solution/leetcode/content/227/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


def min_cut(s):
    n = len(s)
    # 先用n2时间建立整个串的所有子串的回文状态信息表
    st = [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, -1, -1):
            if i - j <= 1:
                st[j][i] = s[j] == s[i]
            else:
                st[j][i] = s[j] == s[i] and st[j + 1][i - 1]
    # 再次使用动规找最少次数
    # 求最少次数的过程中需要查阅回文状态信息表
    f = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        f[i] = 9999999999
        for j in range(i):
            if st[j][i - 1]:
                f[i] = min(f[i], f[j] + 1)
    return max(0, f[n] - 1)


def main():
    print(min_cut("aab"))
    print(min_cut("aaba"))
    print(min_cut("aabacdaafcacf"))
    print(min_cut("baabacaeava"))
    pass


if __name__ == '__main__':
    main()
