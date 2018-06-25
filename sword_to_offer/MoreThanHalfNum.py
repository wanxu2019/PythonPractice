# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 1:51
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    MoreThanHalfNum.py
#  @Place       :    dormitory
'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
思路：使用hash记录出现过的数字次数。
最佳思路：超过一半说明占绝大多数，比其他所有数字加起来还多，那么一个抵消一个之后还有剩余，因此可以不断抵消直到最后留下的一定是最多的那个数字，但是需要后续检验是否真的是大于一半数量。
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        l = len(numbers) / 2
        d = {}
        for x in numbers:
            if x in d.keys():
                d[x] += 1
            else:
                d[x] = 1
            if d[x] > l:
                return x
        return 0


def main():
    print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
    pass


if __name__ == '__main__':
    main()
