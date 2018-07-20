# -*- coding: utf-8 -*-
#  @Time        :    2018/7/18 2:09
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    NumberOf1Between1AndN_Solution.py
#  @Place       :    dormitory
"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
思路：这种很难直接求解的问题一般都会用到递归，子问题的分解可通过求余数运算实现。
然后能用递归的操作一般都能用动规，用存储换时间就行
"""


class Solution:
    # 比较容易想到的递归方式
    def NumberOf1Between1AndN_Solution2(self, n):
        # write code here
        if n < 10:
            if n == 1:
                return 1
            else:
                return 0
        result = 0
        for i in range(1, n + 1):
            result += self.NumberOf1Between1AndN_Solution(
                i / 10) + self.NumberOf1Between1AndN_Solution(i % 10)
        return result

    # 动态规划
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        result = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(10, n + 1):
            result.append(result[i / 10] + result[i % 10])
        return sum(result[:n+1])


def main():
    print(Solution().NumberOf1Between1AndN_Solution(13))
    print(Solution().NumberOf1Between1AndN_Solution(23))
    print(Solution().NumberOf1Between1AndN_Solution(123))
    print(Solution().NumberOf1Between1AndN_Solution(1123))
    print(Solution().NumberOf1Between1AndN_Solution(11123))
    pass


if __name__ == '__main__':
    main()
